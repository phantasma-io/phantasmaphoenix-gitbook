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

## Build And VM Configuration

| API | Purpose |
| --- | ------- |
| `GetVersion(ctx)` | Reads node build metadata as `BuildInfoResult`. |
| `GetPhantasmaVMConfig(ctx, chainAddressOrName)` | Reads VM feature level, gas settings, storage flags, and deploy fuel configuration for a chain. |

## Accounts, Names, And Balances

| API | Purpose |
| --- | ------- |
| `GetPlatforms(ctx)` | Reads configured platforms and interop mappings. |
| `GetAccount(ctx, address)` | Reads one account with compact account data. |
| `GetAccountWithAddressType(ctx, address, extended, checkAddressReservedByte, addressType)` | Reads one account while forwarding node address validation controls. |
| `GetAccounts(ctx, addresses...)` | Reads multiple accounts from variadic address strings. |
| `GetAccountsText(ctx, addresses)` | Reads multiple accounts from a comma-separated RPC string. |
| `GetAccountsWithAddressType(ctx, addresses, extended, checkAddressReservedByte, addressType)` | Reads multiple accounts with explicit address controls. |
| `LookupName(ctx, name)` | Resolves a registered name to an address string. |
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
| `GetChains(ctx, extended)` | Reads all chains. |
| `GetChain(ctx, name, extended)` | Reads one chain by name. |
| `GetNexus(ctx, extended)` | Reads nexus metadata. |
| `GetContracts(ctx, chainAddressOrName, extended)` | Reads contracts on a chain. |
| `GetContract(ctx, name, chainName)` | Legacy order wrapper for contract by name. |
| `GetContractByName(ctx, chainAddressOrName, contractName)` | Chain-first contract by name. |
| `GetContractByAddress(ctx, chainAddressOrName, contractAddress)` | Reads a contract by address. |
| `GetOrganization(ctx, id, extended)` | Reads organization metadata by id. |
| `GetOrganizationByName(ctx, name, extended)` | Reads organization metadata by name. |
| `GetOrganizations(ctx, extended)` | Reads organization list. |
| `GetLeaderboard(ctx, name)` | Reads leaderboard rows. |

## Tokens, Series, And NFTs

| API | Purpose |
| --- | ------- |
| `GetTokens(ctx, extended)` | Reads token definitions. |
| `GetTokensAsMap(ctx, extended)` | Maps token definitions by symbol. |
| `GetTokensByOwner(ctx, extended, ownerAddress)` | Reads tokens filtered by owner. |
| `GetTokensByOwnerWithAddressType(ctx, extended, ownerAddress, addressType)` | Owner-filtered token read with address type. |
| `GetToken(ctx, symbol, extended)` | Reads a token by symbol. |
| `GetTokenWithID(ctx, symbol, extended, carbonTokenID)` | Reads a token by symbol and optional Carbon token id. |
| `GetTokenData(ctx, symbol, tokenID)` | Reads token data for a Phantasma NFT id. |
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
| `GetArchive(ctx, hash)` | Reads archive metadata. |
| `WriteArchive(ctx, hash, blockIndex, blockContent)` | Writes raw archive block bytes. |
| `WriteArchiveBase64(ctx, hash, blockIndex, blockContent)` | Writes already-base64 archive block content. |
| `ReadArchive(ctx, hash, blockIndex)` | Reads one archive block. |
| `InvokeRawScript(ctx, chain, scriptHex)` | Executes a read-only VM script. |
| `SendRawTransaction(ctx, txData)` | Broadcasts signed VM transaction hex. |
| `SendCarbonTransaction(ctx, txData)` | Broadcasts signed Carbon transaction hex. |
| `SignAndSendTransaction(...)` | Builds, signs, and broadcasts a VM transaction. |
| `SignAndSendTransactionWithExpiration(...)` | VM sign-and-send with explicit expiration. |
| `SignAndSendTransactionTextPayload(...)` | VM sign-and-send where payload is provided as text and encoded by the SDK. |
| `SignAndSendBuiltTransaction(ctx, tx, keys)` | Signs and broadcasts an existing VM transaction. |
| `SignAndSendCarbonTransaction(ctx, msg, keys)` | Signs, serializes, and broadcasts a Carbon `TxMsg`. |
