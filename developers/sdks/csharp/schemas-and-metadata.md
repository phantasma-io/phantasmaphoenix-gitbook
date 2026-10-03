---
description: Token metadata, NFT schemas and series metadata in C#.
---

# Schemas And Metadata

Every token carries metadata. An NFT token also carries three schemas, which fix the fields of its series and of each NFT. The chain checks series metadata against the token's schemas and every minted ROM against the ROM schema. The builders live in the namespace `PhantasmaPhoenix.Protocol.Carbon.Blockchain.Modules.Builders`.

## Token Metadata

`TokenMetadataBuilder.BuildAndSerialize(fields)` takes a dictionary of strings and returns the serialized metadata for `TokenInfoBuilder.Build`. It requires four fields:

| Field | Rule |
| --- | --- |
| `name` | Not empty. |
| `icon` | A base64 data URI of a PNG, JPEG or WebP image: `data:image/png;base64,...`, with a non-empty, valid base64 payload. |
| `url` | Not empty. |
| `description` | Not empty. |

More fields can be added; they are stored as strings. A missing or empty required field, or a bad icon, throws `ArgumentException`.

## The Three NFT Schemas

| Schema | Describes | Fields the SDK adds |
| --- | --- | --- |
| `seriesMetadata` | The metadata of each series | `_i` (Int256): the series id; `mode` (Int8): `0` for unique NFTs, `1` for a series whose NFTs share one ROM; `rom` (Bytes): that shared ROM |
| `rom` | The read-only data of each NFT | `_i` (Int256): the NFT id; `rom` (Bytes): raw ROM bytes |
| `ram` | The mutable data of each NFT | none |

The five standard NFT fields, `name`, `description`, `imageURL`, `infoURL` (strings) and `royalties` (Int32), must appear in the series metadata schema or in the ROM schema. `TokenSchemasBuilder.Verify` checks that, and the chain requires them when its `RequireNftStandard` flag is on.

## Standard Schemas

`TokenSchemasBuilder.PrepareStandardTokenSchemas(sharedMetadata)` returns the standard set:

| `sharedMetadata` | The standard fields live in | Use it when |
| --- | --- | --- |
| `false` (default) | The ROM of each NFT | Every NFT has its own name, image and royalties. |
| `true` | The series metadata | All NFTs of a series share them. |

The RAM schema of the standard set has no fields and allows extra dynamic fields.

```csharp
using PhantasmaPhoenix.Protocol.Carbon.Blockchain.Modules.Builders;

var perNft = TokenSchemasBuilder.PrepareStandardTokenSchemas();
var shared = TokenSchemasBuilder.PrepareStandardTokenSchemas(sharedMetadata: true);

// The bytes TokenInfoBuilder.Build takes as tokenSchemas.
var schemaBytes = TokenSchemasBuilder.Serialize(perNft);
```

## Custom Schemas From JSON

`TokenSchemasBuilder.FromJson(json)` builds the schemas from a JSON object with three arrays. Each entry names a field and its type. The SDK adds its own fields from the table above, and `FromJson` runs `Verify`, so the standard fields must be in one of the arrays:

```csharp
using PhantasmaPhoenix.Protocol.Carbon.Blockchain.Modules.Builders;

var schemas = TokenSchemasBuilder.FromJson("""
{
  "seriesMetadata": [],
  "rom": [
    { "name": "name", "type": "String" },
    { "name": "description", "type": "String" },
    { "name": "imageURL", "type": "String" },
    { "name": "infoURL", "type": "String" },
    { "name": "royalties", "type": "Int32" },
    { "name": "power", "type": "Int64" }
  ],
  "ram": [
    { "name": "level", "type": "Int32" }
  ]
}
""");
```

The type names are `Dynamic`, `Bytes`, `Struct`, `Int8`, `Int16`, `Int32`, `Int64`, `Int256`, `Bytes16`, `Bytes32`, `Bytes64`, `String`, `Array`, and the arrays `Array_Dynamic`, `Array_Bytes`, `Array_Struct`, `Array_Int8`, `Array_Int16`, `Array_Int32`, `Array_Int64`, `Array_Int256`, `Array_Bytes16`, `Array_Bytes32`, `Array_Bytes64`, `Array_String`. An unknown name throws. An empty `ram` array gives a RAM schema without fields that allows extra dynamic fields; a non-empty one gives exactly the listed fields.

## Series Metadata

`SeriesInfoBuilder.Build(seriesId, maxMint, maxSupply, owner)` writes the series metadata of the standard per-NFT schemas: the id, `mode` `0` and an empty shared ROM. A token with other series fields builds the metadata itself and passes it as the last argument:

```csharp
using System.Numerics;
using PhantasmaPhoenix.Protocol.Carbon;
using PhantasmaPhoenix.Protocol.Carbon.Blockchain.Modules.Builders;

var schemas = TokenSchemasBuilder.PrepareStandardTokenSchemas(sharedMetadata: true);
var seriesId = IdHelper.GetRandomPhantasmaId();
var owner = new Bytes32(new byte[32]); // the owner's 32-byte public key

var seriesMetadata = TokenSeriesMetadataBuilder.BuildAndSerialize(schemas.seriesMetadata, seriesId, new[]
{
	new MetadataField("name", "Example Collection"),
	new MetadataField("description", "One image for every NFT of the series"),
	new MetadataField("imageURL", "https://example.invalid/collection.png"),
	new MetadataField("infoURL", "https://example.invalid/collection"),
	new MetadataField("royalties", 10_000_000), // 1%
});

var series = SeriesInfoBuilder.Build(seriesId, maxMint: 1000, maxSupply: 0, owner, seriesMetadata);
```

A `rom` field in the list makes the series one whose NFTs share that ROM: the builder sets `mode` to `1`. Without it, `mode` is `0`.

## Values

`MetadataField(name, value)` pairs a field name with a value. Names match the schema exactly, including case. The builders convert each value to the type of its schema field and throw when it does not fit: a string field takes a non-empty string, an integer field a number in its range, a `Bytes` field a byte array or a hex string.

## Related Pages

{% content-ref url="/developers/sdks/csharp/token-deployment.md" %}
Token Deployment
{% endcontent-ref %}

{% content-ref url="/developers/sdks/csharp/nft-minting.md" %}
NFT Minting
{% endcontent-ref %}

{% content-ref url="/developers/sdks/csharp/reference/carbon-and-nft-types.md" %}
Carbon and NFT Types
{% endcontent-ref %}
