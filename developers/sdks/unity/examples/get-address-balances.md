# Get Address Balances

This example demonstrates how to fetch all token balances for a given address

```csharp
public void GetAddressBalances()
{
    // Initialize PhantasmaAPI instance
    var api = new PhantasmaAPI("https://testnet.phantasma.info/rpc");

    // Address to query
    var address = "P2K...";

    // Request account information including all token balances
    StartCoroutine(api.GetAccount(address, (accountResult) =>
        {
           // Convert full account result to readable JSON for logging
           var json = JsonConvert.SerializeObject(accountResult, Formatting.Indented);

           // Output all token balances including NFTs and fungible tokens
           Debug.Log($"[Balance] balances for {address}: {json}");
        },
        (errorCode, errorMessage) =>
        {
            Debug.LogError($"[Error][{errorCode}] {errorMessage}");
        }
    ));
}
```
