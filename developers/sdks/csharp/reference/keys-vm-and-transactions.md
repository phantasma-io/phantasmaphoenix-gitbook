# C# Keys, VM, And Transactions

This page covers local signing, address/hash handling, VM script construction,
and raw Phantasma transactions.

Source baseline:

| Item | Value |
| ---- | ----- |
| Source repo | `phantasmaphoenix-sdk-cs` |
| Source commit | `820680b38e67109b7f94e1d26058d6933f758b26` |
| Primary projects | `PhantasmaPhoenix.Cryptography`, `PhantasmaPhoenix.Protocol`, `PhantasmaPhoenix.VM` |

## Key Pairs

`PhantasmaKeys` implements `IKeyPair` for Ed25519 Phantasma accounts.

| API | Behavior |
| ---- | ---- |
| `PhantasmaKeys.Generate()` | Creates a random 32-byte private key with `Entropy.GetRandomBytes`. |
| `new PhantasmaKeys(byte[] privateKey)` | Accepts a 32-byte private key. If a 64-byte array is supplied, the constructor keeps the first 32 bytes. Any other length throws. |
| `PhantasmaKeys.FromWIF(string wif)` | Decodes Base58Check WIF, requires a 34-byte payload with leading `0x80` and trailing `0x01`, and returns a key pair. |
| `ToWIF()` | Encodes the private key with the WIF wrapper bytes used by `FromWIF`. |
| `Sign(byte[] msg, Func<byte[], byte[], byte[], byte[]>? customSignFunction = null)` | Produces an `Ed25519Signature` from the message bytes. |
| `Address` | Readonly account address derived from the public key. |
| `PrivateKeyLength` | `32`. |

The constructor stores the private key in a new 32-byte array and derives
`PublicKey` with `Ed25519.PublicKeyFromSeed`.

## Addresses

`Address` is a 34-byte value with a kind byte, a reserved byte, and 32 bytes of
public-key or hash data.

| API | Behavior |
| ---- | ---- |
| `Address.Null` | Zero-address constant. `Text` renders as `NULL`. |
| `Address.FromBytes(byte[] bytes)` | Builds an address from 32-byte public-key data or a full 34-byte address buffer. |
| `Address.FromKey(IKeyPair key)` | Builds a user address from a 32-byte public key or an interop address from a 33-byte public key. |
| `Address.FromHash(string str)` / `Address.FromHash(byte[] input)` | Builds a system address from SHA-256 hash data. |
| `GetPublicKey()` | Returns the 32-byte payload from bytes 2 through 33. |
| `Text` | Encodes user addresses with `P`, interop addresses with `X`, and system addresses with `S`. |
| `Kind`, `IsUser`, `IsInterop`, `IsSystem`, `IsNull` | Classifies the stored bytes. |

`Address.FromKey` throws when the public key length is not 32 or 33 bytes.
Address equality compares the stored byte arrays.

## Hashes

`Hash` is a 32-byte value used for transaction hashes, block hashes, and Merkle
operations.

| API | Behavior |
| ---- | ---- |
| `Hash.Parse(string s)` | Accepts 64 hex characters or a `0x`-prefixed value, reverses the parsed bytes, and returns a `Hash`. |
| `Hash.TryParse(string s, out Hash result)` | Returns `false` and `Hash.Null` for empty, wrong-length, or invalid hex input. |
| `Hash.FromBytes(byte[] input)` | Uses the input directly when it is 32 bytes; otherwise hashes the input with SHA-256. |
| `Hash.FromString(string str)` | Hashes the string with SHA-256. |
| `Hash.FromUnpaddedHex(string hash)` | Removes optional `0x`, pads with zero pairs to 64 hex characters, then parses. |
| `ToByteArray()` | Returns a copy of the internal little-endian hash bytes. |
| `ToByteArrayReversed()` / `ToString()` | Uses reversed byte order for display and text conversion. |
| `MerkleCombine(Hash A, Hash B)` | Concatenates the two internal hash buffers and hashes the result. |

The implicit conversion from `BigInteger` pads unsigned integer bytes to 32
bytes and rejects values larger than the hash length.

## Script Builder

`ScriptBuilder` writes VM opcodes into an internal `MemoryStream` and returns
`this` from emit methods so builders can be chained.

| API group | Methods | Notes |
| ---- | ---- | ---- |
| Raw opcodes | `Emit`, `EmitRaw`, `EmitThrow`, `EmitPush`, `EmitPop` | Writes opcode bytes and optional raw bytes. |
| Values | `EmitLoad` overloads for `byte[]`, `string`, `BigInteger`, `bool`, `Enum`, `Timestamp`, `ISerializable` | `byte[]` load rejects payloads larger than `0xFFFF`; `ISerializable` is serialized before loading. |
| Movement | `EmitMove`, `EmitCopy` | Moves or copies between VM registers. |
| Calls | `EmitExtCall`, `EmitCall` | `EmitExtCall` loads the method name before emitting `EXTCALL`; `EmitCall` requires register count from 1 through `VirtualMachine.MaxRegisterCount`. |
| Control flow | `EmitLabel`, `EmitJump`, `EmitConditionalJump` | Jump labels are resolved when `ToScript` is called. Invalid jump opcodes throw. |
| Output | `ToScript()` / `ToScript(out labels)` | Returns final bytecode and optionally returns resolved label offsets. Missing labels throw. |

Use `EmitExtCall("Runtime.TransferTokens")` and similar runtime names only when
the target chain supports the call. The SDK builds bytecode; the VM and chain
decide whether the call is valid.

## Transactions

`Protocol.Transaction` represents a Phantasma VM transaction.

| API | Behavior |
| ---- | ---- |
| `new Transaction(nexusName, chainName, script, expiration, payload)` | Creates an unsigned transaction and computes the hash from unsigned bytes. Payload can be `string`, `byte[]`, or omitted. |
| `ToByteArray(bool withSignature)` | Serializes nexus, chain, script, expiration, payload, and optionally signatures. |
| `Sign(IKeyPair keypair, Func<byte[], byte[], byte[], byte[]>? customSignFunction = null)` | Signs unsigned transaction bytes, appends the signature, and returns the hash of the unsigned message. |
| `AddSignature(Signature signature)` | Appends an externally produced signature. |
| `GetTransactionSignature(IKeyPair keypair, ...)` | Produces a signature without mutating `Signatures`. |
| `IsSignedBy(Address address)` / `IsSignedBy(IEnumerable<Address> addresses)` | Verifies whether any signature matches the supplied address set. |
| `IsSignedByEveryone(IEnumerable<Address> addresses)` | Requires a signature count equal to the address count and verifies all addresses. |
| `Transaction.Unserialize(byte[] bytes)` | Reads a serialized transaction and returns `null` if parsing fails. |
| `Transaction.GetTransactionFee(Hash transactionHash, Block block)` | Sums `GasPayment` events emitted by the `gas` contract for the transaction. |
| `ValidateNexus(Nexus chainNexus)` | Parses the transaction nexus name and compares it with the supplied enum value. |

Gas-specific constructor parameters are present, but gas serialization is
commented out in the current source baseline. Do not rely on those constructor
arguments to write gas fields into the serialized transaction.

## VM Objects

`VMObject` stores decoded VM values with a `VMType`.

| API | Behavior |
| ---- | ---- |
| `AsNumber()` | Converts numbers, numeric strings, byte arrays, enums, bools, timestamps, and hash objects. `None` converts to zero. Other object payloads throw. |
| `AsString()` | Converts strings, numbers, UTF-8 byte arrays, enums, bools, timestamps, addresses, hashes, and structs. Structs become a string when they are arrays of numbers; otherwise they serialize to base64. |
| `AsByteArray()` | Converts VM byte payloads and other supported primitive forms to bytes. |
| `AsBool()` | Converts bool values and accepted numeric forms. |
| `AsTimestamp()` | Requires `VMType.Timestamp`. |
| `AsEnum<T>()` | Requires `T` to be an enum and casts from VM enum or numeric data. |
| `AsArray(VMType type)` | Requires `VMType.Struct` and returns an array of child values cast to the requested type. |
| `SerializeData` / `UnserializeData` | Reads and writes VM object wire data through `BinaryReader` and `BinaryWriter`. |

Conversions throw when the stored type does not match the requested conversion.
Catch those errors around generic script-result decoding.
