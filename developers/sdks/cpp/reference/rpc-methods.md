# C++ SDK RPC Client

`PhantasmaAPI.h` is generated and exposes both low-level JSON helpers and a
high-level adapter-backed facade.

## Construction

| API | Purpose |
| --- | ------- |
| `PhantasmaAPI(httpClient)` | High-level facade. Requires `PHANTASMA_HTTPCLIENT` from an adapter. |
| `PhantasmaJsonAPI::Uri()` | Returns the RPC URI used by the JSON API layer. |
| `PhantasmaJsonAPI::Make...Request(builder, ...)` | Writes a JSON-RPC request. |
| `PhantasmaJsonAPI::Parse...Response(json, out, err)` | Parses a node response into a typed result. |

High-level methods return default-constructed values when a parse or RPC
failure occurs. Pass a `PhantasmaError*` and check it before using the returned
value. Low-level `Parse...Response` helpers use the same error channel.

## Method Groups

| Group | High-level methods |
| ----- | ------------------ |
| Accounts | `GetAccount`, `GetAccounts`, `LookUpName`, `GetAddressTransactions`, `GetAddressTransactionCount` |
| Blocks | `GetBlockHeight`, `GetBlockByHash`, `GetBlockByHeight`, `GetLatestBlock`, `GetBlockTransactionCountByHash` |
| Transactions | `GetTransaction`, `GetTransactionByBlockHashAndIndex`, `SendRawTransaction`, `SendCarbonTransaction`, `InvokeRawScript` |
| Chain metadata | `GetChains`, `GetChain`, `GetNexus`, `GetVersion`, `GetPhantasmaVmConfig` |
| Contracts | `GetContracts`, `GetContract`, `GetContractByAddress` |
| Organizations and leaderboards | `GetOrganization`, `GetOrganizationByName`, `GetOrganizations`, `GetLeaderboard` |
| Tokens | `GetTokens`, `GetToken`, `GetTokenSeries`, `GetTokenSeriesById`, `GetTokenNFTs`, `GetTokenData`, `GetTokenBalance` |
| Account token inventory | `GetAccountFungibleTokens`, `GetAccountNFTs`, `GetAccountOwnedTokens`, `GetAccountOwnedTokenSeries` |
| NFT and marketplace | `GetNFT`, `GetNFTs`, `GetAuctionsCount`, `GetAuctions`, `GetAuction` |
| Archive | `GetArchive`, `WriteArchive`, `ReadArchive` |

## Chain-Aware Overloads

Legacy overloads for `GetBlockTransactionCountByHash(blockHash, err)` and
`GetTransactionByBlockHashAndIndex(blockHash, index, err)` default to `"main"`.
For new code, prefer overloads that pass `chainAddressOrName` explicitly.

## Cursor Parameters

Carbon inventory methods use `pageSize` and `cursor` where the node returns
`CursorPaginatedResult<T>`. Keep passing the returned cursor until it is empty.

## Broadcast Methods

`SendRawTransaction` expects signed classic VM transaction hex.
`SendCarbonTransaction` expects signed Carbon message hex. Both return the hash
reported by the node and do not poll for execution state; call `GetTransaction`
and check `state` before parsing `result`.

## Stubbed Methods

The generated source currently marks these wrappers as stubbed node methods:

| Wrapper | Documented return behavior |
| ------- | -------------------------- |
| `GetChains` | empty array |
| `GetChain` | default chain object |
| `GetNexus` | default nexus object |
| `GetOrganization`, `GetOrganizationByName` | default organization object |
| `GetOrganizations` | empty array |
| `GetLeaderboard` | default leaderboard object |
| `GetArchive` | default archive object |
| `WriteArchive` | false without persistence |
| `ReadArchive` | empty string |

Do not use these wrappers as proof of live chain state without verifying the
connected node behavior.
