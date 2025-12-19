# Get Address Token Balance

This example demonstrates how to query specific token balance for a given address

```csharp
using Newtonsoft.Json;
using PhantasmaPhoenix.Core;
using PhantasmaPhoenix.RPC;

public void GetAddressTokenBalance()
{
	// Initialize PhantasmaAPI instance
	var api = new PhantasmaAPI("https://testnet.phantasma.info/rpc", null);

	// Address to check balance for
	var address = "P2K...";

	// Token symbol to query (e.g. SOUL, KCAL, NFT symbol)
	var symbol = "KCAL";

	// Query information about token by its symbol
	var token = await api.GetTokenAsync(symbol);
	if (token == null)
	{
		throw new Exception("Token not found");
	}

	// Log full token info (decimals, supply, flags, etc.)
	Console.WriteLine($"Token info: {JsonConvert.SerializeObject(token, Formatting.Indented)}");

	// Query token balance for a given address
	var balance = await api.GetTokenBalanceAsync(address, symbol, "main");
	if (balance == null)
	{
		Console.WriteLine("Balance not found");
		return;
	}

	// Check whether the token is fungible (e.g. SOUL, KCAL) or non-fungible (NFT)
	if (token.IsFungible())
	{
		// UnitConversion.ToDecimal() converts raw token amount into human-readable decimal format
		var human = UnitConversion.ToDecimal(balance.Amount, balance.Decimals);
		Console.WriteLine($"Fungible {symbol} amount for {address}: {human}");
	}
	else
	{
		Console.WriteLine($"NFT {symbol} count for {address}: {balance.Amount}");
	}
}
```
