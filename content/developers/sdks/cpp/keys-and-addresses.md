---
title: "C++ SDK Keys And Addresses"
linkTitle: "Keys And Addresses"
weight: 30
---

Keys, addresses, signatures and hashes live under `include/Cryptography/`, in
the namespace `phantasma`. Local key generation, WIF import and signing need a
crypto adapter, such as `Adapters/PhantasmaAPI_openssl.h`, included right after
`PhantasmaAPI.h`; see [Setup](setup.md).

## Errors

The SDK reports a bad input in one of two ways. Functions with an `outError`,
`out_error` or `bool*` parameter fill it. Others call `PHANTASMA_EXCEPTION`,
which throws `std::runtime_error` only when `PHANTASMA_EXCEPTION_ENABLE` is
defined before `PhantasmaAPI.h`; otherwise it does nothing, and the function
returns a default value. Define `PHANTASMA_EXCEPTION_ENABLE`, or check the
results as the sections below describe.

## Keys

```cpp
#include "PhantasmaAPI.h"
#include "Adapters/PhantasmaAPI_openssl.h"
#include "Cryptography/KeyPair.h"

using namespace phantasma;

int main()
{
    PhantasmaKeys keys = PhantasmaKeys::Generate();
    SecureString wif = keys.ToWIF();

    PhantasmaKeys imported = PhantasmaKeys::FromWIF(wif);
    if( imported.IsNull() )
        return 1; // not a valid WIF

    return imported.GetAddress() == keys.GetAddress() ? 0 : 1;
}
```

| Member | Meaning |
| ------ | ------- |
| `PhantasmaKeys::Generate()` | A key pair with 32 random bytes as the private key. |
| `PhantasmaKeys::FromWIF(wif)` | Decodes a compressed WIF: 34 bytes after Base58Check, starting with `0x80` and ending with `0x01`. On a bad WIF it throws, or, without exceptions, returns keys whose `IsNull()` is `true`. |
| `PhantasmaKeys(privateKey, length)` | Takes 32 bytes. |
| `ToWIF()` | The private key as WIF, in a `SecureString`. |
| `GetPublicKey()`, `PublicKeyBytes()`, `PublicKeyLength()` | The 32-byte public key. |
| `GetPrivateKey()` | The private key in a guarded buffer; see [Private Key Bytes](#private-key-bytes). |
| `GetAddress()` | The user address of the public key. |
| `Sign(message)` | An Ed25519 signature over the bytes. |

A WIF string or a private key gives full control of the account. Keep it out of
source code, logs and public configuration.

## Addresses

An address is 34 bytes: a kind byte, a reserved byte and 32 bytes of key or
hash data. Its text form is a prefix letter and the Base58 encoding of the 34
bytes.

| Prefix | `AddressKind` | Meaning |
| ------ | ------------- | ------- |
| `P` | `User` | An account with a public key. |
| `S` | `System` | A chain-owned address, for example of a contract or a token. |
| `X` | `Interop` | An address that stands for an account of another chain. |

```cpp
bool parseError = false;
Address parsed = Address::FromText("P2K7n1pVfy3ZMSextrX1nj3xYdRQvjDntEGAf1x2b7h6Rk4", 0, &parseError);
if( parseError )
    return; // reject the input

bool isUser = parsed.IsUser();
String text = parsed.Text();
```

| Member | Meaning |
| ------ | ------- |
| `Address::FromText(text, length, &error)` | Reads a text address. It accepts the `P`, `S` and `X` prefixes and checks that the kind byte matches the prefix. |
| `Address::IsValidAddress(text)` | `true` when `FromText` succeeds. |
| `Address::FromKey(keys)` | The user address of a key pair. |
| `Address::FromHash(text)` | The system address of a name: the SHA-256 of its UTF-8 bytes. |
| `Address::ForTokenContract(symbol)` | `FromHash` of a token symbol: the system address the VM uses for that token. |
| `Text()` | The text form. |
| `ToString()` | The text form, or `[Null address]` for the null address. |
| `Kind()`, `IsUser()`, `IsSystem()`, `IsInterop()`, `IsNull()` | The kind of the address. The null address has the kind `System`. |
| `ToByteArray()` | A pointer to the 34 bytes. |

## Carbon Account Values

Structured transactions name accounts by their 32-byte public key, a
`carbon::Bytes32`:

```cpp
#include "Carbon/PhantasmaAddress.h"

carbon::Bytes32 fromKeys(keys.GetPublicKey());
carbon::Bytes32 fromAddress = carbon::FromPhantasmaAddress(address);
```

`FromPhantasmaAddress` takes a user or a system address and refuses an interop
address.

## Signing And Verifying

```cpp
ByteArray message = { 1, 2, 3 };
Ed25519Signature signature = keys.Sign(message);

const Address allowed[] = { keys.GetAddress() };
bool valid = signature.Verify(message.data(), (int)message.size(), allowed, 1);
```

`Verify` returns `true` when the signature belongs to one of the addresses.
`Bytes()` points at the 64 signature bytes. `Transaction::Sign(keys)` signs a
script transaction; see [VM And Transactions](vm-and-transactions.md).

A signature over arbitrary bytes is also a valid transaction signature when the
bytes are a transaction. A service that signs messages for other parties adds a
prefix that no transaction starts with; Phantasma Link v5 does that, see
[Signing A Message](../csharp/wallet-link-v5.md#signing-a-message).

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

| Member | Meaning |
| ------ | ------- |
| `Hash::Parse(text)` | Reads a hash as RPC shows it: 64 hex characters. `Hash::TryParse(text, out)` does the same without throwing. |
| `Hash::FromBytes(bytes)` | Uses 32 bytes as they are and hashes any other length with SHA-256. |
| `Hash::FromString(text)` | The SHA-256 of the text's UTF-8 bytes. It does not parse a hash. |
| `ToString()` | The hash as RPC shows it. |
| `GetDifficulty()` | The proof-of-work difficulty of the hash; see [Proof Of Work](vm-and-transactions.md#proof-of-work). |

## Related Pages

- [VM And Transactions](vm-and-transactions.md)
- [VM and Transaction APIs](reference/vm-transaction-binary.md)
- [Private Key Guideline](../../private-key-guideline.md)
