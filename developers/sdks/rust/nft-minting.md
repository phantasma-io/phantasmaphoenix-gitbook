# Rust SDK NFT Minting

This page covers Carbon NFT minting with `phantasma_sdk`. It starts after an
NFT token and series already exist.

## Required Inputs

You need:

- a funded signing key;
- the Carbon token id returned by `CreateToken`;
- the Carbon series id returned by `CreateTokenSeries`;
- the token schemas used by the token;
- a receiver as `Bytes32`;
- ROM metadata that matches the token ROM schema.

The standard NFT ROM fields are:

- `name`
- `description`
- `imageURL`
- `infoURL`
- `royalties`

`royalties` is the integer on-chain royalty value. `10_000_000` represents 1%.

## Build Standard NFT ROM

```rust
use phantasma_sdk::{
    build_nft_rom, prepare_standard_token_schemas, Result, VMValue,
};

fn build_rom() -> Result<Vec<u8>> {
    let schemas = prepare_standard_token_schemas(false);

    build_nft_rom(
        &schemas.rom,
        1i64,
        &[
            ("name", VMValue::String("Example NFT #1".to_string())),
            ("description", VMValue::String("Example NFT metadata".to_string())),
            ("imageURL", VMValue::String("https://example.invalid/nft-1.png".to_string())),
            ("infoURL", VMValue::String("https://example.invalid/nft-1".to_string())),
            ("royalties", VMValue::Int(10_000_000)),
        ],
    )
}
```

`build_nft_rom(...)` adds the chain-owned `_i` field from the Phantasma NFT id
and serializes every schema field with type checks.

## Build And Sign MintNonFungible

```rust
use phantasma_sdk::{
    build_mint_non_fungible_tx_and_sign_hex, bytes32_from_public_key,
    PhantasmaKeys, Result,
};

fn build_mint_hex(wif: &str, rom: Vec<u8>) -> Result<String> {
    let keys = PhantasmaKeys::from_wif(wif)?;
    let receiver = bytes32_from_public_key(&keys.public_key())?;

    build_mint_non_fungible_tx_and_sign_hex(
        123,
        1,
        &keys,
        receiver,
        rom,
        vec![],
        None,
        100_000_000,
        0,
    )
}
```

The empty `vec![]` is RAM bytes. Pass serialized RAM bytes only when the token
has a RAM schema or when the token uses dynamic RAM extras.

## Broadcast And Parse Mint Result

```rust
use phantasma_sdk::{parse_mint_non_fungible_result, PhantasmaRpc, Result};

async fn broadcast_mint(
    rpc: &PhantasmaRpc,
    carbon_token_id: u64,
    tx_hex: &str,
) -> Result<Vec<phantasma_sdk::Bytes32>> {
    let tx_bytes = phantasma_sdk::decode_hex(tx_hex)?;
    let tx_hash = rpc.send_carbon_transaction(&tx_bytes).await?;

    let tx_result = rpc.get_transaction(&tx_hash).await?;
    parse_mint_non_fungible_result(carbon_token_id, &tx_result.result)
}
```

`parse_mint_non_fungible_result(...)` returns Carbon NFT addresses derived from
the Carbon token id and the instance ids emitted by the chain.

## Phantasma NFT Mint Helper

The SDK also exposes Phantasma NFT mint helpers. These use a token-module call
instead of the direct `MintNonFungible` transaction payload and return
`PhantasmaNFTMintResult` values.

Use `build_phantasma_nft_rom(...)` for the caller-provided public ROM. It
rejects reserved fields such as `_i` and `rom`, because those fields are
chain-owned for this flow.

```rust
use phantasma_sdk::{
    build_mint_phantasma_non_fungible_single_tx_and_sign_hex,
    build_phantasma_nft_rom, bytes32_from_public_key,
    prepare_standard_token_schemas, PhantasmaKeys, Result, VMValue,
};

fn build_phantasma_mint_hex(wif: &str) -> Result<String> {
    let keys = PhantasmaKeys::from_wif(wif)?;
    let receiver = bytes32_from_public_key(&keys.public_key())?;
    let schemas = prepare_standard_token_schemas(false);

    let public_rom = build_phantasma_nft_rom(
        &schemas.rom,
        &[
            ("name", VMValue::String("Example NFT #1".to_string())),
            ("description", VMValue::String("Example NFT metadata".to_string())),
            ("imageURL", VMValue::String("https://example.invalid/nft-1.png".to_string())),
            ("infoURL", VMValue::String("https://example.invalid/nft-1".to_string())),
            ("royalties", VMValue::Int(10_000_000)),
        ],
    )?;

    build_mint_phantasma_non_fungible_single_tx_and_sign_hex(
        123,
        1i64,
        &keys,
        receiver,
        public_rom,
        vec![],
        None,
        100_000_000,
        0,
    )
}
```

Parse the result with:

```rust
use phantasma_sdk::{parse_mint_phantasma_non_fungible_result, Result};

fn parse_phantasma_mint_result(
    result_hex: &str,
) -> Result<Vec<phantasma_sdk::PhantasmaNFTMintResult>> {
    parse_mint_phantasma_non_fungible_result(result_hex)
}
```

## Read Back Minted NFTs

Use the current Carbon id-aware RPC calls:

```rust
let nfts_page = rpc
    .get_token_nfts(carbon_token_id, carbon_series_id, 20, "", true, "")
    .await?;

let account_nfts = rpc
    .get_account_nfts(
        &keys.address().to_text(),
        "ART",
        carbon_token_id,
        carbon_series_id,
        20,
        "",
        true,
        false,
    )
    .await?;
```

Use the cursor returned by these calls to continue pagination.

## When To Use Each Mint Helper

| Helper | Use it when |
| ------ | ----------- |
| `build_mint_non_fungible_tx_and_sign_hex` | You already have explicit ROM/RAM bytes for the NFT. |
| `build_mint_phantasma_non_fungible_single_tx_and_sign_hex` | You want the SDK to build the token-module Phantasma NFT mint call for one NFT. |
| `build_mint_phantasma_non_fungible_tx_and_sign_hex` | You want to mint multiple Phantasma NFT entries in one token-module call. |
