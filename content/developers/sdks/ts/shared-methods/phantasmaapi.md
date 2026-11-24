---
title: "PhantasmaAPI"
linkTitle: "Phantasma API"
weight: 80
---

> [!NOTE]
> Use `PhantasmaAPI` to call RPC endpoints directly from Node or the browser.

## Constructor

`new PhantasmaAPI(rpcUrl, peersUrlJson, nexus, options?)`

- `rpcUrl`: full RPC endpoint (for example `https://testnet.phantasma.info/rpc`).
- `peersUrlJson`: optional peers JSON for auto-selecting the fastest RPC. Pass
  `null` when you do not want it.
- `nexus`: `"testnet"` or `"mainnet"`.
- `options.apiKey`: sent as the `X-Api-Key` header on every request.
- `options.maxRpcResponseBytes`: the largest accepted response body. It defaults
  to 16 MiB.

## Testnet Example

```ts
import { PhantasmaAPI } from "phantasma-sdk-ts/public";

const rpcUrl = "https://testnet.phantasma.info/rpc";
const peersUrl = "https://peers.phantasma.info/testnet-getpeers.json";
const api = new PhantasmaAPI(rpcUrl, peersUrl, "testnet");
```

## Mainnet Example

```ts
import { PhantasmaAPI } from "phantasma-sdk-ts/public";

const rpcUrl = "https://pharpc1.phantasma.info/rpc";
const peersUrl = "https://peers.phantasma.info/mainnet-getpeers.json";
const api = new PhantasmaAPI(rpcUrl, peersUrl, "mainnet");
```

> [!NOTE]
> If you do not want automatic RPC selection, pass `null` for `peersUrlJson`.

## Current RPC Shape Notes

The block helpers take the chain as their first argument:

```ts
await api.getBlockTransactionCountByHash("main", blockHash);
await api.getTransactionByBlockHashAndIndex("main", blockHash, index);
```

Read an account through `getAccountInfo`, and its holdings through the
cursor-paginated account methods. `getAccount` and `getAccounts` are deprecated,
because their response grows with the size of the account.

```ts
const info = await api.getAccountInfo(address);
const balances = await api.getAccountFungibleTokens(address);
```

Carbon token and node metadata helpers are exposed through:

- `getTokenSeriesById(symbol, carbonTokenId, seriesId, carbonSeriesId)`
- `getVersion()`
- `getPhantasmaVmConfig(chainAddressOrName)`

The client also carries the fee planner and the one-step send:

- `api.fees.plan(msg)`
- `api.sendTransaction(msg, signers)`

- [Fees And Broadcasting](../fees-and-broadcasting.md)
