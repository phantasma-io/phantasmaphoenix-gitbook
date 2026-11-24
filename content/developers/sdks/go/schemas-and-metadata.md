---
title: "Go SDK Schemas And Metadata"
linkTitle: "Schemas And Metadata"
weight: 80
---

Every token carries metadata. An NFT token also carries three schemas, which
fix the fields of its series and of each NFT. The chain checks series metadata
against the token's schemas and every minted ROM against the ROM schema. The
builders live in `github.com/phantasma-io/phantasma-sdk-go/pkg/carbon`.

## Token Metadata

`BuildTokenMetadata(fields)` takes a `map[string]string` and returns the
serialized metadata for `BuildTokenInfo`. It requires four fields:

| Field | Rule |
| ----- | ---- |
| `name` | Not blank. |
| `icon` | A base64 data URI of a PNG, JPEG or WebP image, `data:image/png;base64,...`, with a valid, non-empty base64 payload. |
| `url` | Not blank. |
| `description` | Not blank. |

More fields can be added. Every value is stored as a string, and the fields are
sorted by name, so the same map always gives the same bytes. A missing or blank
required field, or a bad icon, returns an error. `MustBuildTokenMetadata`
panics instead.

## The Three NFT Schemas

| Schema | `TokenSchemas` field | Describes | Fields the SDK adds |
| ------ | -------------------- | --------- | ------------------- |
| Series metadata | `SeriesMetadata` | The metadata of each series | `_i` (`Int256`): the series id; `mode` (`Int8`): `0` for unique NFTs, `1` for a series whose NFTs share one ROM; `rom` (`Bytes`): that shared ROM |
| ROM | `ROM` | The read-only data of each NFT | `_i` (`Int256`): the NFT id; `rom` (`Bytes`): raw ROM bytes |
| RAM | `RAM` | The data of each NFT that can change | none |

The five standard NFT fields, `name`, `description`, `imageURL`, `infoURL`
(strings) and `royalties` (`Int32`), must appear in the series metadata schema
or in the ROM schema. `VerifyTokenSchemas` checks that, and the chain requires
them while its `RequireNFTStandard` flag is on, as it is on mainnet.

## Standard Schemas

`PrepareStandardTokenSchemas(sharedMetadata)` returns the standard set:

| `sharedMetadata` | The standard fields live in | Use it when |
| ---------------- | --------------------------- | ----------- |
| `false` | The ROM of each NFT | Every NFT has its own name, image and royalties. |
| `true` | The series metadata | All NFTs of a series share them. |

The RAM schema of the standard set has no fields and accepts any extra fields.

```go
perNFT := carbon.PrepareStandardTokenSchemas(false)
shared := carbon.PrepareStandardTokenSchemas(true)

// The bytes BuildTokenInfo takes as its schemas argument.
schemaBytes := carbon.SerializeTokenSchemas(perNFT)
```

## Custom Schemas From JSON

`TokenSchemasFromJSON(json)` builds the schemas from a JSON object with the three
arrays `seriesMetadata`, `rom` and `ram`; each must be present, even when
empty. Each entry names a field and its type:

```go
schemas, err := carbon.TokenSchemasFromJSON(`{
  "seriesMetadata": [],
  "rom": [
    {"name": "name", "type": "String"},
    {"name": "description", "type": "String"},
    {"name": "imageURL", "type": "String"},
    {"name": "infoURL", "type": "String"},
    {"name": "royalties", "type": "Int32"},
    {"name": "artist", "type": "String"}
  ],
  "ram": [{"name": "level", "type": "Int32"}]
}`)
if err != nil {
    return err
}
```

The type names are `Dynamic`, `Bytes`, `Struct`, `Int8`, `Int16`, `Int32`,
`Int64`, `Int256`, `Bytes16`, `Bytes32`, `Bytes64`, `String`, `Array`, and the
arrays `Array_Dynamic`, `Array_Bytes`, `Array_Struct`, `Array_Int8`,
`Array_Int16`, `Array_Int32`, `Array_Int64`, `Array_Int256`, `Array_Bytes16`,
`Array_Bytes32`, `Array_Bytes64`, `Array_String`. The array names are also
accepted without the underscore. An unknown name returns an error.

## Custom Schemas From Fields

`BuildTokenSchemasFromFields(seriesMetadata, rom, ram)` takes the same
declarations as Go values:

```go
schemas, err := carbon.BuildTokenSchemasFromFields(
    nil,
    []carbon.FieldType{
        {Name: "name", Type: carbon.VMTypeString},
        {Name: "description", Type: carbon.VMTypeString},
        {Name: "imageURL", Type: carbon.VMTypeString},
        {Name: "infoURL", Type: carbon.VMTypeString},
        {Name: "royalties", Type: carbon.VMTypeInt32},
        {Name: "artist", Type: carbon.VMTypeString},
    },
    nil,
)
if err != nil {
    return err
}
```

Both functions add the fields from the table above, so leave `_i`, `mode` and
`rom` out of the declarations, and then run `VerifyTokenSchemas`. An empty `ram`
list gives a RAM schema without fields that accepts any extra fields; a
non-empty one gives exactly the listed fields.

## Series Metadata

`BuildSeriesInfo(seriesID, maxMint, maxSupply, owner)` builds a series for the
per-NFT standard schemas: the metadata holds the series id, `mode` `0` and an
empty shared ROM. A token with other series fields builds the metadata itself
with `BuildTokenSeriesMetadata` and puts it into the `SeriesInfo`:

```go
schemas := carbon.PrepareStandardTokenSchemas(true)
seriesID := big.NewInt(1) // unique within the token

metadata, err := carbon.BuildTokenSeriesMetadata(schemas.SeriesMetadata, seriesID, []carbon.MetadataField{
    {Name: "name", Value: "Example Collection"},
    {Name: "description", Value: "One image for every NFT of the series"},
    {Name: "imageURL", Value: "https://example.invalid/collection.png"},
    {Name: "infoURL", Value: "https://example.invalid/collection"},
    {Name: "royalties", Value: int32(10_000_000)}, // 1%
})
if err != nil {
    return err
}

series := carbon.SeriesInfo{
    MaxMint:   1000,
    MaxSupply: 0,
    Owner:     owner, // signs every mint into the series
    Metadata:  metadata,
}
```

A `rom` field in the list, as bytes or hex text, makes the series one whose
NFTs share that ROM: the builder sets `mode` to `1`. Without it, `mode` is `0`.

## NFT ROM

`BuildPhantasmaNFTRom(romSchema, fields)` writes the ROM of one NFT for
`Token.MintPhantasmaNonFungible`. The chain derives the NFT id itself, so the
builder leaves out `_i` and `rom` and refuses those names. It writes one value
for every other field of the schema, in the schema's order. A missing field, or
a field name in the wrong case, returns an error; a field the schema does not
name is ignored. [NFT Minting](nft-minting.md) shows it in a
mint.

`BuildNFTRom(romSchema, nftID, fields)` writes the full ROM with a
caller-chosen `_i`, for a direct `MintNonFungible`. The chain refuses that call
while its configuration disables caller-chosen NFT ids, which is the state of
mainnet.

## RAM

A mint passes RAM bytes next to the ROM. `nil` gives an empty RAM. With the
standard RAM schema, any named values can be written:

```go
ram := carbon.VMDynamicStruct{Fields: []carbon.VMNamedDynamicVariable{
    carbon.MustVMNamedDynamicVariable("level", carbon.VMTypeInt32, int32(1)),
}}

w := carbon.NewWriter()
if !ram.WriteWithSchema(&schemas.RAM, w) {
    return fmt.Errorf("RAM does not match the schema")
}
ramBytes := w.Bytes()
```

With a RAM schema that lists fields, the struct supplies exactly those fields. A
script transaction changes the RAM of an NFT later with the `Runtime.WriteToken`
interop; see [Interop](../../blockchain/chain/information/virtual-machine/interop.md).

## Values

`MetadataField{Name, Value}` pairs a field name with a value. Names match the
schema exactly, including case. The value's Go type has to fit the field's type:

| Field type | Go value |
| ---------- | -------- |
| `String` | `string` |
| `Int8`, `Int16`, `Int32`, `Int64` | `int`, `int8`, `int16`, `int32`, `int64`, `uint`, `uint8`, `uint16`, `uint32` or `uint64` |
| `Int256` | `*big.Int`, `big.Int`, `carbon.IntX`, `int`, `int64` or `uint64` |
| `Bytes` | `[]byte`, `carbon.Bytes16`, `carbon.Bytes32` or `carbon.Bytes64` |
| `Bytes16`, `Bytes32`, `Bytes64` | `carbon.Bytes16`, `carbon.Bytes32`, `carbon.Bytes64` |
| `Struct` | `carbon.VMDynamicStruct` |
| `Array_String`, `Array_Int32` and the other arrays | The matching slice, for example `[]string`, `[]int32`, `[][]byte`, `[]*big.Int`; `carbon.VMStructArray` for `Array_Struct` |

An integer field takes a value in the signed or the unsigned range of its width:
`Int32` takes -2,147,483,648 to 4,294,967,295, and a value above 2,147,483,647
is stored as its two's complement. A value outside that range, or a value of
another Go type, returns an error that names the field.

## Related Pages

- [Token Deployment](token-deployment.md)
- [NFT Minting](nft-minting.md)
- [Carbon API and Wire Format](reference/carbon-wire.md)
