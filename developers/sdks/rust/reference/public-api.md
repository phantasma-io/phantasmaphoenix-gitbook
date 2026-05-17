# Rust SDK Public API Inventory

This page lists public classes, methods, functions, enum values, fields, and
constants from the cited source baseline. Use it to check exact names when
working with lower-level SDK APIs.

Source baseline:

| Item | Value |
| ---- | ----- |
| Source repo | `phantasma-sdk-rs` |
| Source commit | `9b904f43cf702f9a661f7041222dd6a30a5b8979` |
| Scope | public items in `src/**/*.rs` |

## phantasma_sdk::binary

Source: `src/binary.rs`

### Declarations

```rust
pub const MAX_ARRAY_SIZE: usize = 0x0100_0000
```

```rust
pub struct BinaryReader<'a>
```

```rust
pub struct BinaryWriter
```

### Methods

```rust
impl BinaryReader<'a>: pub fn assert_eof(&self) -> Result<()>
```

```rust
impl BinaryReader<'a>: pub fn new(data: &'a [u8]) -> Self
```

```rust
impl BinaryReader<'a>: pub fn read(&mut self, count: usize) -> Result<Vec<u8>>
```

```rust
impl BinaryReader<'a>: pub fn read_array<const N: usize>(&mut self) -> Result<[u8; N]>
```

```rust
impl BinaryReader<'a>: pub fn read_big_integer(&mut self) -> Result<BigInt>
```

```rust
impl BinaryReader<'a>: pub fn read_bool(&mut self) -> Result<bool>
```

```rust
impl BinaryReader<'a>: pub fn read_i64_le(&mut self) -> Result<i64>
```

```rust
impl BinaryReader<'a>: pub fn read_string(&mut self) -> Result<String>
```

```rust
impl BinaryReader<'a>: pub fn read_u16_le(&mut self) -> Result<u16>
```

```rust
impl BinaryReader<'a>: pub fn read_u32_le(&mut self) -> Result<u32>
```

```rust
impl BinaryReader<'a>: pub fn read_u64_le(&mut self) -> Result<u64>
```

```rust
impl BinaryReader<'a>: pub fn read_u8(&mut self) -> Result<u8>
```

```rust
impl BinaryReader<'a>: pub fn read_var_bytes(&mut self, max_size: usize) -> Result<Vec<u8>>
```

```rust
impl BinaryReader<'a>: pub fn read_var_uint(&mut self) -> Result<u64>
```

```rust
impl BinaryReader<'a>: pub fn remaining(&self) -> usize
```

```rust
impl BinaryWriter: pub fn bytes(&self) -> &[u8]
```

```rust
impl BinaryWriter: pub fn into_bytes(self) -> Vec<u8>
```

```rust
impl BinaryWriter: pub fn new() -> Self
```

```rust
impl BinaryWriter: pub fn write(&mut self, data: impl AsRef<[u8]>)
```

```rust
impl BinaryWriter: pub fn write_big_integer(&mut self, value: &BigInt) -> Result<()>
```

```rust
impl BinaryWriter: pub fn write_bool(&mut self, value: bool)
```

```rust
impl BinaryWriter: pub fn write_i64_le(&mut self, value: i64)
```

```rust
impl BinaryWriter: pub fn write_string(&mut self, value: &str)
```

```rust
impl BinaryWriter: pub fn write_u16_le(&mut self, value: u16)
```

```rust
impl BinaryWriter: pub fn write_u32_le(&mut self, value: u32)
```

```rust
impl BinaryWriter: pub fn write_u64_le(&mut self, value: u64)
```

```rust
impl BinaryWriter: pub fn write_u8(&mut self, value: u8)
```

```rust
impl BinaryWriter: pub fn write_var_bytes(&mut self, data: impl AsRef<[u8]>)
```

```rust
impl BinaryWriter: pub fn write_var_uint(&mut self, value: u64)
```

```rust
pub fn big_int_to_vm_bytes(value: &BigInt) -> Result<Vec<u8>>
```

```rust
pub fn vm_bytes_to_big_int(data: &[u8]) -> BigInt
```

## phantasma_sdk::carbon

Source: `src/carbon.rs`

### Declarations

```rust
pub const EMPTY_BYTES16: Bytes16 = Bytes16([0; 16])
```

```rust
pub const EMPTY_BYTES32: Bytes32 = Bytes32([0; 32])
```

```rust
pub const EMPTY_BYTES64: Bytes64 = Bytes64([0; 64])
```

```rust
pub const MARKET_DELISTING_GRACE_MS: u64 = 1_000 * 60 * 60 * 24
```

```rust
pub const MARKET_MAXIMUM_LISTING_TIME_MS: u64 = 1_000 * 60 * 60 * 24 * 90
```

```rust
pub const MARKET_MINIMUM_LISTING_TIME_MS: u64 = 1_000
```

```rust
pub const MARKET_ROYALTY_HUNDRED_PERCENT: u64 = 100 * MARKET_ROYALTY_ONE_PERCENT
```

```rust
pub const MARKET_ROYALTY_ONE_PERCENT: u64 = 10_000_000
```

```rust
pub const STANDARD_META_ID: &str = "_i"
```

```rust
pub const SYSTEM_ADDRESS_DATA_POOL: Bytes32 = Bytes32([ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, ])
```

```rust
pub const SYSTEM_ADDRESS_GAS_POOL: Bytes32 = Bytes32([ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, ])
```

```rust
pub const SYSTEM_ADDRESS_NULL: Bytes32 = EMPTY_BYTES32
```

```rust
pub enum ListingType
```

```rust
pub enum MarketContractMethod
```

```rust
pub enum ModuleId
```

```rust
pub enum TokenContractMethod
```

```rust
pub enum TxPayload
```

```rust
pub enum TxType
```

```rust
pub enum VMType
```

```rust
pub enum VMValue
```

```rust
pub struct BurnFungibleArgs
```

```rust
pub struct BurnNonFungibleArgs
```

```rust
pub struct CallArgSection
```

```rust
pub struct CarbonReader<'a>
```

```rust
pub struct CarbonWriter
```

```rust
pub struct ChainConfig
```

```rust
pub struct CreateMintedTokenSeriesArgs
```

```rust
pub struct CreateSeriesFeeOptions
```

```rust
pub struct CreateTokenFeeOptions
```

```rust
pub struct CreateTokenSeriesArgs
```

```rust
pub struct FeeOptions
```

```rust
pub struct GasConfig
```

```rust
pub struct IntX(pub BigInt)
```

```rust
pub struct MarketBuyTokenArgs
```

```rust
pub struct MarketBuyTokenByIdArgs
```

```rust
pub struct MarketCancelSaleArgs
```

```rust
pub struct MarketCancelSaleByIdArgs
```

```rust
pub struct MarketConfig
```

```rust
pub struct MarketConfigFlags: u32
```

```rust
pub struct MarketGetTokenListingCountArgs
```

```rust
pub struct MarketGetTokenListingInfoArgs
```

```rust
pub struct MarketGetTokenListingInfoByIdArgs
```

```rust
pub struct MarketSellTokenArgs
```

```rust
pub struct MarketSellTokenByIdArgs
```

```rust
pub struct MintFungibleArgs
```

```rust
pub struct MintNonFungibleArgs
```

```rust
pub struct MintPhantasmaNonFungibleArgs
```

```rust
pub struct MsgCallArgSections
```

```rust
pub struct NFTMintInfo
```

```rust
pub struct PhantasmaNFTMintInfo
```

```rust
pub struct PhantasmaNFTMintResult
```

```rust
pub struct SeriesInfo
```

```rust
pub struct SignedTxMsg
```

```rust
pub struct SmallString(pub String)
```

```rust
pub struct TokenFlags: u8
```

```rust
pub struct TokenInfo
```

```rust
pub struct TokenListing
```

```rust
pub struct TokenSchemaField
```

```rust
pub struct TokenSchemas
```

```rust
pub struct TokenSchemasJson
```

```rust
pub struct TokensConfig
```

```rust
pub struct TokensConfigFlags: u8
```

```rust
pub struct TransferFungibleArgs
```

```rust
pub struct TransferNonFungibleArgs
```

```rust
pub struct TxMsg
```

```rust
pub struct TxMsgBurnFungible
```

```rust
pub struct TxMsgBurnFungibleGasPayer
```

```rust
pub struct TxMsgBurnNonFungible
```

```rust
pub struct TxMsgBurnNonFungibleGasPayer
```

```rust
pub struct TxMsgCall
```

```rust
pub struct TxMsgCallMulti
```

```rust
pub struct TxMsgMintFungible
```

```rust
pub struct TxMsgMintNonFungible
```

```rust
pub struct TxMsgPhantasma
```

```rust
pub struct TxMsgPhantasmaRaw
```

```rust
pub struct TxMsgSpecialResolution
```

```rust
pub struct TxMsgTrade
```

```rust
pub struct TxMsgTransferFungible
```

```rust
pub struct TxMsgTransferFungibleGasPayer
```

```rust
pub struct TxMsgTransferNonFungibleMulti
```

```rust
pub struct TxMsgTransferNonFungibleMultiGasPayer
```

```rust
pub struct TxMsgTransferNonFungibleSingle
```

```rust
pub struct TxMsgTransferNonFungibleSingleGasPayer
```

```rust
pub struct UpdateSeriesMetadataArgs
```

```rust
pub struct UpdateTokenMetadataArgs
```

```rust
pub struct VMDynamicStruct
```

```rust
pub struct VMDynamicVariable
```

```rust
pub struct VMNamedDynamicVariable
```

```rust
pub struct VMNamedVariableSchema
```

```rust
pub struct VMStructArray
```

```rust
pub struct VMStructFlags: u8
```

```rust
pub struct VMStructSchema
```

```rust
pub struct VMVariableSchema
```

```rust
pub struct Witness
```

```rust
pub trait CarbonSerializable: Sized
```

```rust
pub type MintNFTFeeOptions = FeeOptions
```

```rust
pub type MintNftFeeOptions = FeeOptions
```

```rust
pub type TokenSchemasJSON = TokenSchemasJson
```

### Fields

- `BurnFungibleArgs.pub amount: IntX`
- `BurnFungibleArgs.pub from_address: Bytes32`
- `BurnFungibleArgs.pub token_id: u64`
- `BurnNonFungibleArgs.pub from_address: Bytes32`
- `BurnNonFungibleArgs.pub instance_ids: Vec<u64>`
- `BurnNonFungibleArgs.pub token_id: u64`
- `CallArgSection.pub args: Vec<u8>`
- `CallArgSection.pub register_offset: i32`
- `ChainConfig.pub allowed_tx_types: u32`
- `ChainConfig.pub block_rate_target: u32`
- `ChainConfig.pub expiry_window: u32`
- `ChainConfig.pub reserved1: u8`
- `ChainConfig.pub reserved2: u8`
- `ChainConfig.pub reserved3: u8`
- `ChainConfig.pub version: u8`
- `CreateMintedTokenSeriesArgs.pub address: Bytes32`
- `CreateMintedTokenSeriesArgs.pub info: SeriesInfo`
- `CreateMintedTokenSeriesArgs.pub rams: Vec<Vec<u8>>`
- `CreateMintedTokenSeriesArgs.pub roms: Vec<Vec<u8>>`
- `CreateMintedTokenSeriesArgs.pub token_id: u64`
- `CreateSeriesFeeOptions.pub fee_multiplier: u64`
- `CreateSeriesFeeOptions.pub gas_fee_base: u64`
- `CreateSeriesFeeOptions.pub gas_fee_create_series_base: u64`
- `CreateTokenFeeOptions.pub fee_multiplier: u64`
- `CreateTokenFeeOptions.pub gas_fee_base: u64`
- `CreateTokenFeeOptions.pub gas_fee_create_token_base: u64`
- `CreateTokenFeeOptions.pub gas_fee_create_token_symbol: u64`
- `CreateTokenSeriesArgs.pub info: SeriesInfo`
- `CreateTokenSeriesArgs.pub token_id: u64`
- `FeeOptions.pub fee_multiplier: u64`
- `FeeOptions.pub gas_fee_base: u64`
- `GasConfig.pub data_escrow_per_row: u64`
- `GasConfig.pub data_token_id: u64`
- `GasConfig.pub fee_multiplier: u64`
- `GasConfig.pub fee_shift: u8`
- `GasConfig.pub gas_burn_ratio_mul: u64`
- `GasConfig.pub gas_burn_ratio_shift: u8`
- `GasConfig.pub gas_fee_create_token_base: u64`
- `GasConfig.pub gas_fee_create_token_series: u64`
- `GasConfig.pub gas_fee_create_token_symbol: u64`
- `GasConfig.pub gas_fee_per_byte: u64`
- `GasConfig.pub gas_fee_query: u64`
- `GasConfig.pub gas_fee_register_name: u64`
- `GasConfig.pub gas_fee_transfer: u64`
- `GasConfig.pub gas_token_id: u64`
- `GasConfig.pub max_name_length: u8`
- `GasConfig.pub max_structure_size: u32`
- `GasConfig.pub max_token_symbol_length: u8`
- `GasConfig.pub minimum_gas_offer: u64`
- `GasConfig.pub version: u8`
- `IntX.pub fn as_bigint(&self) -> &BigInt`
- `IntX.pub fn is_8_byte_safe(&self) -> bool`
- `IntX.pub fn new(value: impl Into<BigInt>) -> Self`
- `MarketBuyTokenArgs.pub from_address: Bytes32`
- `MarketBuyTokenArgs.pub instance_id: u64`
- `MarketBuyTokenArgs.pub token_id: u64`
- `MarketBuyTokenByIdArgs.pub from_address: Bytes32`
- `MarketBuyTokenByIdArgs.pub instance_id: VMDynamicVariable`
- `MarketBuyTokenByIdArgs.pub symbol: SmallString`
- `MarketCancelSaleArgs.pub instance_id: u64`
- `MarketCancelSaleArgs.pub token_id: u64`
- `MarketCancelSaleByIdArgs.pub instance_id: VMDynamicVariable`
- `MarketCancelSaleByIdArgs.pub symbol: SmallString`
- `MarketConfig.pub delisting_grace: u64`
- `MarketConfig.pub flags: MarketConfigFlags`
- `MarketConfig.pub maximum_listing_time: u64`
- `MarketConfig.pub minimum_listing_time: u64`
- `MarketGetTokenListingCountArgs.pub token_id: u64`
- `MarketGetTokenListingInfoArgs.pub instance_id: u64`
- `MarketGetTokenListingInfoArgs.pub token_id: u64`
- `MarketGetTokenListingInfoByIdArgs.pub instance_id: VMDynamicVariable`
- `MarketGetTokenListingInfoByIdArgs.pub symbol: SmallString`
- `MarketSellTokenArgs.pub end_date: i64`
- `MarketSellTokenArgs.pub from_address: Bytes32`
- `MarketSellTokenArgs.pub instance_id: u64`
- `MarketSellTokenArgs.pub price: IntX`
- `MarketSellTokenArgs.pub quote_token_id: u64`
- `MarketSellTokenArgs.pub token_id: u64`
- `MarketSellTokenByIdArgs.pub end_date: i64`
- `MarketSellTokenByIdArgs.pub from_address: Bytes32`
- `MarketSellTokenByIdArgs.pub instance_id: VMDynamicVariable`
- `MarketSellTokenByIdArgs.pub price: IntX`
- `MarketSellTokenByIdArgs.pub quote_symbol: SmallString`
- `MarketSellTokenByIdArgs.pub symbol: SmallString`
- `MintFungibleArgs.pub amount: IntX`
- `MintFungibleArgs.pub to: Bytes32`
- `MintFungibleArgs.pub token_id: u64`
- `MintNonFungibleArgs.pub address: Bytes32`
- `MintNonFungibleArgs.pub token_id: u64`
- `MintNonFungibleArgs.pub tokens: Vec<NFTMintInfo>`
- `MintPhantasmaNonFungibleArgs.pub address: Bytes32`
- `MintPhantasmaNonFungibleArgs.pub token_id: u64`
- `MintPhantasmaNonFungibleArgs.pub tokens: Vec<PhantasmaNFTMintInfo>`
- `MsgCallArgSections.pub sections: Vec<CallArgSection>`
- `NFTMintInfo.pub ram: Vec<u8>`
- `NFTMintInfo.pub rom: Vec<u8>`
- `NFTMintInfo.pub series_id: u32`
- `PhantasmaNFTMintInfo.pub phantasma_series_id: IntX`
- `PhantasmaNFTMintInfo.pub ram: Vec<u8>`
- `PhantasmaNFTMintInfo.pub rom: Vec<u8>`
- `PhantasmaNFTMintResult.pub carbon_instance_id: u64`
- `PhantasmaNFTMintResult.pub phantasma_nft_id: Bytes32`
- `SeriesInfo.pub max_mint: u32`
- `SeriesInfo.pub max_supply: u32`
- `SeriesInfo.pub metadata: Vec<u8>`
- `SeriesInfo.pub owner: Bytes32`
- `SeriesInfo.pub ram: VMStructSchema`
- `SeriesInfo.pub rom: VMStructSchema`
- `SignedTxMsg.pub msg: TxMsg`
- `SignedTxMsg.pub witnesses: Vec<Witness>`
- `SmallString.pub fn as_str(&self) -> &str`
- `SmallString.pub fn new(value: impl Into<String>) -> Result<Self>`
- `TokenInfo.pub decimals: u8`
- `TokenInfo.pub flags: TokenFlags`
- `TokenInfo.pub max_supply: IntX`
- `TokenInfo.pub metadata: Vec<u8>`
- `TokenInfo.pub owner: Bytes32`
- `TokenInfo.pub symbol: SmallString`
- `TokenInfo.pub token_schemas: Vec<u8>`
- `TokenListing.pub end_date: i64`
- `TokenListing.pub listing_type: ListingType`
- `TokenListing.pub price: IntX`
- `TokenListing.pub quote_token_id: u64`
- `TokenListing.pub seller: Bytes32`
- `TokenListing.pub start_date: i64`
- `TokenSchemaField.pub name: String`
- `TokenSchemaField.pub vm_type: VMType`
- `TokenSchemas.pub ram: VMStructSchema`
- `TokenSchemas.pub rom: VMStructSchema`
- `TokenSchemas.pub series_metadata: VMStructSchema`
- `TokenSchemasJson.pub ram: Vec<TokenSchemaField>`
- `TokenSchemasJson.pub rom: Vec<TokenSchemaField>`
- `TokenSchemasJson.pub series_metadata: Vec<TokenSchemaField>`
- `TokensConfig.pub flags: TokensConfigFlags`
- `TransferFungibleArgs.pub amount: IntX`
- `TransferFungibleArgs.pub from_address: Bytes32`
- `TransferFungibleArgs.pub to: Bytes32`
- `TransferFungibleArgs.pub token_id: u64`
- `TransferNonFungibleArgs.pub from_address: Bytes32`
- `TransferNonFungibleArgs.pub instance_ids: Vec<u64>`
- `TransferNonFungibleArgs.pub to: Bytes32`
- `TransferNonFungibleArgs.pub token_id: u64`
- `TxMsg.pub expiry: i64`
- `TxMsg.pub gas_from: Bytes32`
- `TxMsg.pub max_data: u64`
- `TxMsg.pub max_gas: u64`
- `TxMsg.pub msg: TxPayload`
- `TxMsg.pub payload: SmallString`
- `TxMsg.pub tx_type: TxType`
- `TxMsgBurnFungible.pub amount: IntX`
- `TxMsgBurnFungible.pub token_id: u64`
- `TxMsgBurnFungibleGasPayer.pub amount: IntX`
- `TxMsgBurnFungibleGasPayer.pub from_address: Bytes32`
- `TxMsgBurnFungibleGasPayer.pub token_id: u64`
- `TxMsgBurnNonFungible.pub instance_id: u64`
- `TxMsgBurnNonFungible.pub token_id: u64`
- `TxMsgBurnNonFungibleGasPayer.pub from_address: Bytes32`
- `TxMsgBurnNonFungibleGasPayer.pub instance_id: u64`
- `TxMsgBurnNonFungibleGasPayer.pub token_id: u64`
- `TxMsgCall.pub args: Vec<u8>`
- `TxMsgCall.pub method_id: u32`
- `TxMsgCall.pub module_id: u32`
- `TxMsgCall.pub sections: Option<MsgCallArgSections>`
- `TxMsgCallMulti.pub calls: Vec<TxMsgCall>`
- `TxMsgMintFungible.pub amount: IntX`
- `TxMsgMintFungible.pub to: Bytes32`
- `TxMsgMintFungible.pub token_id: u64`
- `TxMsgMintNonFungible.pub ram: Vec<u8>`
- `TxMsgMintNonFungible.pub rom: Vec<u8>`
- `TxMsgMintNonFungible.pub series_id: u32`
- `TxMsgMintNonFungible.pub to: Bytes32`
- `TxMsgMintNonFungible.pub token_id: u64`
- `TxMsgPhantasma.pub chain: SmallString`
- `TxMsgPhantasma.pub nexus: SmallString`
- `TxMsgPhantasma.pub script: Vec<u8>`
- `TxMsgPhantasmaRaw.pub transaction: Vec<u8>`
- `TxMsgSpecialResolution.pub calls: Vec<TxMsgCall>`
- `TxMsgSpecialResolution.pub resolution_id: u64`
- `TxMsgTrade.pub burn_f: Vec<TxMsgBurnFungibleGasPayer>`
- `TxMsgTrade.pub burn_n: Vec<TxMsgBurnNonFungibleGasPayer>`
- `TxMsgTrade.pub mint_f: Vec<TxMsgMintFungible>`
- `TxMsgTrade.pub mint_n: Vec<TxMsgMintNonFungible>`
- `TxMsgTrade.pub transfer_f: Vec<TxMsgTransferFungibleGasPayer>`
- `TxMsgTrade.pub transfer_n: Vec<TxMsgTransferNonFungibleSingleGasPayer>`
- `TxMsgTransferFungible.pub amount: u64`
- `TxMsgTransferFungible.pub to: Bytes32`
- `TxMsgTransferFungible.pub token_id: u64`
- `TxMsgTransferFungibleGasPayer.pub amount: u64`
- `TxMsgTransferFungibleGasPayer.pub from_address: Bytes32`
- `TxMsgTransferFungibleGasPayer.pub to: Bytes32`
- `TxMsgTransferFungibleGasPayer.pub token_id: u64`
- `TxMsgTransferNonFungibleMulti.pub instance_ids: Vec<u64>`
- `TxMsgTransferNonFungibleMulti.pub to: Bytes32`
- `TxMsgTransferNonFungibleMulti.pub token_id: u64`
- `TxMsgTransferNonFungibleMultiGasPayer.pub from_address: Bytes32`
- `TxMsgTransferNonFungibleMultiGasPayer.pub instance_ids: Vec<u64>`
- `TxMsgTransferNonFungibleMultiGasPayer.pub to: Bytes32`
- `TxMsgTransferNonFungibleMultiGasPayer.pub token_id: u64`
- `TxMsgTransferNonFungibleSingle.pub instance_id: u64`
- `TxMsgTransferNonFungibleSingle.pub to: Bytes32`
- `TxMsgTransferNonFungibleSingle.pub token_id: u64`
- `TxMsgTransferNonFungibleSingleGasPayer.pub from_address: Bytes32`
- `TxMsgTransferNonFungibleSingleGasPayer.pub instance_id: u64`
- `TxMsgTransferNonFungibleSingleGasPayer.pub to: Bytes32`
- `TxMsgTransferNonFungibleSingleGasPayer.pub token_id: u64`
- `UpdateSeriesMetadataArgs.pub metadata: Vec<u8>`
- `UpdateSeriesMetadataArgs.pub series_id: u32`
- `UpdateSeriesMetadataArgs.pub token_id: u64`
- `UpdateTokenMetadataArgs.pub metadata: VMDynamicStruct`
- `UpdateTokenMetadataArgs.pub token_id: u64`
- `VMDynamicStruct.pub fields: Vec<VMNamedDynamicVariable>`
- `VMDynamicVariable.pub data: VMValue`
- `VMDynamicVariable.pub vm_type: VMType`
- `VMNamedDynamicVariable.pub name: SmallString`
- `VMNamedDynamicVariable.pub value: VMDynamicVariable`
- `VMNamedVariableSchema.pub name: SmallString`
- `VMNamedVariableSchema.pub schema: VMVariableSchema`
- `VMStructArray.pub schema: VMStructSchema`
- `VMStructArray.pub structs: Vec<VMDynamicStruct>`
- `VMStructSchema.pub fields: Vec<VMNamedVariableSchema>`
- `VMStructSchema.pub flags: VMStructFlags`
- `VMVariableSchema.pub struct_def: Option<VMStructSchema>`
- `VMVariableSchema.pub vm_type: VMType`
- `Witness.pub address: Bytes32`
- `Witness.pub signature: Bytes64`

### Methods

```rust
impl $name: pub fn as_bytes(&self) -> &[u8; $size]
```

```rust
impl $name: pub fn from_hex(value: &str) -> Result<Self>
```

```rust
impl $name: pub fn new(data: [u8; $size]) -> Self
```

```rust
impl $name: pub fn try_from_slice(data: &[u8]) -> Result<Self>
```

```rust
impl CarbonReader<'a>: pub fn assert_eof(&self) -> Result<()>
```

```rust
impl CarbonReader<'a>: pub fn new(data: &'a [u8]) -> Self
```

```rust
impl CarbonReader<'a>: pub fn read(&mut self, count: usize) -> Result<Vec<u8>>
```

```rust
impl CarbonReader<'a>: pub fn read1(&mut self) -> Result<u8>
```

```rust
impl CarbonReader<'a>: pub fn read16(&mut self) -> Result<Bytes16>
```

```rust
impl CarbonReader<'a>: pub fn read2(&mut self) -> Result<i16>
```

```rust
impl CarbonReader<'a>: pub fn read32(&mut self) -> Result<Bytes32>
```

```rust
impl CarbonReader<'a>: pub fn read4(&mut self) -> Result<i32>
```

```rust
impl CarbonReader<'a>: pub fn read4u(&mut self) -> Result<u32>
```

```rust
impl CarbonReader<'a>: pub fn read64(&mut self) -> Result<Bytes64>
```

```rust
impl CarbonReader<'a>: pub fn read8(&mut self) -> Result<i64>
```

```rust
impl CarbonReader<'a>: pub fn read8u(&mut self) -> Result<u64>
```

```rust
impl CarbonReader<'a>: pub fn read_array<const N: usize>(&mut self) -> Result<[u8; N]>
```

```rust
impl CarbonReader<'a>: pub fn read_big_int(&mut self) -> Result<BigInt>
```

```rust
impl CarbonReader<'a>: pub fn read_big_int_array(&mut self) -> Result<Vec<BigInt>>
```

```rust
impl CarbonReader<'a>: pub fn read_big_int_with_header(&mut self, header: u8) -> Result<BigInt>
```

```rust
impl CarbonReader<'a>: pub fn read_byte_array(&mut self) -> Result<Vec<u8>>
```

```rust
impl CarbonReader<'a>: pub fn read_byte_arrays(&mut self) -> Result<Vec<Vec<u8>>>
```

```rust
impl CarbonReader<'a>: pub fn read_i16_array(&mut self) -> Result<Vec<i16>>
```

```rust
impl CarbonReader<'a>: pub fn read_i32_array(&mut self) -> Result<Vec<i32>>
```

```rust
impl CarbonReader<'a>: pub fn read_i64_array(&mut self) -> Result<Vec<i64>>
```

```rust
impl CarbonReader<'a>: pub fn read_i8_array(&mut self) -> Result<Vec<i8>>
```

```rust
impl CarbonReader<'a>: pub fn read_int_array(&mut self, width: u8, signed: bool) -> Result<Vec<i128>>
```

```rust
impl CarbonReader<'a>: pub fn read_length(&mut self) -> Result<usize>
```

```rust
impl CarbonReader<'a>: pub fn read_string_z(&mut self) -> Result<String>
```

```rust
impl CarbonReader<'a>: pub fn read_string_z_array(&mut self) -> Result<Vec<String>>
```

```rust
impl CarbonReader<'a>: pub fn read_u64_array(&mut self) -> Result<Vec<u64>>
```

```rust
impl CarbonReader<'a>: pub fn remaining(&self) -> usize
```

```rust
impl CarbonWriter: pub fn bytes(&self) -> &[u8]
```

```rust
impl CarbonWriter: pub fn into_bytes(self) -> Vec<u8>
```

```rust
impl CarbonWriter: pub fn new() -> Self
```

```rust
impl CarbonWriter: pub fn write(&mut self, data: impl AsRef<[u8]>)
```

```rust
impl CarbonWriter: pub fn write1(&mut self, value: u8)
```

```rust
impl CarbonWriter: pub fn write16(&mut self, value: Bytes16)
```

```rust
impl CarbonWriter: pub fn write2(&mut self, value: i16)
```

```rust
impl CarbonWriter: pub fn write32(&mut self, value: Bytes32)
```

```rust
impl CarbonWriter: pub fn write4(&mut self, value: i32)
```

```rust
impl CarbonWriter: pub fn write4u(&mut self, value: u32)
```

```rust
impl CarbonWriter: pub fn write64(&mut self, value: Bytes64)
```

```rust
impl CarbonWriter: pub fn write8(&mut self, value: i64)
```

```rust
impl CarbonWriter: pub fn write8u(&mut self, value: u64)
```

```rust
impl CarbonWriter: pub fn write_big_int(&mut self, value: &BigInt) -> Result<()>
```

```rust
impl CarbonWriter: pub fn write_big_int_array(&mut self, values: &[BigInt]) -> Result<()>
```

```rust
impl CarbonWriter: pub fn write_byte_array(&mut self, data: impl AsRef<[u8]>) -> Result<()>
```

```rust
impl CarbonWriter: pub fn write_byte_arrays(&mut self, values: &[Vec<u8>]) -> Result<()>
```

```rust
impl CarbonWriter: pub fn write_i16_array(&mut self, values: &[i16]) -> Result<()>
```

```rust
impl CarbonWriter: pub fn write_i32_array(&mut self, values: &[i32]) -> Result<()>
```

```rust
impl CarbonWriter: pub fn write_i64_array(&mut self, values: &[i64]) -> Result<()>
```

```rust
impl CarbonWriter: pub fn write_i8_array(&mut self, values: &[i8]) -> Result<()>
```

```rust
impl CarbonWriter: pub fn write_int_array(&mut self, values: &[i128], width: u8, signed: bool) -> Result<()>
```

```rust
impl CarbonWriter: pub fn write_string_z(&mut self, value: &str) -> Result<()>
```

```rust
impl CarbonWriter: pub fn write_string_z_array(&mut self, values: &[String]) -> Result<()>
```

```rust
impl CarbonWriter: pub fn write_u64_array(&mut self, values: &[u64]) -> Result<()>
```

```rust
impl CreateSeriesFeeOptions: pub fn calculate_max_gas(&self) -> u64
```

```rust
impl CreateTokenFeeOptions: pub fn calculate_max_gas_for_symbol(&self, symbol: &SmallString) -> u64
```

```rust
impl FeeOptions: pub fn calculate_max_gas(&self) -> u64
```

```rust
impl FeeOptions: pub fn calculate_max_gas_for_count(&self, count: u64) -> Result<u64>
```

```rust
impl MsgCallArgSections: pub fn has_sections(&self) -> bool
```

```rust
impl MsgCallArgSections: pub fn read_with_count(reader: &mut CarbonReader<'_>, count_negative: i32) -> Result<Self>
```

```rust
impl TokenSchemaField: pub fn new(name: impl Into<String>, vm_type: VMType) -> Self
```

```rust
impl TxPayload: pub fn from_address(&self) -> Bytes32
```

```rust
impl TxPayload: pub fn from_type(tx_type: TxType, reader: &mut CarbonReader<'_>) -> Result<Self>
```

```rust
impl TxPayload: pub fn write_carbon(&self, writer: &mut CarbonWriter) -> Result<()>
```

```rust
impl VMDynamicStruct: pub fn get(&self, name: &str) -> Option<&VMDynamicVariable>
```

```rust
impl VMDynamicStruct: pub fn new(fields: Vec<VMNamedDynamicVariable>) -> Self
```

```rust
impl VMDynamicStruct: pub fn read_with_schema(
```

```rust
impl VMDynamicStruct: pub fn sort(&mut self)
```

```rust
impl VMDynamicStruct: pub fn write_with_schema(
```

```rust
impl VMDynamicVariable: pub fn bytes(value: impl Into<Vec<u8>>) -> Self
```

```rust
impl VMDynamicVariable: pub fn int256(value: impl Into<BigInt>) -> Self
```

```rust
impl VMDynamicVariable: pub fn int32(value: i32) -> Self
```

```rust
impl VMDynamicVariable: pub fn int64(value: i64) -> Self
```

```rust
impl VMDynamicVariable: pub fn new(vm_type: VMType, data: VMValue) -> Self
```

```rust
impl VMDynamicVariable: pub fn read_static(
```

```rust
impl VMDynamicVariable: pub fn string(value: impl Into<String>) -> Self
```

```rust
impl VMDynamicVariable: pub fn write_static(
```

```rust
impl VMNamedDynamicVariable: pub fn make(name: impl Into<SmallString>, vm_type: VMType, value: VMValue) -> Self
```

```rust
impl VMNamedDynamicVariable: pub fn new(name: impl Into<SmallString>, value: VMDynamicVariable) -> Self
```

```rust
impl VMNamedVariableSchema: pub fn make(name: impl Into<SmallString>, vm_type: VMType) -> Self
```

```rust
impl VMNamedVariableSchema: pub fn make_with_struct(
```

```rust
impl VMNamedVariableSchema: pub fn new(name: impl Into<SmallString>, vm_type: VMType) -> Self
```

```rust
impl VMNamedVariableSchema: pub fn with_struct(
```

```rust
impl VMStructSchema: pub fn new(fields: Vec<VMNamedVariableSchema>) -> Self
```

```rust
impl VMStructSchema: pub fn with_flags(fields: Vec<VMNamedVariableSchema>, flags: VMStructFlags) -> Self
```

```rust
impl VMType: pub fn code(self) -> u8
```

```rust
impl VMVariableSchema: pub fn new(vm_type: VMType) -> Self
```

```rust
impl VMVariableSchema: pub fn with_struct(vm_type: VMType, struct_def: VMStructSchema) -> Self
```

```rust
pub fn build_and_serialize_token_schemas(schemas: Option<&TokenSchemas>) -> Result<Vec<u8>>
```

```rust
pub fn build_create_token_series_tx( token_id: u64, series_info: SeriesInfo, creator: Bytes32, fees: Option<CreateSeriesFeeOptions>, max_data: u64, expiry: i64, ) -> Result<TxMsg>
```

```rust
pub fn build_create_token_series_tx_and_sign( token_id: u64, series_info: SeriesInfo, signer: &PhantasmaKeys, ) -> Result<Vec<u8>>
```

```rust
pub fn build_create_token_series_tx_and_sign_hex( token_id: u64, series_info: SeriesInfo, signer: &PhantasmaKeys, ) -> Result<String>
```

```rust
pub fn build_create_token_series_tx_and_sign_hex_with_options( token_id: u64, series_info: SeriesInfo, signer: &PhantasmaKeys, fees: Option<CreateSeriesFeeOptions>, max_data: u64, expiry: i64, ) -> Result<String>
```

```rust
pub fn build_create_token_series_tx_and_sign_with_options( token_id: u64, series_info: SeriesInfo, signer: &PhantasmaKeys, fees: Option<CreateSeriesFeeOptions>, max_data: u64, expiry: i64, ) -> Result<Vec<u8>>
```

```rust
pub fn build_create_token_tx( token_info: TokenInfo, creator: Bytes32, fees: Option<CreateTokenFeeOptions>, max_data: u64, expiry: i64, ) -> Result<TxMsg>
```

```rust
pub fn build_create_token_tx_and_sign( token_info: TokenInfo, signer: &PhantasmaKeys, ) -> Result<Vec<u8>>
```

```rust
pub fn build_create_token_tx_and_sign_hex( token_info: TokenInfo, signer: &PhantasmaKeys, ) -> Result<String>
```

```rust
pub fn build_create_token_tx_and_sign_hex_with_options( token_info: TokenInfo, signer: &PhantasmaKeys, fees: Option<CreateTokenFeeOptions>, max_data: u64, expiry: i64, ) -> Result<String>
```

```rust
pub fn build_create_token_tx_and_sign_with_options( token_info: TokenInfo, signer: &PhantasmaKeys, fees: Option<CreateTokenFeeOptions>, max_data: u64, expiry: i64, ) -> Result<Vec<u8>>
```

```rust
pub fn build_mint_non_fungible_tx( token_id: u64, series_id: u32, sender: Bytes32, receiver: Bytes32, rom: Vec<u8>, ram: Vec<u8>, fees: Option<FeeOptions>, max_data: u64, expiry: i64, ) -> TxMsg
```

```rust
pub fn build_mint_non_fungible_tx_and_sign( token_id: u64, series_id: u32, signer: &PhantasmaKeys, receiver: Bytes32, rom: Vec<u8>, ram: Vec<u8>, fees: Option<FeeOptions>, max_data: u64, expiry: i64, ) -> Result<Vec<u8>>
```

```rust
pub fn build_mint_non_fungible_tx_and_sign_hex( token_id: u64, series_id: u32, signer: &PhantasmaKeys, receiver: Bytes32, rom: Vec<u8>, ram: Vec<u8>, fees: Option<FeeOptions>, max_data: u64, expiry: i64, ) -> Result<String>
```

```rust
pub fn build_mint_phantasma_non_fungible_single_tx( token_id: u64, phantasma_series_id: impl Into<BigInt>, sender: Bytes32, receiver: Bytes32, public_rom: Vec<u8>, ram: Vec<u8>, fees: Option<FeeOptions>, max_data: u64, expiry: i64, ) -> Result<TxMsg>
```

```rust
pub fn build_mint_phantasma_non_fungible_single_tx_and_sign( token_id: u64, phantasma_series_id: impl Into<BigInt>, signer: &PhantasmaKeys, receiver: Bytes32, public_rom: Vec<u8>, ram: Vec<u8>, fees: Option<FeeOptions>, max_data: u64, expiry: i64, ) -> Result<Vec<u8>>
```

```rust
pub fn build_mint_phantasma_non_fungible_single_tx_and_sign_hex( token_id: u64, phantasma_series_id: impl Into<BigInt>, signer: &PhantasmaKeys, receiver: Bytes32, public_rom: Vec<u8>, ram: Vec<u8>, fees: Option<FeeOptions>, max_data: u64, expiry: i64, ) -> Result<String>
```

```rust
pub fn build_mint_phantasma_non_fungible_tx( token_id: u64, sender: Bytes32, receiver: Bytes32, tokens: Vec<PhantasmaNFTMintInfo>, fees: Option<FeeOptions>, max_data: u64, expiry: i64, ) -> Result<TxMsg>
```

```rust
pub fn build_mint_phantasma_non_fungible_tx_and_sign( token_id: u64, signer: &PhantasmaKeys, receiver: Bytes32, tokens: Vec<PhantasmaNFTMintInfo>, fees: Option<FeeOptions>, max_data: u64, expiry: i64, ) -> Result<Vec<u8>>
```

```rust
pub fn build_mint_phantasma_non_fungible_tx_and_sign_hex( token_id: u64, signer: &PhantasmaKeys, receiver: Bytes32, tokens: Vec<PhantasmaNFTMintInfo>, fees: Option<FeeOptions>, max_data: u64, expiry: i64, ) -> Result<String>
```

```rust
pub fn build_nft_rom( schema: &VMStructSchema, phantasma_nft_id: impl Into<BigInt>, metadata: &[(&str, VMValue)], ) -> Result<Vec<u8>>
```

```rust
pub fn build_phantasma_nft_public_mint_schema(nft_rom_schema: &VMStructSchema) -> VMStructSchema
```

```rust
pub fn build_phantasma_nft_rom( nft_rom_schema: &VMStructSchema, metadata: &[(&str, VMValue)], ) -> Result<Vec<u8>>
```

```rust
pub fn build_series_info( phantasma_series_id: impl Into<BigInt>, max_mint: u32, max_supply: u32, owner: Bytes32, ) -> Result<SeriesInfo>
```

```rust
pub fn build_token_info( symbol: &str, max_supply: IntX, is_nft: bool, decimals: u8, owner: Bytes32, metadata: Vec<u8>, token_schemas: Vec<u8>, ) -> Result<TokenInfo>
```

```rust
pub fn build_token_metadata(fields: &[(&str, &str)]) -> Result<Vec<u8>>
```

```rust
pub fn build_token_schemas_from_fields( series_metadata: &[TokenSchemaField], rom: &[TokenSchemaField], ram: &[TokenSchemaField], ) -> Result<TokenSchemas>
```

```rust
pub fn build_token_series_metadata( schema: &VMStructSchema, phantasma_series_id: impl Into<BigInt>, metadata: &[(&str, VMValue)], ) -> Result<Vec<u8>>
```

```rust
pub fn bytes32_from_phantasma_address(address: &Address) -> Result<Bytes32>
```

```rust
pub fn bytes32_from_phantasma_address_text(text: &str) -> Result<Bytes32>
```

```rust
pub fn bytes32_from_public_key(public_key: &[u8]) -> Result<Bytes32>
```

```rust
pub fn check_token_symbol(symbol: &str) -> Result<()>
```

```rust
pub fn default_market_config() -> MarketConfig
```

```rust
pub fn deserialize<T: CarbonSerializable>(data: impl AsRef<[u8]>) -> Result<T>
```

```rust
pub fn get_nft_address(carbon_token_id: u64, instance_id: u64) -> Bytes32
```

```rust
pub fn now_unix_millis() -> i64
```

```rust
pub fn parse_create_token_result(result_hex: &str) -> Result<u64>
```

```rust
pub fn parse_create_token_series_result(result_hex: &str) -> Result<u32>
```

```rust
pub fn parse_mint_non_fungible_result( carbon_token_id: u64, result_hex: &str, ) -> Result<Vec<Bytes32>>
```

```rust
pub fn parse_mint_phantasma_non_fungible_result( result_hex: &str, ) -> Result<Vec<PhantasmaNFTMintResult>>
```

```rust
pub fn parse_token_schemas_json(data: &str) -> Result<TokenSchemasJson>
```

```rust
pub fn prepare_standard_token_schemas(shared_metadata: bool) -> TokenSchemas
```

```rust
pub fn serialize<T: CarbonSerializable>(value: &T) -> Result<Vec<u8>>
```

```rust
pub fn serialize_token_schemas(schemas: &TokenSchemas) -> Result<Vec<u8>>
```

```rust
pub fn serialize_token_schemas_hex(schemas: &TokenSchemas) -> Result<String>
```

```rust
pub fn sign_and_serialize_tx_msg(msg: &TxMsg, keys: &PhantasmaKeys) -> Result<Vec<u8>>
```

```rust
pub fn sign_and_serialize_tx_msg_hex(msg: &TxMsg, keys: &PhantasmaKeys) -> Result<String>
```

```rust
pub fn sign_tx_msg(msg: &TxMsg, keys: &PhantasmaKeys) -> Result<SignedTxMsg>
```

```rust
pub fn token_schemas_from_json(data: &str) -> Result<TokenSchemas>
```

```rust
pub fn unpack_nft_instance_id(instance_id: u64) -> (u32, u32)
```

```rust
pub fn verify_token_schemas(schemas: &TokenSchemas) -> Result<()>
```

```rust
pub fn vm_type_from_string(value: &str) -> Result<VMType>
```

```rust
pub fn vm_type_name(vm_type: VMType) -> Result<&'static str>
```

### Variants

- `ListingType::FixedPrice = 0`
- `MarketContractMethod::BuyToken = 4`
- `MarketContractMethod::BuyTokenById = 5`
- `MarketContractMethod::CancelSale = 2`
- `MarketContractMethod::CancelSaleById = 3`
- `MarketContractMethod::GetTokenListingCount = 6`
- `MarketContractMethod::GetTokenListingInfo = 7`
- `MarketContractMethod::GetTokenListingInfoById = 8`
- `MarketContractMethod::SellToken = 0`
- `MarketContractMethod::SellTokenById = 1`
- `ModuleId::Governance = 0`
- `ModuleId::Internal = 0xFFFF_FFFF`
- `ModuleId::Market = 4`
- `ModuleId::Org = 3`
- `ModuleId::Phantasma = 2`
- `ModuleId::Token = 1`
- `TokenContractMethod::ApplyInflation = 22`
- `TokenContractMethod::BurnFungible = 4`
- `TokenContractMethod::BurnNonFungible = 9`
- `TokenContractMethod::CreateMintedTokenSeries = 21`
- `TokenContractMethod::CreateToken = 2`
- `TokenContractMethod::CreateTokenSeries = 6`
- `TokenContractMethod::DeleteTokenSeries = 7`
- `TokenContractMethod::GetBalance = 5`
- `TokenContractMethod::GetBalances = 20`
- `TokenContractMethod::GetInstances = 10`
- `TokenContractMethod::GetNextTokenInflation = 24`
- `TokenContractMethod::GetNonFungibleInfo = 11`
- `TokenContractMethod::GetNonFungibleInfoByRomId = 12`
- `TokenContractMethod::GetSeriesInfo = 13`
- `TokenContractMethod::GetSeriesInfoByMetaId = 14`
- `TokenContractMethod::GetSeriesSupply = 18`
- `TokenContractMethod::GetTokenIdBySymbol = 19`
- `TokenContractMethod::GetTokenInfo = 15`
- `TokenContractMethod::GetTokenInfoBySymbol = 16`
- `TokenContractMethod::GetTokenSupply = 17`
- `TokenContractMethod::MintFungible = 3`
- `TokenContractMethod::MintNonFungible = 8`
- `TokenContractMethod::MintPhantasmaNonFungible = 27`
- `TokenContractMethod::SetTokensConfig = 25`
- `TokenContractMethod::TransferFungible = 0`
- `TokenContractMethod::TransferNonFungible = 1`
- `TokenContractMethod::UpdateSeriesMetadata = 26`
- `TokenContractMethod::UpdateTokenMetadata = 23`
- `TxPayload::BurnFungible(TxMsgBurnFungible)`
- `TxPayload::BurnFungibleGasPayer(TxMsgBurnFungibleGasPayer)`
- `TxPayload::BurnNonFungible(TxMsgBurnNonFungible)`
- `TxPayload::BurnNonFungibleGasPayer(TxMsgBurnNonFungibleGasPayer)`
- `TxPayload::Call(TxMsgCall)`
- `TxPayload::CallMulti(TxMsgCallMulti)`
- `TxPayload::MintFungible(TxMsgMintFungible)`
- `TxPayload::MintNonFungible(TxMsgMintNonFungible)`
- `TxPayload::Phantasma(TxMsgPhantasma)`
- `TxPayload::PhantasmaRaw(TxMsgPhantasmaRaw)`
- `TxPayload::Trade(TxMsgTrade)`
- `TxPayload::TransferFungible(TxMsgTransferFungible)`
- `TxPayload::TransferFungibleGasPayer(TxMsgTransferFungibleGasPayer)`
- `TxPayload::TransferNonFungibleMulti(TxMsgTransferNonFungibleMulti)`
- `TxPayload::TransferNonFungibleMultiGasPayer(TxMsgTransferNonFungibleMultiGasPayer)`
- `TxPayload::TransferNonFungibleSingle(TxMsgTransferNonFungibleSingle)`
- `TxPayload::TransferNonFungibleSingleGasPayer(TxMsgTransferNonFungibleSingleGasPayer)`
- `TxType::BurnFungible = 10`
- `TxType::BurnFungibleGasPayer = 11`
- `TxType::BurnNonFungible = 13`
- `TxType::BurnNonFungibleGasPayer = 14`
- `TxType::Call = 0`
- `TxType::CallMulti = 1`
- `TxType::MintFungible = 9`
- `TxType::MintNonFungible = 12`
- `TxType::Phantasma = 15`
- `TxType::PhantasmaRaw = 16`
- `TxType::Trade = 2`
- `TxType::TransferFungible = 3`
- `TxType::TransferFungibleGasPayer = 4`
- `TxType::TransferNonFungibleMulti = 7`
- `TxType::TransferNonFungibleMultiGasPayer = 8`
- `TxType::TransferNonFungibleSingle = 5`
- `TxType::TransferNonFungibleSingleGasPayer = 6`
- `VMType::Array`
- `VMType::ArrayBytes`
- `VMType::ArrayBytes16`
- `VMType::ArrayBytes32`
- `VMType::ArrayBytes64`
- `VMType::ArrayDynamic`
- `VMType::ArrayInt16`
- `VMType::ArrayInt256`
- `VMType::ArrayInt32`
- `VMType::ArrayInt64`
- `VMType::ArrayInt8`
- `VMType::ArrayString`
- `VMType::ArrayStruct`
- `VMType::Bytes`
- `VMType::Bytes16`
- `VMType::Bytes32`
- `VMType::Bytes64`
- `VMType::Dynamic`
- `VMType::Int16`
- `VMType::Int256`
- `VMType::Int32`
- `VMType::Int64`
- `VMType::Int8`
- `VMType::String`
- `VMType::Struct`
- `VMValue::ArrayBytes(Vec<Vec<u8>>)`
- `VMValue::ArrayBytes16(Vec<Bytes16>)`
- `VMValue::ArrayBytes32(Vec<Bytes32>)`
- `VMValue::ArrayBytes64(Vec<Bytes64>)`
- `VMValue::ArrayDynamic(Vec<VMDynamicVariable>)`
- `VMValue::ArrayInt16(Vec<i16>)`
- `VMValue::ArrayInt256(Vec<BigInt>)`
- `VMValue::ArrayInt32(Vec<i32>)`
- `VMValue::ArrayInt64(Vec<i64>)`
- `VMValue::ArrayInt8(Vec<i8>)`
- `VMValue::ArrayString(Vec<String>)`
- `VMValue::ArrayStruct(VMStructArray)`
- `VMValue::Bytes(Vec<u8>)`
- `VMValue::Bytes16(Bytes16)`
- `VMValue::Bytes32(Bytes32)`
- `VMValue::Bytes64(Bytes64)`
- `VMValue::Dynamic(Box<VMDynamicVariable>)`
- `VMValue::Int(i64)`
- `VMValue::Int256(BigInt)`
- `VMValue::None`
- `VMValue::String(String)`
- `VMValue::Struct(VMDynamicStruct)`

## phantasma_sdk::crypto

Source: `src/crypto.rs`

### Declarations

```rust
pub const ADDRESS_LENGTH: usize = 34
```

```rust
pub const PRIVATE_KEY_LENGTH: usize = 32
```

```rust
pub const PUBLIC_KEY_LENGTH: usize = 32
```

```rust
pub const SIGNATURE_LENGTH: usize = 64
```

```rust
pub enum AddressKind
```

```rust
pub enum SignatureKind
```

```rust
pub struct Address
```

```rust
pub struct Ed25519Signature
```

```rust
pub struct Hash(pub [u8; 32])
```

```rust
pub struct PhantasmaKeys
```

### Fields

- `Hash.pub fn difficulty(&self) -> u32`
- `Hash.pub fn new(data: [u8; 32]) -> Self`
- `Hash.pub fn sha256(data: impl AsRef<[u8]>) -> Self`
- `Hash.pub fn to_hex(&self) -> String`
- `Hash.pub fn try_from_slice(data: &[u8]) -> Result<Self>`

### Methods

```rust
impl Address: pub fn data(&self) -> &[u8; ADDRESS_LENGTH]
```

```rust
impl Address: pub fn from_hash(value: impl AsRef<[u8]>) -> Self
```

```rust
impl Address: pub fn from_public_key(public_key: &[u8]) -> Result<Self>
```

```rust
impl Address: pub fn from_text(text: impl AsRef<str>) -> Result<Self>
```

```rust
impl Address: pub fn into_bytes(self) -> [u8; ADDRESS_LENGTH]
```

```rust
impl Address: pub fn is_null(&self) -> bool
```

```rust
impl Address: pub fn kind(&self) -> AddressKind
```

```rust
impl Address: pub fn new(data: [u8; ADDRESS_LENGTH]) -> Self
```

```rust
impl Address: pub fn null() -> Self
```

```rust
impl Address: pub fn prefixed_bytes(&self) -> Vec<u8>
```

```rust
impl Address: pub fn public_key(&self) -> Result<[u8; PUBLIC_KEY_LENGTH]>
```

```rust
impl Address: pub fn to_text(&self) -> String
```

```rust
impl Address: pub fn try_from_slice(data: &[u8]) -> Result<Self>
```

```rust
impl Ed25519Signature: pub fn data(&self) -> &[u8; SIGNATURE_LENGTH]
```

```rust
impl Ed25519Signature: pub fn kind(&self) -> SignatureKind
```

```rust
impl Ed25519Signature: pub fn new(data: [u8; SIGNATURE_LENGTH]) -> Self
```

```rust
impl Ed25519Signature: pub fn serialize_data(&self) -> Vec<u8>
```

```rust
impl Ed25519Signature: pub fn try_from_slice(data: &[u8]) -> Result<Self>
```

```rust
impl Ed25519Signature: pub fn verify<'a>(
```

```rust
impl PhantasmaKeys: pub fn address(&self) -> Address
```

```rust
impl PhantasmaKeys: pub fn from_wif(wif: &str) -> Result<Self>
```

```rust
impl PhantasmaKeys: pub fn generate() -> Self
```

```rust
impl PhantasmaKeys: pub fn new(private_key: [u8; PRIVATE_KEY_LENGTH]) -> Self
```

```rust
impl PhantasmaKeys: pub fn private_key(&self) -> &[u8; PRIVATE_KEY_LENGTH]
```

```rust
impl PhantasmaKeys: pub fn public_key(&self) -> [u8; PUBLIC_KEY_LENGTH]
```

```rust
impl PhantasmaKeys: pub fn sign(&self, message: impl AsRef<[u8]>) -> Ed25519Signature
```

```rust
impl PhantasmaKeys: pub fn signing_key(&self) -> SigningKey
```

```rust
impl PhantasmaKeys: pub fn to_wif(&self) -> String
```

```rust
impl PhantasmaKeys: pub fn try_from_slice(private_key: &[u8]) -> Result<Self>
```

```rust
pub fn double_sha256(data: impl AsRef<[u8]>) -> [u8; 32]
```

### Variants

- `AddressKind::Interop = 3`
- `AddressKind::Invalid = 0`
- `AddressKind::System = 2`
- `AddressKind::User = 1`
- `SignatureKind::Ecdsa = 2`
- `SignatureKind::Ed25519 = 1`
- `SignatureKind::None = 0`
- `SignatureKind::Ring = 3`

## phantasma_sdk::encoding

Source: `src/encoding.rs`

### Methods

```rust
pub fn decode_base58(text: &str) -> Result<Vec<u8>>
```

```rust
pub fn decode_hex(value: &str) -> Result<Vec<u8>>
```

```rust
pub fn encode_base58(data: impl AsRef<[u8]>) -> String
```

```rust
pub fn encode_hex(data: impl AsRef<[u8]>) -> String
```

```rust
pub fn encode_hex_upper(data: impl AsRef<[u8]>) -> String
```

## phantasma_sdk::error

Source: `src/error.rs`

### Declarations

```rust
pub enum PhantasmaError
```

```rust
pub type Result<T> = std::result::Result<T, PhantasmaError>
```

### Variants

- `PhantasmaError::Builder(String)`
- `PhantasmaError::Crypto(String)`
- `PhantasmaError::Encoding(String)`
- `PhantasmaError::Http(String)`
- `PhantasmaError::Json(String)`
- `PhantasmaError::Rpc { code: Option<i64>, message: String }`
- `PhantasmaError::Serialization(String)`

## phantasma_sdk

Source: `src/lib.rs`

### Declarations

```rust
pub const SDK_VERSION: &str = env!("CARGO_PKG_VERSION")
```

```rust
pub mod binary
```

```rust
pub mod carbon
```

```rust
pub mod crypto
```

```rust
pub mod encoding
```

```rust
pub mod error
```

```rust
pub mod rpc
```

```rust
pub mod transaction
```

```rust
pub mod vm
```

```rust
pub use binary::
```

```rust
pub use carbon::*
```

```rust
pub use crypto::
```

```rust
pub use encoding::
```

```rust
pub use error::
```

```rust
pub use rpc::*
```

```rust
pub use transaction::
```

```rust
pub use vm::
```

## phantasma_sdk::rpc

Source: `src/rpc.rs`

### Declarations

```rust
pub struct AbiEventResult
```

```rust
pub struct AbiMethodResult
```

```rust
pub struct AbiParameterResult
```

```rust
pub struct AccountResult
```

```rust
pub struct AddressTransactionsResult
```

```rust
pub struct ArchiveResult
```

```rust
pub struct AuctionResult
```

```rust
pub struct BalanceResult
```

```rust
pub struct BlockResult
```

```rust
pub struct BuildInfoResult
```

```rust
pub struct ChainResult
```

```rust
pub struct ChannelResult
```

```rust
pub struct ContractResult
```

```rust
pub struct CrowdsaleResult
```

```rust
pub struct CursorPaginatedResult<T>
```

```rust
pub struct DappResult
```

```rust
pub struct EventResult
```

```rust
pub struct GovernanceResult
```

```rust
pub struct InteropResult
```

```rust
pub struct LeaderboardResult
```

```rust
pub struct LeaderboardRowResult
```

```rust
pub struct NexusResult
```

```rust
pub struct NftResult
```

```rust
pub struct OracleResult
```

```rust
pub struct OrganizationResult
```

```rust
pub struct PaginatedResult<T>
```

```rust
pub struct PeerResult
```

```rust
pub struct PhantasmaRpc<T = ReqwestTransport>
```

```rust
pub struct PhantasmaVmConfigResult
```

```rust
pub struct PlatformResult
```

```rust
pub struct ReceiptResult
```

```rust
pub struct ReqwestTransport
```

```rust
pub struct ScriptResult
```

```rust
pub struct SignatureResult
```

```rust
pub struct StakeResult
```

```rust
pub struct StorageResult
```

```rust
pub struct SwapResult
```

```rust
pub struct TokenDataResult
```

```rust
pub struct TokenExternalResult
```

```rust
pub struct TokenPriceResult
```

```rust
pub struct TokenPropertyResult
```

```rust
pub struct TokenResult
```

```rust
pub struct TokenSchemasResult
```

```rust
pub struct TokenSeriesResult
```

```rust
pub struct TransactionResult
```

```rust
pub struct ValidatorResult
```

```rust
pub struct VmNamedVariableSchemaResult
```

```rust
pub struct VmStructSchemaResult
```

```rust
pub struct VmVariableSchemaResult
```

```rust
pub trait RpcTransport: Send + Sync
```

```rust
pub type VersionResult = BuildInfoResult
```

### Fields

- `AbiEventResult.pub description: String`
- `AbiEventResult.pub name: String`
- `AbiEventResult.pub return_type: String`
- `AbiEventResult.pub value: u32`
- `AbiMethodResult.pub name: String`
- `AbiMethodResult.pub parameters: Vec<AbiParameterResult>`
- `AbiMethodResult.pub return_type: String`
- `AbiParameterResult.pub name: String`
- `AbiParameterResult.pub type_name: String`
- `AccountResult.pub address: String`
- `AccountResult.pub balances: Vec<BalanceResult>`
- `AccountResult.pub name: String`
- `AccountResult.pub relay: String`
- `AccountResult.pub stake: String`
- `AccountResult.pub stakes: StakeResult`
- `AccountResult.pub storage: StorageResult`
- `AccountResult.pub unclaimed: String`
- `AccountResult.pub validator: String`
- `AddressTransactionsResult.pub address: String`
- `AddressTransactionsResult.pub txs: Vec<TransactionResult>`
- `ArchiveResult.pub block_count: u64`
- `ArchiveResult.pub encryption: String`
- `ArchiveResult.pub hash: String`
- `ArchiveResult.pub missing_blocks: Vec<u64>`
- `ArchiveResult.pub name: String`
- `ArchiveResult.pub owners: Vec<String>`
- `ArchiveResult.pub size: u64`
- `ArchiveResult.pub time: u64`
- `AuctionResult.pub base_symbol: String`
- `AuctionResult.pub chain_address: String`
- `AuctionResult.pub creator_address: String`
- `AuctionResult.pub current_winner: String`
- `AuctionResult.pub end_date: u64`
- `AuctionResult.pub end_price: String`
- `AuctionResult.pub extension_period: String`
- `AuctionResult.pub listing_fee: String`
- `AuctionResult.pub price: String`
- `AuctionResult.pub quote_symbol: String`
- `AuctionResult.pub ram: String`
- `AuctionResult.pub rom: String`
- `AuctionResult.pub start_date: u64`
- `AuctionResult.pub token_id: String`
- `AuctionResult.pub type_name: String`
- `BalanceResult.pub amount: String`
- `BalanceResult.pub chain: String`
- `BalanceResult.pub decimals: u32`
- `BalanceResult.pub ids: Vec<String>`
- `BalanceResult.pub symbol: String`
- `BlockResult.pub chain_address: String`
- `BlockResult.pub events: Vec<EventResult>`
- `BlockResult.pub hash: String`
- `BlockResult.pub height: u64`
- `BlockResult.pub oracles: Vec<OracleResult>`
- `BlockResult.pub previous_hash: String`
- `BlockResult.pub protocol: u32`
- `BlockResult.pub reward: String`
- `BlockResult.pub timestamp: u64`
- `BlockResult.pub txs: Vec<TransactionResult>`
- `BlockResult.pub validator_address: String`
- `BuildInfoResult.pub build_time_utc: String`
- `BuildInfoResult.pub commit: String`
- `BuildInfoResult.pub version: String`
- `ChainResult.pub address: String`
- `ChainResult.pub contracts: Vec<String>`
- `ChainResult.pub dapps: Vec<String>`
- `ChainResult.pub height: u64`
- `ChainResult.pub name: String`
- `ChainResult.pub organization: String`
- `ChainResult.pub parent: String`
- `ChannelResult.pub active: bool`
- `ChannelResult.pub balance: String`
- `ChannelResult.pub chain: String`
- `ChannelResult.pub creation_time: u64`
- `ChannelResult.pub creator_address: String`
- `ChannelResult.pub fee: String`
- `ChannelResult.pub index: u64`
- `ChannelResult.pub name: String`
- `ChannelResult.pub symbol: String`
- `ChannelResult.pub target_address: String`
- `ContractResult.pub address: String`
- `ContractResult.pub events: Vec<AbiEventResult>`
- `ContractResult.pub methods: Vec<AbiMethodResult>`
- `ContractResult.pub name: String`
- `ContractResult.pub script: String`
- `CrowdsaleResult.pub creator: String`
- `CrowdsaleResult.pub end_date: u64`
- `CrowdsaleResult.pub flags: String`
- `CrowdsaleResult.pub global_hard_cap: String`
- `CrowdsaleResult.pub global_soft_cap: String`
- `CrowdsaleResult.pub hash: String`
- `CrowdsaleResult.pub name: String`
- `CrowdsaleResult.pub price: u64`
- `CrowdsaleResult.pub receive_symbol: String`
- `CrowdsaleResult.pub sell_symbol: String`
- `CrowdsaleResult.pub start_date: u64`
- `CrowdsaleResult.pub user_hard_cap: String`
- `CrowdsaleResult.pub user_soft_cap: String`
- `CursorPaginatedResult.pub cursor: String`
- `CursorPaginatedResult.pub result: Option<T>`
- `DappResult.pub address: String`
- `DappResult.pub chain: String`
- `DappResult.pub name: String`
- `EventResult.pub address: String`
- `EventResult.pub contract: String`
- `EventResult.pub data: String`
- `EventResult.pub kind: String`
- `GovernanceResult.pub name: String`
- `GovernanceResult.pub value: String`
- `InteropResult.pub external: String`
- `InteropResult.pub local: String`
- `LeaderboardResult.pub name: String`
- `LeaderboardResult.pub rows: Vec<LeaderboardRowResult>`
- `LeaderboardRowResult.pub address: String`
- `LeaderboardRowResult.pub value: String`
- `NexusResult.pub chains: Vec<ChainResult>`
- `NexusResult.pub governance: Vec<GovernanceResult>`
- `NexusResult.pub name: String`
- `NexusResult.pub organizations: Vec<String>`
- `NexusResult.pub platforms: Vec<PlatformResult>`
- `NexusResult.pub protocol: u32`
- `NexusResult.pub tokens: Vec<TokenResult>`
- `NftResult.pub chain_name: String`
- `NftResult.pub creator_address: String`
- `NftResult.pub id: String`
- `NftResult.pub mint: String`
- `NftResult.pub owner_address: String`
- `NftResult.pub ram: String`
- `NftResult.pub rom: String`
- `NftResult.pub series: String`
- `NftResult.pub status: String`
- `OracleResult.pub content: String`
- `OracleResult.pub url: String`
- `OrganizationResult.pub id: String`
- `OrganizationResult.pub members: Vec<String>`
- `OrganizationResult.pub name: String`
- `PaginatedResult.pub page: u32`
- `PaginatedResult.pub page_size: u32`
- `PaginatedResult.pub result: Option<T>`
- `PaginatedResult.pub total: u64`
- `PaginatedResult.pub total_pages: u32`
- `PeerResult.pub fee: String`
- `PeerResult.pub flags: String`
- `PeerResult.pub pow: u64`
- `PeerResult.pub url: String`
- `PeerResult.pub version: String`
- `PhantasmaVmConfigResult.pub feature_level: u32`
- `PhantasmaVmConfigResult.pub fuel_per_contract_deploy: String`
- `PhantasmaVmConfigResult.pub gas_account: String`
- `PhantasmaVmConfigResult.pub gas_constructor: String`
- `PhantasmaVmConfigResult.pub gas_leaderboard: String`
- `PhantasmaVmConfigResult.pub gas_nexus: String`
- `PhantasmaVmConfigResult.pub gas_oracle: String`
- `PhantasmaVmConfigResult.pub gas_organization: String`
- `PhantasmaVmConfigResult.pub gas_standard: String`
- `PhantasmaVmConfigResult.pub is_stored: bool`
- `PlatformResult.pub chain: String`
- `PlatformResult.pub fuel: String`
- `PlatformResult.pub interop: Vec<InteropResult>`
- `PlatformResult.pub platform: String`
- `PlatformResult.pub tokens: Vec<String>`
- `ReceiptResult.pub channel: String`
- `ReceiptResult.pub index: String`
- `ReceiptResult.pub nexus: String`
- `ReceiptResult.pub receiver: String`
- `ReceiptResult.pub script: String`
- `ReceiptResult.pub sender: String`
- `ReceiptResult.pub timestamp: u64`
- `ScriptResult.pub events: Vec<EventResult>`
- `ScriptResult.pub gas: String`
- `ScriptResult.pub oracles: Vec<OracleResult>`
- `ScriptResult.pub result: String`
- `ScriptResult.pub results: Vec<String>`
- `ScriptResult.pub state: String`
- `SignatureResult.pub data: String`
- `SignatureResult.pub kind: String`
- `StakeResult.pub amount: String`
- `StakeResult.pub time: u64`
- `StakeResult.pub unclaimed: String`
- `StorageResult.pub archives: Vec<ArchiveResult>`
- `StorageResult.pub available: u64`
- `StorageResult.pub avatar: String`
- `StorageResult.pub used: u64`
- `SwapResult.pub destination_address: String`
- `SwapResult.pub destination_chain: String`
- `SwapResult.pub destination_hash: String`
- `SwapResult.pub destination_platform: String`
- `SwapResult.pub source_address: String`
- `SwapResult.pub source_chain: String`
- `SwapResult.pub source_hash: String`
- `SwapResult.pub source_platform: String`
- `SwapResult.pub symbol: String`
- `SwapResult.pub value: String`
- `TokenDataResult.pub carbon_nft_address: String`
- `TokenDataResult.pub carbon_series_id: String`
- `TokenDataResult.pub carbon_token_id: String`
- `TokenDataResult.pub chain_name: String`
- `TokenDataResult.pub creator_address: String`
- `TokenDataResult.pub id: String`
- `TokenDataResult.pub infusion: Vec<TokenPropertyResult>`
- `TokenDataResult.pub mint: String`
- `TokenDataResult.pub owner_address: String`
- `TokenDataResult.pub properties: Vec<TokenPropertyResult>`
- `TokenDataResult.pub ram: String`
- `TokenDataResult.pub rom: String`
- `TokenDataResult.pub series: String`
- `TokenDataResult.pub status: String`
- `TokenExternalResult.pub hash: String`
- `TokenExternalResult.pub platform: String`
- `TokenPriceResult.pub close: String`
- `TokenPriceResult.pub high: String`
- `TokenPriceResult.pub low: String`
- `TokenPriceResult.pub open: String`
- `TokenPriceResult.pub timestamp: u64`
- `TokenPropertyResult.pub key: String`
- `TokenPropertyResult.pub value: String`
- `TokenResult.pub address: String`
- `TokenResult.pub burned_supply: String`
- `TokenResult.pub carbon_id: String`
- `TokenResult.pub current_supply: String`
- `TokenResult.pub decimals: u32`
- `TokenResult.pub external: Vec<TokenExternalResult>`
- `TokenResult.pub flags: String`
- `TokenResult.pub max_supply: String`
- `TokenResult.pub metadata: Vec<TokenPropertyResult>`
- `TokenResult.pub name: String`
- `TokenResult.pub owner: String`
- `TokenResult.pub price: Vec<TokenPriceResult>`
- `TokenResult.pub script: String`
- `TokenResult.pub series: Vec<TokenSeriesResult>`
- `TokenResult.pub symbol: String`
- `TokenResult.pub token_schemas: Option<TokenSchemasResult>`
- `TokenSchemasResult.pub ram: VmStructSchemaResult`
- `TokenSchemasResult.pub rom: VmStructSchemaResult`
- `TokenSchemasResult.pub series_metadata: VmStructSchemaResult`
- `TokenSeriesResult.pub burned_supply: String`
- `TokenSeriesResult.pub carbon_series_id: String`
- `TokenSeriesResult.pub carbon_token_id: String`
- `TokenSeriesResult.pub current_supply: String`
- `TokenSeriesResult.pub max_mint: String`
- `TokenSeriesResult.pub max_supply: String`
- `TokenSeriesResult.pub metadata: Vec<TokenPropertyResult>`
- `TokenSeriesResult.pub methods: Vec<AbiMethodResult>`
- `TokenSeriesResult.pub mint_count: String`
- `TokenSeriesResult.pub mode: String`
- `TokenSeriesResult.pub owner_address: String`
- `TokenSeriesResult.pub script: String`
- `TokenSeriesResult.pub series_id: String`
- `TransactionResult.pub block_hash: String`
- `TransactionResult.pub block_height: u64`
- `TransactionResult.pub chain_address: String`
- `TransactionResult.pub events: Vec<EventResult>`
- `TransactionResult.pub expiration: u64`
- `TransactionResult.pub fee: String`
- `TransactionResult.pub hash: String`
- `TransactionResult.pub payload: String`
- `TransactionResult.pub result: String`
- `TransactionResult.pub script: String`
- `TransactionResult.pub signatures: Vec<SignatureResult>`
- `TransactionResult.pub state: String`
- `TransactionResult.pub timestamp: u64`
- `ValidatorResult.pub address: String`
- `ValidatorResult.pub type_name: String`
- `VmNamedVariableSchemaResult.pub name: String`
- `VmNamedVariableSchemaResult.pub schema: VmVariableSchemaResult`
- `VmStructSchemaResult.pub fields: Vec<VmNamedVariableSchemaResult>`
- `VmStructSchemaResult.pub flags: u32`
- `VmVariableSchemaResult.pub schema: Option<VmStructSchemaResult>`
- `VmVariableSchemaResult.pub type_name: String`

### Methods

```rust
impl AccountResult: pub fn get_token_balance(&mut self, symbol: &str, decimals: u32) -> &BalanceResult
```

```rust
impl AccountResult: pub fn token_balance(&self, symbol: &str) -> Option<&BalanceResult>
```

```rust
impl BalanceResult: pub fn decimal_amount(&self) -> String
```

```rust
impl PhantasmaRpc<ReqwestTransport>: pub fn mainnet() -> Self
```

```rust
impl PhantasmaRpc<ReqwestTransport>: pub fn new(endpoint: impl Into<String>) -> Self
```

```rust
impl PhantasmaRpc<ReqwestTransport>: pub fn testnet() -> Self
```

```rust
impl PhantasmaRpc<T>: pub async fn build_sign_send_tx_msg(
```

```rust
impl PhantasmaRpc<T>: pub async fn call<R: DeserializeOwned>(&self, method: &str, params: Vec<Value>) -> Result<R>
```

```rust
impl PhantasmaRpc<T>: pub async fn call_value(&self, method: &str, params: Vec<Value>) -> Result<Value>
```

```rust
impl PhantasmaRpc<T>: pub async fn get_account(&self, address: &str) -> Result<AccountResult>
```

```rust
impl PhantasmaRpc<T>: pub async fn get_account_fungible_tokens(
```

```rust
impl PhantasmaRpc<T>: pub async fn get_account_fungible_tokens_with_address_type(
```

```rust
impl PhantasmaRpc<T>: pub async fn get_account_nfts(
```

```rust
impl PhantasmaRpc<T>: pub async fn get_account_nfts_with_address_type(
```

```rust
impl PhantasmaRpc<T>: pub async fn get_account_owned_token_series(
```

```rust
impl PhantasmaRpc<T>: pub async fn get_account_owned_token_series_with_address_type(
```

```rust
impl PhantasmaRpc<T>: pub async fn get_account_owned_tokens(
```

```rust
impl PhantasmaRpc<T>: pub async fn get_account_owned_tokens_with_address_type(
```

```rust
impl PhantasmaRpc<T>: pub async fn get_account_with_address_type(
```

```rust
impl PhantasmaRpc<T>: pub async fn get_accounts<S: AsRef<str> + Sync>(
```

```rust
impl PhantasmaRpc<T>: pub async fn get_accounts_text(
```

```rust
impl PhantasmaRpc<T>: pub async fn get_accounts_with_address_type(
```

```rust
impl PhantasmaRpc<T>: pub async fn get_address_transaction_count(&self, address: &str, chain: &str) -> Result<u64>
```

```rust
impl PhantasmaRpc<T>: pub async fn get_address_transactions(
```

```rust
impl PhantasmaRpc<T>: pub async fn get_archive(&self, hash: &str) -> Result<ArchiveResult>
```

```rust
impl PhantasmaRpc<T>: pub async fn get_auction(
```

```rust
impl PhantasmaRpc<T>: pub async fn get_auctions(
```

```rust
impl PhantasmaRpc<T>: pub async fn get_auctions_count(&self, chain: &str, symbol: &str) -> Result<u64>
```

```rust
impl PhantasmaRpc<T>: pub async fn get_block_by_hash(&self, hash: &str) -> Result<BlockResult>
```

```rust
impl PhantasmaRpc<T>: pub async fn get_block_by_height(&self, chain: &str, height: u64) -> Result<BlockResult>
```

```rust
impl PhantasmaRpc<T>: pub async fn get_block_height(&self, chain: &str) -> Result<u64>
```

```rust
impl PhantasmaRpc<T>: pub async fn get_block_transaction_count_by_hash(
```

```rust
impl PhantasmaRpc<T>: pub async fn get_block_transaction_count_by_hash_on_chain(
```

```rust
impl PhantasmaRpc<T>: pub async fn get_chain(&self, chain: &str, extended: bool) -> Result<ChainResult>
```

```rust
impl PhantasmaRpc<T>: pub async fn get_chains(&self, extended: bool) -> Result<Vec<ChainResult>>
```

```rust
impl PhantasmaRpc<T>: pub async fn get_contract(&self, contract_name: &str, chain: &str) -> Result<ContractResult>
```

```rust
impl PhantasmaRpc<T>: pub async fn get_contract_by_address(
```

```rust
impl PhantasmaRpc<T>: pub async fn get_contract_by_name(&self, chain: &str, name: &str) -> Result<ContractResult>
```

```rust
impl PhantasmaRpc<T>: pub async fn get_contracts(&self, chain: &str, extended: bool) -> Result<Vec<ContractResult>>
```

```rust
impl PhantasmaRpc<T>: pub async fn get_latest_block(&self, chain: &str) -> Result<BlockResult>
```

```rust
impl PhantasmaRpc<T>: pub async fn get_leaderboard(&self, name: &str) -> Result<LeaderboardResult>
```

```rust
impl PhantasmaRpc<T>: pub async fn get_nexus(&self, extended: bool) -> Result<NexusResult>
```

```rust
impl PhantasmaRpc<T>: pub async fn get_nft(
```

```rust
impl PhantasmaRpc<T>: pub async fn get_nfts<S: AsRef<str> + Sync>(
```

```rust
impl PhantasmaRpc<T>: pub async fn get_nfts_text(
```

```rust
impl PhantasmaRpc<T>: pub async fn get_organization(
```

```rust
impl PhantasmaRpc<T>: pub async fn get_organization_by_name(
```

```rust
impl PhantasmaRpc<T>: pub async fn get_organizations(&self, extended: bool) -> Result<Vec<OrganizationResult>>
```

```rust
impl PhantasmaRpc<T>: pub async fn get_phantasma_vm_config(&self, chain: &str) -> Result<PhantasmaVmConfigResult>
```

```rust
impl PhantasmaRpc<T>: pub async fn get_platforms(&self) -> Result<Vec<PlatformResult>>
```

```rust
impl PhantasmaRpc<T>: pub async fn get_token(&self, symbol: &str, extended: bool) -> Result<TokenResult>
```

```rust
impl PhantasmaRpc<T>: pub async fn get_token_balance(
```

```rust
impl PhantasmaRpc<T>: pub async fn get_token_balance_checked(
```

```rust
impl PhantasmaRpc<T>: pub async fn get_token_balance_with_address_type(
```

```rust
impl PhantasmaRpc<T>: pub async fn get_token_data(&self, symbol: &str, token_id: &str) -> Result<TokenDataResult>
```

```rust
impl PhantasmaRpc<T>: pub async fn get_token_nfts(
```

```rust
impl PhantasmaRpc<T>: pub async fn get_token_nfts_with_series_id(
```

```rust
impl PhantasmaRpc<T>: pub async fn get_token_series(
```

```rust
impl PhantasmaRpc<T>: pub async fn get_token_series_by_id(
```

```rust
impl PhantasmaRpc<T>: pub async fn get_token_series_by_ids(
```

```rust
impl PhantasmaRpc<T>: pub async fn get_token_with_id(
```

```rust
impl PhantasmaRpc<T>: pub async fn get_tokens(&self, extended: bool) -> Result<Vec<TokenResult>>
```

```rust
impl PhantasmaRpc<T>: pub async fn get_tokens_as_map(&self, extended: bool) -> Result<HashMap<String, TokenResult>>
```

```rust
impl PhantasmaRpc<T>: pub async fn get_tokens_by_owner(
```

```rust
impl PhantasmaRpc<T>: pub async fn get_tokens_by_owner_with_address_type(
```

```rust
impl PhantasmaRpc<T>: pub async fn get_transaction(&self, hash: &str) -> Result<TransactionResult>
```

```rust
impl PhantasmaRpc<T>: pub async fn get_transaction_by_block_hash_and_index(
```

```rust
impl PhantasmaRpc<T>: pub async fn get_transaction_by_block_hash_and_index_on_chain(
```

```rust
impl PhantasmaRpc<T>: pub async fn get_version(&self) -> Result<VersionResult>
```

```rust
impl PhantasmaRpc<T>: pub async fn invoke_raw_script(&self, chain: &str, script_hex: &str) -> Result<ScriptResult>
```

```rust
impl PhantasmaRpc<T>: pub async fn look_up_name(&self, name: &str) -> Result<String>
```

```rust
impl PhantasmaRpc<T>: pub async fn lookup_name(&self, name: &str) -> Result<String>
```

```rust
impl PhantasmaRpc<T>: pub async fn read_archive(&self, hash: &str, block_index: u32) -> Result<String>
```

```rust
impl PhantasmaRpc<T>: pub async fn send_carbon_transaction(&self, tx: &[u8]) -> Result<String>
```

```rust
impl PhantasmaRpc<T>: pub async fn send_create_token_tx(
```

```rust
impl PhantasmaRpc<T>: pub async fn send_raw_transaction(&self, tx_hex: &str) -> Result<String>
```

```rust
impl PhantasmaRpc<T>: pub async fn send_signed_tx_msg(&self, tx: &SignedTxMsg) -> Result<String>
```

```rust
impl PhantasmaRpc<T>: pub async fn send_transaction(&self, tx: &Transaction) -> Result<String>
```

```rust
impl PhantasmaRpc<T>: pub async fn sign_and_send_built_transaction(
```

```rust
impl PhantasmaRpc<T>: pub async fn sign_and_send_carbon_transaction(
```

```rust
impl PhantasmaRpc<T>: pub async fn sign_and_send_transaction(
```

```rust
impl PhantasmaRpc<T>: pub async fn write_archive(
```

```rust
impl PhantasmaRpc<T>: pub async fn write_archive_base64(
```

```rust
impl PhantasmaRpc<T>: pub fn parse_create_token_result(&self, result_hex: &str) -> Result<u64>
```

```rust
impl PhantasmaRpc<T>: pub fn parse_create_token_series_result(&self, result_hex: &str) -> Result<u32>
```

```rust
impl PhantasmaRpc<T>: pub fn sign_carbon_transaction(
```

```rust
impl PhantasmaRpc<T>: pub fn with_timeout(mut self, timeout: Duration) -> Self
```

```rust
impl PhantasmaRpc<T>: pub fn with_transport(endpoint: impl Into<String>, transport: T) -> Self
```

```rust
impl ScriptResult: pub fn decode_result(&self) -> Result<VMObject>
```

```rust
impl ScriptResult: pub fn decode_results(&self, index: usize) -> Result<VMObject>
```

```rust
impl StakeResult: pub fn decimal_amount(&self) -> String
```

```rust
impl TokenResult: pub fn has_flag(&self, flag: &str) -> bool
```

```rust
impl TokenResult: pub fn is_burnable(&self) -> bool
```

```rust
impl TokenResult: pub fn is_divisible(&self) -> bool
```

```rust
impl TokenResult: pub fn is_fiat(&self) -> bool
```

```rust
impl TokenResult: pub fn is_finite(&self) -> bool
```

```rust
impl TokenResult: pub fn is_fuel(&self) -> bool
```

```rust
impl TokenResult: pub fn is_fungible(&self) -> bool
```

```rust
impl TokenResult: pub fn is_mintable(&self) -> bool
```

```rust
impl TokenResult: pub fn is_non_fungible(&self) -> bool
```

```rust
impl TokenResult: pub fn is_stakable(&self) -> bool
```

```rust
impl TokenResult: pub fn is_transferable(&self) -> bool
```

```rust
impl TransactionResult: pub fn state_is_fault(&self) -> bool
```

```rust
impl TransactionResult: pub fn state_is_success(&self) -> bool
```

```rust
pub fn convert_decimals(amount: &str, decimals: u32) -> String
```

```rust
pub fn parse_json_rpc_response(status: u16, body: Value) -> Result<Value>
```

## phantasma_sdk::transaction

Source: `src/transaction.rs`

### Declarations

```rust
pub const SDK_PAYLOAD: &[u8] = b"RS-SDK-v1.0.2"
```

```rust
pub struct Transaction
```

### Fields

- `Transaction.pub chain_name: String`
- `Transaction.pub expiration: u32`
- `Transaction.pub nexus_name: String`
- `Transaction.pub payload: Vec<u8>`
- `Transaction.pub script: Vec<u8>`
- `Transaction.pub signatures: Vec<Ed25519Signature>`

### Methods

```rust
impl Transaction: pub fn from_bytes(data: &[u8]) -> Result<Self>
```

```rust
impl Transaction: pub fn hash(&self) -> Hash
```

```rust
impl Transaction: pub fn is_signed_by(&self, key_pair: &PhantasmaKeys) -> bool
```

```rust
impl Transaction: pub fn mine(&mut self, difficulty: u32)
```

```rust
impl Transaction: pub fn new(
```

```rust
impl Transaction: pub fn sign(&mut self, key_pair: &PhantasmaKeys) -> Ed25519Signature
```

```rust
impl Transaction: pub fn to_bytes(&self, with_signatures: bool) -> Vec<u8>
```

```rust
impl Transaction: pub fn with_payload(mut self, payload: impl Into<Vec<u8>>) -> Self
```

```rust
pub fn big_int(value: i64) -> BigInt
```

```rust
pub fn tx_state_is_fault(state: &str) -> bool
```

```rust
pub fn tx_state_is_success(state: &str) -> bool
```

## phantasma_sdk::vm

Source: `src/vm.rs`

### Declarations

```rust
pub enum Opcode
```

```rust
pub enum ScriptArg
```

```rust
pub enum VMObject
```

```rust
pub enum VMType
```

```rust
pub struct ScriptBuilder
```

### Methods

```rust
impl ScriptBuilder: pub fn allow_gas(
```

```rust
impl ScriptBuilder: pub fn allow_gas_text(
```

```rust
impl ScriptBuilder: pub fn begin() -> Self
```

```rust
impl ScriptBuilder: pub fn call_contract<I>(&mut self, contract_name: &str, method: &str, args: I) -> &mut Self
```

```rust
impl ScriptBuilder: pub fn call_interop<I>(&mut self, method: &str, args: I) -> &mut Self
```

```rust
impl ScriptBuilder: pub fn call_nft<I>(&mut self, symbol: &str, series_id: u64, method: &str, args: I) -> &mut Self
```

```rust
impl ScriptBuilder: pub fn cross_transfer_nft(
```

```rust
impl ScriptBuilder: pub fn cross_transfer_nft_text(
```

```rust
impl ScriptBuilder: pub fn cross_transfer_nft_to_text(
```

```rust
impl ScriptBuilder: pub fn cross_transfer_token(
```

```rust
impl ScriptBuilder: pub fn cross_transfer_token_text(
```

```rust
impl ScriptBuilder: pub fn cross_transfer_token_to_text(
```

```rust
impl ScriptBuilder: pub fn current_size(&self) -> usize
```

```rust
impl ScriptBuilder: pub fn emit(&mut self, opcode: Opcode) -> &mut Self
```

```rust
impl ScriptBuilder: pub fn emit_call(&mut self, label: &str, register_count: u8) -> &mut Self
```

```rust
impl ScriptBuilder: pub fn emit_conditional_jump(&mut self, opcode: Opcode, src_reg: u8, label: &str) -> &mut Self
```

```rust
impl ScriptBuilder: pub fn emit_copy(&mut self, src_reg: u8, dst_reg: u8) -> &mut Self
```

```rust
impl ScriptBuilder: pub fn emit_ext_call(&mut self, method: &str, reg: u8) -> &mut Self
```

```rust
impl ScriptBuilder: pub fn emit_jump(&mut self, opcode: Opcode, label: &str, reg: u8) -> &mut Self
```

```rust
impl ScriptBuilder: pub fn emit_label(&mut self, label: &str) -> &mut Self
```

```rust
impl ScriptBuilder: pub fn emit_load(&mut self, reg: u8, data: impl AsRef<[u8]>, vm_type: VMType) -> &mut Self
```

```rust
impl ScriptBuilder: pub fn emit_load_bool(&mut self, reg: u8, value: bool) -> &mut Self
```

```rust
impl ScriptBuilder: pub fn emit_load_number(&mut self, reg: u8, value: &BigInt) -> &mut Self
```

```rust
impl ScriptBuilder: pub fn emit_load_string(&mut self, reg: u8, value: &str) -> &mut Self
```

```rust
impl ScriptBuilder: pub fn emit_load_time(&mut self, reg: u8, unix_seconds: u64) -> &mut Self
```

```rust
impl ScriptBuilder: pub fn emit_load_timestamp(&mut self, reg: u8, unix_seconds: u64) -> &mut Self
```

```rust
impl ScriptBuilder: pub fn emit_move(&mut self, src_reg: u8, dst_reg: u8) -> &mut Self
```

```rust
impl ScriptBuilder: pub fn emit_pop(&mut self, reg: u8) -> &mut Self
```

```rust
impl ScriptBuilder: pub fn emit_push(&mut self, reg: u8) -> &mut Self
```

```rust
impl ScriptBuilder: pub fn emit_raw(&mut self, data: impl AsRef<[u8]>) -> &mut Self
```

```rust
impl ScriptBuilder: pub fn emit_throw(&mut self, reg: u8) -> &mut Self
```

```rust
impl ScriptBuilder: pub fn emit_var_bytes(&mut self, value: u64) -> &mut Self
```

```rust
impl ScriptBuilder: pub fn end_script(&mut self) -> Result<Vec<u8>>
```

```rust
impl ScriptBuilder: pub fn end_script_hex(&mut self) -> Result<String>
```

```rust
impl ScriptBuilder: pub fn end_script_with_error(&mut self) -> (Vec<u8>, Option<PhantasmaError>)
```

```rust
impl ScriptBuilder: pub fn mint_tokens(
```

```rust
impl ScriptBuilder: pub fn mint_tokens_text(
```

```rust
impl ScriptBuilder: pub fn new() -> Self
```

```rust
impl ScriptBuilder: pub fn spend_gas(&mut self, address: Address) -> &mut Self
```

```rust
impl ScriptBuilder: pub fn spend_gas_text(&mut self, address: &str) -> &mut Self
```

```rust
impl ScriptBuilder: pub fn stake(&mut self, address: Address, amount: u64) -> &mut Self
```

```rust
impl ScriptBuilder: pub fn stake_text(&mut self, address: &str, amount: u64) -> &mut Self
```

```rust
impl ScriptBuilder: pub fn to_script(&self) -> Result<Vec<u8>>
```

```rust
impl ScriptBuilder: pub fn transfer_balance(&mut self, symbol: &str, from: Address, to: Address) -> &mut Self
```

```rust
impl ScriptBuilder: pub fn transfer_balance_text(&mut self, symbol: &str, from: &str, to: &str) -> &mut Self
```

```rust
impl ScriptBuilder: pub fn transfer_nft(
```

```rust
impl ScriptBuilder: pub fn transfer_nft_text(
```

```rust
impl ScriptBuilder: pub fn transfer_nft_to_text(
```

```rust
impl ScriptBuilder: pub fn transfer_tokens(
```

```rust
impl ScriptBuilder: pub fn transfer_tokens_text(
```

```rust
impl ScriptBuilder: pub fn transfer_tokens_to_text(
```

```rust
impl ScriptBuilder: pub fn unstake(&mut self, address: Address, amount: u64) -> &mut Self
```

```rust
impl ScriptBuilder: pub fn unstake_text(&mut self, address: &str, amount: u64) -> &mut Self
```

```rust
impl VMObject: pub fn array_type(&self) -> VMType
```

```rust
impl VMObject: pub fn as_bool(&self) -> Result<bool>
```

```rust
impl VMObject: pub fn as_bytes(&self) -> Result<Vec<u8>>
```

```rust
impl VMObject: pub fn as_number(&self) -> Result<BigInt>
```

```rust
impl VMObject: pub fn as_string(&self) -> Result<String>
```

```rust
impl VMObject: pub fn cast_to(&self, target: VMType) -> Result<Self>
```

```rust
impl VMObject: pub fn from_bytes(data: &[u8]) -> Result<Self>
```

```rust
impl VMObject: pub fn read(reader: &mut BinaryReader<'_>) -> Result<Self>
```

```rust
impl VMObject: pub fn to_bytes(&self) -> Result<Vec<u8>>
```

```rust
impl VMObject: pub fn vm_type(&self) -> VMType
```

```rust
impl VMObject: pub fn write(&self, writer: &mut BinaryWriter) -> Result<()>
```

```rust
pub fn script_arg_number_to_i64(value: &ScriptArg) -> Option<i64>
```

### Variants

- `Opcode::Abs = 34`
- `Opcode::Add = 35`
- `Opcode::And = 22`
- `Opcode::Call = 6`
- `Opcode::Cast = 14`
- `Opcode::Cat = 15`
- `Opcode::Clear = 49`
- `Opcode::Copy = 2`
- `Opcode::Count = 20`
- `Opcode::Ctx = 45`
- `Opcode::Debug = 52`
- `Opcode::Dec = 31`
- `Opcode::Div = 38`
- `Opcode::Equal = 25`
- `Opcode::Evm = 255`
- `Opcode::ExtCall = 7`
- `Opcode::Get = 48`
- `Opcode::Gt = 27`
- `Opcode::Gte = 29`
- `Opcode::Inc = 30`
- `Opcode::Jmp = 8`
- `Opcode::JmpIf = 9`
- `Opcode::JmpNot = 10`
- `Opcode::Left = 17`
- `Opcode::Load = 13`
- `Opcode::Lt = 26`
- `Opcode::Lte = 28`
- `Opcode::Max = 43`
- `Opcode::Min = 42`
- `Opcode::Mod = 39`
- `Opcode::Move = 1`
- `Opcode::Mul = 37`
- `Opcode::Negate = 33`
- `Opcode::Nop = 0`
- `Opcode::Not = 21`
- `Opcode::Or = 23`
- `Opcode::Pack = 51`
- `Opcode::Pop = 4`
- `Opcode::Pow = 44`
- `Opcode::Push = 3`
- `Opcode::Put = 47`
- `Opcode::Range = 16`
- `Opcode::Remove = 54`
- `Opcode::Ret = 11`
- `Opcode::Right = 18`
- `Opcode::Shl = 40`
- `Opcode::Shr = 41`
- `Opcode::Sign = 32`
- `Opcode::Size = 19`
- `Opcode::Sub = 36`
- `Opcode::Substr = 53`
- `Opcode::Swap = 5`
- `Opcode::Switch = 46`
- `Opcode::Throw = 12`
- `Opcode::Unpack = 50`
- `Opcode::Xor = 24`
- `ScriptArg::Address(Address)`
- `ScriptArg::Array(Vec<ScriptArg>)`
- `ScriptArg::Bool(bool)`
- `ScriptArg::Bytes(Vec<u8>)`
- `ScriptArg::Number(BigInt)`
- `ScriptArg::String(String)`
- `ScriptArg::Timestamp(u64)`
- `VMObject::Bool(bool)`
- `VMObject::Bytes(Vec<u8>)`
- `VMObject::Enum(u32)`
- `VMObject::None`
- `VMObject::Number(BigInt)`
- `VMObject::Object(Vec<u8>)`
- `VMObject::String(String)`
- `VMObject::Struct(Vec<(VMObject, VMObject)>)`
- `VMObject::Timestamp(u32)`
- `VMType::Bool = 6`
- `VMType::Bytes = 2`
- `VMType::Enum = 7`
- `VMType::None = 0`
- `VMType::Number = 3`
- `VMType::Object = 8`
- `VMType::String = 4`
- `VMType::Struct = 1`
- `VMType::Timestamp = 5`
