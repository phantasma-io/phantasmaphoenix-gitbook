# C++ SDK Keys And Addresses

Cryptographic types live under `include/Cryptography/`. The main application
types are `PhantasmaKeys`, `Address`, `Ed25519Signature`, `Hash`, and
`PrivateKey`.

Local key generation, WIF import, and signing require a crypto adapter such as
`Adapters/PhantasmaAPI_openssl.h` included immediately after `PhantasmaAPI.h`.

## Keys

```cpp
#include "PhantasmaAPI.h"
#include "Adapters/PhantasmaAPI_openssl.h"
#include "Cryptography/KeyPair.h"

using namespace phantasma;

auto keys = PhantasmaKeys::Generate();
auto address = keys.GetAddress();
auto wif = keys.ToWIF();

auto imported = PhantasmaKeys::FromWIF(wif);
```

`PhantasmaKeys::FromWIF` validates compressed WIF payload length, prefix, and
suffix. Keep WIF values in secure application storage, not logs or public
configuration.

## Addresses

```cpp
bool parseError = false;
auto address = Address::FromText("P...", 0, &parseError);
if (parseError) {
    // reject user input
}
```

`Address::FromText` accepts `P`, `S`, and `X` prefixes and validates that the
decoded address kind matches the prefix. `Address::IsValidAddress(text)` is a
boolean validation helper.

## Signatures

```cpp
ByteArray message = {1, 2, 3};
auto signature = keys.Sign(message);
```

`Transaction::Sign(keys)` signs the unsigned VM transaction bytes and appends
the resulting signature to the transaction.

A signature is checked against the addresses allowed to have produced it:

```cpp
Ed25519Signature signature = keys.Sign(message);

const Address allowed[] = { keys.GetAddress() };
bool ok = signature.Verify(message.data(), (int)message.size(), allowed, 1);
```

## Private Key Bytes

`PrivateKey` keeps its 32 bytes in a guarded buffer. `Read()` and `Write()`
return short-lived accessors with `Bytes()` and `Size()`; use them only inside
the scope that needs the raw key.

```cpp
const PrivateKey& sk = keys.GetPrivateKey();
auto reader = sk.Read();
ByteArray copy(reader.Bytes(), reader.Bytes() + reader.Size());
```

## Hashes

`Hash` is a 32-byte value. `Hash::FromBytes(bytes)` builds one, `Hash::Parse(text)`
reads the hex form, and `ToString()` renders it.

```cpp
Hash h = Hash::FromBytes(bytes);
String text = h.ToString();
```

## Carbon Address Conversion

Carbon helpers use `Bytes32` public-key/account values. Convert a public key or
Phantasma address before building Carbon token transactions.

```cpp
phantasma::carbon::Bytes32 owner(keys.PublicKeyBytes(), keys.PublicKeyLength());
```

Use checked constructors and exception/error handling where user input can be
malformed.
