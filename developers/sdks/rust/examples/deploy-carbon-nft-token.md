# Deploy Carbon NFT Token

This example builds the `CreateToken` and `CreateTokenSeries` transaction
payloads for a standard Carbon NFT collection. It prints signed transaction
hex, but does not broadcast.

```rust
use phantasma_sdk::{
    build_create_token_series_tx_and_sign_hex, build_create_token_tx_and_sign_hex,
    build_series_info, build_token_info, build_token_metadata, bytes32_from_public_key,
    prepare_standard_token_schemas, serialize, IntX, PhantasmaKeys, Result,
};

fn main() -> Result<()> {
    let keys = PhantasmaKeys::generate();
    let owner = bytes32_from_public_key(&keys.public_key())?;
    let schemas = prepare_standard_token_schemas(false);

    let token_info = build_token_info(
        "ART",
        IntX::from(0i64),
        true,
        0,
        owner,
        build_token_metadata(&[
            ("name", "Example Art Token"),
            ("icon", "data:image/png;base64,AA=="),
            ("url", "https://example.invalid/art"),
            ("description", "Example NFT collection"),
        ])?,
        serialize(&schemas)?,
    )?;

    let create_token_hex = build_create_token_tx_and_sign_hex(token_info, &keys)?;
    println!("signer: {}", keys.address().to_text());
    println!("create token tx: {create_token_hex}");

    let carbon_token_id = 123;
    let series_info = build_series_info(1i64, 0, 0, owner)?;

    let create_series_hex =
        build_create_token_series_tx_and_sign_hex(carbon_token_id, series_info, &keys)?;
    println!("create series tx: {create_series_hex}");

    Ok(())
}
```

For live deployment, send `create_token_hex` first, wait for confirmation, parse
the Carbon token id from the transaction result, and then build the series
transaction with that id.
