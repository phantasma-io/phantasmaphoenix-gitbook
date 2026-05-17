# Unity RPC Methods

This page documents the `PhantasmaAPI` coroutine surface. Use
[Public API Inventory](public-api.md) when you need every public runtime symbol
from the source tree.

Source baseline:

| Item | Value |
| ---- | ----- |
| Source repo | `Phantasma-UnitySDK` |
| Source commit | `a8e093654d682de6fd0b7568f036d22b5d6ab69e` |
| Source file | `PhantasmaPhoenix.Unity.Core/Runtime/Scripts/PhantasmaAPI.cs` |

## Coroutine Model

`PhantasmaAPI` is constructed with an RPC host URL:

```csharp
public PhantasmaAPI(string host);
```

RPC methods return `IEnumerator` and should be executed with
`StartCoroutine(...)`. Data is delivered through callbacks. Most methods accept
these optional parameters after the success callback:

```csharp
Action<EPHANTASMA_SDK_ERROR_TYPE, string> errorHandlingCallback = null;
int timeout = WebClient.DefaultTimeout;
int retries = WebClient.DefaultRetries;
```

## Accounts

| Method family | Use it when | Callback |
| ---- | ---- | ---- |
| `GetAccount` | Reading one account by address text. Overloads allow `extended`, reserved-byte checks, and `RpcAddressType`. | `Action<AccountResult>` |
| `GetAccounts` | Reading several accounts. The SDK sends a comma-separated address list. | `Action<AccountResult[]>` |
| `LookUpName` | Resolving a registered name to address text. | `Action<string>` |
| `GetAccountFungibleTokens` | Listing fungible balances owned by an account. Overloads accept symbol, Carbon token id, page size, cursor, address checks, and address type. | `Action<CursorPaginatedResult<BalanceResult[]>>` |
| `GetAccountNFTs` | Listing NFT instances owned by an account. Overloads accept symbol, Carbon token id, Carbon series id, page size, cursor, `extended`, address checks, and address type. | `Action<CursorPaginatedResult<TokenDataResult[]>>` |
| `GetAccountOwnedTokens` | Listing NFT token definitions for which the account owns at least one instance. | `Action<CursorPaginatedResult<TokenResult[]>>` |
| `GetAccountOwnedTokenSeries` | Listing NFT series for which the account owns at least one instance. | `Action<CursorPaginatedResult<TokenSeriesResult[]>>` |

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

The listed source baseline exposes no `chainAddressOrName` overload for
`GetTransactionByBlockHashAndIndex`.

## Chain, Contracts, And Metadata

| Method | Backend status | Callback |
| ---- | ---- | ---- |
| `GetChains` | Stubbed chain query; returns an empty array. | `Action<ChainResult[]>` |
| `GetContract(contractName, ...)` | Reads main-chain contract metadata by name. | `Action<ContractResult>` |
| `GetContracts` | Lists main-chain contracts. | `Action<ContractResult[]>` |
| `GetLeaderboard(name, ...)` | Stubbed leaderboard query; returns a default result. | `Action<LeaderboardResult>` |
| `GetNexus` | Stubbed nexus query; returns a default result. | `Action<NexusResult>` |
| `GetOrganization(ID, ...)` | Stubbed organization query; returns a default result. | `Action<OrganizationResult>` |
| `GetOrganizationByName(name, ...)` | Stubbed organization query; returns a default result. | `Action<OrganizationResult>` |
| `GetOrganizations` | Stubbed organization query; returns an empty array. | `Action<OrganizationResult[]>` |

## Tokens And NFTs

| Method family | Use it when | Callback |
| ---- | ---- | ---- |
| `GetToken` | Reading token metadata by symbol or by symbol plus Carbon token id options. | `Action<TokenResult>` |
| `GetTokens` | Listing token metadata. Overloads allow `extended`, owner address, and `RpcAddressType`. | `Action<TokenResult[]>` |
| `GetTokenSeries` | Listing token series with cursor pagination. | `Action<CursorPaginatedResult<TokenSeriesResult[]>>` |
| `GetTokenSeriesById` | Reading one series by Phantasma series id or Carbon series id. | `Action<TokenSeriesResult>` |
| `GetTokenNFTs` | Listing NFTs for a Carbon token and optional series filters. | `Action<CursorPaginatedResult<TokenDataResult[]>>` |
| `GetTokenData` | Reading token data by symbol and id. | `Action<TokenDataResult>` |
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
| `SignAndSendCarbonTransaction(keys, txMsg, ...)` | Signing, serializing, and broadcasting a Carbon `TxMsg`. | `Action<string, string>` |

The `SignAndSendTransaction` overloads accept string or byte-array payloads.
The byte-array overload also accepts `customSignFunction`.

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
