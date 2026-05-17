# ☁️ PhantasmaAPI

`PhantasmaAPI` is the Unity SDK RPC client for reading chain data and broadcasting transactions. All RPC calls are coroutines (`IEnumerator`) and are meant to be executed via `StartCoroutine(...)`.

#### Variables

* `public readonly string Host;`: The RPC host URL (for example, `https://testnet.phantasma.info/rpc`).

#### Constructor

* `public PhantasmaAPI(string host);`: Initializes a new `PhantasmaAPI` instance with the specified RPC host.

#### Method Notes

* All RPC methods accept an optional `Action<EPHANTASMA_SDK_ERROR_TYPE, string> errorHandlingCallback` plus optional `timeout` and `retries` arguments.
* Some block-hash methods provide both main-chain defaults and explicit `chainAddressOrName` overloads. In the cited Unity SDK source baseline, `GetTransactionByBlockHashAndIndex` only exposes the main-chain overload.
* The Unity wrappers for Chain, Leaderboard, Nexus, Organization, and Storage exist, but the current RPC backend still returns stubbed/default data for those endpoint groups.

#### Methods

**Account**

* `public IEnumerator GetAccount(string addressText, Action<AccountResult> callback, ...);`
* `public IEnumerator GetAccount(string addressText, bool extended, bool checkAddressReservedByte, RpcAddressType addressType, Action<AccountResult> callback, ...);`
* `public IEnumerator GetAccounts(string[] addresses, Action<AccountResult[]> callback, ...);`
* `public IEnumerator GetAccounts(string[] addresses, bool extended, bool checkAddressReservedByte, RpcAddressType addressType, Action<AccountResult[]> callback, ...);`
* `public IEnumerator GetAccountFungibleTokens(string account, string tokenSymbol, ulong carbonTokenId, uint pageSize, string cursor, bool checkAddressReservedByte, Action<CursorPaginatedResult<BalanceResult[]>> callback, ...);`
* `public IEnumerator GetAccountNFTs(string account, string tokenSymbol, ulong carbonTokenId, uint carbonSeriesId, uint pageSize, string cursor, bool extended, bool checkAddressReservedByte, Action<CursorPaginatedResult<TokenDataResult[]>> callback, ...);`
* `public IEnumerator GetAccountOwnedTokens(string account, string tokenSymbol, ulong carbonTokenId, uint pageSize, string cursor, bool checkAddressReservedByte, Action<CursorPaginatedResult<TokenResult[]>> callback, ...);`
* `public IEnumerator GetAccountOwnedTokenSeries(string account, string tokenSymbol, ulong carbonTokenId, uint pageSize, string cursor, bool checkAddressReservedByte, Action<CursorPaginatedResult<TokenSeriesResult[]>> callback, ...);`
* `public IEnumerator LookUpName(string name, Action<string> callback, ...);`

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

Current backend status: stubbed organization queries; single-organization calls return default results and the list call returns an empty array.

* `public IEnumerator GetOrganization(string ID, Action<OrganizationResult> callback, ...);`
* `public IEnumerator GetOrganizationByName(string name, Action<OrganizationResult> callback, ...);`
* `public IEnumerator GetOrganizations(Action<OrganizationResult[]> callback, ...);`

**Token**

* `public IEnumerator GetToken(string symbol, Action<TokenResult> callback, ...);`
* `public IEnumerator GetTokens(Action<TokenResult[]> callback, ...);`
* `public IEnumerator GetTokenSeries(string symbol, ulong carbonTokenId, uint pageSize, string cursor, Action<CursorPaginatedResult<TokenSeriesResult[]>> callback, ...);`
* `public IEnumerator GetTokenSeriesById(string symbol, ulong carbonTokenId, string seriesId, uint carbonSeriesId, Action<TokenSeriesResult> callback, ...);`
* `public IEnumerator GetTokenNFTs(ulong carbonTokenId, uint carbonSeriesId, uint pageSize, string cursor, bool extended, string seriesId, Action<CursorPaginatedResult<TokenDataResult[]>> callback, ...);`
* `public IEnumerator GetTokenData(string symbol, string IDtext, Action<TokenDataResult> callback, ...);`
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

**Storage**

Current backend status: stubbed archive storage queries; archive metadata returns a default result, writes return `false`, and reads return an empty string.

* `public IEnumerator GetArchive(string hashText, Action<ArchiveResult> callback, ...);`
* `public IEnumerator WriteArchive(string hashText, int blockIndex, byte[] blockContent, Action<Boolean> callback, ...);`
* `public IEnumerator ReadArchive(string hashText, int blockIndex, Action<string> callback, ...);`

**Signing Helpers**

* `public IEnumerator SignAndSendTransaction(IKeyPair keys, string nexus, byte[] script, string chain, string payload, Action<string, string> callback, ...);`
* `public IEnumerator SignAndSendTransaction(IKeyPair keys, string nexus, byte[] script, string chain, byte[] payload, Action<string, string> callback, Action<EPHANTASMA_SDK_ERROR_TYPE, string> errorHandlingCallback = null, Func<byte[], byte[], byte[], byte[]> customSignFunction = null, ...);`
* `public IEnumerator SignAndSendCarbonTransaction(IKeyPair keys, TxMsg txMsg, Action<string, string> callback, ...);`

**Validation**

* `public static bool IsValidPrivateKey(string key);`
* `public static bool IsValidAddress(string address);`
