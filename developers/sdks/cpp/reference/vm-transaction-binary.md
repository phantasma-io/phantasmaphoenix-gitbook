# C++ SDK VM And Transaction APIs

Keys, addresses, VM scripts, script transactions and binary helpers: the
C++ SDK outside the Carbon module.

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
| `Text()`, `ToString()`, `Kind()`, `IsUser()`, `IsSystem()`, `IsInterop()`, `IsNull()`, `ToByteArray()` | The text form (`ToString()` gives `[Null address]` for the null address), the kind, and the 34 bytes. |
| `Ed25519Signature::Verify(message, length, addresses, count)`, `Bytes()` | Checks a signature against addresses; the 64 signature bytes. |
| `Hash::Parse`, `Hash::TryParse`, `Hash::FromBytes`, `Hash::FromString`, `ToString()`, `GetDifficulty()` | A 32-byte hash: parsed from hex, taken from 32 bytes or the SHA-256 of other bytes or of text, printed as RPC shows it, and its proof-of-work difficulty. |
| `PrivateKey::Read()`, `Write()` | Short-lived accessors to the guarded private key bytes. |

## VM Script Builder

`VM/ScriptBuilder.h` exposes low-level emitters and high-level call helpers.

| API group | Methods |
| --------- | ------- |
| Low-level opcodes | `Emit`, `EmitPush`, `EmitPop`, arithmetic/logical emitters, jumps, labels, register helpers |
| Load helpers | `EmitLoad` overloads for bytes, strings, big integers, booleans, timestamps, addresses, arrays, and serializable values |
| Contract/interop calls | `CallContract`, `CallInterop` |
| Common chain calls | `AllowGas`, `SpendGas`, `MintTokens`, `TransferTokens`, `TransferToken`, `TransferBalance`, `BurnToken`, `BurnTokens`, `Stake`, `WriteToken`, `WriteTokenFromRegister`, `ReadTokenRAMToRegister` |
| Finishing | `EndScript()` appends `RET` and resolves the jumps; a jump to a label the script never defines throws with `PHANTASMA_EXCEPTION_ENABLE`. |

`Unstake`, `Claim` and `GetUnclaimed` of the `stake` contract have no helper;
call them with `CallContract`. See [Script Helpers](/developers/sdks/cpp/vm-and-transactions.md#script-helpers).

## Transaction

`Blockchain/Transaction.h` exposes the script transaction type.

| API | Purpose |
| --- | ------- |
| Constructor | Sets nexus, chain, script, expiration, and payload. Transactions are unsigned until `Sign` is called. |
| `ToByteArray(withSignature)` | Serializes with or without signatures. |
| `Sign(keypair)` | Signs unsigned transaction bytes and appends a signature. |
| `IsSignedBy(address)` / `SignatureIndex(address)` | Checks appended signatures. |
| `Mine(difficulty)` | Adds a 4-byte counter after the payload and raises it until the hash reaches the difficulty. It refuses a signed transaction. |
| `GetHash()`, `NexusName()`, `ChainName()`, `Script()`, `Expiration()`, `Payload()`, `Signatures()` | The hash of the unsigned bytes and the fields. |
| `Unserialize(...)`, `SerializeData(...)` | Binary parsing and writing helpers. |

## VM Objects

`VM/VMObject.h` holds `VMObject`, a VM value. `VMObject::FromBytes(bytes)`
reads one serialized value, such as an entry of `InvokeRawScript`'s `results`
after `Base16::Decode`, and `AsNumber()`, `AsString()`, `AsBool()` and
`AsByteArray()` convert it.

## Sending Helpers

`Utils/RpcUtils.h`:

| API | Purpose |
| --- | ------- |
| `SignAndSendTransaction(api, keys, nexus, chain, script, payload, &err, expiration)` | Builds, signs and sends a script transaction; 45 seconds of lifetime without `expiration`. |
| `DefaultScriptExpiration()` | 45 seconds from now, as a `Timestamp`. |
| `CheckConfirmation(api, hash, output)`, `WaitForConfirmation(apis, count, hash, expiry, output, sleep)` | Read a transaction until the node returns it or reports it rejected. |
| `SignAndSendCarbonTransaction(api, msg, keys, &err)` | Signs a structured message with one key and sends it. It does not plan the fee. |

## Binary And Serialization Helpers

`Utils/BinaryReader.h`, `Utils/BinaryWriter.h`, and `Utils/Serializable.h`
implement the VM binary format. They are not Carbon serializers. Use
`Carbon/Carbon.h` read/write helpers for Carbon messages.
