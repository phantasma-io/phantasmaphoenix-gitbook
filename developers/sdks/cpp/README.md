# Introduction

This C++ SDK provides tools to interact with the Phantasma blockchain.
It includes modules for cryptography, blockchain data structures, network communication, and adapters for different underlying SDKs.

The SDK is designed for developers who want to integrate Phantasma into their C++ applications, offering both low-level JSON-RPC message builders and high-level API calls.

**Key Features:**
- Complete cryptographic primitives (Ed25519, hashing, encryption)
- Transaction building and signing
- JSON-RPC request/response handling
- Current Carbon RPC helpers for token series, cursor pagination, node build metadata, and VM config
- Adapters for CURL, cpprestsdk, sodium, and more
- Portable C++17 code with adapter-selected HTTP/JSON/crypto backends

# Architecture Overview

The SDK is organized into the following main modules:

- **PhantasmaAPI**: High-level API for interacting with the blockchain
- **PhantasmaJsonAPI**: Low-level JSON message builders and parsers
- **Cryptography**: Key pairs, hashing, signatures, and encryption
- **Blockchain**: Transaction and block structures
- **Adapters**: Implementations for networking, JSON parsing, and cryptography

# Getting Started

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

[Low-level API](/developers/sdks/cpp/low-level-api.md)
[High-level API](/developers/sdks/cpp/high-level-api.md)
[Data models](/developers/sdks/cpp/data-models.md)
[Cryptography](/developers/sdks/cpp/cryptography.md)
