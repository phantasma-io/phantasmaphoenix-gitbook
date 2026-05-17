# Unity SDK Public API Inventory

This page lists public classes, methods, functions, enum values, fields, and
constants from the cited source baseline. Use it to check exact names when
working with lower-level SDK APIs.

Source baseline:

| Item | Value |
| ---- | ----- |
| Source repo | `Phantasma-UnitySDK` |
| Source commit | `a8e093654d682de6fd0b7568f036d22b5d6ab69e` |
| Scope | public runtime symbols in Unity Core and LinkClient packages |

## PhantasmaPhoenix.Unity.Core.Logging.Log

Source: `PhantasmaPhoenix.Unity.Core/Runtime/Scripts/Logging/Log.cs`

### Declarations

```csharp
public static class Log
```

### Methods

```csharp
public enum Level
```

```csharp
public enum UnityDebugLogMode
```

```csharp
public static bool IsInitialized => LogStreamWriter != null;
```

```csharp
public static bool IsWriting => WriteDepth > 0;
```

```csharp
public static string FilePath;
```

```csharp
public static void DisableMultilinePadding(bool disableMultilinePadding)
```

```csharp
public static void Init(string fileName, Level maxLevel, bool forceWorkingFolderUsage = false, bool overwriteOldContent = false, bool addTid = false)
```

```csharp
public static void SwitchConsoleOutput(bool consoleOutput)
```

```csharp
public static void SwitchToCompactMode(bool compactMode)
```

```csharp
public static void SwitchUtcTimestamp(bool utcTimestamp)
```

```csharp
public static void Write(string message, Level level = Level.Logic, UnityDebugLogMode unityDebugLogMode = UnityDebugLogMode.Normal)
```

```csharp
public static void WriteFatalError(string message, Level level = Level.Logic)
```

```csharp
public static void WriteRaw(string message, Level level = Level.Logic, UnityDebugLogMode unityDebugLogMode = UnityDebugLogMode.Normal)
```

```csharp
public static void WriteWarning(string message, Level level = Level.Logic)
```

## PhantasmaPhoenix.Unity.Core.PhantasmaAPI

Source: `PhantasmaPhoenix.Unity.Core/Runtime/Scripts/PhantasmaAPI.cs`

### Declarations

```csharp
public class PhantasmaAPI
```

### Methods

```csharp
public IEnumerator GetAccount(string addressText, Action<AccountResult> callback, Action<EPHANTASMA_SDK_ERROR_TYPE, string> errorHandlingCallback = null, int timeout = WebClient.DefaultTimeout, int retries = WebClient.DefaultRetries)
```

```csharp
public IEnumerator GetAccount(string addressText, bool extended, bool checkAddressReservedByte, RpcAddressType addressType, Action<AccountResult> callback, Action<EPHANTASMA_SDK_ERROR_TYPE, string> errorHandlingCallback = null, int timeout = WebClient.DefaultTimeout, int retries = WebClient.DefaultRetries)
```

```csharp
public IEnumerator GetAccountFungibleTokens(string account, Action<CursorPaginatedResult<BalanceResult[]>> callback, Action<EPHANTASMA_SDK_ERROR_TYPE, string> errorHandlingCallback = null, int timeout = WebClient.DefaultTimeout, int retries = WebClient.DefaultRetries)
```

```csharp
public IEnumerator GetAccountFungibleTokens(string account, string tokenSymbol, ulong carbonTokenId, uint pageSize, string cursor, bool checkAddressReservedByte, Action<CursorPaginatedResult<BalanceResult[]>> callback, Action<EPHANTASMA_SDK_ERROR_TYPE, string> errorHandlingCallback = null, int timeout = WebClient.DefaultTimeout, int retries = WebClient.DefaultRetries)
```

```csharp
public IEnumerator GetAccountFungibleTokens(string account, string tokenSymbol, ulong carbonTokenId, uint pageSize, string cursor, bool checkAddressReservedByte, RpcAddressType addressType, Action<CursorPaginatedResult<BalanceResult[]>> callback, Action<EPHANTASMA_SDK_ERROR_TYPE, string> errorHandlingCallback = null, int timeout = WebClient.DefaultTimeout, int retries = WebClient.DefaultRetries)
```

```csharp
public IEnumerator GetAccountNFTs(string account, Action<CursorPaginatedResult<TokenDataResult[]>> callback, Action<EPHANTASMA_SDK_ERROR_TYPE, string> errorHandlingCallback = null, int timeout = WebClient.DefaultTimeout, int retries = WebClient.DefaultRetries)
```

```csharp
public IEnumerator GetAccountNFTs(string account, string tokenSymbol, ulong carbonTokenId, uint carbonSeriesId, uint pageSize, string cursor, bool extended, bool checkAddressReservedByte, Action<CursorPaginatedResult<TokenDataResult[]>> callback, Action<EPHANTASMA_SDK_ERROR_TYPE, string> errorHandlingCallback = null, int timeout = WebClient.DefaultTimeout, int retries = WebClient.DefaultRetries)
```

```csharp
public IEnumerator GetAccountNFTs(string account, string tokenSymbol, ulong carbonTokenId, uint carbonSeriesId, uint pageSize, string cursor, bool extended, bool checkAddressReservedByte, RpcAddressType addressType, Action<CursorPaginatedResult<TokenDataResult[]>> callback, Action<EPHANTASMA_SDK_ERROR_TYPE, string> errorHandlingCallback = null, int timeout = WebClient.DefaultTimeout, int retries = WebClient.DefaultRetries)
```

```csharp
public IEnumerator GetAccountOwnedTokenSeries(string account, Action<CursorPaginatedResult<TokenSeriesResult[]>> callback, Action<EPHANTASMA_SDK_ERROR_TYPE, string> errorHandlingCallback = null, int timeout = WebClient.DefaultTimeout, int retries = WebClient.DefaultRetries)
```

```csharp
public IEnumerator GetAccountOwnedTokenSeries(string account, string tokenSymbol, ulong carbonTokenId, uint pageSize, string cursor, bool checkAddressReservedByte, Action<CursorPaginatedResult<TokenSeriesResult[]>> callback, Action<EPHANTASMA_SDK_ERROR_TYPE, string> errorHandlingCallback = null, int timeout = WebClient.DefaultTimeout, int retries = WebClient.DefaultRetries)
```

```csharp
public IEnumerator GetAccountOwnedTokenSeries(string account, string tokenSymbol, ulong carbonTokenId, uint pageSize, string cursor, bool checkAddressReservedByte, RpcAddressType addressType, Action<CursorPaginatedResult<TokenSeriesResult[]>> callback, Action<EPHANTASMA_SDK_ERROR_TYPE, string> errorHandlingCallback = null, int timeout = WebClient.DefaultTimeout, int retries = WebClient.DefaultRetries)
```

```csharp
public IEnumerator GetAccountOwnedTokens(string account, Action<CursorPaginatedResult<TokenResult[]>> callback, Action<EPHANTASMA_SDK_ERROR_TYPE, string> errorHandlingCallback = null, int timeout = WebClient.DefaultTimeout, int retries = WebClient.DefaultRetries)
```

```csharp
public IEnumerator GetAccountOwnedTokens(string account, string tokenSymbol, ulong carbonTokenId, uint pageSize, string cursor, bool checkAddressReservedByte, Action<CursorPaginatedResult<TokenResult[]>> callback, Action<EPHANTASMA_SDK_ERROR_TYPE, string> errorHandlingCallback = null, int timeout = WebClient.DefaultTimeout, int retries = WebClient.DefaultRetries)
```

```csharp
public IEnumerator GetAccountOwnedTokens(string account, string tokenSymbol, ulong carbonTokenId, uint pageSize, string cursor, bool checkAddressReservedByte, RpcAddressType addressType, Action<CursorPaginatedResult<TokenResult[]>> callback, Action<EPHANTASMA_SDK_ERROR_TYPE, string> errorHandlingCallback = null, int timeout = WebClient.DefaultTimeout, int retries = WebClient.DefaultRetries)
```

```csharp
public IEnumerator GetAccounts(string[] addresses, Action<AccountResult[]> callback, Action<EPHANTASMA_SDK_ERROR_TYPE, string> errorHandlingCallback = null, int timeout = WebClient.DefaultTimeout, int retries = WebClient.DefaultRetries)
```

```csharp
public IEnumerator GetAccounts(string[] addresses, bool extended, bool checkAddressReservedByte, RpcAddressType addressType, Action<AccountResult[]> callback, Action<EPHANTASMA_SDK_ERROR_TYPE, string> errorHandlingCallback = null, int timeout = WebClient.DefaultTimeout, int retries = WebClient.DefaultRetries)
```

```csharp
public IEnumerator GetAddressTransactionCount(string addressText, string chainInput, Action<int> callback, Action<EPHANTASMA_SDK_ERROR_TYPE, string> errorHandlingCallback = null, int timeout = WebClient.DefaultTimeout, int retries = WebClient.DefaultRetries)
```

```csharp
public IEnumerator GetAddressTransactions(string addressText, uint page, uint pageSize, Action<AccountTransactionsResult, uint, uint> callback, Action<EPHANTASMA_SDK_ERROR_TYPE, string> errorHandlingCallback = null, int timeout = WebClient.DefaultTimeout, int retries = WebClient.DefaultRetries)
```

```csharp
public IEnumerator GetArchive(string hashText, Action<ArchiveResult> callback, Action<EPHANTASMA_SDK_ERROR_TYPE, string> errorHandlingCallback = null, int timeout = WebClient.DefaultTimeout, int retries = WebClient.DefaultRetries)
```

```csharp
public IEnumerator GetAuction(string chainAddressOrName, string symbol, string IDtext, Action<AuctionResult> callback, Action<EPHANTASMA_SDK_ERROR_TYPE, string> errorHandlingCallback = null, int timeout = WebClient.DefaultTimeout, int retries = WebClient.DefaultRetries)
```

```csharp
public IEnumerator GetAuctions(string chainAddressOrName, string symbol, uint page, uint pageSize, Action<AuctionResult[], uint, uint, uint> callback, Action<EPHANTASMA_SDK_ERROR_TYPE, string> errorHandlingCallback = null, int timeout = WebClient.DefaultTimeout, int retries = WebClient.DefaultRetries)
```

```csharp
public IEnumerator GetAuctionsCount(string chainAddressOrName, string symbol, Action<int> callback, Action<EPHANTASMA_SDK_ERROR_TYPE, string> errorHandlingCallback = null, int timeout = WebClient.DefaultTimeout, int retries = WebClient.DefaultRetries)
```

```csharp
public IEnumerator GetBlockByHash(string blockHash, Action<BlockResult> callback, Action<EPHANTASMA_SDK_ERROR_TYPE, string> errorHandlingCallback = null, int timeout = WebClient.DefaultTimeout, int retries = WebClient.DefaultRetries)
```

```csharp
public IEnumerator GetBlockByHeight(string chainInput, long height, Action<BlockResult> callback, Action<EPHANTASMA_SDK_ERROR_TYPE, string> errorHandlingCallback = null, int timeout = WebClient.DefaultTimeout, int retries = WebClient.DefaultRetries)
```

```csharp
public IEnumerator GetBlockHeight(string chainInput, Action<long> callback, Action<EPHANTASMA_SDK_ERROR_TYPE, string> errorHandlingCallback = null, int timeout = WebClient.DefaultTimeout, int retries = WebClient.DefaultRetries)
```

```csharp
public IEnumerator GetBlockTransactionCountByHash(string blockHash, Action<int> callback, Action<EPHANTASMA_SDK_ERROR_TYPE, string> errorHandlingCallback = null, int timeout = WebClient.DefaultTimeout, int retries = WebClient.DefaultRetries)
```

```csharp
public IEnumerator GetBlockTransactionCountByHash(string chainAddressOrName, string blockHash, Action<int> callback, Action<EPHANTASMA_SDK_ERROR_TYPE, string> errorHandlingCallback = null, int timeout = WebClient.DefaultTimeout, int retries = WebClient.DefaultRetries)
```

```csharp
public IEnumerator GetChains(Action<ChainResult[]> callback, Action<EPHANTASMA_SDK_ERROR_TYPE, string> errorHandlingCallback = null, int timeout = WebClient.DefaultTimeout, int retries = WebClient.DefaultRetries)
```

```csharp
public IEnumerator GetContract(string contractName, Action<ContractResult> callback, Action<EPHANTASMA_SDK_ERROR_TYPE, string> errorHandlingCallback = null, int timeout = WebClient.DefaultTimeout, int retries = WebClient.DefaultRetries)
```

```csharp
public IEnumerator GetContractByAddress(string chainAddressOrName, string contractAddress, Action<ContractResult> callback, Action<EPHANTASMA_SDK_ERROR_TYPE, string> errorHandlingCallback = null, int timeout = WebClient.DefaultTimeout, int retries = WebClient.DefaultRetries)
```

```csharp
public IEnumerator GetContracts(Action<ContractResult[]> callback, Action<EPHANTASMA_SDK_ERROR_TYPE, string> errorHandlingCallback = null, int timeout = WebClient.DefaultTimeout, int retries = WebClient.DefaultRetries)
```

```csharp
public IEnumerator GetLatestBlock(string chainInput, Action<BlockResult> callback, Action<EPHANTASMA_SDK_ERROR_TYPE, string> errorHandlingCallback = null, int timeout = WebClient.DefaultTimeout, int retries = WebClient.DefaultRetries)
```

```csharp
public IEnumerator GetLeaderboard(string name, Action<LeaderboardResult> callback, Action<EPHANTASMA_SDK_ERROR_TYPE, string> errorHandlingCallback = null, int timeout = WebClient.DefaultTimeout, int retries = WebClient.DefaultRetries)
```

```csharp
public IEnumerator GetNFT(string symbol, string IDtext, bool loadProperties, Action<TokenDataResult> callback, Action<EPHANTASMA_SDK_ERROR_TYPE, string> errorHandlingCallback = null, int timeout = WebClient.DefaultTimeout, int retries = WebClient.DefaultRetries)
```

```csharp
public IEnumerator GetNFTs(string symbol, string[] IDtext, Action<TokenDataResult[]> callback, Action<EPHANTASMA_SDK_ERROR_TYPE, string> errorHandlingCallback = null, int timeout = WebClient.DefaultTimeout, int retries = WebClient.DefaultRetries)
```

```csharp
public IEnumerator GetNFTs(string symbol, string[] IDtext, bool extended, Action<TokenDataResult[]> callback, Action<EPHANTASMA_SDK_ERROR_TYPE, string> errorHandlingCallback = null, int timeout = WebClient.DefaultTimeout, int retries = WebClient.DefaultRetries)
```

```csharp
public IEnumerator GetNexus(Action<NexusResult> callback, Action<EPHANTASMA_SDK_ERROR_TYPE, string> errorHandlingCallback = null, int timeout = WebClient.DefaultTimeout, int retries = WebClient.DefaultRetries)
```

```csharp
public IEnumerator GetOrganization(string ID, Action<OrganizationResult> callback, Action<EPHANTASMA_SDK_ERROR_TYPE, string> errorHandlingCallback = null, int timeout = WebClient.DefaultTimeout, int retries = WebClient.DefaultRetries)
```

```csharp
public IEnumerator GetOrganizationByName(string name, Action<OrganizationResult> callback, Action<EPHANTASMA_SDK_ERROR_TYPE, string> errorHandlingCallback = null, int timeout = WebClient.DefaultTimeout, int retries = WebClient.DefaultRetries)
```

```csharp
public IEnumerator GetOrganizations(Action<OrganizationResult[]> callback, Action<EPHANTASMA_SDK_ERROR_TYPE, string> errorHandlingCallback = null, int timeout = WebClient.DefaultTimeout, int retries = WebClient.DefaultRetries)
```

```csharp
public IEnumerator GetToken(string symbol, Action<TokenResult> callback, Action<EPHANTASMA_SDK_ERROR_TYPE, string> errorHandlingCallback = null, int timeout = WebClient.DefaultTimeout, int retries = WebClient.DefaultRetries)
```

```csharp
public IEnumerator GetToken(string symbol, bool extended, ulong carbonTokenId, Action<TokenResult> callback, Action<EPHANTASMA_SDK_ERROR_TYPE, string> errorHandlingCallback = null, int timeout = WebClient.DefaultTimeout, int retries = WebClient.DefaultRetries)
```

```csharp
public IEnumerator GetTokenBalance(string account, string tokenSymbol, string chainInput = "main", Action<BalanceResult> callback = null, Action<EPHANTASMA_SDK_ERROR_TYPE, string> errorHandlingCallback = null, int timeout = WebClient.DefaultTimeout, int retries = WebClient.DefaultRetries)
```

```csharp
public IEnumerator GetTokenBalance(string account, string tokenSymbol, string chainInput, bool checkAddressReservedByte, RpcAddressType addressType, Action<BalanceResult> callback = null, Action<EPHANTASMA_SDK_ERROR_TYPE, string> errorHandlingCallback = null, int timeout = WebClient.DefaultTimeout, int retries = WebClient.DefaultRetries)
```

```csharp
public IEnumerator GetTokenData(string symbol, string IDtext, Action<TokenDataResult> callback, Action<EPHANTASMA_SDK_ERROR_TYPE, string> errorHandlingCallback = null, int timeout = WebClient.DefaultTimeout, int retries = WebClient.DefaultRetries)
```

```csharp
public IEnumerator GetTokenNFTs(ulong carbonTokenId, Action<CursorPaginatedResult<TokenDataResult[]>> callback, Action<EPHANTASMA_SDK_ERROR_TYPE, string> errorHandlingCallback = null, int timeout = WebClient.DefaultTimeout, int retries = WebClient.DefaultRetries)
```

```csharp
public IEnumerator GetTokenNFTs(ulong carbonTokenId, uint carbonSeriesId, uint pageSize, string cursor, bool extended, string seriesId, Action<CursorPaginatedResult<TokenDataResult[]>> callback, Action<EPHANTASMA_SDK_ERROR_TYPE, string> errorHandlingCallback = null, int timeout = WebClient.DefaultTimeout, int retries = WebClient.DefaultRetries)
```

```csharp
public IEnumerator GetTokenSeries(Action<CursorPaginatedResult<TokenSeriesResult[]>> callback, Action<EPHANTASMA_SDK_ERROR_TYPE, string> errorHandlingCallback = null, int timeout = WebClient.DefaultTimeout, int retries = WebClient.DefaultRetries)
```

```csharp
public IEnumerator GetTokenSeries(string symbol, ulong carbonTokenId, uint pageSize, string cursor, Action<CursorPaginatedResult<TokenSeriesResult[]>> callback, Action<EPHANTASMA_SDK_ERROR_TYPE, string> errorHandlingCallback = null, int timeout = WebClient.DefaultTimeout, int retries = WebClient.DefaultRetries)
```

```csharp
public IEnumerator GetTokenSeriesById(string symbol, ulong carbonTokenId, string seriesId, uint carbonSeriesId, Action<TokenSeriesResult> callback, Action<EPHANTASMA_SDK_ERROR_TYPE, string> errorHandlingCallback = null, int timeout = WebClient.DefaultTimeout, int retries = WebClient.DefaultRetries)
```

```csharp
public IEnumerator GetTokens(Action<TokenResult[]> callback, Action<EPHANTASMA_SDK_ERROR_TYPE, string> errorHandlingCallback = null, int timeout = WebClient.DefaultTimeout, int retries = WebClient.DefaultRetries)
```

```csharp
public IEnumerator GetTokens(bool extended, Action<TokenResult[]> callback, Action<EPHANTASMA_SDK_ERROR_TYPE, string> errorHandlingCallback = null, int timeout = WebClient.DefaultTimeout, int retries = WebClient.DefaultRetries)
```

```csharp
public IEnumerator GetTokens(bool extended, string ownerAddress, Action<TokenResult[]> callback, Action<EPHANTASMA_SDK_ERROR_TYPE, string> errorHandlingCallback = null, int timeout = WebClient.DefaultTimeout, int retries = WebClient.DefaultRetries)
```

```csharp
public IEnumerator GetTokens(bool extended, string ownerAddress, RpcAddressType addressType, Action<TokenResult[]> callback, Action<EPHANTASMA_SDK_ERROR_TYPE, string> errorHandlingCallback = null, int timeout = WebClient.DefaultTimeout, int retries = WebClient.DefaultRetries)
```

```csharp
public IEnumerator GetTransaction(string hashText, Action<TransactionResult> callback, Action<EPHANTASMA_SDK_ERROR_TYPE, string> errorHandlingCallback = null, int timeout = WebClient.DefaultTimeout, int retries = WebClient.DefaultRetries)
```

```csharp
public IEnumerator GetTransactionByBlockHashAndIndex(string blockHash, int index, Action<TransactionResult> callback, Action<EPHANTASMA_SDK_ERROR_TYPE, string> errorHandlingCallback = null, int timeout = WebClient.DefaultTimeout, int retries = WebClient.DefaultRetries)
```

```csharp
public IEnumerator InvokeRawScript(string chainInput, string scriptData, Action<ScriptResult> callback, Action<EPHANTASMA_SDK_ERROR_TYPE, string> errorHandlingCallback = null, int timeout = WebClient.DefaultTimeout, int retries = WebClient.DefaultRetries)
```

```csharp
public IEnumerator LookUpName(string name, Action<string> callback, Action<EPHANTASMA_SDK_ERROR_TYPE, string> errorHandlingCallback = null, int timeout = WebClient.DefaultTimeout, int retries = WebClient.DefaultRetries)
```

```csharp
public IEnumerator ReadArchive(string hashText, int blockIndex, Action<string> callback, Action<EPHANTASMA_SDK_ERROR_TYPE, string> errorHandlingCallback = null, int timeout = WebClient.DefaultTimeout, int retries = WebClient.DefaultRetries)
```

```csharp
public IEnumerator SendCarbonTransaction(string txData, Action<string, string> callback, Action<EPHANTASMA_SDK_ERROR_TYPE, string> errorHandlingCallback = null, int timeout = WebClient.DefaultTimeout, int retries = WebClient.DefaultRetries)
```

```csharp
public IEnumerator SendRawTransaction(string txData, Hash txHash, Action<string, string, Hash> callback, Action<EPHANTASMA_SDK_ERROR_TYPE, string> errorHandlingCallback = null, int timeout = WebClient.DefaultTimeout, int retries = WebClient.DefaultRetries)
```

```csharp
public IEnumerator SignAndSendCarbonTransaction(IKeyPair keys, TxMsg txMsg, Action<string /*tx hash*/, string /*encoded tx*/> callback, Action<EPHANTASMA_SDK_ERROR_TYPE, string> errorHandlingCallback = null, int timeout = WebClient.DefaultTimeout, int retries = WebClient.DefaultRetries)
```

```csharp
public IEnumerator SignAndSendTransaction(IKeyPair keys, string nexus, byte[] script, string chain, byte[] payload, Action<string /*tx hash*/, string /*encoded tx*/> callback, Action<EPHANTASMA_SDK_ERROR_TYPE, string> errorHandlingCallback = null, Func<byte[], byte[], byte[], byte[]> customSignFunction = null, int timeout = WebClient.DefaultTimeout, int retries = WebClient.DefaultRetries)
```

```csharp
public IEnumerator SignAndSendTransaction(IKeyPair keys, string nexus, byte[] script, string chain, string payload, Action<string /*tx hash*/, string /*encoded tx*/> callback, Action<EPHANTASMA_SDK_ERROR_TYPE, string> errorHandlingCallback = null, int timeout = WebClient.DefaultTimeout, int retries = WebClient.DefaultRetries)
```

```csharp
public IEnumerator WriteArchive(string hashText, int blockIndex, byte[] blockContent, Action<Boolean> callback, Action<EPHANTASMA_SDK_ERROR_TYPE, string> errorHandlingCallback = null, int timeout = WebClient.DefaultTimeout, int retries = WebClient.DefaultRetries)
```

```csharp
public PhantasmaAPI(string host)
```

```csharp
public readonly string Host;
```

```csharp
public static bool IsValidAddress(string address)
```

```csharp
public static bool IsValidPrivateKey(string key)
```

## PhantasmaPhoenix.Unity.Core.EPHANTASMA_SDK_ERROR_TYPE

Source: `PhantasmaPhoenix.Unity.Core/Runtime/Scripts/SDKErrorType.cs`

### Declarations

```csharp
public enum EPHANTASMA_SDK_ERROR_TYPE
```

### Variants

- `API_ERROR`
- `FAILED_PARSING_JSON`
- `MALFORMED_RESPONSE`
- `WEB_REQUEST_ERROR`

## PhantasmaPhoenix.Unity.Core.WebClient

Source: `PhantasmaPhoenix.Unity.Core/Runtime/Scripts/WebClient.cs`

### Declarations

```csharp
public static class WebClient
```

### Methods

```csharp
public JsonRpcError error;
```

```csharp
public JsonRpcRequest(string method, object[] parameters, string id)
```

```csharp
public T result;
```

```csharp
public class JsonRpcError
```

```csharp
public class JsonRpcRequest
```

```csharp
public class JsonRpcResponse<T>
```

```csharp
public const int DefaultRetries = 0;
```

```csharp
public const int DefaultTimeout = 0;
```

```csharp
public int code;
```

```csharp
public object[] @params;
```

```csharp
public static IEnumerator Ping(string url, Action<EPHANTASMA_SDK_ERROR_TYPE, string> errorHandlingCallback, Action<TimeSpan> callback)
```

```csharp
public static IEnumerator RESTGet<T>(string url, int timeout, Action<EPHANTASMA_SDK_ERROR_TYPE, string> errorHandlingCallback, Action<T> callback)
```

```csharp
public static IEnumerator RESTPost<T>(string url, string serializedJson, Action<EPHANTASMA_SDK_ERROR_TYPE, string> errorHandlingCallback, Action<T> callback)
```

```csharp
public static IEnumerator RPCRequest<T>(string url, string method, int timeout, int retriesOnNetworkError, Action<EPHANTASMA_SDK_ERROR_TYPE, string> errorHandlingCallback, Action<T> callback, params object[] parameters)
```

```csharp
public string id;
```

```csharp
public string jsonrpc = "2.0";
```

```csharp
public string jsonrpc;
```

```csharp
public string message;
```

```csharp
public string method;
```

## PhantasmaLinkClient

Source: `PhantasmaPhoenix.Unity.LinkClient/Runtime/Scripts/PhantasmaLinkClient.cs`

### Declarations

```csharp
public class PhantasmaLinkClient : MonoBehaviour
```

### Methods

```csharp
public Balance(string symbol, BigInteger value, uint decimals, string[] ids)
```

```csharp
public IEnumerable<string> Assets => _balanceMap.Keys;
```

```csharp
public PlatformKind Platform = PlatformKind.Phantasma;
```

```csharp
public SignatureKind Signature = SignatureKind.Ed25519;
```

```csharp
public Texture2D Avatar { get; private set; }
```

```csharp
public async void Enable()
```

```csharp
public bool Busy { get; private set; }
```

```csharp
public bool Enabled { get; private set; }
```

```csharp
public bool IsLogged { get; private set; }
```

```csharp
public bool Ready { get; private set; }
```

```csharp
public decimal GetBalance(string symbol)
```

```csharp
public enum PlatformKind
```

```csharp
public int GasLimit = 100000;
```

```csharp
public int GasPrice = 100000;
```

```csharp
public int Version = 2;
```

```csharp
public readonly BigInteger value;
```

```csharp
public readonly string symbol;
```

```csharp
public readonly string[] ids;
```

```csharp
public readonly uint decimals;
```

```csharp
public static PhantasmaLinkClient Instance { get; private set; }
```

```csharp
public static UnityEvent<bool, string> OnLogin;
```

```csharp
public static UnityEvent<string> OnInfo = new UnityEvent<string>();
```

```csharp
public string Address { get; private set; }
```

```csharp
public string DappID = "demo";
```

```csharp
public string Host = "localhost:7090";
```

```csharp
public string Name { get; private set; }
```

```csharp
public string Nexus
```

```csharp
public string Token { get; private set; }
```

```csharp
public string Wallet { get; private set; }
```

```csharp
public string[] GetNFTs(string symbol)
```

```csharp
public struct Balance
```

```csharp
public void Login(Action<bool, string> callback = null)
```

```csharp
public void Logout()
```

```csharp
public void ReloadAccount(Action<bool, string> callback = null)
```

```csharp
public void SendTransaction(string chain, byte[] script, byte[] payload, Action<Hash, string> callback = null, PlatformKind platform = PlatformKind.Phantasma, SignatureKind signature = SignatureKind.Ed25519)
```

```csharp
public void SignData(string data, Action<bool, string, string, string> callback = null, PlatformKind platform = PlatformKind.Phantasma, SignatureKind signature = SignatureKind.Ed25519)
```

## PhantasmaLinkClientPluginManager

Source: `PhantasmaPhoenix.Unity.LinkClient/Runtime/Scripts/PhantasmaLinkClientPluginManager.cs`

### Declarations

```csharp
public class PhantasmaLinkClientPluginManager : MonoBehaviour
```

### Methods

```csharp
public async Task SendTransaction(string tx)
```

```csharp
public static PhantasmaLinkClientPluginManager Instance { get; private set; }
```

```csharp
public void Example()
```

```csharp
public void HandleResult()
```

```csharp
public void OnDoSomething()
```

```csharp
public void OpenWallet()
```

## Login

Source: `PhantasmaPhoenix.Unity.LinkClient/Runtime/Scripts/Utils/Login.cs`

### Declarations

```csharp
public class Login : MonoBehaviour
```

### Methods

```csharp
public event Action<string,bool> OnLoginEvent;
```

```csharp
public void OnLogin()
```

## WalletInteractions

Source: `PhantasmaPhoenix.Unity.LinkClient/Runtime/Scripts/Utils/WalletInteractions.cs`

### Declarations

```csharp
public class WalletInteractions : MonoBehaviour
```

### Methods

```csharp
public event Action<string, bool> OnLoginEvent;
```

```csharp
public static decimal Amount;
```

```csharp
public static string Chain;
```

```csharp
public static string DataToSign;
```

```csharp
public static string Payload;
```

```csharp
public static string PhantasmaRpc = "https://testnet.phantasma.io/rpc";
```

```csharp
public static string RecipientAddress;
```

```csharp
public static string Symbol;
```

```csharp
public static string TokenId;
```

```csharp
public static uint? Decimals;
```

```csharp
public void BurnNFT()
```

```csharp
public void BurnTokens()
```

```csharp
public void GetBalances()
```

```csharp
public void GetNFT()
```

```csharp
public void GetNFTs()
```

```csharp
public void GetTransaction(string hash, Action<TransactionResult> callback)
```

```csharp
public void InfuseToken()
```

```csharp
public void InvokeRawScript()
```

```csharp
public void MintNFT()
```

```csharp
public void MintTokens()
```

```csharp
public void MultiSig()
```

```csharp
public void OnLogin()
```

```csharp
public void SendNFT()
```

```csharp
public void SendRawTransaction()
```

```csharp
public void SignData()
```

```csharp
public void TransferBalance()
```

```csharp
public void TransferTokens()
```

```csharp
public void UpdateNFT()
```

## NativeWebSocket.IWebSocket

Source: `PhantasmaPhoenix.Unity.LinkClient/Runtime/WebSocket/IWebSocket.cs`

### Declarations

```csharp
public interface IWebSocket
```

## MainThreadUtil

Source: `PhantasmaPhoenix.Unity.LinkClient/Runtime/WebSocket/MainThreadUtil.cs`

### Declarations

```csharp
public class MainThreadUtil : MonoBehaviour
```

### Methods

```csharp
public static MainThreadUtil Instance { get; private set; }
```

```csharp
public static SynchronizationContext synchronizationContext { get; private set; }
```

```csharp
public static void Run(IEnumerator waitForUpdate)
```

```csharp
public static void Setup()
```

## NativeWebSocket.WaitForBackgroundThread

Source: `PhantasmaPhoenix.Unity.LinkClient/Runtime/WebSocket/WaitForBackgroundThread.cs`

### Declarations

```csharp
public class WaitForBackgroundThread
```

### Methods

```csharp
public ConfiguredTaskAwaitable.ConfiguredTaskAwaiter GetAwaiter()
```

## WaitForUpdate

Source: `PhantasmaPhoenix.Unity.LinkClient/Runtime/WebSocket/WaitForUpdate.cs`

### Declarations

```csharp
public class WaitForUpdate : CustomYieldInstruction
```

### Methods

```csharp
public MainThreadAwaiter GetAwaiter()
```

```csharp
public bool IsCompleted { get; set; }
```

```csharp
public class MainThreadAwaiter : INotifyCompletion
```

```csharp
public override bool keepWaiting
```

```csharp
public static IEnumerator CoroutineWrapper(IEnumerator theWorker, MainThreadAwaiter awaiter)
```

```csharp
public void Complete()
```

```csharp
public void GetResult() { }
```

## NativeWebSocket.WebSocket

Source: `PhantasmaPhoenix.Unity.LinkClient/Runtime/WebSocket/WebSocket.cs`

### Declarations

```csharp
public class WebSocket : IWebSocket
```

### Methods

```csharp
public Task Close (WebSocketCloseCode code = WebSocketCloseCode.Normal, string reason = null)
```

```csharp
public Task Connect ()
```

```csharp
public Task Send (byte[] data)
```

```csharp
public Task SendText (string message)
```

```csharp
public WebSocket (string url, Dictionary<string, string> headers = null)
```

```csharp
public WebSocketState State
```

```csharp
public event WebSocketCloseEventHandler OnClose;
```

```csharp
public event WebSocketErrorEventHandler OnError;
```

```csharp
public event WebSocketMessageEventHandler OnMessage;
```

```csharp
public event WebSocketOpenEventHandler OnOpen;
```

```csharp
public int GetInstanceId ()
```

```csharp
public static extern int WebSocketClose (int instanceId, int code, string reason);
```

```csharp
public static extern int WebSocketConnect (int instanceId);
```

```csharp
public static extern int WebSocketGetState (int instanceId);
```

```csharp
public static extern int WebSocketSend (int instanceId, byte[] dataPtr, int dataLength);
```

```csharp
public static extern int WebSocketSendText (int instanceId, string message);
```

```csharp
public void CancelConnection ()
```

```csharp
public void DelegateOnCloseEvent (int closeCode)
```

```csharp
public void DelegateOnErrorEvent (string errorMsg)
```

```csharp
public void DelegateOnMessageEvent (byte[] data)
```

```csharp
public void DelegateOnOpenEvent ()
```

## NativeWebSocket.WebSocket

Source: `PhantasmaPhoenix.Unity.LinkClient/Runtime/WebSocket/WebSocket.cs`

### Declarations

```csharp
public class WebSocket : IWebSocket
```

### Methods

```csharp
public Task Send(byte[] bytes)
```

```csharp
public Task SendText(string message)
```

```csharp
public WebSocket(string url, Dictionary<string, string> headers = null)
```

```csharp
public WebSocketState State
```

```csharp
public async Task Close()
```

```csharp
public async Task Connect()
```

```csharp
public async Task Receive()
```

```csharp
public event WebSocketCloseEventHandler OnClose;
```

```csharp
public event WebSocketErrorEventHandler OnError;
```

```csharp
public event WebSocketMessageEventHandler OnMessage;
```

```csharp
public event WebSocketOpenEventHandler OnOpen;
```

```csharp
public void CancelConnection()
```

```csharp
public void DispatchMessageQueue()
```

## NativeWebSocket.WebSocketCloseCode

Source: `PhantasmaPhoenix.Unity.LinkClient/Runtime/WebSocket/WebSocketCloseCode.cs`

### Declarations

```csharp
public enum WebSocketCloseCode
```

### Variants

- `Abnormal = 1006`
- `Away = 1001`
- `InvalidData = 1007`
- `MandatoryExtension = 1010`
- `NoStatus = 1005`
- `Normal = 1000`
- `NotSet = 0`
- `PolicyViolation = 1008`
- `ProtocolError = 1002`
- `ServerError = 1011`
- `TlsHandshakeFailure = 1015`
- `TooBig = 1009`
- `Undefined = 1004`
- `UnsupportedData = 1003`

## NativeWebSocket.WebSocketException

Source: `PhantasmaPhoenix.Unity.LinkClient/Runtime/WebSocket/WebSocketException.cs`

### Declarations

```csharp
public class WebSocketException : Exception
```

### Methods

```csharp
public WebSocketException() { }
```

```csharp
public WebSocketException(string message) : base(message) { }
```

```csharp
public WebSocketException(string message, Exception inner) : base(message, inner) { }
```

## NativeWebSocket.WebSocketFactory

Source: `PhantasmaPhoenix.Unity.LinkClient/Runtime/WebSocket/WebSocketFactory.cs`

### Declarations

```csharp
public static class WebSocketFactory
```

### Methods

```csharp
public delegate void OnCloseCallback (int instanceId, int closeCode);
```

```csharp
public delegate void OnErrorCallback (int instanceId, System.IntPtr errorPtr);
```

```csharp
public delegate void OnMessageCallback (int instanceId, System.IntPtr msgPtr, int msgSize);
```

```csharp
public delegate void OnOpenCallback (int instanceId);
```

```csharp
public static Dictionary<Int32, WebSocket> instances = new Dictionary<Int32, WebSocket> ();
```

```csharp
public static WebSocket CreateInstance(string url)
```

```csharp
public static bool isInitialized = false;
```

```csharp
public static extern int WebSocketAllocate (string url);
```

```csharp
public static extern void WebSocketFree (int instanceId);
```

```csharp
public static extern void WebSocketSetOnClose (OnCloseCallback callback);
```

```csharp
public static extern void WebSocketSetOnError (OnErrorCallback callback);
```

```csharp
public static extern void WebSocketSetOnMessage (OnMessageCallback callback);
```

```csharp
public static extern void WebSocketSetOnOpen (OnOpenCallback callback);
```

```csharp
public static void DelegateOnCloseEvent (int instanceId, int closeCode)
```

```csharp
public static void DelegateOnErrorEvent (int instanceId, System.IntPtr errorPtr)
```

```csharp
public static void DelegateOnMessageEvent (int instanceId, System.IntPtr msgPtr, int msgSize)
```

```csharp
public static void DelegateOnOpenEvent (int instanceId)
```

```csharp
public static void HandleInstanceDestroy (int instanceId)
```

```csharp
public static void Initialize ()
```

## NativeWebSocket.WebSocketHelpers

Source: `PhantasmaPhoenix.Unity.LinkClient/Runtime/WebSocket/WebSocketHelpers.cs`

### Declarations

```csharp
public static class WebSocketHelpers
```

### Methods

```csharp
public static WebSocketCloseCode ParseCloseCodeEnum(int closeCode)
```

```csharp
public static WebSocketException GetErrorMessageFromCode(int errorCode, Exception inner)
```

## NativeWebSocket.WebSocketInvalidArgumentException

Source: `PhantasmaPhoenix.Unity.LinkClient/Runtime/WebSocket/WebSocketInvalidArgumentException.cs`

### Declarations

```csharp
public class WebSocketInvalidArgumentException : WebSocketException
```

### Methods

```csharp
public WebSocketInvalidArgumentException() { }
```

```csharp
public WebSocketInvalidArgumentException(string message) : base(message) { }
```

```csharp
public WebSocketInvalidArgumentException(string message, Exception inner) : base(message, inner) { }
```

## NativeWebSocket.WebSocketInvalidStateException

Source: `PhantasmaPhoenix.Unity.LinkClient/Runtime/WebSocket/WebSocketInvalidStateException.cs`

### Declarations

```csharp
public class WebSocketInvalidStateException : WebSocketException
```

### Methods

```csharp
public WebSocketInvalidStateException() { }
```

```csharp
public WebSocketInvalidStateException(string message) : base(message) { }
```

```csharp
public WebSocketInvalidStateException(string message, Exception inner) : base(message, inner) { }
```

## NativeWebSocket.WebSocketState

Source: `PhantasmaPhoenix.Unity.LinkClient/Runtime/WebSocket/WebSocketState.cs`

### Declarations

```csharp
public enum WebSocketState
```

### Variants

- `Closed`
- `Closing`
- `Connecting`
- `Open`

## NativeWebSocket.WebSocketUnexpectedException

Source: `PhantasmaPhoenix.Unity.LinkClient/Runtime/WebSocket/WebSocketUnexpectedException.cs`

### Declarations

```csharp
public class WebSocketUnexpectedException : WebSocketException
```

### Methods

```csharp
public WebSocketUnexpectedException() { }
```

```csharp
public WebSocketUnexpectedException(string message) : base(message) { }
```

```csharp
public WebSocketUnexpectedException(string message, Exception inner) : base(message, inner) { }
```
