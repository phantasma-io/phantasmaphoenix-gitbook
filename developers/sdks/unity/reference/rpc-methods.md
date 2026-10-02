# Unity RPC Methods

This page documents the `PhantasmaAPI` coroutine surface. Use
[Public API Inventory](public-api.md) when you need every public runtime
symbol.

## Coroutine Model

`PhantasmaAPI` is constructed with an RPC host URL:

```csharp
public PhantasmaAPI(string host, string apiKey = null);
```

`apiKey` is sent as the `X-Api-Key` header on every RPC request.

RPC methods return `IEnumerator` and should be executed with
`StartCoroutine(...)`. Data is delivered through callbacks. Most methods accept
these optional parameters after the success callback:

```csharp
Action<EPHANTASMA_SDK_ERROR_TYPE, string> errorHandlingCallback = null;
int timeout = WebClient.DefaultTimeout;
int retries = WebClient.DefaultRetries;
```

`WebClient.RPCRequest<T>` assigns a generated JSON-RPC id and
`TryDecodeRpcResponse<T>` rejects missing or mismatched response ids, JSON-RPC
error objects, missing `result`, and result values that cannot be decoded into
the requested callback type. These failures are delivered through the error
callback.

## Accounts

| Method family | Use it when | Callback |
| ---- | ---- | ---- |
| `GetAccountInfo` | Reading the account name and staking info of one address. Overloads allow reserved-byte checks and `RpcAddressType`. | `Action<AccountInfoResult>` |
| `GetAccountInfos` | Reading the same record for up to 100 addresses in one call. | `Action<AccountInfoResult[]>` |
| `GetAccount` | Obsolete. Reading one account by address text. Overloads allow `extended`, reserved-byte checks, and `RpcAddressType`. | `Action<AccountResult>` |
| `GetAccounts` | Obsolete. Reading several accounts. The SDK sends a comma-separated address list. | `Action<AccountResult[]>` |
| `LookUpName` | Resolving a registered name to address text. | `Action<string>` |
| `GetAccountFungibleTokens` | Listing fungible balances owned by an account. Overloads accept symbol, Carbon token id, page size, cursor, address checks, and address type. | `Action<CursorPaginatedResult<BalanceResult[]>>` |
| `GetAccountNFTs` | Listing NFT instances owned by an account. Overloads accept symbol, Carbon token id, Carbon series id, page size, cursor, `extended`, address checks, and address type. | `Action<CursorPaginatedResult<TokenDataResult[]>>` |
| `GetAccountOwnedTokens` | Listing NFT token definitions for which the account owns at least one instance. | `Action<CursorPaginatedResult<TokenResult[]>>` |
| `GetAccountOwnedTokenSeries` | Listing NFT series for which the account owns at least one instance. | `Action<CursorPaginatedResult<TokenSeriesResult[]>>` |

`GetAccountInfo` costs the same whatever the address holds. `GetAccount` and
`GetAccounts` are obsolete, because their response embeds every NFT id the
address owns and the node caps each `Balances[].Ids` list at 10000 entries
while `Balances[].Amount` keeps the true count.

The cursor methods accept a `pageSize` of 1 to 100. The NFT methods accept 1 to
50 when `extended` is true.

## Auctions And Blocks

| Method | Use it when | Callback |
| ---- | ---- | ---- |
| `GetAuctionsCount(chainAddressOrName, symbol, ...)` | Counting auctions for a token on one chain. | `Action<int>` |
| `GetAuctions(chainAddressOrName, symbol, page, pageSize, ...)` | Reading one auction page. | `Action<AuctionResult[], uint, uint, uint>` |
| `GetAuction(chainAddressOrName, symbol, IDtext, ...)` | Reading one auction by id. | `Action<AuctionResult>` |
| `GetBlockHeight(chainInput, ...)` | Reading the latest block height for a chain. | `Action<long>` |
| `GetBlockTransactionCountByHash(blockHash, ...)` | Counting transactions in a main-chain block by hash. | `Action<int>` |
| `GetBlockTransactionCountByHash(chainAddressOrName, blockHash, ...)` | Counting transactions in a chain-specific block by hash. | `Action<int>` |
| `GetBlockByHash(blockHash, ...)` | Reading a block by hash. | `Action<BlockResult>` |
| `GetBlockByHeight(chainInput, height, ...)` | Reading a block by chain and height. | `Action<BlockResult>` |
| `GetLatestBlock(chainInput, ...)` | Reading the latest block for a chain. | `Action<BlockResult>` |
| `GetTransactionByBlockHashAndIndex(blockHash, index, ...)` | Reading one transaction by main-chain block hash and index. | `Action<TransactionResult>` |
| `GetTransactionByBlockHashAndIndex(chainAddressOrName, blockHash, index, ...)` | Reading one transaction by chain, block hash, and index. | `Action<TransactionResult>` |

## Chain, Contracts, And Metadata

| Method | Backend status | Callback |
| ---- | ---- | ---- |
| `GetChains` | Stubbed chain query; returns an empty array. | `Action<ChainResult[]>` |
| `GetContract(contractName, ...)` | Reads main-chain contract metadata by name. | `Action<ContractResult>` |
| `GetContracts` | Lists main-chain contracts. | `Action<ContractResult[]>` |
| `GetLeaderboard(name, ...)` | Stubbed leaderboard query; returns a default result. | `Action<LeaderboardResult>` |
| `GetNexus` | Stubbed nexus query; returns a default result. | `Action<NexusResult>` |
| `GetOrganization(name, includeMemberCount, ...)` | Reads one organization by name. | `Action<OrganizationResult>` |
| `GetOrganizations(pageSize, cursor, includeMemberCount, ...)` | Lists organizations with cursor pagination. | `Action<CursorPaginatedResult<OrganizationResult[]>>` |
| `GetOrganizationMembers(name, pageSize, cursor, includeMemberTime, ...)` | Lists organization members with cursor pagination. | `Action<CursorPaginatedResult<OrganizationMemberResult[]>>` |
| `GetOrganizationMember(name, address, checkAddressReservedByte, addressType, ...)` | Checks one address's membership in an organization. | `Action<OrganizationMemberResult>` |

## Tokens And NFTs

| Method family | Use it when | Callback |
| ---- | ---- | ---- |
| `GetToken` | Reading token metadata by symbol or by symbol plus Carbon token id options. | `Action<TokenResult>` |
| `GetTokens` | Listing token metadata. Overloads allow `extended`, owner address, and `RpcAddressType`. | `Action<TokenResult[]>` |
| `GetTokenSeries` | Listing token series with cursor pagination. | `Action<CursorPaginatedResult<TokenSeriesResult[]>>` |
| `GetTokenSeriesById` | Reading one series by Phantasma series id or Carbon series id. | `Action<TokenSeriesResult>` |
| `GetTokenNFTs` | Listing NFTs for a Carbon token and optional series filters. | `Action<CursorPaginatedResult<TokenDataResult[]>>` |
| `GetTokenData` | Deprecated. Reading token data by symbol and id. `GetNFT` covers it entirely. | `Action<TokenDataResult>` |
| `GetNFT` | Reading one NFT and optionally loading properties. | `Action<TokenDataResult>` |
| `GetNFTs` | Reading several NFT ids. | `Action<TokenDataResult[]>` |
| `GetTokenBalance` | Reading one token balance. Overloads allow address checks and `RpcAddressType`. | `Action<BalanceResult>` |

## Transactions And Scripts

| Method | Use it when | Callback |
| ---- | ---- | ---- |
| `GetAddressTransactions(addressText, page, pageSize, ...)` | Reading transaction history for an address. | `Action<AccountTransactionsResult, uint, uint>` |
| `GetAddressTransactionCount(addressText, chainInput, ...)` | Counting transactions for an address on one chain. | `Action<int>` |
| `SendRawTransaction(txData, txHash, ...)` | Broadcasting a hex-encoded Phantasma transaction and checking the expected `Hash`. | `Action<string, string, Hash>` |
| `SendCarbonTransaction(txData, ...)` | Broadcasting a hex-encoded Carbon transaction. | `Action<string, string>` |
| `InvokeRawScript(chainInput, scriptData, ...)` | Running a hex-encoded VM script without committing state. | `Action<ScriptResult>` |
| `GetTransaction(hashText, ...)` | Reading a transaction by hash. | `Action<TransactionResult>` |
| `SignAndSendTransaction(keys, nexus, script, chain, payload, ...)` | Building, signing, serializing, and broadcasting a Phantasma VM transaction. | `Action<string, string>` |
| `SignAndSendCarbonTransaction(keys, txMsg, ...)` | Planning the fee, signing and broadcasting a Carbon `TxMsg`. | `Action<string, string>` |
| `SignAndSendCarbonTransaction(keys[], txMsg, options, ..., preflight)` | The same with several witnesses, fee-plan options and an optional pre-flight. | `Action<string, string>` |
| `PlanCarbonTransaction(keys[], txMsg, options, ...)` | Pricing a Carbon message without signing it. | `Action<FeePlan>` |

The `SignAndSendTransaction` overloads accept string or byte-array payloads.
The byte-array overload also accepts `customSignFunction`. The coroutine stamps
an expiration 20 minutes from now; there is no argument to change it.

## Fees And Gas Configuration

| Method | Use it when | Callback |
| ---- | ---- | ---- |
| `GetGasConfig(...)` | Reading the on-chain gas configuration and the chain parameters. | `Action<GasConfigResult>` |
| `EstimateTransaction(txData, ...)` | Dry-running a serialized envelope against current chain state. | `Action<EstimateTransactionResult>` |

`GetGasConfig` changes only through a governance resolution, so the result is
safe to cache. `EstimateTransaction` returns a standard RPC error until the
estimate service is launched.

{% content-ref url="/developers/sdks/unity/carbon-transactions.md" %}
[Carbon Transactions And Fees](/developers/sdks/unity/carbon-transactions.md)
{% endcontent-ref %}

## Storage And Validation

| Method | Backend status | Callback |
| ---- | ---- | ---- |
| `GetArchive(hashText, ...)` | Stubbed archive query; returns a default result. | `Action<ArchiveResult>` |
| `WriteArchive(hashText, blockIndex, blockContent, ...)` | Stubbed archive write; returns `false`. | `Action<Boolean>` |
| `ReadArchive(hashText, blockIndex, ...)` | Stubbed archive read; returns an empty string. | `Action<string>` |
| `IsValidPrivateKey(key)` | Local WIF shape check. | `bool` |
| `IsValidAddress(address)` | Local address text shape check. | `bool` |

`IsValidPrivateKey` checks for `L` or `K` WIF prefixes and length 52.
`IsValidAddress` checks for prefix `P` and length 45. Chain-side validation is
still authoritative.
