# TypeScript SDK Carbon API And Wire Format

Most core Carbon value types and builders are exported from
`phantasma-sdk-ts/public`. The full Carbon helper surface is exported from
`phantasma-sdk-ts/types`, including fee option classes and helper functions such
as `getRandomPhantasmaId`.

## Core Serialization

| API | Purpose |
| --- | ------- |
| `CarbonBlob`, `CarbonBlobLike` | Interface and base behavior for Carbon-serializable values. |
| `CarbonBinaryReader`, `CarbonBinaryWriter` | Carbon wire-format reader and writer. |
| `readBlob`, `writeBlob` | Generic blob read/write helpers. |
| `Bytes16`, `Bytes32`, `Bytes64` | Fixed-width byte values with `toHex()` and `equals(...)`. |
| `SmallString` | One-byte-length UTF-8 string value. |
| `IntX` | Carbon signed integer wrapper. |

## Enums, Flags, And Message Types

| API | Purpose |
| --- | ------- |
| `TxTypes` | Carbon transaction type enum. |
| `ModuleId` | Carbon module ids. |
| `TokenContractMethods` | Token module method ids. |
| `CarbonTokenFlags` | Token flags used in `TokenInfo`. |
| `VmType`, `VmStructFlags` | Carbon metadata schema types and struct flags. |
| `TxMsg`, `SignedTxMsg`, `Witness` | Unsigned/signed Carbon message and witness structures. |
| `TxMsgCall`, `TxMsgCallMulti`, `TxMsgTransfer*`, `TxMsgMint*`, `TxMsgBurn*`, `TxMsgTrade`, `TxMsgPhantasma`, `TxMsgPhantasmaRaw` | Typed Carbon payload structures. |

## Token, Series, Schema, And Metadata Builders

| API | Purpose |
| --- | ------- |
| `TokenInfoBuilder`, `TokenInfo` | Build create-token payload data. |
| `SeriesInfoBuilder`, `SeriesInfo` | Build NFT series payload data. |
| `TokenMetadataBuilder` | Build required token-level metadata. |
| `TokenSchemasBuilder`, `TokenSchemas`, `TokenSchemasJson` | Standard and custom schema construction. |
| `TokenSeriesMetadataBuilder` | Build series metadata bytes. |
| `NftRomBuilder` | Build direct NFT ROM bytes. |
| `PhantasmaNftRomBuilder` | Build public deterministic Phantasma NFT ROM bytes. |
| `MetadataField`, `FieldType`, `VmDynamicVariable`, `VmDynamicStruct`, `VmStructSchema` | Metadata field and schema structures. |
| `standardMetadataFields`, `nftDefaultMetadataFields`, `seriesDefaultMetadataFields`, `findMetadataField`, `pushMetadataField` | Metadata utility helpers. |

Standard display metadata fields are `name`, `description`, `imageURL`,
`infoURL`, and `royalties`. Token-level metadata requires `name`, `icon`,
`url`, and `description`.

## Fee Options

| Type | Formula |
| ---- | ------- |
| `FeeOptions` | `calculateMaxGas(count = 1)` returns `gasFeeBase * feeMultiplier * count` and rejects non-positive counts. |
| `CreateTokenFeeOptions` | `calculateMaxGas(symbol?)` adds create-token base and symbol-length fee before multiplying. |
| `CreateSeriesFeeOptions` | `calculateMaxGas()` adds create-series base; passing a count other than `1` is rejected. |
| `MintNftFeeOptions` | `calculateMaxGas(countOrTokens = 1)` accepts a positive count or an array and scales one-mint gas by item count. |

Direct NFT mint helpers call `calculateMaxGas(1)`. Phantasma NFT batch helpers
call `calculateMaxGas(tokens)`.

## Lifecycle Builders

| Builder | Purpose |
| ------- | ------- |
| `CreateTokenTxHelper.buildTx` | Builds unsigned create-token `TxMsg`. |
| `CreateTokenTxHelper.buildTxAndSign` / `buildTxAndSignHex` | Signed create-token bytes or hex. |
| `CreateTokenSeriesTxHelper.buildTx` | Builds unsigned create-series `TxMsg`. |
| `CreateTokenSeriesTxHelper.buildTxAndSign` / `buildTxAndSignHex` | Signed create-series bytes or hex. |
| `MintNonFungibleTxHelper.buildTx` | Builds direct one-NFT mint. |
| `MintNonFungibleTxHelper.buildTxAndSign` / `buildTxAndSignHex` | Signed direct NFT mint bytes or hex. |
| `MintPhantasmaNonFungibleTxHelper.buildTx` | Builds deterministic Phantasma NFT mint for one item or a token array. |
| `MintPhantasmaNonFungibleTxHelper.buildTxAndSign` / `buildTxAndSignHex` | Signed deterministic mint bytes or hex. |

## Result Parsers And Address Helpers

| API | Purpose |
| --- | ------- |
| `CreateTokenTxHelper.parseResult(resultHex)` | Parses Carbon token id. |
| `CreateTokenSeriesTxHelper.parseResult(resultHex)` | Parses Carbon series id. |
| `MintNonFungibleTxHelper.parseResult(carbonTokenId, resultHex)` | Parses direct mint instance ids and returns Carbon NFT addresses. |
| `MintPhantasmaNonFungibleTxHelper.parseResult(resultHex)` | Parses deterministic mint rows containing Phantasma NFT id and Carbon instance id. |
| `TokenHelper.getNftAddress(carbonTokenId, instanceId)` | Derives Carbon NFT address bytes. |

Parsers expect the transaction result hex from a finalized successful
transaction. They do not poll or classify transaction state.
