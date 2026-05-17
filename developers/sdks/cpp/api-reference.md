# C++ SDK API Overview

This page summarizes the current C++ SDK public surface and links to deeper
reference pages.

{% content-ref url="reference/README.md" %}
C++ SDK Complete API Reference
{% endcontent-ref %}

## Source Baseline

| Item | Value |
| ---- | ----- |
| Repository | `https://github.com/phantasma-io/phantasma-sdk-cpp` |
| Current branch | `main` |
| Source commit | `b9b755c6e456214f65c1ff8168d5ad41eace302f` |
| Language | C++17 |

## Main API Groups

| API group | Main headers | Purpose |
| --------- | ------------ | ------- |
| RPC | `PhantasmaAPI.h`, `Adapters/*` | High-level RPC calls, low-level JSON request/response construction, adapter-backed HTTP/JSON integration. |
| Cryptography | `Cryptography/*` | Addresses, WIF, Ed25519 keys/signatures, hashing, entropy, secure memory wrappers. |
| VM | `VM/ScriptBuilder.h`, `VM/VMObject.h`, `VM/Opcodes.h` | VM bytecode construction, VM object serialization, opcode-level tooling. |
| Transactions | `Blockchain/Transaction.h` | VM transaction construction, signing, mining, serialization. |
| Carbon | `Carbon/*` | Carbon wire primitives, token schemas, token/series/NFT structures, transaction builders, signing, result parsers. |

Existing deep pages remain available:

{% content-ref url="low-level-api.md" %}
Low-level API
{% endcontent-ref %}

{% content-ref url="high-level-api.md" %}
High-level API
{% endcontent-ref %}

{% content-ref url="data-models.md" %}
Data models
{% endcontent-ref %}

{% content-ref url="cryptography.md" %}
Cryptography
{% endcontent-ref %}
