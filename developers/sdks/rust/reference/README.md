# Rust SDK Complete API Reference

This section documents the public `phantasma_sdk` API at the level needed to
build and maintain applications without reading the SDK source for ordinary
usage. The workflow guides remain the best entry point for common tasks. These
reference pages explain what each API group is for, how related methods differ,
what the important parameters mean, what is returned, and which low-level
helpers are available when a guide does not cover a case.

Source baseline:

| Item | Value |
| ---- | ----- |
| Crate | `phantasma-sdk` |
| Import path | `phantasma_sdk` |
| Version | `1.0.1` |
| Version constant | `SDK_VERSION` |
| Source commit | `1af47ec2d1fdcfb0ae7838a3f0c972021117a1bb` |

## When To Use These Pages

| Page | Use it when |
| ---- | ----------- |
| [RPC Client](rpc-methods.md) | You need to read chain state, invoke read-only scripts, broadcast serialized transactions, or choose between similar RPC wrappers. |
| [RPC Result Models](rpc-models.md) | You need the fields returned by account, token, block, transaction, NFT, auction, or network RPC calls. |
| [VM and Transaction APIs](vm-transaction-binary.md) | You need keys, addresses, VM script building, transaction serialization/signing, binary helpers, or SDK error behavior. |
| [Carbon API and Wire Format](carbon-wire.md) | You need Carbon transaction builders, token/series/NFT structures, schema serialization, message payloads, fee options, or result parsers. |

## Re-exports

The crate re-exports the main user-facing APIs at the crate root. That is
convenient for examples and small tools:

```rust
use phantasma_sdk::{
    Address, PhantasmaKeys, PhantasmaRpc, Result, ScriptBuilder, Transaction,
};
```

For larger applications, importing from the owning module keeps code easier to
review because the import tells the reader whether the code is using RPC, VM,
crypto, or Carbon functionality:

```rust
use phantasma_sdk::carbon::build_create_token_tx_and_sign_hex;
use phantasma_sdk::rpc::PhantasmaRpc;
```

## Error Model

All fallible public APIs return `phantasma_sdk::Result<T>`, which is an alias
for `std::result::Result<T, PhantasmaError>`. The error enum separates encoding,
serialization, crypto, builder, HTTP, JSON, and JSON-RPC failures. Reference
pages call out the relevant error family where it matters; normal application
code can return `Result<T>` from its own SDK-facing functions and handle narrower
variants at validation or transport boundaries.
