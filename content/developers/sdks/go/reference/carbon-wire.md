---
title: "Go SDK Carbon API And Wire Format"
linkTitle: "Carbon API and Wire Format"
weight: 40
---

`pkg/carbon` contains Carbon serialization primitives, typed wire structures,
transaction payloads, schema helpers, fee helpers, token lifecycle builders,
signing helpers, and result parsers.

## Core Serialization

| API | Purpose |
| --- | ------- |
| `NewWriter()` / `Writer` | Writes Carbon primitives and arrays. |
| `NewReader(data)` / `Reader` | Reads Carbon primitives and arrays with bounds checks. |
| `Blob` | The interface of every Carbon structure: `WriteCarbon(*Writer)` and `ReadCarbon(*Reader)`. |
| `Serialize(blob)` | Serializes a complete `Blob`. |
| `Deserialize(data, blob)` | Parses one complete blob into the supplied value. It returns an error for input that is cut short or has bytes left over. |
| `DecodeHex(text)` | Hex to bytes, with or without `0x`. |
| `Bytes16`, `Bytes32`, `Bytes64` | Fixed-width byte values with checked constructors (`NewBytes32`, `Bytes32FromHex`) and `Bytes()`, `String()`. |
| `SmallString` | A UTF-8 string of at most 255 bytes with a one-byte length. |
| `IntX` | Carbon variable-width signed integer: `NewIntX`, `IntXFromInt64`, `MustIntXFromString`, `BigInt()`, `Is8ByteSafe()`. |
| `Bytes32FromPublicKey`, `Bytes32FromPhantasmaAddress`, `Bytes32FromPhantasmaAddressText` | Account and address conversion helpers for Carbon messages. |
| `SystemAddressNull`, `SystemAddressGasPool`, `SystemAddressDataPool` | Fixed system accounts. |

`Must...` helpers panic. Use them for constants and test vectors, not for user
input.

`Reader.ReadLengthFor(elementSize)` rejects non-positive element sizes,
negative Carbon array lengths, and fixed-width array lengths whose required
bytes exceed the remaining input before allocating the result slice.

## Writer And Reader Methods

| Group | Writer methods | Reader methods |
| ----- | -------------- | -------------- |
| Fixed integers | `Write1`, `Write2`, `Write4`, `Write4U`, `Write8`, `Write8U` | `Read1`, `Read2`, `Read4`, `Read4U`, `Read8`, `Read8U` |
| Fixed bytes | `Write16`, `Write32`, `Write64` | `Read16`, `Read32`, `Read64` |
| Big integers | `WriteBigInt`, `WriteBigIntArray` | `ReadBigInt`, `ReadBigIntArray` |
| Strings and bytes | `WriteStringZ`, `WriteStringZArray`, `WriteByteArray`, `WriteByteArrays` | `ReadStringZ`, `ReadStringZArray`, `ReadByteArray`, `ReadByteArrays` |
| Integer arrays | `WriteInt8Array`, `WriteInt16Array`, `WriteInt32Array`, `WriteInt64Array`, `WriteUint64Array` | matching `Read...Array` methods |
| Structures | `WriteBlob`, `WriteBlobArray`, `WriteRaw`, `WriteFixed` | `ReadRaw`, `ReadLength`, `ReadLengthFor`, `AssertEOF` |

## Wire Layout

All integers are little-endian.

| Value | Bytes |
| ----- | ----- |
| Fixed integers | 1, 2, 4 or 8 bytes. |
| `Bytes16`, `Bytes32`, `Bytes64` | 16, 32 or 64 bytes as they are. |
| Byte array | A 4-byte signed length, then the bytes. |
| Array | A 4-byte signed count, then the items. |
| `SmallString` | A 1-byte length, then the UTF-8 bytes. |
| Zero-terminated string | The UTF-8 bytes, then a zero byte. A string that contains a zero byte cannot be written. |
| Big integer (`Int256`) | One header byte, the number of value bytes in its low six bits and `0x80` for a negative number, then the little-endian two's complement bytes without the trailing `0x00` (or `0xFF`) bytes. Zero is the single byte `0x00`. |
| `IntX` | A value that fits `int64` is the header `0x08` (`0x88` when negative) and 8 bytes. A larger value is a big integer. |

A `TxMsg` is written in this order:

| Field | Bytes |
| ----- | ----- |
| `Type` | 1 |
| `Expiry` | 8, signed, milliseconds |
| `MaxGas` | 8 |
| `MaxData` | 8 |
| `GasFrom` | 32 |
| `Payload` | `SmallString` |
| `Msg` | The body of the type |

A signed transaction, `SignedTxMsg`, is the `TxMsg` followed by its witnesses:

| Message type | Witnesses after the message |
| ------------ | --------------------------- |
| `TransferFungible`, `TransferNonFungibleSingle`, `TransferNonFungibleMulti`, `MintFungible`, `BurnFungible`, `MintNonFungible`, `BurnNonFungible` | One 64-byte signature by `GasFrom`. |
| The five `...GasPayer` types | Two 64-byte signatures: the gas payer's, then the token owner's (`From` of the body). |
| `Call`, `CallMulti`, `Trade`, `Phantasma` | A 4-byte count, then per witness a 32-byte address and a 64-byte signature. The gas payer must be one of them. |
| `PhantasmaRaw` | None. |

Every witness signs the serialized `TxMsg`. `RequiredWitnesses(msg)` returns the
fixed witness set of a type, and `EnvelopeBytes(msg, witnessCount)` the size of
the signed transaction before it is signed.

## Enums And Flags

| Type | Values or role |
| ---- | -------------- |
| `TxType` | `TxTypeCall`, `TxTypeCallMulti`, `TxTypeTrade`, the transfer, mint and burn types with their gas-payer forms, `TxTypePhantasma`, `TxTypePhantasmaRaw`. |
| `ModuleID` | `ModuleIDGovernance` (0), `ModuleIDToken` (1), `ModuleIDPhantasma` (2), `ModuleIDOrg` (3), `ModuleIDMarket` (4), `ModuleIDInternal`. |
| `TokenContractMethod` | Token module method ids; see [Token Module Methods](../carbon-operations.md#token-module-methods). |
| `MarketContractMethod`, `ListingType` | Market module method ids and the fixed-price listing type. |
| `GovernanceContractMethod` | `GovernanceMethodRegisterName`, `GovernanceMethodSetGasConfig`. |
| `TokenFlags` | `TokenFlagsNone`, `TokenFlagsBigFungible`, `TokenFlagsNonFungible`. |
| `TokensConfigFlags` | `RequireMetadata`, `RequireSymbol`, `RequireNFTMetaID`, `RequireNFTStandard`, `AllowExplicitNFTMetaIDMint`. |
| `MarketConfigFlags` | `PriceRequired`, `EnforceRoyalties`, `CanCancelEarly`, `CanPurchaseLate`. |
| `VMType` | Carbon dynamic metadata types, including scalar, fixed bytes, struct, dynamic, and array variants. |
| `VMStructFlags` | Dynamic extras and sorted-struct flags. |
| `StandardMeta...` constants | Reserved metadata keys: `_i` (`StandardMetaID`), the chain keys `_a`, `_n`, `_x`, `_t`, and the token keys for staking, inflation, pre-burn and VM script and ABI. |

## Schema And Metadata APIs

| API | Purpose |
| --- | ------- |
| `PrepareStandardTokenSchemas(sharedMetadata)` | Builds the standard NFT schema layout. |
| `BuildTokenSchemasFromFields(seriesMetadata, rom, ram)` | Builds schema objects from `FieldType` declarations. |
| `ParseTokenSchemasJSON(data)` / `TokenSchemasFromJSON(data)` | Parses public schema JSON and converts it to SDK schema values. |
| `VMTypeFromString(name)`, `VMTypeName(type)` | Between type names such as `Int32` and `VMType`. |
| `SerializeTokenSchemas` / `SerializeTokenSchemasHex` / `BuildAndSerializeTokenSchemas` | Serializes token schemas for `TokenInfo`; the last one serializes the per-NFT standard set for `nil`. |
| `VerifyTokenSchemas` | Checks standard NFT field requirements. |
| `BuildTokenMetadata(fields)` | Serializes token-level metadata. |
| `BuildTokenSeriesMetadata(schema, phantasmaSeriesID, metadata)` | Serializes series metadata. |
| `BuildNFTRom(schema, phantasmaNFTID, metadata)` | Serializes the full NFT ROM with `_i`, for a direct mint. |
| `BuildPhantasmaNFTRom(nftRomSchema, metadata)` | Serializes the ROM of a `MintPhantasmaNonFungible` mint, without `_i` and `rom`. |
| `BuildPhantasmaNFTPublicMintSchema(nftRomSchema)` | The ROM schema without `_i` and `rom`, which that ROM follows. |
| `BuildTokenInfo`, `CheckTokenSymbol`, `BuildSeriesInfo` | Builds token and series structures used by lifecycle transactions. |
| `MetadataField`, `FieldType`, `VMStructSchema`, `VMNamedVariableSchema`, `VMDynamicStruct`, `VMNamedDynamicVariable`, `VMDynamicVariable`, `VMStructArray` | The value and schema structures. `VMDynamicStruct.WriteWithSchema` and `ReadWithSchema` write and read a struct by a schema. |

Standard metadata fields are `name`, `description`, `imageURL`, `infoURL`, and
`royalties`. Token-level metadata also requires `name`, `icon`, `url`, and
`description`. See [Schemas And Metadata](../schemas-and-metadata.md).

## Transaction Structures And Signing

| Structure or helper | Purpose |
| ------------------- | ------- |
| `TxMsg` | Unsigned Carbon transaction envelope. |
| `SignedTxMsg` | Signed transaction plus witnesses. |
| `Witness` | Address/signature witness entry. |
| `TxMsgCall`, `TxMsgCallMulti` | Module call payloads. `TxMsgCall.Sections`, a `MsgCallArgSections` of `CallArgSection` values, builds the arguments of a call in a `CallMulti` from bytes and earlier results. |
| `TxMsgTransferFungible`, `TxMsgTransferNonFungible*` | Fungible and NFT transfer payloads. |
| `TxMsgMintFungible`, `TxMsgMintNonFungible` | Mint payloads. |
| `TxMsgBurnFungible`, `TxMsgBurnNonFungible*` | Burn payloads. |
| `TxMsgTrade`, `TxMsgPhantasma`, `TxMsgPhantasmaRaw` | Trade and Phantasma VM payloads. |
| `SignTxMsg`, `SignAndSerializeTxMsg`, `SignAndSerializeTxMsgHex` | Signing with key pairs, and serialization. |
| `SignTxMsgWith`, `SignAndSerializeTxMsgWith`, `TxSigner`, `KeyPairSigner`, `KeyPairSigners` | Signing through any signer. |
| `PlanAndSignWithKeys(msg, keys, config, options)` | Plans an unplanned message against a gas config and signs it; the function behind every `...AndSign` builder. |

Module argument structures:

| Structure | Fields |
| --------- | ------ |
| `MintFungibleArgs` | `TokenID`, `To`, `Amount`. |
| `TransferFungibleArgs` | `To`, `From`, `TokenID`, `Amount`. |
| `TransferNonFungibleArgs` | `To`, `From`, `TokenID`, `InstanceIDs`. |
| `BurnFungibleArgs` | `TokenID`, `From`, `Amount`. |
| `BurnNonFungibleArgs` | `TokenID`, `From`, `InstanceIDs`. |
| `CreateTokenSeriesArgs` | `TokenID`, `Info`. |
| `CreateMintedTokenSeriesArgs` | `TokenID`, `Info`, `Address`, `ROMs`, `RAMs`. |
| `MintNonFungibleArgs` | `TokenID`, `Address`, `Tokens` (`NFTMintInfo`: `SeriesID`, `ROM`, `RAM`). |
| `MintPhantasmaNonFungibleArgs` | `TokenID`, `Address`, `Tokens` (`PhantasmaNFTMintInfo`: `PhantasmaSeriesID`, `ROM`, `RAM`). |
| `PhantasmaNFTMintResult` | `PhantasmaNFTID`, `CarbonInstanceID`: one entry of a `MintPhantasmaNonFungible` result. |
| `UpdateTokenMetadataArgs` | `TokenID`, `Metadata`. |
| `UpdateSeriesMetadataArgs` | `TokenID`, `SeriesID`, `Metadata`. |
| `RegisterNameArgs` | `Address`, `Name`. |
| `TokenListing`, `MarketConfig`, `Market*Args` | Market listing configuration and sell/cancel/buy/query argument payloads. |
| `ChainConfig`, `GasConfig`, `TokensConfig` | The chain, gas and token configuration. `GasConfig.HasGasModelV2()` tells the gas model. |

## Fee Planning

Builders carry no prices. A message is priced after it is built, from the
message itself and the chain's own gas configuration.

| API | Purpose |
| --- | ------- |
| `PhantasmaRPC.Fees()` | The `*rpc.FeePlanner` of this chain. It caches the gas config and prices messages. |
| `carbon.PlanFees(msg, config, options)` | The same calculation against a `carbon.GasConfig` the caller holds. |
| `carbon.FeePlan` | `MaxGas`, `MaxData`, `ExpectedGasBill`, `Kinds`, `Exact`, `EnvelopeBytes`, `Apply(msg)`. |
| `carbon.FeePlanOptions` | The chain-state facts a caller may state, plus `WitnessCount`. |
| `carbon.SummarizeFeePlan(plan)` | `GasBill`, `GasOffer` and `StorageCeiling` as decimal strings. |
| `carbon.NativeFeeKind` | The operation kinds the planner prices. |
| `carbon.BurnedInstances(msg)` | The NFT instances a message burns, in any shape. |
| `carbon.TxLimits` | `MaxGas`, `MaxData` and `Expiry`, plus `DefaultTxExpiry`, `DefaultExpiry()` and `ExpiryWithin`. |
| `carbon.TxSigner`, `carbon.KeyPairSigners` | Any witness that can sign, and the in-memory adapter. |
| `carbon.PlanAndSignOptions` | `FeePlanOptions` and `TxLimits`, taken by the `Build...TxAndSign` helpers. |

- [Fees And Broadcasting](../fees-and-broadcasting.md)

## Builders

| Builder | Purpose |
| ------- | ------- |
| `BuildTransferFungibleTx`, `BuildTransferNonFungibleTx`, `BuildMintFungibleTx`, `BuildBurnFungibleTx`, `BuildBurnNonFungibleTx` | Native transfers, mints and burns from a parameter struct; see [Carbon](../carbon.md#native-builders). |
| `BuildCreateTokenTx` | Builds unsigned create-token `TxMsg`. |
| `BuildCreateTokenTxAndSign` / `BuildCreateTokenTxAndSignHex` | Signed create-token bytes or hex. |
| `BuildCreateTokenSeriesTx` | Builds unsigned create-series `TxMsg`. |
| `BuildCreateTokenSeriesTxAndSign` / `BuildCreateTokenSeriesTxAndSignHex` | Signed create-series bytes or hex. |
| `BuildMintPhantasmaNonFungibleTx` and its `AndSign`, `AndSignHex` forms | A Phantasma NFT mint of one or more instances. |
| `BuildMintPhantasmaNonFungibleSingleTx` and its `AndSign`, `AndSignHex` forms | The same for one instance. |
| `NowUnixMillis()` | The current time in milliseconds, the unit of `TxMsg.Expiry`. |

Builders that accept user metadata return errors. `MustBuild...` variants are
for constants and tests.

## NFT Addresses

| API | Purpose |
| --- | ------- |
| `GetNFTAddress(tokenID, instanceID)` | The address of one NFT instance. |
| `UnpackNFTAddress(address)` | The token id and the instance id of an NFT address. |
| `IsNFTAddress(address)` | Whether 32 bytes have the form of an NFT address. |
| `UnpackNFTInstanceID(instanceID)` | The Carbon series id (low 32 bits) and the mint number (high 32 bits). |

## Result Parsers

| Parser | Returns |
| ------ | ------- |
| `ParseCreateTokenResult(resultHex)` | Carbon token id. |
| `ParseCreateTokenSeriesResult(resultHex)` | Carbon series id. |
| `ParseMintNonFungibleResult(carbonTokenID, resultHex)` | Carbon NFT addresses derived from instance ids, for a direct mint. |
| `ParseMintPhantasmaNonFungibleResult(resultHex)` | `[]PhantasmaNFTMintResult` with Phantasma NFT id and Carbon instance id. |

Parsers do not verify transaction state. Fetch the transaction, require success,
then parse `TransactionResult.Result` with the parser matching the operation.
