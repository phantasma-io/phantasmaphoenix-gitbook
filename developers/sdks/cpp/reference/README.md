# C++ SDK Complete API Reference

This section documents the public C++ SDK API at the level needed for ordinary
application and tooling work. The existing low-level and high-level API pages
remain linked as detailed method lists.

Source baseline:

| Item | Value |
| ---- | ----- |
| Repository | `phantasma-sdk-cpp` |
| Current branch | `main` |
| Source commit | `b9b755c6e456214f65c1ff8168d5ad41eace302f` |
| Language | C++17 |

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

## Related Existing Pages

{% content-ref url="../low-level-api.md" %}
Low-level API
{% endcontent-ref %}

{% content-ref url="../high-level-api.md" %}
High-level API
{% endcontent-ref %}

{% content-ref url="../data-models.md" %}
Data models
{% endcontent-ref %}

{% content-ref url="../cryptography.md" %}
Cryptography
{% endcontent-ref %}
