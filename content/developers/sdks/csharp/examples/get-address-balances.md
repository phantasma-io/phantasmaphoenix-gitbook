---
title: "Get Address Balances"
weight: 40
---

This example demonstrates how to fetch all token balances for a given address.
Balances are read through a cursor-paginated call. The node answers one page at
a time, and the cursor it returns drives the loop.

```csharp
using PhantasmaPhoenix.RPC;
using PhantasmaPhoenix.RPC.Models;

public static async Task GetAddressBalances()
{
	// Initialize PhantasmaAPI instance
	using var api = new PhantasmaAPI("https://testnet.phantasma.info/rpc");

	// Address to query
	var address = "P2K...";

	var balances = new List<BalanceResult>();
	var cursor = "";
	while (true)
	{
		var page = await api.GetAccountFungibleTokensAsync(address, pageSize: 100, cursor: cursor);
		if (page?.Result != null) balances.AddRange(page.Result);
		if (page == null || string.IsNullOrEmpty(page.Cursor)) break;
		cursor = page.Cursor;
	}

	foreach (var balance in balances)
	{
		Console.WriteLine($"{balance.Symbol}: {balance.Amount}");
	}
}
```

`pageSize` accepts 1 to 100. The node rejects anything outside that range.

For the account name and the staking info, call `GetAccountInfoAsync(address)`.
Its cost does not depend on how much the address holds.

> [!WARNING]
> `GetAccountAsync` returned the balances inline and is deprecated. Its response
> embeds every NFT id the address owns, and the node caps each `Balances[].Ids`
> list at 10000 entries while `Balances[].Amount` keeps the true count, so the
> list is silently partial for a large holder.
