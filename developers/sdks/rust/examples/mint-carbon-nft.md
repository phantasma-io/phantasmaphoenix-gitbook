# Mint Carbon NFT

This example builds and signs a Carbon NFT mint transaction without
broadcasting it.

```rust
use phantasma_sdk::{
    build_mint_non_fungible_tx_and_sign_hex, build_nft_rom, bytes32_from_public_key,
    prepare_standard_token_schemas, PhantasmaKeys, Result, VMValue,
};

fn main() -> Result<()> {
    let keys = PhantasmaKeys::generate();
    let receiver = bytes32_from_public_key(&keys.public_key())?;
    let schemas = prepare_standard_token_schemas(false);

    let rom = build_nft_rom(
        &schemas.rom,
        1i64,
        &[
            ("name", VMValue::String("Example NFT #1".to_string())),
            ("description", VMValue::String("Example NFT metadata".to_string())),
            ("imageURL", VMValue::String("https://example.invalid/nft-1.png".to_string())),
            ("infoURL", VMValue::String("https://example.invalid/nft-1".to_string())),
            ("royalties", VMValue::Int(10_000_000)),
        ],
    )?;

    let mint_hex = build_mint_non_fungible_tx_and_sign_hex(
        123,
        1,
        &keys,
        receiver,
        rom,
        vec![],
        None,
        100_000_000,
        0,
    )?;

    println!("signer: {}", keys.address().to_text());
    println!("mint tx: {mint_hex}");
    Ok(())
}
```

Replace `token_id` and `series_id` with the Carbon ids returned by the
confirmed token and series deployment transactions.
