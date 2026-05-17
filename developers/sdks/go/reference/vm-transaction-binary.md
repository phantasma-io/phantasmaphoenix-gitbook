# Go SDK VM And Transaction APIs

This page covers the lower-level Go SDK APIs outside `pkg/carbon`: keys,
addresses, signatures, hashes, VM script building, VM object decoding, and
classic VM transactions.

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
| `CrossTransferToken`, `CrossTransferNFT` | Cross-chain transfer helpers. |
| `Stake`, `Unstake`, `CallNFT` | Stake and NFT contract helpers. |
| `*Text` helpers | Parse Phantasma address text before emitting address bytes. |

Generic `CallContract` and `CallInterop` encode raw strings as VM strings.
Pass `cryptography.Address` values or use `*Text` helpers when the ABI expects
address bytes.

## VM Objects

`pkg/vm` exposes `VMObject`, `VMType`, and opcode values used by script results
and lower-level tooling. `response.ScriptResult` helpers decode result hex into
`VMObject` values.

| API | Purpose |
| --- | ------- |
| `VMObject.AsNumber()` | Converts number-compatible VM values to `*big.Int`; unsupported shapes may panic because this package mirrors the older Go SDK conversion style. |
| `VMObject.AsBytes()` | Converts VM string, byte, bool, number, object, enum, timestamp, or struct values to bytes using SDK rules. |
| `VMObject.AsBool()` | Converts VM bool, one-byte bytes, or number values to `bool`. |
| `VMObject.AsString()` | Converts string-compatible values to text; numeric-array structs are decoded as UTF-16 code units. |
| `VMObject.GetArrayType()` | Detects dense zero-based struct arrays with one element type. |
| `VMObject.CastTo(vmType)` | Applies SDK VM cast rules and returns a new `VMObject`. |
| `VMObject.SetValue(value, vmType)` | Sets a VM object value from bytes and a VM type. |
| `VMObject.Copy(other)` | Copies another VM object into the receiver. |
| `VMObject.Serialize(writer)` / `Deserialize(reader)` | Writes or reads the VM object binary format. |
| `ScriptResult.DecodeResultWithError()` | Decodes the single result hex string into a VM object. |
| `ScriptResult.DecodeResultsWithError(index)` | Decodes one indexed result from `Results`. |

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

## Classic VM Transaction

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

`blockchain.TxStateIsSuccess(state)` and `blockchain.TxStateIsFault(state)`
mirror the transaction state helpers exposed on RPC `TransactionResult`.
