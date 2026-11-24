---
title: "C++ SDK Setup"
linkTitle: "Setup"
weight: 10
---

The C++ SDK is a C++17 header-based source tree. Include one JSON/HTTP adapter
configuration before `PhantasmaAPI.h`, then include the API header. If you use
keys, signatures, WIF, or local transaction signing, include one crypto adapter
immediately after `PhantasmaAPI.h`.

## Requirements

| Item | Requirement |
| ---- | ----------- |
| Language | C++17 |
| Repository | `https://github.com/phantasma-io/phantasma-sdk-cpp` |
| HTTP adapter options | libcurl or CppRestSDK adapter headers |
| JSON adapter options | RapidJSON adapter or CppRestSDK adapter |

## Include Order

RapidJSON plus libcurl:

```cpp
#include "Adapters/PhantasmaAPI_rapidjson.h"
#include "Adapters/PhantasmaAPI_curl.h"
#include "PhantasmaAPI.h"
```

CppRestSDK:

```cpp
#include "Adapters/PhantasmaAPI_cpprest.h"
#include "PhantasmaAPI.h"
```

Use only one adapter stack per translation unit. Adapter headers define the
types and functions expected by `PhantasmaAPI.h`.

Crypto support for local key and signing operations:

```cpp
#include "PhantasmaAPI.h"
#include "Adapters/PhantasmaAPI_openssl.h"
```

The OpenSSL adapter is a crypto adapter, not a JSON/HTTP adapter. Include it
after `PhantasmaAPI.h`; JSON and HTTP adapters must still be included before
`PhantasmaAPI.h`.

## Header Groups

| Path | Contents |
| ---- | -------- |
| `include/PhantasmaAPI.h` | Generated high-level and low-level RPC API. |
| `include/Adapters/` | HTTP, JSON, and crypto adapter integrations. |
| `include/Cryptography/` | Address, key, signature, hash, WIF, entropy, encryption, and proof-of-work helpers. |
| `include/Blockchain/` | Script transaction type. |
| `include/VM/` | Script builder, opcodes, VM object, and NFT helpers. |
| `include/Carbon/` | Carbon wire serialization, token/series/NFT structures, transaction builders, signing, and result parsers. |

## Implementation Mode

`PhantasmaAPI.h` supports single-header style implementation control. In one
translation unit, define `PHANTASMA_IMPLEMENTATION` before including the header
when function bodies are needed there. A program that calls the RPC methods
and defines it nowhere fails to link. If you include implementation bodies in
more than one translation unit, also define `PHANTASMA_FUNCTION inline`.

Keep `PHANTASMA_*` macro overrides consistent across translation units that
include the SDK.

## Node URL

`HttpClient` takes the base URL of the node, such as
`https://testnet.phantasma.info` or `http://localhost:5172`. `PhantasmaAPI`
sends every call to that URL followed by `/rpc`, so a URL that already ends in
`/rpc` reaches `/rpc/rpc` and gets no JSON-RPC answer.

## Exceptions

Define `PHANTASMA_EXCEPTION_ENABLE` before `PhantasmaAPI.h` to have the SDK
throw `std::runtime_error` on bad input. Without it, a function with an error
parameter fills that parameter, and any other function returns a default
value; see [Keys And Addresses](keys-and-addresses.md#errors).
