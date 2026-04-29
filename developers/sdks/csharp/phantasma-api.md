# High level API for interacting with Phantasma chain

Plain .NET RPC wrapper for the Phantasma API using `RpcClient` with `async` / `await`

---

## Initialization

### `PhantasmaAPI(string host, RpcClient? rpcClient)`
Creates a new Phantasma API wrapper using the given `RpcClient` or a new internal instance

**Parameters**
- `host` — RPC endpoint URL like `https://testnet.phantasma.info/rpc`
- `rpcClient` — optional `RpcClient` to use. If `null`, a new instance will be created and disposed by this object

**Ownership**
- If `rpcClient` is not provided, the internal client is owned by `PhantasmaAPI` and will be disposed on `Dispose()`

### `Dispose()`
Disposes this API instance and the internal `RpcClient` if owned

---

## Account

### `Task<AccountResult?> GetAccountAsync(string address)`
Gets account information, including balances, for the specified address

**Parameters**
- `address` — account address

**Returns**
- `AccountResult` or `null` if not found

---

### `Task<AccountResult?> GetAccountAsync(string address, bool extended, bool checkAddressReservedByte, RpcAddressType addressType)`
Gets account information for a specific address encoding.

**Parameters**
- `address` — account address text
- `extended` — deprecated server flag; kept for RPC parity
- `checkAddressReservedByte` — `true` to validate the address reserved byte
- `addressType` — account address encoding expected by the RPC

**Returns**
- `AccountResult` or `null` if not found

---

### `Task<AccountResult[]?> GetAccountsAsync(string[] addresses)`
Gets account information for multiple addresses

**Parameters**
- `addresses` — array of account addresses

**Returns**
- array of `AccountResult` or `null`

---

### `Task<string?> LookUpNameAsync(string name)`
Looks up an address by name

**Parameters**
- `name` — registered name to resolve

**Returns**
- resolved address text or `null`

---

### `Task<CursorPaginatedResult<BalanceResult[]>?> GetAccountFungibleTokensAsync(string account, string tokenSymbol = "", ulong carbonTokenId = 0, uint pageSize = 10, string cursor = "", bool checkAddressReservedByte = true)`
Gets fungible token balances owned by an address (cursor pagination)

**Parameters**
- `account` — account address
- `tokenSymbol` — token symbol filter (optional, cannot be used together with `carbonTokenId`)
- `carbonTokenId` — Carbon token id filter (optional, cannot be used together with `tokenSymbol`)
- `pageSize` — items per page
- `cursor` — cursor for the next page
- `checkAddressReservedByte` — `true` to validate address reserved byte

**Returns**
- cursor paginated balances or `null`

---

### `Task<CursorPaginatedResult<TokenDataResult[]>?> GetAccountNFTsAsync(string account, string tokenSymbol = "", ulong carbonTokenId = 0, uint carbonSeriesId = 0, uint pageSize = 10, string cursor = "", bool extended = false, bool checkAddressReservedByte = true)`
Gets NFTs owned by an address (cursor pagination)

**Parameters**
- `account` — account address
- `tokenSymbol` — token symbol filter (optional)
- `carbonTokenId` — Carbon token id filter (optional)
- `carbonSeriesId` — Carbon series id filter (optional)
- `pageSize` — items per page
- `cursor` — cursor for the next page
- `extended` — `true` to include properties
- `checkAddressReservedByte` — `true` to validate address reserved byte

**Returns**
- cursor paginated NFT data or `null`

---

### `Task<CursorPaginatedResult<TokenResult[]>?> GetAccountOwnedTokensAsync(string account, string tokenSymbol = "", ulong carbonTokenId = 0, uint pageSize = 10, string cursor = "", bool checkAddressReservedByte = true)`
Gets NFT tokens for which the account owns at least one NFT instance (cursor pagination)

**Parameters**
- `account` — account address
- `tokenSymbol` — token symbol filter (optional)
- `carbonTokenId` — Carbon token id filter (optional)
- `pageSize` — items per page
- `cursor` — cursor for the next page
- `checkAddressReservedByte` — `true` to validate address reserved byte

**Returns**
- cursor paginated token data or `null`

---

### `Task<CursorPaginatedResult<TokenSeriesResult[]>?> GetAccountOwnedTokenSeriesAsync(string account, string tokenSymbol = "", ulong carbonTokenId = 0, uint pageSize = 10, string cursor = "", bool checkAddressReservedByte = true)`
Gets NFT series for which the account owns at least one NFT instance (cursor pagination)

**Parameters**
- `account` — account address
- `tokenSymbol` — token symbol filter (optional)
- `carbonTokenId` — Carbon token id filter (optional)
- `pageSize` — items per page
- `cursor` — cursor for the next page
- `checkAddressReservedByte` — `true` to validate address reserved byte

**Returns**
- cursor paginated series data or `null`

---

## Auction

### `Task<int> GetAuctionsCountAsync(string chainAddressOrName, string symbol)`
Gets the number of auctions currently available in the market contract for a given token

**Parameters**
- `chainAddressOrName` — chain address or name
- `symbol` — token symbol

**Returns**
- auctions count as integer

---

### `Task<(AuctionResult[]? result, uint page, uint total, uint totalPages)> GetAuctionsAsync(string chainAddressOrName, string symbol, uint page, uint pageSize)`
Gets all auctions currently available in the market contract for a given token with pagination

**Parameters**
- `chainAddressOrName` — chain address or name
- `symbol` — token symbol
- `page` — page number starting at 1
- `pageSize` — items per page

**Returns**
- tuple with results array, current page, total items and total pages

---

### `Task<AuctionResult?> GetAuctionAsync(string chainAddressOrName, string symbol, string id)`
Gets a single auction by symbol and auction id

**Parameters**
- `chainAddressOrName` — chain address or name
- `symbol` — token symbol
- `id` — auction id

**Returns**
- auction data or `null`

---

## Block

### `Task<long> GetBlockHeightAsync(string chain)`
Gets the latest block height for a chain

**Parameters**
- `chain` — chain name

**Returns**
- block height as `long`

---

### `Task<int> GetBlockTransactionCountByHashAsync(string chainAddressOrName, string blockHash)`
Gets the number of transactions in a block by block hash

**Parameters**
- `chainAddressOrName` — chain address or name
- `blockHash` — block hash

**Returns**
- transaction count

---

### `Task<BlockResult?> GetBlockByHashAsync(string blockHash)`
Gets a block by its hash

**Parameters**
- `blockHash` — block hash

**Returns**
- block data or `null`

---

### `Task<BlockResult?> GetBlockByHeightAsync(string chain, long height)`
Gets a block by chain and height

**Parameters**
- `chain` — chain name
- `height` — block height

**Returns**
- block data or `null`

---

### `Task<BlockResult?> GetLatestBlockAsync(string chain)`
Gets the latest block for a chain

**Parameters**
- `chain` — chain name

**Returns**
- latest block data or `null`

---

### `Task<TransactionResult?> GetTransactionByBlockHashAndIndexAsync(string chainAddressOrName, string blockHash, int index)`
Gets a transaction by chain, block hash, and transaction index. The legacy overload `GetTransactionByBlockHashAndIndexAsync(string blockHash, int index)` is still available and defaults to the main chain.

**Parameters**
- `chainAddressOrName` — chain address or name
- `blockHash` — block hash
- `index` — transaction index within the block

**Returns**
- transaction data or `null`

---

## Chain

{% hint style="warning" %}
The current RPC source exposes these wrappers for compatibility, but the chain endpoints are still placeholders: `getChains` returns an empty array and `getChain` returns a default `ChainResult`. Do not use this section as a reliable chain-data source until the backend query implementation is completed.
{% endhint %}

### `Task<ChainResult[]?> GetChainsAsync()`
Gets an array of all chains deployed on Phantasma

**Returns**
- array of chains or `null`

---

### `Task<ChainResult?> GetChainAsync(string name = "main", bool extended = true)`
Gets chain information by name

**Parameters**
- `name` — chain name
- `extended` — `true` to include extended data

**Returns**
- chain data or `null`

---

## Contract

### `Task<ContractResult?> GetContractAsync(string contractName)`
Gets contract metadata by name from the main chain

**Parameters**
- `contractName` — contract name

**Returns**
- contract data or `null`

---

### `Task<ContractResult?> GetContractByAddressAsync(string chainAddressOrName, string contractAddress)`
Gets contract metadata by address from a specific chain

**Parameters**
- `chainAddressOrName` — chain address or name
- `contractAddress` — contract address

**Returns**
- contract data or `null`

---

### `Task<ContractResult[]?> GetContractsAsync()`
Gets all contracts deployed on the main chain

**Returns**
- array of contracts or `null`

---

## Leaderboard

{% hint style="warning" %}
The current RPC source exposes `getLeaderboard`, but the backend still returns a default `LeaderboardResult` from a placeholder query path. Do not treat this method as live leaderboard data yet.
{% endhint %}

### `Task<LeaderboardResult?> GetLeaderboardAsync(string name)`
Gets a leaderboard by name

**Parameters**
- `name` — leaderboard name

**Returns**
- leaderboard data or `null`

---

## Nexus

{% hint style="warning" %}
The current RPC source exposes `getNexus`, but the backend still returns a default `NexusResult` from a placeholder query path. Do not use it as authoritative nexus metadata yet.
{% endhint %}

### `Task<NexusResult?> GetNexusAsync()`
Gets nexus metadata including an array of all chains deployed on Phantasma

**Returns**
- nexus data or `null`

---

## Organization

{% hint style="warning" %}
The current RPC source exposes the organization endpoints, but `getOrganization` and `getOrganizationByName` return default `OrganizationResult` values, and `getOrganizations` returns an empty array. Do not use this section as reliable organization data until those backend queries are implemented.
{% endhint %}

### `Task<OrganizationResult?> GetOrganizationAsync(string id)`
Gets organization data by id

**Parameters**
- `id` — organization id

**Returns**
- organization data or `null`

---

### `Task<OrganizationResult?> GetOrganizationByNameAsync(string name)`
Gets organization data by name

**Parameters**
- `name` — organization name

**Returns**
- organization data or `null`

---

### `Task<OrganizationResult[]?> GetOrganizationsAsync()`
Gets all organizations deployed on Phantasma

**Returns**
- array of organizations or `null`

---

## Token

### `Task<TokenResult?> GetTokenAsync(string symbol)`
Gets token metadata by symbol

**Parameters**
- `symbol` — token symbol

**Returns**
- token data or `null`

---

### `Task<TokenResult?> GetTokenAsync(string symbol, bool extended, ulong carbonTokenId)`
Gets token metadata by symbol or Carbon token id

**Parameters**
- `symbol` — token symbol (optional when using `carbonTokenId`)
- `extended` — `true` to include extended data
- `carbonTokenId` — Carbon token id (optional when using `symbol`)

**Returns**
- token data or `null`

---

### `Task<TokenResult[]?> GetTokensAsync()`
Gets an array of all tokens deployed on Phantasma

**Returns**
- array of token metadata or `null`

---

### `Task<TokenResult[]?> GetTokensAsync(bool extended, string? ownerAddress = null)`
Gets an array of all tokens deployed on Phantasma with optional owner filtering

**Parameters**
- `extended` — `true` to include extended data
- `ownerAddress` — optional owner address filter

**Returns**
- array of token metadata or `null`

---

### `Task<CursorPaginatedResult<TokenSeriesResult[]>?> GetTokenSeriesAsync(string symbol = "", ulong carbonTokenId = 0, uint pageSize = 10, string cursor = "")`
Gets token series for a token (cursor pagination)

**Parameters**
- `symbol` — token symbol (optional when using `carbonTokenId`)
- `carbonTokenId` — Carbon token id (optional when using `symbol`)
- `pageSize` — items per page
- `cursor` — cursor for the next page

**Returns**
- cursor paginated series data or `null`

---

### `Task<TokenSeriesResult?> GetTokenSeriesByIdAsync(string symbol = "", ulong carbonTokenId = 0, string seriesId = "", uint carbonSeriesId = 0)`
Gets one token series by Phantasma or Carbon identifiers

**Parameters**
- `symbol` — token symbol (optional when using `carbonTokenId`)
- `carbonTokenId` — Carbon token id (optional when using `symbol`)
- `seriesId` — Phantasma series id (optional when using `carbonSeriesId`)
- `carbonSeriesId` — Carbon series id (optional when using `seriesId`)

**Returns**
- token series data or `null`

---

### `Task<CursorPaginatedResult<TokenDataResult[]>?> GetTokenNFTsAsync(ulong carbonTokenId, uint carbonSeriesId = 0, uint pageSize = 10, string cursor = "", bool extended = false, string seriesId = "")`
Gets NFTs for a token (cursor pagination)

**Parameters**
- `carbonTokenId` — Carbon token id
- `carbonSeriesId` — Carbon series id filter (optional)
- `pageSize` — items per page
- `cursor` — cursor for the next page
- `extended` — `true` to include properties
- `seriesId` — Phantasma series id filter (optional)

**Returns**
- cursor paginated NFT data or `null`

---

### `Task<BalanceResult?> GetTokenBalanceAsync(string address, string symbol, string chain = "main")`
Gets the token balance for a given address and token symbol

**Parameters**
- `address` — account address
- `symbol` — token symbol
- `chain` — chain name, default `main`

**Returns**
- balance data or `null`

---

### `Task<BalanceResult?> GetTokenBalanceAsync(string address, string symbol, string chain, bool checkAddressReservedByte, RpcAddressType addressType)`
Gets the token balance for a given address, token symbol, and address encoding.

**Parameters**
- `address` — account address text
- `symbol` — token symbol
- `chain` — chain name
- `checkAddressReservedByte` — `true` to validate the address reserved byte
- `addressType` — account address encoding expected by the RPC

**Returns**
- balance data or `null`

---

### `Task<TokenDataResult?> GetTokenDataAsync(string symbol, string tokenId)`
Gets token data for a specific token id

**Parameters**
- `symbol` — token symbol
- `tokenId` — token id

**Returns**
- token data or `null`

**Notes**
- On current Carbon nodes this is a deprecated alias for `GetNFTAsync(symbol, tokenId, loadProperties: false)`.

---

### `Task<TokenDataResult?> GetNFTAsync(string symbol, string tokenId, bool loadProperties)`
Gets NFT data and optionally loads properties

**Parameters**
- `symbol` — NFT symbol
- `tokenId` — token id
- `loadProperties` — `true` to load properties

**Returns**
- NFT data or `null`

---

### `Task<TokenDataResult[]?> GetNFTsAsync(string symbol, IEnumerable<string> tokenIds, bool extended = false)`
Gets NFT data for multiple token ids

**Parameters**
- `symbol` — NFT symbol
- `tokenIds` — token ids
- `extended` — `true` to load properties

**Returns**
- array of NFT data or `null`

---

## Transactions

### `Task<(AccountTransactionsResult? result, uint page, uint totalPages)> GetAddressTransactionsAsync(string address, uint page, uint pageSize)`
Gets address transactions with pagination

**Parameters**
- `address` — account address
- `page` — page number starting at 1
- `pageSize` — items per page

**Returns**
- tuple with result object, current page, total pages

---

### `Task<int> GetAddressTransactionCountAsync(string address, string chain)`
Gets the number of transactions for an address on a chain

**Parameters**
- `address` — account address
- `chain` — chain name

**Returns**
- total number of transactions

---

### `Task<TransactionResult?> GetTransactionAsync(string txHash)`
Gets a transaction by its hash if available

**Parameters**
- `txHash` — transaction hash

**Returns**
- transaction data or `null`

---

### `Task<string?> SendRawTransactionAsync(string txData)`
Broadcasts a transaction in hexadecimal encoding

**Parameters**
- `txData` — hex encoded transaction bytes

**Returns**
- transaction hash text or `null`

---

### `Task<string?> SendCarbonTransactionAsync(string txData)`
Broadcasts a Carbon transaction in hexadecimal encoding

**Parameters**
- `txData` — hex encoded Carbon transaction bytes

**Returns**
- transaction hash text or `null`

---

### `Task<ScriptResult?> InvokeRawScriptAsync(string chain, string scriptData)`
Invokes a VM script without state changes and returns its result

**Parameters**
- `chain` — chain name
- `scriptData` — hex encoded script bytes

**Returns**
- script invocation result or `null`

---

### `Task<string?> SignAndSendCarbonTransactionAsync(IKeyPair keys, TxMsg txMsg)`
Signs, serializes, and broadcasts a Carbon transaction

**Parameters**
- `keys` — key pair used to sign the Carbon transaction
- `txMsg` — Carbon `TxMsg` struct

**Returns**
- transaction hash text or `null`

---

### `Task<string?> SignAndSendTransactionAsync(IKeyPair keys, string nexus, byte[] script, string chain, string payload, Func<byte[], byte[], byte[], byte[]>? customSignFunction = null)`
Builds, signs and broadcasts a transaction with a UTF8 payload

**Parameters**
- `keys` — key pair used to sign a transaction
- `nexus` — nexus name
- `script` — transaction script bytes
- `chain` — target chain name
- `payload` — UTF8 payload string
- `customSignFunction` — optional custom signer that receives data, script and payload bytes

**Returns**
- transaction hash text or `null`

**Exceptions**
- throws `Exception` when the hash returned by RPC does not match the locally computed hash

---

### `Task<string?> SignAndSendTransactionAsync(IKeyPair keys, string nexus, byte[] script, string chain, byte[] payload, Func<byte[], byte[], byte[], byte[]>? customSignFunction = null)`
Builds, signs and broadcasts a transaction with a binary payload

**Parameters**
- `keys` — key pair used to sign a transaction
- `nexus` — nexus name
- `script` — transaction script bytes
- `chain` — target chain name
- `payload` — binary payload bytes
- `customSignFunction` — optional custom signer that receives data, script and payload bytes

**Returns**
- transaction hash text or `null`

**Behavior**
- Transaction expiration is set to `DateTime.UtcNow + 20 minutes`
- The transaction is signed and sent as hex using `SendRawTransactionAsync`
- If the hash returned by RPC differs from the locally computed hash an `Exception` is thrown

---

## Storage

{% hint style="warning" %}
The current RPC source exposes the archive endpoints, but this storage section is still placeholder-backed: `getArchive` returns a default `ArchiveResult`, `writeArchive` returns `false`, and `readArchive` returns an empty string. Do not use these methods as working archive storage flows yet.
{% endhint %}

### `Task<ArchiveResult?> GetArchiveAsync(string hash)`
Gets archive metadata by its hash

**Parameters**
- `hash` — archive hash

**Returns**
- archive data or `null`

---

### `Task<bool> WriteArchiveAsync(string hash, int blockIndex, byte[] blockContent)`
Writes a single archive block

**Parameters**
- `hash` — archive hash
- `blockIndex` — block index
- `blockContent` — block content bytes

**Returns**
- `true` if the write succeeded

---

### `Task<string?> ReadArchiveAsync(string hash, int blockIndex)`
Reads a single archive block as a base64 string

**Parameters**
- `hash` — archive hash
- `blockIndex` — block index

**Returns**
- base64 block content or `null`

---

## Validation helpers

### `static bool IsValidPrivateKey(string key)`
Validates a WIF‑formatted private key string

**Parameters**
- `key` — WIF string

**Returns**
- `true` if the key format looks valid

**Heuristics**
- must start with `L` or `K` and have length 52

---

### `static bool IsValidAddress(string address)`
Validates the format of a Phantasma address string

**Parameters**
- `address` — address text

**Returns**
- `true` if the address format looks valid

**Heuristics**
- must start with `P` and have length 45
