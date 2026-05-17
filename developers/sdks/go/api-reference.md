# Go SDK API Overview

This page summarizes the current Go SDK public surface and links to the deeper
reference pages for method lists, result fields, wire structures, and low-level
helpers.

{% content-ref url="reference/README.md" %}
Go SDK Complete API Reference
{% endcontent-ref %}

## Module

| Item | Value |
| ---- | ----- |
| Module | `github.com/phantasma-io/phantasma-sdk-go` |
| Go | `1.25+` |
| Current local branch observed | `development` |
| Current public tag observed | `v0.9.0` |

## `pkg/rpc`

| API | Purpose |
| --- | ------- |
| `NewRPC(endpoint)` | Create an RPC client for an explicit endpoint. |
| `NewRPCMainnet()` / `NewRPCSetMainnet()` / `NewRPCTestnet()` | Create clients for public endpoint defaults. |
| `PhantasmaRPC.Call(ctx, method, params...)` | Low-level JSON-RPC call for methods without typed wrappers. |
| Typed RPC wrappers | Account, block, transaction, token, series, NFT, archive, auction, contract, organization, VM config, and broadcast methods. |
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
| `Transaction` | Classic VM transaction with serialization and signing. |
| `TxStateIsSuccess`, `TxStateIsFault` | Helpers for finalized transaction state strings. |

Details: [VM and Transaction APIs](reference/vm-transaction-binary.md).

## `pkg/carbon`

| API | Purpose |
| --- | ------- |
| `Writer`, `Reader`, `Serialize`, `Deserialize` | Carbon wire-format primitives. |
| `Bytes16`, `Bytes32`, `Bytes64`, `SmallString`, `IntX` | Checked Carbon primitive types. |
| `TokenInfo`, `SeriesInfo`, `TokenSchemas`, `TxMsg`, `SignedTxMsg`, `Witness` | Carbon token, schema, transaction, and signing structures. |
| Lifecycle builders | Create token, create series, direct NFT mint, and Phantasma NFT mint builders. |
| Result parsers | Create token, create series, direct NFT mint, and Phantasma NFT mint result parsers. |

Details: [Carbon API and Wire Format](reference/carbon-wire.md).
