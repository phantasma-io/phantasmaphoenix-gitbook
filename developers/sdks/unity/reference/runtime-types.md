# Unity Runtime Types

This page groups the Unity runtime support types that appear around
`PhantasmaAPI` and `PhantasmaLinkClient`.

Source baseline:

| Item | Value |
| ---- | ----- |
| Source repo | `Phantasma-UnitySDK` |
| Source commit | `a8e093654d682de6fd0b7568f036d22b5d6ab69e` |
| Source scope | Unity Core runtime and LinkClient runtime packages |

## Error Handling

`EPHANTASMA_SDK_ERROR_TYPE` is the error enum passed to RPC error callbacks:

```csharp
Action<EPHANTASMA_SDK_ERROR_TYPE, string> errorHandlingCallback
```

Use the callback for transport failures, timeout handling, RPC error responses,
and SDK-side request errors. Successful RPC data is still delivered through the
method-specific success callback.

`WebClient` is the lower-level HTTP helper used by `PhantasmaAPI`.

| API | Use |
| ---- | ---- |
| `WebClient.RPCRequest<T>(...)` | Sends JSON-RPC requests and deserializes typed responses. |
| `WebClient.RESTGet<T>(...)` | Sends typed REST GET requests. |
| `WebClient.RESTPost<T>(...)` | Sends typed REST POST requests. |
| `WebClient.Ping(...)` | Measures endpoint response time. |
| `WebClient.DefaultTimeout` | Default RPC timeout used by `PhantasmaAPI`. |
| `WebClient.DefaultRetries` | Default retry count used by `PhantasmaAPI`. |

## RPC Result Models

The Unity API uses the same typed model names exposed by the C# RPC package.
Common callback result types include:

| Type | Appears in |
| ---- | ---- |
| `AccountResult` | `GetAccount`, `GetAccounts` |
| `BalanceResult` | balance queries and token balance queries |
| `CursorPaginatedResult<T>` | account token/NFT and token series/NFT pagination |
| `TokenResult` | token metadata and owned-token queries |
| `TokenSeriesResult` | series queries |
| `TokenDataResult` | NFT and token data queries |
| `BlockResult` | block queries |
| `TransactionResult` | transaction queries |
| `ScriptResult` | `InvokeRawScript` |
| `AuctionResult` | auction queries |
| `ContractResult` | contract queries |
| `ArchiveResult` | archive storage queries |

For exact fields, use the matching model entries in
[Public API Inventory](public-api.md).

## Wallet Link Types

`PhantasmaLinkClient.Balance` stores cached wallet balances:

| Field | Type | Meaning |
| ---- | ---- | ---- |
| `symbol` | `string` | Token symbol. |
| `value` | `BigInteger` | Integer token amount before decimal conversion. |
| `decimals` | `uint` | Token decimal precision used by `GetBalance`. |
| `ids` | `string[]` | NFT ids returned by the wallet for the symbol. |

`PhantasmaLinkClient.PlatformKind` selects the wallet signing platform. The
component also exposes `SignatureKind`, which is supplied by the imported
cryptography package and defaults to `Ed25519` in the inspector.

## WebSocket Runtime

The LinkClient package includes a runtime WebSocket implementation used by
`PhantasmaLinkClient`.

| Type | Use |
| ---- | ---- |
| `WebSocket` | Connects, sends binary or text messages, receives messages, dispatches callback queues, and closes the socket. |
| `IWebSocket` | Interface for WebSocket implementations. |
| `WebSocketState` | Connection state enum. |
| `WebSocketCloseCode` | Close-code enum. |
| `WebSocketException` and derived exceptions | Error types for invalid state, invalid arguments, and unexpected socket failures. |
| `WebSocketFactory` | WebGL instance factory and event delegation surface. |
| `WaitForUpdate`, `WaitForBackgroundThread`, `MainThreadUtil` | Awaiter and main-thread helpers used by the WebSocket runtime. |

## Logging

`Log` is a Unity Core runtime logging helper. It exposes log levels, Unity debug
log modes, file-path state, initialization, mode switches, and write methods:

| Method family | Use |
| ---- | ---- |
| `Init(...)` | Opens a log file and configures level, working-folder behavior, overwrite behavior, and thread-id output. |
| `SwitchToCompactMode`, `SwitchConsoleOutput`, `SwitchUtcTimestamp`, `DisableMultilinePadding` | Changes logging behavior after initialization. |
| `Write`, `WriteWarning`, `WriteFatalError`, `WriteRaw` | Writes formatted or raw log messages. |

## Cryptography And Transaction Types

Unity Core package code consumes key, address, hash, transaction, and Carbon
types from the Phantasma Phoenix C# libraries. The most visible types are:

| Type | Used by |
| ---- | ---- |
| `IKeyPair` | Signing helpers on `PhantasmaAPI`. |
| `Hash` | Transaction hashes and Link transaction callbacks. |
| `TxMsg` | Carbon signing and broadcast helpers. |
| `Witness`, `Bytes32`, `Bytes64` | Carbon transaction signing internals. |
| `RpcAddressType` | Address-type-aware RPC overloads. |

Use the C# complete reference for deeper behavior of those shared protocol and
cryptography types.
