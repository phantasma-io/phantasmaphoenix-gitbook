# C++ SDK VM And Transactions

Script transactions use `VM/ScriptBuilder.h` for scripts and
`Blockchain/Transaction.h` for transaction wrapping, signing, serialization,
and optional proof-of-work mining.

## Script Builder

`ScriptBuilder` can emit low-level opcodes and higher-level contract/interop
calls. Common helpers include:

| Helper | Purpose |
| ------ | ------- |
| `CallContract(contract, method, ...)` | Emits a contract call. |
| `CallInterop(method, ...)` | Emits an interop call. |
| `AllowGas`, `SpendGas` | Adds the gas allowance and gas spend calls. |
| `TransferTokens`, `TransferToken`, `TransferBalance` | Transfers a fungible amount, one NFT by id, or a whole balance. |
| `MintTokens`, `BurnToken`, `BurnTokens` | Mints a fungible amount, burns one NFT or a fungible amount. |
| `Stake` | Stakes SOUL for an address. |
| `WriteToken`, `WriteTokenFromRegister`, `ReadTokenRAMToRegister` | Writes or reads NFT RAM. |

Generic string arguments are VM strings. Use `Address` values when the target
ABI expects address bytes.

## VM Transaction

`Transaction` wraps:

| Field | Source API |
| ----- | ---------- |
| Nexus name | constructor argument, `NexusName()` |
| Chain name | constructor argument, `ChainName()` |
| Script | constructor argument, `Script()` |
| Expiration | constructor argument, `Expiration()` |
| Payload | constructor argument, `Payload()` |
| Signatures | `Signatures()` |
| Hash | `GetHash()` |

Build a transaction from a final script, sign it, then serialize it for
`SendRawTransaction`.

```cpp
#include "VM/ScriptBuilder.h"
#include "Blockchain/Transaction.h"

phantasma::Transaction tx(
    "mainnet",
    "main",
    script,
    expiration,
    "CPP-SDK"
);

tx.Sign(keys);
auto signedBytes = tx.ToByteArray(true);
```

`ToByteArray(false)` returns the unsigned bytes used for signing. `Mine(...)`
mutates the payload with a nonce and must be called before signing.
