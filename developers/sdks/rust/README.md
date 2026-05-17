# Rust SDK

The Rust SDK is a checked Rust crate for Phantasma applications, services, and
tooling. It covers JSON-RPC access, Ed25519 keys and signatures, VM script
building, VM script transaction signing, and Carbon wire-format transactions.

Crate name:

```toml
[dependencies]
phantasma-sdk = "1.0.2"
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

{% content-ref url="token-deployment.md" %}
Token Deployment
{% endcontent-ref %}

{% content-ref url="nft-minting.md" %}
NFT Minting
{% endcontent-ref %}

{% content-ref url="schemas-and-metadata.md" %}
Schemas And Metadata
{% endcontent-ref %}

{% content-ref url="fees-and-broadcasting.md" %}
Fees And Broadcasting
{% endcontent-ref %}

{% content-ref url="carbon-operations.md" %}
Carbon Operations
{% endcontent-ref %}

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

{% content-ref url="setup.md" %}
Setup
{% endcontent-ref %}

{% content-ref url="rpc.md" %}
RPC
{% endcontent-ref %}

{% content-ref url="keys-and-addresses.md" %}
Keys And Addresses
{% endcontent-ref %}

{% content-ref url="vm-and-transactions.md" %}
VM and Transactions
{% endcontent-ref %}

{% content-ref url="carbon.md" %}
Carbon
{% endcontent-ref %}

{% content-ref url="api-reference.md" %}
API Overview
{% endcontent-ref %}

{% content-ref url="reference/README.md" %}
Complete API Reference
{% endcontent-ref %}

{% content-ref url="examples/README.md" %}
Examples
{% endcontent-ref %}
