# Rust SDK RPC

`PhantasmaRpc` is an async JSON-RPC client with typed response models and helper
methods for common Phantasma RPC flows.

## Client

```rust
use phantasma_sdk::{PhantasmaRpc, Result};

#[tokio::main]
async fn main() -> Result<()> {
    let rpc = PhantasmaRpc::new("http://localhost:5172/rpc");
    let version = rpc.get_version().await?;

    println!("version={} commit={}", version.version, version.commit);
    Ok(())
}
```

`PhantasmaRpc::new(endpoint)` uses the default reqwest transport. Tests and
advanced applications can use `PhantasmaRpc::with_transport(...)` with a custom
transport.

## Accounts And Balances

```rust
use phantasma_sdk::{PhantasmaRpc, Result};

#[tokio::main]
async fn main() -> Result<()> {
    let rpc = PhantasmaRpc::new("http://localhost:5172/rpc");
    let account = rpc.get_account("P...").await?;

    if let Some(balance) = account.token_balance("SOUL") {
        println!("{}", balance.decimal_amount());
    }

    Ok(())
}
```

Use `get_token_balance(address, symbol, chain, extended)` when you want one
balance directly from RPC instead of reading the full account object.

## Blocks And Transactions

```rust
use phantasma_sdk::{PhantasmaRpc, Result};

#[tokio::main]
async fn main() -> Result<()> {
    let rpc = PhantasmaRpc::new("http://localhost:5172/rpc");

    let height = rpc.get_block_height("main").await?;
    let block = rpc.get_block_by_height("main", height).await?;

    println!("{}", block.hash);
    Ok(())
}
```

The SDK includes chain-aware wrappers for current block and transaction RPC
signatures:

```rust
let count = rpc
    .get_block_transaction_count_by_hash_on_chain("main", &block.hash)
    .await?;

let tx = rpc
    .get_transaction_by_block_hash_and_index_on_chain("main", &block.hash, 0)
    .await?;
```

## Tokens And NFTs

Representative token and NFT calls:

```rust
let token = rpc.get_token("SOUL", true).await?;
println!("{} {}", token.symbol, token.decimals);

let series = rpc.get_token_series("ART", 1, 20, "").await?;
let one_series = rpc.get_token_series_by_ids("ART", 1, "", 1).await?;
let nfts = rpc.get_token_nfts(1, 0, 20, "", true, "").await?;
```

The RPC client also exposes account token cursor helpers such as
`get_account_fungible_tokens`, `get_account_nfts`,
`get_account_owned_tokens`, and `get_account_owned_token_series`.

Use `get_token_series_by_id(symbol, series_id)` when you have the Phantasma
series id string. Use `get_token_series_by_ids(symbol, carbon_token_id,
series_id, carbon_series_id)` when your read-back flow is keyed by Carbon ids.

Cursor result wrappers expose the decoded items and the next cursor returned by
the node. Keep passing the returned cursor until the endpoint returns an empty
cursor or your application has enough results.

```rust
let mut cursor = String::new();

loop {
    let page = rpc
        .get_token_nfts(1, 0, 20, &cursor, true, "")
        .await?;

    for nft in page.result.as_deref().unwrap_or(&[]) {
        println!("{} {}", nft.id, nft.series);
    }

    if page.cursor.is_empty() {
        break;
    }

    cursor = page.cursor;
}
```

Use account cursor helpers when the question starts from a wallet address:

```rust
let owned = rpc
    .get_account_nfts("P...", "ART", 1, 0, 20, "", true, false)
    .await?;
```

Use token cursor helpers when the question starts from a collection or series.

## Invoke Script

```rust
use phantasma_sdk::{PhantasmaRpc, Result, ScriptArg, ScriptBuilder};

#[tokio::main]
async fn main() -> Result<()> {
    let rpc = PhantasmaRpc::new("http://localhost:5172/rpc");
    let script = ScriptBuilder::begin()
        .call_interop("Runtime.Time", Vec::<ScriptArg>::new())
        .end_script_hex()?;

    let result = rpc.invoke_raw_script("main", &script).await?;
    let value = result.decode_result()?;

    println!("{value:?}");
    Ok(())
}
```

## Broadcasting

Broadcasting helpers are explicit and should be used only after selecting the
endpoint, keys, and funds intentionally:

```rust
let tx_hash = rpc.send_raw_transaction(&raw_vm_tx_hex).await?;
let carbon_hash = rpc.send_carbon_transaction(&raw_carbon_tx_bytes).await?;
```

`sign_and_send_transaction(...)`, `send_transaction(...)`,
`sign_and_send_carbon_transaction(...)`, and `send_signed_tx_msg(...)` combine
local signing or serialization with RPC broadcast helpers.

For the full broadcast, confirmation, and result parser flow, see
[Fees And Broadcasting](fees-and-broadcasting.md).

## Custom RPC Calls

If the node exposes a method that does not have a typed wrapper yet, use
`call_value(...)` or `call::<T>(...)` directly. The SDK still sends JSON-RPC
positional parameters and validates the response envelope.

```rust
use serde_json::json;

let height: u64 = rpc.call("getBlockHeight", vec![json!("main")]).await?;
```

Prefer typed wrappers when they exist; typed wrappers decode structs and use the
parameter order expected by current RPC methods.

## RPC Method Families

| Group | Representative methods |
| ----- | ---------------------- |
| Build info | `get_version`, `get_phantasma_vm_config` |
| Account | `get_account`, `get_accounts`, `lookup_name`, `get_address_transactions` |
| Blocks | `get_block_height`, `get_block_by_height`, `get_block_by_hash`, `get_latest_block` |
| Transactions | `get_transaction`, `get_transaction_by_block_hash_and_index_on_chain`, `send_raw_transaction` |
| Chain and contracts | `get_chains`, `get_chain`, `get_nexus`, `get_contract`, `get_contracts` |
| Organizations | `get_organization`, `get_organization_by_name`, `get_organizations` |
| Tokens and NFTs | `get_token`, `get_tokens`, `get_token_balance`, `get_token_series`, `get_token_nfts`, `get_nft`, `get_nfts` |
| Account token cursors | `get_account_fungible_tokens`, `get_account_nfts`, `get_account_owned_tokens`, `get_account_owned_token_series` |
| Auctions and archives | `get_auctions`, `get_auction`, `get_archive`, `read_archive`, `write_archive` |
| Scripts and Carbon | `invoke_raw_script`, `send_carbon_transaction`, `sign_carbon_transaction` |
