---
title: "Go SDK API Overview"
linkTitle: "API Overview"
weight: 110
---

The packages of the Go SDK and their main types. The reference pages list every
method, result field, wire structure and low-level helper.

- [Go SDK Complete API Reference](reference/_index.md)

## Module

| Item | Value |
| ---- | ----- |
| Module | `github.com/phantasma-io/phantasma-sdk-go` |
| Go | `1.25+` |
| Current public tag | `v0.18.1` |

## `pkg/rpc`

| API | Purpose |
| --- | ------- |
| `NewRPC(endpoint)` | Create an RPC client for an explicit endpoint. |
| `NewRPCMainnet()` / `NewRPCSetMainnet()` / `NewRPCTestnet()` | Create clients for public endpoint defaults. |
| `PhantasmaRPC.Call(ctx, method, params...)` | Low-level JSON-RPC call for methods without typed wrappers. |
| Typed RPC wrappers | Account, block, transaction, token, series, NFT, archive, auction, contract, organization, VM config, and broadcast methods. |
| `PhantasmaRPC.Fees()` | The fee planner of this chain. It caches the gas config and prices messages. |
| `PhantasmaRPC.SendTransaction(...)` | Plans, pre-flights, signs and broadcasts a Carbon message in one call. |
| `PreflightTransaction(...)` | Asks the chain whether a token creation's symbol is already taken. |
| `AddressTypePhantasma`, `AddressTypeCarbon` | Address interpretation selectors for wrappers that expose node address-type parameters. |

Details: [RPC Client](reference/rpc-methods.md).

## `pkg/rpc/response`

| API | Purpose |
| --- | ------- |
| Result structs | `AccountResult`, `BalanceResult`, `TransactionResult`, `TokenResult`, `TokenDataResult`, `TokenSeriesResult`, `ScriptResult`, and related chain models. |
| Pagination | `PaginatedResult[T]`, `CursorPaginatedResult[T]`. |
| Helpers | Decimal formatting, token flag checks, account balance lookup, transaction state helpers, and VM result decoding. |

Details: [RPC Result Models](reference/rpc-models.md).

## `pkg/cryptography`

| API | Purpose |
| --- | ------- |
| `PhantasmaKeys` | Ed25519 key pair with generation, WIF import/export, address derivation, and signing. |
| `Address` | Checked Phantasma address parsing, formatting, and null address helpers. |
| `Ed25519Signature` | Signature wrapper and verification. |
| `Hash` | Checked 32-byte hash wrapper and difficulty helper. |

Details: [VM and Transaction APIs](reference/vm-transaction-binary.md).

## `pkg/vm/script_builder` And `pkg/blockchain`

| API | Purpose |
| --- | ------- |
| `ScriptBuilder` | VM bytecode builder with generic contract/interop calls and high-level gas/transfer/stake helpers. |
| `Transaction` | Script transaction with serialization and signing. |
| `TxStateIsSuccess`, `TxStateIsFault` | Helpers for finalized transaction state strings. |

Details: [VM and Transaction APIs](reference/vm-transaction-binary.md).

## `pkg/carbon`

| API | Purpose |
| --- | ------- |
| `Writer`, `Reader`, `Serialize`, `Deserialize` | Carbon wire-format primitives. |
| `Bytes16`, `Bytes32`, `Bytes64`, `SmallString`, `IntX` | Checked Carbon primitive types. |
| `TokenInfo`, `SeriesInfo`, `TokenSchemas`, `TxMsg`, `SignedTxMsg`, `Witness` | Carbon token, schema, transaction, and signing structures. |
| Lifecycle builders | Create token, create series and Phantasma NFT mint builders. |
| Native builders | Transfers, mints and burns, which need no VM script. |
| Schemas and metadata | `PrepareStandardTokenSchemas`, `TokenSchemasFromJSON`, `BuildTokenSchemasFromFields`, `BuildTokenMetadata`, `BuildTokenSeriesMetadata`, `BuildSeriesInfo`, `BuildPhantasmaNFTRom`, `BuildNFTRom`. |
| NFT addresses | `GetNFTAddress`, `UnpackNFTAddress`, `IsNFTAddress`, `UnpackNFTInstanceID`. |
| Module calls | Token module argument structs, the market module (`MarketSellTokenArgs` and the rest), the governance module (`RegisterNameArgs`), and the configuration structures `ChainConfig`, `GasConfig`, `TokensConfig`, `MarketConfig`. |
| Fee planning | `PlanFees`, `FeePlan`, `FeePlanOptions`, `SummarizeFeePlan`, `TxLimits`, `ExpiryWithin`, `BurnedInstances`. |
| Signing | `TxSigner`, `KeyPairSigners`, `SignTxMsg`, `SignTxMsgWith`. |
| Result parsers | Create token, create series, NFT mint and Phantasma NFT mint result parsers. |

Details: [Carbon API and Wire Format](reference/carbon-wire.md).

## Other Packages

| Package | Holds |
| ------- | ----- |
| `pkg/vm` | Opcodes, `VMType`, and `VMObject`, which decodes the values of a script result. |
| `pkg/util` | `ConvertDecimals` and `ConvertDecimalsBack` between atoms and decimal text, and the byte forms of big integers. |
| `pkg/encoding/base58` | Base58 with and without the 4-byte checksum. |
| `pkg/io` | The binary reader and writer of script transactions and event data, and `Deserialize[T]`. |
| `pkg/jsonrpc` | The JSON-RPC transport and `RPCError`. |
| `pkg/domain/event` | Event kinds and the data types of events, such as `TokenEventData`. |
| `pkg/domain` | `SDKVersion` and `SDKPayload`. |
| `pkg/domain/contract`, `pkg/domain/token`, `pkg/domain/stake`, `pkg/domain/types` | Models of contract interfaces, token definitions, stakes and timestamps. |
| `pkg/cryptography/ecdsa`, `pkg/cryptography/proofOfAddress` | secp256k1 and secp256r1 signatures, and the check of a message signed by Phantasma, Ethereum and NEO Legacy keys. |

## Fees

Under gas model v2 the chain bills every byte a transaction puts in the block,
and it escrows every new storage row. Builders carry no prices, so a message is
planned before it is signed.

- [Fees And Broadcasting](fees-and-broadcasting.md)
