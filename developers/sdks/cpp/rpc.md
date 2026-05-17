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

The generated API includes current chain and Carbon-era wrappers for:

| Area | Methods |
| ---- | ------- |
| Accounts and balances | `GetAccount`, `GetAccounts`, `LookUpName`, `GetTokenBalance`, account inventory cursor methods |
| Blocks and transactions | `GetBlockHeight`, `GetBlockByHash`, `GetBlockByHeight`, `GetLatestBlock`, transaction-by-block methods, `GetTransaction` |
| Chain metadata | `GetChains`, `GetChain`, `GetNexus`, `GetPhantasmaVmConfig`, `GetVersion` |
| Contracts and organizations | `GetContracts`, `GetContract`, `GetContractByAddress`, organization and leaderboard wrappers |
| Tokens, series, NFTs | `GetTokens`, `GetToken`, `GetTokenSeries`, `GetTokenSeriesById`, `GetTokenNFTs`, `GetTokenData`, `GetNFT`, `GetNFTs` |
| Archives and auctions | `GetArchive`, `ReadArchive`, `WriteArchive`, auction wrappers |
| Broadcast and invoke | `InvokeRawScript`, `SendRawTransaction`, `SendCarbonTransaction` |

## Stubbed Node Methods

The C++ generated header marks several Phantasma RPC methods as currently
stubbed in the underlying node/API surface. They should not be treated as live
data sources until the node returns real values:

| Method group | Stub behavior documented in source |
| ------------ | ---------------------------------- |
| `GetChains` | returns an empty array |
| `GetChain` | returns a default chain object |
| `GetNexus` | returns a default nexus object |
| `GetOrganization`, `GetOrganizationByName` | return a default organization object |
| `GetOrganizations` | returns an empty array |
| `GetLeaderboard` | returns a default leaderboard object |
| `GetArchive` | returns a default archive object |
| `WriteArchive` | returns false without persisting data |
| `ReadArchive` | returns an empty string |

Document code paths that depend on these methods and prefer direct node
verification before making them production-critical.
