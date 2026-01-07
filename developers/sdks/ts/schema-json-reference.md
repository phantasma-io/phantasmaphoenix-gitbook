# Schema JSON Reference (TS SDK)

This page documents the JSON format accepted by `TokenSchemasBuilder.fromJson` in `phantasma-sdk-ts`.

## JSON shape

```json
{
  "seriesMetadata": [
    { "name": "name", "type": "String" }
  ],
  "rom": [
    { "name": "artist", "type": "String" }
  ],
  "ram": [
    { "name": "level", "type": "Int32" }
  ]
}
```

Rules:
- `seriesMetadata`, `rom`, and `ram` must be JSON arrays (they can be empty).
- Each entry must be an object with `name` (string) and `type` (string).
- `type` is a `VmType` name string; see the list below.
- Field names are case-sensitive.

## Accepted type strings

The `type` value must be one of the strings accepted by `vmTypeFromString`:

- `Dynamic`, `Array`
- `Bytes`, `Bytes16`, `Bytes32`, `Bytes64`
- `Struct`
- `Int8`, `Int16`, `Int32`, `Int64`, `Int256`
- `String`
- `Array_Dynamic`, `Array_Bytes`, `Array_Struct`
- `Array_Int8`, `Array_Int16`, `Array_Int32`, `Array_Int64`, `Array_Int256`
- `Array_Bytes16`, `Array_Bytes32`, `Array_Bytes64`
- `Array_String`

Notes:
- The JSON arrays above describe **schema fields**. They are not related to `Array_*` type strings.
- `Array_*` types are field types; use them when a **field** itself stores an array.

## Default/system fields

`TokenSchemasBuilder` always adds default fields, so you should not include them in JSON:

- Series metadata: `_i`, `mode`, `rom`.
- NFT ROM schema: `_i`, `rom`.

## Standard NFT fields requirement

When using `fromJson`, the builder verifies that the standard NFT fields exist in either
`seriesMetadata` or the NFT `rom` schema:

- `name`
- `description`
- `imageURL`
- `infoURL`
- `royalties`

## RAM and DynamicExtras

If `ram` is an empty array, the SDK sets the RAM schema flag `DynamicExtras`. This causes
extra RAM fields (not defined in the schema) to be serialized. When you define RAM fields,
`DynamicExtras` is not set, so only schema-defined RAM fields are serialized. This means any
extra RAM fields you include are dropped and cannot be read or updated later.
