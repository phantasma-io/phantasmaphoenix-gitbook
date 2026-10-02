# TypeScript SDK Carbon API And Wire Format

Most core Carbon value types and builders are exported from
`phantasma-sdk-ts/public`. The full Carbon helper surface is exported from
`phantasma-sdk-ts/types`, including the wire serializers, the fee plan types and
helper functions such as `getRandomPhantasmaId`.

## Core Serialization

| API | Purpose |
| --- | ------- |
| `CarbonBlob`, `CarbonBlobLike` | Interface and base behavior for Carbon-serializable values. |
| `CarbonBinaryReader`, `CarbonBinaryWriter` | Carbon wire-format reader and writer. |
| `readBlob`, `writeBlob` | Generic blob read/write helpers. |
| `Bytes16`, `Bytes32`, `Bytes64` | Fixed-width byte values with `toHex()` and `equals(...)`. |
| `SmallString` | One-byte-length UTF-8 string value. |
| `IntX` | Carbon signed integer wrapper. |

`CarbonBinaryReader` rejects negative Carbon array lengths and rejects fixed-
width array lengths whose required bytes exceed the remaining input before it
allocates result arrays.

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

## Fee Planning

Builders carry no prices. A message is priced after it is built, from the
message itself and the chain's own gas configuration.

| API | Purpose |
| --- | ------- |
| `PhantasmaAPI.fees` | The `FeePlanner` of the chain this client talks to. |
| `FeePlanner.plan(msg, options?)` | Prices one message and returns a `FeePlan`. |
| `planFees(msg, config, options?)` | The same calculation against a `GasConfig` the caller holds. It touches no network. |
| `FeePlan.apply(msg)` | Returns a copy of the message with `maxGas` and `maxData` set. |
| `summarizeFeePlan(plan, decimals?)` | Renders `gasBill`, `gasOffer` and `storageCeiling` as decimal strings. |
| `NativeFeeKind` | The operation kinds the planner prices. |
| `GasConfig`, `gasConfigFromRpc(result)` | The chain's prices, and the conversion from the RPC response. |
| `TxLimits` | `maxGas`, `maxData` and `expiry`, which a builder writes into the message. |
| `DEFAULT_TX_EXPIRY_MS`, `expiryWithin(windowMs, marginMs?)` | The default expiry, and the longest one a chain window allows. |
| `parseUnits(value, decimals)`, `formatUnits(atoms, decimals)` | Conversion between decimal amounts and atoms. |
| `burnedInstances(msg)` | The instances a burn message destroys. |

{% content-ref url="/developers/sdks/ts/fees-and-broadcasting.md" %}
[Fees And Broadcasting](/developers/sdks/ts/fees-and-broadcasting.md)
{% endcontent-ref %}

## Lifecycle Builders

| Builder | Purpose |
| ------- | ------- |
| `CreateTokenTxHelper.buildTx` | Builds unsigned create-token `TxMsg`. |
| `CreateTokenTxHelper.buildTxAndSign` / `buildTxAndSignHex` | Signed create-token bytes or hex. |
| `CreateTokenSeriesTxHelper.buildTx` | Builds unsigned create-series `TxMsg`. |
| `CreateTokenSeriesTxHelper.buildTxAndSign` / `buildTxAndSignHex` | Signed create-series bytes or hex. |
| `MintPhantasmaNonFungibleTxHelper.buildTx` | Builds deterministic Phantasma NFT mint for one item or a token array. |
| `MintPhantasmaNonFungibleTxHelper.buildTxAndSign` / `buildTxAndSignHex` | Signed deterministic mint bytes or hex. |
| `NativeTxHelper.transferFungible` / `transferNonFungible` | Builds a native transfer, in the plain or the gas-payer form. |
| `NativeTxHelper.mintFungible` / `burnFungible` / `burnNonFungible` | Builds a native fungible mint, or a burn. |

`buildTxAndSign` and `buildTxAndSignHex` take a `GasConfig` and plan the message
before signing it. `buildTx` leaves the message unplanned, which is what
`PhantasmaAPI.sendTransaction` and a wallet-signing flow both expect.

The SDK carries no builder for a direct `MintNonFungible`. The chain refuses
that operation where governance has not allowed caller-supplied ROM ids, and
that is the state of the public chains today.

## Result Parsers And Address Helpers

| API | Purpose |
| --- | ------- |
| `CreateTokenTxHelper.parseResult(resultHex)` | Parses the Carbon token id as a `bigint`. |
| `CreateTokenSeriesTxHelper.parseResult(resultHex)` | Parses Carbon series id. |
| `MintPhantasmaNonFungibleTxHelper.parseResult(resultHex)` | Parses deterministic mint rows containing Phantasma NFT id and Carbon instance id. |
| `TokenHelper.getNftAddress(carbonTokenId, instanceId)` | Derives Carbon NFT address bytes. |

Parsers expect the transaction result hex from a finalized successful
transaction. They do not poll or classify transaction state.
