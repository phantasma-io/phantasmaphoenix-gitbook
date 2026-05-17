# Go SDK Schemas And Metadata

Carbon NFT metadata is schema-driven. The Go SDK models token schemas as
`TokenSchemas`, with separate structures for series metadata, NFT ROM, and NFT
RAM.

## Standard Schemas

```go
schemas := carbon.PrepareStandardTokenSchemas(false)
```

`sharedMetadata = true` places standard display fields in series metadata.
`sharedMetadata = false` places them in NFT ROM. Standard display fields are:

| Field | Type |
| ----- | ---- |
| `name` | `String` |
| `description` | `String` |
| `imageURL` | `String` |
| `infoURL` | `String` |
| `royalties` | `Int32` |

Standard series and NFT system fields such as `_i`, `mode`, and `rom` are added
by the SDK. Do not include them in public mint metadata.

## Custom Schemas

Use field declarations when the schema is built in Go:

```go
schemas, err := carbon.BuildTokenSchemasFromFields(
    nil,
    []carbon.FieldType{
        {Name: "artist", Type: carbon.VMTypeString},
    },
    nil,
)
```

Use JSON when the schema comes from configuration or another tool:

```go
schemas, err := carbon.TokenSchemasFromJSON(`{
  "seriesMetadata": [],
  "rom": [{"name":"artist","type":"String"}],
  "ram": [{"name":"level","type":"Int32"}]
}`)
```

The parser expects `seriesMetadata`, `rom`, and `ram` arrays of objects with
string `name` and `type` fields.

## Metadata Builders

| Helper | Use it for |
| ------ | ---------- |
| `BuildTokenMetadata` | Token-level metadata for create-token calls. |
| `BuildTokenSeriesMetadata` | Series metadata encoded according to a series metadata schema. |
| `BuildNFTRom` | Direct Carbon NFT ROM with caller-provided Phantasma NFT id. |
| `BuildPhantasmaNFTRom` | Public deterministic Phantasma NFT ROM without chain-owned fields. |
| `VerifyTokenSchemas` | Required standard-field validation before deployment. |

Use checked builders for user input. `MustBuild...` variants panic and should
be limited to tests and hardcoded constants.
