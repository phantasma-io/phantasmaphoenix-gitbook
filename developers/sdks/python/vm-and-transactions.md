# Python SDK VM And Transactions

`phantasma_py.vm` builds VM scripts. `phantasma_py.transaction` serializes and
signs VM script transactions.

## Keys And Addresses

```python
from phantasma_py.crypto import Address, PhantasmaKeys

keys = PhantasmaKeys.from_wif("...")
address = keys.address

print(address.text)
print(Address.from_text(address.text) == address)
```

`PhantasmaKeys.generate()` creates a new local key pair. Store generated WIF
values securely and never commit them.

```python
keys = PhantasmaKeys.generate()
signature = keys.sign(b"message")

assert signature.verify(b"message", [keys.address])
```

## Script Builder

Use `ScriptBuilder.begin()` and chain helper calls. `end_script()` validates the
script and raises `BuilderError` if the builder has unresolved labels or invalid
user input.

```python
from phantasma_py.crypto import Address, PhantasmaKeys
from phantasma_py.vm import ScriptBuilder

keys = PhantasmaKeys.from_wif("...")

script = (
    ScriptBuilder.begin()
    .allow_gas(keys.address, Address.null(), gas_price=10_000, gas_limit=210_000)
    .call_contract("stake", "GetStake", keys.address)
    .spend_gas(keys.address)
    .end_script()
)
```

Use `end_script_hex()` when an RPC method expects hex:

```python
script_hex = ScriptBuilder.begin().call_interop("Runtime.Time").end_script_hex()
```

Use `end_script_with_error()` when script input comes from an untrusted UI or
configuration file and you prefer explicit error handling:

```python
script, error = builder.end_script_with_error()
if error is not None:
    raise error
```

## Common Builder Helpers

`ScriptBuilder` includes low-level opcodes and higher-level helpers:

| Helper | Purpose |
| ------ | ------- |
| `call_interop(method, *args)` | Call a runtime interop such as `Runtime.Time`. |
| `call_contract(contract_name, method, *args)` | Call a contract method. |
| `allow_gas(...)` / `spend_gas(...)` | Add gas allowance and settlement calls. |
| `transfer_tokens(...)` | Add a fungible token transfer call. |
| `transfer_nft(...)` | Add a non-fungible token transfer call. |
| `stake(...)` / `unstake(...)` | Add staking calls. |
| `call_nft(symbol, series_id, method, *args)` | Call an NFT method by token symbol and series. |

Most address helpers also have `_text` variants when caller input is address
text instead of an `Address` object.

Amount arguments are base units. For an 8-decimal token, `100_000_000`
represents one whole token. Fetch token decimals through RPC before converting
human input into base units.

```python
token = rpc.get_token("SOUL")
amount = 1 * 10**token.decimals
```

## Low-Level Script Emission

Use low-level `emit_*` methods only when a helper does not cover the script you
need.

```python
from phantasma_py.vm import Opcode, ScriptBuilder, VMType

script = (
    ScriptBuilder.begin()
    .emit_load_string(0, "hello")
    .emit_push(0)
    .emit(Opcode.RET)
    .end_script()
)
```

`end_script()` resolves labels and raises `BuilderError` for unresolved jumps or
invalid input. This is safer than manually concatenating bytecode.

## Signing A VM Script Transaction

```python
import time

from phantasma_py.crypto import PhantasmaKeys
from phantasma_py.transaction import Transaction
from phantasma_py.vm import ScriptBuilder

keys = PhantasmaKeys.generate()
script = ScriptBuilder.begin().call_interop("Runtime.Time").end_script()

tx = Transaction(
    nexus_name="mainnet",
    chain_name="main",
    script=script,
    expiration=int(time.time()) + 300,
)

signature = tx.sign(keys)

print(tx.hash)
print(signature.verify(tx.to_bytes(with_signatures=False), [keys.address]))
print(tx.to_bytes().hex())
```

The transaction hash is computed from unsigned transaction bytes. Signed wire
bytes include the signature list.

Use `tx.is_signed_by(keys)` when you need to verify a decoded transaction
before submitting or inspecting it.

```python
assert tx.is_signed_by(keys)
```

## Proof Of Work

`Transaction.mine(difficulty)` mutates the transaction payload with a nonce
until the transaction hash reaches the requested difficulty.

```python
tx.mine(difficulty=1)
```

Use this only when the target network or endpoint requires proof of work for
the transaction you are building.

## Broadcast Through RPC

Broadcast signed bytes through RPC only after selecting the endpoint and funding
the signing account.

```python
from phantasma_py.rpc import PhantasmaRPC

rpc = PhantasmaRPC("http://localhost:5172/rpc")
tx_hash = rpc.send_raw_transaction(tx)
```

Fetch the transaction after broadcast and check its VM state before treating the
operation as successful.

```python
confirmed = rpc.get_transaction(tx_hash)

if not confirmed.state_is_success:
    raise RuntimeError(confirmed.state)
```
