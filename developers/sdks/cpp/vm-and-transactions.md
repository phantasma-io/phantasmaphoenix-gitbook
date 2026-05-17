# C++ SDK VM And Transactions

Classic VM transactions use `VM/ScriptBuilder.h` for scripts and
`Blockchain/Transaction.h` for transaction wrapping, signing, serialization,
and optional proof-of-work mining.

## Script Builder

`ScriptBuilder` can emit low-level opcodes and higher-level contract/interop
calls. Common helpers include:

| Helper | Purpose |
| ------ | ------- |
| `CallContract(contract, method, ...)` | Emits a contract call. |
| `CallInterop(method, ...)` | Emits an interop call. |
| `AllowGas`, `SpendGas` | Adds gas allowance and gas spend calls. |
| `TransferTokens`, `TransferBalance`, `TransferNFT` | Transfer helpers. |
| `CrossTransferToken`, `CrossTransferNFT` | Cross-chain transfer helpers. |
| `Stake`, `Unstake`, `CallNFT` | Stake and NFT contract helpers. |

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
