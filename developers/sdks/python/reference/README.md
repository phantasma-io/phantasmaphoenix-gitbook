# Python SDK Complete API Reference

This section documents the public `phantasma_py` API at the level needed to
build and maintain applications without reading the SDK source for ordinary
usage. Start with setup and task pages for common flows; use this section when
you need method groups, parameter details, return values, and lower-level
helpers.

Source baseline:

| Item | Value |
| ---- | ----- |
| Package | `phantasma-sdk-py` |
| Import namespace | `phantasma_py` |
| Version | `2.0.3` |
| Source commit | `559fd95ed1267b214a92a958283fceacb0c9d029` |

## When To Use These Pages

| Page | Use it when |
| ---- | ----------- |
| [RPC Client](rpc-methods.md) | You need to read chain state, invoke read-only scripts, broadcast serialized transactions, or choose between similar RPC wrappers. |
| [RPC Result Models](rpc-models.md) | You need the fields returned by account, token, block, transaction, NFT, auction, or network RPC calls. |
| [VM and Transaction APIs](vm-transaction-binary.md) | You need keys, addresses, VM script building, transaction serialization/signing, binary helpers, or SDK error behavior. |
| [Carbon API and Wire Format](carbon-wire.md) | You need Carbon transaction builders, token/series/NFT structures, schema serialization, message payloads, fee options, or result parsers. |
| [Public API Inventory](public-api.md) | You need the complete list of public modules, classes, methods, fields, and constants under `phantasma_py`. |

## Import Policy

The package re-exports the main user-facing APIs from `phantasma_py`. That is
convenient for examples:

```python
from phantasma_py import PhantasmaRPC, PhantasmaKeys
```

For larger applications, import from the module that owns the API. It makes the
code easier to review because the import tells the reader whether the code is
using RPC, VM, crypto, or Carbon functionality:

```python
from phantasma_py.crypto import PhantasmaKeys
from phantasma_py.rpc import PhantasmaRPC
from phantasma_py.carbon import build_create_token_tx_and_sign_hex
```

## Error Model

All SDK-specific exceptions inherit from `PhantasmaError`. The most common
subclasses are `RPCError`, `CryptoError`, `EncodingError`, `SerializationError`,
and `BuilderError`. Reference pages call out the error family where it matters;
normal application code can catch `PhantasmaError` at module boundaries and
handle narrower subclasses in validation-heavy code paths.
