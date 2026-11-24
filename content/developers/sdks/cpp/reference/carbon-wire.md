---
title: "C++ SDK Carbon API And Wire Format"
linkTitle: "Carbon API and Wire Format"
weight: 40
---

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

Reader and writer failures go through `PHANTASMA_EXCEPTION`: they throw with
`PHANTASMA_EXCEPTION_ENABLE` and are silent otherwise. The builders also answer
`false` with an error text.

`ReadLengthFor(ReadView&, elementSize)` rejects negative Carbon array lengths,
non-positive element sizes, and fixed-width array lengths whose required bytes
exceed the remaining input.

## Token And Schema Structures

| Structure | Purpose |
| --------- | ------- |
| `TokenInfo` | Token definition for create-token messages. |
| `SeriesInfo` | NFT series definition. |
| `TokenSchemas` | Series metadata, ROM, and RAM schemas. |
| `TokenInfoOwned`, `SeriesInfoOwned` | Own buffers referenced by view structs. |
| `NftMintInfo`, `PhantasmaNftMintInfo` | Direct and deterministic NFT mint records. |
| `PhantasmaNftMintResult` | Deterministic mint result row. |
| `TokenSchemasOwned` | Owns the field vectors a `TokenSchemas` points into; `View()`, `Rebind()`. |
| `FieldType`, `MetadataField`, `MetadataValue` | A schema field declaration, and a metadata name with a typed value (`FromString`, `FromInt64`, `FromUInt64`, `FromInt256`, `FromUInt256`, `FromBytes`, `FromBytes16`, `FromBytes32`, `FromBytes64`, `FromStruct`, `FromArray`). |

## Builders

| Builder | Purpose |
| ------- | ------- |
| `TokenMetadataBuilder::BuildAndSerialize(fields, out, error)` | Token metadata bytes; requires `name`, `icon`, `url` and `description`. |
| `TokenInfoBuilder::Build(symbol, maxSupply, isNFT, decimals, owner, metadata, [schemas], out, error)` | A `TokenInfoOwned`; checks the symbol and sets the big-fungible or NFT flag. |
| `TokenSchemasBuilder::PrepareStandardTokenSchemas(sharedMetadata)`, `BuildFromFields`, `FromJson`, `Serialize`, `SerializeHex`, `BuildAndSerialize` | The token schemas. `FromJson` needs the RapidJSON adapter. |
| `TokenSeriesMetadataBuilder::BuildAndSerialize(schema, seriesId, fields, out, error)` | Series metadata bytes. |
| `SeriesInfoBuilder::Build(...)` | A `SeriesInfoOwned`, from a schema and fields or from ready metadata bytes. |
| `PhantasmaNftRomBuilder::BuildAndSerialize(romSchema, fields, out, error)` | The ROM of a `MintPhantasmaNonFungible`, without `_i` and `rom`. |
| `NftRomBuilder::BuildAndSerialize(...)` | The full ROM with a caller-chosen `_i`, for a direct mint the chain refuses on mainnet. |
| `IdHelper::GetRandomPhantasmaId()` | A random 256-bit id for a new series. |

See [Schemas And Metadata](../schemas-and-metadata.md).

## Fee Planning

| Type | Formula |
| ---- | ------- |
| `PlanFees(msg, config, options, out)` | Prices a message from the message itself. It touches no network. |
| `ChainFeePlanner` | The same plan against a chain. It holds the gas config and reads a burn's infusions. |
| `FeePlan` | `maxGas`, `maxData`, `expectedGasBill`, `kinds`, `exact`, `envelopeBytes`, `Apply(msg)`. |
| `FeePlanOptions` | The chain-state facts a caller may state, plus `witnessCount`. |
| `SummarizeFeePlan(plan)` | `gasBill`, `gasOffer` and `storageCeiling` as decimal strings. |
| `FormatTokenAmount`, `ParseTokenAmount` | Conversion between atoms and decimal amounts. |
| `BurnedInstances(msg)` | The NFT instances a message burns, in any shape. |
| `ReadInfusedAssets(api, msg, out)` | What the burned instances hold, read from the chain. |
| `TxLimits`, `DefaultExpiryMs`, `ExpiryWithin` | The limits a builder writes, and the chain's expiry window. |
| `PreflightTransaction(api, msg, controlTokenId)` | The symbol check before a token creation is signed. |
| `SendTransaction(api, msg, signers, config, options, outHash, outError)` | Build, plan, check, sign and send in one call. |

Overflow is reported through the SDK exception macro path.

## Lifecycle Builders

| Builder | Important behavior |
| ------- | ------------------ |
| `CreateTokenTxHelper::BuildTx` | Serializes `TokenInfo` into a `Token.CreateToken` call. The envelope carries the `TxLimits` given, a zero gas offer by default, and `DefaultExpiryMs` from now when `expiry` is zero. |
| `CreateTokenSeriesTxHelper::BuildTx` | Serializes token id plus `SeriesInfo` and sets token module `CreateTokenSeries`. |
| `MintNonFungibleTxHelper::BuildTx` | Builds a direct `MintNonFungible` message for one NFT, with the same limits rule. The chain refuses it while caller-chosen NFT ids are disabled, as on mainnet. |
| `NativeTxHelper::TransferFungible`, `TransferNonFungible`, `MintFungible`, `BurnFungible`, `BurnNonFungible` | The native transfers, mints and burns; see [Carbon](../carbon.md#native-builders). |
| `MintPhantasmaNonFungibleTxHelper::BuildTx` | Serializes a count plus `PhantasmaNftMintInfo` records into a `Token.MintPhantasmaNonFungible` call and returns the envelope through its out parameter; it answers `false` for an empty list. The fee is planned afterwards and grows with the count. |
| `SignAndSerialize(env, keys)` | Signs the `TxMsg` in a `TxEnvelope` and serializes the signed Carbon message. |

`TxEnvelope.buffers` owns serialized argument buffers referenced by the `TxMsg`.
Keep the envelope alive until after signing/serialization, and move it rather
than copy it: a copy's message still points into the original's buffers.

## Signing And Reading Messages

| API | Purpose |
| --- | ------- |
| `Blockchain::TxMsgSigner::SignAndSerialize(msg, keys)` | Signs a message with one key. Answers an empty result for a message whose `maxGas` is `0`. |
| `Blockchain::TxMsgSigner::SignAndSerialize(msg, signers, out, error)` | Signs with several keys; the gas payer first, then the owner of a `_GasPayer` type. Answers `false` for a message whose `maxGas` is `0`. |
| `Blockchain::RequiredWitnessCount(type, out)` | The fixed number of witnesses of a type; `false` for the types whose witnesses the caller chooses. |
| `Blockchain::ParseTx(msg, bytes, alloc)`, `Blockchain::ParseSignedTx(signed, signedPortion, bytes, alloc)` | Read a message or a signed transaction the way the chain does. |
| `FromPhantasmaAddress(address)`, `FromPhantasmaSystemAddress(address)` | A Phantasma address as a `Bytes32`. |
| `TokenHelper::GetNftAddress`, `TokenHelper::IsNftAddress` | The address of an NFT instance. |

The signing functions do not check the gas offer; plan the message first.

## Wire Layout

The bytes are the same in every SDK. All integers are little-endian. A byte
array is a 4-byte signed length and the bytes, an array a 4-byte count and the
items, a `SmallString` a 1-byte length and UTF-8 bytes. A big integer is one
header byte, the number of value bytes in its low six bits and `0x80` for a
negative number, then the little-endian two's complement bytes without the
trailing fill bytes; zero is `0x00`. An `IntX` that fits `int64` is `0x08`
(`0x88` when negative) and 8 bytes, a larger one a big integer.

A `TxMsg` is `type` (1 byte), `expiry` (8, milliseconds), `maxGas` (8),
`maxData` (8), `gasFrom` (32), `payload` (`SmallString`), then the body of the
type. A signed transaction follows it with the witnesses: one 64-byte signature
by `gasFrom` for the plain native types, two for the `_GasPayer` types (the gas
payer's, then the owner's), and for `Call`, `Call_Multi`, `Trade` and
`Phantasma` a 4-byte count and per witness a 32-byte address and a 64-byte
signature. Every witness signs the serialized `TxMsg`.

## Result Parsers

| Parser | Returns |
| ------ | ------- |
| `CreateTokenTxHelper::ParseResult` | Carbon token id. |
| `CreateTokenSeriesTxHelper::ParseResult` | Carbon series id. |
| `MintNonFungibleTxHelper::ParseResult` | Carbon NFT addresses for direct mints. |
| `MintPhantasmaNonFungibleTxHelper::ParseResult` | Phantasma NFT id and Carbon instance id rows. |
