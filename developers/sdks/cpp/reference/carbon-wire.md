# C++ SDK Carbon API And Wire Format

The C++ Carbon API lives under `include/Carbon/`. It uses view structures for
wire payloads and owned helper wrappers where backing storage must be retained.
Include `Carbon/Types.h` when using `IntX` and fixed byte aliases directly.
Include a crypto adapter after `PhantasmaAPI.h` before calling signing helpers.

## Serialization Primitives

| API | Purpose |
| --- | ------- |
| `WriteView`, `ReadView` | View-based Carbon writer and reader state. |
| `Write1`, `Write2`, `Write4`, `Write4u`, `Write8`, `Write8u` | Fixed integer writers. |
| `Read1`, `Read2`, `Read4`, `Read4u`, `Read8`, `Read8u` | Fixed integer readers. |
| `Write16`, `Write32`, `Write64` / fixed byte readers | Fixed-width byte values. |
| `WriteArray`, `ReadArray`, array helper variants | Carbon arrays and byte arrays. |
| `SmallString`, `Bytes16`, `Bytes32`, `Bytes64`, `IntX` | Core Carbon primitive wrappers. |
| `CarbonSerialize(value)` | Serializes a Carbon object into a byte array where available. |

The C++ Carbon API follows the repository's macro-based error model. Reader and
writer failures are surfaced through the SDK exception macro path rather than
per-method `std::error_code` returns.

## Token And Schema Structures

| Structure | Purpose |
| --------- | ------- |
| `TokenInfo` | Token definition for create-token messages. |
| `SeriesInfo` | NFT series definition. |
| `TokenSchemas` | Series metadata, ROM, and RAM schemas. |
| `TokenInfoOwned`, `SeriesInfoOwned` | Own buffers referenced by view structs. |
| `NftMintInfo`, `PhantasmaNftMintInfo` | Direct and deterministic NFT mint records. |
| `PhantasmaNftMintResult` | Deterministic mint result row. |
| `TokenMetadataBuilder` | Token metadata bytes. |

## Fee Options

| Type | Formula |
| ---- | ------- |
| `FeeOptions` | `CalculateMaxGas(count)` returns `gasFeeBase * feeMultiplier * count`; `count` must be positive. |
| `CreateTokenFeeOptions` | Adds create-token base and symbol-length cost before multiplying. |
| `CreateSeriesFeeOptions` | Adds create-series base before multiplying and rejects meaningful count values. |
| `MintNftFeeOptions` | Scales one-mint gas by count for deterministic Phantasma NFT batches. |

Overflow is reported through the SDK exception macro path.

## Lifecycle Builders

| Builder | Important behavior |
| ------- | ------------------ |
| `CreateTokenTxHelper::BuildTx` | Serializes `TokenInfo`, sets token module `CreateToken`, computes create-token gas, and defaults expiry when zero. |
| `CreateTokenSeriesTxHelper::BuildTx` | Serializes token id plus `SeriesInfo` and sets token module `CreateTokenSeries`. |
| `MintNonFungibleTxHelper::BuildTx` | Builds direct `MINT_NON_FUNGIBLE` transaction for one NFT and uses one-mint gas. |
| `MintPhantasmaNonFungibleTxHelper::BuildTx` | Serializes a count plus `PhantasmaNftMintInfo` records and scales gas by count. |
| `SignAndSerialize(env, keys)` | Signs the `TxMsg` in a `TxEnvelope` and serializes the signed Carbon message. |

`TxEnvelope.buffers` owns serialized argument buffers referenced by the `TxMsg`.
Keep the envelope alive until after signing/serialization.

## Result Parsers

| Parser | Returns |
| ------ | ------- |
| `CreateTokenTxHelper::ParseResult` | Carbon token id. |
| `CreateTokenSeriesTxHelper::ParseResult` | Carbon series id. |
| `MintNonFungibleTxHelper::ParseResult` | Carbon NFT addresses for direct mints. |
| `MintPhantasmaNonFungibleTxHelper::ParseResult` | Phantasma NFT id and Carbon instance id rows. |
