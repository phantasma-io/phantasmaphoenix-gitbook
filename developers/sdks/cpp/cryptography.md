# Cryptography — Phantasma C++ SDK

This document explains the SDK’s cryptography layer in practical terms, grounded on the headers in `include/Cryptography/*` and the serialization helpers in `include/Utils/*`. It is written for engineers who need to generate keys, derive addresses, sign/verify payloads, and serialize/deserialize cryptographic types.

## What’s inside
- **PrivateKey** — secure 32‑byte secret key (guarded reads/writes)
- **PhantasmaKeys** — convenience holder: private key, public key, and derived address; also provides signing
- **Address** — canonical on‑chain address with parsing/formatting and validation
- **Signature** — variant container for signatures (Ed25519 provided by default)
- **Hash** — 32‑byte hash value with I/O helpers
- **(Utils)** `BinaryReader`, `BinaryWriter`, `Serializable`, `Entropy` — used across the types

## Include & namespaces
```cpp
#include "Cryptography/PrivateKey.h"
#include "Cryptography/KeyPair.h"
#include "Cryptography/Address.h"
#include "Cryptography/Signature.h"
#include "Cryptography/Hash.h"
#include "Utils/BinaryReader.h"
#include "Utils/BinaryWriter.h"

using namespace phantasma;
```

## PrivateKey
`PrivateKey` stores a 32‑byte secret key. The bytes are kept in a secure buffer and can only be accessed via short‑lived reader/writer proxies. Typical flows:
- Generate a random key (recommended: use `PhantasmaKeys::Generate()`)
- Import/export into the secure buffer via `Write()`/`Read()`
**Key members & methods (selection)**
- `PHANTASMA_EXCEPTION("privateKey should have length 32")` → ``

**Example — create and access**
```cpp
PrivateKey sk;                   // default-constructed = empty
if (sk.IsNull()) { /* no key material yet */ }

// Fill with strong randomness (low-level)
auto w = sk.Write();             // SecureByteWriter
Byte tmp[PrivateKey::Length];
Entropy::GetRandomBytes(tmp, PrivateKey::Length);
w.Write(tmp, PrivateKey::Length);

// Read back (e.g., for export)
auto r = sk.Read();              // SecureByteReader
Byte out[PrivateKey::Length];
r.Read(out, PrivateKey::Length);
```

## PhantasmaKeys
`PhantasmaKeys` bundles a private key, the corresponding public key bytes, and the derived `Address`. It also provides message signing helpers.
**Public API (selection)**

**Example — generate, inspect, sign**
```cpp
PhantasmaKeys keys = PhantasmaKeys::Generate();
const PrivateKey& sk = keys.GetPrivateKey();
const ByteArray&  pk = keys.GetPublicKey();
const Address&    addr = keys.GetAddress();

// Produce an Ed25519 signature over arbitrary bytes
ByteArray msg = /* ... */;
Ed25519Signature sig = keys.Sign(msg.data(), (int)msg.size());
```

## Address
`Address` represents an on‑chain account address. It supports deriving from a public key, parsing from text, validating, and converting to string.
**Public API (selection)**

**Example — parse and derive**
```cpp
Address a = Address::FromText("P2K...");  // parse from base58 form
bool ok = a.IsValid();
String text = a.ToString();

// From PhantasmaKeys / public key
Address b = Address::FromKey(keys);
```

## Signature (Ed25519)
`Signature` is a serializable container that can hold an Ed25519 signature. Verification checks the signature against one or more allowed addresses (derived from public keys).
**Public API (selection)**

**Example — verify**
```cpp
const Address allowed[] = { keys.GetAddress() };
bool ok = sig.Verify(message.data(), (int)message.size(), allowed, 1);
```

## Hash
`Hash` encapsulates a 32‑byte hash with helpers to construct from bytes and to print/compare/serialize.
**Public API (selection)**

**Example**
```cpp
Hash h = Hash::FromBytes(bytes, len);
String s = h.ToString(); // typically base16 (hex)
```

## Recipes

### Sign & verify an arbitrary message
```cpp
PhantasmaKeys keys = PhantasmaKeys::Generate();

ByteArray msg = /* your bytes */;
Ed25519Signature sig = keys.Sign(msg.data(), (int)msg.size());

const Address allowed[] = { keys.GetAddress() };
bool ok = sig.Verify(msg.data(), (int)msg.size(), allowed, 1);
```

### Sign a transaction (end-to-end)
```cpp
// Build a transaction first (see Transaction docs)
Transaction tx("main", "chain", scriptBytes, Timestamp::Now()+Timespan::FromMinutes(5));

// Append your Ed25519 signature. The SDK signs the bytes of ToByteArray(false):
tx.Sign(keys);

// Broadcast (see High-Level API / Workflows)
```

### Serialize / deserialize a signature
```cpp
BinaryWriter w;
sig.SerializeData(w);
ByteArray raw = w.ToArray();

BinaryReader r(raw);
Signature sig2;
sig2.UnserializeData(r);
```
