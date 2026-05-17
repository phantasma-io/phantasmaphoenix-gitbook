# Python Example: Keys And Addresses

This example uses a deterministic local key for repeatable output. Do not use
deterministic keys for real accounts.

```python
from phantasma_py.carbon import (
    bytes32_from_phantasma_address,
    bytes32_from_public_key,
)
from phantasma_py.crypto import Address, Hash, PhantasmaKeys

keys = PhantasmaKeys(bytes([7]) * 32)
address = keys.address
parsed = Address.from_text(address.text)

assert parsed == address

message = b"docs example"
signature = keys.sign(message)

assert signature.verify(message, [address])

carbon_from_key = bytes32_from_public_key(keys.public_key)
carbon_from_address = bytes32_from_phantasma_address(address)

assert carbon_from_key == carbon_from_address

digest = Hash.sha256(message)

print("address:", address.text)
print("wif:", keys.to_wif())
print("carbon address:", carbon_from_key.hex())
print("hash:", digest.hex)
print("difficulty:", digest.difficulty())
```

For live use, load WIF values from a secret store or wallet flow instead of
embedding them in source code.
