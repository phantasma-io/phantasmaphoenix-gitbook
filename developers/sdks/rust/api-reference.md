# Rust SDK API Reference

This page summarizes the current Rust SDK public surface.

## Crate

| Item | Value |
| ---- | ----- |
| Crate | `phantasma-sdk` |
| Import path | `phantasma_sdk` |
| Current source version | `1.0.1` |
| Rust edition | 2021 |
| Minimum Rust version | `1.74` |

## Top-Level Imports

The crate re-exports common APIs from `phantasma_sdk`.

```rust
use phantasma_sdk::{
    Address, PhantasmaKeys, PhantasmaRpc, Result, ScriptBuilder, Transaction,
};
```

## `crypto`

| API | Purpose |
| --- | ------- |
| `Address` | Checked Phantasma address with `from_text`, `from_public_key`, `from_hash`, `null`, `to_text`, `kind`, and `public_key`. |
| `PhantasmaKeys` | Ed25519 key pair with `generate`, `from_wif`, `to_wif`, `public_key`, `address`, and `sign`. |
| `Ed25519Signature` | Signature wrapper with `verify` and `serialize_data`. |
| `Hash` | SHA-256 hash wrapper with `to_hex` and `difficulty`. |
| `AddressKind`, `SignatureKind` | Typed enums for address and signature kinds. |

See [Keys And Addresses](keys-and-addresses.md) for WIF, signing, address
parsing, and Carbon `Bytes32` conversion examples.

## `vm`

| API | Purpose |
| --- | ------- |
| `ScriptBuilder` | Chainable VM script builder. |
| `ScriptArg` | Strongly typed script argument enum. |
| `Opcode` | VM opcode enum. |
| `VMObject` | VM object decoding and typed conversion. |

Common `ScriptBuilder` methods include `call_interop`, `call_contract`,
`allow_gas`, `spend_gas`, `transfer_tokens`, `transfer_nft`, `stake`,
`unstake`, `call_nft`, `end_script`, `end_script_hex`, and
`end_script_with_error`.

## `transaction`

| API | Purpose |
| --- | ------- |
| `Transaction` | VM script transaction with `new`, `with_payload`, `to_bytes`, `from_bytes`, `hash`, `sign`, `is_signed_by`, and `mine`. |
| `tx_state_is_success` | Returns true for `HALT`. |
| `tx_state_is_fault` | Returns true for `FAULT` or `BREAK`. |
| `SDK_PAYLOAD` | Default SDK payload bytes. |

## `rpc`

| API | Purpose |
| --- | ------- |
| `PhantasmaRpc` | Async typed RPC facade. |
| `RpcTransport` | Transport trait for live or test transports. |
| `ReqwestTransport` | Default HTTP transport. |
| Result structs | `AccountResult`, `BlockResult`, `TransactionResult`, `TokenResult`, `TokenDataResult`, `TokenSeriesResult`, `ScriptResult`, and related RPC models. |

`PhantasmaRpc` exposes read wrappers, invoke-script wrappers, and send helpers.
See [RPC](rpc.md) for the grouped method list.

## `carbon`

| API | Purpose |
| --- | ------- |
| `CarbonSerializable`, `CarbonWriter`, `CarbonReader` | Carbon wire-format primitives. |
| `Bytes16`, `Bytes32`, `Bytes64`, `SmallString`, `IntX` | Checked Carbon primitive types. |
| `serialize`, `deserialize` | Generic Carbon round-trip helpers. |
| `TokenInfo`, `SeriesInfo`, `TokenSchemas` | Token and schema structures. |
| `TokenSchemaField`, `TokenSchemasJson`, `VMStructSchema`, `VMDynamicStruct`, `VMDynamicVariable` | Schema and metadata structures used by token series, ROM, and RAM. |
| `TxMsg`, `SignedTxMsg`, `Witness` | Carbon transaction message structures. |
| `build_token_metadata`, `build_token_info`, `prepare_standard_token_schemas` | Metadata and schema helpers. |
| `token_schemas_from_json`, `parse_token_schemas_json`, `build_token_schemas_from_fields`, `verify_token_schemas` | Custom schema parsing and validation helpers. |
| `build_create_token_tx`, `build_create_token_series_tx`, `build_mint_non_fungible_tx` | Token lifecycle transaction builders. |
| `sign_tx_msg`, `sign_and_serialize_tx_msg`, `sign_and_serialize_tx_msg_hex` | Carbon transaction signing helpers. |
| `FeeOptions`, `CreateTokenFeeOptions`, `CreateSeriesFeeOptions`, `MintNFTFeeOptions` | Carbon fee option structures used by lifecycle builders. |
| Result parsers | `parse_create_token_result`, `parse_create_token_series_result`, `parse_mint_non_fungible_result`, `parse_mint_phantasma_non_fungible_result`. |

See [Schemas And Metadata](schemas-and-metadata.md),
[Fees And Broadcasting](fees-and-broadcasting.md), and
[Carbon Operations](carbon-operations.md) for usage examples and workflow
guidance.

## `encoding`, `binary`, And `error`

| Module | Purpose |
| ------ | ------- |
| `encoding` | Base58 and hex helpers: `encode_base58`, `decode_base58`, `encode_hex`, `decode_hex`, `encode_hex_upper`. |
| `binary` | VM binary readers, writers, and VM bigint helpers. |
| `error` | `PhantasmaError` and `Result<T>`. |

Every public parsing, RPC, and builder path returns `Result<T>` for fallible
work.
