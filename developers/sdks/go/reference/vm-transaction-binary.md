# Go SDK VM And Transaction APIs

The Go SDK APIs outside `pkg/carbon`: keys, addresses, signatures, hashes, VM
script building, VM object decoding, and script transactions.

## Cryptography

| API | Purpose |
| --- | ------- |
| `GeneratePhantasmaKeys()` | Creates a random Ed25519 key pair. |
| `NewPhantasmaKeys(seed)` | Creates a key pair from a 32-byte seed. |
| `FromWIF(wif)` | Parses compressed WIF and validates payload, version, and suffix. |
| `PhantasmaKeys.PrivateKey()` | Returns a copy of the private seed. |
| `PhantasmaKeys.ExpandedPrivateKey()` | Returns a copy of the expanded Ed25519 private key. |
| `PhantasmaKeys.PublicKey()` | Returns a copy of the public key. |
| `PhantasmaKeys.Address()` | Returns the key pair address. |
| `PhantasmaKeys.WIF()` | Returns compressed WIF text. |
| `PhantasmaKeys.Sign(msg)` | Returns an Ed25519 signature. |
| `FromString(text)` | Parses `P`, `S`, or `X` address text. |
| `MustAddressFromString(text)` | Parses address text and panics on failure. Use only for constants/tests. |
| `NullAddress()` | Returns the all-zero address. |
| `IsValidAddress(text)` | Checks whether address text parses. |
| `HashFromBytes`, `ParseHash`, `HashFromString` | Construct checked hash values. |

Public slices returned by key methods are copies so callers cannot mutate key
material owned by the SDK.

## Script Builder

`scriptbuilder.ScriptBuilder` emits VM bytecode. The package name is
`scriptbuilder` even though the import path is `pkg/vm/script_builder`.

| API | Purpose |
| --- | ------- |
| `BeginScript()` / `NewScriptBuilder()` | Create an empty builder. |
| `EndScript()` | Finalize the script with `RET`; panics if the builder has an error. |
| `EndScriptWithError()` | Finalize and return the error instead of panicking. |
| `ToScript()` | Returns the current script body after label patching. |
| `CallContract(contractName, method, args...)` | Emits a contract call. |
| `CallInterop(method, args...)` | Emits an interop call. |
| `AllowGas`, `SpendGas`, `MintTokens`, `TransferTokens`, `TransferBalance`, `TransferNFT` | Typed address helpers for common calls. |
| `CrossTransferToken`, `CrossTransferNFT` | Emit `Runtime.SendTokens` and `Runtime.SendToken`. The chain has no such interops, and a script that calls one faults. |
| `Stake`, `Unstake`, `CallNFT` | Stake and NFT contract helpers. |
| `*Text` helpers | Parse Phantasma address text, or `NULL`, before emitting address bytes. |
| `EmitS`, `EmitM`, `EmitLoad...`, `EmitPush`, `EmitPop`, `EmitMove`, `EmitCopy`, `EmitExtCall`, `EmitLabel`, `EmitJump`, `EmitConditionalJump`, `EmitCall`, `EmitThrow`, `EmitRaw`, `EmitVarBytes`, `CurrentSize` | Single instructions and raw bytes; see [Low-Level Script Emission](/developers/sdks/go/vm-and-transactions.md#low-level-script-emission). |

`CallContract` and `CallInterop` load a `string` argument as a VM string and a
`cryptography.Address` as address bytes. The chain reads an address argument
from either form; the `Address` value is checked before the transaction is
signed. The Go types each argument may have are listed on
[Arguments](/developers/sdks/go/vm-and-transactions.md#arguments).

## VM Objects

`pkg/vm` exposes `VMObject`, `VMType`, and opcode values used by script results
and lower-level tooling. `response.ScriptResult` helpers decode result hex into
`VMObject` values.

| API | Purpose |
| --- | ------- |
| `VMObject.AsNumber()` | Converts number-compatible VM values to `*big.Int`. A value of another type panics. |
| `VMObject.AsBytes()` | Converts VM string, byte, bool, number, object, enum, timestamp, or struct values to bytes using SDK rules. |
| `VMObject.AsBool()` | Converts VM bool, one-byte bytes, or number values to `bool`. |
| `VMObject.AsString()` | Converts string-compatible values to text; numeric-array structs are decoded as UTF-16 code units. |
| `VMObject.GetArrayType()` | Detects dense zero-based struct arrays with one element type. |
| `VMObject.CastTo(vmType)` | Applies SDK VM cast rules and returns a new `VMObject`. |
| `VMObject.SetValue(value, vmType)` | Sets a VM object value from bytes and a VM type. |
| `VMObject.Copy(other)` | Copies another VM object into the receiver. |
| `VMObject.Serialize(writer)` / `Deserialize(reader)` | Writes or reads the VM object binary format. |
| `ScriptResult.DecodeResultWithError()` | Decodes `Result`, the last value the script left, into a VM object. |
| `ScriptResult.DecodeResultsWithError(index)` | Decodes one value of `Results`, which holds every value the script left. |

## Binary Helpers

`pkg/io` provides VM binary reader and writer helpers for transaction and VM
object serialization. These are separate from `pkg/carbon.Writer` and
`pkg/carbon.Reader`, which implement the Carbon wire format.

| API | Purpose |
| --- | ------- |
| `NewBufBinWriter()` | Creates an in-memory writer. `Bytes()` drains the buffer and makes later writes fail until `Reset()`. |
| `NewBinWriterFromIO(writer)` | Writes VM binary fields to an existing `io.Writer`. |
| `WriteU64LE`, `WriteU32LE`, `WriteU16LE`, `WriteU16BE`, `WriteB`, `WriteBool` | Writes fixed-width VM primitive values. |
| `WriteArray`, `WriteVarUint`, `WriteVarBytes`, `WriteString`, `WriteBigInteger`, `WriteTimestamp` | Writes VM length-prefixed arrays, strings, big integers, and timestamps. |
| `NewBinReaderFromBuf(data)` / `NewBinReaderFromIO(reader)` | Reads VM binary fields from bytes or an `io.Reader`. |
| `ReadU64LE`, `ReadU32LE`, `ReadU16LE`, `ReadU16BE`, `ReadB`, `ReadBool` | Reads fixed-width VM primitive values. |
| `ReadArray`, `ReadVarUint`, `ReadVarBytes`, `ReadString`, `ReadBigInteger`, `ReadTimestamp` | Reads VM length-prefixed arrays, strings, big integers, and timestamps. |
| `Serialize(object)` / generic `Deserialize` | Convenience helpers for values implementing the SDK binary serialization interfaces. |
| `GetVarSize(value)` | Computes the VM variable-size encoding size for supported values. |

`BinReader` and `BinWriter` store the first failure in `Err` and continue
returning zero values or ignoring writes. Check `Err` before using decoded data
from untrusted input.

## Script Transaction

```go
tx := blockchain.NewTransaction(
    "testnet",
    "main",
    script,
    expirationUnix,
    payloadBytes,
)

if err := tx.Sign(keys); err != nil {
    return err
}

hexTx := hex.EncodeToString(tx.Bytes())
```

| API | Purpose |
| --- | ------- |
| `NewTransaction(nexus, chain, script, expiration, payload)` | Builds a transaction that expires at `expiration`, in Unix seconds, and computes `Hash`. |
| `Sign(keyPair)` | Signs the unsigned bytes and appends the signature. |
| `Bytes()`, `BytesEx(withSignatures)` | The serialized transaction, with or without the signatures. |
| `Hash` | The hash of the unsigned bytes, set when the transaction is built, decoded or mined. |
| `HasSignatures()`, `IsSignedBy(addresses)` | Whether it carries signatures, and whether one belongs to one of the addresses. |
| `Mine(difficulty)` | Replaces the payload with a 4-byte counter and raises it until the hash reaches the difficulty. Run it before signing. |
| `Serialize(writer)`, `Deserialize(reader)` | The binary form. Decoding reads only Ed25519 signatures and at most `MaxTransactionSignatureCount` (1024) of them. |

`blockchain.TxStateIsSuccess(state)` is `true` for `HALT`, and
`blockchain.TxStateIsFault(state)` for `FAULT` and `BREAK`. The RPC
`TransactionResult` has the same checks as `StateIsSuccess()` and
`StateIsFault()`.
