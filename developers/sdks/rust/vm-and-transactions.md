# Rust SDK VM And Transactions

`ScriptBuilder` builds VM scripts. `Transaction` serializes, signs, and checks
VM script transactions.

## Keys And Addresses

```rust
use phantasma_sdk::{Address, PhantasmaKeys, Result};

fn main() -> Result<()> {
    let keys = PhantasmaKeys::from_wif("...")?;
    let address = keys.address();

    println!("{}", address.to_text());
    assert_eq!(Address::from_text(address.to_text())?, address);

    Ok(())
}
```

Generate local keys only for development or offline examples:

```rust
let keys = PhantasmaKeys::generate();
let signature = keys.sign(b"message");
let address = keys.address();

assert!(signature.verify(b"message", [&address]));
```

## Script Builder

`ScriptBuilder::begin()` starts a chainable builder. `end_script()` validates the
script and returns `Result<Vec<u8>>`.

```rust
use phantasma_sdk::{Address, PhantasmaKeys, Result, ScriptArg, ScriptBuilder};

fn main() -> Result<()> {
    let keys = PhantasmaKeys::from_wif("...")?;
    let from = keys.address();

    let script = ScriptBuilder::begin()
        .allow_gas(from, Address::null(), 10_000, 210_000)
        .call_contract("stake", "GetStake", [ScriptArg::from(from)])
        .spend_gas(from)
        .end_script()?;

    println!("{}", script.len());
    Ok(())
}
```

Use `end_script_hex()` when an RPC method expects hex:

```rust
let script_hex = ScriptBuilder::begin()
    .call_interop("Runtime.Time", Vec::<ScriptArg>::new())
    .end_script_hex()?;
```

## Common Builder Helpers

| Helper | Purpose |
| ------ | ------- |
| `call_interop(method, args)` | Call a runtime interop such as `Runtime.Time`. |
| `call_contract(contract_name, method, args)` | Call a contract method. |
| `allow_gas(...)` / `spend_gas(...)` | Add gas allowance and settlement calls. |
| `transfer_tokens(...)` | Add a fungible token transfer call. |
| `transfer_nft(...)` | Add a non-fungible token transfer call. |
| `stake(...)` / `unstake(...)` | Add staking calls. |
| `call_nft(symbol, series_id, method, args)` | Call an NFT method by token symbol and series. |

The builder also exposes low-level emit methods for custom scripts.

Amount arguments are base units. For an 8-decimal token, `100_000_000`
represents one whole token. Fetch token decimals through RPC before converting
human input into base units.

```rust
let token = rpc.get_token("SOUL", true).await?;
let amount = 1u64 * 10u64.pow(token.decimals as u32);
```

## Low-Level Script Emission

Use low-level `emit_*` methods only when a helper does not cover the script you
need.

```rust
use phantasma_sdk::{Opcode, Result, ScriptBuilder};

fn main() -> Result<()> {
    let script = ScriptBuilder::begin()
        .emit_load_string(0, "hello")
        .emit_push(0)
        .emit(Opcode::Ret)
        .end_script()?;

    println!("{}", script.len());
    Ok(())
}
```

`end_script()` resolves labels and returns an error for unresolved jumps or
invalid input. This is safer than manually concatenating bytecode.

## Signing A VM Script Transaction

```rust
use phantasma_sdk::{encode_hex, Address, PhantasmaKeys, Result, ScriptBuilder, Transaction};

fn main() -> Result<()> {
    let keys = PhantasmaKeys::try_from_slice(&[7u8; 32])?;
    let from = keys.address();
    let to = Address::from_hash(b"example receiver");

    let script = ScriptBuilder::begin()
        .allow_gas(from, Address::null(), 100_000, 21_000)
        .transfer_tokens("SOUL", from, to, 1)
        .spend_gas(from)
        .end_script()?;

    let mut tx = Transaction::new("mainnet", "main", script, 0)
        .with_payload(b"example".to_vec());
    tx.sign(&keys);

    println!("{}", encode_hex(tx.to_bytes(true)));
    Ok(())
}
```

`Transaction::hash()` is computed from unsigned transaction bytes.
`to_bytes(true)` includes signatures; `to_bytes(false)` returns the signing
payload.

Use `tx.is_signed_by(&keys)` when you need to verify a decoded transaction
before submitting or inspecting it.

```rust
assert!(tx.is_signed_by(&keys));
```

## Proof Of Work

```rust
tx.mine(1);
```

`mine(difficulty)` mutates the transaction payload with a nonce until the hash
meets the requested difficulty.

## Broadcast Through RPC

```rust
let tx_hash = rpc.send_transaction(&tx).await?;
```

Broadcast only when the caller has intentionally selected a funded key and RPC
endpoint.

Fetch the transaction after broadcast and check its VM state before treating the
operation as successful.

```rust
let confirmed = rpc.get_transaction(&tx_hash).await?;

if !confirmed.state_is_success() {
    eprintln!("transaction failed: {}", confirmed.state);
}
```
