# Python SDK API Overview

This page summarizes the current Python SDK public surface and links to the
complete reference pages for detailed RPC methods, result fields, wire
structures, and low-level helpers.

For the deeper API material, use the complete API reference:

{% content-ref url="reference/README.md" %}
Python SDK Complete API Reference
{% endcontent-ref %}

## Package

| Item | Value |
| ---- | ----- |
| Package | `phantasma-sdk-py` |
| Import namespace | `phantasma_py` |
| Current source version | `2.0.2` |
| Python | `>=3.11` |

## Top-Level Imports

The package re-exports the most common classes and helpers from `phantasma_py`.

```python
from phantasma_py import (
    Address,
    PhantasmaKeys,
    PhantasmaRPC,
    ScriptBuilder,
    Transaction,
)
```

For larger applications, importing from the module that owns the API keeps code
clearer:

```python
from phantasma_py.carbon import build_create_token_tx_and_sign_hex
from phantasma_py.rpc import PhantasmaRPC
```

## `phantasma_py.crypto`

| API | Purpose |
| --- | ------- |
| `Address` | Checked 34-byte Phantasma address with `from_text`, `from_public_key`, `from_hash`, `null`, `text`, `kind`, and `public_key`. |
| `PhantasmaKeys` | Ed25519 key pair with `private_key`, `generate`, `from_wif`, `to_wif`, `public_key`, `address`, and `sign`. |
| `Ed25519Signature` | Signature wrapper with `verify` and `serialize_data`. |
| `Hash` | SHA-256 hash wrapper with `from_hex`, `sha256`, `hex`, and `difficulty`. |
| `AddressKind`, `SignatureKind` | Typed enums for address and signature kinds. |

See [Keys And Addresses](keys-and-addresses.md) for WIF, signing, address
parsing, and Carbon `Bytes32` conversion examples.

Details: [VM and Transaction APIs](reference/vm-transaction-binary.md).

## `phantasma_py.vm`

| API | Purpose |
| --- | ------- |
| `ScriptBuilder` | Chainable VM script builder. |
| `Opcode` | VM opcode enum. |
| `VMObject` | VM object decoding and typed conversion. |
| `VMType` | VM object type enum. |

Common `ScriptBuilder` methods include `call_interop`, `call_contract`,
`allow_gas`, `spend_gas`, `transfer_tokens`, `transfer_nft`, `stake`,
`unstake`, `call_nft`, `end_script`, `end_script_hex`, and
`end_script_with_error`.

Method and helper reference: [VM and Transaction APIs](reference/vm-transaction-binary.md).

## `phantasma_py.transaction`

| API | Purpose |
| --- | ------- |
| `Transaction` | VM script transaction with `to_bytes`, `from_bytes`, `hash`, `sign`, `is_signed_by`, and `mine`. |
| `tx_state_is_success` | Returns true for `HALT`. |
| `tx_state_is_fault` | Returns true for `FAULT` or `BREAK`. |

## `phantasma_py.rpc`

| API | Purpose |
| --- | ------- |
| `JsonRpcClient` | Low-level JSON-RPC client. |
| `PhantasmaRPC` | Typed RPC facade. |
| Result dataclasses | `AccountResult`, `BlockResult`, `TransactionResult`, `TokenResult`, `TokenDataResult`, `TokenSeriesResult`, `ScriptResult`, and related RPC models. |

`PhantasmaRPC` exposes read wrappers, invoke-script wrappers, and send helpers.
See [RPC](rpc.md) for workflow usage, [RPC Methods](reference/rpc-methods.md)
for signatures, and [RPC Models](reference/rpc-models.md) for result fields.

## `phantasma_py.carbon`

| API | Purpose |
| --- | ------- |
| `CarbonWriter`, `CarbonReader` | Carbon wire-format primitives. |
| `Bytes16`, `Bytes32`, `Bytes64`, `SmallString`, `IntX` | Checked Carbon primitive types. |
| `CarbonVMType` | Top-level alias for `phantasma_py.carbon.VMType`; use it when code also imports `phantasma_py.vm.VMType`. |
| `serialize`, `deserialize` | Generic Carbon round-trip helpers. |
| `TokenInfo`, `SeriesInfo`, `TokenSchemas` | Token and schema structures. |
| `TokenSchemaField`, `TokenSchemasJSON`, `VMStructSchema`, `VMDynamicStruct`, `VMDynamicVariable` | Schema and metadata structures used by token series, ROM, and RAM. |
| `TxMsg`, `SignedTxMsg`, `Witness` | Carbon transaction message structures. |
| `build_token_metadata`, `build_token_info`, `prepare_standard_token_schemas` | Metadata and schema helpers. |
| `token_schemas_from_json`, `parse_token_schemas_json`, `build_token_schemas_from_fields`, `verify_token_schemas` | Custom schema parsing and validation helpers. |
| `build_create_token_tx`, `build_create_token_series_tx`, `build_mint_non_fungible_tx` | Token lifecycle transaction builders. |
| `sign_tx_msg`, `sign_and_serialize_tx_msg`, `sign_and_serialize_tx_msg_hex` | Carbon transaction signing helpers. |
| `FeeOptions`, `CreateTokenFeeOptions`, `CreateSeriesFeeOptions`, `MintNFTFeeOptions` | Carbon fee option structures used by lifecycle builders. |
| Result parsers | `parse_create_token_result`, `parse_create_token_series_result`, `parse_mint_non_fungible_result`, `parse_mint_phantasma_non_fungible_result`. |

The Carbon module also exposes module-call argument structs for token, market,
chain, gas, and tokens configuration flows.

See [Schemas And Metadata](schemas-and-metadata.md),
[Fees And Broadcasting](fees-and-broadcasting.md), and
[Carbon Operations](carbon-operations.md) for usage examples and workflow
guidance.

Carbon type and builder reference: [Carbon API and Wire Format](reference/carbon-wire.md).

## Exceptions

All SDK-specific exceptions inherit from `PhantasmaError`.

| Exception | Raised by |
| --------- | --------- |
| `EncodingError` | Base58/hex and binary encoding failures. |
| `SerializationError` | VM or Carbon serialization failures. |
| `CryptoError` | Address, key, WIF, hash, and signature failures. |
| `RPCError` | JSON-RPC transport or RPC response failures. |
| `BuilderError` | Script builder and Carbon builder validation failures. |
