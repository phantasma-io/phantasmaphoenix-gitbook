# C# Carbon And NFT Types

This page covers Carbon wire blobs, transaction helpers, token/NFT builders,
and metadata structures.

Source baseline:

| Item | Value |
| ---- | ----- |
| Source repo | `phantasmaphoenix-sdk-cs` |
| Source commit | `820680b38e67109b7f94e1d26058d6933f758b26` |
| Primary project | `PhantasmaPhoenix.Protocol.Carbon` |

## Wire Blob Model

Carbon types implement `ICarbonBlob` and define:

```csharp
void Write(BinaryWriter w);
void Read(BinaryReader r);
```

`CarbonBlob` provides the generic entry points:

| API | Behavior |
| ---- | ---- |
| `CarbonBlob.New<T>(BinaryReader r)` | Creates `T`, calls `Read`, and returns the populated value. |
| `CarbonBlob.New<T>(Stream s, bool allowTrailingBytes = false)` | Reads from a stream and, unless allowed, rejects trailing bytes when the stream can seek. |
| `CarbonBlob.New<T>(byte[] bytes, bool allowTrailingBytes = false, long offset = 0)` | Reads a blob from a byte array, optionally from an offset. |
| `CarbonBlob.Serialize<T>(T carbonBlob)` | Writes the blob into a byte array. |

Use `allowTrailingBytes` only for callers that intentionally parse a prefix of
a larger payload.

## Fixed And Compact Types

| Type | Use |
| ---- | ---- |
| `Bytes16`, `Bytes32`, `Bytes64` | Fixed-size byte containers used by addresses, public keys, and signatures. |
| `SmallString` | Compact string value used in Carbon wire structures. |
| `IntX` | Integer helper for Carbon wire integer values. |
| `Witness` | Signature witness with public key/address bytes and signature bytes. |
| `GasConfig` | Gas fields serialized into Carbon chain configuration and fee-related payloads. |
| `ChainConfig` | Chain-level configuration blob. |

All of these are low-level wire types. Build transactions through helper
classes when a helper exists; use the wire types directly when implementing new
Carbon message types.

## Transaction Message Envelopes

| Type | Purpose |
| ---- | ---- |
| `TxMsg` | Top-level Carbon message wrapper used by helper builders and `SignAndSendCarbonTransactionAsync`. |
| `SignedTxMsg` | A `TxMsg` plus one or more `Witness` entries. |
| `TxMsgCall` / `TxMsgCall_Multi` | Contract call messages. |
| `TxMsgPhantasma` / `TxMsgPhantasma_Raw` | Phantasma-specific message wrappers. |
| `TxMsgMintFungible` / `TxMsgBurnFungible` / gas-payer variants | Fungible token mint and burn messages. |
| `TxMsgMintNonFungible` / `TxMsgBurnNonFungible` / gas-payer variants | NFT mint and burn messages. |
| `TxMsgTransferFungible` / gas-payer variant | Fungible transfer messages. |
| `TxMsgTransferNonFungible_Single`, `TxMsgTransferNonFungible_Multi`, and gas-payer variants | NFT transfer messages. |
| `TxMsgTrade` | Trade message payload. |
| `TxMsgSpecialResolution` | Special-resolution message payload. |

Message structs expose `Write` and `Read`. The chain validates addresses, token
ids, fees, permissions, and contract state after the SDK serializes the message.

## Transaction Helpers

| Helper | Main APIs | Use it when |
| ---- | ---- | ---- |
| `CreateTokenTxHelper` | `BuildTx`, `BuildTxAndSign`, `BuildTxAndSignHex`, `ParseResult` | Creating a Carbon token and optionally signing/hex-encoding the transaction. |
| `CreateTokenSeriesTxHelper` | `BuildTx`, `BuildTxAndSign`, `BuildTxAndSignHex`, `ParseResult` | Creating a new series for an NFT token. |
| `MintNonFungibleTxHelper` | `BuildTx`, `BuildTxAndSign`, `BuildTxAndSignHex` | Minting Carbon NFT instances. |
| `MintPhantasmaNonFungibleTxHelper` | `BuildTx`, `BuildTxAndSign`, `BuildTxAndSignHex`, `ParseResult` | Minting Phantasma-style NFT instances and parsing mint results. |
| `TxMsgSigner` | `Sign(TxMsg msg, PhantasmaKeys keys)` | Producing signed Carbon transaction bytes from a `TxMsg`. |

Helper `BuildTx` methods return unsigned `TxMsg` values. `BuildTxAndSign`
returns signed bytes. `BuildTxAndSignHex` returns a hex string ready for
`SendCarbonTransactionAsync`.

## Fee Options

| Type | Behavior |
| ---- | ---- |
| `IFeeOptions` | Exposes `FeeMultiplier` and `CalculateMaxGas(params object[] args)`. |
| `FeeOptions` | Base implementation with `GasFeeBase = 10_000` and `FeeMultiplier = 1_000` defaults. |
| `CreateTokenFeeOptions` | Adds token-creation base and symbol-length fee components. |
| `CreateSeriesFeeOptions` | Adds series-creation base fee. |
| `MintNftFeeOptions` | Uses mint count or collection length when estimating mint gas. |

Fee option methods validate count arguments and use checked arithmetic. Passing
zero, negative, too many, or wrong-typed count arguments throws before the
transaction is built.

## Token Builders And Metadata

| Builder or type | Use |
| ---- | ---- |
| `TokenInfoBuilder.Build(...)` | Builds the `TokenInfo` blob for token creation. |
| `SeriesInfoBuilder.Build(...)` | Builds `SeriesInfo` for NFT series creation. |
| `TokenSchemasBuilder.PrepareStandardTokenSchemas(sharedMetadata)` | Creates standard token schema definitions. |
| `TokenSchemasBuilder.ParseTokenSchemasJson`, `FromJson`, `Serialize`, `SerializeHex`, `BuildAndSerialize` | Converts schema JSON and schema blobs. |
| `TokenMetadataBuilder.BuildAndSerialize(Dictionary<string, string> fields)` | Serializes token metadata fields. |
| `TokenSeriesMetadataBuilder.BuildAndSerialize(...)` | Serializes series metadata. |
| `MetadataHelper.FindMetadataField`, `GetOptionalBytesField`, `PushMetadataField` | Reads or appends metadata fields in helper code. |
| `IdHelper.GetRandomPhantasmaId()` | Produces a random Phantasma id value. |

Token, series, schema, and metadata builders construct bytes for transaction
arguments. They do not guarantee that the submitted token definition satisfies
chain-side policy.

## NFT ROM And Token Helpers

| API | Use |
| ---- | ---- |
| `NftRomBuilder.BuildAndSerialize(...)` | Builds serialized NFT ROM bytes from schema-shaped data. |
| `PhantasmaNftRomBuilder.BuildPublicMintSchema(nftRomSchema)` | Builds the public mint schema used by Phantasma-style NFT minting. |
| `PhantasmaNftRomBuilder.BuildAndSerialize(...)` | Builds serialized Phantasma NFT ROM bytes. |
| `TokenHelper.GetNftAddress(tokenId, instanceId)` | Computes the NFT address bytes from token id and instance id. |
| `TokenHelper.UnpackNftInstanceId(instanceId, out seriesId, out mintNumber)` | Extracts series id and mint number from an NFT instance id. |

## Call Arguments

| Struct | Use |
| ---- | ---- |
| `NftMintInfo` | Per-NFT mint metadata inside NFT mint calls. |
| `MintNonFungibleArgs` | Carbon NFT mint call arguments. |
| `CreateTokenSeriesArgs` | NFT series creation call arguments. |
| `CreateMintedTokenSeriesArgs` | Series creation with initial minted data. |
| `PhantasmaNftMintInfo` | Per-NFT Phantasma mint data. |
| `MintPhantasmaNonFungibleArgs` | Phantasma-style NFT mint call arguments. |
| `PhantasmaNftMintResult` | Parsed mint result entry. |
| `MintFungibleArgs`, `TransferFungibleArgs`, `BurnFungibleArgs` | Fungible token operation arguments. |
| `TransferNonFungibleArgs`, `BurnNonFungibleArgs` | NFT transfer and burn arguments. |
| `UpdateTokenMetadataArgs`, `UpdateSeriesMetadataArgs` | Metadata update arguments. |

Market call argument structs are available for listing, cancel, buy, and query
operations. See [Public API Inventory](public-api.md) for the complete symbol
list.
