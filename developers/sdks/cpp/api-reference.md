# C++ SDK API Overview

This page lists the public surface of the C++ SDK by header group. The
reference section documents each group.

{% content-ref url="reference/README.md" %}
C++ SDK Complete API Reference
{% endcontent-ref %}

## Main API Groups

| API group | Main headers | Purpose |
| --------- | ------------ | ------- |
| RPC | `PhantasmaAPI.h`, `Adapters/*` | High-level RPC calls, low-level JSON request/response construction, adapter-backed HTTP/JSON integration. |
| Cryptography | `Cryptography/*` | Addresses, WIF, Ed25519 keys/signatures, hashing, entropy, secure memory wrappers. |
| VM | `VM/ScriptBuilder.h`, `VM/VMObject.h`, `VM/Opcodes.h` | VM bytecode construction, VM object serialization, opcode-level tooling. |
| Transactions | `Blockchain/Transaction.h` | VM transaction construction, signing, mining, serialization. |
| Carbon | `Carbon/*` | Carbon wire primitives, token schemas, token/series/NFT structures, transaction builders, signing, result parsers. |
