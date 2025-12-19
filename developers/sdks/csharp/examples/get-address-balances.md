# Get Address Balances

This example demonstrates how to fetch all token balances for a given address

```csharp
using Newtonsoft.Json;
using PhantasmaPhoenix.RPC;

public void GetAddressBalances()
{
	// Initialize PhantasmaAPI instance
	var api = new PhantasmaAPI("https://testnet.phantasma.info/rpc", null);

	// Address to query
	var address = "P2K...";

	// Request account information including all token balances
	var account = await api.GetAccountAsync(address);
	if (account == null)
	{
		Console.WriteLine("Account not found or empty response");
		return;
	}

	// Convert full account result to readable JSON for logging
	var json = JsonConvert.SerializeObject(account, Formatting.Indented);
	Console.WriteLine(json);
}
```
