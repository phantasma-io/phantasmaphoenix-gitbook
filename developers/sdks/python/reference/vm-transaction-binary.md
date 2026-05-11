# Python SDK VM and Transaction APIs

This page documents the lower-level `phantasma_py` APIs outside the Carbon module.
Use these APIs for classic VM scripts, VM script transactions, VM object decoding,
key and address handling, and binary values used by VM serialization. Use the
Carbon reference when the operation is a Carbon token, series, NFT, transfer,
market, or message-payload flow.

Failure model:

| Area | Failure type |
| ---- | ------------ |
| Crypto and address parsing | `CryptoError` for invalid address text, WIF payloads, key lengths, hash lengths, and signature lengths. |
| Encoding helpers | `EncodingError` for malformed Base58 or hex text. |
| VM and binary serialization | `SerializationError` for malformed streams, unsupported VM object casts, invalid integer encodings, and trailing bytes. |
| Script building | `BuilderError` is stored by the builder and raised by `end_script()`; `end_script_with_error()` returns the error instead of raising. |

## Crypto Types

| API | Purpose and parameters | Returns and failures | Use it when |
| --- | ---------------------- | -------------------- | ----------- |
| `Address.null()` | Creates the all-zero address. | Returns `Address`. | A VM call needs the null address, for example gas allowance target. |
| `Address.from_public_key(public_key)` | Builds a user address from a 32-byte public key, a 33-byte prefixed public key, or a 64-byte key where the first 32 bytes are used. | Returns `Address`; raises `CryptoError` for unsupported public-key lengths. | A caller has raw Ed25519 public key bytes and needs a Phantasma address. |
| `Address.from_text(text)` | Parses `P`, `S`, `X`, empty, `None`, or `NULL` address text. Prefix must match the decoded address kind. | Returns `Address`; raises `CryptoError` for short text, unknown prefixes, bad Base58, invalid length, or mismatched kind. | User input or config provides address text. |
| `Address.from_hash(value)` | Hashes bytes or UTF-8 text with SHA-256 and wraps the digest as a user address payload. | Returns `Address`. | Code needs the SDK's deterministic hash-backed address helper. |
| `Address.is_null` | Property that checks whether all address bytes are zero. | Returns `bool`. | Code needs to distinguish the null address from normal user/system/interop addresses. |
| `Address.kind` | Property that classifies the address as `USER`, `SYSTEM`, `INTEROP`, or `INVALID`. | Returns `AddressKind`. | Validation or display code needs address type. |
| `Address.public_key` | Property that extracts the 32-byte public key from a user address. | Returns `bytes`; raises `CryptoError` for non-user addresses. | Signature verification needs the embedded Ed25519 public key. |
| `Address.text` | Property that formats the address with `P`, `S`, `X`, or `NULL`. | Returns `str`. | Code needs the canonical text address for UI or RPC parameters. |
| `Address.prefixed_bytes()` | Serializes address bytes with a VM var-bytes length prefix. | Returns `bytes`. | `ScriptBuilder` needs the VM argument representation for addresses. |
| `Hash.sha256(data)` | Calculates SHA-256 over `data`. | Returns `Hash`. | Transaction or payload tooling needs a checked hash wrapper. |
| `Hash.from_hex(text)` | Parses a 32-byte hash from hex text. | Returns `Hash`; raises `CryptoError` if the decoded length is not 32 bytes. | RPC or config provides hash text and code needs a `Hash` object. |
| `Hash.hex` | Property that formats the hash as uppercase hex. | Returns `str`. | UI, logs, or RPC parameters need hash text. |
| `Hash.difficulty()` | Calculates Phantasma proof-of-work difficulty from hash bytes interpreted with the SDK's VM transaction rule. | Returns `int`. | Transaction mining needs to compare a transaction hash against a difficulty target. |
| `Ed25519Signature.kind` | Property that reports `SignatureKind.ED25519`. | Returns `SignatureKind`. | Transaction serialization needs the signature kind byte. |
| `Ed25519Signature.verify(message, addresses)` | Verifies the signature against the public key embedded in any user address from `addresses`. Non-user addresses are skipped. | Returns `True` on the first valid signer and `False` otherwise. | Login challenges, off-chain messages, or transaction checks need signer validation. |
| `Ed25519Signature.serialize_data()` | Writes the raw 64-byte signature as VM var-bytes. | Returns `bytes`. | Low-level transaction or wire tooling needs signature payload bytes. |
| `PhantasmaKeys.generate()` | Creates a random Ed25519 private key with `os.urandom`. | Returns `PhantasmaKeys`. | Tests, local tools, or onboarding examples need a new key pair. |
| `PhantasmaKeys.from_wif(wif)` | Parses compressed Ed25519 WIF. It validates Base58 payload length, checksum, prefix, and compression marker. | Returns `PhantasmaKeys`; raises `CryptoError` for invalid WIF. | A trusted backend, CLI, or local script imports a private key. |
| `PhantasmaKeys.public_key` | Property that derives the raw 32-byte public key. | Returns `bytes`. | Address derivation, signature verification, or Carbon address conversion needs public key bytes. |
| `PhantasmaKeys.address` | Property that derives `Address.from_public_key(public_key)`. | Returns `Address`. | Code needs the account address for the key pair. |
| `PhantasmaKeys.to_wif()` | Serializes the private key as compressed Ed25519 WIF with checksum. | Returns `str`. | Trusted tooling needs to export a private key. Do not expose this in browser flows. |
| `PhantasmaKeys.sign(message)` | Signs `message` with the private key. | Returns `Ed25519Signature`. | Trusted code signs VM transactions, Carbon messages, or off-chain challenges. |

## Encoding Helpers

| API | Purpose and parameters | Returns and failures | Use it when |
| --- | ---------------------- | -------------------- | ----------- |
| `encode_base58(data)` | Encodes bytes with the SDK's Base58 alphabet. | Returns `str`. | Address, WIF, or other Phantasma text formats need Base58 output. |
| `decode_base58(text)` | Decodes Base58 text. | Returns `bytes`; raises `EncodingError` for invalid characters. | Parsing address or WIF text before higher-level validation. |
| `encode_hex(data)` | Encodes bytes as lowercase hex. | Returns `str`. | RPC input accepts hex and uppercase is not required. |
| `decode_hex(value)` | Decodes hex text. | Returns `bytes`; raises `EncodingError` for malformed hex. | RPC or config provides byte payloads as hex. |

## VM Binary Reader And Writer

`BinaryWriter` and `BinaryReader` implement the VM binary format used by VM
objects, scripts, and VM script transactions. They are not Carbon serializers.
Use `CarbonReader` and `CarbonWriter` for Carbon message payloads.

| API | Purpose and parameters | Returns and failures | Use it when |
| --- | ---------------------- | -------------------- | ----------- |
| `BinaryWriter.write_u8(value)` | Writes one unsigned byte. | Returns `None`; raises `SerializationError` when `value` is outside `0..255`. | A VM field is exactly one byte. |
| `write_u16_le(value)`, `write_u32_le(value)`, `write_u64_le(value)` | Writes unsigned integers in little-endian form. | Return `None`; raise `SerializationError` for negative values or values wider than the target bit width. | VM transaction fields require fixed-width unsigned integers. |
| `write_i64_le(value)` | Writes a signed 64-bit integer in little-endian form. | Returns `None`; raises `SerializationError` outside the signed 64-bit range. | A VM binary field is signed 64-bit. |
| `write_bool(value)` | Writes `1` for true and `0` for false. | Returns `None`. | A VM field is boolean encoded as one byte. |
| `write(data)` | Appends raw bytes. | Returns `None`. | The length is handled by surrounding code or the field is fixed-size. |
| `write_var_uint(value)` | Writes Phantasma VM variable-length unsigned integer encoding. | Returns `None`; raises `SerializationError` for negative values. | A VM field uses varuint length or count encoding. |
| `write_var_bytes(data)` | Writes a varuint byte length followed by raw bytes. | Returns `None`. | A VM field is length-prefixed bytes. |
| `write_string(value)` | Writes UTF-8 bytes as VM var-bytes. | Returns `None`. | A VM field is a string. |
| `write_big_integer(value)` | Writes a VM big integer as var-bytes using the SDK bigint representation. | Returns `None`; can raise `SerializationError` through bigint conversion. | VM object or transaction code needs VM integer bytes. |
| `bytes()` | Returns an immutable copy of the writer buffer. | Returns `bytes`. | Finalizing binary output. |
| `BinaryReader.remaining` | Property with the number of unread bytes. | Returns `int`. | A parser needs to decide whether more data is available. |
| `assert_eof()` | Verifies that no unread bytes remain. | Returns `None`; raises `SerializationError` on trailing bytes. | A parser must reject payloads with extra data. |
| `read(count)` | Reads exactly `count` bytes. | Returns `bytes`; raises `SerializationError` if `count` is negative or beyond the remaining stream. | A parser has a fixed-width byte field. |
| `read_u8()`, `read_u16_le()`, `read_u32_le()`, `read_u64_le()`, `read_i64_le()` | Reads fixed-width numeric fields. | Return `int`; raise `SerializationError` when the stream ends early. | Decoding VM transaction and VM object fields. |
| `read_bool()` | Reads one byte and treats non-zero as true. | Returns `bool`; raises `SerializationError` when the stream ends early. | Decoding VM boolean fields. |
| `read_var_uint()` | Reads VM variable-length unsigned integer encoding. | Returns `int`; raises `SerializationError` for malformed or truncated values. | Decoding VM lengths and counts. |
| `read_var_bytes(*, max_size=MAX_ARRAY_SIZE)` | Reads a varuint length and that many bytes. | Returns `bytes`; raises `SerializationError` when length exceeds `max_size` or the stream ends early. | Decoding VM byte arrays while enforcing a size limit. |
| `read_string()` | Reads VM var-bytes and decodes UTF-8. | Returns `str`; UTF-8 errors propagate as decode failures. | Decoding VM string fields. |
| `read_big_integer()` | Reads VM bigint var-bytes and converts to Python `int`. | Returns `int`. | Decoding VM numeric object values. |
| `big_int_to_vm_bytes(value)` | Converts a Python integer to VM bigint bytes. | Returns `bytes`. | Low-level code needs the VM integer payload without writing a full field. |
| `vm_bytes_to_big_int(data)` | Converts VM bigint bytes to Python `int`. | Returns `int`. | Low-level code decodes VM numeric payload bytes. |

## VM Object Decoding

`VMObject` is used by `ScriptResult.decode_result()` and
`ScriptResult.decode_results(index)` from the RPC models.

| API | Purpose and parameters | Returns and failures | Use it when |
| --- | ---------------------- | -------------------- | ----------- |
| `VMObject.from_bytes(data)` | Reads one VM object from bytes and requires end-of-stream after the object. | Returns `VMObject`; raises `SerializationError` for unsupported types, malformed payloads, or trailing bytes. | RPC script result hex contains one VM object. |
| `VMObject.read(reader)` | Reads one VM object from an existing `BinaryReader`. | Returns `VMObject`; raises `SerializationError` for unsupported or malformed data. | A larger parser embeds VM objects in another VM payload. |
| `as_number()` | Converts NUMBER, BYTES, 32-byte OBJECT, BOOL, STRING, ENUM, TIMESTAMP, or NONE according to SDK rules. | Returns `int`; raises `SerializationError` for unsupported conversions. | Script output should be consumed as a number. |
| `as_string()` | Converts VM string-compatible values to Python text. STRUCT numeric arrays are interpreted as UTF-16 code units; other STRUCT values are base64 of their byte representation. | Returns `str`; raises `SerializationError` for invalid conversions or invalid UTF-16 code units. | Script output should be displayed or compared as text. |
| `as_bytes()` | Converts VM values to bytes. STRING becomes UTF-8, BOOL becomes one byte, NUMBER becomes VM bigint bytes, STRUCT becomes serialized VM bytes. | Returns `bytes`; raises `SerializationError` for NONE or unsupported conversions. | Script output feeds another binary API. |
| `as_bool()` | Converts BOOL directly, one-byte BYTES by non-zero value, and NUMBER by non-zero value. | Returns `bool`; raises `SerializationError` for unsupported types. | Script output is expected to be boolean. |
| `cast_to(target)` | Converts the object to a target `VMType` using the same conversion helpers. STRING to STRUCT creates a UTF-16 numeric-array struct. | Returns `VMObject`; raises `SerializationError` for invalid casts. | Tooling needs the VM cast behavior before serializing or comparing objects. |
| `array_type()` | Detects whether a STRUCT is a zero-based numeric-key array whose values all share one `VMType`. | Returns the detected `VMType` or `VMType.NONE`. | A parser needs to distinguish array-like structs from maps. |
| `to_bytes()` | Serializes the object with `BinaryWriter`. | Returns `bytes`; raises `SerializationError` for unsupported contained values. | Code needs VM object bytes for storage or tests. |
| `write(writer)` | Writes the object into an existing `BinaryWriter`. | Returns `None`; raises `SerializationError` for unsupported types or invalid enum values. | A larger VM payload contains a VM object. |

## ScriptBuilder

`ScriptBuilder` is an incremental VM bytecode builder. It stores the first
builder error internally, so chained calls can be written naturally. Call
`end_script()` when invalid input should raise, or `end_script_with_error()` when
tooling needs to show the partial script and the validation error together.

Lifecycle methods:

| API | Purpose and parameters | Returns and failures | Use it when |
| --- | ---------------------- | -------------------- | ----------- |
| `ScriptBuilder.begin()` | Creates an empty builder. | Returns `ScriptBuilder`. | Starting a chain of builder calls. |
| `current_size` | Property with the current byte length of emitted script data. | Returns `int`. | Low-level code needs offsets for labels or diagnostics. |
| `end_script()` | Emits `RET`, resolves labels, and raises any stored builder error. | Returns final script `bytes`; raises `BuilderError` or another stored/patching error. | Production code needs valid script bytes or an exception. |
| `end_script_hex()` | Calls `end_script()` and returns uppercase hex. | Returns `str`; same failures as `end_script()`. | The next API expects script hex, such as `invoke_raw_script(...)`. |
| `end_script_with_error()` | Emits `RET` and returns either `(script, None)` or `(b"", error)`. | Returns `tuple[bytes, Exception | None]`. | UI or CLI tooling wants to display validation failures without exceptions. |
| `to_script()` | Resolves jump labels against the current buffer without appending `RET`. | Returns `bytes`; raises `BuilderError` for missing labels or invalid patch offsets. | Advanced tooling needs the current script body. |

Low-level emission methods:

| API | Purpose and parameters | Returns and failures | Use it when |
| --- | ---------------------- | -------------------- | ----------- |
| `emit(opcode)` | Writes one opcode byte. | Returns `ScriptBuilder`. | Compiler-like code emits VM opcodes directly. |
| `emit_raw(data)` | Appends raw script bytes. | Returns `ScriptBuilder`. | Code already has validated bytecode fragments. |
| `emit_push(reg)`, `emit_pop(reg)`, `emit_throw(reg)` | Emits stack/register operations for one register. | Return `ScriptBuilder`; invalid byte values can surface from binary writing. | Low-level VM scripts manage registers manually. |
| `emit_ext_call(method, reg=0)` | Loads an interop method name and emits `EXTCALL`. | Returns `ScriptBuilder`. | Low-level code wants direct interop emission instead of `call_interop(...)`. |
| `emit_load(reg, data, vm_type)` | Emits `LOAD` for raw payload bytes and a VM type. Payloads longer than `0xFFFF` store a builder error. | Returns `ScriptBuilder`. | Code needs a custom register load. |
| `emit_load_string(reg, value)`, `emit_load_bool(reg, value)`, `emit_load_number(reg, value)`, `emit_load_time(reg, value)` | Typed register-load helpers for strings, booleans, integers, and datetimes. Naive datetimes are treated as UTC; timestamps must fit VM `uint32`. | Return `ScriptBuilder`; invalid timestamp or oversized payload stores a builder error. | Low-level code needs typed VM register values. |
| `emit_move(src_reg, dst_reg)`, `emit_copy(src_reg, dst_reg)` | Emits register move/copy operations. | Return `ScriptBuilder`. | Advanced scripts manipulate registers directly. |
| `emit_label(label)` | Emits `NOP` and records the current offset for a lowercase label key. | Returns `ScriptBuilder`. | Jump or call targets are resolved later by label. |
| `emit_jump(opcode, label, reg=0)` | Emits `JMP`, `JMPIF`, or `JMPNOT` and records a patch location. Conditional jumps include `reg`. | Returns `ScriptBuilder`; invalid jump opcode stores a builder error. | Low-level scripts need branch control flow. |
| `emit_call(label, register_count)` | Emits a local VM call to a label with a register count. | Returns `ScriptBuilder`; register count must be `1..32`. | Advanced scripts call local routines. |
| `emit_conditional_jump(opcode, src_reg, label)` | Wrapper for `JMPIF`/`JMPNOT` conditional jumps. | Returns `ScriptBuilder`; invalid conditional opcode stores a builder error. | Branching depends on a source register. |
| `emit_var_bytes(value)` | Writes a VM varuint directly to the script stream. | Returns `ScriptBuilder`. | Compiler-like code needs a raw varuint field. |

High-level call methods:

| API | Purpose and parameters | Returns and failures | Use it when |
| --- | ---------------------- | -------------------- | ----------- |
| `call_interop(method, *args)` | Pushes arguments in reverse order, loads `method`, and emits `EXTCALL`. Supported args include `Address`, `str`, `bool`, bytes, integers, datetimes, and arrays. | Returns `ScriptBuilder`; unsupported args store a `BuilderError`. | Building a read/write script for a VM interop call. |
| `call_contract(contract_name, method, *args)` | Pushes arguments, loads method and contract name, emits `CTX`, then `SWITCH`. | Returns `ScriptBuilder`; unsupported args store a `BuilderError`. | Calling a contract method by name. |
| `allow_gas(from_address, to_address, gas_price, gas_limit)` | Appends `gas.AllowGas`. Addresses must already be `Address` objects. | Returns `ScriptBuilder`. | VM transaction script needs gas allowance before work. |
| `allow_gas_text(from_address, to_address, gas_price, gas_limit)` | Parses address text and delegates to `allow_gas(...)`. | Returns `ScriptBuilder`; parse failures are stored as builder errors. | Examples or CLI code receives addresses as text. |
| `spend_gas(address)` | Appends `gas.SpendGas`. | Returns `ScriptBuilder`. | VM transaction script should close gas handling. |
| `spend_gas_text(address)` | Parses address text and delegates to `spend_gas(...)`. | Returns `ScriptBuilder`; parse failures are stored as builder errors. | Examples or CLI code receives address text. |
| `transfer_tokens(symbol, from_address, to_address, amount)` | Appends `Runtime.TransferTokens` for fungible amount transfer. | Returns `ScriptBuilder`. | VM script transfers fungible tokens using validated addresses. |
| `transfer_tokens_text(symbol, from_address, to_address, amount)` | Parses both address strings and delegates to `transfer_tokens(...)`. | Returns `ScriptBuilder`; parse failures are stored as builder errors. | CLI/example code receives both addresses as text. |
| `transfer_tokens_to_text(symbol, from_address, to_address, amount)` | Uses an `Address` sender and parses text receiver. | Returns `ScriptBuilder`; receiver parse failure is stored as builder error. | Code already validated the sender but not the receiver. |
| `mint_tokens(symbol, from_address, to_address, amount)` | Appends `Runtime.MintTokens`. | Returns `ScriptBuilder`. | VM script mints fungible tokens through the runtime path. |
| `mint_tokens_text(symbol, from_address, to_address, amount)` | Parses both addresses and delegates to `mint_tokens(...)`. | Returns `ScriptBuilder`; parse failures are stored as builder errors. | CLI/example code receives both addresses as text. |
| `transfer_balance(symbol, from_address, to_address)` | Appends `Runtime.TransferBalance` for the whole balance of a symbol. | Returns `ScriptBuilder`. | VM script should transfer the full token balance. |
| `transfer_balance_text(symbol, from_address, to_address)` | Parses both addresses and delegates to `transfer_balance(...)`. | Returns `ScriptBuilder`; parse failures are stored as builder errors. | CLI/example code receives both addresses as text. |
| `transfer_nft(symbol, from_address, to_address, token_id)` | Appends `Runtime.TransferToken` for one NFT id. | Returns `ScriptBuilder`. | VM script transfers a single NFT. |
| `transfer_nft_text(symbol, from_address, to_address, token_id)` | Parses both addresses and delegates to `transfer_nft(...)`. | Returns `ScriptBuilder`; parse failures are stored as builder errors. | CLI/example code receives both addresses as text. |
| `transfer_nft_to_text(symbol, from_address, to_address, token_id)` | Uses an `Address` sender and parses text receiver. | Returns `ScriptBuilder`; receiver parse failure is stored as builder error. | Code already validated the sender but not the receiver. |
| `cross_transfer_token(destination_chain, symbol, from_address, to_address, amount)` | Appends `Runtime.SendTokens` with destination chain address and token amount. | Returns `ScriptBuilder`. | VM script sends fungible tokens across chains. |
| `cross_transfer_token_text(destination_chain, symbol, from_address, to_address, amount)` | Parses destination, sender, and receiver address text and delegates to `cross_transfer_token(...)`. | Returns `ScriptBuilder`; parse failures are stored as builder errors. | CLI/example code receives all addresses as text. |
| `cross_transfer_token_to_text(destination_chain, symbol, from_address, to_address, amount)` | Uses validated destination and sender addresses and parses receiver text. | Returns `ScriptBuilder`; receiver parse failure is stored as builder error. | Code already validated source-side addresses. |
| `cross_transfer_nft(destination_chain, symbol, from_address, to_address, token_id)` | Appends `Runtime.SendToken` with destination chain address and NFT id. | Returns `ScriptBuilder`. | VM script sends one NFT across chains. |
| `cross_transfer_nft_text(destination_chain, symbol, from_address, to_address, token_id)` | Parses destination, sender, and receiver address text and delegates to `cross_transfer_nft(...)`. | Returns `ScriptBuilder`; parse failures are stored as builder errors. | CLI/example code receives all addresses as text. |
| `cross_transfer_nft_to_text(destination_chain, symbol, from_address, to_address, token_id)` | Uses validated destination and sender addresses and parses receiver text. | Returns `ScriptBuilder`; receiver parse failure is stored as builder error. | Code already validated source-side addresses. |
| `stake(address, amount)` | Appends `stake.Stake`. | Returns `ScriptBuilder`. | VM script stakes a base-unit amount. |
| `stake_text(address, amount)` | Parses address text and delegates to `stake(...)`. | Returns `ScriptBuilder`; parse failure is stored as builder error. | CLI/example code receives address text. |
| `unstake(address, amount)` | Appends `stake.Unstake`. | Returns `ScriptBuilder`. | VM script unstakes a base-unit amount. |
| `unstake_text(address, amount)` | Parses address text and delegates to `unstake(...)`. | Returns `ScriptBuilder`; parse failure is stored as builder error. | CLI/example code receives address text. |
| `call_nft(symbol, series_id, method, *args)` | Calls a token-series contract named `"{symbol}#{series_id}"`. | Returns `ScriptBuilder`; unsupported args store a builder error. | VM script calls an NFT series contract method. |

Example:

```python
from phantasma_py.crypto import Address
from phantasma_py.vm import ScriptBuilder

sender = Address.from_text("P...")
receiver = Address.from_text("P...")

script = (
    ScriptBuilder.begin()
    .allow_gas(sender, Address.null(), 100000, 21000)
    .transfer_tokens("SOUL", sender, receiver, 100000000)
    .spend_gas(sender)
    .end_script()
)
```

## VM Transactions

| API | Purpose and parameters | Returns and failures | Use it when |
| --- | ---------------------- | -------------------- | ----------- |
| `Transaction(nexus_name, chain_name, script, expiration, payload=SDK_PAYLOAD, signatures=[])` | Creates a VM script transaction. `script` and `payload` are bytes; `expiration` is a Unix timestamp in seconds. | Returns `Transaction`. | Code has final script bytes and is ready to sign or serialize a VM transaction. |
| `hash` | Property calculated from unsigned transaction bytes, excluding signatures. | Returns `Hash`. | Code needs the transaction hash before or after signing. |
| `to_bytes(*, with_signatures=True)` | Serializes nexus, chain, script, expiration, payload, and optionally signatures. | Returns `bytes`. | RPC broadcast or signing needs transaction bytes. Use `with_signatures=False` for the signing message. |
| `Transaction.from_bytes(data)` | Parses transaction bytes, including Ed25519 signatures. | Returns `Transaction`; raises on unsupported signature kind, malformed streams, or trailing bytes. | A tool needs to inspect or re-broadcast serialized VM transaction bytes. |
| `sign(key_pair)` | Signs unsigned transaction bytes and appends the signature. | Returns `Ed25519Signature`. | Trusted code owns a private key and signs a VM transaction. |
| `is_signed_by(key_pair)` | Verifies whether any appended signature matches the key pair's address. | Returns `bool`. | Tooling checks whether a transaction already has the expected signer. |
| `mine(difficulty)` | Mutates `payload` with incrementing 4-byte nonces until `hash.difficulty()` reaches `difficulty`. Difficulty `<= 0` is a no-op. | Returns `None`. | A transaction needs the SDK's proof-of-work payload mining behavior. |
| `tx_state_is_success(state)` | Compares state case-insensitively to `HALT`. | Returns `bool`. | Code checks finalized RPC transaction state. |
| `tx_state_is_fault(state)` | Compares state case-insensitively to `FAULT` or `BREAK`. | Returns `bool`. | Code checks finalized RPC transaction failure state. |
