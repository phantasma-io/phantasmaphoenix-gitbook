# Node RPC

Every Phantasma node serves the same RPC on one host, as JSON-RPC and as REST. The SDKs wrap it; this section describes it directly. [Quick Start](/developers/quick-start.md#connecting-to-the-chain-apis) lists the public nodes of each network.

{% content-ref url="methods.md" %}
[Methods](methods.md)
{% endcontent-ref %}

{% content-ref url="models.md" %}
[Models](models.md)
{% endcontent-ref %}

## Routes

| Route | Serves |
| --- | --- |
| `POST /rpc` | JSON-RPC 2.0. |
| `POST /rpc/v2` | JSON-RPC 2.0 with structured [property values](#property-values). |
| `GET /api/v1/<Method>` | REST. The parameters go in the query string. |
| `GET /api/v2/<Method>` | REST with structured property values. |
| `GET /swagger` | The interactive API reference of both versions. The node root `/` redirects to it. |
| `GET /health` | A health check of the node. |

The four data routes serve the same methods with the same parameters. They differ only in how they write property values.

## JSON-RPC Requests

```json
{"jsonrpc": "2.0", "method": "getAccountInfo", "params": ["P2KJC8TB6XyY9sr1s4GprPD2XjnnUggRq86pwsFZjUEqCXt"], "id": 1}
```

- `method` is the method name; case does not matter.
- `params` is a JSON array in the order of the method's parameter table. Trailing parameters that have a default can be left out. More values than parameters fail with `Invalid params`.
- A number can be a JSON number or a decimal string. A boolean is a JSON boolean. `addressType` is the name `Phantasma` or `Carbon`. An array parameter is a JSON array.
- The answer carries `result`, or `error` with a `code` and a `message`.

```json
{"jsonrpc": "2.0", "id": 1, "result": {"address": "P2KJC8TB6XyY9sr1s4GprPD2XjnnUggRq86pwsFZjUEqCXt", "name": "anonymous", "stake": {"amount": "0", "time": 0, "unclaimed": "0"}}}
```

## REST Requests

```text
GET /api/v1/GetAccountInfo?account=P2KJC8TB6XyY9sr1s4GprPD2XjnnUggRq86pwsFZjUEqCXt
```

A REST path is the method name; case does not matter. The parameters go in the query string under the names of the parameter table; an array parameter repeats its name, as in `?accounts=P2K...&accounts=P2K...`. The answer is the result object itself. An error answers with the body `{"Error": "<message>"}` and the HTTP status described under [Errors](#errors).

## Answers

- Field names are in camel case, as the [models](models.md) list them.
- A field whose value is null is left out.
- Enumerations are written by name, such as `Halt` for a transaction state.
- Amounts are integer strings in the smallest unit of their token. Convert them with the token's decimals: 8 for SOUL, 10 for KCAL.
- Hashes, scripts, and other binary data are hexadecimal strings.

### Property Values

Token metadata, series metadata, organization metadata, and NFT properties carry values decoded from chain storage. A scalar is a string: numbers are decimal strings and bytes are upper-case hexadecimal.

| Route | Struct or array value |
| --- | --- |
| `/rpc`, `/api/v1` | A JSON document packed into a string, such as `"[{\"div\":\"10000\"}]"`. |
| `/rpc/v2`, `/api/v2` | The JSON array or object itself. A value that the node cannot decode is null. |

## Errors

| JSON-RPC code | Meaning |
| --- | --- |
| `-32700` | The body is not a JSON-RPC request. |
| `-32601` | The method does not exist. |
| `-32602` | A parameter is missing, has the wrong type, or there are more values than parameters. |
| `-32603` | The node refused or failed the request; `message` says why, such as `Invalid chainInput value` or `Transaction not found`. |

The HTTP status of an error answer is 400 for a bad request and 500 or 503 when the node fails. A lookup that finds nothing, such as `Transaction not found`, answers with HTTP 200 and the error.

## Addresses And Chains

An address parameter takes a Phantasma address such as `P2KJC8TB6XyY9sr1s4GprPD2XjnnUggRq86pwsFZjUEqCXt`. Where a method has an `addressType` parameter, `Carbon` makes the same parameter take a 32-byte account key in 64 hexadecimal characters instead.

`checkAddressReservedByte`, `true` by default, refuses an address that fails the reserved-byte check. Keep it `true`.

The node serves one chain. A chain parameter, such as `chainInput` or `chainAddressOrName`, accepts only `main`; any other value answers `Invalid <parameter> value`.

## Pages

Most list methods read by cursor. Leave `cursor` empty for the first page, pass back the `cursor` of each answer for the next one, and keep the other parameters the same. The last page carries no `cursor`. A page holds 1 to 100 entries, 10 by default, and at most 50 when `extended` is `true`.

`getAuctions` and `getAddressTransactions` read by page number instead: `page` starts at 1, `pageSize` is 1 to 100, and the answer carries `total` and `totalPages`.

## Limits

- A node can limit the requests of each client per minute. A request over the limit answers HTTP 429.
- A node can issue API keys. A request with a key in the `X-Api-Key` header is served at the key's own limit. A node can also refuse every request without a known key, with HTTP 401 and the body `{"error":"API key required"}`.
- `getAccountInfos` takes at most 100 addresses.
- The NFT id lists of `getAccount`, `getAccounts`, and `getTokenBalance` hold at most 10,000 ids; `amount` carries the true count.

## Node Policies

A node operator can switch these off. The public mainnet nodes serve contract reads and fee estimates.

| Policy | Effect when it is off |
| --- | --- |
| Accepting transactions | `sendCarbonTransaction` and `sendRawTransaction` answer `This node is in readonly mode, cannot accept new transaction`. |
| Contract reads | `invokeRawScript` and `estimateTransaction` answer `Smart contract read RPC is disabled on this node.` |
| Contract writes | A script transaction may call only `gas.AllowGas`, `gas.SpendGas`, `Runtime.TransferTokens`, `Runtime.TransferToken`, `Runtime.TransferBalance`, `Runtime.BurnTokens`, `Runtime.BurnToken`, `stake.Stake`, `stake.Unstake`, `stake.Claim`, and `stake.MasterClaim`; any other script answers `Smart contract writes are disabled on this node.` Structured transactions are not affected. |

## Deprecated Methods

| Method | Use instead |
| --- | --- |
| `getAccount` | `getAccountInfo`, with `getAccountFungibleTokens` and `getAccountNFTs` for the balances. |
| `getAccounts` | `getAccountInfos`, with `getAccountFungibleTokens` and `getAccountNFTs` per address. |
| `getTokenData` | `getNFT`. |

`getChain`, `getChains`, `getNexus`, `getLeaderboard`, `getArchive`, `readArchive`, and `writeArchive` read and store nothing; they answer empty objects, an empty array, an empty string, or `false`.

## Related Pages

{% content-ref url="/developers/blockchain/chain/fees-and-gas.md" %}
[Fees And Gas](/developers/blockchain/chain/fees-and-gas.md)
{% endcontent-ref %}

{% content-ref url="/developers/sdks/README.md" %}
[SDKs](/developers/sdks/README.md)
{% endcontent-ref %}
