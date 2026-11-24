---
title: "☁️ PhantasmaAPI"
linkTitle: "Phantasma API"
weight: 30
---

`PhantasmaAPI` is the Unity SDK RPC client for reading chain data and broadcasting transactions. All RPC calls are coroutines (`IEnumerator`) and are meant to be executed via `StartCoroutine(...)`.

#### Variables

* `public readonly string Host;`: The RPC host URL (for example, `https://testnet.phantasma.info/rpc`).
* `public readonly string ApiKey;`: Optional API key sent in the `X-Api-Key` header on every RPC request.

#### Constructor

* `public PhantasmaAPI(string host, string apiKey = null);`: Initializes a new `PhantasmaAPI` instance with the specified RPC host and optional API key.

#### Method Notes

* All RPC methods accept an optional `Action<EPHANTASMA_SDK_ERROR_TYPE, string> errorHandlingCallback` plus optional `timeout` and `retries` arguments.
* Block-hash methods provide both main-chain defaults and explicit `chainAddressOrName` overloads for transaction counts and transaction-by-block-position reads.
* The node stubs the Chain, Leaderboard, Nexus and Storage endpoints and returns default data for them.

#### Methods

**Account**

* `public IEnumerator GetAccountInfo(string addressText, Action<AccountInfoResult> callback, ...);`
* `public IEnumerator GetAccountInfo(string addressText, bool checkAddressReservedByte, RpcAddressType addressType, Action<AccountInfoResult> callback, ...);`
* `public IEnumerator GetAccountInfos(string[] addresses, Action<AccountInfoResult[]> callback, ...);`
* `public IEnumerator GetAccountInfos(string[] addresses, bool checkAddressReservedByte, RpcAddressType addressType, Action<AccountInfoResult[]> callback, ...);`
* `public IEnumerator GetAccount(string addressText, Action<AccountResult> callback, ...);`
* `public IEnumerator GetAccount(string addressText, bool extended, bool checkAddressReservedByte, RpcAddressType addressType, Action<AccountResult> callback, ...);`
* `public IEnumerator GetAccounts(string[] addresses, Action<AccountResult[]> callback, ...);`
* `public IEnumerator GetAccounts(string[] addresses, bool extended, bool checkAddressReservedByte, RpcAddressType addressType, Action<AccountResult[]> callback, ...);`
* `public IEnumerator GetAccountFungibleTokens(string account, string tokenSymbol, ulong carbonTokenId, uint pageSize, string cursor, bool checkAddressReservedByte, Action<CursorPaginatedResult<BalanceResult[]>> callback, ...);`
* `public IEnumerator GetAccountNFTs(string account, string tokenSymbol, ulong carbonTokenId, uint carbonSeriesId, uint pageSize, string cursor, bool extended, bool checkAddressReservedByte, Action<CursorPaginatedResult<TokenDataResult[]>> callback, ...);`
* `public IEnumerator GetAccountOwnedTokens(string account, string tokenSymbol, ulong carbonTokenId, uint pageSize, string cursor, bool checkAddressReservedByte, Action<CursorPaginatedResult<TokenResult[]>> callback, ...);`
* `public IEnumerator GetAccountOwnedTokenSeries(string account, string tokenSymbol, ulong carbonTokenId, uint pageSize, string cursor, bool checkAddressReservedByte, Action<CursorPaginatedResult<TokenSeriesResult[]>> callback, ...);`
* `public IEnumerator LookUpName(string name, Action<string> callback, ...);`

`GetAccountInfo` returns the account name and the staking info. Its cost does
not depend on how much the address holds, which makes it the call for a refresh
loop. `GetAccountInfos` answers up to 100 addresses from one state snapshot.

`GetAccount` and `GetAccounts` are obsolete. Their response embeds every NFT id
the address owns, and the node caps each `Balances[].Ids` list at 10000 entries
while `Balances[].Amount` keeps the true count. Read balances and NFTs through
the cursor methods instead.

**Auction**

* `public IEnumerator GetAuctionsCount(string chainAddressOrName, string symbol, Action<int> callback, ...);`
* `public IEnumerator GetAuctions(string chainAddressOrName, string symbol, uint page, uint pageSize, Action<AuctionResult[], uint, uint, uint> callback, ...);`
* `public IEnumerator GetAuction(string chainAddressOrName, string symbol, string IDtext, Action<AuctionResult> callback, ...);`

**Block**

* `public IEnumerator GetBlockHeight(string chainInput, Action<long> callback, ...);`
* `public IEnumerator GetBlockTransactionCountByHash(string blockHash, Action<int> callback, ...);`
* `public IEnumerator GetBlockTransactionCountByHash(string chainAddressOrName, string blockHash, Action<int> callback, ...);`
* `public IEnumerator GetBlockByHash(string blockHash, Action<BlockResult> callback, ...);`
* `public IEnumerator GetBlockByHeight(string chainInput, long height, Action<BlockResult> callback, ...);`
* `public IEnumerator GetLatestBlock(string chainInput, Action<BlockResult> callback, ...);`
* `public IEnumerator GetTransactionByBlockHashAndIndex(string blockHash, int index, Action<TransactionResult> callback, ...);`
* `public IEnumerator GetTransactionByBlockHashAndIndex(string chainAddressOrName, string blockHash, int index, Action<TransactionResult> callback, ...);`

**Chain**

Current backend status: stubbed chain query; `GetChains` returns an empty array.

* `public IEnumerator GetChains(Action<ChainResult[]> callback, ...);`

**Contract**

* `public IEnumerator GetContract(string contractName, Action<ContractResult> callback, ...);`
* `public IEnumerator GetContracts(Action<ContractResult[]> callback, ...);`

**Leaderboard**

Current backend status: stubbed leaderboard query; `GetLeaderboard` returns a default result.

* `public IEnumerator GetLeaderboard(string name, Action<LeaderboardResult> callback, ...);`

**Nexus**

Current backend status: stubbed nexus query; `GetNexus` returns a default result.

* `public IEnumerator GetNexus(Action<NexusResult> callback, ...);`

**Organization**

* `public IEnumerator GetOrganization(string name, bool includeMemberCount, Action<OrganizationResult> callback, ...);`
* `public IEnumerator GetOrganizations(uint pageSize, string cursor, bool includeMemberCount, Action<CursorPaginatedResult<OrganizationResult[]>> callback, ...);`
* `public IEnumerator GetOrganizationMembers(string name, uint pageSize, string cursor, bool includeMemberTime, Action<CursorPaginatedResult<OrganizationMemberResult[]>> callback, ...);`
* `public IEnumerator GetOrganizationMember(string name, string address, bool checkAddressReservedByte, RpcAddressType addressType, Action<OrganizationMemberResult> callback, ...);`

**Token**

* `public IEnumerator GetToken(string symbol, Action<TokenResult> callback, ...);`
* `public IEnumerator GetTokens(Action<TokenResult[]> callback, ...);`
* `public IEnumerator GetTokenSeries(string symbol, ulong carbonTokenId, uint pageSize, string cursor, Action<CursorPaginatedResult<TokenSeriesResult[]>> callback, ...);`
* `public IEnumerator GetTokenSeriesById(string symbol, ulong carbonTokenId, string seriesId, uint carbonSeriesId, Action<TokenSeriesResult> callback, ...);`
* `public IEnumerator GetTokenNFTs(ulong carbonTokenId, uint carbonSeriesId, uint pageSize, string cursor, bool extended, string seriesId, Action<CursorPaginatedResult<TokenDataResult[]>> callback, ...);`
* `public IEnumerator GetTokenData(string symbol, string IDtext, Action<TokenDataResult> callback, ...);` Deprecated, `GetNFT` covers it entirely.
* `public IEnumerator GetNFT(string symbol, string IDtext, bool loadProperties, Action<TokenDataResult> callback, ...);`
* `public IEnumerator GetNFTs(string symbol, string[] IDtext, Action<TokenDataResult[]> callback, ...);`
* `public IEnumerator GetTokenBalance(string account, string tokenSymbol, string chainInput = "main", Action<BalanceResult> callback = null, ...);`
* `public IEnumerator GetTokenBalance(string account, string tokenSymbol, string chainInput, bool checkAddressReservedByte, RpcAddressType addressType, Action<BalanceResult> callback = null, ...);`

**Transaction**

* `public IEnumerator GetAddressTransactions(string addressText, uint page, uint pageSize, Action<AccountTransactionsResult, uint, uint> callback, ...);`
* `public IEnumerator GetAddressTransactionCount(string addressText, string chainInput, Action<int> callback, ...);`
* `public IEnumerator SendRawTransaction(string txData, Hash txHash, Action<string, string, Hash> callback, ...);`
* `public IEnumerator SendCarbonTransaction(string txData, Action<string, string> callback, ...);`
* `public IEnumerator InvokeRawScript(string chainInput, string scriptData, Action<ScriptResult> callback, ...);`
* `public IEnumerator GetTransaction(string hashText, Action<TransactionResult> callback, ...);`

**Fees**

* `public IEnumerator GetGasConfig(Action<GasConfigResult> callback, ...);`
* `public IEnumerator EstimateTransaction(string txData, Action<EstimateTransactionResult> callback, ...);`

`GetGasConfig` returns the on-chain gas configuration and the chain parameters
fee estimation needs. It changes only through a governance resolution, so the
result is safe to cache.

`EstimateTransaction` dry-runs a serialized envelope against current chain
state. A node with the estimate service switched off answers a standard RPC error.

**Storage**

Current backend status: stubbed archive storage queries; archive metadata returns a default result, writes return `false`, and reads return an empty string.

* `public IEnumerator GetArchive(string hashText, Action<ArchiveResult> callback, ...);`
* `public IEnumerator WriteArchive(string hashText, int blockIndex, byte[] blockContent, Action<Boolean> callback, ...);`
* `public IEnumerator ReadArchive(string hashText, int blockIndex, Action<string> callback, ...);`

**Signing Helpers**

* `public IEnumerator SignAndSendTransaction(IKeyPair keys, string nexus, byte[] script, string chain, string payload, Action<string, string> callback, Action<EPHANTASMA_SDK_ERROR_TYPE, string> errorHandlingCallback = null, int timeout = WebClient.DefaultTimeout, int retries = WebClient.DefaultRetries, Timestamp? expiration = null);`
* `public IEnumerator SignAndSendTransaction(IKeyPair keys, string nexus, byte[] script, string chain, byte[] payload, Action<string, string> callback, Action<EPHANTASMA_SDK_ERROR_TYPE, string> errorHandlingCallback = null, Func<byte[], byte[], byte[], byte[]> customSignFunction = null, int timeout = WebClient.DefaultTimeout, int retries = WebClient.DefaultRetries, Timestamp? expiration = null);` Without `expiration` the transaction expires `TxLimits.DefaultExpiryMs` (45 seconds) after it is built.
* `public IEnumerator SignAndSendCarbonTransaction(IKeyPair keys, TxMsg txMsg, Action<string, string> callback, ...);`
* `public IEnumerator SignAndSendCarbonTransaction(IKeyPair[] keys, TxMsg txMsg, PlanAndSignOptions options, Action<string, string> callback, Action<EPHANTASMA_SDK_ERROR_TYPE, string> errorHandlingCallback = null, bool preflight = true, ...);`
* `public IEnumerator PlanCarbonTransaction(IKeyPair[] keys, TxMsg txMsg, PlanAndSignOptions options, Action<FeePlan> callback, ...);`

`SignAndSendCarbonTransaction` plans the fee, signs and broadcasts in one call.
`PlanCarbonTransaction` prices a message and signs nothing, so a game can show
the cost before it asks the player to confirm.

- [Carbon Transactions And Fees](../carbon-transactions.md)

**Validation**

* `public static bool IsValidPrivateKey(string key);` checks the WIF shape (`L` or `K` prefix, length 52). Validate addresses with `PhantasmaPhoenix.Cryptography.Address.IsValidAddress(text)`.
