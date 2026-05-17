# Unity Link Client

This page documents `PhantasmaLinkClient`, the Unity wallet-link component used
by wallet-facing examples.

Source baseline:

| Item | Value |
| ---- | ----- |
| Source repo | `Phantasma-UnitySDK` |
| Source commit | `a8e093654d682de6fd0b7568f036d22b5d6ab69e` |
| Source file | `PhantasmaPhoenix.Unity.LinkClient/Runtime/Scripts/PhantasmaLinkClient.cs` |

## Component State

`PhantasmaLinkClient` is a `MonoBehaviour` singleton. On `Awake`, it assigns
`Instance` unless another instance already exists. On `Start`, it calls
`Enable()`.

| Field or property | Use |
| ---- | ---- |
| `Version` | Link protocol version. The inspector default is `2`. |
| `DappID` | DApp or contract identifier included in wallet authorization requests. |
| `Host` | Wallet endpoint host. The inspector default is `localhost:7090`. |
| `Platform` | Signing platform. Default is `PlatformKind.Phantasma`. |
| `Signature` | Signature kind. Default is `SignatureKind.Ed25519`. |
| `GasPrice`, `GasLimit` | Inspector-configured gas values used by example flows around the component. |
| `Ready` | True after the WebSocket connection opens. |
| `Enabled` | True after `Enable()` initializes the component. |
| `Busy` | Public state flag reserved by the component. |
| `Nexus` | Configured nexus value copied from the serialized `_nexus` field on enable. |
| `Wallet`, `Token`, `Name`, `Address`, `IsLogged` | Session values populated by wallet authorization and account fetch. |
| `Avatar` | Texture slot cleared on logout. |
| `Assets` | Symbol keys currently present in the balance cache. |

## Events

| Event | Payload | Use |
| ---- | ---- | ---- |
| `OnLogin` | `UnityEvent<bool, string>` | Receives login success state and message. |
| `OnInfo` | `UnityEvent<string>` | Receives status messages emitted by the component. |

## Connection Lifecycle

| Method | Behavior |
| ---- | ---- |
| `Enable()` | Creates a WebSocket at `ws://{Host}/phantasma`, assigns event handlers, sets default session state, and connects. Returns immediately because it is `async void`. |
| `Update()` | Dispatches queued WebSocket messages outside WebGL player builds and outside editor-disabled paths. |
| `OnApplicationQuit()` | Closes the WebSocket if it exists. |
| `Logout()` | Clears nexus, wallet, token, avatar, name, address, login state, and balance cache. |

Wallet messages are matched to callbacks by numeric request id. Unknown ids are
logged as warnings.

## Login And Account Cache

| Method | Behavior |
| ---- | ---- |
| `Login(Action<bool, string> callback = null)` | Sends `authorize/{DappID}/{Version}`. On success it verifies that the returned nexus equals `Nexus`, stores wallet token fields, and fetches account data. |
| `ReloadAccount(Action<bool, string> callback = null)` | Calls the same account-fetch path used after login. |
| `GetBalance(string symbol)` | Returns the cached balance as a decimal using the cached token decimals. Returns `0` when the symbol is missing. |
| `GetNFTs(string symbol)` | Returns cached NFT ids for a symbol. Returns an empty array when the symbol is missing. |

The account fetch uses `getAccount/{Platform}` through Phantasma Link. It
populates `_balanceMap` for all returned balances and `_ownershipMap` for
entries that include NFT ids.

## Transaction Signing

```csharp
public void SendTransaction(
    string chain,
    byte[] script,
    byte[] payload,
    Action<Hash, string> callback = null,
    PlatformKind platform = PlatformKind.Phantasma,
    SignatureKind signature = SignatureKind.Ed25519)
```

`SendTransaction` rejects scripts with length `>= 8192` before sending the
wallet request. For Link version 2 and newer, the request contains chain,
hex-encoded script, hex-encoded payload, signature kind, and platform. For older
versions, the request includes `Nexus` before the chain/script/payload segment.

On wallet success, the callback receives the parsed `Hash` and `null` error
text. On wallet rejection, the callback receives `Hash.Null` and a rejection
message.

## Data Signing

```csharp
public void SignData(
    string data,
    Action<bool, string, string, string> callback = null,
    PlatformKind platform = PlatformKind.Phantasma,
    SignatureKind signature = SignatureKind.Ed25519)
```

`SignData` requires the component to be enabled, rejects `null` data, and
rejects data strings with length `>= 1024`. It UTF-8 encodes the input, converts
it to hex, and sends `signData/{hex}/{signature}/{platform}`.

On success, the callback receives:

| Position | Value |
| ---- | ---- |
| `bool` | `true` |
| `string` | Wallet signature |
| `string` | Wallet random value |
| `string` | Hex-encoded data |

On failure, the callback receives `false`, a failure message, and empty strings
for the random and encoded data fields.

## Platform Enum

`PlatformKind` values exposed by this source baseline:

| Name | Value |
| ---- | ---- |
| `None` | `0x0` |
| `Phantasma` | `0x1` |
| `Neo` | `0x2` |
| `Ethereum` | `0x4` |
| `BSC` | `0x8` |
