---
title: "Rust SDK"
weight: 60
---

The Rust SDK is a checked Rust crate for Phantasma applications, services, and
tooling. It covers JSON-RPC access, Ed25519 keys and signatures, VM script
building, VM script transaction signing, and Carbon wire-format transactions.

Crate name:

```toml
[dependencies]
phantasma-sdk = "3.0.1"
tokio = { version = "1", features = ["macros", "rt-multi-thread"] }
```

Import path:

```rust
use phantasma_sdk::{PhantasmaRpc, Result};
```

All fallible public APIs return `phantasma_sdk::Result<T>`. Parsing and builder
code rejects malformed input with `PhantasmaError` instead of panicking.

## What It Covers

| Area | Module | Use it for |
| ---- | ------ | ---------- |
| RPC | `phantasma_sdk::rpc` | Async JSON-RPC calls and typed response models. |
| Keys and addresses | `phantasma_sdk::crypto` | WIF, Ed25519 signatures, address parsing, hashes. |
| VM scripts | `phantasma_sdk::vm` | Building VM scripts for contract calls, interop calls, gas, transfers, staking, and NFT calls. |
| VM transactions | `phantasma_sdk::transaction` | Serializing, signing, mining, and checking VM script transactions. |
| Carbon | `phantasma_sdk::carbon` | Carbon serialization, schemas, token creation payloads, NFT mint payloads, signed Carbon messages. |

## Carbon Workflows

Use the Carbon workflow pages when creating native assets:

- [Token Deployment](token-deployment.md)
- [NFT Minting](nft-minting.md)
- [Schemas And Metadata](schemas-and-metadata.md)
- [Fees And Broadcasting](fees-and-broadcasting.md)
- [Carbon Operations](carbon-operations.md)

## Read-Only RPC Example

```rust
use phantasma_sdk::{PhantasmaRpc, Result};

#[tokio::main]
async fn main() -> Result<()> {
    let rpc = PhantasmaRpc::new("http://localhost:5172/rpc");
    let version = rpc.get_version().await?;
    println!("{} {}", version.version, version.commit);
    Ok(())
}
```

## Guides

- [Setup](setup.md)
- [RPC](rpc.md)
- [Keys And Addresses](keys-and-addresses.md)
- [VM and Transactions](vm-and-transactions.md)
- [Carbon](carbon.md)
- [API Overview](api-reference.md)
- [Complete API Reference](reference/_index.md)
- [Examples](examples/_index.md)
