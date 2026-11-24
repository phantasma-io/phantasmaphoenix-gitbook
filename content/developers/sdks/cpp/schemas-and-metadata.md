---
title: "C++ SDK Schemas And Metadata"
linkTitle: "Schemas And Metadata"
weight: 80
---

Every token carries metadata. An NFT token also carries three schemas, which
fix the fields of its series and of each NFT. The chain checks series metadata
against the token's schemas and every minted ROM against the ROM schema. The
builders live in `Carbon/Contracts/Token.h` and `Carbon/Contracts/TokenSchemas.h`,
in the namespace `phantasma::carbon`. Each answers `false` and fills `error`
when an input is refused, or throws with `PHANTASMA_EXCEPTION_ENABLE`.

## Token Metadata

`TokenMetadataBuilder::BuildAndSerialize(fields, out, error)` takes a list of
name and value strings and writes the metadata for `TokenInfoBuilder::Build`. It
requires four fields:

| Field | Rule |
| ----- | ---- |
| `name` | Not blank. |
| `icon` | A base64 data URI of a PNG, JPEG or WebP image, `data:image/png;base64,...`, with a valid, non-empty base64 payload. |
| `url` | Not blank. |
| `description` | Not blank. |

More fields can be added. Every value is stored as a string, and the fields are
sorted by name. A name given twice keeps its last value.

## The Three NFT Schemas

| Schema | `TokenSchemas` member | Describes | Fields the SDK adds |
| ------ | --------------------- | --------- | ------------------- |
| Series metadata | `seriesMetadata` | The metadata of each series | `_i` (`Int256`): the series id; `mode` (`Int8`): `0` for unique NFTs, `1` for a series whose NFTs share one ROM; `rom` (`Bytes`): that shared ROM |
| ROM | `rom` | The read-only data of each NFT | `_i` (`Int256`): the NFT id; `rom` (`Bytes`): raw ROM bytes |
| RAM | `ram` | The data of each NFT that can change | none |

The five standard NFT fields, `name`, `description`, `imageURL`, `infoURL`
(strings) and `royalties` (`Int32`), must appear in the series metadata schema
or in the ROM schema. The schema builders check that, and the chain requires
them while its `RequireNftStandard` flag is on, as it is on mainnet.

## Standard Schemas

`TokenSchemasBuilder::PrepareStandardTokenSchemas(sharedMetadata)` returns the
standard set as a `TokenSchemasOwned`:

| `sharedMetadata` | The standard fields live in | Use it when |
| ---------------- | --------------------------- | ----------- |
| `false` (default) | The ROM of each NFT | Every NFT has its own name, image and royalties. |
| `true` | The series metadata | All NFTs of a series share them. |

The RAM schema of the standard set has no fields and accepts any extra fields.

```cpp
using namespace phantasma::carbon;

const TokenSchemasOwned perNft = TokenSchemasBuilder::PrepareStandardTokenSchemas();
const TokenSchemasOwned shared = TokenSchemasBuilder::PrepareStandardTokenSchemas(true);

// The bytes TokenInfoBuilder::Build takes as tokenSchemas.
const ByteArray schemaBytes = TokenSchemasBuilder::Serialize(perNft.View());
```

`View()` returns a `TokenSchemas` that points into the vectors of its
`TokenSchemasOwned`, so the owned object has to outlive it. After copying a
`TokenSchemasOwned`, call `Rebind()` on the copy before using its `view`
member.
`SerializeHex` returns the same bytes as hex, and `BuildAndSerialize(nullptr)`
the bytes of the per-NFT standard set.

## Custom Schemas From Fields

`TokenSchemasBuilder::BuildFromFields(seriesFields, romFields, ramFields, out, error)`
takes `FieldType` declarations, a name and a `VmType`:

```cpp
using namespace phantasma::carbon;

TokenSchemasOwned custom;
std::string error;
if( !TokenSchemasBuilder::BuildFromFields(
        {},
        {
            FieldType{ "name", VmType::String },
            FieldType{ "description", VmType::String },
            FieldType{ "imageURL", VmType::String },
            FieldType{ "infoURL", VmType::String },
            FieldType{ "royalties", VmType::Int32 },
            FieldType{ "artist", VmType::String },
        },
        { FieldType{ "level", VmType::Int32 } },
        custom, error) )
    return;
```

The builder adds the fields from the table above, so leave `_i`, `mode` and
`rom` out of the declarations, and then checks the standard fields. An empty
RAM list gives a RAM schema without fields that accepts any extra fields; a
non-empty one gives exactly the listed fields.

## Custom Schemas From JSON

With the RapidJSON adapter, `TokenSchemasBuilder::FromJson(json, out, error)`
reads the same declarations from a JSON object with the three arrays
`seriesMetadata`, `rom` and `ram`; each must be present, even when empty:

```json
{
  "seriesMetadata": [],
  "rom": [
    { "name": "name", "type": "String" },
    { "name": "description", "type": "String" },
    { "name": "imageURL", "type": "String" },
    { "name": "infoURL", "type": "String" },
    { "name": "royalties", "type": "Int32" },
    { "name": "artist", "type": "String" }
  ],
  "ram": [{ "name": "level", "type": "Int32" }]
}
```

The type names are `Dynamic`, `Bytes`, `Struct`, `Int8`, `Int16`, `Int32`,
`Int64`, `Int256`, `Bytes16`, `Bytes32`, `Bytes64`, `String`, `Array`, and the
arrays `Array_Bytes`, `Array_Struct`, `Array_Int8`, `Array_Int16`,
`Array_Int32`, `Array_Int64`, `Array_Int256`, `Array_Bytes16`,
`Array_Bytes32`, `Array_Bytes64`, `Array_String`, in any case. An unknown name
is refused.

## Series Metadata

`SeriesInfoBuilder::Build(seriesMetadataSchema, seriesId, maxMint, maxSupply, owner, fields, out, error)`
writes the series id, `mode` and the shared ROM, then one value for every other
field of the schema. With the per-NFT standard schemas the field list is empty.
A token whose series carry the standard fields lists them:

```cpp
using namespace phantasma::carbon;

const TokenSchemasOwned sharedSchemas = TokenSchemasBuilder::PrepareStandardTokenSchemas(true);
SeriesInfoOwned series;
std::string error;
if( !SeriesInfoBuilder::Build(sharedSchemas.View().seriesMetadata, IdHelper::GetRandomPhantasmaId(), 1000, 0, owner, {
        MetadataField{ "name", MetadataValue::FromString("Example Collection") },
        MetadataField{ "description", MetadataValue::FromString("One image for every NFT of the series") },
        MetadataField{ "imageURL", MetadataValue::FromString("https://example.invalid/collection.png") },
        MetadataField{ "infoURL", MetadataValue::FromString("https://example.invalid/collection") },
        MetadataField{ "royalties", MetadataValue::FromInt64(10000000) }, // 1%
    }, series, error) )
    return;
```

A `rom` field in the list, as bytes or hex text, makes the series one whose
NFTs share that ROM: the builder sets `mode` to `1`. Without it, `mode` is `0`.
`TokenSeriesMetadataBuilder::BuildAndSerialize(schema, seriesId, fields, out, error)`
writes the metadata bytes alone, for `Token.UpdateSeriesMetadata` or for the
`SeriesInfoBuilder::Build` overload that takes ready bytes.

## NFT ROM

`PhantasmaNftRomBuilder::BuildAndSerialize(romSchema, fields, out, error)`
writes the ROM of one NFT for `Token.MintPhantasmaNonFungible`. It leaves out
`_i` and `rom`, refuses those names, and needs every other field of the schema.
A field the schema does not name is ignored. [NFT Minting](nft-minting.md)
shows it in a mint.

`NftRomBuilder::BuildAndSerialize` writes the full ROM with a caller-chosen
`_i`, for a direct `MintNonFungible`. The chain refuses that call while its
configuration disables caller-chosen NFT ids, which is the state of mainnet.

## Values

`MetadataField{ name, value }` pairs a field name with a `MetadataValue`. Names
match the schema exactly, including case. The builders convert each value to
the type of its schema field:

| Field type | `MetadataValue` |
| ---------- | --------------- |
| `String` | `FromString`. A blank string is refused; surrounding spaces are removed. |
| `Int8`, `Int16`, `Int32`, `Int64` | `FromInt64` or `FromUInt64`, within the signed or the unsigned range of the width; a value above the signed maximum is stored as its two's complement. |
| `Int256` | `FromInt256`, `FromUInt256`, `FromInt64`, `FromUInt64`. |
| `Bytes` | `FromBytes`, or `FromString` with hex text. |
| `Bytes16`, `Bytes32`, `Bytes64` | `FromBytes16`, `FromBytes32`, `FromBytes64`. |
| `Struct` | `FromStruct` with name and value pairs. |
| The array types | `FromArray` with one value per element. |

A value of another kind, or out of range, is refused with the field's name in
the error.

## Related Pages

- [Token Deployment](token-deployment.md)
- [NFT Minting](nft-minting.md)
- [Carbon API and Wire Format](reference/carbon-wire.md)
