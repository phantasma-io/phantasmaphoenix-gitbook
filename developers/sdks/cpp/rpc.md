# C++ SDK RPC

The C++ SDK exposes two RPC layers:

| Layer | API | Use it when |
| ----- | --- | ----------- |
| High-level | `phantasma::rpc::PhantasmaAPI` | You configured an HTTP and JSON adapter and want typed method calls. |
| Low-level | `phantasma::rpc::PhantasmaJsonAPI` | You want to build JSON-RPC requests and parse responses while using your own transport. |

## High-Level Calls

```cpp
HttpClient http("http://localhost:5172/rpc");
phantasma::rpc::PhantasmaAPI api(http);

phantasma::rpc::PhantasmaError err{};
auto height = api.GetBlockHeight("main", &err);
if (err.code != 0) {
    // handle err.message
}
```

Methods return typed result objects and write errors into the optional
`PhantasmaError*`.

For nodes that require an API key, pass it as the third argument of the cURL
adapter; it is sent in the `X-Api-Key` header on every request:

```cpp
HttpClient http("http://localhost:5172/rpc", PHANTASMA_DEFAULT_MAX_RPC_RESPONSE_BYTES, "your-api-key");
```

## Low-Level Calls

`PhantasmaJsonAPI` has matching `Make...Request` and `Parse...Response` methods.
Use it when the application owns transport, retries, logging, or an existing
HTTP stack.

```cpp
JSONBuilder request;
phantasma::rpc::PhantasmaJsonAPI::MakeGetBlockHeightRequest(request, "main");
```

After sending the JSON to the node, parse the JSON result into the corresponding
model.

## Current RPC Coverage

The generated API includes wrappers for:

| Area | Methods |
| ---- | ------- |
| Accounts and balances | `GetAccountInfo`, `GetAccountInfos`, `LookUpName`, `GetTokenBalance`, account inventory cursor methods |
| Blocks and transactions | `GetBlockHeight`, `GetBlockByHash`, `GetBlockByHeight`, `GetLatestBlock`, transaction-by-block methods, `GetTransaction` |
| Chain metadata | `GetChains`, `GetChain`, `GetNexus`, `GetPhantasmaVmConfig`, `GetVersion` |
| Contracts and organizations | `GetContracts`, `GetContract`, `GetContractByAddress`, organization and leaderboard wrappers |
| Tokens, series, NFTs | `GetTokens`, `GetToken`, `GetTokenSeries`, `GetTokenSeriesById`, `GetTokenNFTs`, `GetNFT`, `GetNFTs` |
| Fees | `GetGasConfig`, `EstimateTransaction` |
| Archives and auctions | `GetArchive`, `ReadArchive`, `WriteArchive`, auction wrappers |
| Broadcast and invoke | `InvokeRawScript`, `SendRawTransaction`, `SendCarbonTransaction` |

`GetAccountInfo` returns the account name and the staking info. Its cost does
not depend on how much the address holds, which makes it the call for a refresh
loop. `GetAccountInfos` answers up to 100 addresses in one call.

`GetAccount` and `GetAccounts` are deprecated. Their response embeds every NFT
id the address owns, and the node caps each `balances[].ids` list at 10000
entries while `balances[].amount` keeps the true count. `GetTokenData` is
deprecated too, because `GetNFT` covers it entirely.

## Stubbed Node Methods

`GetChains`, `GetChain`, `GetNexus`, `GetLeaderboard`, `GetArchive`,
`WriteArchive` and `ReadArchive` are stubbed on the node and return default
values. The table is in the [RPC Client](reference/rpc-methods.md#stubbed-methods)
reference.
