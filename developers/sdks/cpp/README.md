# C++ SDK

The C++ SDK is a C++17 header-based SDK for Phantasma applications, services,
and tooling. It covers adapter-backed JSON-RPC access, request/response JSON
builders, cryptographic primitives, VM script and transaction helpers, and
Carbon wire-format transaction builders.

{% hint style="info" %}
Repository: [https://github.com/phantasma-io/phantasma-sdk-cpp](https://github.com/phantasma-io/phantasma-sdk-cpp)
{% endhint %}

## What It Covers

| Area | Headers | Use it for |
| ---- | ------- | ---------- |
| RPC | `PhantasmaAPI.h`, `Adapters/*` | High-level RPC calls or low-level JSON request/response construction. |
| Keys and addresses | `Cryptography/*` | WIF, Ed25519 signatures, addresses, hashes, proof of work, and secure byte/string wrappers. |
| VM scripts | `VM/ScriptBuilder.h` | Contract calls, interop calls, gas, transfers, staking, and low-level opcode emission. |
| VM transactions | `Blockchain/Transaction.h` | Classic VM transaction construction, signing, serialization, and mining. |
| Carbon | `Carbon/*` | Carbon serialization, token info, schemas, token/series/NFT transaction builders, signing, and result parsing. |

## Getting Started

The SDK supports multiple backends. **Include an adapter BEFORE `PhantasmaAPI.h`**:

- `Adapters/PhantasmaAPI_rapidjson.h` + `Adapters/PhantasmaAPI_curl.h` (RapidJSON + libcurl)
- or `Adapters/PhantasmaAPI_cpprest.h` (Microsoft CppRestSDK)

```cpp
// JSON + HTTP backends first
#include "Adapters/PhantasmaAPI_rapidjson.h"
#include "Adapters/PhantasmaAPI_curl.h"

// Then the generated API
#include "PhantasmaAPI.h"

using namespace phantasma;
using namespace phantasma::rpc;

int main() {
    HttpClient http("https://your-node-url"); // provided by adapter
    PhantasmaAPI api(http);

    PhantasmaError err{};
    Account me = api.GetAccount("P2K...address", &err);
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

Compatibility notes:
- `GetBlockTransactionCountByHash(blockHash, err)` and `GetTransactionByBlockHashAndIndex(blockHash, index, err)` are legacy overloads that default to the `"main"` chain.
- Prefer the chain-aware overloads for new code: pass `chainAddressOrName` explicitly before the block hash.
- Carbon token endpoints use `carbonTokenId` / `carbonSeriesId`; pass `0` when resolving by Phantasma symbol or series id only.

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
