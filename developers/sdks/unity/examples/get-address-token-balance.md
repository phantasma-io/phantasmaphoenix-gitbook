# Get Address Token Balance

This example demonstrates how to query specific token balance for a given address

```csharp
public void GetAddressTokenBalance()
{
    // Initialize PhantasmaAPI instance
    var api = new PhantasmaAPI("https://testnet.phantasma.info/rpc");

    // Address to check balance for
    var address = "P2K...";

    // Token symbol to query (e.g. SOUL, KCAL, NFT symbol)
    var symbol = "KCAL";

    StartCoroutine(api.GetToken(symbol,
        // Callback on success
        (tokenResult) =>
        {
            StartCoroutine(api.GetTokenBalance(address, symbol, "main",
                // Callback on success
                (tokenBalanceResult) =>
                {
                    // Check whether the token is fungible (e.g. SOUL, KCAL) or non-fungible (NFT)
                    if (tokenResult.IsFungible())
                    {
                        // UnitConversion.ToDecimal() converts raw token amount into human-readable decimal format
                        Debug.Log($"[Balance] Fungible {symbol} amount for {address}: {UnitConversion.ToDecimal(tokenBalanceResult.Amount, tokenBalanceResult.Decimals)}");
                    }
                    else
                    {
                        Debug.Log($"[Balance] NFT {symbol} count for {address}: {tokenBalanceResult.Amount}");
                    }
                },
                // Callback for RPC errors (invalid token, network error, etc.)
                (errorCode, errorMessage) =>
                {
                    Debug.LogError($"[Error][{errorCode}] {errorMessage}");
                }
            ));
        },
        // Callback for RPC errors (invalid token, network error, etc.)
        (errorCode, errorMessage) =>
        {
            Debug.LogError($"[Error][{errorCode}] {errorMessage}");
        }
    ));
}
```
