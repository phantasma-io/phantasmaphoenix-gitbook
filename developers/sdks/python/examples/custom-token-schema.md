# Python Example: Custom Token Schema

This example builds custom NFT schemas and serializes ROM metadata offline. It
does not deploy a token or broadcast a transaction.

```python
from phantasma_py.carbon import (
    build_nft_rom,
    build_token_schemas_from_fields,
    serialize_token_schemas_hex,
)

schemas = build_token_schemas_from_fields(
    series_metadata=[],
    rom=[
        ("name", "String"),
        ("description", "String"),
        ("imageURL", "String"),
        ("infoURL", "String"),
        ("royalties", "Int32"),
        ("artist", "String"),
        ("rarity", "Int32"),
    ],
    ram=[
        ("level", "Int32"),
    ],
)

rom = build_nft_rom(
    schemas.rom,
    phantasma_nft_id=1001,
    metadata=[
        ("name", "Example #1001"),
        ("description", "Custom schema NFT"),
        ("imageURL", "https://example.invalid/nft.png"),
        ("infoURL", "https://example.invalid/nft/1001"),
        ("royalties", 10_000_000),
        ("artist", "Ada"),
        ("rarity", 5),
    ],
)

print("schemas:", serialize_token_schemas_hex(schemas))
print("rom:", rom.hex())
```

The standard NFT fields are still required. Custom fields are additional fields,
not replacements for `name`, `description`, `imageURL`, `infoURL`, and
`royalties`.
