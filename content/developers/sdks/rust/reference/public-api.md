---
title: "Rust SDK Public API Inventory"
linkTitle: "Public API Inventory"
weight: 50
---

This page lists the public classes, methods, functions, enum values,
fields, and constants of the SDK. Use it to check exact names when
working with lower-level SDK APIs.

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
pub const DEFAULT_TX_EXPIRY: Duration = Duration::from_secs(45)
```

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
pub enum GovernanceContractMethod
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
pub mod standard_meta
```

```rust
pub struct BurnFungibleArgs
```

```rust
pub struct BurnFungibleParams
```

```rust
pub struct BurnNonFungibleArgs
```

```rust
pub struct BurnNonFungibleParams
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
pub struct CreateTokenSeriesArgs
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
pub struct MintFungibleParams
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
pub struct RegisterNameArgs
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
pub struct TransferFungibleParams
```

```rust
pub struct TransferNonFungibleArgs
```

```rust
pub struct TransferNonFungibleParams
```

```rust
pub struct TxLimits
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
pub trait TxSigner: Send + Sync
```

```rust
pub type TokenSchemasJSON = TokenSchemasJson
```

### Fields

- `BurnFungibleArgs.pub amount: IntX`
- `BurnFungibleArgs.pub from_address: Bytes32`
- `BurnFungibleArgs.pub token_id: u64`
- `BurnFungibleParams.pub amount: IntX`
- `BurnFungibleParams.pub from: Bytes32`
- `BurnFungibleParams.pub gas_payer: Option<Bytes32>`
- `BurnFungibleParams.pub limits: TxLimits`
- `BurnFungibleParams.pub token_id: u64`
- `BurnNonFungibleArgs.pub from_address: Bytes32`
- `BurnNonFungibleArgs.pub instance_ids: Vec<u64>`
- `BurnNonFungibleArgs.pub token_id: u64`
- `BurnNonFungibleParams.pub from: Bytes32`
- `BurnNonFungibleParams.pub gas_payer: Option<Bytes32>`
- `BurnNonFungibleParams.pub instance_id: u64`
- `BurnNonFungibleParams.pub limits: TxLimits`
- `BurnNonFungibleParams.pub token_id: u64`
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
- `CreateTokenSeriesArgs.pub info: SeriesInfo`
- `CreateTokenSeriesArgs.pub token_id: u64`
- `GasConfig.pub data_escrow_per_row: u64`
- `GasConfig.pub data_token_id: u64`
- `GasConfig.pub fee_multiplier: u64`
- `GasConfig.pub fee_shift: u8`
- `GasConfig.pub gas_burn_ratio_mul: u64`
- `GasConfig.pub gas_burn_ratio_shift: u8`
- `GasConfig.pub gas_dapp_ratio_mul: u64`
- `GasConfig.pub gas_dapp_ratio_shift: u8`
- `GasConfig.pub gas_fee_create_token_base: u64`
- `GasConfig.pub gas_fee_create_token_series: u64`
- `GasConfig.pub gas_fee_create_token_symbol: u64`
- `GasConfig.pub gas_fee_per_byte: u64`
- `GasConfig.pub gas_fee_query: u64`
- `GasConfig.pub gas_fee_register_name: u64`
- `GasConfig.pub gas_fee_transfer: u64`
- `GasConfig.pub gas_producer_ratio_mul: u64`
- `GasConfig.pub gas_producer_ratio_shift: u8`
- `GasConfig.pub gas_token_id: u64`
- `GasConfig.pub legacy_data_escrow_per_row: u64`
- `GasConfig.pub max_name_length: u8`
- `GasConfig.pub max_structure_size: u32`
- `GasConfig.pub max_token_symbol_length: u8`
- `GasConfig.pub minimum_gas_bill: u64`
- `GasConfig.pub minimum_gas_offer: u64`
- `GasConfig.pub policy_fee_create_token_base: u64`
- `GasConfig.pub policy_fee_create_token_series: u64`
- `GasConfig.pub policy_fee_create_token_symbol: u64`
- `GasConfig.pub policy_fee_register_name: u64`
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
- `MintFungibleParams.pub amount: IntX`
- `MintFungibleParams.pub limits: TxLimits`
- `MintFungibleParams.pub owner: Bytes32`
- `MintFungibleParams.pub to: Bytes32`
- `MintFungibleParams.pub token_id: u64`
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
- `RegisterNameArgs.pub address: Bytes32`
- `RegisterNameArgs.pub name: SmallString`
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
- `TransferFungibleParams.pub amount: u64`
- `TransferFungibleParams.pub from: Bytes32`
- `TransferFungibleParams.pub gas_payer: Option<Bytes32>`
- `TransferFungibleParams.pub limits: TxLimits`
- `TransferFungibleParams.pub to: Bytes32`
- `TransferFungibleParams.pub token_id: u64`
- `TransferNonFungibleArgs.pub from_address: Bytes32`
- `TransferNonFungibleArgs.pub instance_ids: Vec<u64>`
- `TransferNonFungibleArgs.pub to: Bytes32`
- `TransferNonFungibleArgs.pub token_id: u64`
- `TransferNonFungibleParams.pub from: Bytes32`
- `TransferNonFungibleParams.pub gas_payer: Option<Bytes32>`
- `TransferNonFungibleParams.pub instance_ids: Vec<u64>`
- `TransferNonFungibleParams.pub limits: TxLimits`
- `TransferNonFungibleParams.pub to: Bytes32`
- `TransferNonFungibleParams.pub token_id: u64`
- `TxLimits.pub expiry: i64`
- `TxLimits.pub max_data: u64`
- `TxLimits.pub max_gas: u64`
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
impl CarbonReader<'a>: pub fn read_length_for(&mut self, element_size: usize) -> Result<usize>
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
impl GasConfig: pub fn has_gas_model_v2(&self) -> bool
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
pub async fn sign_and_serialize_tx_msg_with( msg: &TxMsg, signers: &[&dyn TxSigner], ) -> Result<Vec<u8>>
```

```rust
pub async fn sign_tx_msg_with(msg: &TxMsg, signers: &[&dyn TxSigner]) -> Result<SignedTxMsg>
```

```rust
pub fn build_and_serialize_token_schemas(schemas: Option<&TokenSchemas>) -> Result<Vec<u8>>
```

```rust
pub fn build_burn_fungible_tx(p: BurnFungibleParams) -> TxMsg
```

```rust
pub fn build_burn_non_fungible_tx(p: BurnNonFungibleParams) -> TxMsg
```

```rust
pub fn build_create_token_series_tx( token_id: u64, series_info: SeriesInfo, creator: Bytes32, limits: TxLimits, ) -> Result<TxMsg>
```

```rust
pub fn build_create_token_series_tx_and_sign( token_id: u64, series_info: SeriesInfo, signer: &PhantasmaKeys, config: Option<&GasConfig>, options: &PlanAndSignOptions, ) -> Result<Vec<u8>>
```

```rust
pub fn build_create_token_series_tx_and_sign_hex( token_id: u64, series_info: SeriesInfo, signer: &PhantasmaKeys, config: Option<&GasConfig>, options: &PlanAndSignOptions, ) -> Result<String>
```

```rust
pub fn build_create_token_tx( token_info: TokenInfo, creator: Bytes32, limits: TxLimits, ) -> Result<TxMsg>
```

```rust
pub fn build_create_token_tx_and_sign( token_info: TokenInfo, signer: &PhantasmaKeys, config: Option<&GasConfig>, options: &PlanAndSignOptions, ) -> Result<Vec<u8>>
```

```rust
pub fn build_create_token_tx_and_sign_hex( token_info: TokenInfo, signer: &PhantasmaKeys, config: Option<&GasConfig>, options: &PlanAndSignOptions, ) -> Result<String>
```

```rust
pub fn build_mint_fungible_tx(p: MintFungibleParams) -> TxMsg
```

```rust
pub fn build_mint_phantasma_non_fungible_single_tx( token_id: u64, phantasma_series_id: impl Into<BigInt>, sender: Bytes32, receiver: Bytes32, public_rom: Vec<u8>, ram: Vec<u8>, limits: TxLimits, ) -> Result<TxMsg>
```

```rust
pub fn build_mint_phantasma_non_fungible_single_tx_and_sign( token_id: u64, phantasma_series_id: impl Into<BigInt>, signer: &PhantasmaKeys, receiver: Bytes32, public_rom: Vec<u8>, ram: Vec<u8>, config: Option<&GasConfig>, options: &PlanAndSignOptions, ) -> Result<Vec<u8>>
```

```rust
pub fn build_mint_phantasma_non_fungible_single_tx_and_sign_hex( token_id: u64, phantasma_series_id: impl Into<BigInt>, signer: &PhantasmaKeys, receiver: Bytes32, public_rom: Vec<u8>, ram: Vec<u8>, config: Option<&GasConfig>, options: &PlanAndSignOptions, ) -> Result<String>
```

```rust
pub fn build_mint_phantasma_non_fungible_tx( token_id: u64, sender: Bytes32, receiver: Bytes32, tokens: Vec<PhantasmaNFTMintInfo>, limits: TxLimits, ) -> Result<TxMsg>
```

```rust
pub fn build_mint_phantasma_non_fungible_tx_and_sign( token_id: u64, signer: &PhantasmaKeys, receiver: Bytes32, tokens: Vec<PhantasmaNFTMintInfo>, config: Option<&GasConfig>, options: &PlanAndSignOptions, ) -> Result<Vec<u8>>
```

```rust
pub fn build_mint_phantasma_non_fungible_tx_and_sign_hex( token_id: u64, signer: &PhantasmaKeys, receiver: Bytes32, tokens: Vec<PhantasmaNFTMintInfo>, config: Option<&GasConfig>, options: &PlanAndSignOptions, ) -> Result<String>
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
pub fn build_transfer_fungible_tx(p: TransferFungibleParams) -> TxMsg
```

```rust
pub fn build_transfer_non_fungible_tx(p: TransferNonFungibleParams) -> Result<TxMsg>
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
pub fn default_expiry() -> i64
```

```rust
pub fn default_market_config() -> MarketConfig
```

```rust
pub fn deserialize<T: CarbonSerializable>(data: impl AsRef<[u8]>) -> Result<T>
```

```rust
pub fn envelope_bytes(msg: &TxMsg, witness_count: Option<u32>) -> Result<u32>
```

```rust
pub fn expiry_within(expiry_window: Duration, margin: Duration) -> Result<i64>
```

```rust
pub fn get_nft_address(carbon_token_id: u64, instance_id: u64) -> Bytes32
```

```rust
pub fn is_nft_address(address: &Bytes32) -> bool
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
pub fn required_witnesses(msg: &TxMsg) -> Option<Vec<Bytes32>>
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
pub fn sign_and_serialize_tx_msg_with_keys( msg: &TxMsg, keys: &[&PhantasmaKeys], ) -> Result<Vec<u8>>
```

```rust
pub fn sign_tx_msg(msg: &TxMsg, keys: &PhantasmaKeys) -> Result<SignedTxMsg>
```

```rust
pub fn sign_tx_msg_with_keys(msg: &TxMsg, keys: &[&PhantasmaKeys]) -> Result<SignedTxMsg>
```

```rust
pub fn token_schemas_from_json(data: &str) -> Result<TokenSchemas>
```

```rust
pub fn unpack_nft_address(address: &Bytes32) -> (u64, u64)
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

- `GovernanceContractMethod::RegisterName = 1`
- `GovernanceContractMethod::SetGasConfig = 3`
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
- `PhantasmaError::Preflight(String)`
- `PhantasmaError::Rpc { code: Option<i64>, message: String }`
- `PhantasmaError::Serialization(String)`

## phantasma_sdk::extended_events

Source: `src/extended_events.rs`

### Declarations

```rust
pub enum EventData
```

```rust
pub enum SpecialResolutionArguments
```

```rust
pub struct AddressArguments
```

```rust
pub struct BalanceArguments
```

```rust
pub struct BurnFungibleArguments
```

```rust
pub struct BurnNonFungibleArguments
```

```rust
pub struct ChainConfigArguments
```

```rust
pub struct ConsensusNode
```

```rust
pub struct ContractStorageRow
```

```rust
pub struct ContractStorageTable
```

```rust
pub struct CreateMintedTokenSeriesArguments
```

```rust
pub struct CreateTokenArguments
```

```rust
pub struct DeployContractArguments
```

```rust
pub struct ExecuteScriptArguments
```

```rust
pub struct GasConfigArguments
```

```rust
pub struct ImportContractsArguments
```

```rust
pub struct ImportedContract
```

```rust
pub struct MarketOrderData
```

```rust
pub struct MetadataArguments
```

```rust
pub struct MintFungibleArguments
```

```rust
pub struct MintNonFungibleArguments
```

```rust
pub struct MintPhantasmaNonFungibleArguments
```

```rust
pub struct NameArguments
```

```rust
pub struct NestedResolutionArguments
```

```rust
pub struct NftMint
```

```rust
pub struct NodeConfigArguments
```

```rust
pub struct NonFungibleInfoArguments
```

```rust
pub struct NonFungibleInfoByRomIdArguments
```

```rust
pub struct PhantasmaNftMint
```

```rust
pub struct PhantasmaVmConfigArguments
```

```rust
pub struct RawArguments
```

```rust
pub struct RegisterNameArguments
```

```rust
pub struct RegisterTokenContractArguments
```

```rust
pub struct RepairSeriesArguments
```

```rust
pub struct RepairTokenArguments
```

```rust
pub struct SeriesInfoByMetaIdArguments
```

```rust
pub struct SeriesMintCountRepair
```

```rust
pub struct SeriesSupplement
```

```rust
pub struct SpecialResolutionCall
```

```rust
pub struct SpecialResolutionData
```

```rust
pub struct SymbolArguments
```

```rust
pub struct TokenCreateData
```

```rust
pub struct TokenReferenceArguments
```

```rust
pub struct TokenRepair
```

```rust
pub struct TokenSeriesArguments
```

```rust
pub struct TokenSeriesCreateData
```

```rust
pub struct TokenSeriesReferenceArguments
```

```rust
pub struct TokensConfigArguments
```

```rust
pub struct TransferFungibleArguments
```

```rust
pub struct TransferNonFungibleArguments
```

```rust
pub struct UpdateSeriesMetadataArguments
```

```rust
pub struct UpdateTokenMetadataArguments
```

### Fields

- `AddressArguments.pub address: String`
- `BalanceArguments.pub address: String`
- `BalanceArguments.pub token: String`
- `BalanceArguments.pub token_id: String`
- `BurnFungibleArguments.pub amount: String`
- `BurnFungibleArguments.pub from: String`
- `BurnFungibleArguments.pub token: String`
- `BurnFungibleArguments.pub token_id: String`
- `BurnNonFungibleArguments.pub address: String`
- `BurnNonFungibleArguments.pub instance_ids: Vec<String>`
- `BurnNonFungibleArguments.pub token: String`
- `BurnNonFungibleArguments.pub token_id: String`
- `ChainConfigArguments.pub allowed_tx_types: String`
- `ChainConfigArguments.pub block_rate_target: String`
- `ChainConfigArguments.pub expiry_window: String`
- `ChainConfigArguments.pub reserved1: String`
- `ChainConfigArguments.pub reserved2: String`
- `ChainConfigArguments.pub reserved3: String`
- `ChainConfigArguments.pub version: String`
- `ConsensusNode.pub id: String`
- `ConsensusNode.pub type_name: String`
- `ContractStorageRow.pub key: String`
- `ContractStorageRow.pub value: String`
- `ContractStorageTable.pub name: String`
- `ContractStorageTable.pub rows: Vec<ContractStorageRow>`
- `CreateMintedTokenSeriesArguments.pub max_mint: String`
- `CreateMintedTokenSeriesArguments.pub max_supply: String`
- `CreateMintedTokenSeriesArguments.pub metadata: Option<BTreeMap<String, VmValue>>`
- `CreateMintedTokenSeriesArguments.pub metadata_raw: Option<String>`
- `CreateMintedTokenSeriesArguments.pub owner: String`
- `CreateMintedTokenSeriesArguments.pub rams: Vec<String>`
- `CreateMintedTokenSeriesArguments.pub recipient: String`
- `CreateMintedTokenSeriesArguments.pub roms: Vec<String>`
- `CreateMintedTokenSeriesArguments.pub series_id: Option<String>`
- `CreateMintedTokenSeriesArguments.pub token: String`
- `CreateMintedTokenSeriesArguments.pub token_id: String`
- `CreateTokenArguments.pub decimals: String`
- `CreateTokenArguments.pub flags: String`
- `CreateTokenArguments.pub max_supply: String`
- `CreateTokenArguments.pub metadata: Option<BTreeMap<String, VmValue>>`
- `CreateTokenArguments.pub owner: String`
- `CreateTokenArguments.pub symbol: String`
- `CreateTokenArguments.pub token_schemas: Option<String>`
- `DeployContractArguments.pub abi: String`
- `DeployContractArguments.pub contract_name: String`
- `DeployContractArguments.pub from: String`
- `DeployContractArguments.pub script: String`
- `ExecuteScriptArguments.pub gas_from: String`
- `ExecuteScriptArguments.pub max_gas: String`
- `ExecuteScriptArguments.pub script: String`
- `GasConfigArguments.pub data_escrow_per_row: String`
- `GasConfigArguments.pub data_token_id: String`
- `GasConfigArguments.pub fee_multiplier: String`
- `GasConfigArguments.pub fee_shift: String`
- `GasConfigArguments.pub gas_burn_ratio_mul: String`
- `GasConfigArguments.pub gas_burn_ratio_shift: String`
- `GasConfigArguments.pub gas_dapp_ratio_mul: Option<String>`
- `GasConfigArguments.pub gas_dapp_ratio_shift: Option<String>`
- `GasConfigArguments.pub gas_fee_create_token_base: String`
- `GasConfigArguments.pub gas_fee_create_token_series: String`
- `GasConfigArguments.pub gas_fee_create_token_symbol: String`
- `GasConfigArguments.pub gas_fee_per_byte: String`
- `GasConfigArguments.pub gas_fee_query: String`
- `GasConfigArguments.pub gas_fee_register_name: String`
- `GasConfigArguments.pub gas_fee_transfer: String`
- `GasConfigArguments.pub gas_producer_ratio_mul: Option<String>`
- `GasConfigArguments.pub gas_producer_ratio_shift: Option<String>`
- `GasConfigArguments.pub gas_token_id: String`
- `GasConfigArguments.pub legacy_data_escrow_per_row: Option<String>`
- `GasConfigArguments.pub max_name_length: String`
- `GasConfigArguments.pub max_structure_size: String`
- `GasConfigArguments.pub max_token_symbol_length: String`
- `GasConfigArguments.pub minimum_gas_bill: Option<String>`
- `GasConfigArguments.pub minimum_gas_offer: String`
- `GasConfigArguments.pub policy_fee_create_token_base: Option<String>`
- `GasConfigArguments.pub policy_fee_create_token_series: Option<String>`
- `GasConfigArguments.pub policy_fee_create_token_symbol: Option<String>`
- `GasConfigArguments.pub policy_fee_register_name: Option<String>`
- `GasConfigArguments.pub version: String`
- `ImportContractsArguments.pub contracts: Vec<ImportedContract>`
- `ImportContractsArguments.pub contracts_count: String`
- `ImportedContract.pub abi: String`
- `ImportedContract.pub address: String`
- `ImportedContract.pub name: String`
- `ImportedContract.pub owner: String`
- `ImportedContract.pub root_variables: Vec<ContractStorageRow>`
- `ImportedContract.pub script: String`
- `ImportedContract.pub tables: Vec<ContractStorageTable>`
- `MarketOrderData.pub base_symbol: String`
- `MarketOrderData.pub buyer: String`
- `MarketOrderData.pub carbon_base_token_id: u64`
- `MarketOrderData.pub carbon_instance_id: u64`
- `MarketOrderData.pub carbon_quote_token_id: u64`
- `MarketOrderData.pub end_date: i64`
- `MarketOrderData.pub end_price: String`
- `MarketOrderData.pub price: String`
- `MarketOrderData.pub quote_symbol: String`
- `MarketOrderData.pub seller: String`
- `MarketOrderData.pub start_date: i64`
- `MarketOrderData.pub token_id: String`
- `MarketOrderData.pub type_name: String`
- `MetadataArguments.pub metadata: BTreeMap<String, VmValue>`
- `MintFungibleArguments.pub amount: String`
- `MintFungibleArguments.pub to: String`
- `MintFungibleArguments.pub token: String`
- `MintFungibleArguments.pub token_id: String`
- `MintNonFungibleArguments.pub owner: String`
- `MintNonFungibleArguments.pub token: String`
- `MintNonFungibleArguments.pub token_id: String`
- `MintNonFungibleArguments.pub tokens: Vec<NftMint>`
- `MintPhantasmaNonFungibleArguments.pub owner: String`
- `MintPhantasmaNonFungibleArguments.pub token: String`
- `MintPhantasmaNonFungibleArguments.pub token_id: String`
- `MintPhantasmaNonFungibleArguments.pub tokens: Vec<PhantasmaNftMint>`
- `NameArguments.pub name: String`
- `NestedResolutionArguments.pub resolution_id: String`
- `NftMint.pub ram: String`
- `NftMint.pub rom: String`
- `NftMint.pub series_id: String`
- `NodeConfigArguments.pub nodes: Vec<ConsensusNode>`
- `NonFungibleInfoArguments.pub get_schemas: String`
- `NonFungibleInfoArguments.pub instance_id: String`
- `NonFungibleInfoArguments.pub token: String`
- `NonFungibleInfoArguments.pub token_id: String`
- `NonFungibleInfoByRomIdArguments.pub get_schemas: String`
- `NonFungibleInfoByRomIdArguments.pub rom_id: String`
- `NonFungibleInfoByRomIdArguments.pub token: String`
- `NonFungibleInfoByRomIdArguments.pub token_id: String`
- `PhantasmaNftMint.pub phantasma_series_id: String`
- `PhantasmaNftMint.pub ram: String`
- `PhantasmaNftMint.pub rom: String`
- `PhantasmaVmConfigArguments.pub feature_level: String`
- `PhantasmaVmConfigArguments.pub fuel_per_contract_deploy: String`
- `PhantasmaVmConfigArguments.pub gas_account: String`
- `PhantasmaVmConfigArguments.pub gas_constructor: String`
- `PhantasmaVmConfigArguments.pub gas_leaderboard: String`
- `PhantasmaVmConfigArguments.pub gas_nexus: String`
- `PhantasmaVmConfigArguments.pub gas_oracle: String`
- `PhantasmaVmConfigArguments.pub gas_organization: String`
- `PhantasmaVmConfigArguments.pub gas_standard: String`
- `RawArguments.pub raw_args: String`
- `RegisterNameArguments.pub address: String`
- `RegisterNameArguments.pub name: String`
- `RegisterTokenContractArguments.pub abi: String`
- `RegisterTokenContractArguments.pub script: String`
- `RegisterTokenContractArguments.pub symbol: String`
- `RegisterTokenContractArguments.pub token: Option<String>`
- `RegisterTokenContractArguments.pub token_id: String`
- `RepairSeriesArguments.pub repairs: Vec<SeriesMintCountRepair>`
- `RepairSeriesArguments.pub repairs_count: String`
- `RepairSeriesArguments.pub supplements: Vec<SeriesSupplement>`
- `RepairSeriesArguments.pub supplements_count: String`
- `RepairTokenArguments.pub repairs: Vec<TokenRepair>`
- `RepairTokenArguments.pub repairs_count: String`
- `SeriesInfoByMetaIdArguments.pub rom_id: String`
- `SeriesInfoByMetaIdArguments.pub token: String`
- `SeriesInfoByMetaIdArguments.pub token_id: String`
- `SeriesMintCountRepair.pub abi: String`
- `SeriesMintCountRepair.pub imported_live_count: String`
- `SeriesMintCountRepair.pub phantasma_series_id: String`
- `SeriesMintCountRepair.pub script: String`
- `SeriesMintCountRepair.pub token: String`
- `SeriesMintCountRepair.pub token_id: String`
- `SeriesSupplement.pub abi: String`
- `SeriesSupplement.pub max_supply: String`
- `SeriesSupplement.pub mint_count: String`
- `SeriesSupplement.pub mode: String`
- `SeriesSupplement.pub phantasma_series_id: String`
- `SeriesSupplement.pub rom: String`
- `SeriesSupplement.pub script: String`
- `SeriesSupplement.pub token: String`
- `SeriesSupplement.pub token_id: String`
- `SpecialResolutionCall.pub arguments: Option<SpecialResolutionArguments>`
- `SpecialResolutionCall.pub calls: Option<Vec<SpecialResolutionCall>>`
- `SpecialResolutionCall.pub method: String`
- `SpecialResolutionCall.pub method_id: u32`
- `SpecialResolutionCall.pub module: String`
- `SpecialResolutionCall.pub module_id: u32`
- `SpecialResolutionData.pub calls: Vec<SpecialResolutionCall>`
- `SpecialResolutionData.pub description: Option<String>`
- `SpecialResolutionData.pub resolution_id: u64`
- `SymbolArguments.pub symbol: String`
- `TokenCreateData.pub carbon_token_id: u64`
- `TokenCreateData.pub decimals: u32`
- `TokenCreateData.pub is_non_fungible: bool`
- `TokenCreateData.pub max_supply: String`
- `TokenCreateData.pub metadata: BTreeMap<String, String>`
- `TokenCreateData.pub symbol: String`
- `TokenReferenceArguments.pub token: String`
- `TokenReferenceArguments.pub token_id: String`
- `TokenRepair.pub abi: String`
- `TokenRepair.pub repair_mask: String`
- `TokenRepair.pub script: String`
- `TokenRepair.pub symbol: String`
- `TokenRepair.pub token: String`
- `TokenRepair.pub token_flags: String`
- `TokenRepair.pub token_id: String`
- `TokenSeriesArguments.pub max_mint: String`
- `TokenSeriesArguments.pub max_supply: String`
- `TokenSeriesArguments.pub metadata: Option<BTreeMap<String, VmValue>>`
- `TokenSeriesArguments.pub metadata_raw: Option<String>`
- `TokenSeriesArguments.pub owner: String`
- `TokenSeriesArguments.pub series_id: Option<String>`
- `TokenSeriesArguments.pub token: String`
- `TokenSeriesArguments.pub token_id: String`
- `TokenSeriesCreateData.pub carbon_series_id: u32`
- `TokenSeriesCreateData.pub carbon_token_id: u64`
- `TokenSeriesCreateData.pub max_mint: u32`
- `TokenSeriesCreateData.pub max_supply: u32`
- `TokenSeriesCreateData.pub metadata: BTreeMap<String, String>`
- `TokenSeriesCreateData.pub owner: String`
- `TokenSeriesCreateData.pub series_id: String`
- `TokenSeriesCreateData.pub symbol: String`
- `TokenSeriesReferenceArguments.pub series_id: String`
- `TokenSeriesReferenceArguments.pub token: String`
- `TokenSeriesReferenceArguments.pub token_id: String`
- `TokensConfigArguments.pub flags: String`
- `TokensConfigArguments.pub flags_names: Vec<String>`
- `TransferFungibleArguments.pub amount: String`
- `TransferFungibleArguments.pub from: String`
- `TransferFungibleArguments.pub to: String`
- `TransferFungibleArguments.pub token: String`
- `TransferFungibleArguments.pub token_id: String`
- `TransferNonFungibleArguments.pub from: String`
- `TransferNonFungibleArguments.pub instance_ids: Vec<String>`
- `TransferNonFungibleArguments.pub to: String`
- `TransferNonFungibleArguments.pub token: String`
- `TransferNonFungibleArguments.pub token_id: String`
- `UpdateSeriesMetadataArguments.pub metadata: String`
- `UpdateSeriesMetadataArguments.pub series_id: String`
- `UpdateSeriesMetadataArguments.pub token: String`
- `UpdateSeriesMetadataArguments.pub token_id: String`
- `UpdateTokenMetadataArguments.pub metadata: Option<BTreeMap<String, VmValue>>`
- `UpdateTokenMetadataArguments.pub token: String`
- `UpdateTokenMetadataArguments.pub token_id: String`

### Methods

```rust
impl EventData: pub fn as_market_order(&self) -> Option<&MarketOrderData>
```

```rust
impl EventData: pub fn as_special_resolution(&self) -> Option<&SpecialResolutionData>
```

```rust
impl EventData: pub fn as_token_create(&self) -> Option<&TokenCreateData>
```

```rust
impl EventData: pub fn as_token_series_create(&self) -> Option<&TokenSeriesCreateData>
```

```rust
impl EventData: pub fn as_unknown(&self) -> Option<&Value>
```

```rust
impl SpecialResolutionArguments: pub fn as_raw(&self) -> Option<&RawArguments>
```

```rust
impl SpecialResolutionArguments: pub fn as_unrecognized(&self) -> Option<&Value>
```

### Variants

- `EventData::MarketOrder(MarketOrderData)`
- `EventData::SpecialResolution(SpecialResolutionData)`
- `EventData::TokenCreate(TokenCreateData)`
- `EventData::TokenSeriesCreate(TokenSeriesCreateData)`
- `EventData::Unknown(Value)`
- `SpecialResolutionArguments::Address(AddressArguments)`
- `SpecialResolutionArguments::Balance(BalanceArguments)`
- `SpecialResolutionArguments::BurnFungible(BurnFungibleArguments)`
- `SpecialResolutionArguments::BurnNonFungible(BurnNonFungibleArguments)`
- `SpecialResolutionArguments::ChainConfig(ChainConfigArguments)`
- `SpecialResolutionArguments::CreateMintedTokenSeries(CreateMintedTokenSeriesArguments)`
- `SpecialResolutionArguments::CreateToken(CreateTokenArguments)`
- `SpecialResolutionArguments::DeployContract(DeployContractArguments)`
- `SpecialResolutionArguments::ExecuteScript(ExecuteScriptArguments)`
- `SpecialResolutionArguments::GasConfig(Box<GasConfigArguments>)`
- `SpecialResolutionArguments::ImportContracts(ImportContractsArguments)`
- `SpecialResolutionArguments::Metadata(MetadataArguments)`
- `SpecialResolutionArguments::MintFungible(MintFungibleArguments)`
- `SpecialResolutionArguments::MintNonFungible(MintNonFungibleArguments)`
- `SpecialResolutionArguments::MintPhantasmaNonFungible(MintPhantasmaNonFungibleArguments)`
- `SpecialResolutionArguments::Name(NameArguments)`
- `SpecialResolutionArguments::NestedResolution(NestedResolutionArguments)`
- `SpecialResolutionArguments::NodeConfig(NodeConfigArguments)`
- `SpecialResolutionArguments::NonFungibleInfo(NonFungibleInfoArguments)`
- `SpecialResolutionArguments::NonFungibleInfoByRomId(NonFungibleInfoByRomIdArguments)`
- `SpecialResolutionArguments::PhantasmaVmConfig(PhantasmaVmConfigArguments)`
- `SpecialResolutionArguments::Raw(RawArguments)`
- `SpecialResolutionArguments::RegisterName(RegisterNameArguments)`
- `SpecialResolutionArguments::RegisterTokenContract(RegisterTokenContractArguments)`
- `SpecialResolutionArguments::RepairSeries(RepairSeriesArguments)`
- `SpecialResolutionArguments::RepairToken(RepairTokenArguments)`
- `SpecialResolutionArguments::SeriesInfoByMetaId(SeriesInfoByMetaIdArguments)`
- `SpecialResolutionArguments::Symbol(SymbolArguments)`
- `SpecialResolutionArguments::TokenReference(TokenReferenceArguments)`
- `SpecialResolutionArguments::TokenSeries(TokenSeriesArguments)`
- `SpecialResolutionArguments::TokenSeriesReference(TokenSeriesReferenceArguments)`
- `SpecialResolutionArguments::TokensConfig(TokensConfigArguments)`
- `SpecialResolutionArguments::TransferFungible(TransferFungibleArguments)`
- `SpecialResolutionArguments::TransferNonFungible(TransferNonFungibleArguments)`
- `SpecialResolutionArguments::Unrecognized(Value)`
- `SpecialResolutionArguments::UpdateSeriesMetadata(UpdateSeriesMetadataArguments)`
- `SpecialResolutionArguments::UpdateTokenMetadata(UpdateTokenMetadataArguments)`

## phantasma_sdk::fees

Source: `src/fees.rs`

### Declarations

```rust
pub const GAS_MODEL_V2_UNITS_PER_BLOCK_DATA_BYTE: u64 = 25
```

```rust
pub const KCAL_DECIMALS: u32 = 10
```

```rust
pub const NATIVE_SIGNATURE_BYTES: u32 = 64
```

```rust
pub const SOUL_DECIMALS: u32 = 8
```

```rust
pub const STORAGE_QUANTUM_BYTES: u32 = 1024
```

```rust
pub const WITNESS_ARRAY_ENTRY_BYTES: u32 = 96
```

```rust
pub enum NativeFeeKind
```

```rust
pub struct BurnedInstance
```

```rust
pub struct FeePlan
```

```rust
pub struct FeePlanOptions
```

```rust
pub struct FeePlanSummary
```

```rust
pub struct FeeQuote
```

```rust
pub struct InfusedAsset
```

```rust
pub struct NativeFeeEstimate
```

```rust
pub struct NativeFeeParams
```

```rust
pub struct NativeFeePart
```

```rust
pub struct NativeFeeTransactionParams
```

```rust
pub struct PlanAndSignOptions
```

### Fields

- `BurnedInstance.pub instance_id: u64`
- `BurnedInstance.pub token_id: u64`
- `FeePlan.pub deleted_storage_quanta: u32`
- `FeePlan.pub envelope_bytes: u32`
- `FeePlan.pub exact: bool`
- `FeePlan.pub expected_gas_bill: u64`
- `FeePlan.pub kinds: Vec<NativeFeeKind>`
- `FeePlan.pub max_data: u64`
- `FeePlan.pub max_gas: u64`
- `FeePlan.pub new_storage_quanta: u32`
- `FeePlanOptions.pub big_fungible: Option<bool>`
- `FeePlanOptions.pub duplicated_series: Option<bool>`
- `FeePlanOptions.pub infusions: Option<Vec<InfusedAsset>>`
- `FeePlanOptions.pub recipient_holds_token: bool`
- `FeePlanOptions.pub rom_has_meta_id: Option<bool>`
- `FeePlanOptions.pub script_event_bytes: Option<u32>`
- `FeePlanOptions.pub script_storage_quanta: Option<u32>`
- `FeePlanOptions.pub script_units_allowance: Option<u64>`
- `FeePlanOptions.pub series_has_meta_id: Option<bool>`
- `FeePlanOptions.pub supply_row_exists: bool`
- `FeePlanOptions.pub token_burned_before: bool`
- `FeePlanOptions.pub witness_count: Option<u32>`
- `FeePlanSummary.pub gas_bill: String`
- `FeePlanSummary.pub gas_offer: String`
- `FeePlanSummary.pub storage_ceiling: String`
- `FeeQuote.pub expected_gas_bill: u64`
- `FeeQuote.pub max_data: u64`
- `FeeQuote.pub max_gas: u64`
- `InfusedAsset.pub burner_holds_token: bool`
- `InfusedAsset.pub instance_count: Option<u32>`
- `InfusedAsset.pub non_fungible: bool`
- `InfusedAsset.pub token_id: Option<u64>`
- `NativeFeeEstimate.pub deleted_storage_quanta: u32`
- `NativeFeeEstimate.pub expected_gas_bill: u64`
- `NativeFeeEstimate.pub max_data: u64`
- `NativeFeeEstimate.pub max_gas: u64`
- `NativeFeeEstimate.pub new_storage_quanta: u32`
- `NativeFeeParams.pub big_fungible: Option<bool>`
- `NativeFeeParams.pub count: Option<u32>`
- `NativeFeeParams.pub distinct_series_count: Option<u32>`
- `NativeFeeParams.pub duplicated_series: Option<bool>`
- `NativeFeeParams.pub envelope_bytes: u32`
- `NativeFeeParams.pub has_inflation_schedule: bool`
- `NativeFeeParams.pub has_pre_burn: bool`
- `NativeFeeParams.pub has_staking_organisation: bool`
- `NativeFeeParams.pub has_staking_reward_token: bool`
- `NativeFeeParams.pub infusions: Option<Vec<InfusedAsset>>`
- `NativeFeeParams.pub name_length: u32`
- `NativeFeeParams.pub non_fungible: bool`
- `NativeFeeParams.pub payload_bytes: u32`
- `NativeFeeParams.pub ram_bytes: Vec<u32>`
- `NativeFeeParams.pub recipient_holds_token: bool`
- `NativeFeeParams.pub rom_bytes: Vec<u32>`
- `NativeFeeParams.pub rom_has_meta_id: Option<bool>`
- `NativeFeeParams.pub script_event_bytes: Option<u32>`
- `NativeFeeParams.pub script_storage_quanta: Option<u32>`
- `NativeFeeParams.pub script_units_allowance: Option<u64>`
- `NativeFeeParams.pub series_has_meta_id: Option<bool>`
- `NativeFeeParams.pub series_info_bytes: u32`
- `NativeFeeParams.pub supply_row_exists: bool`
- `NativeFeeParams.pub symbol_length: u32`
- `NativeFeeParams.pub to_is_nft_address: bool`
- `NativeFeeParams.pub token_burned_before: bool`
- `NativeFeeParams.pub token_id: Option<u64>`
- `NativeFeeParams.pub token_info_bytes: u32`
- `NativeFeePart.pub kind: NativeFeeKind`
- `NativeFeePart.pub params: NativeFeeParams`
- `NativeFeeTransactionParams.pub envelope_bytes: u32`
- `NativeFeeTransactionParams.pub payload_bytes: u32`
- `PlanAndSignOptions.pub facts: FeePlanOptions`
- `PlanAndSignOptions.pub limits: TxLimits`

### Methods

```rust
impl FeePlan: pub fn apply(&self, msg: &TxMsg) -> TxMsg
```

```rust
impl FeePlan: pub fn quote(&self) -> FeeQuote
```

```rust
impl NativeFeeEstimate: pub fn quote(&self) -> FeeQuote
```

```rust
pub fn burned_instances(msg: &TxMsg) -> Vec<BurnedInstance>
```

```rust
pub fn envelope_bytes_for( kind: NativeFeeKind, serialized_message_length: u32, witness_count: u32, ) -> u32
```

```rust
pub fn estimate_native_fee( kind: NativeFeeKind, config: &GasConfig, params: &NativeFeeParams, ) -> Result<NativeFeeEstimate>
```

```rust
pub fn estimate_native_fee_batch( parts: &[NativeFeePart], config: &GasConfig, transaction: NativeFeeTransactionParams, ) -> Result<NativeFeeEstimate>
```

```rust
pub fn phantasma_canonical_rom_bytes(public_rom_bytes: u32) -> u32
```

```rust
pub fn plan_and_sign_with_keys( msg: &TxMsg, keys: &[&PhantasmaKeys], config: Option<&GasConfig>, options: &PlanAndSignOptions, ) -> Result<Vec<u8>>
```

```rust
pub fn plan_fees(msg: &TxMsg, config: &GasConfig, options: &FeePlanOptions) -> Result<FeePlan>
```

```rust
pub fn storage_quanta_for(row_bytes: u32) -> u32
```

```rust
pub fn summarize_fee_plan(plan: &FeePlan) -> FeePlanSummary
```

```rust
pub fn summarize_fee_plan_with_decimals( plan: &FeePlan, gas_decimals: u32, data_decimals: u32, ) -> FeePlanSummary
```

### Variants

- `NativeFeeKind::BurnFungible`
- `NativeFeeKind::BurnNonFungible`
- `NativeFeeKind::CreateToken`
- `NativeFeeKind::CreateTokenSeries`
- `NativeFeeKind::MintFungible`
- `NativeFeeKind::MintNonFungible`
- `NativeFeeKind::MintPhantasmaNonFungible`
- `NativeFeeKind::RegisterName`
- `NativeFeeKind::Script`
- `NativeFeeKind::TransferFungible`
- `NativeFeeKind::TransferNonFungible`

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
pub mod extended_events
```

```rust
pub mod fees
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
pub use extended_events::*
```

```rust
pub use fees::*
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
pub const ADDRESS_TYPE_CARBON: &str = "Carbon"
```

```rust
pub const API_KEY_HEADER: &str = "X-Api-Key"
```

```rust
pub const DEFAULT_FEE_CONFIG_TTL: Duration = Duration::from_secs(60)
```

```rust
pub const DEFAULT_MAX_RPC_RESPONSE_BYTES: usize = 16 * 1024 * 1024
```

```rust
pub enum PreflightVerdict
```

```rust
pub enum VmValue
```

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
pub struct AccountInfoResult
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
pub struct ChainFeeParams
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
pub struct EstimateTransactionResult
```

```rust
pub struct EventExResult
```

```rust
pub struct EventResult
```

```rust
pub struct FeePlanner<'a, T>
```

```rust
pub struct GasConfigDataResult
```

```rust
pub struct GasConfigResult
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
pub struct OrganizationMemberResult
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
pub struct PlanRequestOptions
```

```rust
pub struct PlatformResult
```

```rust
pub struct PreflightResult
```

```rust
pub struct ReceiptResult
```

```rust
pub struct ReqwestTransport
```

```rust
pub struct RpcCallResult<T>
```

```rust
pub struct ScriptResult
```

```rust
pub struct SendTransactionOptions
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
- `AccountInfoResult.pub address: String`
- `AccountInfoResult.pub name: String`
- `AccountInfoResult.pub stake: StakeResult`
- `AccountResult.pub address: String`
- `AccountResult.pub balances: Vec<BalanceResult>`
- `AccountResult.pub name: String`
- `AccountResult.pub relay: Option<String>`
- `AccountResult.pub stake: String`
- `AccountResult.pub stakes: StakeResult`
- `AccountResult.pub storage: StorageResult`
- `AccountResult.pub txs: Option<Vec<String>>`
- `AccountResult.pub unclaimed: String`
- `AccountResult.pub validator: String`
- `AddressTransactionsResult.pub address: String`
- `AddressTransactionsResult.pub txs: Vec<TransactionResult>`
- `ArchiveResult.pub block_count: u64`
- `ArchiveResult.pub encryption: Option<String>`
- `ArchiveResult.pub hash: Option<String>`
- `ArchiveResult.pub missing_blocks: Option<Vec<u64>>`
- `ArchiveResult.pub name: Option<String>`
- `ArchiveResult.pub owners: Option<Vec<String>>`
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
- `BalanceResult.pub ids: Option<Vec<String>>`
- `BalanceResult.pub symbol: String`
- `BlockResult.pub chain_address: String`
- `BlockResult.pub events: Option<Vec<EventResult>>`
- `BlockResult.pub hash: String`
- `BlockResult.pub height: u64`
- `BlockResult.pub oracles: Option<Vec<OracleResult>>`
- `BlockResult.pub previous_hash: String`
- `BlockResult.pub producer_address: Option<String>`
- `BlockResult.pub protocol: u32`
- `BlockResult.pub reward: String`
- `BlockResult.pub timestamp: u64`
- `BlockResult.pub txs: Vec<TransactionResult>`
- `BlockResult.pub validator_address: String`
- `BuildInfoResult.pub build_time_utc: String`
- `BuildInfoResult.pub commit: String`
- `BuildInfoResult.pub version: String`
- `ChainFeeParams.pub block_rate_target: Duration`
- `ChainFeeParams.pub expiry_window: Duration`
- `ChainFeeParams.pub gas_model_version: u32`
- `ChainResult.pub address: Option<String>`
- `ChainResult.pub contracts: Option<Vec<String>>`
- `ChainResult.pub dapps: Option<Vec<String>>`
- `ChainResult.pub height: u64`
- `ChainResult.pub name: Option<String>`
- `ChainResult.pub organization: Option<String>`
- `ChainResult.pub parent: Option<String>`
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
- `ContractResult.pub events: Option<Vec<AbiEventResult>>`
- `ContractResult.pub methods: Option<Vec<AbiMethodResult>>`
- `ContractResult.pub name: String`
- `ContractResult.pub owner: Option<String>`
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
- `CursorPaginatedResult.pub cursor: Option<String>`
- `CursorPaginatedResult.pub result: Option<T>`
- `DappResult.pub address: String`
- `DappResult.pub chain: String`
- `DappResult.pub name: String`
- `EstimateTransactionResult.pub abort_reason: String`
- `EstimateTransactionResult.pub data_escrow_atoms: Option<String>`
- `EstimateTransactionResult.pub data_refund_atoms: Option<String>`
- `EstimateTransactionResult.pub data_rows: Option<String>`
- `EstimateTransactionResult.pub gas_bill_kcal_base: Option<String>`
- `EstimateTransactionResult.pub recommended_max_data: Option<String>`
- `EstimateTransactionResult.pub recommended_max_gas: Option<String>`
- `EstimateTransactionResult.pub would_abort: bool`
- `EventExResult.pub address: String`
- `EventExResult.pub contract: String`
- `EventExResult.pub data: EventData`
- `EventExResult.pub kind: String`
- `EventResult.pub address: String`
- `EventResult.pub contract: String`
- `EventResult.pub data: String`
- `EventResult.pub kind: String`
- `EventResult.pub name: String`
- `GasConfigDataResult.pub data_escrow_per_row: Option<String>`
- `GasConfigDataResult.pub data_token_id: Option<String>`
- `GasConfigDataResult.pub fee_multiplier: Option<String>`
- `GasConfigDataResult.pub fee_shift: u8`
- `GasConfigDataResult.pub gas_burn_ratio_mul: Option<String>`
- `GasConfigDataResult.pub gas_burn_ratio_shift: u8`
- `GasConfigDataResult.pub gas_dapp_ratio_mul: Option<String>`
- `GasConfigDataResult.pub gas_dapp_ratio_shift: Option<u8>`
- `GasConfigDataResult.pub gas_fee_create_token_base: Option<String>`
- `GasConfigDataResult.pub gas_fee_create_token_series: Option<String>`
- `GasConfigDataResult.pub gas_fee_create_token_symbol: Option<String>`
- `GasConfigDataResult.pub gas_fee_per_byte: Option<String>`
- `GasConfigDataResult.pub gas_fee_query: Option<String>`
- `GasConfigDataResult.pub gas_fee_register_name: Option<String>`
- `GasConfigDataResult.pub gas_fee_transfer: Option<String>`
- `GasConfigDataResult.pub gas_producer_ratio_mul: Option<String>`
- `GasConfigDataResult.pub gas_producer_ratio_shift: Option<u8>`
- `GasConfigDataResult.pub gas_token_id: Option<String>`
- `GasConfigDataResult.pub legacy_data_escrow_per_row: Option<String>`
- `GasConfigDataResult.pub max_name_length: u8`
- `GasConfigDataResult.pub max_structure_size: u32`
- `GasConfigDataResult.pub max_token_symbol_length: u8`
- `GasConfigDataResult.pub minimum_gas_bill: Option<String>`
- `GasConfigDataResult.pub minimum_gas_offer: Option<String>`
- `GasConfigDataResult.pub policy_fee_create_token_base: Option<String>`
- `GasConfigDataResult.pub policy_fee_create_token_series: Option<String>`
- `GasConfigDataResult.pub policy_fee_create_token_symbol: Option<String>`
- `GasConfigDataResult.pub policy_fee_register_name: Option<String>`
- `GasConfigDataResult.pub version: u8`
- `GasConfigResult.pub block_rate_target: u32`
- `GasConfigResult.pub expiry_window: u32`
- `GasConfigResult.pub gas_config: Option<GasConfigDataResult>`
- `GasConfigResult.pub gas_model_version: u32`
- `GasConfigResult.pub units_per_block_data_byte: Option<u32>`
- `GovernanceResult.pub name: String`
- `GovernanceResult.pub value: String`
- `InteropResult.pub external: String`
- `InteropResult.pub local: String`
- `LeaderboardResult.pub name: Option<String>`
- `LeaderboardResult.pub rows: Option<Vec<LeaderboardRowResult>>`
- `LeaderboardRowResult.pub address: String`
- `LeaderboardRowResult.pub value: String`
- `NexusResult.pub chains: Option<Vec<ChainResult>>`
- `NexusResult.pub governance: Option<Vec<GovernanceResult>>`
- `NexusResult.pub name: Option<String>`
- `NexusResult.pub organizations: Option<Vec<String>>`
- `NexusResult.pub platforms: Option<Vec<PlatformResult>>`
- `NexusResult.pub protocol: u32`
- `NexusResult.pub tokens: Option<Vec<TokenResult>>`
- `NftResult.pub carbon_nft_address: String`
- `NftResult.pub carbon_series_id: String`
- `NftResult.pub carbon_token_id: String`
- `NftResult.pub chain_name: String`
- `NftResult.pub creator_address: String`
- `NftResult.pub id: String`
- `NftResult.pub infusion: Vec<TokenPropertyResult>`
- `NftResult.pub mint: String`
- `NftResult.pub owner_address: String`
- `NftResult.pub properties: Vec<TokenPropertyResult>`
- `NftResult.pub ram: String`
- `NftResult.pub rom: String`
- `NftResult.pub series: String`
- `NftResult.pub status: String`
- `OracleResult.pub content: String`
- `OracleResult.pub url: String`
- `OrganizationMemberResult.pub address: Option<String>`
- `OrganizationMemberResult.pub carbon_address: Option<String>`
- `OrganizationMemberResult.pub is_member: bool`
- `OrganizationMemberResult.pub member_time: Option<u64>`
- `OrganizationResult.pub carbon_owner: Option<String>`
- `OrganizationResult.pub member_count: Option<String>`
- `OrganizationResult.pub metadata: Vec<TokenPropertyResult>`
- `OrganizationResult.pub name: Option<String>`
- `OrganizationResult.pub owner: Option<String>`
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
- `PlanRequestOptions.pub facts: FeePlanOptions`
- `PlanRequestOptions.pub refresh_config: bool`
- `PlatformResult.pub chain: String`
- `PlatformResult.pub fuel: String`
- `PlatformResult.pub interop: Vec<InteropResult>`
- `PlatformResult.pub platform: String`
- `PlatformResult.pub tokens: Vec<String>`
- `PreflightResult.pub reason: String`
- `PreflightResult.pub subject: String`
- `PreflightResult.pub verdict: PreflightVerdict`
- `ReceiptResult.pub channel: String`
- `ReceiptResult.pub index: String`
- `ReceiptResult.pub nexus: String`
- `ReceiptResult.pub receiver: String`
- `ReceiptResult.pub script: String`
- `ReceiptResult.pub sender: String`
- `ReceiptResult.pub timestamp: u64`
- `RpcCallResult.pub canonical_envelope_bytes: usize`
- `RpcCallResult.pub canonical_result_bytes: usize`
- `RpcCallResult.pub endpoint: String`
- `RpcCallResult.pub http_status: u16`
- `RpcCallResult.pub method: String`
- `RpcCallResult.pub raw_envelope: Value`
- `RpcCallResult.pub raw_result: Value`
- `RpcCallResult.pub value: T`
- `ScriptResult.pub error: Option<String>`
- `ScriptResult.pub events: Vec<EventResult>`
- `ScriptResult.pub gas: Option<String>`
- `ScriptResult.pub oracles: Vec<OracleResult>`
- `ScriptResult.pub result: String`
- `ScriptResult.pub results: Vec<String>`
- `ScriptResult.pub state: Option<String>`
- `SendTransactionOptions.pub plan: PlanRequestOptions`
- `SendTransactionOptions.pub skip_preflight: bool`
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
- `TokenPropertyResult.pub value: VmValue`
- `TokenResult.pub address: String`
- `TokenResult.pub burned_supply: String`
- `TokenResult.pub carbon_id: String`
- `TokenResult.pub current_supply: String`
- `TokenResult.pub decimals: u32`
- `TokenResult.pub external: Option<Vec<TokenExternalResult>>`
- `TokenResult.pub flags: String`
- `TokenResult.pub max_supply: String`
- `TokenResult.pub metadata: Option<Vec<TokenPropertyResult>>`
- `TokenResult.pub name: String`
- `TokenResult.pub owner: String`
- `TokenResult.pub price: Option<Vec<TokenPriceResult>>`
- `TokenResult.pub script: Option<String>`
- `TokenResult.pub series: Vec<TokenSeriesResult>`
- `TokenResult.pub symbol: String`
- `TokenResult.pub token_schemas: Option<TokenSchemasResult>`
- `TokenSchemasResult.pub ram: VmStructSchemaResult`
- `TokenSchemasResult.pub rom: VmStructSchemaResult`
- `TokenSchemasResult.pub series_metadata: VmStructSchemaResult`
- `TokenSeriesResult.pub burned_supply: Option<String>`
- `TokenSeriesResult.pub carbon_series_id: String`
- `TokenSeriesResult.pub carbon_token_id: String`
- `TokenSeriesResult.pub current_supply: String`
- `TokenSeriesResult.pub max_mint: String`
- `TokenSeriesResult.pub max_supply: String`
- `TokenSeriesResult.pub metadata: Vec<TokenPropertyResult>`
- `TokenSeriesResult.pub methods: Option<Vec<AbiMethodResult>>`
- `TokenSeriesResult.pub mint_count: String`
- `TokenSeriesResult.pub mode: Option<String>`
- `TokenSeriesResult.pub owner_address: String`
- `TokenSeriesResult.pub script: Option<String>`
- `TokenSeriesResult.pub series_id: String`
- `TransactionResult.pub block_hash: String`
- `TransactionResult.pub block_height: u64`
- `TransactionResult.pub carbon_tx_data: String`
- `TransactionResult.pub carbon_tx_type: u32`
- `TransactionResult.pub chain_address: String`
- `TransactionResult.pub debug_comment: Option<String>`
- `TransactionResult.pub events: Vec<EventResult>`
- `TransactionResult.pub expiration: u64`
- `TransactionResult.pub extended_events: Vec<EventExResult>`
- `TransactionResult.pub fee: String`
- `TransactionResult.pub gas_limit: String`
- `TransactionResult.pub gas_payer: String`
- `TransactionResult.pub gas_price: String`
- `TransactionResult.pub gas_target: String`
- `TransactionResult.pub hash: String`
- `TransactionResult.pub payload: String`
- `TransactionResult.pub result: String`
- `TransactionResult.pub script: String`
- `TransactionResult.pub sender: String`
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
impl EstimateTransactionResult: pub fn to_fee_quote(&self) -> Result<FeeQuote>
```

```rust
impl FeePlanner<'_, T>: pub async fn chain_params(&self, refresh: bool) -> Result<ChainFeeParams>
```

```rust
impl FeePlanner<'_, T>: pub async fn config(&self, refresh: bool) -> Result<GasConfig>
```

```rust
impl FeePlanner<'_, T>: pub async fn plan(&self, msg: &TxMsg, options: &PlanRequestOptions) -> Result<FeePlan>
```

```rust
impl FeePlanner<'_, T>: pub fn invalidate(&self)
```

```rust
impl FeePlanner<'_, T>: pub fn plan_with(
```

```rust
impl GasConfigResult: pub fn to_gas_config(&self) -> Result<GasConfig>
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
impl PhantasmaRpc<ReqwestTransport>: pub fn with_api_key(mut self, api_key: impl Into<String>) -> Self
```

```rust
impl PhantasmaRpc<ReqwestTransport>: pub fn with_max_response_bytes(mut self, max_response_bytes: usize) -> Self
```

```rust
impl PhantasmaRpc<T>: pub async fn call<R: DeserializeOwned>(&self, method: &str, params: Vec<Value>) -> Result<R>
```

```rust
impl PhantasmaRpc<T>: pub async fn call_value(&self, method: &str, params: Vec<Value>) -> Result<Value>
```

```rust
impl PhantasmaRpc<T>: pub async fn call_value_with_raw(
```

```rust
impl PhantasmaRpc<T>: pub async fn call_with_raw<R: DeserializeOwned>(
```

```rust
impl PhantasmaRpc<T>: pub async fn control_token_id(&self) -> Result<u64>
```

```rust
impl PhantasmaRpc<T>: pub async fn estimate_transaction(&self, tx_data: &str) -> Result<EstimateTransactionResult>
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
impl PhantasmaRpc<T>: pub async fn get_account_info(&self, address: &str) -> Result<AccountInfoResult>
```

```rust
impl PhantasmaRpc<T>: pub async fn get_account_info_with_address_type(
```

```rust
impl PhantasmaRpc<T>: pub async fn get_account_infos<S: AsRef<str> + Sync>(
```

```rust
impl PhantasmaRpc<T>: pub async fn get_account_infos_with_address_type<S: AsRef<str> + Sync>(
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
impl PhantasmaRpc<T>: pub async fn get_block_by_hash_with_raw(
```

```rust
impl PhantasmaRpc<T>: pub async fn get_block_by_height(&self, chain: &str, height: u64) -> Result<BlockResult>
```

```rust
impl PhantasmaRpc<T>: pub async fn get_block_by_height_with_raw(
```

```rust
impl PhantasmaRpc<T>: pub async fn get_block_height(&self, chain: &str) -> Result<u64>
```

```rust
impl PhantasmaRpc<T>: pub async fn get_block_height_with_raw(&self, chain: &str) -> Result<RpcCallResult<u64>>
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
impl PhantasmaRpc<T>: pub async fn get_gas_config(&self) -> Result<GasConfigResult>
```

```rust
impl PhantasmaRpc<T>: pub async fn get_latest_block(&self, chain: &str) -> Result<BlockResult>
```

```rust
impl PhantasmaRpc<T>: pub async fn get_latest_block_with_raw(
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
impl PhantasmaRpc<T>: pub async fn get_organization_member(
```

```rust
impl PhantasmaRpc<T>: pub async fn get_organization_members(
```

```rust
impl PhantasmaRpc<T>: pub async fn get_organizations(
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
impl PhantasmaRpc<T>: pub async fn get_transaction_by_block_hash_and_index_with_raw(
```

```rust
impl PhantasmaRpc<T>: pub async fn get_transaction_with_raw(
```

```rust
impl PhantasmaRpc<T>: pub async fn get_version(&self) -> Result<VersionResult>
```

```rust
impl PhantasmaRpc<T>: pub async fn infused_assets(
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
impl PhantasmaRpc<T>: pub async fn preflight_transaction(&self, msg: &TxMsg) -> Result<PreflightResult>
```

```rust
impl PhantasmaRpc<T>: pub async fn read_archive(&self, hash: &str, block_index: u32) -> Result<String>
```

```rust
impl PhantasmaRpc<T>: pub async fn send_carbon_transaction(&self, tx: &[u8]) -> Result<String>
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
impl PhantasmaRpc<T>: pub async fn send_tx_msg(
```

```rust
impl PhantasmaRpc<T>: pub async fn sign_and_send_built_transaction(
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
impl PhantasmaRpc<T>: pub fn fees(&self) -> FeePlanner<'_, T>
```

```rust
impl PhantasmaRpc<T>: pub fn parse_create_token_result(&self, result_hex: &str) -> Result<u64>
```

```rust
impl PhantasmaRpc<T>: pub fn parse_create_token_series_result(&self, result_hex: &str) -> Result<u32>
```

```rust
impl PhantasmaRpc<T>: pub fn with_fee_config_ttl(mut self, ttl: Duration) -> Self
```

```rust
impl PhantasmaRpc<T>: pub fn with_timeout(mut self, timeout: Duration) -> Self
```

```rust
impl PhantasmaRpc<T>: pub fn with_transport(endpoint: impl Into<String>, transport: T) -> Self
```

```rust
impl ReqwestTransport: pub fn with_api_key(mut self, api_key: impl Into<String>) -> Self
```

```rust
impl RpcCallResult<T>: pub fn map_value<U>(self, value: U) -> RpcCallResult<U>
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
impl VmValue: pub fn as_fields(&self) -> Option<&BTreeMap<String, VmValue>>
```

```rust
impl VmValue: pub fn as_items(&self) -> Option<&[VmValue]>
```

```rust
impl VmValue: pub fn as_text(&self) -> Option<&str>
```

```rust
impl VmValue: pub fn field(&self, name: &str) -> Option<&VmValue>
```

```rust
impl VmValue: pub fn is_text(&self) -> bool
```

```rust
impl VmValue: pub fn text(value: impl Into<String>) -> Self
```

```rust
pub fn convert_decimals(amount: &str, decimals: u32) -> String
```

```rust
pub fn parse_json_rpc_response(status: u16, body: Value) -> Result<Value>
```

```rust
pub fn parse_json_rpc_response_for_request( status: u16, body: Value, expected_request_id: u64, ) -> Result<Value>
```

### Variants

- `PreflightVerdict::Free`
- `PreflightVerdict::NotApplicable`
- `PreflightVerdict::Taken`
- `PreflightVerdict::Unknown`
- `VmValue::Fields(BTreeMap<String, VmValue>)`
- `VmValue::Items(Vec<VmValue>)`
- `VmValue::Text(String)`

## phantasma_sdk::transaction

Source: `src/transaction.rs`

### Declarations

```rust
pub const SDK_PAYLOAD: &[u8] = concat!("RS-SDK-v", env!("CARGO_PKG_VERSION")).as_bytes()
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
