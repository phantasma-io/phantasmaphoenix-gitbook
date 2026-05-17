# C# RPC Methods

This page documents the `PhantasmaAPI` surface. Use
[Public API Inventory](public-api.md) when you need the complete list of public
classes, methods, fields, and enum values from the source tree.

Source baseline:

| Item | Value |
| ---- | ----- |
| Source repo | `phantasmaphoenix-sdk-cs` |
| Source commit | `820680b38e67109b7f94e1d26058d6933f758b26` |
| Source file | `PhantasmaPhoenix.RPC/src/PhantasmaAPI.cs` |

## Call Model

`PhantasmaAPI` wraps JSON-RPC calls with async methods. The constructor stores
the RPC endpoint URL in `Host` and uses either the supplied `RpcClient` or an
owned internal client:

```csharp
public PhantasmaAPI(string host, RpcClient? rpcClient)
```

Most read methods return `Task<T?>`. Methods that adapt paginated RPC responses
return tuples or `CursorPaginatedResult<T>`. Methods that broadcast transactions
return the transaction hash text returned by the node.

## Accounts

| Method | RPC method | Use it when | Return |
| ---- | ---- | ---- | ---- |
| `GetAccountAsync(address)` | `getAccount` | Reading one account with default address validation. | `Task<AccountResult?>` |
| `GetAccountAsync(address, extended, checkAddressReservedByte, addressType)` | `getAccount` | Reading one account with explicit address validation and address type. | `Task<AccountResult?>` |
| `GetAccountsAsync(addresses)` | `getAccounts` | Reading several accounts in one request. The SDK joins the array with commas. | `Task<AccountResult[]?>` |
| `GetAccountsAsync(addresses, extended, checkAddressReservedByte, addressType)` | `getAccounts` | Reading several accounts with explicit address options. | `Task<AccountResult[]?>` |
| `LookUpNameAsync(name)` | `lookUpName` | Resolving a registered name to address text. | `Task<string?>` |
| `GetAccountFungibleTokensAsync(...)` | `getAccountFungibleTokens` | Listing fungible balances owned by an account with optional symbol, Carbon token id, cursor, and address checks. | `Task<CursorPaginatedResult<BalanceResult[]>?>` |
| `GetAccountNFTsAsync(...)` | `getAccountNFTs` | Listing NFT instances owned by an account with optional token, series, cursor, and extended-property flags. | `Task<CursorPaginatedResult<TokenDataResult[]>?>` |
| `GetAccountOwnedTokensAsync(...)` | `getAccountOwnedTokens` | Listing NFT token definitions for which the account owns at least one instance. | `Task<CursorPaginatedResult<TokenResult[]>?>` |
| `GetAccountOwnedTokenSeriesAsync(...)` | `getAccountOwnedTokenSeries` | Listing NFT series for which the account owns at least one instance. | `Task<CursorPaginatedResult<TokenSeriesResult[]>?>` |

The account cursor methods also expose overloads that accept
`RpcAddressType`. Use those overloads when the caller is working with non-default
address families or wants reserved-byte validation to be explicit.

## Auctions And Blocks

| Method | RPC method | Use it when | Return |
| ---- | ---- | ---- | ---- |
| `GetAuctionsCountAsync(chainAddressOrName, symbol)` | `getAuctionsCount` | Counting market auctions for one token on one chain. | `Task<int>` |
| `GetAuctionsAsync(chainAddressOrName, symbol, page, pageSize)` | `getAuctions` | Reading one auction page. The SDK unwraps `PaginatedResult<AuctionResult[]>`. | `Task<(AuctionResult[]? result, uint page, uint total, uint totalPages)>` |
| `GetAuctionAsync(chainAddressOrName, symbol, id)` | `getAuction` | Reading one auction by id. | `Task<AuctionResult?>` |
| `GetBlockHeightAsync(chain)` | `getBlockHeight` | Reading the latest height for a chain. | `Task<long>` |
| `GetBlockTransactionCountByHashAsync(chainAddressOrName, blockHash)` | `getBlockTransactionCountByHash` | Counting transactions in a block by hash. | `Task<int>` |
| `GetBlockByHashAsync(blockHash)` | `getBlockByHash` | Reading a block by hash. | `Task<BlockResult?>` |
| `GetBlockByHeightAsync(chain, height)` | `getBlockByHeight` | Reading a block by chain and height. | `Task<BlockResult?>` |
| `GetLatestBlockAsync(chain)` | `getLatestBlock` | Reading the most recent block for a chain. | `Task<BlockResult?>` |
| `GetTransactionByBlockHashAndIndexAsync(chainAddressOrName, blockHash, index)` | `getTransactionByBlockHashAndIndex` | Reading one transaction from a known block position. | `Task<TransactionResult?>` |

`GetBlockHeightAsync`, `GetBlockTransactionCountByHashAsync`, and
`GetAuctionsCountAsync` parse string RPC results into numeric values using
`InvariantCulture`.

## Chain, Contracts, And Metadata

| Method | RPC method | Use it when | Return |
| ---- | ---- | ---- | ---- |
| `GetChainsAsync()` | `getChains` | Listing chains. Current backend behavior is stubbed and returns an empty array. | `Task<ChainResult[]?>` |
| `GetChainAsync(name, extended)` | `getChain` | Reading one chain. Current backend behavior is stubbed and returns a default chain result. | `Task<ChainResult?>` |
| `GetContractAsync(contractName)` | `getContract` | Reading a main-chain contract by name. The SDK passes `DomainSettings.RootChainName`. | `Task<ContractResult?>` |
| `GetContractByAddressAsync(chainAddressOrName, contractAddress)` | `getContractByAddress` | Reading a contract by chain and address. | `Task<ContractResult?>` |
| `GetContractsAsync()` | `getContracts` | Listing main-chain contracts. The SDK passes `DomainSettings.RootChainName`. | `Task<ContractResult[]?>` |
| `GetLeaderboardAsync(name)` | `getLeaderboard` | Reading one leaderboard. Current backend behavior is stubbed and returns a default result. | `Task<LeaderboardResult?>` |
| `GetNexusAsync()` | `getNexus` | Reading nexus metadata. Current backend behavior is stubbed and returns a default result. | `Task<NexusResult?>` |
| `GetOrganizationAsync(id)` | `getOrganization` | Reading one organization by id. Current backend behavior is stubbed. | `Task<OrganizationResult?>` |
| `GetOrganizationByNameAsync(name)` | `getOrganizationByName` | Reading one organization by name. Current backend behavior is stubbed. | `Task<OrganizationResult?>` |
| `GetOrganizationsAsync()` | `getOrganizations` | Listing organizations. Current backend behavior is stubbed and returns an empty array. | `Task<OrganizationResult[]?>` |

## Tokens And NFTs

| Method | RPC method | Use it when | Return |
| ---- | ---- | ---- | ---- |
| `GetTokenAsync(symbol)` | `getToken` | Reading token metadata by symbol. | `Task<TokenResult?>` |
| `GetTokenAsync(symbol, extended, carbonTokenId)` | `getToken` | Reading token metadata by symbol or Carbon token id. | `Task<TokenResult?>` |
| `GetTokensAsync()` | `getTokens` | Listing tokens with default server options. | `Task<TokenResult[]?>` |
| `GetTokensAsync(extended, ownerAddress)` | `getTokens` | Listing tokens with extended data and optional owner filter. | `Task<TokenResult[]?>` |
| `GetTokensAsync(extended, ownerAddress, addressType)` | `getTokens` | Listing tokens with owner filter and explicit owner address type. | `Task<TokenResult[]?>` |
| `GetTokenSeriesAsync(symbol, carbonTokenId, pageSize, cursor)` | `getTokenSeries` | Listing series for a token using cursor pagination. | `Task<CursorPaginatedResult<TokenSeriesResult[]>?>` |
| `GetTokenSeriesByIdAsync(symbol, carbonTokenId, seriesId, carbonSeriesId)` | `getTokenSeriesById` | Reading one series by either Phantasma series id or Carbon series id. | `Task<TokenSeriesResult?>` |
| `GetTokenNFTsAsync(carbonTokenId, carbonSeriesId, pageSize, cursor, extended, seriesId)` | `getTokenNFTs` | Listing NFTs for a Carbon token. `seriesId` is appended last for positional compatibility with older RPC servers. | `Task<CursorPaginatedResult<TokenDataResult[]>?>` |
| `GetTokenBalanceAsync(address, symbol, chain)` | `getTokenBalance` | Reading one token balance. | `Task<BalanceResult?>` |
| `GetTokenBalanceAsync(address, symbol, chain, checkAddressReservedByte, addressType)` | `getTokenBalance` | Reading one token balance with explicit address validation and address type. | `Task<BalanceResult?>` |
| `GetTokenDataAsync(symbol, tokenId)` | `getTokenData` | Reading token data for one token id. | `Task<TokenDataResult?>` |
| `GetNFTAsync(symbol, tokenId, loadProperties)` | `getNFT` | Reading NFT data and optionally loading properties. | `Task<TokenDataResult?>` |
| `GetNFTsAsync(symbol, tokenIds, extended)` | `getNFTs` | Reading several NFT ids. The SDK joins ids with commas. | `Task<TokenDataResult[]?>` |

## Transactions And Scripts

| Method | RPC method | Use it when | Return |
| ---- | ---- | ---- | ---- |
| `GetAddressTransactionsAsync(address, page, pageSize)` | `getAddressTransactions` | Reading transaction history for one address. The SDK unwraps `PaginatedResult<AccountTransactionsResult>`. | `Task<(AccountTransactionsResult? result, uint page, uint totalPages)>` |
| `GetAddressTransactionCountAsync(address, chain)` | `getAddressTransactionCount` | Counting address transactions on one chain. | `Task<int>` |
| `GetTransactionAsync(txHash)` | `getTransaction` | Reading a transaction by hash. | `Task<TransactionResult?>` |
| `SendRawTransactionAsync(txData)` | `sendRawTransaction` | Broadcasting a hex-encoded Phantasma transaction. | `Task<string?>` |
| `SendCarbonTransactionAsync(txData)` | `sendCarbonTransaction` | Broadcasting a hex-encoded Carbon transaction. | `Task<string?>` |
| `InvokeRawScriptAsync(chain, scriptData)` | `invokeRawScript` | Running a hex-encoded VM script without committing state. | `Task<ScriptResult?>` |
| `SignAndSendTransactionAsync(keys, nexus, script, chain, payload, customSignFunction)` | `sendRawTransaction` | Building a `Protocol.Transaction`, signing it, broadcasting it, and checking the returned hash against the local hash. | `Task<string?>` |
| `SignAndSendCarbonTransactionAsync(keys, txMsg)` | `sendCarbonTransaction` | Signing a Carbon `TxMsg` with an Ed25519 witness and broadcasting it. | `Task<string?>` |

`SignAndSendTransactionAsync` throws if the RPC hash differs from the locally
computed transaction hash. It signs the transaction bytes before signatures are
attached, serializes with signatures, and broadcasts the hex string.

## Storage And Validation

| Method | RPC method | Use it when | Return |
| ---- | ---- | ---- | ---- |
| `GetArchiveAsync(hash)` | `getArchive` | Reading archive metadata. Current backend behavior is stubbed and returns a default result. | `Task<ArchiveResult?>` |
| `WriteArchiveAsync(hash, blockIndex, blockContent)` | `writeArchive` | Writing one archive block. Current backend behavior is stubbed and returns `false`. | `Task<bool>` |
| `ReadArchiveAsync(hash, blockIndex)` | `readArchive` | Reading one archive block. Current backend behavior is stubbed and returns an empty string. | `Task<string?>` |
| `IsValidPrivateKey(key)` | none | Checking the WIF shape used by the SDK helper. | `bool` |
| `IsValidAddress(address)` | none | Checking the SDK address text shape. | `bool` |

`IsValidPrivateKey` checks for `L` or `K` WIF prefixes and length 52.
`IsValidAddress` checks for prefix `P` and length 45. These helpers do not
replace chain-side validation.
