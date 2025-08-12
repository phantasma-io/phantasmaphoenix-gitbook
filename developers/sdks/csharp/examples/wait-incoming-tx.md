# Wait Incoming Tx (Read Blocks)

This example demonstrates how to monitor incoming transactions

```csharp
using PhantasmaPhoenix.Core;
using PhantasmaPhoenix.Cryptography;
using PhantasmaPhoenix.Protocol;
using PhantasmaPhoenix.RPC;

// In-memory cache mapping token symbol to its decimals
private static readonly Dictionary<string, uint> _tokenDecimals = new(StringComparer.OrdinalIgnoreCase);

public void WaitIncomingTx_ReadBlocks()
{
	// Initialize PhantasmaAPI instance
	var api = new PhantasmaAPI("https://testnet.phantasma.info/rpc");

	// Address to monitor
	var address = "P2K...";

	using var cts = new CancellationTokenSource();
	Console.CancelKeyPress += (_, e) => { e.Cancel = true; cts.Cancel(); };
	await WaitIncomingTransfers(api, address, null, "main", cts.Token);
}

public static async Task WaitIncomingTransfers(PhantasmaAPI api, string address, string chain, CancellationToken ct)
{
	if (string.IsNullOrWhiteSpace(address))
	{
		throw new ArgumentException("Empty address provided");
	}
	if (string.IsNullOrWhiteSpace(chain))
	{
		throw new ArgumentException("Empty chain provided");
	}

	// Initialize from current chain height
	// Current block height will be our starting point for monitoring
	long height = await api.GetBlockHeightAsync(chain);
	Console.WriteLine($"[Init] Starting monitoring from block #{height}");

	// Continuous block scanning loop
	while (!ct.IsCancellationRequested)
	{
		try
		{
			// Fetch block data for the current height
			var block = await api.GetBlockByHeightAsync(chain, height);
			if (block?.Txs != null)
			{
				foreach (var tx in block.Txs)
				{
					// Only process successful transactions
					if (tx.State != ExecutionState.Halt)
					{
						continue;
					}

					// Empty tx, should not happen
					if (tx.Events == null)
					{
						continue;
					}

					foreach (var e in tx.Events)
					{
						if (!Enum.TryParse<EventKind>(e.Kind, true, out var kind))
						{
							Console.WriteLine($"[Error] Unsupported event kind '{e.Kind}'");
							continue;
						}

						if (kind != EventKind.TokenReceive)
						{
							// In this example we only log token receive events
							continue;
						}

						if (!string.Equals(e.Address, address, StringComparison.OrdinalIgnoreCase))
						{
							// We only monitor events for provided address
							continue;
						}

						// Decode and unserialize TokenEventData from event payload
						var dataBytes = Base16.Decode(e.Data);
						var data = Serialization.Unserialize<TokenEventData>(dataBytes);

						// Get decimals from cache or fetch from API
						uint decimals = await GetDecimalsAsync(api, data.Symbol);

						// Convert chain amount to human-readable format
						var decimalAmount = UnitConversion.ToDecimal(data.Value, decimals);

						Console.WriteLine($"Address {e.Address} received {decimalAmount} {data.Symbol} (tx: {tx.Hash})");
					}
				}
			}

			// Wait until a new block is produced (or loop is cancelled)
			while (!ct.IsCancellationRequested)
			{
				// Fetch latest block height again
				var newHeight = await api.GetBlockHeightAsync(chain);

				// If chain height increased, move to next block
				if (newHeight > height)
				{
					height += 1;
					break;
				}

				// Delay before re-checking block height - sleep for 1 second
				await Task.Delay(1000, ct);
			}
		}
		catch (OperationCanceledException)
		{
			// graceful exit
			break;
		}
		catch (Exception ex)
		{
			Console.WriteLine($"Error: {ex.Message}");
			await Task.Delay(1000, ct);
		}
	}

	Console.WriteLine("Stopped");
}

// Gets decimals for token from cache or requests it from chain and stores it in the cache
private static async Task<uint> GetDecimalsAsync(PhantasmaAPI api, string symbol)
{
	// Checking cache first
	if (_tokenDecimals.TryGetValue(symbol, out var d))
	{
		return d;
	}

	// Not found in cache, querying from the chain
	var tok = await api.GetTokenAsync(symbol);
	d = tok?.Decimals ?? 0;

	// Storing in cache
	_tokenDecimals[symbol] = d;

	return d;
}
```
