# Rust SDK VM and Transaction APIs

This page documents the lower-level `phantasma_sdk` APIs outside the Carbon
module. Use these APIs for classic VM scripts, VM transaction bytes, local
transaction signing, key/address handling, and VM object decoding. Use the
Carbon API instead for Carbon token, series, NFT, transfer, market, and message
payload flows.

Fallible APIs return `phantasma_sdk::Result<T>`, an alias for
`std::result::Result<T, PhantasmaError>`.

## Crypto Constants And Enums

| API | Purpose |
| --- | ------- |
| `ADDRESS_LENGTH` | Address byte length, currently `34`. |
| `PRIVATE_KEY_LENGTH` | Private key byte length, currently `32`. |
| `PUBLIC_KEY_LENGTH` | Ed25519 public key byte length, currently `32`. |
| `SIGNATURE_LENGTH` | Ed25519 signature byte length, currently `64`. |
| `AddressKind` | Address kind enum: `Invalid`, `User`, `System`, `Interop`. `Address::kind()` returns `System` for the null address. |
| `SignatureKind` | Signature kind enum: `None`, `Ed25519`, `Ecdsa`, `Ring`. The SDK only implements Ed25519 signatures in `Ed25519Signature`. |

## Address

`Address` stores the 34-byte Phantasma address payload. It is the type to keep
at API boundaries after text input has been parsed.

| Method | Purpose | Inputs | Returns and failures |
| ------ | ------- | ------ | -------------------- |
| `Address::new(data)` | Wraps an already validated `[u8; ADDRESS_LENGTH]`. | `data`: exact 34-byte address payload. | Returns `Address`. It does not validate the kind byte. |
| `Address::try_from_slice(data)` | Parses an address from a byte slice. | `data`: must contain exactly `ADDRESS_LENGTH` bytes. | Returns `Result<Address>`. Fails with `Crypto` if the slice length is not 34. |
| `Address::null()` | Builds the null address. | None. | Returns an all-zero `Address`. `to_text()` renders it as `NULL`. |
| `Address::from_public_key(public_key)` | Derives a user address from an Ed25519 public key shape accepted by the SDK. | `public_key`: 32, 33, or 64 bytes. A 32-byte key is stored after the user kind/reserved bytes; a 33-byte key is copied after the kind byte; a 64-byte value uses the first 32 bytes. | Returns `Result<Address>`. Fails with `Crypto` for any other public-key length. |
| `Address::from_text(text)` | Parses a Phantasma address string. | `text`: `NULL`, empty string, or a Base58 address prefixed with `P`, `S`, or `X`. | Returns `Result<Address>`. Fails with `Encoding` for invalid Base58, or `Crypto` for short text, unknown prefixes, wrong byte length, or prefix/kind mismatch. |
| `Address::from_hash(value)` | Derives a user address from a SHA-256 hash of arbitrary bytes. | `value`: bytes to hash. | Returns `Address`; the result is kind `User`. |
| `data()` | Borrows the address payload. | None. | Returns `&[u8; ADDRESS_LENGTH]`. |
| `into_bytes()` | Consumes the address and returns the payload. | None. | Returns `[u8; ADDRESS_LENGTH]`. |
| `is_null()` | Checks for the all-zero address. | None. | Returns `bool`. |
| `kind()` | Reads the address kind from the payload. | None. | Returns `AddressKind`; null is reported as `System`, byte `1` as `User`, byte `2` as `System`, bytes `>= 3` as `Interop`, and other values as `Invalid`. |
| `public_key()` | Extracts the embedded Ed25519 public key from a user address. | None. | Returns `Result<[u8; PUBLIC_KEY_LENGTH]>`. Fails with `Crypto` if the address kind is not `User`. |
| `to_text()` | Converts the address to Phantasma text form. | None. | Returns `String`: `NULL`, or Base58 with `P`, `S`, or `X` prefix based on `kind()`. Invalid kinds use the `P` prefix path. |
| `prefixed_bytes()` | Encodes the address as VM var-bytes. | None. | Returns `Vec<u8>` containing a VM length prefix followed by the 34-byte payload. Use this when manually building VM script arguments. |

Use `from_text(...)` once at the input boundary, then pass `Address` through the
rest of the program. Use the `*_text` ScriptBuilder variants only when the
builder is the first place where an address string is available.

## Hash

`Hash` stores a 32-byte hash and provides Phantasma text and local PoW helpers.

| Method | Purpose | Inputs | Returns and failures |
| ------ | ------- | ------ | -------------------- |
| `Hash::new(data)` | Wraps an already validated 32-byte value. | `data`: `[u8; 32]`. | Returns `Hash`. |
| `Hash::try_from_slice(data)` | Parses a hash from a slice. | `data`: must contain exactly 32 bytes. | Returns `Result<Hash>`. Fails with `Crypto` if the length is not 32. |
| `Hash::sha256(data)` | Computes SHA-256 over bytes. | `data`: bytes to hash. | Returns `Hash`. |
| `to_hex()` | Renders uppercase hexadecimal. | None. | Returns `String`. |
| `difficulty()` | Computes the Phantasma transaction mining difficulty from the hash bytes. | None. | Returns `u32`. Difficulty is derived from the last set bit in the little-endian hash representation used by the SDK transaction mining helper. |

## Ed25519Signature

`Ed25519Signature` stores a 64-byte Ed25519 signature and can verify it against
one or more candidate Phantasma user addresses.

| Method | Purpose | Inputs | Returns and failures |
| ------ | ------- | ------ | -------------------- |
| `Ed25519Signature::new(data)` | Wraps an exact signature byte array. | `data`: `[u8; SIGNATURE_LENGTH]`. | Returns `Ed25519Signature`. |
| `Ed25519Signature::try_from_slice(data)` | Parses a signature from a slice. | `data`: must contain exactly 64 bytes. | Returns `Result<Ed25519Signature>`. Fails with `Crypto` if the length is not 64. |
| `data()` | Borrows the signature bytes. | None. | Returns `&[u8; SIGNATURE_LENGTH]`. |
| `kind()` | Reports the SDK signature kind. | None. | Returns `SignatureKind::Ed25519`. |
| `verify(message, addresses)` | Checks whether the signature is valid for any supplied user address. | `message`: signed bytes. `addresses`: iterable of `&Address`. | Returns `bool`. Non-user addresses, invalid extracted public keys, and failed Ed25519 verification return `false`; they do not raise errors. |
| `serialize_data()` | Encodes signature bytes as VM var-bytes. | None. | Returns `Vec<u8>`. This serializes only the signature data, not the signature kind byte used inside transaction bytes. |

Use `verify(...)` for local login challenges, signed off-chain messages, or
local checks on transaction signatures. Transaction parsing already rejects
unsupported signature kinds before constructing `Ed25519Signature` values.

## PhantasmaKeys

`PhantasmaKeys` owns a private key. Use it in trusted tools, local scripts,
backend services, and tests. Wallet-facing applications should ask a wallet to
sign instead of importing private keys.

| Method | Purpose | Inputs | Returns and failures |
| ------ | ------- | ------ | -------------------- |
| `PhantasmaKeys::new(private_key)` | Wraps an exact private-key byte array. | `private_key`: `[u8; PRIVATE_KEY_LENGTH]`. | Returns `PhantasmaKeys`. |
| `PhantasmaKeys::try_from_slice(private_key)` | Parses private-key bytes. | `private_key`: 32 bytes, or 64 bytes where the first 32 bytes are used. | Returns `Result<PhantasmaKeys>`. Fails with `Crypto` for any other length. |
| `PhantasmaKeys::generate()` | Generates a new Ed25519 private key from the OS RNG. | None. | Returns `PhantasmaKeys`. |
| `PhantasmaKeys::from_wif(wif)` | Parses a compressed Phantasma WIF string. | `wif`: Base58 WIF text. | Returns `Result<PhantasmaKeys>`. Fails with `Crypto` for empty text, invalid length, invalid checksum, or non-compressed payload shape; fails with `Encoding` for invalid Base58. |
| `private_key()` | Borrows the private-key bytes. | None. | Returns `&[u8; PRIVATE_KEY_LENGTH]`. |
| `signing_key()` | Builds an `ed25519_dalek::SigningKey`. | None. | Returns `SigningKey`. |
| `public_key()` | Derives the Ed25519 public key. | None. | Returns `[u8; PUBLIC_KEY_LENGTH]`. |
| `address()` | Derives the Phantasma user address for the key pair. | None. | Returns `Address`. |
| `to_wif()` | Serializes the private key to compressed WIF. | None. | Returns Base58 WIF `String` with checksum. |
| `sign(message)` | Signs bytes with Ed25519. | `message`: bytes to sign. | Returns `Ed25519Signature`. |

## Encoding Helpers

These helpers are byte/text codecs. They do not validate higher-level
transaction, VM object, or Carbon payload structure.

| Function | Purpose | Inputs | Returns and failures |
| -------- | ------- | ------ | -------------------- |
| `encode_base58(data)` | Encodes bytes with the Bitcoin Base58 alphabet used by Phantasma address and WIF text. | `data`: bytes. | Returns `String`. |
| `decode_base58(text)` | Decodes Base58 text. | `text`: non-empty Base58 text. | Returns `Result<Vec<u8>>`. Fails with `Encoding` for empty text, invalid characters, or Base58 decoder failures. |
| `encode_hex(data)` | Encodes lowercase hexadecimal. | `data`: bytes. | Returns `String`. |
| `encode_hex_upper(data)` | Encodes uppercase hexadecimal. | `data`: bytes. | Returns `String`. |
| `decode_hex(value)` | Decodes hexadecimal text. | `value`: hex text; optional `0x` or `0X` prefix is accepted and surrounding whitespace is trimmed. | Returns `Result<Vec<u8>>`. Fails with `Encoding` when the number of digits is odd or a digit is invalid. |
| `double_sha256(data)` | Computes SHA-256 twice. | `data`: bytes. | Returns `[u8; 32]`. Used by WIF checksum handling. |

## VM Binary Writer

`BinaryWriter` implements the VM binary encoding used by scripts, transactions,
and VM object values. It is separate from `CarbonWriter`; Carbon uses different
length and integer rules.

| Method | Purpose | Inputs | Returns and failures |
| ------ | ------- | ------ | -------------------- |
| `BinaryWriter::new()` | Creates an empty writer. | None. | Returns `BinaryWriter`. |
| `write_u8(value)` | Writes one byte. | `value`: `u8`. | Mutates the writer. |
| `write_u16_le(value)` | Writes a little-endian unsigned 16-bit integer. | `value`: `u16`. | Mutates the writer. |
| `write_u32_le(value)` | Writes a little-endian unsigned 32-bit integer. | `value`: `u32`. | Mutates the writer. |
| `write_u64_le(value)` | Writes a little-endian unsigned 64-bit integer. | `value`: `u64`. | Mutates the writer. |
| `write_i64_le(value)` | Writes a little-endian signed 64-bit integer. | `value`: `i64`. | Mutates the writer. |
| `write_bool(value)` | Writes a VM boolean byte. | `value`: `bool`. | Writes `0` or `1`. |
| `write(data)` | Appends raw bytes. | `data`: bytes. | Mutates the writer without adding a length prefix. |
| `write_var_uint(value)` | Writes the VM variable-length unsigned integer format. | `value`: `u64`. | Uses one byte for `< 0xFD`, then `0xFD`/`u16`, `0xFE`/`u32`, or `0xFF`/`u64`. |
| `write_var_bytes(data)` | Writes a VM var-uint length followed by bytes. | `data`: bytes. | Mutates the writer. |
| `write_string(value)` | Writes UTF-8 string bytes as VM var-bytes. | `value`: `&str`. | Mutates the writer. |
| `write_big_integer(value)` | Writes a VM BigInteger var-byte payload. | `value`: `BigInt`. | Returns `Result<()>`. The current encoder accepts arbitrary `BigInt` values and applies the VM sign-padding shape. |
| `bytes()` | Borrows the current buffer. | None. | Returns `&[u8]`. |
| `into_bytes()` | Consumes the writer. | None. | Returns `Vec<u8>`. |

## VM Binary Reader

`MAX_ARRAY_SIZE` is `0x0100_0000` and is used as the upper bound for hostile or
external length-prefixed payloads.

| Method | Purpose | Inputs | Returns and failures |
| ------ | ------- | ------ | -------------------- |
| `BinaryReader::new(data)` | Creates a reader over existing bytes. | `data`: borrowed byte slice. | Returns `BinaryReader`. |
| `remaining()` | Reports unread bytes. | None. | Returns `usize`. |
| `assert_eof()` | Verifies that the reader consumed the whole slice. | None. | Returns `Result<()>`. Fails with `Serialization` if trailing bytes remain. |
| `read(count)` | Reads a fixed number of bytes. | `count`: requested byte count. | Returns `Result<Vec<u8>>`. Fails with `Serialization` if the stream ends first. |
| `read_array::<N>()` | Reads a fixed-size byte array. | Const `N`: requested array length. | Returns `Result<[u8; N]>`. Fails with `Serialization` if fewer than `N` bytes remain. |
| `read_u8()` | Reads one byte. | None. | Returns `Result<u8>`. |
| `read_u16_le()` | Reads little-endian `u16`. | None. | Returns `Result<u16>`. |
| `read_u32_le()` | Reads little-endian `u32`. | None. | Returns `Result<u32>`. |
| `read_u64_le()` | Reads little-endian `u64`. | None. | Returns `Result<u64>`. |
| `read_i64_le()` | Reads little-endian `i64`. | None. | Returns `Result<i64>`. |
| `read_bool()` | Reads a VM boolean byte. | None. | Returns `Result<bool>`. Any non-zero byte is `true`. |
| `read_var_uint()` | Reads the VM variable-length unsigned integer format. | None. | Returns `Result<u64>`. Fails if the stream ends while reading the prefix or payload. |
| `read_var_bytes(max_size)` | Reads VM var-bytes with an allocation guard. | `max_size`: caller-supplied maximum accepted length. | Returns `Result<Vec<u8>>`. Fails with `Serialization` if the encoded length exceeds `usize`, exceeds `max_size`, or bytes are truncated. |
| `read_string()` | Reads UTF-8 VM var-bytes. | None. | Returns `Result<String>`. Fails with `Serialization` for oversized/truncated bytes or invalid UTF-8. |
| `read_big_integer()` | Reads a VM BigInteger payload. | None. | Returns `Result<BigInt>`. Fails if the var-bytes cannot be read. |

| Function | Purpose | Inputs | Returns and failures |
| -------- | ------- | ------ | -------------------- |
| `big_int_to_vm_bytes(value)` | Encodes a Rust `BigInt` into Phantasma VM BigInteger bytes. | `value`: `BigInt`. | Returns `Result<Vec<u8>>`. It writes the Gen2 sign-padding shape used by `BinaryWriter` and `VMObject`. |
| `vm_bytes_to_big_int(data)` | Decodes Phantasma VM BigInteger bytes. | `data`: bytes. | Returns `BigInt`; an empty slice decodes to zero. |

## VM Object

`VMObject` decodes values returned by read-only VM scripts. Its variants are
`None`, `Struct`, `Bytes`, `Number`, `String`, `Timestamp`, `Bool`, `Enum`, and
`Object`. `VMType` has the corresponding discriminants.

| Method | Purpose | Inputs | Returns and failures |
| ------ | ------- | ------ | -------------------- |
| `VMObject::from_bytes(data)` | Decodes one complete VM object from bytes. | `data`: encoded VM object bytes. | Returns `Result<VMObject>`. Fails with `Serialization` for unsupported object type, truncated fields, invalid UTF-8 where strings are decoded, or trailing bytes after the object. |
| `VMObject::read(reader)` | Decodes one VM object from an existing `BinaryReader`. | `reader`: mutable VM reader. | Returns `Result<VMObject>`. Leaves the reader after the object. It does not require EOF. |
| `vm_type()` | Reports the variant as `VMType`. | None. | Returns `VMType`. |
| `as_number()` | Converts the object to a number using SDK conversion rules. | None. | Returns `Result<BigInt>`. Numbers return themselves; bytes decode as signed VM integers; 32-byte objects decode as unsigned hash-backed integers; booleans return `0`/`1`; strings must parse as `BigInt`; enum and timestamp values convert directly; `None` returns zero. Other structs/objects fail with `Serialization`. |
| `as_string()` | Converts the object to a string. | None. | Returns `Result<String>`. Strings return themselves; bytes must be valid UTF-8; booleans return `true`/`false`; numbers, enum, and timestamp values use decimal text; `None` returns `Null`; numeric arrays are decoded as UTF-16 strings; other structs are base64 of their encoded bytes; objects fail. |
| `as_bytes()` | Converts the object to bytes. | None. | Returns `Result<Vec<u8>>`. Strings use UTF-8; bytes and objects return their payloads; booleans return one byte; enum/timestamp use little-endian `u32`; numbers use VM BigInteger bytes; structs serialize with `to_bytes()`. `None` fails with `Serialization`. |
| `as_bool()` | Converts the object to a boolean. | None. | Returns `Result<bool>`. Booleans return themselves; one-byte byte arrays return whether the byte is non-zero; numbers return whether they are non-zero. Other types fail with `Serialization`. |
| `cast_to(target)` | Converts the object to a target VM type. | `target`: `VMType`. | Returns `Result<VMObject>`. Supports conversions to `None`, `String`, `Bytes`, `Number`, and `Bool`; string-to-struct creates a UTF-16 indexed struct; object-to-struct returns the object clone. Unsupported casts fail with `Serialization`. |
| `array_type()` | Detects whether a struct is an array of one VM type. | None. | Returns `VMType`; non-structs, sparse keys, mixed element types, and empty structs return `VMType::None`. |
| `to_bytes()` | Serializes the object. | None. | Returns `Result<Vec<u8>>`. Fails if `write(...)` fails. |
| `write(writer)` | Writes the object to a `BinaryWriter`. | `writer`: mutable VM writer. | Returns `Result<()>`. Fails with `Serialization` if an `Enum` value exceeds one byte or nested object serialization fails. |

Use the typed accessors only after checking the expected script return shape.
They apply SDK conversion rules; they are not schema validation for arbitrary
contract data.

## Script Arguments

`ScriptArg` is the input type used by high-level `ScriptBuilder` calls.

| Variant or impl | Purpose |
| --------------- | ------- |
| `Address(Address)` | VM address argument; the builder writes the address as VM bytes using `Address::prefixed_bytes()`. |
| `String(String)` / `From<&str>` | VM string argument. |
| `Bool(bool)` | VM boolean argument. |
| `Bytes(Vec<u8>)` / `From<&[u8]>` | Raw VM byte argument. |
| `Number(BigInt)` | VM number argument. `From<i64>`, `From<u64>`, `From<i32>`, `From<u32>`, `From<usize>`, and `From<BigInt>` are implemented. |
| `Timestamp(u64)` | VM timestamp argument. Construct this variant directly when a timestamp is required. |
| `Array(Vec<ScriptArg>)` / `From<Vec<ScriptArg>>` | VM array-like struct argument. Array loading needs three registers starting at the target register. |
| `script_arg_number_to_i64(value)` | Returns `Some(i64)` only when `value` is `ScriptArg::Number` and fits into `i64`; otherwise returns `None`. |

## ScriptBuilder Lifecycle

`ScriptBuilder` latches builder errors and reports them when the final script is
requested. This allows chained builder calls to keep returning `&mut Self`.

| Method | Purpose | Inputs | Returns and failures |
| ------ | ------- | ------ | -------------------- |
| `ScriptBuilder::new()` | Creates an empty script builder. | None. | Returns `ScriptBuilder`. |
| `ScriptBuilder::begin()` | Alias for `new()`. | None. | Returns `ScriptBuilder`. |
| `current_size()` | Reports the number of bytes currently emitted. | None. | Returns `usize`. |
| `end_script()` | Appends `Opcode::Ret`, patches labels, and returns script bytes. | None. | Returns `Result<Vec<u8>>`. Fails with `Builder` for latched builder errors, missing labels, invalid jump patch offsets, invalid jump opcodes, invalid register counts, invalid address text in `*_text` methods, oversized loads, or timestamp overflow. |
| `end_script_hex()` | Finalizes the script and encodes it as uppercase hex. | None. | Returns `Result<String>`; propagates `end_script()` failures. |
| `end_script_with_error()` | Finalizes without using `Result`. | None. | Returns `(Vec<u8>, Option<PhantasmaError>)`. On error the script vector is empty and the error is returned. |
| `to_script()` | Returns emitted bytes with jump labels patched, without appending `Ret`. | None. | Returns `Result<Vec<u8>>`. Fails with `Builder` for missing labels or invalid patch offsets. Use this for compiler-style flows that manage the final opcode themselves. |

`ScriptBuilder::MAX_REGISTER_COUNT` is `32`.

## ScriptBuilder Low-Level Emission

Use these methods for compiler-like tools, tests, or advanced VM scripts. Most
application code should use `call_contract(...)`, `call_interop(...)`, or one of
the convenience methods.

| Method | Purpose | Inputs | Returns and failures |
| ------ | ------- | ------ | -------------------- |
| `emit(opcode)` | Appends an opcode byte. | `opcode`: `Opcode`. | Returns `&mut Self`. |
| `emit_raw(data)` | Appends raw bytes with no validation. | `data`: bytes. | Returns `&mut Self`. |
| `emit_push(reg)` | Emits `Push` for a register. | `reg`: register index. | Returns `&mut Self`. |
| `emit_pop(reg)` | Emits `Pop` for a register. | `reg`: register index. | Returns `&mut Self`. |
| `emit_throw(reg)` | Emits `Throw` for a register. | `reg`: register index. | Returns `&mut Self`. |
| `emit_ext_call(method, reg)` | Loads an interop method name into `reg` and emits `ExtCall`. | `method`: interop name. `reg`: register index. | Returns `&mut Self`; can latch a builder error if the method string load exceeds the load size limit. |
| `emit_load(reg, data, vm_type)` | Emits a VM `Load` instruction. | `reg`: target register. `data`: raw payload. `vm_type`: payload type. | Returns `&mut Self`. Latches `Builder` if `data` is longer than `0xFFFF` bytes. |
| `emit_load_string(reg, value)` | Loads a VM string. | `value`: UTF-8 string. | Returns `&mut Self`; can latch the same oversized-load error as `emit_load`. |
| `emit_load_bool(reg, value)` | Loads a VM bool. | `value`: `bool`. | Returns `&mut Self`. |
| `emit_load_number(reg, value)` | Loads a VM number for a `LOAD` instruction. | `value`: `BigInt`. | Returns `&mut Self`. This uses C# `BigInteger` bytes, not the padded VM object BigInteger bytes used by `BinaryWriter`. |
| `emit_load_timestamp(reg, unix_seconds)` | Loads a VM timestamp. | `unix_seconds`: must fit in `u32`. | Returns `&mut Self`; latches `Builder` if the timestamp is outside the VM `u32` range. |
| `emit_load_time(reg, unix_seconds)` | Alias for `emit_load_timestamp`. | Same as `emit_load_timestamp`. | Returns `&mut Self`. |
| `emit_move(src_reg, dst_reg)` | Emits register move. | Source and destination registers. | Returns `&mut Self`. |
| `emit_copy(src_reg, dst_reg)` | Emits register copy. | Source and destination registers. | Returns `&mut Self`. |
| `emit_label(label)` | Marks a jump target at the current byte position. | `label`: case-insensitive label text. | Returns `&mut Self`; internally emits `Nop` before recording the label location. |
| `emit_jump(opcode, label, reg)` | Emits an unconditional or conditional jump to a label. | `opcode`: must be `Jmp`, `JmpIf`, or `JmpNot`. `label`: target label. `reg`: condition register for conditional jumps. | Returns `&mut Self`. Latches `Builder` if the opcode is not a jump opcode; missing labels are reported by `to_script()`/`end_script()`. |
| `emit_call(label, register_count)` | Emits a VM call to a local label. | `label`: target label. `register_count`: `1..=32`. | Returns `&mut Self`. Latches `Builder` if the register count is zero or greater than `MAX_REGISTER_COUNT`. |
| `emit_conditional_jump(opcode, src_reg, label)` | Emits `JmpIf` or `JmpNot`. | `opcode`: must be `JmpIf` or `JmpNot`. | Returns `&mut Self`; latches `Builder` for other opcodes. |
| `emit_var_bytes(value)` | Emits a VM var-uint value directly. | `value`: `u64`. | Returns `&mut Self`. Despite the method name, it writes the length integer only. |

## ScriptBuilder Contract And Runtime Calls

The following methods append standard Phantasma VM calls.

| Method | Purpose | Inputs | Returns and failures |
| ------ | ------- | ------ | -------------------- |
| `call_interop(method, args)` | Calls a runtime interop method with VM arguments. | `method`: interop name, for example `Runtime.TransferTokens`. `args`: iterable of `ScriptArg`. | Returns `&mut Self`. Argument loading can latch builder errors for invalid array register use, oversized string/byte loads, or timestamp overflow. |
| `call_contract(contract_name, method, args)` | Switches context to a contract and calls a method. | `contract_name`, `method`, and iterable of `ScriptArg`. | Returns `&mut Self`; same argument-loading failures as `call_interop`. |
| `allow_gas(from, to, gas_price, gas_limit)` | Adds `gas.AllowGas`. | `from` and `to`: `Address`; `gas_price`/`gas_limit`: base-unit gas values. | Returns `&mut Self`. |
| `allow_gas_text(from, to, gas_price, gas_limit)` | Parses address strings and adds `gas.AllowGas`. | `from`, `to`: address text. | Returns `&mut Self`. Latches `Builder` if either address fails `Address::from_text`. |
| `spend_gas(address)` | Adds `gas.SpendGas`. | `address`: `Address`. | Returns `&mut Self`. |
| `spend_gas_text(address)` | Parses an address string and adds `gas.SpendGas`. | `address`: address text. | Returns `&mut Self`. Latches `Builder` on parse failure. |
| `transfer_tokens(symbol, from, to, amount)` | Adds `Runtime.TransferTokens` for fungible units. | `symbol`: token symbol. `from`, `to`: `Address`. `amount`: base units. | Returns `&mut Self`. |
| `transfer_tokens_text(symbol, from, to, amount)` | Parses sender and receiver text and adds `Runtime.TransferTokens`. | `from`, `to`: address text. | Returns `&mut Self`. Latches `Builder` if either address is invalid. |
| `transfer_tokens_to_text(symbol, from, to, amount)` | Uses a validated sender address and parses receiver text. | `from`: `Address`; `to`: address text. | Returns `&mut Self`. Use this when the sender is already typed and the recipient is user-entered text. |
| `mint_tokens(symbol, from, to, amount)` | Adds `Runtime.MintTokens`. | `symbol`, minter `from`, recipient `to`, base-unit `amount`. | Returns `&mut Self`. Chain-side authorization is decided when the transaction executes. |
| `mint_tokens_text(symbol, from, to, amount)` | Parses minter and recipient text and adds `Runtime.MintTokens`. | `from`, `to`: address text. | Returns `&mut Self`; latches address parse failures. |
| `transfer_balance(symbol, from, to)` | Adds `Runtime.TransferBalance`. | `symbol`, sender, receiver. | Returns `&mut Self`. |
| `transfer_balance_text(symbol, from, to)` | Parses sender and receiver text and adds `Runtime.TransferBalance`. | `from`, `to`: address text. | Returns `&mut Self`; latches address parse failures. |
| `transfer_nft(symbol, from, to, token_id)` | Adds `Runtime.TransferToken` for one NFT id. | `symbol`, sender, receiver, `token_id`. | Returns `&mut Self`. |
| `transfer_nft_text(symbol, from, to, token_id)` | Parses sender and receiver text and adds NFT transfer. | `from`, `to`: address text. | Returns `&mut Self`; latches address parse failures. |
| `transfer_nft_to_text(symbol, from, to, token_id)` | Uses a validated sender and parses receiver text for NFT transfer. | `from`: `Address`; `to`: address text. | Returns `&mut Self`; latches receiver parse failures. |
| `cross_transfer_token(destination_chain, symbol, from, to, amount)` | Adds `Runtime.SendTokens` for cross-chain fungible transfer. | `destination_chain`, sender, receiver: `Address`; `amount`: base units. | Returns `&mut Self`. |
| `cross_transfer_token_text(destination_chain, symbol, from, to, amount)` | Parses all addresses and adds cross-chain fungible transfer. | `destination_chain`, `from`, `to`: address text. | Returns `&mut Self`; latches the first address parse failure. |
| `cross_transfer_token_to_text(destination_chain, symbol, from, to, amount)` | Uses typed destination/sender and parses receiver text. | `destination_chain`, `from`: `Address`; `to`: address text. | Returns `&mut Self`; latches receiver parse failures. |
| `cross_transfer_nft(destination_chain, symbol, from, to, token_id)` | Adds `Runtime.SendToken` for one NFT id. | `destination_chain`, sender, receiver: `Address`; `token_id`: NFT id. | Returns `&mut Self`. |
| `cross_transfer_nft_text(destination_chain, symbol, from, to, token_id)` | Parses all addresses and adds cross-chain NFT transfer. | `destination_chain`, `from`, `to`: address text. | Returns `&mut Self`; latches the first address parse failure. |
| `cross_transfer_nft_to_text(destination_chain, symbol, from, to, token_id)` | Uses typed destination/sender and parses receiver text for NFT transfer. | `destination_chain`, `from`: `Address`; `to`: address text. | Returns `&mut Self`; latches receiver parse failures. |
| `stake(address, amount)` | Adds `stake.Stake`. | `address`: staker. `amount`: base units. | Returns `&mut Self`. |
| `stake_text(address, amount)` | Parses staker text and adds `stake.Stake`. | `address`: address text. | Returns `&mut Self`; latches parse failures. |
| `unstake(address, amount)` | Adds `stake.Unstake`. | `address`: staker. `amount`: base units. | Returns `&mut Self`. |
| `unstake_text(address, amount)` | Parses staker text and adds `stake.Unstake`. | `address`: address text. | Returns `&mut Self`; latches parse failures. |
| `call_nft(symbol, series_id, method, args)` | Calls a method on the contract name formed as `{symbol}#{series_id}`. | `symbol`, `series_id`, method name, and arguments. | Returns `&mut Self`. Use this for VM contract calls against NFT series contracts, not Carbon lifecycle builders. |

Example:

```rust
use phantasma_sdk::{Address, Result, ScriptBuilder};

fn transfer_script(sender_text: &str, receiver_text: &str) -> Result<Vec<u8>> {
    let sender = Address::from_text(sender_text)?;
    let receiver = Address::from_text(receiver_text)?;

    ScriptBuilder::begin()
        .allow_gas(sender, Address::null(), 100000, 21000)
        .transfer_tokens("SOUL", sender, receiver, 100000000)
        .spend_gas(sender)
        .end_script()
}
```

## Transaction

`Transaction` wraps a VM script with nexus, chain, expiration, payload, and
signatures. Build the script first, create the transaction, sign it locally, and
broadcast with `PhantasmaRpc::send_transaction(...)` or
`PhantasmaRpc::send_raw_transaction(...)`.

`SDK_PAYLOAD` is the default payload marker for newly built Rust SDK VM
transactions: `RS-SDK-v1.0.1`.

Fields:

```rust
pub nexus_name: String
pub chain_name: String
pub script: Vec<u8>
pub expiration: u32
pub payload: Vec<u8>
pub signatures: Vec<Ed25519Signature>
```

| Method | Purpose | Inputs | Returns and failures |
| ------ | ------- | ------ | -------------------- |
| `Transaction::new(nexus_name, chain_name, script, expiration)` | Creates an unsigned VM transaction. | `nexus_name`, `chain_name`, script bytes, and expiration as a Unix timestamp in seconds. | Returns `Transaction` with `SDK_PAYLOAD` and no signatures. It does not validate whether the chain will accept the expiration. |
| `with_payload(payload)` | Replaces the transaction payload. | `payload`: bytes. | Returns the updated `Transaction`. Use this before signing; changing the payload after signing changes the transaction hash and invalidates signatures. |
| `hash()` | Computes the transaction hash. | None. | Returns `Hash` over unsigned transaction bytes (`to_bytes(false)`). |
| `to_bytes(with_signatures)` | Serializes the transaction. | `with_signatures`: include signature count, kind, and signature bytes when `true`. | Returns `Vec<u8>`. Use `false` for the signable message and hash; use `true` for broadcast bytes. |
| `Transaction::from_bytes(data)` | Parses a serialized transaction with signatures. | `data`: serialized transaction bytes. | Returns `Result<Transaction>`. Fails with `Serialization` for truncated fields, unsupported signature kinds, or trailing bytes; fails with `Crypto` for malformed Ed25519 signature lengths. |
| `sign(key_pair)` | Signs the unsigned transaction bytes and appends the signature. | `key_pair`: `PhantasmaKeys`. | Returns the new `Ed25519Signature`. Mutates `signatures`. |
| `is_signed_by(key_pair)` | Checks whether any current signature verifies against the key pair address. | `key_pair`: `PhantasmaKeys`. | Returns `bool`. |
| `mine(difficulty)` | Mutates payload bytes until `hash().difficulty()` is at least `difficulty`. | `difficulty`: desired local PoW difficulty. | Returns `()`. Difficulty `0` is a no-op. Mining changes the payload and therefore must be done before signing. |

| Helper | Purpose | Inputs | Returns |
| ------ | ------- | ------ | ------- |
| `tx_state_is_success(state)` | Checks for a successful transaction state string. | `state`: transaction state text. | Returns `true` for `HALT`, case-insensitive. |
| `tx_state_is_fault(state)` | Checks for a failed transaction state string. | `state`: transaction state text. | Returns `true` for `FAULT` or `BREAK`, case-insensitive. |
| `transaction::big_int(value)` | Convenience constructor for `num_bigint::BigInt`. | `value`: `i64`. | Returns `BigInt`. This helper is available through the `transaction` module, not the crate root re-export list. |

## Error Model

| Error variant | Raised for |
| ------------- | ---------- |
| `Encoding(String)` | Base58, hex, and low-level encoding failures. |
| `Serialization(String)` | VM or Carbon serialization/deserialization failures. |
| `Crypto(String)` | Address, key, WIF, hash, and signature validation failures. |
| `Builder(String)` | Script builder and Carbon builder validation failures. |
| `Rpc { code, message }` | JSON-RPC error responses. |
| `Http(String)` | HTTP transport failures. |
| `Json(String)` | JSON serialization/deserialization failures. |

Handle narrow variants close to validation boundaries when the UI can show a
specific message. Propagate `Result<T>` from SDK-facing functions when the
caller only needs to know that SDK processing failed.
