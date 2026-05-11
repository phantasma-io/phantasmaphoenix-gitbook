# Rust Example: Custom Token Schema

This example builds custom NFT schemas and serializes ROM metadata offline. It
does not deploy a token or broadcast a transaction.

```rust
use phantasma_sdk::{
    build_nft_rom, build_token_schemas_from_fields, serialize_token_schemas_hex, Result,
    TokenSchemaField, VMType, VMValue,
};

fn main() -> Result<()> {
    let schemas = build_token_schemas_from_fields(
        &[],
        &[
            TokenSchemaField::new("name", VMType::String),
            TokenSchemaField::new("description", VMType::String),
            TokenSchemaField::new("imageURL", VMType::String),
            TokenSchemaField::new("infoURL", VMType::String),
            TokenSchemaField::new("royalties", VMType::Int32),
            TokenSchemaField::new("artist", VMType::String),
            TokenSchemaField::new("rarity", VMType::Int32),
        ],
        &[TokenSchemaField::new("level", VMType::Int32)],
    )?;

    let rom = build_nft_rom(
        &schemas.rom,
        1001i64,
        &[
            ("name", VMValue::String("Example #1001".to_string())),
            ("description", VMValue::String("Custom schema NFT".to_string())),
            ("imageURL", VMValue::String("https://example.invalid/nft.png".to_string())),
            ("infoURL", VMValue::String("https://example.invalid/nft/1001".to_string())),
            ("royalties", VMValue::Int(10_000_000)),
            ("artist", VMValue::String("Ada".to_string())),
            ("rarity", VMValue::Int(5)),
        ],
    )?;

    println!("schemas: {}", serialize_token_schemas_hex(&schemas)?);
    println!("rom: {}", phantasma_sdk::encode_hex(rom));

    Ok(())
}
```

The standard NFT fields are still required. Custom fields are additional fields,
not replacements for `name`, `description`, `imageURL`, `infoURL`, and
`royalties`.
