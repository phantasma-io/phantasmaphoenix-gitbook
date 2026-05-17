# Rust SDK Fees And Broadcasting

The Rust SDK can build and sign VM transactions and Carbon transactions. It does
not hide broadcasting behind examples: applications choose the endpoint, key
source, fee options, confirmation policy, and retry behavior.

## Two Transaction Families

| Family | Build with | Broadcast with | Result handling |
| ------ | ---------- | -------------- | --------------- |
| VM script transaction | `ScriptBuilder` + `Transaction` | `PhantasmaRpc::send_raw_transaction(...)` or `send_transaction(...)` | `PhantasmaRpc::get_transaction(...)`, `TransactionResult::state_is_success()` |
| Carbon transaction | `TxMsg` / Carbon lifecycle helpers | `PhantasmaRpc::send_carbon_transaction(...)` or `send_signed_tx_msg(...)` | `PhantasmaRpc::get_transaction(...)`, Carbon result parser helpers |

VM transactions use nexus/chain names and a VM script. Carbon transactions use
Carbon `TxMsg` fields such as `expiry`, `max_gas`, `max_data`, `gas_from`, and
typed Carbon payloads.

## Carbon Fee Options

High-level Carbon lifecycle builders accept fee option objects:

| Type | Used by | Default behavior |
| ---- | ------- | ---------------- |
| `FeeOptions` | generic Carbon messages and NFT mint helpers | `calculate_max_gas()` for one item or `calculate_max_gas_for_count(count)` for count-sensitive builders |
| `CreateTokenFeeOptions` | `build_create_token_tx*` | includes create-token base and symbol-length fee estimate |
| `CreateSeriesFeeOptions` | `build_create_token_series_tx*` | includes create-series base estimate |
| `MintNFTFeeOptions` / `MintNftFeeOptions` | NFT mint helpers | aliases of `FeeOptions`; Phantasma NFT batch helpers call `calculate_max_gas_for_count(tokens.len())` |

```rust
use phantasma_sdk::{CreateTokenFeeOptions, SmallString, Result};

fn main() -> Result<()> {
    let fees = CreateTokenFeeOptions::default();
    let symbol = SmallString::new("MYNFT")?;
    let max_gas = fees.calculate_max_gas_for_symbol(&symbol);

    println!("{max_gas}");
    Ok(())
}
```

These values are maximums placed into the transaction. The chain determines the
actual consumed fee.

Direct `build_mint_non_fungible_tx*` calls mint one NFT and use
`fees.calculate_max_gas()`. Phantasma NFT batch builders scale the maximum gas
by the number of public mint records, so empty or non-positive counts are not a
valid fee input.

## `max_data`

High-level Carbon builders default `max_data` to `100_000_000`. This is the
maximum data escrow cap carried by the transaction. The chain aborts the
transaction if the required data escrow is greater than the cap.

```rust
let tx_hex = build_create_token_tx_and_sign_hex_with_options(
    token_info,
    &keys,
    None,
    100_000_000,
    0,
)?;
```

Use a larger cap only after the application understands the storage growth of
the operation it is building. Unused escrow is handled by the chain, not by the
SDK.

## Expiry

High-level Carbon builders use `expiry = 0` as "now plus 60 seconds" based on
`now_unix_millis()`.

```rust
use phantasma_sdk::now_unix_millis;

let expiry = now_unix_millis() + 5 * 60 * 1000;
```

Pass an explicit expiry when the transaction may wait in a signing queue or
when your service batches transactions.

## Explicit Carbon Broadcast

```rust
use phantasma_sdk::{PhantasmaRpc, Result};

#[tokio::main]
async fn main() -> Result<()> {
    let rpc = PhantasmaRpc::new("https://testnet.phantasma.info/rpc");
    let tx_hash = rpc.send_carbon_transaction(&signed_tx_bytes).await?;

    println!("{tx_hash}");
    Ok(())
}
```

`send_carbon_transaction(...)` accepts signed Carbon bytes. Use
`send_signed_tx_msg(...)` when you already have a decoded `SignedTxMsg`.

## Confirmation And Result Parsing

Broadcasting only submits the transaction. Fetch the confirmed transaction and
then parse the result for the specific Carbon operation.

```rust
use phantasma_sdk::{parse_create_token_result, PhantasmaRpc, Result};

#[tokio::main]
async fn main() -> Result<()> {
    let rpc = PhantasmaRpc::new("https://testnet.phantasma.info/rpc");

    let tx_hash = rpc.send_carbon_transaction(&signed_create_token_bytes).await?;
    let tx = rpc.get_transaction(&tx_hash).await?;

    if !tx.state_is_success() {
        eprintln!("transaction failed: {}", tx.state);
        return Ok(());
    }

    let carbon_token_id = parse_create_token_result(&tx.result)?;
    println!("{carbon_token_id}");

    Ok(())
}
```

Use the parser that matches the operation:

| Operation | Parser |
| --------- | ------ |
| Create token | `parse_create_token_result(result_hex)` |
| Create token series | `parse_create_token_series_result(result_hex)` |
| Direct Carbon NFT mint | `parse_mint_non_fungible_result(carbon_token_id, result_hex)` |
| Phantasma NFT helper mint | `parse_mint_phantasma_non_fungible_result(result_hex)` |

Do not parse one operation's result with another operation's parser.

## VM Broadcast

```rust
let tx_hash = rpc.send_transaction(&tx).await?;
```

`send_transaction(...)` serializes a signed `Transaction`. Use
`send_raw_transaction(...)` when you already have signed VM transaction hex.

## Combined Sign And Send Helpers

`PhantasmaRpc` also exposes helpers that combine local signing and broadcast:

| Helper | Family |
| ------ | ------ |
| `sign_and_send_transaction(...)` | VM script transaction |
| `sign_carbon_transaction(...)` | sign a Carbon `TxMsg` locally |
| `sign_and_send_carbon_transaction(...)` | Carbon `TxMsg` signing plus broadcast |
| `build_sign_send_tx_msg(...)` | lower-level Carbon message build/sign/send |
| `send_create_token_tx(...)` | create-token specific Carbon helper |

These are convenience methods for applications that already own the key and
endpoint selection. They are not wallet prompts and they do not add user
confirmation.

## Read Back After Broadcast

For token workflows, always verify chain state after parsing the result:

```rust
let token = rpc.get_token_with_id("MYNFT", true, carbon_token_id).await?;
let series = rpc.get_token_series("MYNFT", carbon_token_id, 20, "").await?;
```

For NFT mints, read by token id, series cursor, account cursor, or NFT id:

```rust
let nfts = rpc
    .get_token_nfts(carbon_token_id, 0, 20, "", true, "")
    .await?;
let owned = rpc
    .get_account_nfts(address_text, "MYNFT", carbon_token_id, 0, 20, "", true, false)
    .await?;
```

This catches a common integration mistake: a transaction can be submitted to an
endpoint, but the app may be reading from a different network or a stale RPC
node.

## Safety Checklist

- Use mainnet, testnet, and devnet endpoints intentionally.
- Keep wallet WIF values outside docs, logs, and Git.
- Check `tx.state_is_success()` before parsing `tx.result`.
- Keep the token symbol and Carbon token id together in application state.
- Keep the exact `TokenSchemas` used for deployment; do not reconstruct a
different schema before creating series or minting.
- Treat examples as local builder examples unless they explicitly say they were
  run against a funded live endpoint.
