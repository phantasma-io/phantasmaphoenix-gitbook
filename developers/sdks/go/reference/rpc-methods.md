# Go SDK RPC Client

`rpc.PhantasmaRPC` is the typed JSON-RPC facade. Methods are context-first and
return `(value, error)`. Transaction submission methods return the transaction
hash reported by the node and do not wait for execution.

## Construction And Raw Calls

| API | Purpose | Returns and failures |
| --- | ------- | -------------------- |
| `NewRPC(endpoint)` | Creates a client for an explicit RPC URL. | Returns `PhantasmaRPC`. Construction does not call the node. |
| `NewRPCMainnet()` | Creates a client for `https://pharpc1.phantasma.info/rpc`. | Returns `PhantasmaRPC`. |
| `NewRPCSetMainnet()` | Creates clients for the public mainnet endpoint set. | Returns `[]PhantasmaRPC`. |
| `NewRPCTestnet()` | Creates a client for `https://testnet.phantasma.info/rpc`. | Returns `PhantasmaRPC`. |
| `Call(ctx, method, params...)` | Sends a raw JSON-RPC call. | Returns `*jsonrpc.RPCResponse` or an error from transport or JSON-RPC error handling. |

`nil` contexts are normalized to `context.Background()`, but application code
should pass a timeout or cancellation context.

The underlying `pkg/jsonrpc` client generates request ids for `Call` and
`CallBatch`, rejects missing or mismatched response ids, rejects batch responses
whose id set does not match the request set, and enforces
`jsonrpc.DefaultMaxResponseBytes`, 16 MiB. Lower-level users can pass
`RPCClientOpts.MaxResponseBytes` to `jsonrpc.NewClientWithOpts(...)`.

## Build And VM Configuration

| API | Purpose |
| --- | ------- |
| `GetVersion(ctx)` | Reads node build metadata as `BuildInfoResult`. |
| `GetPhantasmaVMConfig(ctx, chainAddressOrName)` | Reads VM feature level, gas settings, storage flags, and deploy fuel configuration for a chain. |

## Accounts, Names, And Balances

| API | Purpose |
| --- | ------- |
| `GetPlatforms(ctx)` | Reads configured platforms and interop mappings. |
| `GetAccountInfo(ctx, address)` | Reads the account name and staking info of one address. |
| `GetAccountInfoWithAddressType(ctx, address, checkAddressReservedByte, addressType)` | The same with explicit address controls. |
| `GetAccountInfos(ctx, addresses)` | Reads the same record for up to 100 addresses in one call. |
| `GetAccountInfosWithAddressType(ctx, addresses, checkAddressReservedByte, addressType)` | The same with explicit address controls. |
| `GetAccount(ctx, address)` | Deprecated. Reads one account with compact account data. |
| `GetAccountWithAddressType(ctx, address, extended, checkAddressReservedByte, addressType)` | Reads one account while forwarding node address validation controls. |
| `GetAccounts(ctx, addresses...)` | Deprecated. Reads multiple accounts from variadic address strings. |
| `GetAccountsText(ctx, addresses)` | Reads multiple accounts from a comma-separated RPC string. |
| `GetAccountsWithAddressType(ctx, addresses, extended, checkAddressReservedByte, addressType)` | Reads multiple accounts with explicit address controls. |
| `LookupName(ctx, name)` | Resolves a registered name to an address string. |

`GetAccountInfo` costs the same whatever the address holds. `GetAccount` and
`GetAccounts` are deprecated, because their response embeds every NFT id the
address owns and the node caps each `Balances[].Ids` list at 10000 entries while
`Balances[].Amount` keeps the true count.

The cursor methods accept a `pageSize` of 1 to 100. The NFT methods accept 1 to
50 when `extended` is true.

| `GetTokenBalance(ctx, address, tokenSymbol, chainAddressOrName)` | Reads one token balance without loading the full account. |
| `GetTokenBalanceChecked(ctx, address, tokenSymbol, chainAddressOrName, checkAddressReservedByte)` | Balance read with reserved-byte validation flag. |
| `GetTokenBalanceWithAddressType(ctx, address, tokenSymbol, chainAddressOrName, checkAddressReservedByte, addressType)` | Balance read with reserved-byte and address-type controls. |
| `GetAddressTransactions(ctx, address, page, pageSize)` | Reads address transaction history with page pagination. |
| `GetAddressTransactionCount(ctx, address, chainName)` | Reads the transaction count for an address on a chain. |

## Blocks And Transactions

| API | Purpose |
| --- | ------- |
| `GetBlockHeight(ctx, chainName)` | Returns the latest height as `*big.Int`. |
| `GetBlockByHeight(ctx, chain, height)` | Reads one block by chain and height string. |
| `GetBlockByHash(ctx, blockHash)` | Reads one block by hash. |
| `GetLatestBlock(ctx, chainAddressOrName)` | Reads the latest block object on a chain. |
| `GetBlockTransactionCountByHash(ctx, blockHash)` | Reads main-chain transaction count for a block hash. |
| `GetBlockTransactionCountByHashOnChain(ctx, chainAddressOrName, blockHash)` | Chain-aware block transaction count. |
| `GetTransaction(ctx, txHash)` | Reads a transaction by hash. |
| `GetTransactionByBlockHashAndIndex(ctx, blockHash, index)` | Reads a main-chain transaction by block hash and index. |
| `GetTransactionByBlockHashAndIndexOnChain(ctx, chainAddressOrName, blockHash, index)` | Chain-aware transaction-by-block-position read. |

## Chain, Contract, Organization, And Leaderboard Metadata

| API | Purpose |
| --- | ------- |
| `GetChains(ctx, extended)` | A stub on the node; see [Stubbed Node Methods](#stubbed-node-methods). |
| `GetChain(ctx, name, extended)` | A stub on the node; see [Stubbed Node Methods](#stubbed-node-methods). |
| `GetNexus(ctx, extended)` | A stub on the node; see [Stubbed Node Methods](#stubbed-node-methods). |
| `GetContracts(ctx, chainAddressOrName, extended)` | Reads contracts on a chain. |
| `GetContract(ctx, name, chainName)` | Legacy order wrapper for contract by name. |
| `GetContractByName(ctx, chainAddressOrName, contractName)` | Chain-first contract by name. |
| `GetContractByAddress(ctx, chainAddressOrName, contractAddress)` | Reads a contract by address. |
| `GetOrganization(ctx, name, includeMemberCount)` | Reads one organization by name. |
| `GetOrganizations(ctx, pageSize, cursor, includeMemberCount)` | Lists organizations with cursor pagination. |
| `GetOrganizationMembers(ctx, name, pageSize, cursor, includeMemberTime)` | Lists organization members with cursor pagination. |
| `GetOrganizationMember(ctx, name, address, checkAddressReservedByte, addressType)` | Checks one address's membership in an organization. |
| `GetLeaderboard(ctx, name)` | A stub on the node; see [Stubbed Node Methods](#stubbed-node-methods). |

## Tokens, Series, And NFTs

| API | Purpose |
| --- | ------- |
| `GetTokens(ctx, extended)` | Reads token definitions. |
| `GetTokensAsMap(ctx, extended)` | Maps token definitions by symbol. |
| `GetTokensByOwner(ctx, extended, ownerAddress)` | Reads tokens filtered by owner. |
| `GetTokensByOwnerWithAddressType(ctx, extended, ownerAddress, addressType)` | Owner-filtered token read with address type. |
| `GetToken(ctx, symbol, extended)` | Reads a token by symbol. |
| `GetTokenWithID(ctx, symbol, extended, carbonTokenID)` | Reads a token by symbol and optional Carbon token id. |
| `GetTokenData(ctx, symbol, tokenID)` | Deprecated. Reads token data for a Phantasma NFT id. `GetNFT` covers it entirely. |
| `GetTokenSeries(ctx, symbol, carbonTokenID, pageSize, cursor)` | Reads cursor-paginated series. |
| `GetTokenSeriesByID(ctx, symbol, carbonTokenID, seriesID, carbonSeriesID)` | Reads one series by Phantasma or Carbon id. |
| `GetTokenNFTs(ctx, carbonTokenID, carbonSeriesID, pageSize, cursor, extended)` | Reads cursor-paginated NFTs for a Carbon token. |
| `GetTokenNFTsWithSeriesID(ctx, carbonTokenID, carbonSeriesID, seriesID, pageSize, cursor, extended)` | Adds Phantasma series id filtering. |
| `GetNFT(ctx, symbol, tokenID, extended)` | Reads one NFT. |
| `GetNFTs(ctx, symbol, tokenIDs, extended)` | Reads multiple NFTs from a string slice. |
| `GetNFTsText(ctx, symbol, tokenIDs, extended)` | Reads multiple NFTs from a comma-separated id string. |

For Carbon id filters, pass `0` when the endpoint should use its no-filter
behavior. `seriesID` is the Phantasma series id string filter.

## Account Token And NFT Inventory

| API | Result shape |
| --- | ------------ |
| `GetAccountFungibleTokens(...)` | `CursorPaginatedResult[[]BalanceResult]` |
| `GetAccountNFTs(...)` | `CursorPaginatedResult[[]TokenDataResult]` |
| `GetAccountOwnedTokens(...)` | `CursorPaginatedResult[[]TokenResult]` |
| `GetAccountOwnedTokenSeries(...)` | `CursorPaginatedResult[[]TokenSeriesResult]` |

Each method has a `WithAddressType` variant that forwards the node address-type
parameter.

## Auctions, Archives, Scripts, And Broadcast

| API | Purpose |
| --- | ------- |
| `GetAuctionsCount(ctx, chainAddressOrName, symbol)` | Reads auction count for a token. |
| `GetAuctions(ctx, chainAddressOrName, symbol, page, pageSize)` | Reads one page of auctions. |
| `GetAuction(ctx, chainAddressOrName, symbol, tokenID)` | Reads one auction. |
| `GetArchive(ctx, hash)` | A stub on the node; see [Stubbed Node Methods](#stubbed-node-methods). |
| `WriteArchive(ctx, hash, blockIndex, blockContent)` | A stub on the node; see [Stubbed Node Methods](#stubbed-node-methods). |
| `WriteArchiveBase64(ctx, hash, blockIndex, blockContent)` | A stub on the node; see [Stubbed Node Methods](#stubbed-node-methods). |
| `ReadArchive(ctx, hash, blockIndex)` | A stub on the node; see [Stubbed Node Methods](#stubbed-node-methods). |
| `InvokeRawScript(ctx, chain, scriptHex)` | Executes a read-only VM script. |
| `SendRawTransaction(ctx, txData)` | Broadcasts signed VM transaction hex. |
| `SendCarbonTransaction(ctx, txData)` | Broadcasts signed Carbon transaction hex. |
| `SignAndSendTransaction(ctx, keys, nexus, script, chainName, payload)` | Builds, signs, and broadcasts a VM transaction that expires `carbon.DefaultTxExpiry` (45 seconds) from now. |
| `SignAndSendTransactionWithExpiration(ctx, keys, nexus, script, chainName, payload, expiration)` | The same with an explicit expiration, a Unix time in seconds. |
| `SignAndSendTransactionTextPayload(...)` | VM sign-and-send where payload is provided as text and encoded by the SDK. |
| `SignAndSendBuiltTransaction(ctx, tx, keys)` | Signs and broadcasts an existing VM transaction. |
| `SendTransaction(ctx, msg, signers, options)` | Plans, pre-flights, signs and broadcasts a Carbon message. |

## Stubbed Node Methods

The node answers these methods with a fixed value and reads or stores nothing:

| Method | Answer |
| ------ | ------ |
| `GetChains` | An empty slice. |
| `GetChain` | A default chain object. |
| `GetNexus` | A default nexus object. |
| `GetLeaderboard` | A default leaderboard object. |
| `GetArchive` | A default archive object. |
| `ReadArchive` | An empty string. |
| `WriteArchive`, `WriteArchiveBase64` | `false`; nothing is stored. |

## Fees And Gas Configuration

| API | Purpose |
| --- | ------- |
| `Fees()` | The fee planner of this chain. |
| `GetGasConfig(ctx)` | Reads the on-chain gas configuration and the chain parameters. |
| `EstimateTransaction(ctx, txData)` | Dry-runs a serialized envelope against current chain state. |
| `ControlTokenID(ctx)` | Reads the gas token's id, which the pre-flight uses as its control lookup. |
| `InfusedAssets(ctx, tokenID, instanceID)` | Reads what an NFT holds at its own address, which a burn plan requires. |

{% content-ref url="/developers/sdks/go/fees-and-broadcasting.md" %}
[Fees And Broadcasting](/developers/sdks/go/fees-and-broadcasting.md)
{% endcontent-ref %}
