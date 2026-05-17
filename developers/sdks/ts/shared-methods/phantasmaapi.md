# PhantasmaAPI

{% hint style="info" %}
Use `PhantasmaAPI` to call RPC endpoints directly from Node or the browser.
{% endhint %}

## Constructor

`new PhantasmaAPI(rpcUrl, peersUrlJson, nexus)`

- `rpcUrl`: full RPC endpoint (for example `https://testnet.phantasma.info/rpc`).
- `peersUrlJson`: optional peers JSON for auto-selecting the fastest RPC.
- `nexus`: `"testnet"` or `"mainnet"`.

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

{% hint style="info" %}
If you do not want automatic RPC selection, pass `undefined` for `peersUrlJson`.
{% endhint %}

## Current RPC Shape Notes

For new code, use the chain-aware block helpers:

```ts
await api.getBlockTransactionCountByHash("main", blockHash);
await api.getTransactionByBlockHashAndIndex("main", blockHash, index);
```

The legacy overloads without `chainAddressOrName` still work and default to `"main"`:

```ts
await api.getBlockTransactionCountByHash(blockHash);
await api.getTransactionByBlockHashAndIndex(blockHash, index);
```

Carbon token and node metadata helpers are exposed through:

- `getTokenSeriesById(symbol, carbonTokenId, seriesId, carbonSeriesId)`
- `getVersion()`
- `getPhantasmaVmConfig(chainAddressOrName)`
