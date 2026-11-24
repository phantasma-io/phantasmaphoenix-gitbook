---
title: "Get User Balances"
weight: 80
---

Balances are read through a cursor-paginated call. The node answers one page at
a time, and the cursor it returns drives the loop.

```ts
import { PhantasmaAPI } from "phantasma-sdk-ts/public";
import type { Balance } from "phantasma-sdk-ts/public";

const NETWORK_API_URL = "https://testnet.phantasma.info/rpc";
const NETWORK_PEER_URL = null; // peers URL for automatic RPC selection, or null
const NEXUS_NAME = "testnet"; // For mainnet use this "mainnet"

const api = new PhantasmaAPI(NETWORK_API_URL, NETWORK_PEER_URL, NEXUS_NAME);

/**
 * Reads every fungible balance of an address.
 * @param address Address of the account you want to read
 */
async function getUserBalances(address: string): Promise<Balance[]> {
  const balances: Balance[] = [];
  let cursor = "";
  for (;;) {
    const page = await api.getAccountFungibleTokens(address, "", 0n, 100, cursor);
    if (page.result) balances.push(...page.result);
    if (!page.cursor) return balances;
    cursor = page.cursor;
  }
}
```

`pageSize` accepts 1 to 100. The node rejects anything outside that range.

For the account name and the staking info, call `getAccountInfo(address)`. It
costs the same whatever the address holds.

> [!WARNING]
> `getAccount` returned the balances inline and is deprecated. Its response embeds
> every NFT id the address owns, and the node caps each `ids` list at 10000
> entries while `amount` keeps the true count, so the list is silently partial for
> a large holder.
