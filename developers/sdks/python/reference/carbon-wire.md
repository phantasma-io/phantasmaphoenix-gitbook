# Python SDK Carbon API and Wire Format

`phantasma_py.carbon` contains Carbon serialization primitives, typed wire
structures, transaction message payloads, schema helpers, fee helpers, token
lifecycle builders, and result parsers.

Use the high-level builders for token deployment, token series creation, NFT
minting, and Phantasma NFT mint payloads. Use the typed message structures when
a wallet or service needs to inspect or assemble a Carbon transaction. Use
`CarbonReader` and `CarbonWriter` only for protocol tooling, diagnostics, tests,
or custom messages not covered by a builder.

## API Layers

| Layer | Main APIs | Use it for |
| ----- | --------- | ---------- |
| Lifecycle builders | `build_create_token_tx`, `build_create_token_series_tx`, `build_mint_non_fungible_tx`, `build_mint_phantasma_non_fungible_tx`, signed and hex builder variants | Build token, series, and NFT transaction messages with SDK fee defaults, expiry defaults, schema validation, and signer-derived addresses where the signed variants provide them. |
| Typed messages | `TxMsg`, `TxPayload`, `TxMsg*`, `SignedTxMsg`, `Witness`, module argument structures | Inspect, assemble, sign, serialize, or deserialize Carbon transaction messages directly when a lifecycle builder is not the right shape. |
| Wire primitives | `CarbonReader`, `CarbonWriter`, `serialize`, `deserialize`, `VMType`, `VMDynamicVariable`, `VMDynamicStruct` | Implement protocol tooling, tests, diagnostics, schema-aware metadata handling, or custom message support that does not have a lifecycle builder. |

## Error Model

| Error | Raised for |
| ----- | ---------- |
| `SerializationError` | Carbon byte-format errors, fixed-width byte length errors, integer range errors, truncated reads, unsupported dynamic VM types, invalid witness layout, and trailing bytes during `deserialize(...)`. |
| `BuilderError` | Schema JSON errors, metadata validation errors, token-symbol validation errors, missing required metadata fields, reserved Phantasma NFT fields, and invalid token lifecycle inputs. |
| `CryptoError` | Carbon address conversion or signing-key validation failures. |

## Core Serialization

| API | Purpose | Inputs | Returns and failures |
| --- | ------- | ------ | -------------------- |
| `serialize(value)` | Serializes a `CarbonSerializable` object. | `value`: object with `write_carbon(writer)`. | Returns `bytes`. Propagates errors from the object's writer. |
| `deserialize(data, cls)` | Parses one complete Carbon object. | `data`: bytes. `cls`: class with `read_carbon(reader)`. | Returns the decoded object. Fails if the object parser fails or if trailing bytes remain. |
| `bytes32_from_public_key(public_key)` | Converts an Ed25519 public key to Carbon `Bytes32`. | `public_key`: exactly 32 bytes. | Returns `Bytes32`. Fails with `CryptoError` if the length is not 32. |
| `bytes32_from_phantasma_address(address)` | Converts a Phantasma user or system address to Carbon `Bytes32`. | `address`: `phantasma_py.crypto.Address`. | Returns `Bytes32` from `address.data[2:]`. Fails with `CryptoError` for unsupported address kinds. |
| `bytes32_from_phantasma_address_text(text)` | Parses Phantasma address text, then converts it to Carbon `Bytes32`. | `text`: Phantasma address string. | Returns `Bytes32`. Propagates address parse errors and Carbon address-kind errors. |

## Fixed Byte Values And Small Values

| Type or method | Purpose | Inputs | Returns and failures |
| -------------- | ------- | ------ | -------------------- |
| `FixedBytes` | Base class for fixed-width Carbon byte wrappers. | Subclasses set `SIZE`; direct use is not needed for normal code. | Handles bytes, bytearray, hex strings, and empty zero-filled values for subclasses. |
| `Bytes16(value=b"")`, `Bytes32(value=b"")`, `Bytes64(value=b"")` | Fixed-width Carbon byte wrappers. | `value`: bytes, bytearray, hex string, or empty value. Empty value creates zero-filled bytes of the target size. | Returns an immutable bytes subclass. Fails with `SerializationError` when the decoded length is not 16, 32, or 64. |
| `Bytes16.from_hex(value)`, `Bytes32.from_hex(value)`, `Bytes64.from_hex(value)` | Builds fixed bytes from hex text. | `value`: hex string accepted by `decode_hex`. | Returns the fixed byte type. Fails on invalid hex or wrong length. |
| `str(fixed_bytes)` | Renders lowercase hex. | Fixed byte instance. | Returns `str`. |
| `SmallString(value="")` | Carbon one-byte-length UTF-8 string. | `value`: Python string whose UTF-8 length is at most 255 bytes. | Returns `SmallString`. Fails with `SerializationError` if the UTF-8 length exceeds 255 bytes. |
| `SmallString.write_carbon(writer)` | Writes one-byte length and UTF-8 bytes. | `writer`: `CarbonWriter`. | Mutates the writer. |
| `SmallString.read_carbon(reader)` | Reads one-byte length and UTF-8 bytes. | `reader`: `CarbonReader`. | Returns `SmallString`. Fails on truncated input, invalid UTF-8, or length > 255 in constructor. |
| `IntX(value=0)` | Carbon variable-width signed integer. | `value`: Python int. | Stores the value. |
| `IntX.is_8_byte_safe` | Checks whether `value` fits signed 64-bit range. | None. | Returns `bool`. |
| `IntX.write_carbon(writer)` | Writes the 8-byte IntX fast path when possible, otherwise compact Int256. | `writer`: `CarbonWriter`. | Fails with `SerializationError` if the wider value requires more than 256 bits. |
| `IntX.read_carbon(reader)` | Reads IntX from Carbon bytes. | `reader`: `CarbonReader`. | Returns `IntX`. Fails for invalid packing, truncated input, or non-standard BigInt header. |

Constants:

| Constant | Value role |
| -------- | ---------- |
| `EMPTY_BYTES16`, `EMPTY_BYTES32`, `EMPTY_BYTES64` | Zero-filled fixed byte values. |
| `SYSTEM_ADDRESS_NULL`, `SYSTEM_ADDRESS_GAS_POOL`, `SYSTEM_ADDRESS_DATA_POOL` | Carbon system address constants. |
| `STANDARD_META_ID` | Standard metadata id field name, `_i`. |

## CarbonWriter

`CarbonWriter` writes the Carbon binary format. It is not the VM transaction
binary writer.

| Method | Purpose | Inputs | Returns and failures |
| ------ | ------- | ------ | -------------------- |
| `CarbonWriter()` | Creates an empty writer. | None. | Returns `CarbonWriter`. |
| `write(data)` | Appends raw bytes without a length prefix. | `data`: bytes. | Mutates the writer. |
| `write1(value)` | Writes unsigned 8-bit integer. | `value`: 0..255. | Fails with `SerializationError` outside the range. |
| `write2(value)` | Writes signed little-endian 16-bit integer. | `value`: signed 16-bit range. | Fails outside the range. |
| `write4(value)` | Writes signed little-endian 32-bit integer. | `value`: signed 32-bit range. | Fails outside the range. |
| `write4u(value)` | Writes unsigned little-endian 32-bit integer. | `value`: unsigned 32-bit range. | Fails outside the range. |
| `write8(value)` | Writes signed little-endian 64-bit integer. | `value`: signed 64-bit range. | Fails outside the range. |
| `write8u(value)` | Writes unsigned little-endian 64-bit integer. | `value`: unsigned 64-bit range. | Fails outside the range. |
| `write16(value)` | Writes a `Bytes16` value. | `value`: `Bytes16` or bytes. | Fails if the value cannot be converted to 16 bytes. |
| `write32(value)` | Writes a `Bytes32` value. | `value`: `Bytes32` or bytes. | Fails if the value cannot be converted to 32 bytes. |
| `write64(value)` | Writes a `Bytes64` value. | `value`: `Bytes64` or bytes. | Fails if the value cannot be converted to 64 bytes. |
| `write_big_int(value)` | Writes compact Carbon Int256 bytes. | `value`: Python int. | Writes header `0` for zero. Otherwise writes the shortest little-endian slice of a 256-bit two's-complement word. Fails if the value requires more than 256 bits. |
| `write_big_int_array(values)` | Writes a Carbon array of compact big integers. | `values`: list of ints. | Writes signed 32-bit count then each big integer. Propagates big integer failures. |
| `write_string_z(value)` | Writes UTF-8 string followed by zero byte. | `value`: string without `\0`. | Fails if the string contains a zero byte. |
| `write_string_z_array(values)` | Writes an array of zero-terminated strings. | `values`: list of strings. | Writes signed 32-bit count and each `write_string_z(...)`. |
| `write_byte_array(data)` | Writes Carbon byte array. | `data`: bytes. | Writes signed 32-bit length and raw bytes. |
| `write_byte_arrays(values)` | Writes an array of byte arrays. | `values`: list of bytes. | Writes signed 32-bit count and each byte array. |
| `write_int_array(values, width, signed=...)` | Writes a fixed-width integer array. | `values`: list of ints. `width`: 1, 2, 4, or 8. `signed`: used for width 8 writer choice. | Writes signed 32-bit count. Width 1 writes the low byte with `value & 0xFF`; width 2 and 4 use signed writers; width 8 uses `write8` or `write8u`. Fails for unsupported widths or range failures from the selected writer. |
| `bytes()` | Returns current buffer. | None. | Returns `bytes`. |

## CarbonReader

`CarbonReader` is bounds-checked. `remaining` is a property, not a method.

| Method or property | Purpose | Inputs | Returns and failures |
| ------------------ | ------- | ------ | -------------------- |
| `CarbonReader(data)` | Creates a reader over bytes. | `data`: bytes. | Returns `CarbonReader`. |
| `remaining` | Reports unread bytes. | None. | Returns `int`. |
| `assert_eof()` | Checks that all bytes were consumed. | None. | Fails with `SerializationError` if any unread bytes remain. |
| `read(count)` | Reads exact byte count. | `count`: non-negative int not greater than `remaining`. | Returns `bytes`. Fails if count is negative or truncated. |
| `read_length()` | Reads signed 32-bit Carbon array length. | None. | Returns non-negative int. Fails if the length is negative or greater than remaining bytes. |
| `read1()` | Reads unsigned 8-bit integer. | None. | Returns `int`. |
| `read2()` | Reads signed little-endian 16-bit integer. | None. | Returns `int`. |
| `read4()` | Reads signed little-endian 32-bit integer. | None. | Returns `int`. |
| `read4u()` | Reads unsigned little-endian 32-bit integer. | None. | Returns `int`. |
| `read8()` | Reads signed little-endian 64-bit integer. | None. | Returns `int`. |
| `read8u()` | Reads unsigned little-endian 64-bit integer. | None. | Returns `int`. |
| `read16()` | Reads fixed 16 bytes. | None. | Returns `Bytes16`. |
| `read32()` | Reads fixed 32 bytes. | None. | Returns `Bytes32`. |
| `read64()` | Reads fixed 64 bytes. | None. | Returns `Bytes64`. |
| `read_big_int()` | Reads compact Carbon Int256. | None. | Returns `int`. Fails for truncated input, reserved header bit, length greater than 32, or non-standard sign header. |
| `read_big_int_with_header(header)` | Reads compact Int256 using an already-read header. | `header`: int or `None`. If `None`, the reader reads one byte first. | Returns `int`. Same failures as `read_big_int()`. |
| `read_big_int_array()` | Reads an array of compact big integers. | None. | Returns `list[int]`. |
| `read_string_z()` | Reads zero-terminated UTF-8 string. | None. | Returns `str`. Fails if no zero byte is found before EOF or UTF-8 decoding fails. |
| `read_string_z_array()` | Reads an array of zero-terminated strings. | None. | Returns `list[str]`. |
| `read_byte_array()` | Reads a Carbon byte array. | None. | Returns `bytes`. |
| `read_byte_arrays()` | Reads an array of byte arrays. | None. | Returns `list[bytes]`. |
| `read_int_array(width, signed=...)` | Reads a fixed-width integer array. | `width`: 1, 2, 4, or 8. `signed`: controls width 1 and width 8 interpretation. | Returns `list[int]`. Fails for unsupported widths or truncated input. |

## Enums And Flags

| Type | Values |
| ---- | ------ |
| `TxType` | `CALL`, `CALL_MULTI`, `TRADE`, `TRANSFER_FUNGIBLE`, `TRANSFER_FUNGIBLE_GAS_PAYER`, `TRANSFER_NON_FUNGIBLE_SINGLE`, `TRANSFER_NON_FUNGIBLE_SINGLE_GAS_PAYER`, `TRANSFER_NON_FUNGIBLE_MULTI`, `TRANSFER_NON_FUNGIBLE_MULTI_GAS_PAYER`, `MINT_FUNGIBLE`, `BURN_FUNGIBLE`, `BURN_FUNGIBLE_GAS_PAYER`, `MINT_NON_FUNGIBLE`, `BURN_NON_FUNGIBLE`, `BURN_NON_FUNGIBLE_GAS_PAYER`, `PHANTASMA`, `PHANTASMA_RAW`. |
| `ModuleID` | `GOVERNANCE`, `TOKEN`, `PHANTASMA`, `PHANTASMA_VM`, `ORG`, `MARKET`, `INTERNAL`. `PHANTASMA_VM` is the same numeric id as `PHANTASMA`. |
| `TokenContractMethod` | Token module method ids, including create-token, series, mint, burn, metadata, balance, supply, and Phantasma NFT methods. |
| `TokenFlags` | `NONE`, `BIG_FUNGIBLE`, `NON_FUNGIBLE`. |
| `TokensConfigFlags` | `NONE`, `REQUIRE_METADATA`, `REQUIRE_SYMBOL`, `REQUIRE_NFT_META_ID`, `REQUIRE_NFT_STANDARD`, `ALLOW_EXPLICIT_NFT_META_ID_MINT`. |
| `ListingType` | `FIXED_PRICE`. |
| `MarketContractMethod` | Market module method ids for sell, cancel, buy, and listing queries. |
| `MarketConfigFlags` | `NONE`, `PRICE_REQUIRED`, `ENFORCE_ROYALTIES`, `CAN_CANCEL_EARLY`, `CAN_PURCHASE_LATE`. |
| `VMStructFlags` | `NONE`, `DYNAMIC_EXTRAS`, `IS_SORTED`. |
| `VMType` | Carbon dynamic metadata types: scalar types, fixed bytes, strings, struct, dynamic, and array variants. This is not `phantasma_py.vm.VMType`; the package root exports this Carbon enum as `CarbonVMType` to avoid that name collision. |

Market constants:

| Constant | Meaning |
| -------- | ------- |
| `MARKET_MINIMUM_LISTING_TIME_MS` | Minimum listing time in milliseconds. |
| `MARKET_MAXIMUM_LISTING_TIME_MS` | Maximum listing time in milliseconds. |
| `MARKET_DELISTING_GRACE_MS` | Delisting grace period in milliseconds. |
| `MARKET_ROYALTY_ONE_PERCENT` | Carbon royalty unit for one percent. |
| `MARKET_ROYALTY_HUNDRED_PERCENT` | Carbon royalty unit for one hundred percent. |

## Schema And Metadata APIs

`TokenSchemas` separates metadata into `series_metadata`, `rom`, and `ram`.
Series metadata belongs to the token series, ROM is immutable NFT data, and RAM
is mutable NFT data when the chain allows updates.

| API | Purpose | Inputs | Returns and failures |
| --- | ------- | ------ | -------------------- |
| `VMVariableSchema` | Describes one Carbon dynamic field type and optional nested struct schema. | Fields: `type`, `struct_def`. | Serialized as one VM type byte plus nested struct definition for `STRUCT` and `ARRAY_STRUCT`. |
| `VMStructSchema` | Describes a Carbon dynamic struct. | Fields: `fields`, `flags`. | Serialized as field count, named field schemas, and `VMStructFlags`. |
| `VMStructArray` | Carries an array schema with dynamic struct values. | Fields: `schema`, `structs`. | Used by `ARRAY_STRUCT` metadata values. |
| `VMNamedVariableSchema.make(name, vm_type, struct_def=None)` | Builds a named schema field. | `name`: string. `vm_type`: `VMType`. `struct_def`: required for struct fields. | Returns `VMNamedVariableSchema`. Fails through `SmallString` if the name is longer than 255 UTF-8 bytes. |
| `VMDynamicVariable.write_static(vm_type, schema, writer)` | Writes the variable data using a schema-selected Carbon VM type. | `vm_type`: target Carbon `VMType`; `schema`: optional struct schema; `writer`: `CarbonWriter`. | Returns `bool`. Fails for unsupported VM types, invalid integer ranges, fixed-byte length errors, invalid nested metadata, or string/array serialization errors. |
| `VMDynamicVariable.read_static(vm_type, schema, reader)` | Reads data for a schema-selected Carbon VM type into the object. | `vm_type`, optional schema, `CarbonReader`. | Mutates `data`. Fails for unsupported VM types or reader errors. |
| `VMNamedDynamicVariable.make(name, vm_type, value)` | Builds a named dynamic metadata field. | `name`, `vm_type`, Python value. | Returns `VMNamedDynamicVariable`. The value is validated when written with a schema. |
| `VMDynamicStruct.get(name)` | Looks up a dynamic field by exact name. | `name`: case-sensitive string. | Returns `VMDynamicVariable` or `None`. |
| `VMDynamicStruct.write_carbon(writer)` | Writes a self-describing dynamic struct. | `writer`: `CarbonWriter`. | Sorts fields by name before writing. |
| `VMDynamicStruct.read_carbon(reader)` | Reads a self-describing dynamic struct. | `reader`: `CarbonReader`. | Returns `VMDynamicStruct` sorted by field name. |
| `VMDynamicStruct.write_with_schema(schema, writer)` | Writes fields in schema order, with optional dynamic extras. | `schema`: `VMStructSchema` or `None`. | Returns `bool`. Missing declared fields use default values; extra fields are written only when `DYNAMIC_EXTRAS` is set. |
| `VMDynamicStruct.read_with_schema(schema, reader)` | Reads fields according to a schema. | `schema`: `VMStructSchema` or `None`. | Returns `VMDynamicStruct`. Reads dynamic extras when the schema flag is set. |
| `prepare_standard_token_schemas(shared_metadata=False)` | Builds the standard NFT schemas. | `shared_metadata`: when `True`, standard display metadata fields live in series metadata; otherwise they live in ROM. | Returns `TokenSchemas`. RAM is created with `DYNAMIC_EXTRAS`. |
| `serialize_token_schemas(schemas)` | Serializes `TokenSchemas`. | `schemas`: `TokenSchemas`. | Returns `bytes`. |
| `serialize_token_schemas_hex(schemas)` | Serializes token schemas as uppercase hex. | `schemas`: `TokenSchemas`. | Returns `str`. |
| `build_and_serialize_token_schemas(schemas=None)` | Serializes explicit schemas or the standard schemas. | `schemas`: optional `TokenSchemas`. | Returns `bytes`. Default is `prepare_standard_token_schemas(False)`. |
| `parse_token_schemas_json(data)` | Parses public token schema JSON. | `data`: JSON object string with `seriesMetadata`, `rom`, and `ram` arrays. | Returns `TokenSchemasJSON`. Fails if the JSON is not an object, a section is not an array, or any field lacks string `name` and string `type`. |
| `token_schemas_from_json(data)` | Parses JSON and builds SDK schema objects. | `data`: schema JSON string. | Returns `TokenSchemas`. Propagates JSON, VM type, and required-field errors. |
| `build_token_schemas_from_fields(series_metadata, rom, ram)` | Builds token schemas from field declarations. | Each sequence may contain `TokenSchemaField`, `(name, type)` tuples, or mappings with `name` and `type`. | Returns `TokenSchemas`. Standard series and NFT fields are prepended. RAM uses `DYNAMIC_EXTRAS` only when no explicit RAM fields are provided. |
| `vm_type_from_string(value)` | Converts public schema type text to `VMType`. | Canonical names such as `String`, `Int256`, `Array_String`, and compact aliases such as `ArrayString`. | Returns `VMType`. Fails with `BuilderError` for unknown names. |
| `vm_type_name(vm_type)` | Converts `VMType` to canonical schema text. | `vm_type`: Carbon `VMType`. | Returns `str`. Fails for unknown enum values. |
| `verify_token_schemas(schemas)` | Checks that standard required metadata fields exist with exact case and expected type. | `schemas`: `TokenSchemas`. | Returns `None`. Fails for missing fields, case-only mismatches, or type mismatches. |

Standard display metadata fields are `name`, `description`, `imageURL`,
`infoURL`, and `royalties`. Standard series fields are `_i`, `mode`, and `rom`.
Standard NFT ROM fields are `_i` and `rom`.

## Token Metadata And Lifecycle Structures

| API | Purpose | Inputs | Returns and failures |
| --- | ------- | ------ | -------------------- |
| `build_token_metadata(fields)` | Serializes token metadata as a dynamic struct. | `fields`: dict of string keys and values. Required keys are `name`, `icon`, `url`, and `description`. | Returns `bytes`. Fails if required keys are absent or blank, if `icon` is not a `data:image/png`, `data:image/jpeg`, or `data:image/webp` URI, if icon payload is empty, or if base64 is invalid. |
| `build_token_info(symbol, max_supply, is_nft, decimals, owner, metadata, token_schemas=b"")` | Builds `TokenInfo` for create-token messages. | `symbol`: uppercase ASCII token symbol. `max_supply`: `IntX`. `is_nft`: controls token flags. `decimals`: serialized as one byte later. `owner`: `Bytes32`. `metadata`: bytes. `token_schemas`: required for NFTs. | Returns `TokenInfo`. Fails for invalid symbol, `metadata is None`, NFT max supply outside signed 64-bit range, or missing NFT schemas. For fungible tokens with max supply outside signed 64-bit range, sets `BIG_FUNGIBLE`. |
| `build_series_info(phantasma_series_id, max_mint, max_supply, owner)` | Builds standard `SeriesInfo`. | `phantasma_series_id`: required int. `max_mint`, `max_supply`, `owner`. | Returns `SeriesInfo` with standard series metadata and default empty ROM/RAM schemas. |
| `build_token_series_metadata(schema, phantasma_series_id, metadata)` | Serializes series metadata. | `schema`: series metadata schema. `metadata`: list of `(name, value)` pairs. | Returns `bytes`. Writes `_i`, `mode`, `rom`, and declared custom fields. Fails for non-int series id, missing mandatory custom fields, incorrect field case, or type coercion errors. |
| `build_nft_rom(schema, phantasma_nft_id, metadata)` | Serializes standard NFT ROM. | `schema`: ROM schema. `phantasma_nft_id`: required int. `metadata`: list of pairs. | Returns `bytes`. Writes `_i`, `rom`, and declared custom fields. Fails for missing or invalid custom fields. |
| `build_phantasma_nft_public_mint_schema(nft_rom_schema)` | Removes chain-owned Phantasma NFT fields from a public mint schema. | `nft_rom_schema`: ROM schema. | Returns `VMStructSchema` without `_i` and `rom`. |
| `build_phantasma_nft_rom(nft_rom_schema, metadata)` | Serializes public Phantasma NFT ROM input. | `metadata`: list of public field pairs. | Returns `bytes`. Fails if metadata is empty, contains reserved `_i` or `rom`, omits declared fields, has incorrect case, or cannot be coerced to the schema type. |
| `check_token_symbol(symbol)` | Validates token symbol syntax. | `symbol`: string. | Returns `None`. Fails if empty, longer than 255 UTF-8 bytes, or not only uppercase ASCII letters `A-Z`. |

## Serializable Carbon Structures

The structures below are the exact payloads used by Carbon modules. They all
implement `write_carbon(writer)` and `read_carbon(reader)` unless they are only
public data containers. Use `serialize(...)` and `deserialize(...)` for complete
object round trips.

| Structure | Fields |
| --------- | ------ |
| `ChainConfig` | `version`, `reserved1`, `reserved2`, `reserved3`, `allowed_tx_types`, `expiry_window`, `block_rate_target`. |
| `GasConfig` | `version`, `max_name_length`, `max_token_symbol_length`, `fee_shift`, `max_structure_size`, `fee_multiplier`, `gas_token_id`, `data_token_id`, `minimum_gas_offer`, `data_escrow_per_row`, `gas_fee_transfer`, `gas_fee_query`, `gas_fee_create_token_base`, `gas_fee_create_token_symbol`, `gas_fee_create_token_series`, `gas_fee_per_byte`, `gas_fee_register_name`, `gas_burn_ratio_mul`, `gas_burn_ratio_shift`. |
| `TokensConfig` | `flags`. |
| `TokenInfo` | `max_supply`, `flags`, `decimals`, `owner`, `symbol`, `metadata`, `token_schemas`. `token_schemas` is serialized only for `NON_FUNGIBLE`. |
| `SeriesInfo` | `max_mint`, `max_supply`, `owner`, `metadata`, `rom`, `ram`. |
| `NFTMintInfo` | `series_id`, `rom`, `ram`. |
| `PhantasmaNFTMintInfo` | `phantasma_series_id`, `rom`, `ram`. |
| `PhantasmaNFTMintResult` | `phantasma_nft_id`, `carbon_instance_id`. |
| `MintFungibleArgs` | `token_id`, `to`, `amount`. |
| `TransferFungibleArgs` | `to`, `from_address`, `token_id`, `amount`. |
| `TransferNonFungibleArgs` | `to`, `from_address`, `token_id`, `instance_ids`. |
| `BurnFungibleArgs` | `token_id`, `from_address`, `amount`. |
| `BurnNonFungibleArgs` | `token_id`, `from_address`, `instance_ids`. |
| `CreateTokenSeriesArgs` | `token_id`, `info`. |
| `CreateMintedTokenSeriesArgs` | `token_id`, `info`, `address`, `roms`, `rams`. |
| `MintNonFungibleArgs` | `token_id`, `address`, `tokens`. |
| `MintPhantasmaNonFungibleArgs` | `token_id`, `address`, `tokens`. |
| `UpdateTokenMetadataArgs` | `token_id`, `metadata`. |
| `UpdateSeriesMetadataArgs` | `token_id`, `series_id`, `metadata`. |
| `TokenListing` | `type`, `seller`, `quote_token_id`, `price`, `start_date`, `end_date`. |
| `MarketConfig` | `minimum_listing_time`, `maximum_listing_time`, `delisting_grace`, `flags`. |
| `MarketSellTokenArgs` | `from_address`, `token_id`, `instance_id`, `quote_token_id`, `price`, `end_date`. |
| `MarketSellTokenByIDArgs` | `from_address`, `symbol`, `instance_id`, `quote_symbol`, `price`, `end_date`. |
| `MarketCancelSaleArgs` | `token_id`, `instance_id`. |
| `MarketCancelSaleByIDArgs` | `symbol`, `instance_id`. |
| `MarketBuyTokenArgs` | `from_address`, `token_id`, `instance_id`. |
| `MarketBuyTokenByIDArgs` | `from_address`, `symbol`, `instance_id`. |
| `MarketGetTokenListingCountArgs` | `token_id`. |
| `MarketGetTokenListingInfoArgs` | `token_id`, `instance_id`. |
| `MarketGetTokenListingInfoByIDArgs` | `symbol`, `instance_id`. |

`default_market_config()` returns `MarketConfig()` using the market constants and
the default flags `PRICE_REQUIRED | ENFORCE_ROYALTIES`.

## Transaction Messages And Signing

| API | Purpose | Inputs | Returns and failures |
| --- | ------- | ------ | -------------------- |
| `TxMsg.write_carbon(writer)` | Writes an unsigned Carbon transaction envelope. | Fields: `type`, `expiry`, `max_gas`, `max_data`, `gas_from`, `payload`, `msg`. | Fails if any field or payload writer fails. |
| `TxMsg.read_carbon(reader)` | Reads an unsigned Carbon transaction envelope. | `reader`: `CarbonReader`. | Returns `TxMsg`. Fails for unsupported transaction type or payload parse errors. |
| `TxPayload` | Union of all supported `TxMsg*` payload structures. | Determined by `TxType`. | Payload structures provide `write_carbon` and `read_carbon`. |
| `Witness` | Signature witness entry. | Fields: `address`, `signature`. | Serialized as `Bytes32` address followed by `Bytes64` signature. |
| `TxMsgCall.write_carbon(writer)` | Writes a module call payload. | `module_id`, `method_id`, and either raw `args` or non-empty `sections`. | Writes raw args when no sections exist; writes sections when `sections.has_sections` is true. |
| `MsgCallArgSections.has_sections` | Checks whether call sections exist. | None. | Returns `bool`. |
| `MsgCallArgSections.write_carbon(writer)` | Writes negative section count and sections. | `sections`: non-empty list. | Fails with `SerializationError` if the list is empty. |
| `MsgCallArgSections.read_with_count(reader, count_negative)` | Reads call sections after a negative count was already read. | `count_negative`: must be negative. | Returns `MsgCallArgSections`. Fails if count is not negative. |
| `SignedTxMsg.write_carbon(writer)` | Writes a signed Carbon message using the witness layout required by `TxType`. | `msg` and `witnesses`. | Fails for witness count/address mismatches, witnesses on `PHANTASMA_RAW`, unsupported transaction type, or nested writer errors. |
| `SignedTxMsg.read_carbon(reader)` | Reads a signed Carbon message and reconstructs witness records according to `TxType`. | `reader`: `CarbonReader`. | Returns `SignedTxMsg`. For gas-payer transactions, the second witness address comes from the payload's `from_address`; other non-gas payer direct transactions use `gas_from`. |
| `sign_tx_msg(msg, keys)` | Signs the serialized unsigned `TxMsg`. | `msg`: `TxMsg`. `keys`: `PhantasmaKeys`. | Returns `SignedTxMsg` with one witness. Fails with `CryptoError` if `keys` is not a `PhantasmaKeys` instance or public key conversion fails. |
| `sign_and_serialize_tx_msg(msg, keys)` | Signs and serializes a Carbon message. | Same as `sign_tx_msg`. | Returns signed bytes. |
| `sign_and_serialize_tx_msg_hex(msg, keys)` | Signs, serializes, and hex-encodes. | Same as `sign_tx_msg`. | Returns lowercase hex string. |

Call and transaction payload structures:

| Structure | Fields |
| --------- | ------ |
| `TxMsgCall` | `module_id`, `method_id`, `args`, `sections`. |
| `CallArgSection` | `register_offset`, `args`. |
| `MsgCallArgSections` | `sections`. |
| `TxMsgCallMulti` | `calls`. |
| `TxMsgSpecialResolution` | `resolution_id`, `calls`. |
| `TxMsgTransferFungible` | `to`, `token_id`, `amount`. |
| `TxMsgTransferFungibleGasPayer` | `to`, `from_address`, `token_id`, `amount`. |
| `TxMsgTransferNonFungibleSingle` | `to`, `token_id`, `instance_id`. |
| `TxMsgTransferNonFungibleSingleGasPayer` | `to`, `from_address`, `token_id`, `instance_id`. |
| `TxMsgTransferNonFungibleMulti` | `to`, `token_id`, `instance_ids`. |
| `TxMsgTransferNonFungibleMultiGasPayer` | `to`, `from_address`, `token_id`, `instance_ids`. |
| `TxMsgMintFungible` | `token_id`, `to`, `amount`. |
| `TxMsgBurnFungible` | `token_id`, `amount`. |
| `TxMsgBurnFungibleGasPayer` | `token_id`, `from_address`, `amount`. |
| `TxMsgMintNonFungible` | `token_id`, `to`, `series_id`, `rom`, `ram`. |
| `TxMsgBurnNonFungible` | `token_id`, `instance_id`. |
| `TxMsgBurnNonFungibleGasPayer` | `token_id`, `from_address`, `instance_id`. |
| `TxMsgTrade` | `transfer_f`, `transfer_n`, `mint_f`, `burn_f`, `mint_n`, `burn_n`. |
| `TxMsgPhantasma` | `nexus`, `chain`, `script`. |
| `TxMsgPhantasmaRaw` | `transaction`. |

## Fees

| Type or method | Purpose | Defaults and formula |
| -------------- | ------- | -------------------- |
| `FeeOptions` | Base fee policy for mint operations. | Defaults: `gas_fee_base = 10_000`, `fee_multiplier = 1_000`. `calculate_max_gas()` returns `gas_fee_base * fee_multiplier`. |
| `CreateTokenFeeOptions` | Fee policy for create-token messages. | Defaults: `gas_fee_base = 10_000`, `fee_multiplier = 10_000`, `gas_fee_create_token_base = 10_000_000_000`, `gas_fee_create_token_symbol = 10_000_000_000`. |
| `CreateTokenFeeOptions.calculate_max_gas_for_symbol(symbol)` | Calculates create-token gas from symbol length. | `shift = max(len(symbol.value.encode("utf-8")) - 1, 0)`. Symbol fee is `gas_fee_create_token_symbol >> shift` when `shift < 64`, otherwise zero. Final value is `(gas_fee_base + gas_fee_create_token_base + symbol_part) * fee_multiplier`. |
| `CreateSeriesFeeOptions` | Fee policy for create-series messages. | Defaults: `gas_fee_base = 10_000`, `fee_multiplier = 10_000`, `gas_fee_create_series_base = 2_500_000_000`. `calculate_max_gas()` returns `(gas_fee_base + gas_fee_create_series_base) * fee_multiplier`. |
| `MintNFTFeeOptions` | Mint fee policy. | Inherits `FeeOptions` unchanged. |

## Lifecycle Builders

All lifecycle builders use `expiry or now_unix_millis() + 60_000`. Pass a
non-zero `expiry` when the application must control the expiration timestamp.
All builder default `max_data` values are `100_000_000`.

| Builder | Purpose | Inputs | Returns and failures |
| ------- | ------- | ------ | -------------------- |
| `now_unix_millis()` | Current Unix time in milliseconds. | None. | Returns `int`. |
| `build_create_token_tx(token_info, creator, fees=None, max_data=100000000, expiry=0)` | Builds unsigned create-token `CALL` message. | `token_info`: `TokenInfo`. `creator`: `Bytes32` used as `gas_from`. | Returns `TxMsg` with `ModuleID.TOKEN`, `TokenContractMethod.CREATE_TOKEN`, serialized `TokenInfo`, empty `SmallString` payload, default expiry if `expiry` is zero, and create-token gas formula. Propagates serialization failures. |
| `build_create_token_tx_and_sign(...)` | Builds, signs, and serializes create-token message. | `signer`: `PhantasmaKeys`. Other args match `build_create_token_tx`. | Returns signed bytes. Derives `creator` from `signer.public_key`. |
| `build_create_token_tx_and_sign_hex(...)` | Hex form of the signed create-token message. | Same as `_and_sign`. | Returns lowercase hex string. |
| `build_create_token_series_tx(token_id, series_info, creator, fees=None, max_data=100000000, expiry=0)` | Builds unsigned create-series `CALL` message. | `token_id`: Carbon token id. `series_info`: `SeriesInfo`. `creator`: `Bytes32`. | Returns `TxMsg` with `TokenContractMethod.CREATE_TOKEN_SERIES`; args are `token_id` as `u64` followed by serialized `SeriesInfo`. |
| `build_create_token_series_tx_and_sign(...)` | Builds, signs, and serializes create-series message. | `signer`: `PhantasmaKeys`. | Returns signed bytes; derives creator from `signer.public_key`. |
| `build_create_token_series_tx_and_sign_hex(...)` | Hex form of signed create-series message. | Same as `_and_sign`. | Returns lowercase hex string. |
| `build_mint_non_fungible_tx(token_id, series_id, sender, receiver, rom, ram=b"", fees=None, max_data=100000000, expiry=0)` | Builds direct `MINT_NON_FUNGIBLE` message. | Carbon token id, Carbon series id, sender and receiver `Bytes32`, ROM bytes, optional RAM bytes. | Returns `TxMsg` with `TxType.MINT_NON_FUNGIBLE`; `sender` is `gas_from`. |
| `build_mint_non_fungible_tx_and_sign(...)` | Builds, signs, and serializes direct NFT mint message. | `signer`: `PhantasmaKeys`; receiver and metadata args match unsigned builder. | Returns signed bytes; derives sender from `signer.public_key`. |
| `build_mint_non_fungible_tx_and_sign_hex(...)` | Hex form of signed direct NFT mint message. | Same as `_and_sign`. | Returns lowercase hex string. |
| `build_mint_phantasma_non_fungible_tx(token_id, sender, receiver, tokens, fees=None, max_data=100000000, expiry=0)` | Builds `CALL` message for `MINT_PHANTASMA_NON_FUNGIBLE`. | `tokens`: sequence of `PhantasmaNFTMintInfo`. | Returns `TxMsg` with serialized `MintPhantasmaNonFungibleArgs`. |
| `build_mint_phantasma_non_fungible_tx_and_sign(...)` | Builds, signs, and serializes batch Phantasma NFT mint message. | `signer`: `PhantasmaKeys`. | Returns signed bytes; derives sender from `signer.public_key`. |
| `build_mint_phantasma_non_fungible_tx_and_sign_hex(...)` | Hex form of signed batch Phantasma NFT mint message. | Same as `_and_sign`. | Returns lowercase hex string. |
| `build_mint_phantasma_non_fungible_single_tx(token_id, phantasma_series_id, sender, receiver, public_rom, ram=b"", fees=None, max_data=100000000, expiry=0)` | Builds batch Phantasma NFT mint message for one token. | `phantasma_series_id`: required int. `public_rom`: public ROM bytes. | Returns `TxMsg`; internally wraps one `PhantasmaNFTMintInfo(IntX(phantasma_series_id), public_rom, ram)`. |
| `build_mint_phantasma_non_fungible_single_tx_and_sign(...)` | Builds, signs, and serializes one-token Phantasma NFT mint message. | `signer`: `PhantasmaKeys`. | Returns signed bytes. |
| `build_mint_phantasma_non_fungible_single_tx_and_sign_hex(...)` | Hex form of signed one-token Phantasma NFT mint message. | Same as `_and_sign`. | Returns lowercase hex string. |

## NFT Address And Result Parsers

Result parsers decode execution result hex after a transaction has finalized.
They do not broadcast, poll, or verify transaction state. The usual flow is:
broadcast signed Carbon bytes, poll `get_transaction(hash)`, require successful
state, then parse `TransactionResult.result` with the matching parser.

| API | Purpose | Inputs | Returns and failures |
| --- | ------- | ------ | -------------------- |
| `get_nft_address(carbon_token_id, instance_id)` | Builds Carbon NFT address bytes from token id and instance id. | `carbon_token_id`: u64-compatible int. `instance_id`: u64-compatible int. | Returns `Bytes32` with byte 15 set to `1`, token id in bytes 16..24 little-endian, and instance id in bytes 24..32 little-endian. |
| `unpack_nft_instance_id(instance_id)` | Splits a packed NFT instance id. | `instance_id`: int. | Returns `(low32, high32)`. |
| `parse_create_token_result(result_hex)` | Parses create-token result. | `result_hex`: hex string. | Returns Carbon token id as `int`. Fails for invalid hex, wrong byte length, or trailing bytes. |
| `parse_create_token_series_result(result_hex)` | Parses create-series result. | `result_hex`: hex string. | Returns Carbon series id as `int`. Fails for invalid hex, wrong byte length, or trailing bytes. |
| `parse_mint_non_fungible_result(carbon_token_id, result_hex)` | Parses direct NFT mint result instance ids and maps them to NFT addresses. | `carbon_token_id`: token id used for address construction. `result_hex`: Carbon result bytes as hex. | Returns `list[Bytes32]`. Fails for invalid array/result encoding. |
| `parse_mint_phantasma_non_fungible_result(result_hex)` | Parses Phantasma NFT mint results. | `result_hex`: Carbon result bytes as hex. | Returns `list[PhantasmaNFTMintResult]`, each containing `phantasma_nft_id` and `carbon_instance_id`. |

Example:

```python
from phantasma_py.carbon import (
    build_create_token_tx,
    bytes32_from_phantasma_address,
)
from phantasma_py.crypto import PhantasmaKeys

keys = PhantasmaKeys.from_wif("...")
creator = bytes32_from_phantasma_address(keys.address)

# Create token_info with build_token_info(...).
msg = build_create_token_tx(token_info, creator)
```
