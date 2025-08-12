# High level API for interacting with Phantasma chain

Plain .NET RPC wrapper for the Phantasma API using `RpcClient` with `async` / `await`

> **Note**  
> Some RPC endpoints are temporarily unavailable or partially implemented as noted below and will follow the project roadmap: https://phantasma.info/blockchain#roadmap

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

## Auction

{% hint style="warning" %}
This functionality is currently disabled and will be re‑enabled according to the [roadmap](https://phantasma.info/blockchain#roadmap)
{% endhint %}

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

### `Task<int> GetBlockTransactionCountByHashAsync(string blockHash)`
Gets the number of transactions in a block by block hash

**Parameters**
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

### `Task<TransactionResult?> GetTransactionByBlockHashAndIndexAsync(string blockHash, int index)`
Gets a transaction by block hash and transaction index

**Parameters**
- `blockHash` — block hash
- `index` — transaction index within the block

**Returns**
- transaction data or `null`

---

## Chain

{% hint style="warning" %}
This functionality is currently disabled and will be re‑enabled according to the [roadmap](https://phantasma.info/blockchain#roadmap)
{% endhint %}

### `Task<ChainResult[]?> GetChainsAsync()`
Gets an array of all chains deployed on Phantasma

**Returns**
- array of chains or `null`

---

## Contract

{% hint style="warning" %}
This functionality is currently disabled and will be re‑enabled according to the [roadmap](https://phantasma.info/blockchain#roadmap)
{% endhint %}

### `Task<ContractResult?> GetContractAsync(string contractName)`
Gets contract metadata by name from the main chain

**Parameters**
- `contractName` — contract name

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
This functionality is currently disabled and will be re‑enabled according to the [roadmap](https://phantasma.info/blockchain#roadmap)
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
This functionality is currently disabled and will be re‑enabled according to the [roadmap](https://phantasma.info/blockchain#roadmap)
{% endhint %}

### `Task<NexusResult?> GetNexusAsync()`
Gets nexus metadata including an array of all chains deployed on Phantasma

**Returns**
- nexus data or `null`

---

## Organization

{% hint style="warning" %}
This functionality is currently disabled and will be re‑enabled according to the [roadmap](https://phantasma.info/blockchain#roadmap)
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

### `Task<TokenResult[]?> GetTokensAsync()`
Gets an array of all tokens deployed on Phantasma

**Returns**
- array of token metadata or `null`

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

### `Task<TokenDataResult?> GetTokenDataAsync(string symbol, string tokenId)`
Gets token data for a specific token id

{% hint style="warning" %}
**Partially implemented** - some features may be missing or incomplete. See the [roadmap](https://phantasma.info/blockchain#roadmap)
{% endhint %}

**Parameters**
- `symbol` — token symbol
- `tokenId` — token id

**Returns**
- token data or `null`

---

### `Task<TokenDataResult?> GetNFTAsync(string symbol, string tokenId, bool loadProperties)`
Gets NFT data and optionally loads properties

{% hint style="warning" %}
**Partially implemented** - some features may be missing or incomplete. See the [roadmap](https://phantasma.info/blockchain#roadmap)
{% endhint %}

**Parameters**
- `symbol` — NFT symbol
- `tokenId` — token id
- `loadProperties` — `true` to load properties

**Returns**
- NFT data or `null`

---

### `Task<TokenDataResult[]?> GetNFTsAsync(string symbol, string[] tokenIds)`
Gets NFT data for multiple token ids

{% hint style="warning" %}
This functionality is currently disabled and will be re‑enabled according to the [roadmap](https://phantasma.info/blockchain#roadmap)
{% endhint %}

**Parameters**
- `symbol` — NFT symbol
- `tokenIds` — array of token ids

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

### `Task<ScriptResult?> InvokeRawScriptAsync(string chain, string scriptData)`
Invokes a VM script without state changes and returns its result

{% hint style="warning" %}
This functionality is currently disabled and will be re‑enabled according to the [roadmap](https://phantasma.info/blockchain#roadmap)
{% endhint %}

**Parameters**
- `chain` — chain name
- `scriptData` — hex encoded script bytes

**Returns**
- script invocation result or `null`

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
This functionality is currently disabled and will be re‑enabled according to the [roadmap](https://phantasma.info/blockchain#roadmap)
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
