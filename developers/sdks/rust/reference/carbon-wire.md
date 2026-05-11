# Rust SDK Carbon API and Wire Format

`phantasma_sdk::carbon` contains Carbon serialization primitives, typed wire
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
| Lifecycle builders | `build_create_token_tx`, `build_create_token_series_tx`, `build_mint_non_fungible_tx`, `build_mint_phantasma_non_fungible_tx`, signed, hex, and `_with_options` builder variants | Build token, series, and NFT transaction messages with SDK fee defaults, expiry defaults, schema validation, explicit option overloads, and signer-derived addresses where the signed variants provide them. |
| Typed messages | `TxMsg`, `TxPayload`, `TxMsg*`, `SignedTxMsg`, `Witness`, module argument structures | Inspect, assemble, sign, serialize, or deserialize Carbon transaction messages directly when a lifecycle builder is not the right shape. |
| Wire primitives | `CarbonReader`, `CarbonWriter`, `serialize`, `deserialize`, `VMType`, `VMValue`, `VMDynamicVariable`, `VMDynamicStruct` | Implement protocol tooling, tests, diagnostics, schema-aware metadata handling, or custom message support that does not have a lifecycle builder. |

Fallible APIs return `phantasma_sdk::Result<T>`.

## Core Serialization

| API | Purpose | Inputs | Returns and failures |
| --- | ------- | ------ | -------------------- |
| `CarbonSerializable::write_carbon(&self, writer)` | Trait method for writing a Carbon object. | `writer`: mutable `CarbonWriter`. | Returns `Result<()>`; implementors propagate field serialization failures. |
| `CarbonSerializable::read_carbon(reader)` | Trait method for reading a Carbon object. | `reader`: mutable `CarbonReader`. | Returns `Result<Self>`; implementors propagate reader and validation failures. |
| `serialize(value)` | Serializes a `CarbonSerializable` object. | `value`: borrowed serializable object. | Returns `Result<Vec<u8>>`. |
| `deserialize(data)` | Parses one complete Carbon object. | `data`: byte slice. Target type is inferred from `T`. | Returns `Result<T>`. Fails if the parser fails or if trailing bytes remain. |
| `bytes32_from_public_key(public_key)` | Converts an Ed25519 public key to Carbon `Bytes32`. | `public_key`: exactly 32 bytes. | Returns `Result<Bytes32>`. Fails with `Crypto` if the length is not 32. |
| `bytes32_from_phantasma_address(address)` | Converts a Phantasma user or system address to Carbon `Bytes32`. | `address`: `Address`. | Returns `Result<Bytes32>` from `address.data()[2..]`. Fails with `Crypto` for unsupported address kinds. |
| `bytes32_from_phantasma_address_text(text)` | Parses Phantasma address text, then converts it to Carbon `Bytes32`. | `text`: Phantasma address string. | Returns `Result<Bytes32>`. Propagates address parse and address-kind errors. |

## Fixed Byte Values And Small Values

| Type or method | Purpose | Inputs | Returns and failures |
| -------------- | ------- | ------ | -------------------- |
| `Bytes16::new(data)`, `Bytes32::new(data)`, `Bytes64::new(data)` | Wraps exact fixed byte arrays. | `[u8; 16]`, `[u8; 32]`, or `[u8; 64]`. | Returns the fixed byte value. |
| `try_from_slice(data)` | Parses fixed bytes from a slice. | `data`: exact length slice. | Returns `Result<Bytes*>`. Fails with `Serialization` if the length is wrong. |
| `from_hex(value)` | Parses fixed bytes from hex. | `value`: hex string accepted by `decode_hex`. | Returns `Result<Bytes*>`. Fails on invalid hex or wrong decoded length. |
| `as_bytes()` | Borrows the fixed byte array. | None. | Returns `&[u8; SIZE]`. |
| `Display` for fixed bytes | Renders lowercase hex. | Fixed byte value. | Returns formatted text. |
| `FromStr` for fixed bytes | Parses fixed bytes from hex text. | `&str`. | Returns `Result<Bytes*>`. |
| `SmallString::new(value)` | Carbon one-byte-length UTF-8 string. | UTF-8 string whose byte length is at most 255. | Returns `Result<SmallString>`. Fails with `Serialization` if longer than 255 bytes. |
| `SmallString::as_str()` | Borrows the stored string. | None. | Returns `&str`. |
| `From<&str>` / `From<String>` for `SmallString` | Convenience conversion for values expected to fit. | String input. | Returns `SmallString`; these conversions call `expect(...)`, so use `SmallString::new(...)` for external input that may exceed 255 bytes. |
| `IntX::new(value)` | Builds a Carbon variable-width integer. | Any value convertible to `BigInt`. | Returns `IntX`. |
| `IntX::is_8_byte_safe()` | Checks signed 64-bit range. | None. | Returns `bool`. |
| `IntX::as_bigint()` | Borrows the underlying `BigInt`. | None. | Returns `&BigInt`. |
| `IntX::write_carbon(writer)` | Writes the 8-byte IntX fast path when possible, otherwise compact Int256. | `writer`: `CarbonWriter`. | Returns `Result<()>`. Fails if the wider value is outside the accepted 256-bit Carbon word range. |
| `IntX::read_carbon(reader)` | Reads IntX from Carbon bytes. | `reader`: `CarbonReader`. | Returns `Result<IntX>`. Fails for invalid packing, truncated input, or non-standard BigInt header. |

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
| `CarbonWriter::new()` | Creates an empty writer. | None. | Returns `CarbonWriter`. |
| `write(data)` | Appends raw bytes without a length prefix. | `data`: bytes. | Mutates the writer. |
| `write1(value)` | Writes unsigned 8-bit integer. | `value`: `u8`. | Mutates the writer. |
| `write2(value)` | Writes signed little-endian 16-bit integer. | `value`: `i16`. | Mutates the writer. |
| `write4(value)` | Writes signed little-endian 32-bit integer. | `value`: `i32`. | Mutates the writer. |
| `write4u(value)` | Writes unsigned little-endian 32-bit integer. | `value`: `u32`. | Mutates the writer. |
| `write8(value)` | Writes signed little-endian 64-bit integer. | `value`: `i64`. | Mutates the writer. |
| `write8u(value)` | Writes unsigned little-endian 64-bit integer. | `value`: `u64`. | Mutates the writer. |
| `write16(value)` | Writes a `Bytes16` value. | `value`: `Bytes16`. | Mutates the writer. |
| `write32(value)` | Writes a `Bytes32` value. | `value`: `Bytes32`. | Mutates the writer. |
| `write64(value)` | Writes a `Bytes64` value. | `value`: `Bytes64`. | Mutates the writer. |
| `write_big_int(value)` | Writes compact Carbon Int256 bytes. | `value`: `BigInt`. | Returns `Result<()>`. Writes header `0` for zero. Otherwise writes the shortest little-endian slice of a 256-bit two's-complement word. Fails with `Serialization` if the value is outside the accepted word range. |
| `write_big_int_array(values)` | Writes a Carbon array of compact big integers. | `values`: slice of `BigInt`. | Returns `Result<()>`. Fails if count does not fit `u32` or any element fails. |
| `write_string_z(value)` | Writes UTF-8 string followed by zero byte. | `value`: string without zero byte. | Returns `Result<()>`. Fails if the string contains `\0`. |
| `write_string_z_array(values)` | Writes an array of zero-terminated strings. | `values`: slice of strings. | Returns `Result<()>`. Fails if count does not fit `u32` or any string contains `\0`. |
| `write_byte_array(data)` | Writes Carbon byte array. | `data`: bytes. | Returns `Result<()>`; writes a 4-byte count then raw bytes. |
| `write_byte_arrays(values)` | Writes an array of byte arrays. | `values`: slice of byte vectors. | Returns `Result<()>`. |
| `write_i8_array(values)` | Writes signed 8-bit array. | `values`: slice of `i8`. | Returns `Result<()>`. |
| `write_i16_array(values)` | Writes signed 16-bit array. | `values`: slice of `i16`. | Returns `Result<()>`. |
| `write_i32_array(values)` | Writes signed 32-bit array. | `values`: slice of `i32`. | Returns `Result<()>`. |
| `write_i64_array(values)` | Writes signed 64-bit array. | `values`: slice of `i64`. | Returns `Result<()>`. |
| `write_u64_array(values)` | Writes unsigned 64-bit array. | `values`: slice of `u64`. | Returns `Result<()>`. |
| `write_int_array(values, width, signed)` | Writes a fixed-width integer array with runtime width. | `values`: slice of `i128`. `width`: 1, 2, 4, or 8. `signed`: signed or unsigned interpretation for widths 2, 4, and 8. | Returns `Result<()>`. Fails for unsupported width, count overflow, or value outside the selected integer range. Width 1 accepts the `i8..=u8::MAX` range and writes the low byte. |
| `bytes()` | Borrows the current buffer. | None. | Returns `&[u8]`. |
| `into_bytes()` | Consumes the writer. | None. | Returns `Vec<u8>`. |

## CarbonReader

`CarbonReader` is bounds-checked. `remaining()` is a method in Rust.

| Method | Purpose | Inputs | Returns and failures |
| ------ | ------- | ------ | -------------------- |
| `CarbonReader::new(data)` | Creates a reader over bytes. | `data`: borrowed byte slice. | Returns `CarbonReader`. |
| `remaining()` | Reports unread bytes. | None. | Returns `usize`. |
| `assert_eof()` | Checks that all bytes were consumed. | None. | Returns `Result<()>`; fails with `Serialization` if bytes remain. |
| `read(count)` | Reads exact byte count. | `count`: number of bytes. | Returns `Result<Vec<u8>>`. Fails if truncated. |
| `read_array::<N>()` | Reads an exact fixed-size byte array. | Const `N`. | Returns `Result<[u8; N]>`. |
| `read_length()` | Reads signed 32-bit Carbon array length. | None. | Returns `Result<usize>`. Fails if the length is negative or greater than remaining bytes. |
| `read1()` | Reads unsigned 8-bit integer. | None. | Returns `Result<u8>`. |
| `read2()` | Reads signed little-endian 16-bit integer. | None. | Returns `Result<i16>`. |
| `read4()` | Reads signed little-endian 32-bit integer. | None. | Returns `Result<i32>`. |
| `read4u()` | Reads unsigned little-endian 32-bit integer. | None. | Returns `Result<u32>`. |
| `read8()` | Reads signed little-endian 64-bit integer. | None. | Returns `Result<i64>`. |
| `read8u()` | Reads unsigned little-endian 64-bit integer. | None. | Returns `Result<u64>`. |
| `read16()` | Reads fixed 16 bytes. | None. | Returns `Result<Bytes16>`. |
| `read32()` | Reads fixed 32 bytes. | None. | Returns `Result<Bytes32>`. |
| `read64()` | Reads fixed 64 bytes. | None. | Returns `Result<Bytes64>`. |
| `read_big_int()` | Reads compact Carbon Int256. | None. | Returns `Result<BigInt>`. Fails for truncated input, reserved header bit, length greater than 32, or non-standard sign header. |
| `read_big_int_with_header(header)` | Reads compact Int256 using an already-read header. | `header`: `u8`. | Returns `Result<BigInt>`. |
| `read_big_int_array()` | Reads an array of compact big integers. | None. | Returns `Result<Vec<BigInt>>`. |
| `read_string_z()` | Reads zero-terminated UTF-8 string. | None. | Returns `Result<String>`. Fails if no zero byte is found before EOF or UTF-8 decoding fails. |
| `read_string_z_array()` | Reads an array of zero-terminated strings. | None. | Returns `Result<Vec<String>>`. |
| `read_byte_array()` | Reads a Carbon byte array. | None. | Returns `Result<Vec<u8>>`. |
| `read_byte_arrays()` | Reads an array of byte arrays. | None. | Returns `Result<Vec<Vec<u8>>>`. |
| `read_i8_array()` | Reads signed 8-bit array. | None. | Returns `Result<Vec<i8>>`. |
| `read_i16_array()` | Reads signed 16-bit array. | None. | Returns `Result<Vec<i16>>`. |
| `read_i32_array()` | Reads signed 32-bit array. | None. | Returns `Result<Vec<i32>>`. |
| `read_i64_array()` | Reads signed 64-bit array. | None. | Returns `Result<Vec<i64>>`. |
| `read_u64_array()` | Reads unsigned 64-bit array. | None. | Returns `Result<Vec<u64>>`. |
| `read_int_array(width, signed)` | Reads a fixed-width integer array with runtime width. | `width`: 1, 2, 4, or 8. `signed`: controls interpretation. | Returns `Result<Vec<i128>>`. Fails for unsupported width or truncated input. |

## Enums And Flags

| Type | Values and helpers |
| ---- | ------------------ |
| `TxType` | `Call`, `CallMulti`, `Trade`, direct transfer/mint/burn types, gas-payer variants, `Phantasma`, and `PhantasmaRaw`. `TryFrom<u8>` fails with `Serialization` for unsupported ids. |
| `ModuleId` | `Governance`, `Token`, `Phantasma`, `Org`, `Market`, `Internal`. |
| `TokenContractMethod` | Token module method ids, including create-token, series, mint, burn, metadata, balance, supply, and Phantasma NFT methods. |
| `TokenFlags` | `NONE`, `BIG_FUNGIBLE`, `NON_FUNGIBLE`. |
| `TokensConfigFlags` | `NONE`, `REQUIRE_METADATA`, `REQUIRE_SYMBOL`, `REQUIRE_NFT_META_ID`, `REQUIRE_NFT_STANDARD`, `ALLOW_EXPLICIT_NFT_META_ID_MINT`. |
| `ListingType` | `FixedPrice`. |
| `MarketContractMethod` | Market module method ids for sell, cancel, buy, and listing queries. |
| `MarketConfigFlags` | `NONE`, `PRICE_REQUIRED`, `ENFORCE_ROYALTIES`, `CAN_CANCEL_EARLY`, `CAN_PURCHASE_LATE`. |
| `VMStructFlags` | `NONE`, `DYNAMIC_EXTRAS`, `IS_SORTED`. |
| `VMType` | Carbon dynamic metadata types: scalar types, fixed bytes, strings, struct, dynamic, and array variants. `code()` returns the serialized type byte. `TryFrom<u8>` fails with `Serialization` for unsupported type ids. |
| `VMValue` | Dynamic value enum used by schema-aware metadata builders. |

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
| `VMVariableSchema::new(vm_type)` | Builds scalar schema field. | `vm_type`: Carbon `VMType`. | Returns `VMVariableSchema` without nested struct definition. |
| `VMVariableSchema::with_struct(vm_type, struct_def)` | Builds struct or array-struct schema field. | `vm_type`, nested `VMStructSchema`. | Returns `VMVariableSchema`. |
| `VMNamedVariableSchema::new(name, vm_type)` / `make(...)` | Builds a named schema field. | `name`: `SmallString` input. `vm_type`: `VMType`. | Returns `VMNamedVariableSchema`. Conversions from too-long external strings should use `SmallString::new(...)` first. |
| `VMNamedVariableSchema::with_struct(...)` / `make_with_struct(...)` | Builds a named struct field. | Name, `VMType`, and nested schema. | Returns `VMNamedVariableSchema`. |
| `VMStructSchema::new(fields)` | Builds schema with no flags. | `fields`: vector of named schema fields. | Returns `VMStructSchema`. |
| `VMStructSchema::with_flags(fields, flags)` | Builds schema with explicit flags. | `fields`, `VMStructFlags`. | Returns `VMStructSchema`. |
| `VMDynamicVariable::new(vm_type, data)` | Builds a typed dynamic value. | `vm_type`, `VMValue`. | Returns `VMDynamicVariable`. |
| `VMDynamicVariable::string(value)` | Convenience builder for `VMType::String`. | String. | Returns `VMDynamicVariable`. |
| `VMDynamicVariable::int32(value)` | Convenience builder for `VMType::Int32`. | `i32`. | Returns `VMDynamicVariable`. |
| `VMDynamicVariable::int64(value)` | Convenience builder for `VMType::Int64`. | `i64`. | Returns `VMDynamicVariable`. |
| `VMDynamicVariable::int256(value)` | Convenience builder for `VMType::Int256`. | `BigInt` input. | Returns `VMDynamicVariable`. |
| `VMDynamicVariable::bytes(value)` | Convenience builder for `VMType::Bytes`. | Bytes. | Returns `VMDynamicVariable`. |
| `VMDynamicVariable::write_static(vm_type, schema, writer)` | Writes this value using a schema-selected Carbon VM type. | Target `VMType`, optional struct schema, mutable writer. | Returns `Result<bool>`. If the stored `VMValue` does not match the requested type, default values are written for that target type. Fails for unsupported `VMType::Array`, invalid ranges, count overflow, fixed-byte length errors, or nested serialization errors. |
| `VMDynamicVariable::read_static(vm_type, schema, reader)` | Reads one value using a schema-selected Carbon VM type. | Target `VMType`, optional schema, reader. | Returns `Result<VMValue>`. Fails for unsupported `VMType::Array` or reader errors. |
| `VMNamedDynamicVariable::new(name, value)` | Builds a named dynamic value. | Name and `VMDynamicVariable`. | Returns `VMNamedDynamicVariable`. |
| `VMNamedDynamicVariable::make(name, vm_type, value)` | Builds a named dynamic value from raw `VMValue`. | Name, VM type, raw value. | Returns `VMNamedDynamicVariable`. |
| `VMDynamicStruct::new(fields)` | Builds and sorts a dynamic struct. | Named dynamic fields. | Returns `VMDynamicStruct`. |
| `VMDynamicStruct::sort()` | Sorts fields by name. | None. | Mutates the struct. |
| `VMDynamicStruct::get(name)` | Looks up a dynamic field by exact name. | `name`: case-sensitive string. | Returns `Option<&VMDynamicVariable>`. |
| `VMDynamicStruct::write_with_schema(schema, writer)` | Writes fields in schema order, with optional dynamic extras. | `schema`: `VMStructSchema`. | Returns `Result<bool>`. Missing declared fields use default values; extra fields are written only when `DYNAMIC_EXTRAS` is set. |
| `VMDynamicStruct::read_with_schema(schema, reader)` | Reads fields according to a schema. | `schema`: `VMStructSchema`. | Returns `Result<VMDynamicStruct>`. Reads dynamic extras when the schema flag is set. |
| `VMStructArray` | Carries an array schema with dynamic struct values. | Fields: `schema`, `structs`. | Used by `VMValue::ArrayStruct` and `VMType::ArrayStruct` metadata. |
| `TokenSchemaField::new(name, vm_type)` | Builds public schema field declaration. | Name and Carbon `VMType`. | Returns `TokenSchemaField`. |
| `TokenSchemasJson` / `TokenSchemasJSON` | Parsed public JSON token-schema shape. | Fields: `series_metadata`, `rom`, `ram`. | `TokenSchemasJSON` is a type alias for `TokenSchemasJson`. |
| `prepare_standard_token_schemas(shared_metadata)` | Builds the standard NFT schemas. | `shared_metadata`: when `true`, standard display metadata fields live in series metadata; otherwise they live in ROM. | Returns `TokenSchemas`. RAM is created with `DYNAMIC_EXTRAS`. |
| `serialize_token_schemas(schemas)` | Serializes `TokenSchemas`. | Borrowed schemas. | Returns `Result<Vec<u8>>`. |
| `serialize_token_schemas_hex(schemas)` | Serializes token schemas as uppercase hex. | Borrowed schemas. | Returns `Result<String>`. |
| `build_and_serialize_token_schemas(schemas)` | Serializes explicit schemas or the standard schemas. | `Option<&TokenSchemas>`. | Returns `Result<Vec<u8>>`. `None` uses `prepare_standard_token_schemas(false)`. |
| `parse_token_schemas_json(data)` | Parses public token schema JSON. | JSON object string with `seriesMetadata`, `rom`, and `ram` arrays. | Returns `Result<TokenSchemasJson>`. Fails if the JSON is not an object, a section is not an array, or any field lacks string `name` and string `type`. |
| `token_schemas_from_json(data)` | Parses JSON and builds SDK schema objects. | Schema JSON string. | Returns `Result<TokenSchemas>`. |
| `build_token_schemas_from_fields(series_metadata, rom, ram)` | Builds token schemas from `TokenSchemaField` slices. | Three field slices. | Returns `Result<TokenSchemas>`. Standard series and NFT fields are prepended. RAM uses `DYNAMIC_EXTRAS` only when no explicit RAM fields are provided. |
| `vm_type_from_string(value)` | Converts public schema type text to `VMType`. | Canonical names such as `String`, `Int256`, `Array_String`, and compact aliases such as `ArrayString`. | Returns `Result<VMType>`. Fails with `Builder` for unknown names. |
| `vm_type_name(vm_type)` | Converts `VMType` to canonical schema text. | Carbon `VMType`. | Returns `Result<&'static str>`. |
| `verify_token_schemas(schemas)` | Checks that standard required metadata fields exist with exact case and expected type. | `schemas`: `TokenSchemas`. | Returns `Result<()>`. Fails for missing fields, case-only mismatches, or type mismatches. |

Standard display metadata fields are `name`, `description`, `imageURL`,
`infoURL`, and `royalties`. Standard series fields are `_i`, `mode`, and `rom`.
Standard NFT ROM fields are `_i` and `rom`.

## Token Metadata And Lifecycle Structures

| API | Purpose | Inputs | Returns and failures |
| --- | ------- | ------ | -------------------- |
| `build_token_metadata(fields)` | Serializes token metadata as a dynamic struct. | Slice of `(&str, &str)`. Required keys are `name`, `icon`, `url`, and `description`. | Returns `Result<Vec<u8>>`. Fails if required keys are absent or blank, if `icon` is not a `data:image/png`, `data:image/jpeg`, or `data:image/webp` URI, if icon payload is empty, or if base64 is invalid. |
| `build_token_info(symbol, max_supply, is_nft, decimals, owner, metadata, token_schemas)` | Builds `TokenInfo` for create-token messages. | `symbol`: uppercase ASCII token symbol. `max_supply`: `IntX`. `decimals`: `u8`. `owner`: `Bytes32`. `metadata`: bytes. `token_schemas`: required for NFTs. | Returns `Result<TokenInfo>`. Fails for invalid symbol, empty metadata, NFT max supply outside signed 64-bit range, or missing NFT schemas. For fungible tokens with max supply outside signed 64-bit range, sets `BIG_FUNGIBLE`. |
| `build_series_info(phantasma_series_id, max_mint, max_supply, owner)` | Builds standard `SeriesInfo`. | Phantasma series id, max mint, max supply, owner. | Returns `Result<SeriesInfo>` with standard series metadata and default empty ROM/RAM schemas. |
| `build_token_series_metadata(schema, phantasma_series_id, metadata)` | Serializes series metadata. | `schema`: series metadata schema. `metadata`: slice of `(name, VMValue)` pairs. | Returns `Result<Vec<u8>>`. Writes `_i`, `mode`, `rom`, and declared custom fields. Fails for missing mandatory custom fields, incorrect field case, or type coercion errors. |
| `build_nft_rom(schema, phantasma_nft_id, metadata)` | Serializes standard NFT ROM. | `schema`: ROM schema. `metadata`: slice of pairs. | Returns `Result<Vec<u8>>`. Writes `_i`, `rom`, and declared custom fields. |
| `build_phantasma_nft_public_mint_schema(nft_rom_schema)` | Removes chain-owned Phantasma NFT fields from a public mint schema. | ROM schema. | Returns `VMStructSchema` without `_i` and `rom`. |
| `build_phantasma_nft_rom(nft_rom_schema, metadata)` | Serializes public Phantasma NFT ROM input. | `metadata`: slice of public field pairs. | Returns `Result<Vec<u8>>`. Fails if metadata is empty, contains reserved `_i` or `rom`, omits declared fields, has incorrect case, or cannot be coerced to the schema type. |
| `check_token_symbol(symbol)` | Validates token symbol syntax. | `symbol`: string. | Returns `Result<()>`. Fails if empty, longer than 255 UTF-8 bytes, or not only uppercase ASCII letters `A-Z`. |

## Serializable Carbon Structures

The structures below are the exact payloads used by Carbon modules. They
implement `CarbonSerializable` unless they are only public data containers. Use
`serialize(...)` and `deserialize(...)` for complete object round trips.

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
| `TokenListing` | `listing_type`, `seller`, `quote_token_id`, `price`, `start_date`, `end_date`. |
| `MarketConfig` | `minimum_listing_time`, `maximum_listing_time`, `delisting_grace`, `flags`. |
| `MarketSellTokenArgs` | `from_address`, `token_id`, `instance_id`, `quote_token_id`, `price`, `end_date`. |
| `MarketSellTokenByIdArgs` | `from_address`, `symbol`, `instance_id`, `quote_symbol`, `price`, `end_date`. |
| `MarketCancelSaleArgs` | `token_id`, `instance_id`. |
| `MarketCancelSaleByIdArgs` | `symbol`, `instance_id`. |
| `MarketBuyTokenArgs` | `from_address`, `token_id`, `instance_id`. |
| `MarketBuyTokenByIdArgs` | `from_address`, `symbol`, `instance_id`. |
| `MarketGetTokenListingCountArgs` | `token_id`. |
| `MarketGetTokenListingInfoArgs` | `token_id`, `instance_id`. |
| `MarketGetTokenListingInfoByIdArgs` | `symbol`, `instance_id`. |

`default_market_config()` returns `MarketConfig::default()` using the market
constants and the default flags `PRICE_REQUIRED | ENFORCE_ROYALTIES`.

## Transaction Messages And Signing

| API | Purpose | Inputs | Returns and failures |
| --- | ------- | ------ | -------------------- |
| `TxPayload::write_carbon(writer)` | Writes the payload variant. | `writer`: `CarbonWriter`. | Returns `Result<()>`; dispatches to the wrapped `TxMsg*` type. |
| `TxPayload::from_type(tx_type, reader)` | Reads the payload matching a transaction type. | `tx_type`: `TxType`; `reader`: `CarbonReader`. | Returns `Result<TxPayload>`. Fails if the selected payload parser fails. |
| `TxPayload::from_address()` | Gets the second signer address for gas-payer payloads. | None. | Returns payload `from_address` for gas-payer transfer/burn variants, otherwise `EMPTY_BYTES32`. |
| `TxMsg::write_carbon(writer)` | Writes an unsigned Carbon transaction envelope. | Fields: `tx_type`, `expiry`, `max_gas`, `max_data`, `gas_from`, `payload`, `msg`. | Returns `Result<()>`. |
| `TxMsg::read_carbon(reader)` | Reads an unsigned Carbon transaction envelope. | `reader`: `CarbonReader`. | Returns `Result<TxMsg>`. Fails for unsupported transaction type or payload parse errors. |
| `Witness` | Signature witness entry. | Fields: `address`, `signature`. | Serialized as `Bytes32` address followed by `Bytes64` signature. |
| `TxMsgCall` | Token, market, or other module method call payload. | Fields: `module_id`, `method_id`, `args`, `sections`. | Writes raw args when no sections exist; writes sections when `sections.has_sections()` is true. |
| `MsgCallArgSections::has_sections()` | Checks whether call sections exist. | None. | Returns `bool`. |
| `MsgCallArgSections::read_with_count(reader, count_negative)` | Reads call sections after a negative count was already read. | `count_negative`: must be negative. | Returns `Result<MsgCallArgSections>`. Fails if count is not negative. |
| `SignedTxMsg::write_carbon(writer)` | Writes a signed Carbon message using the witness layout required by `TxType`. | `msg` and `witnesses`. | Returns `Result<()>`. Fails for witness count/address mismatches, witnesses on `PhantasmaRaw`, or nested writer errors. |
| `SignedTxMsg::read_carbon(reader)` | Reads a signed Carbon message and reconstructs witness records according to `TxType`. | `reader`: `CarbonReader`. | Returns `Result<SignedTxMsg>`. For gas-payer transactions, the second witness address comes from `TxPayload::from_address()`. |
| `sign_tx_msg(msg, keys)` | Signs the serialized unsigned `TxMsg`. | `msg`: `TxMsg`; `keys`: `PhantasmaKeys`. | Returns `Result<SignedTxMsg>` with one witness. Fails if message serialization or signer address conversion fails. |
| `sign_and_serialize_tx_msg(msg, keys)` | Signs and serializes a Carbon message. | Same as `sign_tx_msg`. | Returns `Result<Vec<u8>>`. |
| `sign_and_serialize_tx_msg_hex(msg, keys)` | Signs, serializes, and hex-encodes. | Same as `sign_tx_msg`. | Returns lowercase hex `Result<String>`. |

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
| `FeeOptions` | Base fee policy for mint operations. | `Default`: `gas_fee_base = 10_000`, `fee_multiplier = 1_000`. `calculate_max_gas()` returns `gas_fee_base * fee_multiplier`. |
| `CreateTokenFeeOptions` | Fee policy for create-token messages. | `Default`: `gas_fee_base = 10_000`, `fee_multiplier = 10_000`, `gas_fee_create_token_base = 10_000_000_000`, `gas_fee_create_token_symbol = 10_000_000_000`. |
| `CreateTokenFeeOptions::calculate_max_gas_for_symbol(symbol)` | Calculates create-token gas from symbol length. | `shift = symbol.0.len().saturating_sub(1)`. Symbol fee is `gas_fee_create_token_symbol >> shift` when `shift < 64`, otherwise zero. Final value is `(gas_fee_base + gas_fee_create_token_base + symbol_part) * fee_multiplier`. |
| `CreateSeriesFeeOptions` | Fee policy for create-series messages. | `Default`: `gas_fee_base = 10_000`, `fee_multiplier = 10_000`, `gas_fee_create_series_base = 2_500_000_000`. `calculate_max_gas()` returns `(gas_fee_base + gas_fee_create_series_base) * fee_multiplier`. |
| `MintNftFeeOptions` / `MintNFTFeeOptions` | Mint fee policy. | Type aliases of `FeeOptions`. |

## Lifecycle Builders

All lifecycle builders use `expiry == 0` as "set expiry to
`now_unix_millis() + 60_000`". Pass a non-zero `expiry` when the application must
control the expiration timestamp. Default signing overloads use `max_data =
100_000_000`.

| Builder | Purpose | Inputs | Returns and failures |
| ------- | ------- | ------ | -------------------- |
| `now_unix_millis()` | Current Unix time in milliseconds. | None. | Returns `i64`. |
| `build_create_token_tx(token_info, creator, fees, max_data, expiry)` | Builds unsigned create-token `Call` message. | `token_info`: `TokenInfo`. `creator`: `Bytes32` used as `gas_from`. `fees`: `Option<CreateTokenFeeOptions>`. | Returns `Result<TxMsg>` with `ModuleId::Token`, `TokenContractMethod::CreateToken`, serialized `TokenInfo`, empty `SmallString` payload, default expiry if `expiry` is zero, and create-token gas formula. |
| `build_create_token_tx_and_sign(token_info, signer)` | Builds, signs, and serializes create-token message with defaults. | `signer`: `PhantasmaKeys`. | Returns `Result<Vec<u8>>`. Derives creator from `signer.public_key()`, uses default fees, `max_data = 100_000_000`, and default expiry. |
| `build_create_token_tx_and_sign_with_options(token_info, signer, fees, max_data, expiry)` | Builds, signs, and serializes create-token message with explicit options. | Same as unsigned builder plus signer. | Returns `Result<Vec<u8>>`. |
| `build_create_token_tx_and_sign_hex(...)` | Hex form of signed create-token message with defaults. | Same as default `_and_sign`. | Returns lowercase `Result<String>`. |
| `build_create_token_tx_and_sign_hex_with_options(...)` | Hex form of signed create-token message with explicit options. | Same as `_with_options`. | Returns lowercase `Result<String>`. |
| `build_create_token_series_tx(token_id, series_info, creator, fees, max_data, expiry)` | Builds unsigned create-series `Call` message. | `token_id`: Carbon token id. `series_info`: `SeriesInfo`. `creator`: `Bytes32`. | Returns `Result<TxMsg>` with `TokenContractMethod::CreateTokenSeries`; args are serialized `CreateTokenSeriesArgs`. |
| `build_create_token_series_tx_and_sign(token_id, series_info, signer)` | Builds, signs, and serializes create-series message with defaults. | `signer`: `PhantasmaKeys`. | Returns `Result<Vec<u8>>`; derives creator from `signer.public_key()`. |
| `build_create_token_series_tx_and_sign_with_options(...)` | Builds, signs, and serializes create-series message with explicit options. | Token id, series info, signer, fees, max data, expiry. | Returns `Result<Vec<u8>>`. |
| `build_create_token_series_tx_and_sign_hex(...)` | Hex form of signed create-series message with defaults. | Same as default `_and_sign`. | Returns lowercase `Result<String>`. |
| `build_create_token_series_tx_and_sign_hex_with_options(...)` | Hex form of signed create-series message with explicit options. | Same as `_with_options`. | Returns lowercase `Result<String>`. |
| `build_mint_non_fungible_tx(token_id, series_id, sender, receiver, rom, ram, fees, max_data, expiry)` | Builds direct `MintNonFungible` message. | Carbon token id, Carbon series id, sender and receiver `Bytes32`, ROM bytes, RAM bytes, optional fees. | Returns `TxMsg`; `sender` is `gas_from`. |
| `build_mint_non_fungible_tx_and_sign(...)` | Builds, signs, and serializes direct NFT mint message. | `signer`: `PhantasmaKeys`; receiver and metadata args match unsigned builder. | Returns `Result<Vec<u8>>`; derives sender from `signer.public_key()`. |
| `build_mint_non_fungible_tx_and_sign_hex(...)` | Hex form of signed direct NFT mint message. | Same as `_and_sign`. | Returns lowercase `Result<String>`. |
| `build_mint_phantasma_non_fungible_tx(token_id, sender, receiver, tokens, fees, max_data, expiry)` | Builds `Call` message for `MintPhantasmaNonFungible`. | `tokens`: vector of `PhantasmaNFTMintInfo`. | Returns `Result<TxMsg>` with serialized `MintPhantasmaNonFungibleArgs`. |
| `build_mint_phantasma_non_fungible_tx_and_sign(...)` | Builds, signs, and serializes batch Phantasma NFT mint message. | `signer`: `PhantasmaKeys`. | Returns `Result<Vec<u8>>`; derives sender from `signer.public_key()`. |
| `build_mint_phantasma_non_fungible_tx_and_sign_hex(...)` | Hex form of signed batch Phantasma NFT mint message. | Same as `_and_sign`. | Returns lowercase `Result<String>`. |
| `build_mint_phantasma_non_fungible_single_tx(token_id, phantasma_series_id, sender, receiver, public_rom, ram, fees, max_data, expiry)` | Builds batch Phantasma NFT mint message for one token. | `phantasma_series_id`: `BigInt` input. `public_rom`: public ROM bytes. | Returns `Result<TxMsg>`; internally wraps one `PhantasmaNFTMintInfo { phantasma_series_id: IntX(...), rom: public_rom, ram }`. |
| `build_mint_phantasma_non_fungible_single_tx_and_sign(...)` | Builds, signs, and serializes one-token Phantasma NFT mint message. | `signer`: `PhantasmaKeys`. | Returns `Result<Vec<u8>>`. |
| `build_mint_phantasma_non_fungible_single_tx_and_sign_hex(...)` | Hex form of signed one-token Phantasma NFT mint message. | Same as `_and_sign`. | Returns lowercase `Result<String>`. |

## NFT Address And Result Parsers

Result parsers decode execution result hex after a transaction has finalized.
They do not broadcast, poll, or verify transaction state. The usual flow is:
broadcast signed Carbon bytes, poll `get_transaction(hash)`, require successful
state, then parse `TransactionResult.result` with the matching parser.

| API | Purpose | Inputs | Returns and failures |
| --- | ------- | ------ | -------------------- |
| `get_nft_address(carbon_token_id, instance_id)` | Builds Carbon NFT address bytes from token id and instance id. | `carbon_token_id`: `u64`; `instance_id`: `u64`. | Returns `Bytes32` with byte 15 set to `1`, token id in bytes 16..24 little-endian, and instance id in bytes 24..32 little-endian. |
| `unpack_nft_instance_id(instance_id)` | Splits a packed NFT instance id. | `instance_id`: `u64`. | Returns `(u32, u32)` as low 32 bits and high 32 bits. |
| `parse_create_token_result(result_hex)` | Parses create-token result. | `result_hex`: hex string. | Returns `Result<u64>`. Fails for invalid hex, wrong byte length, or trailing bytes. |
| `parse_create_token_series_result(result_hex)` | Parses create-series result. | `result_hex`: hex string. | Returns `Result<u32>`. Fails for invalid hex, wrong byte length, or trailing bytes. |
| `parse_mint_non_fungible_result(carbon_token_id, result_hex)` | Parses direct NFT mint result instance ids and maps them to NFT addresses. | `carbon_token_id`: token id used for address construction. `result_hex`: Carbon result bytes as hex. | Returns `Result<Vec<Bytes32>>`. |
| `parse_mint_phantasma_non_fungible_result(result_hex)` | Parses Phantasma NFT mint results. | `result_hex`: Carbon result bytes as hex. | Returns `Result<Vec<PhantasmaNFTMintResult>>`, each containing `phantasma_nft_id` and `carbon_instance_id`. |

Example:

```rust
use phantasma_sdk::carbon::{
    build_create_token_tx,
    bytes32_from_phantasma_address,
    TokenInfo,
    TxMsg,
};
use phantasma_sdk::{PhantasmaKeys, Result};

fn unsigned_create_token_msg(keys: &PhantasmaKeys, token_info: TokenInfo) -> Result<TxMsg> {
    let creator = bytes32_from_phantasma_address(&keys.address())?;
    build_create_token_tx(token_info, creator, None, 100_000_000, 0)
}
```
