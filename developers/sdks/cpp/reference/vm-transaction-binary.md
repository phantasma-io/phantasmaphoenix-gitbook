# C++ SDK VM And Transaction APIs

This page covers keys, addresses, VM scripts, classic VM transactions, and
binary helpers outside the Carbon module.

## Keys And Addresses

| API | Purpose |
| --- | ------- |
| `PhantasmaKeys::Generate()` | Creates a random Ed25519 key pair. |
| `PhantasmaKeys::FromWIF(...)` | Parses compressed WIF. |
| `PhantasmaKeys::ToWIF()` | Exports compressed WIF. |
| `GetPrivateKey`, `GetPublicKey`, `GetAddress` | Canonical key accessors. Deprecated PascalCase property-style names remain for compatibility. |
| `PhantasmaKeys::Sign(message)` | Signs a byte array. |
| `Address::FromText(...)` | Parses `P`, `S`, or `X` address text and validates the decoded kind. |
| `Address::FromKey(...)` | Creates a user address from a key or public key bytes. |
| `Address::FromHash(...)`, `Address::ForTokenContract(...)` | Deterministic system address helpers. |
| `Address::IsValidAddress(text)` | Boolean address validation helper. |

## VM Script Builder

`VM/ScriptBuilder.h` exposes low-level emitters and high-level call helpers.

| API group | Methods |
| --------- | ------- |
| Low-level opcodes | `Emit`, `EmitPush`, `EmitPop`, arithmetic/logical emitters, jumps, labels, register helpers |
| Load helpers | `EmitLoad` overloads for bytes, strings, big integers, booleans, timestamps, addresses, arrays, and serializable values |
| Contract/interop calls | `CallContract`, `CallInterop` |
| Common chain calls | `AllowGas`, `SpendGas`, `MintTokens`, `TransferTokens`, `TransferBalance`, `TransferNFT`, `Stake`, `Unstake`, `CallNFT` |
| Cross-chain helpers | `CrossTransferToken`, `CrossTransferNFT` |

## Transaction

`Blockchain/Transaction.h` exposes the classic VM transaction type.

| API | Purpose |
| --- | ------- |
| Constructor | Sets nexus, chain, script, expiration, and payload. Transactions are unsigned until `Sign` is called. |
| `ToByteArray(withSignature)` | Serializes with or without signatures. |
| `Sign(keypair)` | Signs unsigned transaction bytes and appends a signature. |
| `IsSignedBy(address)` / `SignatureIndex(address)` | Checks appended signatures. |
| `Mine(difficulty)` | Mutates payload with a nonce until hash difficulty is high enough. Must run before signing. |
| `Unserialize(...)`, `SerializeData(...)` | Binary parsing and writing helpers. |

## Binary And Serialization Helpers

`Utils/BinaryReader.h`, `Utils/BinaryWriter.h`, and `Utils/Serializable.h`
implement the VM binary format. They are not Carbon serializers. Use
`Carbon/Carbon.h` read/write helpers for Carbon messages.
