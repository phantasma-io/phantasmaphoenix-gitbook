---
title: "C++ SDK Complete API Reference"
linkTitle: "Complete API Reference"
weight: 120
---

The public API of the C++ SDK: the RPC client and its result structs, the key,
VM and transaction types, the Carbon API and the full declaration inventory.

## Pages

| Page | Use it when |
| ---- | ----------- |
| [RPC Client](rpc-methods.md) | You need high-level RPC calls, low-level JSON builders/parsers, or method caveats. |
| [RPC Result Models](rpc-models.md) | You need result model groups and where to find their fields. |
| [VM and Transaction APIs](vm-transaction-binary.md) | You need key/address handling, VM scripts, transaction signing, or binary helpers. |
| [Carbon API and Wire Format](carbon-wire.md) | You need Carbon serialization, schemas, token/series/NFT builders, fee options, signing, or result parsers. |
| [Public API Inventory](public-api.md) | You need the complete list of public declarations exposed by headers under `include/**`. |

## Header And Adapter Rules

JSON and HTTP adapters are selected before including `PhantasmaAPI.h`; crypto
adapters such as `Adapters/PhantasmaAPI_openssl.h` are included immediately
after `PhantasmaAPI.h`. Carbon transaction signing uses the crypto adapter.

The Carbon headers expose a mix of view structs and owned helper structs. When a
builder returns a `TxEnvelope`, keep it alive until signing or serialization is
complete because it owns buffers referenced by the `TxMsg`.
