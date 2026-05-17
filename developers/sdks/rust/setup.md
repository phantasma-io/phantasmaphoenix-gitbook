# Rust SDK Setup

The Rust SDK crate is `phantasma-sdk`. Its library import path is
`phantasma_sdk`.

## Requirements

- Rust 1.74 or newer.
- Rust 2021 edition.
- Tokio for async RPC examples and applications.

## Install

Add the SDK to `Cargo.toml`:

```toml
[dependencies]
phantasma-sdk = "1.0.2"
tokio = { version = "1", features = ["macros", "rt-multi-thread"] }
```

Then import the crate:

```rust
use phantasma_sdk::{PhantasmaRpc, Result};
```

## Local Development

```bash
git clone https://github.com/phantasma-io/phantasma-sdk-rs.git
cd phantasma-sdk-rs
just verify
```

The source `just verify` gate runs:

- `cargo fmt --all -- --check`
- `cargo check --all-targets`
- `cargo test --all-targets --no-fail-fast`
- `cargo clippy --all-targets -- -D warnings`
- `RUSTDOCFLAGS="-D warnings" cargo doc --no-deps`

Use `just release-check` before publishing; it also runs package creation and
`cargo publish --dry-run`.

## Endpoint Selection

Use explicit endpoints in applications and examples:

```rust
use phantasma_sdk::PhantasmaRpc;

let rpc = PhantasmaRpc::new("http://localhost:5172/rpc");
```

For command-line examples, pass the endpoint as an argument or through an
environment variable so deployment-specific values stay out of source code.
