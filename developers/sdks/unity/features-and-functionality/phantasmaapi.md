# ☁️ PhantasmaAPI

`PhantasmaAPI` is the Unity SDK RPC client for reading chain data and broadcasting transactions. All RPC calls are coroutines (`IEnumerator`) and are meant to be executed via `StartCoroutine(...)`.

#### Variables

* `public readonly string Host;`: The RPC host URL (for example, `https://testnet.phantasma.info/rpc`).

#### Constructor

* `public PhantasmaAPI(string host);`: Initializes a new `PhantasmaAPI` instance with the specified RPC host.

#### Method Notes

* All RPC methods accept an optional `Action<EPHANTASMA_SDK_ERROR_TYPE, string> errorHandlingCallback` plus optional `timeout` and `retries` arguments.
* Some RPC endpoints may be disabled on public nodes; check the roadmap if you receive server-side errors.

#### Methods

**Account**

* `public IEnumerator GetAccount(string addressText, Action<AccountResult> callback, ...);`
* `public IEnumerator GetAccounts(string[] addresses, Action<AccountResult[]> callback, ...);`
* `public IEnumerator LookUpName(string name, Action<string> callback, ...);`

**Auction**

* `public IEnumerator GetAuctionsCount(string chainAddressOrName, string symbol, Action<int> callback, ...);`
* `public IEnumerator GetAuctions(string chainAddressOrName, string symbol, uint page, uint pageSize, Action<AuctionResult[], uint, uint, uint> callback, ...);`
* `public IEnumerator GetAuction(string chainAddressOrName, string symbol, string IDtext, Action<AuctionResult> callback, ...);`

**Block**

* `public IEnumerator GetBlockHeight(string chainInput, Action<long> callback, ...);`
* `public IEnumerator GetBlockTransactionCountByHash(string blockHash, Action<int> callback, ...);`
* `public IEnumerator GetBlockByHash(string blockHash, Action<BlockResult> callback, ...);`
* `public IEnumerator GetBlockByHeight(string chainInput, long height, Action<BlockResult> callback, ...);`
* `public IEnumerator GetLatestBlock(string chainInput, Action<BlockResult> callback, ...);`
* `public IEnumerator GetTransactionByBlockHashAndIndex(string blockHash, int index, Action<TransactionResult> callback, ...);`

**Chain**

* `public IEnumerator GetChains(Action<ChainResult[]> callback, ...);`

**Contract**

* `public IEnumerator GetContract(string contractName, Action<ContractResult> callback, ...);`
* `public IEnumerator GetContracts(Action<ContractResult[]> callback, ...);`

**Leaderboard**

* `public IEnumerator GetLeaderboard(string name, Action<LeaderboardResult> callback, ...);`

**Nexus**

* `public IEnumerator GetNexus(Action<NexusResult> callback, ...);`

**Organization**

* `public IEnumerator GetOrganization(string ID, Action<OrganizationResult> callback, ...);`
* `public IEnumerator GetOrganizationByName(string name, Action<OrganizationResult> callback, ...);`
* `public IEnumerator GetOrganizations(Action<OrganizationResult[]> callback, ...);`

**Token**

* `public IEnumerator GetToken(string symbol, Action<TokenResult> callback, ...);`
* `public IEnumerator GetTokens(Action<TokenResult[]> callback, ...);`
* `public IEnumerator GetTokenData(string symbol, string IDtext, Action<TokenDataResult> callback, ...);`
* `public IEnumerator GetNFT(string symbol, string IDtext, bool loadProperties, Action<TokenDataResult> callback, ...);`
* `public IEnumerator GetNFTs(string symbol, string[] IDtext, Action<TokenDataResult[]> callback, ...);`
* `public IEnumerator GetTokenBalance(string account, string tokenSymbol, string chainInput = "main", Action<BalanceResult> callback = null, ...);`

**Transaction**

* `public IEnumerator GetAddressTransactions(string addressText, uint page, uint pageSize, Action<AccountTransactionsResult, uint, uint> callback, ...);`
* `public IEnumerator GetAddressTransactionCount(string addressText, string chainInput, Action<int> callback, ...);`
* `public IEnumerator SendRawTransaction(string txData, Hash txHash, Action<string, string, Hash> callback, ...);`
* `public IEnumerator SendCarbonTransaction(string txData, Action<string, string> callback, ...);`
* `public IEnumerator InvokeRawScript(string chainInput, string scriptData, Action<ScriptResult> callback, ...);`
* `public IEnumerator GetTransaction(string hashText, Action<TransactionResult> callback, ...);`

**Storage**

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
