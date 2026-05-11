# Python SDK Keys And Addresses

`phantasma_py.crypto` contains the local identity primitives used by both VM
transactions and Carbon transactions.

## Core Types

| Type | Use it for |
| ---- | ---------- |
| `PhantasmaKeys` | Local Ed25519 private key, public key, WIF import/export, address derivation, and signing. |
| `Address` | Checked Phantasma address text and bytes. |
| `Ed25519Signature` | Signature bytes plus verification against one or more addresses. |
| `Hash` | 32-byte hash wrapper with hex parsing, SHA-256 construction, and difficulty calculation. |
| `AddressKind`, `SignatureKind` | Address and signature type enums. |

## Import A Wallet Key

```python
from phantasma_py.crypto import PhantasmaKeys

keys = PhantasmaKeys.from_wif("YOUR_WIF")

print(keys.address.text)
print(keys.public_key.hex())
```

`from_wif(...)` validates checksum and key length. Invalid WIF input raises
`CryptoError`.

## Generate A Local Key

```python
from phantasma_py.crypto import PhantasmaKeys

keys = PhantasmaKeys.generate()

print(keys.address.text)
print(keys.to_wif())
```

Use generated keys only when the application is meant to create a new account or
an offline test identity. Never put WIF strings in source files, docs examples,
logs, Git history, or browser-visible configuration.

## Parse And Validate Addresses

```python
from phantasma_py.crypto import Address

address = Address.from_text("P...")

print(address.kind)
print(address.public_key.hex())
print(address.prefixed_bytes().hex())
```

`Address.from_text(...)` accepts normal Phantasma address text and returns a
checked 34-byte address object. `Address.null()` returns the null address used by
some gas helper calls.

```python
from phantasma_py.crypto import Address

null_address = Address.null()

assert null_address.is_null()
```

## Sign And Verify Bytes

```python
from phantasma_py.crypto import PhantasmaKeys

keys = PhantasmaKeys.from_wif("YOUR_WIF")
message = b"payload to sign"

signature = keys.sign(message)

assert signature.verify(message, [keys.address])
print(signature.serialize_data().hex())
```

Signatures are verified against Phantasma addresses, not raw public-key strings.
This keeps the caller on the same address format used by transactions.

## Hashes

```python
from phantasma_py.crypto import Hash

digest = Hash.sha256(b"example")

print(digest.hex)
print(digest.difficulty())
```

`Hash.from_hex(...)` expects 32 bytes of hex data. `Hash.hex` returns uppercase
hex text. `difficulty()` reports the
leading zero-bit difficulty used by local proof-of-work checks.

## Carbon Address Bytes

Carbon transaction messages use 32-byte address values. Convert local
Phantasma identities through the Carbon helpers instead of slicing address text
or public-key hex manually.

```python
from phantasma_py.carbon import (
    bytes32_from_phantasma_address,
    bytes32_from_phantasma_address_text,
    bytes32_from_public_key,
)
from phantasma_py.crypto import PhantasmaKeys

keys = PhantasmaKeys.from_wif("YOUR_WIF")

gas_from = bytes32_from_public_key(keys.public_key)
same_address = bytes32_from_phantasma_address(keys.address)
from_text = bytes32_from_phantasma_address_text(keys.address.text)

assert gas_from == same_address == from_text
```

Use these helpers when filling Carbon `gas_from`, owner, receiver, seller, or
buyer fields.

## Error Handling

```python
from phantasma_py.errors import CryptoError
from phantasma_py.crypto import Address

try:
    Address.from_text("not-an-address")
except CryptoError as exc:
    print(exc)
```

The SDK raises `CryptoError` for malformed WIF, malformed addresses, invalid
hash lengths, unsupported address kinds, and signature verification inputs that
cannot be converted into checked public keys.
