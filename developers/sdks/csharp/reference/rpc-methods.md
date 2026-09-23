# C# RPC Methods

This page documents the `PhantasmaAPI` surface. Use
[Public API Inventory](public-api.md) when you need the complete list of public
classes, methods, fields, and enum values.

## Call Model

`PhantasmaAPI` wraps JSON-RPC calls with async methods. The constructor stores
the RPC endpoint URL in `Host` and uses either the supplied `RpcClient` or an
owned internal client:

```csharp
public PhantasmaAPI(string host, RpcClient? rpcClient = null, string? apiKey = null)
```

`apiKey` is sent as the `X-Api-Key` header on every request. It is used only
when this wrapper creates its own `RpcClient`.

Most read methods return `Task<T?>`. Methods that adapt paginated RPC responses
return tuples or `CursorPaginatedResult<T>`. Methods that broadcast transactions
return the transaction hash text returned by the node.

`RpcClient` generates a per-request JSON-RPC id, rejects missing or mismatched
response ids, rejects responses that omit `result`, and enforces
`RpcClient.DefaultMaxResponseBytes`, currently 16 MiB. The constructor accepts
`maxResponseBytes` when a caller needs a different positive limit.

## Result Models

`PhantasmaAPI` methods decode node responses into models under
`PhantasmaPhoenix.RPC.Models`.

| Model | Fields and helpers |
| ---- | ---- |
| `AccountInfoResult` | `Address`, `Name`, `Stake` |
| `AccountResult` | `Address`, `Name`, `Stakes`, `Stake`, `Unclaimed`, optional `Relay`, `Validator`, `Storage`, `Balances`, optional `Txs` |
| `BlockResult` | `Hash`, `PreviousHash`, `Timestamp`, `Height`, `ChainAddress`, `Protocol`, `Txs`, `ValidatorAddress`, optional `ProducerAddress`, `Reward`, optional `Events`, optional `Oracles` |
| `EventResult` | `Address`, `Contract`, `Kind`, `Name`, `Data` |
| `GasConfigResult` | `GasModelVersion`, optional `GasConfig` of type `GasConfigDataResult`, `BlockRateTarget`, `ExpiryWindow`, optional `UnitsPerBlockDataByte`, and `ToGasConfig()` |
| `EstimateTransactionResult` | `WouldAbort`, optional `AbortReason`, `GasBillKcalBase`, `DataRows`, `DataEscrowAtoms`, `DataRefundAtoms`, `RecommendedMaxGas`, `RecommendedMaxData`, and `ToFeeQuote()` |
| `TransactionResult` | `Hash`, `ChainAddress`, `Timestamp`, `BlockHeight`, `BlockHash`, `Script`, `CarbonTxType`, `CarbonTxData`, `Payload`, optional `DebugComment`, `Events`, `ExtendedEvents`, `Result`, `Fee`, `State`, optional `Signatures`, `Sender`, `GasPayer`, `GasTarget`, `GasPrice`, `GasLimit`, `Expiration` |
| `ScriptResult` | `Events`, optional `Result`, optional `Error`, `Results`, `Oracles`, optional `State`, optional `Gas` |
| `TokenResult` | token definition fields, optional `Script`, `Series`, `CarbonId`, optional `Metadata`, optional `TokenSchemas`, optional `External`, optional `Price`, and token-flag helpers |
| `TokenSeriesResult` | `SeriesId`, `carbonTokenId`, `carbonSeriesId`, `OwnerAddress`, `MaxMint`, `MintCount`, `CurrentSupply`, `MaxSupply`, optional `BurnedSupply`, optional `Mode`, optional `Script`, optional `Methods`, `Metadata` |
| `TokenDataResult` | NFT id, series, Carbon identifiers, owner/creator, ROM/RAM, status, infusion, and properties |
| `TokenPropertyResult` | `Key`, and `Value` of type `VmValue` |
| `VmValue` | A value decoded from VM storage: `Text` for a scalar, `Items` for an array, `Fields` for a struct |

At most one of `Text`, `Items` and `Fields` is set. A scalar whose content the
producer could not read carries none of them and arrives as JSON null, so a
consumer reading `Text` has to handle null. That state is real chain data: a
shared-ROM NFT property can have no string content, and it is still answered so
that its key does not disappear.

On the wire a `VmValue` is the plain JSON value, which is a string, an array or
an object. The shape itself says which of the three it is. Scalars are always
`Text`, because chain numbers are big integers and JSON numbers lose precision
above 2^53. Byte values arrive as hex. Reading a scalar stays a string
assignment, through the implicit conversion the type declares.

For a contract event, `Kind` is `Custom_V2` and `Name` is the event name the
contract declared. For every other event, `Name` repeats `Kind`.

## Accounts

| Method | RPC method | Use it when | Return |
| ---- | ---- | ---- | ---- |
| `GetAccountInfoAsync(account)` | `getAccountInfo` | Reading the account name and staking info of one address. | `Task<AccountInfoResult?>` |
| `GetAccountInfosAsync(accounts)` | `getAccountInfos` | Reading the same record for up to 100 addresses in one call. | `Task<AccountInfoResult[]?>` |
| `GetAccountAsync(address)` | `getAccount` | Deprecated. Reading one account with default address validation. | `Task<AccountResult?>` |
| `GetAccountAsync(address, extended, checkAddressReservedByte, addressType)` | `getAccount` | Deprecated. Reading one account with explicit address validation and address type. | `Task<AccountResult?>` |
| `GetAccountsAsync(addresses)` | `getAccounts` | Deprecated. Reading several accounts in one request. The SDK joins the array with commas. | `Task<AccountResult[]?>` |
| `GetAccountsAsync(addresses, extended, checkAddressReservedByte, addressType)` | `getAccounts` | Deprecated. Reading several accounts with explicit address options. | `Task<AccountResult[]?>` |
| `LookUpNameAsync(name)` | `lookUpName` | Resolving a registered name to address text. | `Task<string?>` |
| `GetAccountFungibleTokensAsync(...)` | `getAccountFungibleTokens` | Listing fungible balances owned by an account with optional symbol, Carbon token id, cursor, and address checks. | `Task<CursorPaginatedResult<BalanceResult[]>?>` |
| `GetAccountNFTsAsync(...)` | `getAccountNFTs` | Listing NFT instances owned by an account with optional token, series, cursor, and extended-property flags. | `Task<CursorPaginatedResult<TokenDataResult[]>?>` |
| `GetAccountOwnedTokensAsync(...)` | `getAccountOwnedTokens` | Listing NFT token definitions for which the account owns at least one instance. | `Task<CursorPaginatedResult<TokenResult[]>?>` |
| `GetAccountOwnedTokenSeriesAsync(...)` | `getAccountOwnedTokenSeries` | Listing NFT series for which the account owns at least one instance. | `Task<CursorPaginatedResult<TokenSeriesResult[]>?>` |

The account cursor methods also expose overloads that accept
`RpcAddressType`. Use those overloads when the caller is working with non-default
address families or wants reserved-byte validation to be explicit.

`GetAccountAsync` and `GetAccountsAsync` are marked obsolete. Their response
embeds every NFT id the address owns, and the node caps each `Balances[].Ids`
list at 10000 entries while `Balances[].Amount` keeps the true count. Use
`GetAccountInfoAsync` with the cursor methods.

The cursor methods accept a `pageSize` of 1 to 100. The NFT methods accept 1 to
50 when `extended` is true. The node rejects anything outside the range.

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
| `GetOrganizationAsync(name, includeMemberCount)` | `getOrganization` | Reading one organization by name. | `Task<OrganizationResult?>` |
| `GetOrganizationsAsync(pageSize, cursor, includeMemberCount)` | `getOrganizations` | Listing organizations with cursor pagination. | `Task<CursorPaginatedResult<OrganizationResult[]>?>` |
| `GetOrganizationMembersAsync(name, pageSize, cursor, includeMemberTime)` | `getOrganizationMembers` | Listing organization members with cursor pagination. | `Task<CursorPaginatedResult<OrganizationMemberResult[]>?>` |
| `GetOrganizationMemberAsync(name, address, checkAddressReservedByte, addressType)` | `getOrganizationMember` | Checking one address's membership in an organization. | `Task<OrganizationMemberResult?>` |

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
| `GetTokenDataAsync(symbol, tokenId)` | `getTokenData` | Deprecated. Reading token data for one token id. `getNFT` covers it entirely. | `Task<TokenDataResult?>` |
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
| `SendTransactionAsync(msg, signers, options, cancellationToken)` | `sendCarbonTransaction` | Planning, pre-flighting, signing and broadcasting a Carbon message in one call. | `Task<string>` |

`SignAndSendTransactionAsync` throws if the RPC hash differs from the locally
computed transaction hash. It signs the transaction bytes before signatures are
attached, serializes with signatures, and broadcasts the hex string.

`SendTransactionAsync` takes one `ITxSigner`, a list of them, one `IKeyPair` or
an array of them. It plans a message whose `MaxGas` is still zero, and refuses a
token creation whose symbol the chain reports as taken.

## Fees And Gas Configuration

| Method | RPC method | Use it when | Return |
| ---- | ---- | ---- | ---- |
| `Fees` | none | Planning fees against this chain. It is a `ChainFeePlanner`. | `ChainFeePlanner` |
| `GetGasConfigAsync()` | `getGasConfig` | Reading the on-chain gas configuration and the chain parameters. | `Task<GasConfigResult?>` |
| `EstimateTransactionAsync(txData)` | `estimateTransaction` | Dry-running a serialized envelope against current chain state. | `Task<EstimateTransactionResult?>` |
| `ControlTokenIdAsync()` | none | Reading the gas token's id, which the pre-flight uses as its control lookup. | `Task<ulong?>` |
| `InfusedAssetsAsync(tokenId, instanceId)` | several | Reading what an NFT holds at its own address, which a burn plan requires. | `Task<IReadOnlyList<InfusedAsset>>` |

{% content-ref url="/developers/sdks/csharp/fees-and-broadcasting.md" %}
[Fees And Broadcasting](/developers/sdks/csharp/fees-and-broadcasting.md)
{% endcontent-ref %}

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
