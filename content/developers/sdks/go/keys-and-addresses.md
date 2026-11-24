---
title: "Go SDK Keys And Addresses"
linkTitle: "Keys And Addresses"
weight: 30
---

Keys, addresses, signatures and hashes live in the package
`github.com/phantasma-io/phantasma-sdk-go/pkg/cryptography`. Structured
transactions name an account by its 32-byte public key, which the
`pkg/carbon` helpers derive from a key pair or an address.

## Core Types

| Type | Use it for |
| ---- | ---------- |
| `PhantasmaKeys` | One Ed25519 key pair: private key, public key, address, WIF export, signing. |
| `KeyPair` | The interface `PhantasmaKeys` implements. The signing functions of the SDK take it. |
| `Address` | A 34-byte address and its text form. |
| `Signature`, `Ed25519Signature` | A signature and its check against addresses. |
| `Hash` | A 32-byte hash, for example a transaction or block hash. |

## Create And Import Keys

```go
package main

import (
    "encoding/hex"
    "fmt"
    "log"

    "github.com/phantasma-io/phantasma-sdk-go/pkg/cryptography"
)

func main() {
    // A new random key.
    keys, err := cryptography.GeneratePhantasmaKeys()
    if err != nil {
        log.Fatal(err)
    }

    // The same key, exported and imported as WIF.
    imported, err := cryptography.FromWIF(keys.WIF())
    if err != nil {
        log.Fatal(err)
    }

    // The same key from its 32 private key bytes.
    fromSeed, err := cryptography.NewPhantasmaKeys(keys.PrivateKey())
    if err != nil {
        log.Fatal(err)
    }

    fmt.Println(keys.Address().String())
    fmt.Println(imported.Address().String() == keys.Address().String())
    fmt.Println(hex.EncodeToString(fromSeed.PublicKey()))
}
```

| Function or method | Meaning |
| ------------------ | ------- |
| `GeneratePhantasmaKeys()` | Returns a key pair whose private key is 32 random bytes from `crypto/rand`. |
| `FromWIF(wif)` | Decodes a WIF string. It returns an error when the checksum fails, the payload is not 33 or 34 bytes, the first byte is not `0x80`, or a 34-byte payload does not end with `0x01`. |
| `NewPhantasmaKeys(seed)` | Takes exactly 32 bytes. Any other length returns an error. |
| `WIF()` | The private key as compressed WIF. |
| `PrivateKey()`, `PublicKey()` | Copies of the 32-byte private key and the 32-byte public key. |
| `ExpandedPrivateKey()` | The 64-byte private key form of the Go `crypto/ed25519` package. |
| `Address()` | The user address of the public key. |

The Go SDK has no seed phrase support. A WIF string or a private key gives full
control of the account: keep it out of source code, logs and repositories.

## Addresses

An address is 34 bytes: a kind byte, a reserved byte and 32 bytes of key or
hash data. Its text form is a prefix letter followed by the Base58 encoding of
the 34 bytes.

| Prefix | `AddressKind` | Meaning |
| ------ | ------------- | ------- |
| `P` | `cryptography.User` | An account with a public key. |
| `S` | `cryptography.System` | A chain-owned address, for example of a contract or a token. |
| `X` | `cryptography.Interop` | An address that stands for an account of another chain. |

```go
package main

import (
    "encoding/hex"
    "fmt"
    "log"

    "github.com/phantasma-io/phantasma-sdk-go/pkg/cryptography"
)

func main() {
    text := "P2K7n1pVfy3ZMSextrX1nj3xYdRQvjDntEGAf1x2b7h6Rk4"
    if !cryptography.IsValidAddress(text) {
        log.Fatal("not a Phantasma address")
    }

    address, err := cryptography.FromString(text)
    if err != nil {
        log.Fatal(err)
    }
    publicKey, err := address.GetPublicKey()
    if err != nil {
        log.Fatal(err)
    }

    fmt.Println(address.IsUser(), address.Kind() == cryptography.User)
    fmt.Println(hex.EncodeToString(publicKey))
    fmt.Println(cryptography.NullAddress().String())
}
```

| Function or method | Meaning |
| ------------------ | ------- |
| `FromString(text)` | Reads a text address after trimming spaces. It returns an error for an unknown prefix, invalid Base58, a length other than 34 bytes, or a prefix that does not match the kind byte. It does not accept `NULL`. |
| `MustAddressFromString(text)` | The same, but it panics on an error. Use it for constants only. |
| `IsValidAddress(text)` | `true` when `FromString` succeeds. |
| `NullAddress()` | The null address: 34 zero bytes. Its kind is `System`. |
| `String()` | The text form, or `NULL` for the null address. |
| `Text()` | The text form without that exception: the null address gives `S1111111111111111111111111111111111`. |
| `Bytes()` | A copy of the 34 bytes. |
| `GetPublicKey()` | The 32 bytes after the kind byte and the reserved byte. |
| `Kind()`, `IsUser()`, `IsNull()` | The kind of the address. |

Structured transactions name accounts by their 32-byte public key, a
`carbon.Bytes32`:

| Function | Converts |
| -------- | -------- |
| `carbon.Bytes32FromPublicKey(keys.PublicKey())` | A 32-byte public key. Any other length returns an error. |
| `carbon.Bytes32FromPhantasmaAddress(address)` | A user or system address. An interop address returns an error. |
| `carbon.Bytes32FromPhantasmaAddressText(text)` | Address text, parsed with `FromString` first. |

Each has a `Must...` variant that panics instead of returning the error.

## Sign And Verify

```go
package main

import (
    "fmt"
    "log"

    "github.com/phantasma-io/phantasma-sdk-go/pkg/cryptography"
)

func main() {
    keys, err := cryptography.GeneratePhantasmaKeys()
    if err != nil {
        log.Fatal(err)
    }
    message := []byte("Example message")

    signature, err := keys.Sign(message)
    if err != nil {
        log.Fatal(err)
    }
    fmt.Println(signature.Verify(message, []cryptography.Address{keys.Address()}))

    // Bytes is the serialized form: one length byte, then the 64 signature bytes.
    raw := signature.Bytes()[1:]
    fmt.Println(len(raw))
}
```

`keys.Sign(message)` returns an Ed25519 signature over the bytes as they are.
`Verify(message, addresses)` returns `true` when the signature belongs to one of
the addresses and skips every address that is not a user address.
`cryptography.NewEd25519Signature(raw)` makes a signature from 64 raw bytes, for
example ones a wallet returned.

A signature over arbitrary bytes is also a valid transaction signature when the
bytes are a transaction. A service that signs messages for other parties adds a
prefix that no transaction starts with; Phantasma Link v5 does that, see
[Signing A Message](../csharp/wallet-link-v5.md#signing-a-message).

## Hashes

| Function or method | Meaning |
| ------------------ | ------- |
| `ParseHash(text)` | Reads a hash as RPC shows it: 64 hex characters, with or without `0x`. |
| `HashFromBytes(data)` | Uses 32 bytes as they are and hashes any other length with SHA-256. |
| `HashFromString(text)` | The SHA-256 of the text's bytes. It does not parse a hash; `ParseHash` does. |
| `String()` | The hash as RPC shows it. |
| `Bytes()` | The 32 bytes in stored order, which is the reverse of the text form. |
| `GetDifficulty()` | The proof-of-work difficulty of the hash; see [Proof Of Work](vm-and-transactions.md#proof-of-work). |

## Encodings

`pkg/encoding/base58` has `Encode` and `Decode` for plain Base58, and
`CheckEncode` and `CheckDecode` for Base58 with a 4-byte checksum, the first
four bytes of a double SHA-256, as WIF uses it.

## Other Key Types

`pkg/cryptography/ecdsa` signs and verifies secp256k1 and secp256r1 signatures
over the SHA-256 of a message. `pkg/cryptography/proofOfAddress` checks a text
message signed by one Phantasma, one Ethereum and one NEO Legacy key, and
checks that each address belongs to its key. Neither signs a Phantasma
transaction: the chain accepts only Ed25519 signatures on transactions.

## Errors

Every function that reads input returns an error. A `Must...` variant panics
instead; keep those for constants and tests, and return the error to the caller
for user input.
