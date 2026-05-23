# Unity Runtime Types

This page groups the Unity runtime support types that appear around
`PhantasmaAPI` and `PhantasmaLinkClient`.

Source baseline:

| Item | Value |
| ---- | ----- |
| Source repo | `phantasma-sdk-unity` |
| Source commit | `2706c004fe1cf9f3919724c6522990ae803584d8` |
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

`WebClient.RPCRequest<T>` tracks request ids and reports malformed responses
through the supplied RPC error callback when an endpoint omits `id`, echoes a
different id, omits `result`, or returns a result shape that cannot be decoded.

## RPC Result Models

The Unity API uses the same typed model names exposed by the C# RPC package.
Common callback result types include:

| Type | Fields or use |
| ---- | ---- |
| `AccountResult` | `Address`, `Name`, `Stakes`, `Stake`, `Unclaimed`, optional `Relay`, `Validator`, `Storage`, `Balances`, optional `Txs`. |
| `BalanceResult` | `Chain`, `Amount`, `Symbol`, `Decimals`, optional `Ids`. |
| `CursorPaginatedResult<T>` | `Result` plus cursor text for account token/NFT and token series/NFT pagination. |
| `BlockResult` | `Hash`, `PreviousHash`, `Timestamp`, `Height`, `ChainAddress`, `Protocol`, `Txs`, `ValidatorAddress`, `Reward`, optional `Events`, optional `Oracles`. |
| `TransactionResult` | `Hash`, `ChainAddress`, `Timestamp`, `BlockHeight`, `BlockHash`, `Script`, `CarbonTxType`, `CarbonTxData`, `Payload`, optional `DebugComment`, `Events`, `ExtendedEvents`, `Result`, `Fee`, `State`, optional `Signatures`, `Sender`, `GasPayer`, `GasTarget`, `GasPrice`, `GasLimit`, `Expiration`. |
| `ScriptResult` | `Events`, optional `Result`, optional `Error`, `Results`, `Oracles`, optional `State`, optional `Gas`. |
| `TokenResult` | `Symbol`, `Name`, `Decimals`, `CurrentSupply`, `MaxSupply`, `BurnedSupply`, `Address`, `Owner`, `Flags`, optional `Script`, `Series`, `CarbonId`, optional `Metadata`, optional `TokenSchemas`, optional `External`, optional `Price`, and token-flag helpers. |
| `TokenSeriesResult` | `SeriesId`, `carbonTokenId`, `carbonSeriesId`, `OwnerAddress`, `MaxMint`, `MintCount`, `CurrentSupply`, `MaxSupply`, optional `BurnedSupply`, optional `Mode`, optional `Script`, optional `Methods`, `Metadata`. |
| `TokenDataResult` | `Id`, `Series`, `carbonTokenId`, `carbonSeriesId`, `carbonNftAddress`, `Mint`, `ChainName`, `OwnerAddress`, `CreatorAddress`, `Ram`, `Rom`, `Status`, `Infusion`, `Properties`. |
| `AuctionResult`, `ContractResult`, `ArchiveResult` | Marketplace listing, contract ABI, and archive storage response models. |

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
