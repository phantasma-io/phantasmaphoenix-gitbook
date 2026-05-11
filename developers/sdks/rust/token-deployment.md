# Rust SDK Token Deployment

This page shows the Carbon token deployment flow in `phantasma_sdk`. It builds
native Carbon transaction messages, signs them locally, and shows where to
broadcast and parse results.

## Flow

Carbon NFT deployment has three steps:

1. Build token metadata and schemas.
2. Sign and broadcast `CreateToken`.
3. Parse the returned Carbon token id and use it when creating series or
   minting NFTs.

Series creation is a separate transaction after the token exists:

1. Build `SeriesInfo`.
2. Sign and broadcast `CreateTokenSeries`.
3. Parse the returned Carbon series id and use it when minting.

The SDK does not hide broadcasting. `send_carbon_transaction(...)` sends signed
bytes to the selected RPC endpoint, so use it only with an intentional endpoint,
funded signing key, and final wallet/operator approval.

## Build Token Metadata

Token metadata is required for all Carbon tokens. The SDK validates the four
required string fields and the icon data URI.

```rust
use phantasma_sdk::{build_token_metadata, Result};

fn metadata() -> Result<Vec<u8>> {
    build_token_metadata(&[
        ("name", "Example Art Token"),
        ("icon", "data:image/png;base64,AA=="),
        ("url", "https://example.invalid/art"),
        ("description", "Example NFT collection"),
    ])
}
```

Rules enforced by the SDK:

- `name`, `icon`, `url`, and `description` must be present and non-empty.
- `icon` must be a PNG, JPEG, or WebP data URI with non-empty base64 data.
- Token symbols must contain uppercase ASCII letters `A-Z`.

## Build NFT Schemas

For a standard NFT collection, use `prepare_standard_token_schemas(false)`.
With `shared_metadata=false`, the standard NFT fields are stored per NFT in
ROM.

```rust
use phantasma_sdk::{prepare_standard_token_schemas, serialize, Result};

fn token_schemas() -> Result<Vec<u8>> {
    let schemas = prepare_standard_token_schemas(false);
    serialize(&schemas)
}
```

The standard NFT fields are:

- `name`
- `description`
- `imageURL`
- `infoURL`
- `royalties`

Use `shared_metadata=true` only when those standard fields should live in
series metadata instead of each NFT ROM.

## Build And Sign CreateToken

```rust
use phantasma_sdk::{
    build_create_token_tx_and_sign_hex, build_token_info, build_token_metadata,
    bytes32_from_public_key, prepare_standard_token_schemas, serialize, IntX,
    PhantasmaKeys, Result,
};

fn build_create_token_hex(wif: &str) -> Result<String> {
    let keys = PhantasmaKeys::from_wif(wif)?;
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

    build_create_token_tx_and_sign_hex(token_info, &keys)
}
```

For NFT tokens:

- `is_nft=true` sets the non-fungible token flag.
- `decimals` should be `0`.
- `IntX::from(0i64)` as max supply means unlimited supply.
- token schemas are required.

## Broadcast And Parse Token Id

```rust
use phantasma_sdk::{parse_create_token_result, PhantasmaRpc, Result};

async fn broadcast_create_token(rpc: &PhantasmaRpc, tx_hex: &str) -> Result<u64> {
    let tx_bytes = phantasma_sdk::decode_hex(tx_hex)?;
    let tx_hash = rpc.send_carbon_transaction(&tx_bytes).await?;

    let tx_result = rpc.get_transaction(&tx_hash).await?;
    parse_create_token_result(&tx_result.result)
}
```

This broadcast block is live network code. The SDK tests verify serialization,
signing, and result parsing; funded live broadcasting must be done by the
caller on the intended network.

## Build And Sign CreateTokenSeries

Use the Carbon token id returned by `CreateToken`.

```rust
use phantasma_sdk::{
    build_create_token_series_tx_and_sign_hex, build_series_info,
    bytes32_from_public_key, PhantasmaKeys, Result,
};

fn build_create_series_hex(wif: &str, carbon_token_id: u64) -> Result<String> {
    let keys = PhantasmaKeys::from_wif(wif)?;
    let owner = bytes32_from_public_key(&keys.public_key())?;

    let series_info = build_series_info(
        1i64,
        0,
        0,
        owner,
    )?;

    build_create_token_series_tx_and_sign_hex(carbon_token_id, series_info, &keys)
}
```

`max_mint=0` and `max_supply=0` leave those series limits unlimited. Use
positive values when the collection needs explicit caps.

## Broadcast And Parse Series Id

```rust
use phantasma_sdk::{parse_create_token_series_result, PhantasmaRpc, Result};

async fn broadcast_create_series(rpc: &PhantasmaRpc, tx_hex: &str) -> Result<u32> {
    let tx_bytes = phantasma_sdk::decode_hex(tx_hex)?;
    let tx_hash = rpc.send_carbon_transaction(&tx_bytes).await?;

    let tx_result = rpc.get_transaction(&tx_hash).await?;
    parse_create_token_series_result(&tx_result.result)
}
```

Use the parsed `carbon_series_id` when minting Carbon NFTs.

## Read Back Deployment State

After the deployment transactions are confirmed, read the token and series
through RPC:

```rust
let token = rpc.get_token("ART", true).await?;
let series_page = rpc.get_token_series("ART", carbon_token_id, 100, "").await?;

println!("{} {}", token.symbol, token.carbon_id);
println!("cursor={}", series_page.cursor);
```

`get_token_series_by_id(symbol, series_id)` fetches one known series by
Phantasma series id. Use `get_token_series_by_ids(symbol, carbon_token_id,
series_id, carbon_series_id)` when your read-back state is keyed by the Carbon
token id and Carbon series id returned by the deployment transactions.
