# Go SDK Carbon API And Wire Format

`pkg/carbon` contains Carbon serialization primitives, typed wire structures,
transaction payloads, schema helpers, fee helpers, token lifecycle builders,
signing helpers, and result parsers.

## Core Serialization

| API | Purpose |
| --- | ------- |
| `NewWriter()` / `Writer` | Writes Carbon primitives and arrays. |
| `NewReader(data)` / `Reader` | Reads Carbon primitives and arrays with bounds checks. |
| `Serialize(blob)` | Serializes a complete `Blob`. |
| `Deserialize` | Parses one complete Carbon blob into the supplied generic type. |
| `Bytes16`, `Bytes32`, `Bytes64` | Fixed-width byte wrappers with checked constructors and hex helpers. |
| `SmallString` | One-byte-length UTF-8 string wrapper. |
| `IntX` | Carbon variable-width signed integer. |
| `Bytes32FromPublicKey`, `Bytes32FromPhantasmaAddress`, `Bytes32FromPhantasmaAddressText` | Account/address conversion helpers for Carbon messages. |

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

## Enums And Flags

| Type | Values or role |
| ---- | -------------- |
| `TxType` | Call, multi-call, trade, transfer, mint, burn, Phantasma VM payload, and raw Phantasma transaction message types. |
| `ModuleID` | Governance, token, Phantasma VM, organization, market, internal module identifiers. |
| `TokenContractMethod` | Token module method ids for create, mint, burn, balance, metadata, and Phantasma NFT flows. |
| `TokenFlags` | `TokenFlagsNone`, `TokenFlagsBigFungible`, `TokenFlagsNonFungible`. |
| `TokensConfigFlags` | Token configuration requirements such as metadata, symbol, NFT meta id, and NFT standard requirements. |
| `VMType` | Carbon dynamic metadata types, including scalar, fixed bytes, struct, dynamic, and array variants. |
| `VMStructFlags` | Dynamic extras and sorted-struct flags. |

## Schema And Metadata APIs

| API | Purpose |
| --- | ------- |
| `PrepareStandardTokenSchemas(sharedMetadata)` | Builds the standard NFT schema layout. |
| `BuildTokenSchemasFromFields(seriesMetadata, rom, ram)` | Builds schema objects from field declarations. |
| `ParseTokenSchemasJSON(data)` / `TokenSchemasFromJSON(data)` | Parses public schema JSON and converts it to SDK schema values. |
| `SerializeTokenSchemas` / `SerializeTokenSchemasHex` | Serializes token schemas for `TokenInfo`. |
| `VerifyTokenSchemas` | Checks standard NFT field requirements. |
| `BuildTokenMetadata(fields)` | Serializes token-level metadata. |
| `BuildTokenSeriesMetadata(schema, phantasmaSeriesID, metadata)` | Serializes series metadata. |
| `BuildNFTRom(schema, phantasmaNFTID, metadata)` | Serializes direct NFT ROM. |
| `BuildPhantasmaNFTRom(nftRomSchema, metadata)` | Serializes public deterministic Phantasma NFT ROM input. |
| `BuildTokenInfo` / `BuildSeriesInfo` | Builds token and series structures used by lifecycle transactions. |

Standard metadata fields are `name`, `description`, `imageURL`, `infoURL`, and
`royalties`. Token-level metadata also requires `name`, `icon`, `url`, and
`description`.

## Transaction Structures And Signing

| Structure or helper | Purpose |
| ------------------- | ------- |
| `TxMsg` | Unsigned Carbon transaction envelope. |
| `SignedTxMsg` | Signed transaction plus witnesses. |
| `Witness` | Address/signature witness entry. |
| `TxMsgCall`, `TxMsgCallMulti` | Module call payloads. |
| `TxMsgTransferFungible`, `TxMsgTransferNonFungible*` | Fungible and NFT transfer payloads. |
| `TxMsgMintFungible`, `TxMsgMintNonFungible` | Mint payloads. |
| `TxMsgBurnFungible`, `TxMsgBurnNonFungible*` | Burn payloads. |
| `TxMsgTrade`, `TxMsgPhantasma`, `TxMsgPhantasmaRaw` | Trade and Phantasma VM payloads. |
| `SignTxMsg`, `SignAndSerializeTxMsg`, `SignAndSerializeTxMsgHex` | Signing and serialization helpers. |

Module argument structures:

| Structure | Fields |
| --------- | ------ |
| `MintFungibleArgs` | `TokenID`, `To`, `Amount`. |
| `TransferFungibleArgs` | `To`, `FromAddress`, `TokenID`, `Amount`. |
| `TransferNonFungibleArgs` | `To`, `FromAddress`, `TokenID`, `InstanceIDs`. |
| `BurnFungibleArgs` | `TokenID`, `FromAddress`, `Amount`. |
| `BurnNonFungibleArgs` | `TokenID`, `FromAddress`, `InstanceIDs`. |
| `CreateTokenSeriesArgs` | `TokenID`, `Info`. |
| `CreateMintedTokenSeriesArgs` | `TokenID`, `Info`, `Address`, `Roms`, `Rams`. |
| `MintNonFungibleArgs` | `TokenID`, `Address`, `Tokens`. |
| `MintPhantasmaNonFungibleArgs` | `TokenID`, `Address`, `Tokens`. |
| `UpdateTokenMetadataArgs` | `TokenID`, `Metadata`. |
| `UpdateSeriesMetadataArgs` | `TokenID`, `SeriesID`, `Metadata`. |
| `TokenListing`, `MarketConfig`, `Market*Args` | Market listing configuration and sell/cancel/buy/query argument payloads. |

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
| `carbon.TxLimits` | `MaxGas`, `MaxData` and `Expiry`, plus `DefaultTxExpiry` and `ExpiryWithin`. |
| `carbon.TxSigner`, `carbon.KeyPairSigners` | Any witness that can sign, and the in-memory adapter. |
| `carbon.PlanAndSignOptions` | `FeePlanOptions` and `TxLimits`, taken by the `Build...TxAndSign` helpers. |

{% content-ref url="/developers/sdks/go/fees-and-broadcasting.md" %}
[Fees And Broadcasting](/developers/sdks/go/fees-and-broadcasting.md)
{% endcontent-ref %}

## Lifecycle Builders

| Builder | Purpose |
| ------- | ------- |
| `BuildCreateTokenTx` | Builds unsigned create-token `TxMsg`. |
| `BuildCreateTokenTxAndSign` / `BuildCreateTokenTxAndSignHex` | Signed create-token bytes or hex. |
| `BuildCreateTokenSeriesTx` | Builds unsigned create-series `TxMsg`. |
| `BuildCreateTokenSeriesTxAndSign` / `BuildCreateTokenSeriesTxAndSignHex` | Signed create-series bytes or hex. |
| `BuildMintPhantasmaNonFungibleTx` | Builds deterministic Phantasma NFT mint for a token slice. |
| `BuildMintPhantasmaNonFungibleSingleTx` | Convenience wrapper for one deterministic Phantasma NFT. |

Builders that accept user metadata return errors. `MustBuild...` variants are
for constants and tests.

## Result Parsers

| Parser | Returns |
| ------ | ------- |
| `ParseCreateTokenResult(resultHex)` | Carbon token id. |
| `ParseCreateTokenSeriesResult(resultHex)` | Carbon series id. |
| `ParseMintNonFungibleResult(carbonTokenID, resultHex)` | Carbon NFT addresses derived from instance ids. |
| `ParseMintPhantasmaNonFungibleResult(resultHex)` | `[]PhantasmaNFTMintResult` with Phantasma NFT id and Carbon instance id. |

Parsers do not verify transaction state. Fetch the transaction, require success,
then parse `TransactionResult.Result` with the parser matching the operation.
