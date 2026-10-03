# Rust SDK NFT Minting

This page covers Carbon NFT minting with `phantasma_sdk`. It starts after an
NFT token and series already exist.

## Required Inputs

You need:

- a funded signing key;
- the Carbon token id returned by `CreateToken`;
- the Phantasma series id used when the series was created;
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

## Build The Public ROM

`build_phantasma_nft_rom(...)` serializes the public part of the ROM. It rejects
the reserved fields `_i` and `rom`, because the chain owns them for a
deterministic mint.

Use the ROM schema the token was created with. The example continues from a
token created with `prepare_standard_token_schemas(false)`, which puts the
standard fields in the per-NFT ROM.

```rust
use phantasma_sdk::{
    build_phantasma_nft_rom, prepare_standard_token_schemas, Result, VMValue,
};

fn build_rom() -> Result<Vec<u8>> {
    let schemas = prepare_standard_token_schemas(false);

    build_phantasma_nft_rom(
        &schemas.rom,
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

`build_nft_rom(schema, phantasma_nft_id, metadata)` is the other ROM builder. It
writes the chain-owned `_i` field itself, and it serves the flows where the
caller supplies the id.

## Build, Plan, Sign And Send

```rust
use phantasma_sdk::{
    build_mint_phantasma_non_fungible_single_tx, bytes32_from_public_key, PhantasmaKeys,
    PhantasmaRpc, Result, SendTransactionOptions, TxLimits, TxSigner,
};

async fn mint(client: &PhantasmaRpc, wif: &str, public_rom: Vec<u8>) -> Result<String> {
    let keys = PhantasmaKeys::from_wif(wif)?;
    let sender = bytes32_from_public_key(&keys.public_key())?;

    let msg = build_mint_phantasma_non_fungible_single_tx(
        123,   // Carbon token id
        777i64, // Phantasma series id
        sender,
        sender, // receiver
        public_rom,
        vec![], // RAM
        TxLimits::default(),
    )?;

    let signers: [&dyn TxSigner; 1] = [&keys];
    client.send_tx_msg(&msg, &signers, &SendTransactionOptions::default()).await
}
```

The builder carries no prices. `send_tx_msg` plans the fee from the message,
signs it and broadcasts it.

The SDK carries no builder for a direct `MintNonFungible`. The chain refuses
that operation where governance has not allowed caller-supplied ROM ids, and
that is the state of the public chains today.

The empty `vec![]` is RAM bytes. Pass serialized RAM bytes only when the token
has a RAM schema or when the token uses dynamic RAM extras.

## Broadcast And Parse Mint Result

After the transaction is in a block, its result names every minted instance:

```rust
use phantasma_sdk::{
    parse_mint_phantasma_non_fungible_result, PhantasmaNFTMintResult, PhantasmaRpc, Result,
};

async fn minted_instances(rpc: &PhantasmaRpc, tx_hash: &str) -> Result<Vec<PhantasmaNFTMintResult>> {
    let tx_result = rpc.get_transaction(tx_hash).await?;
    parse_mint_phantasma_non_fungible_result(&tx_result.result)
}
```

Each entry carries the Phantasma NFT id the chain derived and the Carbon
instance id it minted. Check that the transaction state is `HALT` before
parsing. `parse_mint_non_fungible_result(...)` is the parser of a direct
`MintNonFungible` result, which has another layout.

## Mint Without A Client

`build_mint_phantasma_non_fungible_single_tx_and_sign_hex(...)` builds the same
mint, plans it against a gas config the caller provides, and signs it. It suits
a process that signs without a client.

```rust
use phantasma_sdk::{
    build_mint_phantasma_non_fungible_single_tx_and_sign_hex,
    build_phantasma_nft_rom, bytes32_from_public_key, prepare_standard_token_schemas,
    GasConfig, PhantasmaKeys, PlanAndSignOptions, Result, VMValue,
};

fn build_phantasma_mint_hex(wif: &str, config: &GasConfig) -> Result<String> {
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
        123,    // Carbon token id
        777i64, // Phantasma series id
        &keys,
        receiver,
        public_rom,
        vec![], // RAM
        Some(config),
        &PlanAndSignOptions::default(),
    )
}
```

`rpc.send_carbon_transaction(&decode_hex(&tx_hex)?)` sends the signed bytes.

## Read Back Minted NFTs

Use the current Carbon id-aware RPC calls:

```rust
// `parse_create_token_series_result` yields the series id as `u32`; the NFT reads take `u64`.
let nfts_page = rpc
    .get_token_nfts(carbon_token_id, u64::from(carbon_series_id), 20, "", true, "")
    .await?;

let account_nfts = rpc
    .get_account_nfts(
        &keys.address().to_text(),
        "ART",
        carbon_token_id,
        u64::from(carbon_series_id),
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
| `build_mint_phantasma_non_fungible_single_tx_and_sign_hex` | You want the SDK to build the token-module Phantasma NFT mint call for one NFT. |
| `build_mint_phantasma_non_fungible_tx_and_sign_hex` | You want to mint multiple Phantasma NFT entries in one token-module call. |
