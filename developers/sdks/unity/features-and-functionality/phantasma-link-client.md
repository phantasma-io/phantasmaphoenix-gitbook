# 🔗 Phantasma Link Client

`PhantasmaLinkClient` is a class in the Unity SDK that provides an abstraction layer to interact with Phantasma wallets.

#### Variables

* `public static PhantasmaLinkClient Instance { get; private set; }`: Singleton instance of PhantasmaLinkClient.
* `public int Version = 2;`: The version of the Phantasma Link Client.
* `public string DappID = "demo";`: The ID of the decentralized application.
* `public string Host = "localhost:7090";`: The host and port of the Phantasma Link server.
* `public PlatformKind Platform = PlatformKind.Phantasma;`: The blockchain platform to use.
* `public SignatureKind Signature = SignatureKind.Ed25519;`: The signature algorithm to use.
* `public int GasPrice = 100000;`: The gas price for transactions.
* `public int GasLimit = 100000;`: The gas limit for transactions.
* `public bool Ready { get; private set; }`: Indicates if the Phantasma Link Client is ready.
* `public bool Enabled { get; private set; }`: Indicates if the Phantasma Link Client is enabled.
* `public string Nexus { get; private set; }`: The Phantasma blockchain Nexus.
* `public string Wallet { get; private set; }`: The wallet address.
* `public string Token { get; private set; }`: The Session token to the wallet.
* `public string Name { get; private set; }`: The wallet name.
* `public string Address { get; private set; }`: The wallet address.
* `public bool IsLogged { get; private set; }`: Indicates if the user is logged in.
* `public Texture2D Avatar { get; private set; }`: The user's avatar.
* `public IEnumerable<string> Assets => _balanceMap.Keys;`: The user's asset symbols.

#### Methods

* `public decimal GetBalance(string symbol);`: Returns the balance of a specified token symbol.
* `public void Login(Action<bool, string> callback = null);`: Logs in the user to the wallet and triggers the callback upon completion.
* `public void ReloadAccount(Action<bool, string> callback = null);`: Reloads the user's account data and triggers the callback upon completion.
* `public void Logout();`: Logs out the user from the wallet.
* `public void SendTransaction(string chain, byte[] script, byte[] payload, Action<Hash, string> callback = null, PlatformKind platform = PlatformKind.Phantasma, SignatureKind signature = SignatureKind.Ed25519);`: Sends a transaction on the specified chain with the given script and payload, and triggers the callback upon completion.
* `public void SignData(string data, Action<bool, string, string, string> callback = null, PlatformKind platform = PlatformKind.Phantasma, SignatureKind signature = SignatureKind.Ed25519);`: Signs data with the user's private key and triggers the callback upon completion.
