# Python SDK Schemas And Metadata

Carbon NFT workflows use two different metadata layers:

- Token metadata: required for every token, fungible or NFT.
- NFT schemas and metadata: required for NFT token series and minted NFT data.

The SDK validates both layers before it serializes Carbon bytes.

## Token Metadata

Token metadata is a dynamic VM struct built by `build_token_metadata(...)`.

Required fields:

| Field | Meaning |
| ----- | ------- |
| `name` | Display name. |
| `icon` | PNG, JPEG, or WebP data URI with a non-empty base64 payload. |
| `url` | Project or token URL. |
| `description` | Token description. |

```python
from phantasma_py.carbon import build_token_metadata

metadata = build_token_metadata(
    {
        "name": "Example Token",
        "icon": "data:image/png;base64,AA==",
        "url": "https://example.invalid/token",
        "description": "Example token metadata",
    }
)
```

The helper raises `BuilderError` when a required field is missing, blank, or the
icon is not a supported data URI.

## Standard NFT Schemas

```python
from phantasma_py.carbon import prepare_standard_token_schemas

schemas = prepare_standard_token_schemas(shared_metadata=False)
```

`shared_metadata=False` puts the standard NFT fields in ROM, so each NFT can
have its own `name`, `description`, `imageURL`, `infoURL`, and `royalties`.

```python
schemas = prepare_standard_token_schemas(shared_metadata=True)
```

`shared_metadata=True` puts those standard NFT fields in series metadata, so the
fields are shared by the whole series.

The standard system fields are inserted by the SDK:

| Location | System fields |
| -------- | ------------- |
| Series metadata | `_i`, `mode`, `rom` |
| NFT ROM | `_i`, `rom` |

Do not add those fields as custom fields.

## Custom Schema JSON

Use JSON when a tool or UI needs to store schema declarations outside Python.

```python
from phantasma_py.carbon import token_schemas_from_json

schemas = token_schemas_from_json(
    """
    {
      "seriesMetadata": [
        { "name": "season", "type": "String" }
      ],
      "rom": [
        { "name": "artist", "type": "String" },
        { "name": "rarity", "type": "Int32" }
      ],
      "ram": [
        { "name": "level", "type": "Int32" }
      ]
    }
    """
)
```

The JSON object must contain `seriesMetadata`, `rom`, and `ram` arrays. Each
entry is an object with `name` and `type`.

Supported type names:

| Family | Names |
| ------ | ----- |
| Scalar | `Dynamic`, `Bytes`, `Struct`, `Int8`, `Int16`, `Int32`, `Int64`, `Int256`, `Bytes16`, `Bytes32`, `Bytes64`, `String` |
| Arrays | `Array_Dynamic`, `Array_Bytes`, `Array_Struct`, `Array_Int8`, `Array_Int16`, `Array_Int32`, `Array_Int64`, `Array_Int256`, `Array_Bytes16`, `Array_Bytes32`, `Array_Bytes64`, `Array_String` |

`ArrayString` and similar names are accepted by `vm_type_from_string(...)`, but
the canonical names returned by `vm_type_name(...)` use the underscore form.

## Build Schemas From Fields

```python
from phantasma_py.carbon import build_token_schemas_from_fields

schemas = build_token_schemas_from_fields(
    series_metadata=[("season", "String")],
    rom=[("artist", "String"), ("rarity", "Int32")],
    ram=[("level", "Int32")],
)
```

The SDK adds the standard system fields and then verifies that required NFT
metadata fields exist either in series metadata or ROM.

## RAM Dynamic Extras

When the RAM field list is empty, the SDK sets the RAM schema flag
`DYNAMIC_EXTRAS`. That allows extra RAM fields to be serialized. When you define
explicit RAM fields, `DYNAMIC_EXTRAS` is not set and only declared RAM fields
are serialized.

```python
from phantasma_py.carbon import VMStructFlags, prepare_standard_token_schemas

schemas = prepare_standard_token_schemas(shared_metadata=False)

assert schemas.ram.flags & VMStructFlags.DYNAMIC_EXTRAS
```

## Series Metadata

```python
from phantasma_py.carbon import VMType, build_token_series_metadata

metadata = build_token_series_metadata(
    schemas.series_metadata,
    phantasma_series_id=42,
    metadata=[
        ("name", "Series One"),
        ("description", "Shared series metadata"),
        ("imageURL", "https://example.invalid/series.png"),
        ("infoURL", "https://example.invalid/series"),
        ("royalties", 10_000_000),
    ],
)
```

Use a series schema that matches the token you deployed. If the token was built
with custom schemas, keep those schema bytes and reuse them when creating series
or ROM data.

## NFT ROM

```python
from phantasma_py.carbon import build_nft_rom

rom = build_nft_rom(
    schemas.rom,
    phantasma_nft_id=1001,
    metadata=[
        ("name", "NFT #1001"),
        ("description", "Per-NFT metadata"),
        ("imageURL", "https://example.invalid/nft.png"),
        ("infoURL", "https://example.invalid/nft/1001"),
        ("royalties", 10_000_000),
        ("artist", "Ada"),
        ("rarity", 5),
    ],
)
```

Field names are case-sensitive. Metadata values are coerced according to the VM
types in the schema, including fixed byte widths and signed integer bounds.

## Phantasma NFT Public Mint ROM

`build_phantasma_nft_rom(...)` is for the Phantasma NFT helper flow. It removes
chain-owned deterministic fields from the public mint schema and rejects
metadata entries named `_i` or `rom`.

```python
from phantasma_py.carbon import build_phantasma_nft_rom

public_rom = build_phantasma_nft_rom(
    schemas.rom,
    [
        ("name", "NFT #1001"),
        ("description", "Minted through Phantasma NFT helper"),
        ("imageURL", "https://example.invalid/nft.png"),
        ("infoURL", "https://example.invalid/nft/1001"),
        ("royalties", 10_000_000),
    ],
)
```

Use `build_nft_rom(...)` for direct Carbon `MintNonFungible`. Use
`build_phantasma_nft_rom(...)` with `build_mint_phantasma_non_fungible_*`.
