---
title: "Mint Carbon NFT"
weight: 80
---

This example builds a Carbon NFT mint message, plans its fee against a node,
signs it and broadcasts it.

```rust
use phantasma_sdk::{
    build_mint_phantasma_non_fungible_single_tx, build_phantasma_nft_rom,
    bytes32_from_public_key, prepare_standard_token_schemas, summarize_fee_plan, PhantasmaKeys,
    PhantasmaRpc, PlanRequestOptions, Result, SendTransactionOptions, TxLimits, TxSigner, VMValue,
};

#[tokio::main]
async fn main() -> Result<()> {
    let client = PhantasmaRpc::new("https://testnet.phantasma.info/rpc");
    let keys = PhantasmaKeys::generate();
    let sender = bytes32_from_public_key(&keys.public_key())?;
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

    let msg = build_mint_phantasma_non_fungible_single_tx(
        123,    // Carbon token id
        777i64, // Phantasma series id
        sender,
        sender, // receiver
        public_rom,
        vec![], // RAM
        TxLimits::default(),
    )?;

    let plan = client.fees().plan(&msg, &PlanRequestOptions::default()).await?;
    let summary = summarize_fee_plan(&plan);
    println!("gas {} KCAL, storage deposit up to {} SOUL", summary.gas_bill, summary.storage_ceiling);

    let signers: [&dyn TxSigner; 1] = [&keys];
    let tx_hash = client
        .send_tx_msg(&plan.apply(&msg), &signers, &SendTransactionOptions::default())
        .await?;

    println!("signer: {}", keys.address().to_text());
    println!("mint tx: {tx_hash}");
    Ok(())
}
```

Replace the Carbon token id with the id returned by the confirmed token
deployment, and the Phantasma series id with the id used when the series was
created.

The builder carries no prices. `plan.apply(&msg)` writes the ceilings into the
message, so `send_tx_msg` sends it as it is. To build without a node, state the
offer in `TxLimits` and use the `_and_sign_hex` variant. See
[Fees And Broadcasting](../fees-and-broadcasting.md).
