# Wait Incoming Tx (Read Blocks)

This example demonstrates how to monitor incoming transactions

```csharp
// In-memory cache mapping token symbol to its decimals
private readonly Dictionary<string, uint> _tokenDecimals = new(StringComparer.OrdinalIgnoreCase);

public void WaitIncomingTx_ReadBlocks()
{
    // Initialize PhantasmaAPI instance
    var api = new PhantasmaAPI("https://testnet.phantasma.info/rpc");

    // Address to monitor
    var address = "P2K...";

    StartCoroutine(WaitIncomingTransfers(api, address));
}

// Coroutine that scans blocks by height and processes TokenReceive events for the specified address
private IEnumerator WaitIncomingTransfers(PhantasmaAPI api, string address)
{
    const string chain = "main";

    long height = -1;
    bool gotHeight = false;

    // --- Step 1: Initialize starting block height ---
    while (!gotHeight)
    {
        // Fetch latest block height for the chain
        yield return api.GetBlockHeight(chain,
            h => { height = h; gotHeight = true; },
            // Callback for RPC errors (network issue, chain not found, etc.)
            (code, msg) => { Debug.LogError($"[Error][{code}] GetBlockHeight failed: {msg}"); });

        if (!gotHeight)
            yield return new WaitForSeconds(1f); // Retry delay before trying again
    }

    Debug.Log($"[Init] Starting from block #{height}");

    // --- Step 2: Continuous block scanning loop ---
    while (true)
    {
        // Fetch block data for the current height
        BlockResult block = null;
        yield return api.GetBlockByHeight(chain, height,
            b => block = b,
            // Callback for RPC errors (invalid height, network error, etc.)
            (code, msg) => Debug.LogError($"[Error][{code}] GetBlockByHeight({height}) failed: {msg}"));

        if (block?.Txs != null)
        {
            foreach (var tx in block.Txs)
            {
                // Only process successful transactions
                if (tx.State != ExecutionState.Halt)
                    continue;

                if (tx.Events == null) continue;

                foreach (var e in tx.Events)
                {
                    // Expect TokenReceive for the monitored address
                    var eventKind = Enum.Parse<EventKind>(e.Kind);
                    if (eventKind != EventKind.TokenReceive || !string.Equals(e.Address, address, StringComparison.OrdinalIgnoreCase))
                        continue;

                    // Decode TokenEventData from event payload
                    var dataBytes = Base16.Decode(e.Data);
                    var data = Serialization.Unserialize<TokenEventData>(dataBytes);

                    // Get decimals from cache or fetch from API
                    uint decimals;
                    if (!_tokenDecimals.TryGetValue(data.Symbol, out decimals))
                    {
                        bool fetched = false;
                        yield return api.GetToken(data.Symbol,
                            t =>
                            {
                                decimals = t.Decimals;
                                _tokenDecimals[data.Symbol] = decimals; // cache for reuse
                                fetched = true;
                            },
                            // Callback for RPC errors (invalid token, network error, etc.)
                            (code, msg) =>
                            {
                                Debug.LogError($"[Error][{code}] GetToken({data.Symbol}) failed: {msg}");
                                decimals = 0; // fallback to 0 to continue
                                fetched = true;
                            });
                        while (!fetched) yield return null;
                    }

                    // Convert chain amount to human-readable format
                    var human = UnitConversion.ToDecimal(data.Value, decimals);

                    Debug.Log($"Address {e.Address} received {human} {data.Symbol}");
                }
            }
        }

        // --- Step 3: Wait until a new block is produced ---
        while (true)
        {
            long newHeight = height;
            bool got = false;

            // Fetch latest block height again
            yield return api.GetBlockHeight(chain,
                h => { newHeight = h; got = true; },
                // Callback for RPC errors (network issue, etc.)
                (code, msg) => { Debug.LogError($"[Error][{code}] GetBlockHeight wait failed: {msg}"); got = true; });

            // If chain height increased, move to next block
            if (got && newHeight > height)
            {
                height += 1;
                break;
            }

            // Delay before re-checking block height
            yield return new WaitForSeconds(1f);
        }
    }
}
```
