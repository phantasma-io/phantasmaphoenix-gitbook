# Rust Example: Keys And Addresses

This example uses a deterministic local key for documentation output. Do not use
deterministic keys for real accounts.

```rust
use phantasma_sdk::{
    bytes32_from_phantasma_address, bytes32_from_public_key, encode_hex, Address, Hash,
    PhantasmaKeys, Result,
};

fn main() -> Result<()> {
    let keys = PhantasmaKeys::try_from_slice(&[7u8; 32])?;
    let address = keys.address();
    let parsed = Address::from_text(address.to_text())?;

    assert_eq!(parsed, address);

    let message = b"docs example";
    let signature = keys.sign(message);

    assert!(signature.verify(message, [&address]));

    let carbon_from_key = bytes32_from_public_key(&keys.public_key())?;
    let carbon_from_address = bytes32_from_phantasma_address(&address)?;

    assert_eq!(carbon_from_key, carbon_from_address);

    let digest = Hash::sha256(message);

    println!("address: {}", address.to_text());
    println!("wif: {}", keys.to_wif());
    println!("carbon address: {}", encode_hex(carbon_from_key));
    println!("hash: {}", digest.to_hex());
    println!("difficulty: {}", digest.difficulty());

    Ok(())
}
```

For live use, load WIF values from a secret store or wallet flow instead of
embedding them in source code.
