# Rust SDK Keys And Addresses

`phantasma_sdk::crypto` contains the local identity primitives used by VM
transactions and Carbon transactions. The crate re-exports the common types at
the top level.

## Core Types

| Type | Use it for |
| ---- | ---------- |
| `PhantasmaKeys` | Local Ed25519 private key, public key, WIF import/export, address derivation, and signing. |
| `Address` | Checked Phantasma address text and bytes. |
| `Ed25519Signature` | Signature bytes plus verification against one or more addresses. |
| `Hash` | 32-byte hash wrapper with SHA-256 construction, hex output, and difficulty calculation. |
| `AddressKind`, `SignatureKind` | Address and signature type enums. |

## Import A Wallet Key

```rust
use phantasma_sdk::{encode_hex, PhantasmaKeys, Result};

fn main() -> Result<()> {
    let keys = PhantasmaKeys::from_wif("YOUR_WIF")?;

    println!("{}", keys.address().to_text());
    println!("{}", encode_hex(keys.public_key()));

    Ok(())
}
```

`from_wif(...)` validates checksum and key length. Invalid WIF input returns
`PhantasmaError`.

## Generate A Local Key

```rust
use phantasma_sdk::PhantasmaKeys;

let keys = PhantasmaKeys::generate();

println!("{}", keys.address().to_text());
println!("{}", keys.to_wif());
```

Use generated keys only when the application is meant to create a new account or
an offline test identity. Never put WIF strings in source files, docs examples,
logs, Git history, or browser-visible configuration.

## Parse And Validate Addresses

```rust
use phantasma_sdk::{encode_hex, Address, Result};

fn main() -> Result<()> {
    let address = Address::from_text("P...")?;

    println!("{:?}", address.kind());
    println!("{}", encode_hex(address.public_key()?));
    println!("{}", encode_hex(address.prefixed_bytes()));

    Ok(())
}
```

`Address::from_text(...)` accepts normal Phantasma address text and returns a
checked address object. `Address::null()` returns the null address used by some
gas helper calls.

```rust
use phantasma_sdk::Address;

let null_address = Address::null();

assert!(null_address.is_null());
```

## Sign And Verify Bytes

```rust
use phantasma_sdk::{PhantasmaKeys, Result};

fn main() -> Result<()> {
    let keys = PhantasmaKeys::try_from_slice(&[7u8; 32])?;
    let message = b"payload to sign";

    let signature = keys.sign(message);
    let address = keys.address();

    assert!(signature.verify(message, [&address]));
    println!("{}", phantasma_sdk::encode_hex(signature.serialize_data()));

    Ok(())
}
```

Signatures are verified against Phantasma addresses, not raw public-key strings.
This keeps the caller on the same address format used by transactions.

## Hashes

```rust
use phantasma_sdk::Hash;

let digest = Hash::sha256(b"example");

println!("{}", digest.to_hex());
println!("{}", digest.difficulty());
```

`Hash::try_from_slice(...)` expects exactly 32 bytes. `difficulty()` reports the
leading zero-bit difficulty used by local proof-of-work checks.

## Carbon Address Bytes

Carbon transaction messages use `Bytes32` address values. Convert local
Phantasma identities through the Carbon helpers instead of slicing address text
or public-key hex manually.

```rust
use phantasma_sdk::{
    bytes32_from_phantasma_address, bytes32_from_phantasma_address_text,
    bytes32_from_public_key, PhantasmaKeys, Result,
};

fn main() -> Result<()> {
    let keys = PhantasmaKeys::try_from_slice(&[7u8; 32])?;

    let gas_from = bytes32_from_public_key(&keys.public_key())?;
    let same_address = bytes32_from_phantasma_address(&keys.address())?;
    let from_text = bytes32_from_phantasma_address_text(&keys.address().to_text())?;

    assert_eq!(gas_from, same_address);
    assert_eq!(same_address, from_text);

    Ok(())
}
```

Use these helpers when filling Carbon `gas_from`, owner, receiver, seller, or
buyer fields.

## Error Handling

```rust
use phantasma_sdk::{Address, Result};

fn main() -> Result<()> {
    match Address::from_text("not-an-address") {
        Ok(address) => println!("{}", address.to_text()),
        Err(err) => println!("{err}"),
    }

    Ok(())
}
```

The crate returns `Result<T>` for malformed WIF, malformed addresses, invalid
hash lengths, unsupported address kinds, and signature verification inputs that
cannot be converted into checked public keys.
