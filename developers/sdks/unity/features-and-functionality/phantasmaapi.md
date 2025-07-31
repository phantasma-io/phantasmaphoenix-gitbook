# ☁️ PhantasmaAPI

`PhantasmaAPI` is a class in the Unity SDK that provides an abstraction layer for making API calls and requests to the Phantasma blockchain for fetching data.

#### Variables

* `public readonly string Host;`: The host URL of the Phantasma API.

#### Constructor

* `public PhantasmaAPI(string host);`: Initializes a new PhantasmaAPI instance with the specified host URL.

#### Methods

* `public IEnumerator GetAccount(string addressText, Action<Account> callback, Action<EPHANTASMA_SDK_ERROR_TYPE, string> errorHandlingCallback = null);`: Retrieves account details for a given address.
* `public IEnumerator GetAccounts(string[] addresses, Action<Account[]> callback, Action<EPHANTASMA_SDK_ERROR_TYPE, string> errorHandlingCallback = null);`: Retrieves account details for an array of addresses.
* `public IEnumerator LookUpName(string name, Action<string> callback, Action<EPHANTASMA_SDK_ERROR_TYPE, string> errorHandlingCallback = null);`: Retrieves an address associated with a registered name.
* `public IEnumerator GetAuctionsCount(string chainAddressOrName, string symbol, Action<int> callback, Action<EPHANTASMA_SDK_ERROR_TYPE, string> errorHandlingCallback = null);`: Retrieves the count of active auctions for a specific token symbol on a given chain.
* `public IEnumerator GetAuctions(string chainAddressOrName, string symbol, uint page, uint pageSize, Action<Auction[], int, int, int> callback, Action<EPHANTASMA_SDK_ERROR_TYPE, string> errorHandlingCallback = null);`: Retrieves a list of active auctions for a specific token symbol on a given chain, with pagination.
* `public IEnumerator GetAuction(string chainAddressOrName, string symbol, string IDtext, Action<Auction> callback, Action<EPHANTASMA_SDK_ERROR_TYPE, string> errorHandlingCallback = null);`: Retrieves an auction by its ID for a specific token symbol on a given chain.
* `public IEnumerator GetBlockHeight(string chainInput, Action<int> callback, Action<EPHANTASMA_SDK_ERROR_TYPE, string> errorHandlingCallback = null);`: Retrieves the current block height for a given chain.
* `public IEnumerator GetBlockTransactionCountByHash(string blockHash, Action<int> callback, Action<EPHANTASMA_SDK_ERROR_TYPE, string> errorHandlingCallback = null);`: Retrieves the transaction count for a block, given its hash.
* `public IEnumerator GetBlockByHash(string blockHash, Action<Block> callback, Action<EPHANTASMA_SDK_ERROR_TYPE, string> errorHandlingCallback = null);`: Retrieves a block by its hash.
* `public IEnumerator GetRawBlockByHash(string blockHash, Action<string> callback, Action<EPHANTASMA_SDK_ERROR_TYPE, string> errorHandlingCallback = null);`: Retrieves the raw block data as a string, given a block hash.
* `public IEnumerator GetBlockByHeight(string chainInput, uint height, Action<Block> callback, Action<EPHANTASMA_SDK_ERROR_TYPE, string> errorHandlingCallback = null);`: Retrieves a block by its height on a given chain.
* `public IEnumerator GetRawBlockByHeight(string chainInput, uint height, Action<string> callback, Action<EPHANTASMA_SDK_ERROR_TYPE, string> errorHandlingCallback = null);`: Retrieves the raw block data as a string, given a block height on a specified chain.
*   `public IEnumerator GetLatestBlock(string chainInput, Action<Block> callback, Action<EPHANTASMA_SDK_ERROR_TYPE, string> errorHandlingCallback = null);`: Retrieves the latest block on a&#x20;

    given chain.
* `public IEnumerator GetRawLatestBlock(string chainInput, Action<string> callback, Action<EPHANTASMA_SDK_ERROR_TYPE, string> errorHandlingCallback = null);`: Retrieves the raw data of the latest block on a given chain as a string.
* `public IEnumerator GetTransactionByBlockHashAndIndex(string blockHash, int index, Action<Transaction> callback, Action<EPHANTASMA_SDK_ERROR_TYPE, string> errorHandlingCallback = null);`: Retrieves a transaction by its index in a block, given the block hash.
* `public IEnumerator GetChains(Action<Chain[]> callback, Action<EPHANTASMA_SDK_ERROR_TYPE, string> errorHandlingCallback = null);`: Retrieves all chains available in the Phantasma network.
* `public IEnumerator GetContract(string contractName, Action<Contract> callback, Action<EPHANTASMA_SDK_ERROR_TYPE, string> errorHandlingCallback = null);`: Retrieves a contract by its name.
* `public IEnumerator GetContracts(Action<Contract> callback, Action<EPHANTASMA_SDK_ERROR_TYPE, string> errorHandlingCallback = null);`: Retrieves all contracts available in the Phantasma network.
* `public IEnumerator GetNexus(Action<Nexus> callback, Action<EPHANTASMA_SDK_ERROR_TYPE, string> errorHandlingCallback = null);`: Retrieves the Phantasma Nexus details.
* `public IEnumerator GetOrganization(string ID, Action<Organization> callback, Action<EPHANTASMA_SDK_ERROR_TYPE, string> errorHandlingCallback = null);`: Retrieves an organization by its ID.
* `public IEnumerator GetOrganizationByName(string name, Action<Organization> callback, Action<EPHANTASMA_SDK_ERROR_TYPE, string> errorHandlingCallback = null);`: Retrieves an organization by its name.
* `public IEnumerator GetOrganizations(Action<Organization[]> callback, Action<EPHANTASMA_SDK_ERROR_TYPE, string> errorHandlingCallback = null);`: Retrieves all organizations available in the Phantasma network.
* `public IEnumerator GetLatestSaleHash(Action<string> callback, Action<EPHANTASMA_SDK_ERROR_TYPE, string> errorHandlingCallback = null);`: Retrieves the latest crowdsale hash.
* `public IEnumerator GetSale(string hashText, Action<Crowdsale> callback, Action<EPHANTASMA_SDK_ERROR_TYPE, string> errorHandlingCallback = null);`: Retrieves a crowdsale by its hash.
* `public IEnumerator GetToken(string symbol, Action<Token> callback, Action<EPHANTASMA_SDK_ERROR_TYPE, string> errorHandlingCallback = null);`: Retrieves a token by its symbol.
* `public IEnumerator GetTokens(Action<Token[]> callback, Action<EPHANTASMA_SDK_ERROR_TYPE, string> errorHandlingCallback = null);`: Retrieves all tokens available in the Phantasma network.
* `public IEnumerator GetTokenData(string symbol, string IDtext, Action<TokenData> callback, Action<EPHANTASMA_SDK_ERROR_TYPE, string> errorHandlingCallback = null);`: Retrieves token data for a specific token ID.
* `public IEnumerator GetNFT(string symbol, string IDtext, Action<TokenData> callback, Action<EPHANTASMA_SDK_ERROR_TYPE, string> errorHandlingCallback = null);`: Retrieves an NFT by its symbol and ID.
* `public IEnumerator GetNFTs(string symbol, string[] IDtext, Action<TokenData[]> callback, Action<EPHANTASMA_SDK_ERROR_TYPE, string> errorHandlingCallback = null);`: Retrieves multiple NFTs by their symbols and IDs.
* `public IEnumerator GetTokenBalance(string account, string tokenSymbol, string chainInput = "main", Action<Balance> callback = null, Action<EPHANTASMA_SDK_ERROR_TYPE, string> errorHandlingCallback = null);`: Retrieves the token balance of a specific account, given the token symbol and chain (default: main).\

* `public IEnumerator GetAddressTransactions(string addressText, uint page, uint pageSize, Action<Account, int, int> callback, Action<EPHANTASMA_SDK_ERROR_TYPE, string> errorHandlingCallback = null);`: Retrieves transactions associated with a specific address with pagination.
* `public IEnumerator GetAddressTransactionCount(string addressText, string chainInput, Action<int> callback, Action<EPHANTASMA_SDK_ERROR_TYPE, string> errorHandlingCallback = null);`: Retrieves the transaction count for a specific address on a given chain.
* `public IEnumerator SendRawTransaction(string txData, Action<string> callback, Action<EPHANTASMA_SDK_ERROR_TYPE, string> errorHandlingCallback = null);`: Sends a raw transaction with the provided data.
* `public IEnumerator InvokeRawScript(string chainInput, string scriptData, Action<Script> callback, Action<EPHANTASMA_SDK_ERROR_TYPE, string> errorHandlingCallback = null);`: Invokes a raw script on a given chain.
* `public IEnumerator GetTransaction(string hashText, Action<Transaction> callback, Action<EPHANTASMA_SDK_ERROR_TYPE, string> errorHandlingCallback = null);`: Retrieves a transaction by its hash.
* `public IEnumerator GetValidators(Action<Validator[]> callback, Action<EPHANTASMA_SDK_ERROR_TYPE, string> errorHandlingCallback = null);`: Retrieves all validators in the Phantasma network.
* `public IEnumerator GetArchive(string hashText, Action<Archive> callback, Action<EPHANTASMA_SDK_ERROR_TYPE, string> errorHandlingCallback = null);`: Retrieves an archive by its hash.
* `public IEnumerator WriteArchive(string hashText, int blockIndex, string blockContent, Action<Boolean> callback, Action<EPHANTASMA_SDK_ERROR_TYPE, string> errorHandlingCallback = null);`: Writes an archive block with specified content and index.
* `public IEnumerator ReadArchive(string hashText, int blockIndex, Action<string> callback, Action<EPHANTASMA_SDK_ERROR_TYPE, string> errorHandlingCallback = null);`: Reads an archive block by its index.
* `public IEnumerator SignAndSendTransaction(PhantasmaKeys keys, string nexus, byte[] script, string chain, Action<string> callback, Action<EPHANTASMA_SDK_ERROR_TYPE, string> errorHandlingCallback = null);`: Signs and sends a transaction using the provided keys, nexus, script, and chain.
* `public IEnumerator SignAndSendTransactionWithPayload(PhantasmaKeys keys, string nexus, byte[] script, string chain, string payload, Action<string> callback, Action<EPHANTASMA_SDK_ERROR_TYPE, string> errorHandlingCallback = null);`: Signs and sends a transaction with an additional payload using the provided keys, nexus, script, and chain.
* `public IEnumerator SignAndSendTransactionWithPayload(IKeyPair keys, string nexus, byte[] script, string chain, byte[] payload, Action<string> callback, Action<EPHANTASMA_SDK_ERROR_TYPE, string> errorHandlingCallback = null, Func<byte[], byte[], byte[], byte[]> customSignFunction = null);`: Signs and sends a transaction with an additional byte array payload using the provided keys, nexus, script, and chain. Allows for a custom signing function.
