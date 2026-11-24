---
title: "C++ SDK"
weight: 70
---

The C++ SDK is a C++17 header-based SDK for Phantasma applications, services,
and tooling. It covers adapter-backed JSON-RPC access, request/response JSON
builders, cryptographic primitives, VM script and transaction helpers, and
Carbon wire-format transaction builders.

> [!NOTE]
> Repository: [https://github.com/phantasma-io/phantasma-sdk-cpp](https://github.com/phantasma-io/phantasma-sdk-cpp)

## What It Covers

| Area | Headers | Use it for |
| ---- | ------- | ---------- |
| RPC | `PhantasmaAPI.h`, `Adapters/*` | High-level RPC calls or low-level JSON request/response construction. |
| Keys and addresses | `Cryptography/*` | WIF, Ed25519 signatures, addresses, hashes, proof of work, and secure byte/string wrappers. |
| VM scripts | `VM/ScriptBuilder.h` | Contract calls, interop calls, gas, transfers, staking, and low-level opcode emission. |
| VM transactions | `Blockchain/Transaction.h` | Script transaction construction, signing, serialization, and mining. |
| Carbon | `Carbon/*` | Carbon serialization, token info, schemas, token/series/NFT transaction builders, signing, and result parsing. |

## Getting Started

The SDK supports multiple backends. **Include an adapter BEFORE `PhantasmaAPI.h`**:

- `Adapters/PhantasmaAPI_rapidjson.h` + `Adapters/PhantasmaAPI_curl.h` (RapidJSON + libcurl)
- or `Adapters/PhantasmaAPI_cpprest.h` (Microsoft CppRestSDK)

```cpp
// The function bodies of the API, in exactly one source file.
#define PHANTASMA_IMPLEMENTATION

// JSON + HTTP backends first
#include "Adapters/PhantasmaAPI_rapidjson.h"
#include "Adapters/PhantasmaAPI_curl.h"

// Then the generated API
#include "PhantasmaAPI.h"

using namespace phantasma;
using namespace phantasma::rpc;

int main() {
    HttpClient http("https://testnet.phantasma.info"); // the node's base URL; the API adds /rpc
    PhantasmaAPI api(http);

    PhantasmaError err{};
    AccountInfo me = api.GetAccountInfo("P2K...address", &err);
    if (err.code != 0) {
        // handle err.message
    }
}
```

> If you use the CppRestSDK adapter, include **only** `Adapters/PhantasmaAPI_cpprest.h` before `PhantasmaAPI.h`.

Build system notes:
- Requires a C++17 compiler
- Link with `curl` when using the CURL adapter
- Add RapidJSON headers when using the RapidJSON adapter
- Add CppRestSDK when using the cpprest adapter

Notes:
- `GetBlockTransactionCountByHash` and `GetTransactionByBlockHashAndIndex` take `chainAddressOrName` before the block hash; there is no overload that defaults the chain.
- Carbon token endpoints use `carbonTokenId` / `carbonSeriesId`; pass `0` when resolving by Phantasma symbol or series id only.

## Guides

- [Setup](setup.md)
- [RPC](rpc.md)
- [Keys And Addresses](keys-and-addresses.md)
- [VM and Transactions](vm-and-transactions.md)
- [Carbon](carbon.md)
- [API Overview](api-reference.md)
- [Complete API Reference](reference/_index.md)
- [Examples](examples/_index.md)
