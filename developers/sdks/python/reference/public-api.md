# Python SDK Public API Inventory

This page lists public classes, methods, functions, enum values, fields, and
constants from the cited source baseline. Use it to check exact names when
working with lower-level SDK APIs.

Source baseline:

| Item | Value |
| ---- | ----- |
| Source repo | `phantasma-sdk-py` |
| Source commit | `559fd95ed1267b214a92a958283fceacb0c9d029` |
| Scope | public module members under `src/phantasma_py` |

## phantasma_py

Source: `src/phantasma_py/__init__.py`

### Fields

- `__all__`
- `__version__`

## phantasma_py.binary

Source: `src/phantasma_py/binary.py`

### Declarations

```python
class BinaryWriter
```

```python
class BinaryReader
```

### Fields

- `MAX_ARRAY_SIZE`

### Methods

```python
BinaryReader.assert_eof(self) -> None
```

```python
BinaryReader.read(self, count: int) -> bytes
```

```python
BinaryReader.read_big_integer(self) -> int
```

```python
BinaryReader.read_bool(self) -> bool
```

```python
BinaryReader.read_i64_le(self) -> int
```

```python
BinaryReader.read_string(self) -> str
```

```python
BinaryReader.read_u16_le(self) -> int
```

```python
BinaryReader.read_u32_le(self) -> int
```

```python
BinaryReader.read_u64_le(self) -> int
```

```python
BinaryReader.read_u8(self) -> int
```

```python
BinaryReader.read_var_bytes(self, *, max_size: int = MAX_ARRAY_SIZE) -> bytes
```

```python
BinaryReader.read_var_uint(self) -> int
```

```python
BinaryReader.remaining(self) -> int
```

```python
BinaryWriter.bytes(self) -> bytes
```

```python
BinaryWriter.write(self, data: bytes) -> None
```

```python
BinaryWriter.write_big_integer(self, value: int) -> None
```

```python
BinaryWriter.write_bool(self, value: bool) -> None
```

```python
BinaryWriter.write_i64_le(self, value: int) -> None
```

```python
BinaryWriter.write_string(self, value: str) -> None
```

```python
BinaryWriter.write_u16_le(self, value: int) -> None
```

```python
BinaryWriter.write_u32_le(self, value: int) -> None
```

```python
BinaryWriter.write_u64_le(self, value: int) -> None
```

```python
BinaryWriter.write_u8(self, value: int) -> None
```

```python
BinaryWriter.write_var_bytes(self, data: bytes) -> None
```

```python
BinaryWriter.write_var_uint(self, value: int) -> None
```

```python
def big_int_to_vm_bytes(value: int) -> bytes
```

```python
def vm_bytes_to_big_int(data: bytes) -> int
```

## phantasma_py.carbon

Source: `src/phantasma_py/carbon.py`

### Declarations

```python
class CarbonSerializable(Protocol)
```

```python
class FixedBytes(bytes)
```

```python
class Bytes16(FixedBytes)
```

```python
class Bytes32(FixedBytes)
```

```python
class Bytes64(FixedBytes)
```

```python
class SmallString
```

```python
class CarbonWriter
```

```python
class CarbonReader
```

```python
class IntX
```

```python
class TxType(IntEnum)
```

```python
class ModuleID(IntEnum)
```

```python
class TokenContractMethod(IntEnum)
```

```python
class TokenFlags(IntFlag)
```

```python
class TokensConfigFlags(IntFlag)
```

```python
class ListingType(IntEnum)
```

```python
class MarketContractMethod(IntEnum)
```

```python
class MarketConfigFlags(IntFlag)
```

```python
class VMType(IntEnum)
```

```python
class VMStructFlags(IntFlag)
```

```python
class VMVariableSchema
```

```python
class VMNamedVariableSchema
```

```python
class VMStructSchema
```

```python
class VMDynamicVariable
```

```python
class VMNamedDynamicVariable
```

```python
class VMDynamicStruct
```

```python
class VMStructArray
```

```python
class TokenSchemas
```

```python
class TokenSchemaField
```

```python
class TokenSchemasJSON
```

```python
class ChainConfig
```

```python
class GasConfig
```

```python
class TokensConfig
```

```python
class TokenInfo
```

```python
class SeriesInfo
```

```python
class NFTMintInfo
```

```python
class MintNonFungibleArgs
```

```python
class CreateTokenSeriesArgs
```

```python
class CreateMintedTokenSeriesArgs
```

```python
class PhantasmaNFTMintInfo
```

```python
class MintPhantasmaNonFungibleArgs
```

```python
class PhantasmaNFTMintResult
```

```python
class MintFungibleArgs
```

```python
class TransferFungibleArgs
```

```python
class TransferNonFungibleArgs
```

```python
class BurnFungibleArgs
```

```python
class BurnNonFungibleArgs
```

```python
class UpdateTokenMetadataArgs
```

```python
class UpdateSeriesMetadataArgs
```

```python
class TokenListing
```

```python
class MarketConfig
```

```python
class MarketSellTokenArgs
```

```python
class MarketSellTokenByIDArgs
```

```python
class MarketCancelSaleArgs
```

```python
class MarketCancelSaleByIDArgs
```

```python
class MarketBuyTokenArgs
```

```python
class MarketBuyTokenByIDArgs
```

```python
class MarketGetTokenListingCountArgs
```

```python
class MarketGetTokenListingInfoArgs
```

```python
class MarketGetTokenListingInfoByIDArgs
```

```python
class TxMsgCall
```

```python
class CallArgSection
```

```python
class MsgCallArgSections
```

```python
class TxMsgCallMulti
```

```python
class TxMsgSpecialResolution
```

```python
class TxMsgTransferFungible
```

```python
class TxMsgTransferFungibleGasPayer
```

```python
class TxMsgTransferNonFungibleSingle
```

```python
class TxMsgTransferNonFungibleSingleGasPayer
```

```python
class TxMsgTransferNonFungibleMulti
```

```python
class TxMsgTransferNonFungibleMultiGasPayer
```

```python
class TxMsgMintFungible
```

```python
class TxMsgBurnFungible
```

```python
class TxMsgBurnFungibleGasPayer
```

```python
class TxMsgMintNonFungible
```

```python
class TxMsgBurnNonFungible
```

```python
class TxMsgBurnNonFungibleGasPayer
```

```python
class TxMsgTrade
```

```python
class TxMsgPhantasma
```

```python
class TxMsgPhantasmaRaw
```

```python
class TxMsg
```

```python
class Witness
```

```python
class SignedTxMsg
```

```python
class FeeOptions
```

```python
class CreateTokenFeeOptions(FeeOptions)
```

```python
class CreateSeriesFeeOptions(FeeOptions)
```

```python
class MintNFTFeeOptions(FeeOptions)
```

### Fields

- `BurnFungibleArgs.amount: IntX`
- `BurnFungibleArgs.from_address: Bytes32`
- `BurnFungibleArgs.token_id: int`
- `BurnNonFungibleArgs.from_address: Bytes32`
- `BurnNonFungibleArgs.instance_ids: list[int]`
- `BurnNonFungibleArgs.token_id: int`
- `Bytes16.SIZE`
- `Bytes32.SIZE`
- `Bytes64.SIZE`
- `C`
- `CallArgSection.args: bytes`
- `CallArgSection.register_offset: int`
- `ChainConfig.allowed_tx_types: int`
- `ChainConfig.block_rate_target: int`
- `ChainConfig.expiry_window: int`
- `ChainConfig.reserved1: int`
- `ChainConfig.reserved2: int`
- `ChainConfig.reserved3: int`
- `ChainConfig.version: int`
- `CreateMintedTokenSeriesArgs.address: Bytes32`
- `CreateMintedTokenSeriesArgs.info: SeriesInfo`
- `CreateMintedTokenSeriesArgs.rams: list[bytes]`
- `CreateMintedTokenSeriesArgs.roms: list[bytes]`
- `CreateMintedTokenSeriesArgs.token_id: int`
- `CreateSeriesFeeOptions.fee_multiplier: int`
- `CreateSeriesFeeOptions.gas_fee_base: int`
- `CreateSeriesFeeOptions.gas_fee_create_series_base: int`
- `CreateTokenFeeOptions.fee_multiplier: int`
- `CreateTokenFeeOptions.gas_fee_base: int`
- `CreateTokenFeeOptions.gas_fee_create_token_base: int`
- `CreateTokenFeeOptions.gas_fee_create_token_symbol: int`
- `CreateTokenSeriesArgs.info: SeriesInfo`
- `CreateTokenSeriesArgs.token_id: int`
- `EMPTY_BYTES16`
- `EMPTY_BYTES32`
- `EMPTY_BYTES64`
- `FeeOptions.fee_multiplier: int`
- `FeeOptions.gas_fee_base: int`
- `FixedBytes.SIZE: ClassVar[int]`
- `GasConfig.data_escrow_per_row: int`
- `GasConfig.data_token_id: int`
- `GasConfig.fee_multiplier: int`
- `GasConfig.fee_shift: int`
- `GasConfig.gas_burn_ratio_mul: int`
- `GasConfig.gas_burn_ratio_shift: int`
- `GasConfig.gas_fee_create_token_base: int`
- `GasConfig.gas_fee_create_token_series: int`
- `GasConfig.gas_fee_create_token_symbol: int`
- `GasConfig.gas_fee_per_byte: int`
- `GasConfig.gas_fee_query: int`
- `GasConfig.gas_fee_register_name: int`
- `GasConfig.gas_fee_transfer: int`
- `GasConfig.gas_token_id: int`
- `GasConfig.max_name_length: int`
- `GasConfig.max_structure_size: int`
- `GasConfig.max_token_symbol_length: int`
- `GasConfig.minimum_gas_offer: int`
- `GasConfig.version: int`
- `IntX.value: int`
- `ListingType.FIXED_PRICE`
- `MARKET_DELISTING_GRACE_MS`
- `MARKET_MAXIMUM_LISTING_TIME_MS`
- `MARKET_MINIMUM_LISTING_TIME_MS`
- `MARKET_ROYALTY_HUNDRED_PERCENT`
- `MARKET_ROYALTY_ONE_PERCENT`
- `MarketBuyTokenArgs.from_address: Bytes32`
- `MarketBuyTokenArgs.instance_id: int`
- `MarketBuyTokenArgs.token_id: int`
- `MarketBuyTokenByIDArgs.from_address: Bytes32`
- `MarketBuyTokenByIDArgs.instance_id: VMDynamicVariable`
- `MarketBuyTokenByIDArgs.symbol: SmallString`
- `MarketCancelSaleArgs.instance_id: int`
- `MarketCancelSaleArgs.token_id: int`
- `MarketCancelSaleByIDArgs.instance_id: VMDynamicVariable`
- `MarketCancelSaleByIDArgs.symbol: SmallString`
- `MarketConfig.delisting_grace: int`
- `MarketConfig.flags: MarketConfigFlags`
- `MarketConfig.maximum_listing_time: int`
- `MarketConfig.minimum_listing_time: int`
- `MarketConfigFlags.CAN_CANCEL_EARLY`
- `MarketConfigFlags.CAN_PURCHASE_LATE`
- `MarketConfigFlags.ENFORCE_ROYALTIES`
- `MarketConfigFlags.NONE`
- `MarketConfigFlags.PRICE_REQUIRED`
- `MarketContractMethod.BUY_TOKEN`
- `MarketContractMethod.BUY_TOKEN_BY_ID`
- `MarketContractMethod.CANCEL_SALE`
- `MarketContractMethod.CANCEL_SALE_BY_ID`
- `MarketContractMethod.GET_TOKEN_LISTING_COUNT`
- `MarketContractMethod.GET_TOKEN_LISTING_INFO`
- `MarketContractMethod.GET_TOKEN_LISTING_INFO_BY_ID`
- `MarketContractMethod.SELL_TOKEN`
- `MarketContractMethod.SELL_TOKEN_BY_ID`
- `MarketGetTokenListingCountArgs.token_id: int`
- `MarketGetTokenListingInfoArgs.instance_id: int`
- `MarketGetTokenListingInfoArgs.token_id: int`
- `MarketGetTokenListingInfoByIDArgs.instance_id: VMDynamicVariable`
- `MarketGetTokenListingInfoByIDArgs.symbol: SmallString`
- `MarketSellTokenArgs.end_date: int`
- `MarketSellTokenArgs.from_address: Bytes32`
- `MarketSellTokenArgs.instance_id: int`
- `MarketSellTokenArgs.price: IntX`
- `MarketSellTokenArgs.quote_token_id: int`
- `MarketSellTokenArgs.token_id: int`
- `MarketSellTokenByIDArgs.end_date: int`
- `MarketSellTokenByIDArgs.from_address: Bytes32`
- `MarketSellTokenByIDArgs.instance_id: VMDynamicVariable`
- `MarketSellTokenByIDArgs.price: IntX`
- `MarketSellTokenByIDArgs.quote_symbol: SmallString`
- `MarketSellTokenByIDArgs.symbol: SmallString`
- `MintFungibleArgs.amount: IntX`
- `MintFungibleArgs.to: Bytes32`
- `MintFungibleArgs.token_id: int`
- `MintNonFungibleArgs.address: Bytes32`
- `MintNonFungibleArgs.token_id: int`
- `MintNonFungibleArgs.tokens: list[NFTMintInfo]`
- `MintPhantasmaNonFungibleArgs.address: Bytes32`
- `MintPhantasmaNonFungibleArgs.token_id: int`
- `MintPhantasmaNonFungibleArgs.tokens: list[PhantasmaNFTMintInfo]`
- `ModuleID.GOVERNANCE`
- `ModuleID.INTERNAL`
- `ModuleID.MARKET`
- `ModuleID.ORG`
- `ModuleID.PHANTASMA`
- `ModuleID.PHANTASMA_VM`
- `ModuleID.TOKEN`
- `MsgCallArgSections.sections: list[CallArgSection]`
- `NFTMintInfo.ram: bytes`
- `NFTMintInfo.rom: bytes`
- `NFTMintInfo.series_id: int`
- `PhantasmaNFTMintInfo.phantasma_series_id: IntX`
- `PhantasmaNFTMintInfo.ram: bytes`
- `PhantasmaNFTMintInfo.rom: bytes`
- `PhantasmaNFTMintResult.carbon_instance_id: int`
- `PhantasmaNFTMintResult.phantasma_nft_id: Bytes32`
- `STANDARD_META_ID`
- `SYSTEM_ADDRESS_DATA_POOL`
- `SYSTEM_ADDRESS_GAS_POOL`
- `SYSTEM_ADDRESS_NULL`
- `SchemaFieldInput`
- `SeriesInfo.max_mint: int`
- `SeriesInfo.max_supply: int`
- `SeriesInfo.metadata: bytes`
- `SeriesInfo.owner: Bytes32`
- `SeriesInfo.ram: VMStructSchema`
- `SeriesInfo.rom: VMStructSchema`
- `SignedTxMsg.msg: TxMsg`
- `SignedTxMsg.witnesses: list[Witness]`
- `SmallString.value: str`
- `TokenContractMethod.APPLY_INFLATION`
- `TokenContractMethod.BURN_FUNGIBLE`
- `TokenContractMethod.BURN_NON_FUNGIBLE`
- `TokenContractMethod.CREATE_MINTED_TOKEN_SERIES`
- `TokenContractMethod.CREATE_TOKEN`
- `TokenContractMethod.CREATE_TOKEN_SERIES`
- `TokenContractMethod.DELETE_TOKEN_SERIES`
- `TokenContractMethod.GET_BALANCE`
- `TokenContractMethod.GET_BALANCES`
- `TokenContractMethod.GET_INSTANCES`
- `TokenContractMethod.GET_NEXT_TOKEN_INFLATION`
- `TokenContractMethod.GET_NON_FUNGIBLE_INFO`
- `TokenContractMethod.GET_NON_FUNGIBLE_INFO_BY_ROM_ID`
- `TokenContractMethod.GET_SERIES_INFO`
- `TokenContractMethod.GET_SERIES_INFO_BY_META_ID`
- `TokenContractMethod.GET_SERIES_SUPPLY`
- `TokenContractMethod.GET_TOKEN_ID_BY_SYMBOL`
- `TokenContractMethod.GET_TOKEN_INFO`
- `TokenContractMethod.GET_TOKEN_INFO_BY_SYMBOL`
- `TokenContractMethod.GET_TOKEN_SUPPLY`
- `TokenContractMethod.MINT_FUNGIBLE`
- `TokenContractMethod.MINT_NON_FUNGIBLE`
- `TokenContractMethod.MINT_PHANTASMA_NON_FUNGIBLE`
- `TokenContractMethod.SET_TOKENS_CONFIG`
- `TokenContractMethod.TRANSFER_FUNGIBLE`
- `TokenContractMethod.TRANSFER_NON_FUNGIBLE`
- `TokenContractMethod.UPDATE_SERIES_METADATA`
- `TokenContractMethod.UPDATE_TOKEN_METADATA`
- `TokenFlags.BIG_FUNGIBLE`
- `TokenFlags.NONE`
- `TokenFlags.NON_FUNGIBLE`
- `TokenInfo.decimals: int`
- `TokenInfo.flags: TokenFlags`
- `TokenInfo.max_supply: IntX`
- `TokenInfo.metadata: bytes`
- `TokenInfo.owner: Bytes32`
- `TokenInfo.symbol: SmallString`
- `TokenInfo.token_schemas: bytes`
- `TokenListing.end_date: int`
- `TokenListing.price: IntX`
- `TokenListing.quote_token_id: int`
- `TokenListing.seller: Bytes32`
- `TokenListing.start_date: int`
- `TokenListing.type: ListingType`
- `TokenSchemaField.name: str`
- `TokenSchemaField.type: VMType`
- `TokenSchemas.ram: VMStructSchema`
- `TokenSchemas.rom: VMStructSchema`
- `TokenSchemas.series_metadata: VMStructSchema`
- `TokenSchemasJSON.ram: list[TokenSchemaField]`
- `TokenSchemasJSON.rom: list[TokenSchemaField]`
- `TokenSchemasJSON.series_metadata: list[TokenSchemaField]`
- `TokensConfig.flags: TokensConfigFlags`
- `TokensConfigFlags.ALLOW_EXPLICIT_NFT_META_ID_MINT`
- `TokensConfigFlags.NONE`
- `TokensConfigFlags.REQUIRE_METADATA`
- `TokensConfigFlags.REQUIRE_NFT_META_ID`
- `TokensConfigFlags.REQUIRE_NFT_STANDARD`
- `TokensConfigFlags.REQUIRE_SYMBOL`
- `TransferFungibleArgs.amount: IntX`
- `TransferFungibleArgs.from_address: Bytes32`
- `TransferFungibleArgs.to: Bytes32`
- `TransferFungibleArgs.token_id: int`
- `TransferNonFungibleArgs.from_address: Bytes32`
- `TransferNonFungibleArgs.instance_ids: list[int]`
- `TransferNonFungibleArgs.to: Bytes32`
- `TransferNonFungibleArgs.token_id: int`
- `TxMsg.expiry: int`
- `TxMsg.gas_from: Bytes32`
- `TxMsg.max_data: int`
- `TxMsg.max_gas: int`
- `TxMsg.msg: TxPayload`
- `TxMsg.payload: SmallString`
- `TxMsg.type: TxType`
- `TxMsgBurnFungible.amount: IntX`
- `TxMsgBurnFungible.token_id: int`
- `TxMsgBurnFungibleGasPayer.amount: IntX`
- `TxMsgBurnFungibleGasPayer.from_address: Bytes32`
- `TxMsgBurnFungibleGasPayer.token_id: int`
- `TxMsgBurnNonFungible.instance_id: int`
- `TxMsgBurnNonFungible.token_id: int`
- `TxMsgBurnNonFungibleGasPayer.from_address: Bytes32`
- `TxMsgBurnNonFungibleGasPayer.instance_id: int`
- `TxMsgBurnNonFungibleGasPayer.token_id: int`
- `TxMsgCall.args: bytes`
- `TxMsgCall.method_id: int`
- `TxMsgCall.module_id: int`
- `TxMsgCall.sections: MsgCallArgSections | None`
- `TxMsgCallMulti.calls: list[TxMsgCall]`
- `TxMsgMintFungible.amount: IntX`
- `TxMsgMintFungible.to: Bytes32`
- `TxMsgMintFungible.token_id: int`
- `TxMsgMintNonFungible.ram: bytes`
- `TxMsgMintNonFungible.rom: bytes`
- `TxMsgMintNonFungible.series_id: int`
- `TxMsgMintNonFungible.to: Bytes32`
- `TxMsgMintNonFungible.token_id: int`
- `TxMsgPhantasma.chain: SmallString`
- `TxMsgPhantasma.nexus: SmallString`
- `TxMsgPhantasma.script: bytes`
- `TxMsgPhantasmaRaw.transaction: bytes`
- `TxMsgSpecialResolution.calls: list[TxMsgCall]`
- `TxMsgSpecialResolution.resolution_id: int`
- `TxMsgTrade.burn_f: list[TxMsgBurnFungibleGasPayer]`
- `TxMsgTrade.burn_n: list[TxMsgBurnNonFungibleGasPayer]`
- `TxMsgTrade.mint_f: list[TxMsgMintFungible]`
- `TxMsgTrade.mint_n: list[TxMsgMintNonFungible]`
- `TxMsgTrade.transfer_f: list[TxMsgTransferFungibleGasPayer]`
- `TxMsgTrade.transfer_n: list[TxMsgTransferNonFungibleSingleGasPayer]`
- `TxMsgTransferFungible.amount: int`
- `TxMsgTransferFungible.to: Bytes32`
- `TxMsgTransferFungible.token_id: int`
- `TxMsgTransferFungibleGasPayer.amount: int`
- `TxMsgTransferFungibleGasPayer.from_address: Bytes32`
- `TxMsgTransferFungibleGasPayer.to: Bytes32`
- `TxMsgTransferFungibleGasPayer.token_id: int`
- `TxMsgTransferNonFungibleMulti.instance_ids: list[int]`
- `TxMsgTransferNonFungibleMulti.to: Bytes32`
- `TxMsgTransferNonFungibleMulti.token_id: int`
- `TxMsgTransferNonFungibleMultiGasPayer.from_address: Bytes32`
- `TxMsgTransferNonFungibleMultiGasPayer.instance_ids: list[int]`
- `TxMsgTransferNonFungibleMultiGasPayer.to: Bytes32`
- `TxMsgTransferNonFungibleMultiGasPayer.token_id: int`
- `TxMsgTransferNonFungibleSingle.instance_id: int`
- `TxMsgTransferNonFungibleSingle.to: Bytes32`
- `TxMsgTransferNonFungibleSingle.token_id: int`
- `TxMsgTransferNonFungibleSingleGasPayer.from_address: Bytes32`
- `TxMsgTransferNonFungibleSingleGasPayer.instance_id: int`
- `TxMsgTransferNonFungibleSingleGasPayer.to: Bytes32`
- `TxMsgTransferNonFungibleSingleGasPayer.token_id: int`
- `TxPayload`
- `TxType.BURN_FUNGIBLE`
- `TxType.BURN_FUNGIBLE_GAS_PAYER`
- `TxType.BURN_NON_FUNGIBLE`
- `TxType.BURN_NON_FUNGIBLE_GAS_PAYER`
- `TxType.CALL`
- `TxType.CALL_MULTI`
- `TxType.MINT_FUNGIBLE`
- `TxType.MINT_NON_FUNGIBLE`
- `TxType.PHANTASMA`
- `TxType.PHANTASMA_RAW`
- `TxType.TRADE`
- `TxType.TRANSFER_FUNGIBLE`
- `TxType.TRANSFER_FUNGIBLE_GAS_PAYER`
- `TxType.TRANSFER_NON_FUNGIBLE_MULTI`
- `TxType.TRANSFER_NON_FUNGIBLE_MULTI_GAS_PAYER`
- `TxType.TRANSFER_NON_FUNGIBLE_SINGLE`
- `TxType.TRANSFER_NON_FUNGIBLE_SINGLE_GAS_PAYER`
- `UpdateSeriesMetadataArgs.metadata: bytes`
- `UpdateSeriesMetadataArgs.series_id: int`
- `UpdateSeriesMetadataArgs.token_id: int`
- `UpdateTokenMetadataArgs.metadata: VMDynamicStruct`
- `UpdateTokenMetadataArgs.token_id: int`
- `VMDynamicStruct.fields: list[VMNamedDynamicVariable]`
- `VMDynamicVariable.data: Any`
- `VMDynamicVariable.type: VMType`
- `VMNamedDynamicVariable.name: SmallString`
- `VMNamedDynamicVariable.value: VMDynamicVariable`
- `VMNamedVariableSchema.name: SmallString`
- `VMNamedVariableSchema.schema: VMVariableSchema`
- `VMStructArray.schema: VMStructSchema`
- `VMStructArray.structs: list[VMDynamicStruct]`
- `VMStructFlags.DYNAMIC_EXTRAS`
- `VMStructFlags.IS_SORTED`
- `VMStructFlags.NONE`
- `VMStructSchema.fields: list[VMNamedVariableSchema]`
- `VMStructSchema.flags: VMStructFlags`
- `VMType.ARRAY`
- `VMType.ARRAY_BYTES`
- `VMType.ARRAY_BYTES16`
- `VMType.ARRAY_BYTES32`
- `VMType.ARRAY_BYTES64`
- `VMType.ARRAY_DYNAMIC`
- `VMType.ARRAY_INT16`
- `VMType.ARRAY_INT256`
- `VMType.ARRAY_INT32`
- `VMType.ARRAY_INT64`
- `VMType.ARRAY_INT8`
- `VMType.ARRAY_STRING`
- `VMType.ARRAY_STRUCT`
- `VMType.BYTES`
- `VMType.BYTES16`
- `VMType.BYTES32`
- `VMType.BYTES64`
- `VMType.DYNAMIC`
- `VMType.INT16`
- `VMType.INT256`
- `VMType.INT32`
- `VMType.INT64`
- `VMType.INT8`
- `VMType.STRING`
- `VMType.STRUCT`
- `VMVariableSchema.struct_def: VMStructSchema | None`
- `VMVariableSchema.type: VMType`
- `Witness.address: Bytes32`
- `Witness.signature: Bytes64`

### Methods

```python
BurnFungibleArgs.read_carbon(cls, reader: CarbonReader) -> BurnFungibleArgs
```

```python
BurnFungibleArgs.write_carbon(self, writer: CarbonWriter) -> None
```

```python
BurnNonFungibleArgs.read_carbon(cls, reader: CarbonReader) -> BurnNonFungibleArgs
```

```python
BurnNonFungibleArgs.write_carbon(self, writer: CarbonWriter) -> None
```

```python
CallArgSection.read_carbon(cls, reader: CarbonReader) -> CallArgSection
```

```python
CallArgSection.write_carbon(self, writer: CarbonWriter) -> None
```

```python
CarbonReader.__init__(self, data: bytes) -> None
```

```python
CarbonReader.assert_eof(self) -> None
```

```python
CarbonReader.read(self, count: int) -> bytes
```

```python
CarbonReader.read1(self) -> int
```

```python
CarbonReader.read16(self) -> Bytes16
```

```python
CarbonReader.read2(self) -> int
```

```python
CarbonReader.read32(self) -> Bytes32
```

```python
CarbonReader.read4(self) -> int
```

```python
CarbonReader.read4u(self) -> int
```

```python
CarbonReader.read64(self) -> Bytes64
```

```python
CarbonReader.read8(self) -> int
```

```python
CarbonReader.read8u(self) -> int
```

```python
CarbonReader.read_big_int(self) -> int
```

```python
CarbonReader.read_big_int_array(self) -> list[int]
```

```python
CarbonReader.read_big_int_with_header(self, header: int | None) -> int
```

```python
CarbonReader.read_byte_array(self) -> bytes
```

```python
CarbonReader.read_byte_arrays(self) -> list[bytes]
```

```python
CarbonReader.read_int_array(self, width: int, *, signed: bool) -> list[int]
```

```python
CarbonReader.read_length(self) -> int
```

```python
CarbonReader.read_string_z(self) -> str
```

```python
CarbonReader.read_string_z_array(self) -> list[str]
```

```python
CarbonReader.remaining(self) -> int
```

```python
CarbonSerializable.read_carbon(cls, reader: CarbonReader) -> Self
```

```python
CarbonSerializable.write_carbon(self, writer: CarbonWriter) -> None
```

```python
CarbonWriter.__init__(self) -> None
```

```python
CarbonWriter.bytes(self) -> bytes
```

```python
CarbonWriter.write(self, data: bytes) -> None
```

```python
CarbonWriter.write1(self, value: int) -> None
```

```python
CarbonWriter.write16(self, value: Bytes16 | bytes) -> None
```

```python
CarbonWriter.write2(self, value: int) -> None
```

```python
CarbonWriter.write32(self, value: Bytes32 | bytes) -> None
```

```python
CarbonWriter.write4(self, value: int) -> None
```

```python
CarbonWriter.write4u(self, value: int) -> None
```

```python
CarbonWriter.write64(self, value: Bytes64 | bytes) -> None
```

```python
CarbonWriter.write8(self, value: int) -> None
```

```python
CarbonWriter.write8u(self, value: int) -> None
```

```python
CarbonWriter.write_big_int(self, value: int) -> None
```

```python
CarbonWriter.write_big_int_array(self, values: list[int]) -> None
```

```python
CarbonWriter.write_byte_array(self, data: bytes) -> None
```

```python
CarbonWriter.write_byte_arrays(self, values: list[bytes]) -> None
```

```python
CarbonWriter.write_int_array(self, values: list[int], width: int, *, signed: bool) -> None
```

```python
CarbonWriter.write_string_z(self, value: str) -> None
```

```python
CarbonWriter.write_string_z_array(self, values: list[str]) -> None
```

```python
ChainConfig.read_carbon(cls, reader: CarbonReader) -> ChainConfig
```

```python
ChainConfig.write_carbon(self, writer: CarbonWriter) -> None
```

```python
CreateMintedTokenSeriesArgs.read_carbon(cls, reader: CarbonReader) -> CreateMintedTokenSeriesArgs
```

```python
CreateMintedTokenSeriesArgs.write_carbon(self, writer: CarbonWriter) -> None
```

```python
CreateSeriesFeeOptions.calculate_max_gas(self, count: int = 1) -> int
```

```python
CreateTokenFeeOptions.calculate_max_gas_for_symbol(self, symbol: SmallString) -> int
```

```python
CreateTokenSeriesArgs.read_carbon(cls, reader: CarbonReader) -> CreateTokenSeriesArgs
```

```python
CreateTokenSeriesArgs.write_carbon(self, writer: CarbonWriter) -> None
```

```python
FeeOptions.calculate_max_gas(self, count: int = 1) -> int
```

```python
FixedBytes.__new__(cls, value: bytes | bytearray | str = b'') -> Self
```

```python
FixedBytes.__str__(self) -> str
```

```python
FixedBytes.from_hex(cls, value: str) -> Self
```

```python
GasConfig.read_carbon(cls, reader: CarbonReader) -> GasConfig
```

```python
GasConfig.write_carbon(self, writer: CarbonWriter) -> None
```

```python
IntX.__str__(self) -> str
```

```python
IntX.is_8_byte_safe(self) -> bool
```

```python
IntX.read_carbon(cls, reader: CarbonReader) -> IntX
```

```python
IntX.write_carbon(self, writer: CarbonWriter) -> None
```

```python
MarketBuyTokenArgs.read_carbon(cls, reader: CarbonReader) -> MarketBuyTokenArgs
```

```python
MarketBuyTokenArgs.write_carbon(self, writer: CarbonWriter) -> None
```

```python
MarketBuyTokenByIDArgs.read_carbon(cls, reader: CarbonReader) -> MarketBuyTokenByIDArgs
```

```python
MarketBuyTokenByIDArgs.write_carbon(self, writer: CarbonWriter) -> None
```

```python
MarketCancelSaleArgs.read_carbon(cls, reader: CarbonReader) -> MarketCancelSaleArgs
```

```python
MarketCancelSaleArgs.write_carbon(self, writer: CarbonWriter) -> None
```

```python
MarketCancelSaleByIDArgs.read_carbon(cls, reader: CarbonReader) -> MarketCancelSaleByIDArgs
```

```python
MarketCancelSaleByIDArgs.write_carbon(self, writer: CarbonWriter) -> None
```

```python
MarketConfig.read_carbon(cls, reader: CarbonReader) -> MarketConfig
```

```python
MarketConfig.write_carbon(self, writer: CarbonWriter) -> None
```

```python
MarketGetTokenListingCountArgs.read_carbon(cls, reader: CarbonReader) -> MarketGetTokenListingCountArgs
```

```python
MarketGetTokenListingCountArgs.write_carbon(self, writer: CarbonWriter) -> None
```

```python
MarketGetTokenListingInfoArgs.read_carbon(cls, reader: CarbonReader) -> MarketGetTokenListingInfoArgs
```

```python
MarketGetTokenListingInfoArgs.write_carbon(self, writer: CarbonWriter) -> None
```

```python
MarketGetTokenListingInfoByIDArgs.read_carbon(cls, reader: CarbonReader) -> MarketGetTokenListingInfoByIDArgs
```

```python
MarketGetTokenListingInfoByIDArgs.write_carbon(self, writer: CarbonWriter) -> None
```

```python
MarketSellTokenArgs.read_carbon(cls, reader: CarbonReader) -> MarketSellTokenArgs
```

```python
MarketSellTokenArgs.write_carbon(self, writer: CarbonWriter) -> None
```

```python
MarketSellTokenByIDArgs.read_carbon(cls, reader: CarbonReader) -> MarketSellTokenByIDArgs
```

```python
MarketSellTokenByIDArgs.write_carbon(self, writer: CarbonWriter) -> None
```

```python
MintFungibleArgs.read_carbon(cls, reader: CarbonReader) -> MintFungibleArgs
```

```python
MintFungibleArgs.write_carbon(self, writer: CarbonWriter) -> None
```

```python
MintNFTFeeOptions.calculate_max_gas(self, count_or_tokens: int | Sequence[Any] = 1) -> int
```

```python
MintNonFungibleArgs.read_carbon(cls, reader: CarbonReader) -> MintNonFungibleArgs
```

```python
MintNonFungibleArgs.write_carbon(self, writer: CarbonWriter) -> None
```

```python
MintPhantasmaNonFungibleArgs.read_carbon(cls, reader: CarbonReader) -> MintPhantasmaNonFungibleArgs
```

```python
MintPhantasmaNonFungibleArgs.write_carbon(self, writer: CarbonWriter) -> None
```

```python
MsgCallArgSections.has_sections(self) -> bool
```

```python
MsgCallArgSections.read_with_count(cls, reader: CarbonReader, count_negative: int) -> MsgCallArgSections
```

```python
MsgCallArgSections.write_carbon(self, writer: CarbonWriter) -> None
```

```python
NFTMintInfo.read_carbon(cls, reader: CarbonReader) -> NFTMintInfo
```

```python
NFTMintInfo.write_carbon(self, writer: CarbonWriter) -> None
```

```python
PhantasmaNFTMintInfo.read_carbon(cls, reader: CarbonReader) -> PhantasmaNFTMintInfo
```

```python
PhantasmaNFTMintInfo.write_carbon(self, writer: CarbonWriter) -> None
```

```python
PhantasmaNFTMintResult.read_carbon(cls, reader: CarbonReader) -> PhantasmaNFTMintResult
```

```python
PhantasmaNFTMintResult.write_carbon(self, writer: CarbonWriter) -> None
```

```python
SeriesInfo.read_carbon(cls, reader: CarbonReader) -> SeriesInfo
```

```python
SeriesInfo.write_carbon(self, writer: CarbonWriter) -> None
```

```python
SignedTxMsg.read_carbon(cls, reader: CarbonReader) -> SignedTxMsg
```

```python
SignedTxMsg.write_carbon(self, writer: CarbonWriter) -> None
```

```python
SmallString.__post_init__(self) -> None
```

```python
SmallString.__str__(self) -> str
```

```python
SmallString.read_carbon(cls, reader: CarbonReader) -> SmallString
```

```python
SmallString.write_carbon(self, writer: CarbonWriter) -> None
```

```python
TokenInfo.read_carbon(cls, reader: CarbonReader) -> TokenInfo
```

```python
TokenInfo.write_carbon(self, writer: CarbonWriter) -> None
```

```python
TokenListing.read_carbon(cls, reader: CarbonReader) -> TokenListing
```

```python
TokenListing.write_carbon(self, writer: CarbonWriter) -> None
```

```python
TokenSchemas.read_carbon(cls, reader: CarbonReader) -> TokenSchemas
```

```python
TokenSchemas.write_carbon(self, writer: CarbonWriter) -> None
```

```python
TokensConfig.read_carbon(cls, reader: CarbonReader) -> TokensConfig
```

```python
TokensConfig.write_carbon(self, writer: CarbonWriter) -> None
```

```python
TransferFungibleArgs.read_carbon(cls, reader: CarbonReader) -> TransferFungibleArgs
```

```python
TransferFungibleArgs.write_carbon(self, writer: CarbonWriter) -> None
```

```python
TransferNonFungibleArgs.read_carbon(cls, reader: CarbonReader) -> TransferNonFungibleArgs
```

```python
TransferNonFungibleArgs.write_carbon(self, writer: CarbonWriter) -> None
```

```python
TxMsg.read_carbon(cls, reader: CarbonReader) -> TxMsg
```

```python
TxMsg.write_carbon(self, writer: CarbonWriter) -> None
```

```python
TxMsgBurnFungible.read_carbon(cls, reader: CarbonReader) -> TxMsgBurnFungible
```

```python
TxMsgBurnFungible.write_carbon(self, writer: CarbonWriter) -> None
```

```python
TxMsgBurnFungibleGasPayer.read_carbon(cls, reader: CarbonReader) -> TxMsgBurnFungibleGasPayer
```

```python
TxMsgBurnFungibleGasPayer.write_carbon(self, writer: CarbonWriter) -> None
```

```python
TxMsgBurnNonFungible.read_carbon(cls, reader: CarbonReader) -> TxMsgBurnNonFungible
```

```python
TxMsgBurnNonFungible.write_carbon(self, writer: CarbonWriter) -> None
```

```python
TxMsgBurnNonFungibleGasPayer.read_carbon(cls, reader: CarbonReader) -> TxMsgBurnNonFungibleGasPayer
```

```python
TxMsgBurnNonFungibleGasPayer.write_carbon(self, writer: CarbonWriter) -> None
```

```python
TxMsgCall.read_carbon(cls, reader: CarbonReader) -> TxMsgCall
```

```python
TxMsgCall.write_carbon(self, writer: CarbonWriter) -> None
```

```python
TxMsgCallMulti.read_carbon(cls, reader: CarbonReader) -> TxMsgCallMulti
```

```python
TxMsgCallMulti.write_carbon(self, writer: CarbonWriter) -> None
```

```python
TxMsgMintFungible.read_carbon(cls, reader: CarbonReader) -> TxMsgMintFungible
```

```python
TxMsgMintFungible.write_carbon(self, writer: CarbonWriter) -> None
```

```python
TxMsgMintNonFungible.read_carbon(cls, reader: CarbonReader) -> TxMsgMintNonFungible
```

```python
TxMsgMintNonFungible.write_carbon(self, writer: CarbonWriter) -> None
```

```python
TxMsgPhantasma.read_carbon(cls, reader: CarbonReader) -> TxMsgPhantasma
```

```python
TxMsgPhantasma.write_carbon(self, writer: CarbonWriter) -> None
```

```python
TxMsgPhantasmaRaw.read_carbon(cls, reader: CarbonReader) -> TxMsgPhantasmaRaw
```

```python
TxMsgPhantasmaRaw.write_carbon(self, writer: CarbonWriter) -> None
```

```python
TxMsgSpecialResolution.read_carbon(cls, reader: CarbonReader) -> TxMsgSpecialResolution
```

```python
TxMsgSpecialResolution.write_carbon(self, writer: CarbonWriter) -> None
```

```python
TxMsgTrade.read_carbon(cls, reader: CarbonReader) -> TxMsgTrade
```

```python
TxMsgTrade.write_carbon(self, writer: CarbonWriter) -> None
```

```python
TxMsgTransferFungible.read_carbon(cls, reader: CarbonReader) -> TxMsgTransferFungible
```

```python
TxMsgTransferFungible.write_carbon(self, writer: CarbonWriter) -> None
```

```python
TxMsgTransferFungibleGasPayer.read_carbon(cls, reader: CarbonReader) -> TxMsgTransferFungibleGasPayer
```

```python
TxMsgTransferFungibleGasPayer.write_carbon(self, writer: CarbonWriter) -> None
```

```python
TxMsgTransferNonFungibleMulti.read_carbon(cls, reader: CarbonReader) -> TxMsgTransferNonFungibleMulti
```

```python
TxMsgTransferNonFungibleMulti.write_carbon(self, writer: CarbonWriter) -> None
```

```python
TxMsgTransferNonFungibleMultiGasPayer.read_carbon(cls, reader: CarbonReader) -> TxMsgTransferNonFungibleMultiGasPayer
```

```python
TxMsgTransferNonFungibleMultiGasPayer.write_carbon(self, writer: CarbonWriter) -> None
```

```python
TxMsgTransferNonFungibleSingle.read_carbon(cls, reader: CarbonReader) -> TxMsgTransferNonFungibleSingle
```

```python
TxMsgTransferNonFungibleSingle.write_carbon(self, writer: CarbonWriter) -> None
```

```python
TxMsgTransferNonFungibleSingleGasPayer.read_carbon(cls, reader: CarbonReader) -> TxMsgTransferNonFungibleSingleGasPayer
```

```python
TxMsgTransferNonFungibleSingleGasPayer.write_carbon(self, writer: CarbonWriter) -> None
```

```python
UpdateSeriesMetadataArgs.read_carbon(cls, reader: CarbonReader) -> UpdateSeriesMetadataArgs
```

```python
UpdateSeriesMetadataArgs.write_carbon(self, writer: CarbonWriter) -> None
```

```python
UpdateTokenMetadataArgs.read_carbon(cls, reader: CarbonReader) -> UpdateTokenMetadataArgs
```

```python
UpdateTokenMetadataArgs.write_carbon(self, writer: CarbonWriter) -> None
```

```python
VMDynamicStruct.get(self, name: str) -> VMDynamicVariable | None
```

```python
VMDynamicStruct.read_carbon(cls, reader: CarbonReader) -> VMDynamicStruct
```

```python
VMDynamicStruct.read_with_schema(cls, schema: VMStructSchema | None, reader: CarbonReader) -> VMDynamicStruct
```

```python
VMDynamicStruct.write_carbon(self, writer: CarbonWriter) -> None
```

```python
VMDynamicStruct.write_with_schema(self, schema: VMStructSchema | None, writer: CarbonWriter) -> bool
```

```python
VMDynamicVariable.read_carbon(cls, reader: CarbonReader) -> VMDynamicVariable
```

```python
VMDynamicVariable.read_static(self, vm_type: VMType, schema: VMStructSchema | None, reader: CarbonReader) -> None
```

```python
VMDynamicVariable.write_carbon(self, writer: CarbonWriter) -> None
```

```python
VMDynamicVariable.write_static(self, vm_type: VMType, schema: VMStructSchema | None, writer: CarbonWriter) -> bool
```

```python
VMNamedDynamicVariable.make(cls, name: str, vm_type: VMType, value: Any) -> VMNamedDynamicVariable
```

```python
VMNamedDynamicVariable.read_carbon(cls, reader: CarbonReader) -> VMNamedDynamicVariable
```

```python
VMNamedDynamicVariable.write_carbon(self, writer: CarbonWriter) -> None
```

```python
VMNamedVariableSchema.make(cls, name: str, vm_type: VMType, struct_def: VMStructSchema | None = None) -> VMNamedVariableSchema
```

```python
VMNamedVariableSchema.read_carbon(cls, reader: CarbonReader) -> VMNamedVariableSchema
```

```python
VMNamedVariableSchema.write_carbon(self, writer: CarbonWriter) -> None
```

```python
VMStructSchema.read_carbon(cls, reader: CarbonReader) -> VMStructSchema
```

```python
VMStructSchema.write_carbon(self, writer: CarbonWriter) -> None
```

```python
VMVariableSchema.read_carbon(cls, reader: CarbonReader) -> VMVariableSchema
```

```python
VMVariableSchema.write_carbon(self, writer: CarbonWriter) -> None
```

```python
Witness.read_carbon(cls, reader: CarbonReader) -> Witness
```

```python
Witness.write_carbon(self, writer: CarbonWriter) -> None
```

```python
def build_and_serialize_token_schemas(schemas: TokenSchemas | None = None) -> bytes
```

```python
def build_create_token_series_tx(token_id: int, series_info: SeriesInfo, creator: Bytes32, fees: CreateSeriesFeeOptions | None = None, max_data: int = 100000000, expiry: int = 0) -> TxMsg
```

```python
def build_create_token_series_tx_and_sign(token_id: int, series_info: SeriesInfo, signer: PhantasmaKeys, fees: CreateSeriesFeeOptions | None = None, max_data: int = 100000000, expiry: int = 0) -> bytes
```

```python
def build_create_token_series_tx_and_sign_hex(token_id: int, series_info: SeriesInfo, signer: PhantasmaKeys, fees: CreateSeriesFeeOptions | None = None, max_data: int = 100000000, expiry: int = 0) -> str
```

```python
def build_create_token_tx(token_info: TokenInfo, creator: Bytes32, fees: CreateTokenFeeOptions | None = None, max_data: int = 100000000, expiry: int = 0) -> TxMsg
```

```python
def build_create_token_tx_and_sign(token_info: TokenInfo, signer: PhantasmaKeys, fees: CreateTokenFeeOptions | None = None, max_data: int = 100000000, expiry: int = 0) -> bytes
```

```python
def build_create_token_tx_and_sign_hex(token_info: TokenInfo, signer: PhantasmaKeys, fees: CreateTokenFeeOptions | None = None, max_data: int = 100000000, expiry: int = 0) -> str
```

```python
def build_mint_non_fungible_tx(token_id: int, series_id: int, sender: Bytes32, receiver: Bytes32, rom: bytes, ram: bytes = b'', fees: MintNFTFeeOptions | None = None, max_data: int = 100000000, expiry: int = 0) -> TxMsg
```

```python
def build_mint_non_fungible_tx_and_sign(token_id: int, series_id: int, signer: PhantasmaKeys, receiver: Bytes32, rom: bytes, ram: bytes = b'', fees: MintNFTFeeOptions | None = None, max_data: int = 100000000, expiry: int = 0) -> bytes
```

```python
def build_mint_non_fungible_tx_and_sign_hex(token_id: int, series_id: int, signer: PhantasmaKeys, receiver: Bytes32, rom: bytes, ram: bytes = b'', fees: MintNFTFeeOptions | None = None, max_data: int = 100000000, expiry: int = 0) -> str
```

```python
def build_mint_phantasma_non_fungible_single_tx(token_id: int, phantasma_series_id: int, sender: Bytes32, receiver: Bytes32, public_rom: bytes, ram: bytes = b'', fees: MintNFTFeeOptions | None = None, max_data: int = 100000000, expiry: int = 0) -> TxMsg
```

```python
def build_mint_phantasma_non_fungible_single_tx_and_sign(token_id: int, phantasma_series_id: int, signer: PhantasmaKeys, receiver: Bytes32, public_rom: bytes, ram: bytes = b'', fees: MintNFTFeeOptions | None = None, max_data: int = 100000000, expiry: int = 0) -> bytes
```

```python
def build_mint_phantasma_non_fungible_single_tx_and_sign_hex(token_id: int, phantasma_series_id: int, signer: PhantasmaKeys, receiver: Bytes32, public_rom: bytes, ram: bytes = b'', fees: MintNFTFeeOptions | None = None, max_data: int = 100000000, expiry: int = 0) -> str
```

```python
def build_mint_phantasma_non_fungible_tx(token_id: int, sender: Bytes32, receiver: Bytes32, tokens: Sequence[PhantasmaNFTMintInfo], fees: MintNFTFeeOptions | None = None, max_data: int = 100000000, expiry: int = 0) -> TxMsg
```

```python
def build_mint_phantasma_non_fungible_tx_and_sign(token_id: int, signer: PhantasmaKeys, receiver: Bytes32, tokens: Sequence[PhantasmaNFTMintInfo], fees: MintNFTFeeOptions | None = None, max_data: int = 100000000, expiry: int = 0) -> bytes
```

```python
def build_mint_phantasma_non_fungible_tx_and_sign_hex(token_id: int, signer: PhantasmaKeys, receiver: Bytes32, tokens: Sequence[PhantasmaNFTMintInfo], fees: MintNFTFeeOptions | None = None, max_data: int = 100000000, expiry: int = 0) -> str
```

```python
def build_nft_rom(schema: VMStructSchema, phantasma_nft_id: int, metadata: list[tuple[str, Any]]) -> bytes
```

```python
def build_phantasma_nft_public_mint_schema(nft_rom_schema: VMStructSchema) -> VMStructSchema
```

```python
def build_phantasma_nft_rom(nft_rom_schema: VMStructSchema, metadata: list[tuple[str, Any]]) -> bytes
```

```python
def build_series_info(phantasma_series_id: int, max_mint: int, max_supply: int, owner: Bytes32) -> SeriesInfo
```

```python
def build_token_info(symbol: str, max_supply: IntX, *, is_nft: bool, decimals: int, owner: Bytes32, metadata: bytes, token_schemas: bytes = b'') -> TokenInfo
```

```python
def build_token_metadata(fields: dict[str, str]) -> bytes
```

```python
def build_token_schemas_from_fields(series_metadata: Sequence[SchemaFieldInput], rom: Sequence[SchemaFieldInput], ram: Sequence[SchemaFieldInput]) -> TokenSchemas
```

```python
def build_token_series_metadata(schema: VMStructSchema, phantasma_series_id: int, metadata: list[tuple[str, Any]]) -> bytes
```

```python
def bytes32_from_phantasma_address(address: Address) -> Bytes32
```

```python
def bytes32_from_phantasma_address_text(text: str) -> Bytes32
```

```python
def bytes32_from_public_key(public_key: bytes) -> Bytes32
```

```python
def check_token_symbol(symbol: str) -> None
```

```python
def default_market_config() -> MarketConfig
```

```python
def deserialize(data: bytes, cls: type[CarbonSerializable]) -> CarbonSerializable
```

```python
def get_nft_address(carbon_token_id: int, instance_id: int) -> Bytes32
```

```python
def now_unix_millis() -> int
```

```python
def parse_create_token_result(result_hex: str) -> int
```

```python
def parse_create_token_series_result(result_hex: str) -> int
```

```python
def parse_mint_non_fungible_result(carbon_token_id: int, result_hex: str) -> list[Bytes32]
```

```python
def parse_mint_phantasma_non_fungible_result(result_hex: str) -> list[PhantasmaNFTMintResult]
```

```python
def parse_token_schemas_json(data: str) -> TokenSchemasJSON
```

```python
def prepare_standard_token_schemas(shared_metadata: bool = False) -> TokenSchemas
```

```python
def serialize(value: CarbonSerializable) -> bytes
```

```python
def serialize_token_schemas(schemas: TokenSchemas) -> bytes
```

```python
def serialize_token_schemas_hex(schemas: TokenSchemas) -> str
```

```python
def sign_and_serialize_tx_msg(msg: TxMsg, keys: PhantasmaKeys) -> bytes
```

```python
def sign_and_serialize_tx_msg_hex(msg: TxMsg, keys: PhantasmaKeys) -> str
```

```python
def sign_tx_msg(msg: TxMsg, keys: PhantasmaKeys) -> SignedTxMsg
```

```python
def token_schemas_from_json(data: str) -> TokenSchemas
```

```python
def unpack_nft_instance_id(instance_id: int) -> tuple[int, int]
```

```python
def verify_token_schemas(schemas: TokenSchemas) -> None
```

```python
def vm_type_from_string(value: str) -> VMType
```

```python
def vm_type_name(vm_type: VMType) -> str
```

## phantasma_py.crypto

Source: `src/phantasma_py/crypto.py`

### Declarations

```python
class AddressKind(IntEnum)
```

```python
class SignatureKind(IntEnum)
```

```python
class Address
```

```python
class Hash
```

```python
class Ed25519Signature
```

```python
class PhantasmaKeys
```

### Fields

- `ADDRESS_LENGTH`
- `Address.data: bytes`
- `AddressKind.INTEROP`
- `AddressKind.INVALID`
- `AddressKind.SYSTEM`
- `AddressKind.USER`
- `Ed25519Signature.data: bytes`
- `Hash.data: bytes`
- `NULL_ADDRESS`
- `PRIVATE_KEY_LENGTH`
- `PUBLIC_KEY_LENGTH`
- `PhantasmaKeys.private_key: bytes`
- `SIGNATURE_LENGTH`
- `SignatureKind.ECDSA`
- `SignatureKind.ED25519`
- `SignatureKind.NONE`
- `SignatureKind.RING`

### Methods

```python
Address.__post_init__(self) -> None
```

```python
Address.__str__(self) -> str
```

```python
Address.from_hash(cls, value: bytes | str) -> Address
```

```python
Address.from_public_key(cls, public_key: bytes) -> Address
```

```python
Address.from_text(cls, text: str | None) -> Address
```

```python
Address.is_null(self) -> bool
```

```python
Address.kind(self) -> AddressKind
```

```python
Address.null(cls) -> Address
```

```python
Address.prefixed_bytes(self) -> bytes
```

```python
Address.public_key(self) -> bytes
```

```python
Address.text(self) -> str
```

```python
Ed25519Signature.__post_init__(self) -> None
```

```python
Ed25519Signature.kind(self) -> SignatureKind
```

```python
Ed25519Signature.serialize_data(self) -> bytes
```

```python
Ed25519Signature.verify(self, message: bytes, addresses: Iterable[Address]) -> bool
```

```python
Hash.__post_init__(self) -> None
```

```python
Hash.__str__(self) -> str
```

```python
Hash.difficulty(self) -> int
```

```python
Hash.from_hex(cls, text: str) -> Hash
```

```python
Hash.hex(self) -> str
```

```python
Hash.sha256(cls, data: bytes) -> Hash
```

```python
PhantasmaKeys.__post_init__(self) -> None
```

```python
PhantasmaKeys.__str__(self) -> str
```

```python
PhantasmaKeys.address(self) -> Address
```

```python
PhantasmaKeys.from_wif(cls, wif: str) -> PhantasmaKeys
```

```python
PhantasmaKeys.generate(cls) -> PhantasmaKeys
```

```python
PhantasmaKeys.public_key(self) -> bytes
```

```python
PhantasmaKeys.sign(self, message: bytes) -> Ed25519Signature
```

```python
PhantasmaKeys.to_wif(self) -> str
```

## phantasma_py.encoding

Source: `src/phantasma_py/encoding.py`

### Fields

- `BASE58_ALPHABET`

### Methods

```python
def decode_base58(text: str) -> bytes
```

```python
def decode_hex(value: str) -> bytes
```

```python
def encode_base58(data: bytes) -> str
```

```python
def encode_hex(data: bytes) -> str
```

## phantasma_py.errors

Source: `src/phantasma_py/errors.py`

### Declarations

```python
class PhantasmaError(Exception)
```

```python
class EncodingError(PhantasmaError, ValueError)
```

```python
class SerializationError(PhantasmaError, ValueError)
```

```python
class CryptoError(PhantasmaError, ValueError)
```

```python
class RPCError(PhantasmaError)
```

```python
class BuilderError(PhantasmaError, ValueError)
```

### Methods

```python
RPCError.__init__(self, message: str, *, code: int | None = None, data: object | None = None) -> None
```

## phantasma_py.rpc

Source: `src/phantasma_py/rpc.py`

### Declarations

```python
class HTTPSession(Protocol)
```

```python
class BalanceResult
```

```python
class InteropResult
```

```python
class PlatformResult
```

```python
class GovernanceResult
```

```python
class OrganizationResult
```

```python
class CrowdsaleResult
```

```python
class StakeResult
```

```python
class StorageResult
```

```python
class AccountResult
```

```python
class AddressTransactionsResult
```

```python
class LeaderboardRowResult
```

```python
class LeaderboardResult
```

```python
class DappResult
```

```python
class ChainResult
```

```python
class NexusResult
```

```python
class PaginatedResult(Generic[T])
```

```python
class CursorPaginatedResult(Generic[T])
```

```python
class EventResult
```

```python
class OracleResult
```

```python
class SignatureResult
```

```python
class TransactionResult
```

```python
class BlockResult
```

```python
class TokenPropertyResult
```

```python
class TokenExternalResult
```

```python
class TokenPriceResult
```

```python
class VMVariableSchemaResult
```

```python
class VMNamedVariableSchemaResult
```

```python
class VMStructSchemaResult
```

```python
class TokenSchemasResult
```

```python
class TokenSeriesResult
```

```python
class TokenResult
```

```python
class TokenDataResult
```

```python
class ScriptResult
```

```python
class ArchiveResult
```

```python
class ABIParameterResult
```

```python
class ABIMethodResult
```

```python
class ABIEventResult
```

```python
class ContractResult
```

```python
class AuctionResult
```

```python
class ChannelResult
```

```python
class ReceiptResult
```

```python
class PeerResult
```

```python
class ValidatorResult
```

```python
class SwapResult
```

```python
class BuildInfoResult
```

```python
class PhantasmaVMConfigResult
```

```python
class JsonRpcClient
```

```python
class PhantasmaRPC
```

### Fields

- `ABIEventResult.description: str`
- `ABIEventResult.name: str`
- `ABIEventResult.return_type: str`
- `ABIEventResult.value: int`
- `ABIMethodResult.name: str`
- `ABIMethodResult.parameters: list[ABIParameterResult]`
- `ABIMethodResult.return_type: str`
- `ABIParameterResult.name: str`
- `ABIParameterResult.type: str`
- `AccountResult.address: str`
- `AccountResult.balances: list[BalanceResult]`
- `AccountResult.name: str`
- `AccountResult.relay: str`
- `AccountResult.stake: str`
- `AccountResult.stakes: StakeResult`
- `AccountResult.storage: StorageResult`
- `AccountResult.unclaimed: str`
- `AccountResult.validator: str`
- `AddressTransactionsResult.address: str`
- `AddressTransactionsResult.txs: list[TransactionResult]`
- `ArchiveResult.block_count: int`
- `ArchiveResult.encryption: str`
- `ArchiveResult.hash: str`
- `ArchiveResult.missing_blocks: list[int]`
- `ArchiveResult.name: str`
- `ArchiveResult.owners: list[str]`
- `ArchiveResult.size: int`
- `ArchiveResult.time: int`
- `AuctionResult.base_symbol: str`
- `AuctionResult.chain_address: str`
- `AuctionResult.creator_address: str`
- `AuctionResult.current_winner: str`
- `AuctionResult.end_date: int`
- `AuctionResult.end_price: str`
- `AuctionResult.extension_period: str`
- `AuctionResult.listing_fee: str`
- `AuctionResult.price: str`
- `AuctionResult.quote_symbol: str`
- `AuctionResult.ram: str`
- `AuctionResult.rom: str`
- `AuctionResult.start_date: int`
- `AuctionResult.token_id: str`
- `AuctionResult.type: str`
- `BalanceResult.amount: str`
- `BalanceResult.chain: str`
- `BalanceResult.decimals: int`
- `BalanceResult.ids: list[str]`
- `BalanceResult.symbol: str`
- `BlockResult.chain_address: str`
- `BlockResult.events: list[EventResult]`
- `BlockResult.hash: str`
- `BlockResult.height: int`
- `BlockResult.oracles: list[OracleResult]`
- `BlockResult.previous_hash: str`
- `BlockResult.protocol: int`
- `BlockResult.reward: str`
- `BlockResult.timestamp: int`
- `BlockResult.txs: list[TransactionResult]`
- `BlockResult.validator_address: str`
- `BuildInfoResult.build_time_utc: str`
- `BuildInfoResult.commit: str`
- `BuildInfoResult.version: str`
- `ChainResult.address: str`
- `ChainResult.contracts: list[str]`
- `ChainResult.dapps: list[str]`
- `ChainResult.height: int`
- `ChainResult.name: str`
- `ChainResult.organization: str`
- `ChainResult.parent: str`
- `ChannelResult.active: bool`
- `ChannelResult.balance: str`
- `ChannelResult.chain: str`
- `ChannelResult.creation_time: int`
- `ChannelResult.creator_address: str`
- `ChannelResult.fee: str`
- `ChannelResult.index: int`
- `ChannelResult.name: str`
- `ChannelResult.symbol: str`
- `ChannelResult.target_address: str`
- `ContractResult.address: str`
- `ContractResult.events: list[ABIEventResult]`
- `ContractResult.methods: list[ABIMethodResult]`
- `ContractResult.name: str`
- `ContractResult.script: str`
- `CrowdsaleResult.creator: str`
- `CrowdsaleResult.end_date: int`
- `CrowdsaleResult.flags: str`
- `CrowdsaleResult.global_hard_cap: str`
- `CrowdsaleResult.global_soft_cap: str`
- `CrowdsaleResult.hash: str`
- `CrowdsaleResult.name: str`
- `CrowdsaleResult.price: int`
- `CrowdsaleResult.receive_symbol: str`
- `CrowdsaleResult.sell_symbol: str`
- `CrowdsaleResult.start_date: int`
- `CrowdsaleResult.user_hard_cap: str`
- `CrowdsaleResult.user_soft_cap: str`
- `CursorPaginatedResult.cursor: str`
- `CursorPaginatedResult.result: T | None`
- `DappResult.address: str`
- `DappResult.chain: str`
- `DappResult.name: str`
- `EventResult.address: str`
- `EventResult.contract: str`
- `EventResult.data: str`
- `EventResult.kind: str`
- `GovernanceResult.name: str`
- `GovernanceResult.value: str`
- `InteropResult.external: str`
- `InteropResult.local: str`
- `LeaderboardResult.name: str`
- `LeaderboardResult.rows: list[LeaderboardRowResult]`
- `LeaderboardRowResult.address: str`
- `LeaderboardRowResult.value: str`
- `NexusResult.chains: list[ChainResult]`
- `NexusResult.governance: list[GovernanceResult]`
- `NexusResult.name: str`
- `NexusResult.organizations: list[str]`
- `NexusResult.platforms: list[PlatformResult]`
- `NexusResult.protocol: int`
- `NexusResult.tokens: list[TokenResult]`
- `OracleResult.content: str`
- `OracleResult.url: str`
- `OrganizationResult.id: str`
- `OrganizationResult.members: list[str]`
- `OrganizationResult.name: str`
- `PaginatedResult.page: int`
- `PaginatedResult.page_size: int`
- `PaginatedResult.result: T | None`
- `PaginatedResult.total: int`
- `PaginatedResult.total_pages: int`
- `PeerResult.fee: str`
- `PeerResult.flags: str`
- `PeerResult.pow: int`
- `PeerResult.url: str`
- `PeerResult.version: str`
- `PhantasmaVMConfigResult.feature_level: int`
- `PhantasmaVMConfigResult.fuel_per_contract_deploy: str`
- `PhantasmaVMConfigResult.gas_account: str`
- `PhantasmaVMConfigResult.gas_constructor: str`
- `PhantasmaVMConfigResult.gas_leaderboard: str`
- `PhantasmaVMConfigResult.gas_nexus: str`
- `PhantasmaVMConfigResult.gas_oracle: str`
- `PhantasmaVMConfigResult.gas_organization: str`
- `PhantasmaVMConfigResult.gas_standard: str`
- `PhantasmaVMConfigResult.is_stored: bool`
- `PlatformResult.chain: str`
- `PlatformResult.fuel: str`
- `PlatformResult.interop: list[InteropResult]`
- `PlatformResult.platform: str`
- `PlatformResult.tokens: list[str]`
- `ReceiptResult.channel: str`
- `ReceiptResult.index: str`
- `ReceiptResult.nexus: str`
- `ReceiptResult.receiver: str`
- `ReceiptResult.script: str`
- `ReceiptResult.sender: str`
- `ReceiptResult.timestamp: int`
- `ScriptResult.events: list[EventResult]`
- `ScriptResult.oracles: list[OracleResult]`
- `ScriptResult.result: str`
- `ScriptResult.results: list[str]`
- `SignatureResult.data: str`
- `SignatureResult.kind: str`
- `StakeResult.amount: str`
- `StakeResult.time: int`
- `StakeResult.unclaimed: str`
- `StorageResult.archives: list[ArchiveResult]`
- `StorageResult.available: int`
- `StorageResult.avatar: str`
- `StorageResult.used: int`
- `SwapResult.destination_address: str`
- `SwapResult.destination_chain: str`
- `SwapResult.destination_hash: str`
- `SwapResult.destination_platform: str`
- `SwapResult.source_address: str`
- `SwapResult.source_chain: str`
- `SwapResult.source_hash: str`
- `SwapResult.source_platform: str`
- `SwapResult.symbol: str`
- `SwapResult.value: str`
- `T`
- `TokenDataResult.carbon_nft_address: str`
- `TokenDataResult.carbon_series_id: str`
- `TokenDataResult.carbon_token_id: str`
- `TokenDataResult.chain_name: str`
- `TokenDataResult.creator_address: str`
- `TokenDataResult.id: str`
- `TokenDataResult.infusion: list[TokenPropertyResult]`
- `TokenDataResult.mint: str`
- `TokenDataResult.owner_address: str`
- `TokenDataResult.properties: list[TokenPropertyResult]`
- `TokenDataResult.ram: str`
- `TokenDataResult.rom: str`
- `TokenDataResult.series: str`
- `TokenDataResult.status: str`
- `TokenExternalResult.hash: str`
- `TokenExternalResult.platform: str`
- `TokenPriceResult.close: str`
- `TokenPriceResult.high: str`
- `TokenPriceResult.low: str`
- `TokenPriceResult.open: str`
- `TokenPriceResult.timestamp: int`
- `TokenPropertyResult.key: str`
- `TokenPropertyResult.value: str`
- `TokenResult.address: str`
- `TokenResult.burned_supply: str`
- `TokenResult.carbon_id: str`
- `TokenResult.current_supply: str`
- `TokenResult.decimals: int`
- `TokenResult.external: list[TokenExternalResult]`
- `TokenResult.flags: str`
- `TokenResult.max_supply: str`
- `TokenResult.metadata: list[TokenPropertyResult]`
- `TokenResult.name: str`
- `TokenResult.owner: str`
- `TokenResult.price: list[TokenPriceResult]`
- `TokenResult.script: str`
- `TokenResult.series: list[TokenSeriesResult]`
- `TokenResult.symbol: str`
- `TokenResult.token_schemas: TokenSchemasResult | None`
- `TokenSchemasResult.ram: VMStructSchemaResult`
- `TokenSchemasResult.rom: VMStructSchemaResult`
- `TokenSchemasResult.series_metadata: VMStructSchemaResult`
- `TokenSeriesResult.burned_supply: str`
- `TokenSeriesResult.carbon_series_id: str`
- `TokenSeriesResult.carbon_token_id: str`
- `TokenSeriesResult.current_supply: str`
- `TokenSeriesResult.max_mint: str`
- `TokenSeriesResult.max_supply: str`
- `TokenSeriesResult.metadata: list[TokenPropertyResult]`
- `TokenSeriesResult.methods: list[ABIMethodResult]`
- `TokenSeriesResult.mint_count: str`
- `TokenSeriesResult.mode: str`
- `TokenSeriesResult.owner_address: str`
- `TokenSeriesResult.script: str`
- `TokenSeriesResult.series_id: str`
- `TransactionResult.block_hash: str`
- `TransactionResult.block_height: int`
- `TransactionResult.chain_address: str`
- `TransactionResult.events: list[EventResult]`
- `TransactionResult.expiration: int`
- `TransactionResult.fee: str`
- `TransactionResult.hash: str`
- `TransactionResult.payload: str`
- `TransactionResult.result: str`
- `TransactionResult.script: str`
- `TransactionResult.signatures: list[SignatureResult]`
- `TransactionResult.state: str`
- `TransactionResult.timestamp: int`
- `VMNamedVariableSchemaResult.name: str`
- `VMNamedVariableSchemaResult.schema: VMVariableSchemaResult`
- `VMStructSchemaResult.fields: list[VMNamedVariableSchemaResult]`
- `VMStructSchemaResult.flags: int`
- `VMVariableSchemaResult.schema: VMStructSchemaResult | None`
- `VMVariableSchemaResult.type: str`
- `ValidatorResult.address: str`
- `ValidatorResult.type: str`

### Methods

```python
AccountResult.get_token_balance(self, symbol: str, decimals: int = 0) -> BalanceResult
```

```python
BalanceResult.decimal_amount(self) -> str
```

```python
HTTPSession.post(self, url: str, *, json: Mapping[str, Any], timeout: float) -> Any
```

```python
JsonRpcClient.__init__(self, endpoint: str, *, session: HTTPSession | None = None, timeout: float = 30.0) -> None
```

```python
JsonRpcClient.call(self, method: str, *params) -> Any
```

```python
PhantasmaRPC.__init__(self, endpoint: str, *, session: HTTPSession | None = None, timeout: float = 30.0) -> None
```

```python
PhantasmaRPC.call(self, method: str, *params) -> Any
```

```python
PhantasmaRPC.get_account(self, address: str, *, extended: bool = False, check_address_reserved_byte: bool | None = None, address_type: str | None = None) -> AccountResult
```

```python
PhantasmaRPC.get_account_fungible_tokens(self, account: str, token_symbol: str = '', carbon_token_id: int = 0, *, page_size: int = 100, cursor: str = '', check_address_reserved_byte: bool = False, address_type: str | None = None) -> CursorPaginatedResult[list[BalanceResult]]
```

```python
PhantasmaRPC.get_account_fungible_tokens_with_address_type(self, account: str, token_symbol: str, carbon_token_id: int, page_size: int, cursor: str, check_address_reserved_byte: bool, address_type: str) -> CursorPaginatedResult[list[BalanceResult]]
```

```python
PhantasmaRPC.get_account_nfts(self, account: str, token_symbol: str = '', carbon_token_id: int = 0, carbon_series_id: int = 0, *, page_size: int = 100, cursor: str = '', extended: bool = True, check_address_reserved_byte: bool = False, address_type: str | None = None) -> CursorPaginatedResult[list[TokenDataResult]]
```

```python
PhantasmaRPC.get_account_nfts_with_address_type(self, account: str, token_symbol: str, carbon_token_id: int, carbon_series_id: int, page_size: int, cursor: str, extended: bool, check_address_reserved_byte: bool, address_type: str) -> CursorPaginatedResult[list[TokenDataResult]]
```

```python
PhantasmaRPC.get_account_owned_token_series(self, account: str, token_symbol: str = '', carbon_token_id: int = 0, *, page_size: int = 100, cursor: str = '', check_address_reserved_byte: bool = False, address_type: str | None = None) -> CursorPaginatedResult[list[TokenSeriesResult]]
```

```python
PhantasmaRPC.get_account_owned_token_series_with_address_type(self, account: str, token_symbol: str, carbon_token_id: int, page_size: int, cursor: str, check_address_reserved_byte: bool, address_type: str) -> CursorPaginatedResult[list[TokenSeriesResult]]
```

```python
PhantasmaRPC.get_account_owned_tokens(self, account: str, token_symbol: str = '', carbon_token_id: int = 0, *, page_size: int = 100, cursor: str = '', check_address_reserved_byte: bool = False, address_type: str | None = None) -> CursorPaginatedResult[list[TokenResult]]
```

```python
PhantasmaRPC.get_account_owned_tokens_with_address_type(self, account: str, token_symbol: str, carbon_token_id: int, page_size: int, cursor: str, check_address_reserved_byte: bool, address_type: str) -> CursorPaginatedResult[list[TokenResult]]
```

```python
PhantasmaRPC.get_account_with_address_type(self, address: str, extended: bool, check_address_reserved_byte: bool, address_type: str) -> AccountResult
```

```python
PhantasmaRPC.get_accounts(self, addresses: Sequence[str] | str, *, extended: bool = False, check_address_reserved_byte: bool | None = None, address_type: str | None = None) -> list[AccountResult]
```

```python
PhantasmaRPC.get_accounts_text(self, addresses: str, *, extended: bool = False) -> list[AccountResult]
```

```python
PhantasmaRPC.get_accounts_with_address_type(self, addresses: Sequence[str] | str, extended: bool, check_address_reserved_byte: bool, address_type: str) -> list[AccountResult]
```

```python
PhantasmaRPC.get_address_transaction_count(self, address: str, chain: str = 'main') -> int
```

```python
PhantasmaRPC.get_address_transactions(self, address: str, page: int, page_size: int) -> PaginatedResult[AddressTransactionsResult]
```

```python
PhantasmaRPC.get_archive(self, archive_hash: str) -> ArchiveResult
```

```python
PhantasmaRPC.get_auction(self, chain: str, symbol: str, token_id: str) -> AuctionResult
```

```python
PhantasmaRPC.get_auctions(self, chain: str, symbol: str, page: int, page_size: int) -> PaginatedResult[list[AuctionResult]]
```

```python
PhantasmaRPC.get_auctions_count(self, chain: str, symbol: str) -> int
```

```python
PhantasmaRPC.get_block_by_hash(self, block_hash: str) -> BlockResult
```

```python
PhantasmaRPC.get_block_by_height(self, chain: str, height: int | str) -> BlockResult
```

```python
PhantasmaRPC.get_block_height(self, chain: str = 'main') -> int
```

```python
PhantasmaRPC.get_block_transaction_count_by_hash(self, block_hash: str, chain: str = 'main') -> int
```

```python
PhantasmaRPC.get_block_transaction_count_by_hash_on_chain(self, chain: str, block_hash: str) -> int
```

```python
PhantasmaRPC.get_chain(self, name: str = 'main', *, extended: bool = True) -> ChainResult
```

```python
PhantasmaRPC.get_chains(self, *, extended: bool = True) -> list[ChainResult]
```

```python
PhantasmaRPC.get_contract(self, contract_name: str, chain: str = 'main') -> ContractResult
```

```python
PhantasmaRPC.get_contract_by_address(self, chain: str, contract_address: str) -> ContractResult
```

```python
PhantasmaRPC.get_contract_by_name(self, chain: str, contract_name: str) -> ContractResult
```

```python
PhantasmaRPC.get_contracts(self, chain: str = 'main', *, extended: bool = True) -> list[ContractResult]
```

```python
PhantasmaRPC.get_latest_block(self, chain: str = 'main') -> BlockResult
```

```python
PhantasmaRPC.get_leaderboard(self, name: str) -> LeaderboardResult
```

```python
PhantasmaRPC.get_nexus(self, *, extended: bool = True) -> NexusResult
```

```python
PhantasmaRPC.get_nft(self, symbol: str, nft_id: str, *, extended: bool = True) -> TokenDataResult
```

```python
PhantasmaRPC.get_nfts(self, symbol: str, nft_ids: Sequence[str] | str, *, extended: bool = True) -> list[TokenDataResult]
```

```python
PhantasmaRPC.get_nfts_text(self, symbol: str, nft_ids: str, *, extended: bool = True) -> list[TokenDataResult]
```

```python
PhantasmaRPC.get_organization(self, organization_id: str, *, extended: bool = True) -> OrganizationResult
```

```python
PhantasmaRPC.get_organization_by_name(self, name: str, *, extended: bool = True) -> OrganizationResult
```

```python
PhantasmaRPC.get_organizations(self, *, extended: bool = False) -> list[OrganizationResult]
```

```python
PhantasmaRPC.get_phantasma_vm_config(self, chain: str = 'main') -> PhantasmaVMConfigResult
```

```python
PhantasmaRPC.get_platforms(self) -> list[PlatformResult]
```

```python
PhantasmaRPC.get_token(self, symbol: str, *, extended: bool = True, carbon_token_id: int = 0) -> TokenResult
```

```python
PhantasmaRPC.get_token_balance(self, address: str, symbol: str, chain: str = 'main', *, check_address_reserved_byte: bool | None = None, address_type: str | None = None) -> BalanceResult
```

```python
PhantasmaRPC.get_token_balance_checked(self, address: str, symbol: str, chain: str, check_address_reserved_byte: bool) -> BalanceResult
```

```python
PhantasmaRPC.get_token_balance_with_address_type(self, address: str, symbol: str, chain: str, check_address_reserved_byte: bool, address_type: str) -> BalanceResult
```

```python
PhantasmaRPC.get_token_data(self, symbol: str, nft_id: str) -> TokenDataResult
```

```python
PhantasmaRPC.get_token_nfts(self, carbon_token_id: int, carbon_series_id: int = 0, *, series_id: str = '', page_size: int = 100, cursor: str = '', extended: bool = True) -> CursorPaginatedResult[list[TokenDataResult]]
```

```python
PhantasmaRPC.get_token_nfts_with_series_id(self, carbon_token_id: int, carbon_series_id: int, series_id: str, page_size: int, cursor: str, extended: bool) -> CursorPaginatedResult[list[TokenDataResult]]
```

```python
PhantasmaRPC.get_token_series(self, symbol: str, carbon_token_id: int = 0, page_size: int = 100, cursor: str = '') -> CursorPaginatedResult[list[TokenSeriesResult]]
```

```python
PhantasmaRPC.get_token_series_by_id(self, symbol: str, *, carbon_token_id: int = 0, series_id: str = '', carbon_series_id: int = 0) -> TokenSeriesResult
```

```python
PhantasmaRPC.get_token_with_id(self, symbol: str, extended: bool, carbon_token_id: int) -> TokenResult
```

```python
PhantasmaRPC.get_tokens(self, *, extended: bool = True, owner_address: str | None = None, address_type: str | None = None) -> list[TokenResult]
```

```python
PhantasmaRPC.get_tokens_as_map(self, *, extended: bool = True) -> dict[str, TokenResult]
```

```python
PhantasmaRPC.get_tokens_by_owner(self, owner_address: str, *, extended: bool = True) -> list[TokenResult]
```

```python
PhantasmaRPC.get_tokens_by_owner_with_address_type(self, owner_address: str, address_type: str, *, extended: bool = True) -> list[TokenResult]
```

```python
PhantasmaRPC.get_transaction(self, tx_hash: str) -> TransactionResult
```

```python
PhantasmaRPC.get_transaction_by_block_hash_and_index(self, block_hash: str, index: int, *, chain: str = 'main') -> TransactionResult
```

```python
PhantasmaRPC.get_transaction_by_block_hash_and_index_on_chain(self, chain: str, block_hash: str, index: int) -> TransactionResult
```

```python
PhantasmaRPC.get_version(self) -> BuildInfoResult
```

```python
PhantasmaRPC.invoke_raw_script(self, chain: str, script_hex: str) -> ScriptResult
```

```python
PhantasmaRPC.look_up_name(self, name: str) -> str
```

```python
PhantasmaRPC.lookup_name(self, name: str) -> str
```

```python
PhantasmaRPC.mainnet(cls) -> PhantasmaRPC
```

```python
PhantasmaRPC.parse_create_token_result(self, result_hex: str) -> int
```

```python
PhantasmaRPC.parse_create_token_series_result(self, result_hex: str) -> int
```

```python
PhantasmaRPC.read_archive(self, archive_hash: str, block_index: int) -> str
```

```python
PhantasmaRPC.send_carbon_transaction(self, tx: bytes | str) -> str
```

```python
PhantasmaRPC.send_raw_transaction(self, tx: Transaction | bytes | str) -> str
```

```python
PhantasmaRPC.sign_and_send_built_transaction(self, tx: Transaction, keys: PhantasmaKeys) -> str
```

```python
PhantasmaRPC.sign_and_send_carbon_transaction(self, msg: TxMsg, keys: PhantasmaKeys) -> str
```

```python
PhantasmaRPC.sign_and_send_transaction(self, keys: PhantasmaKeys, nexus: str, script: bytes, chain: str = 'main', payload: bytes | str = b'', *, expiration: int | None = None) -> str
```

```python
PhantasmaRPC.sign_carbon_transaction(self, msg: TxMsg, keys: PhantasmaKeys) -> SignedTxMsg
```

```python
PhantasmaRPC.testnet(cls) -> PhantasmaRPC
```

```python
PhantasmaRPC.write_archive(self, archive_hash: str, block_index: int, block_content: bytes | str) -> bool
```

```python
PhantasmaRPC.write_archive_base64(self, archive_hash: str, block_index: int, block_content: str) -> bool
```

```python
ScriptResult.decode_result(self) -> VMObject
```

```python
ScriptResult.decode_results(self, index: int) -> VMObject
```

```python
StakeResult.decimal_amount(self) -> str
```

```python
TokenResult.has_flag(self, flag: str) -> bool
```

```python
TokenResult.is_burnable(self) -> bool
```

```python
TokenResult.is_divisible(self) -> bool
```

```python
TokenResult.is_fiat(self) -> bool
```

```python
TokenResult.is_finite(self) -> bool
```

```python
TokenResult.is_fuel(self) -> bool
```

```python
TokenResult.is_fungible(self) -> bool
```

```python
TokenResult.is_mintable(self) -> bool
```

```python
TokenResult.is_stakable(self) -> bool
```

```python
TokenResult.is_transferable(self) -> bool
```

```python
TransactionResult.state_is_fault(self) -> bool
```

```python
TransactionResult.state_is_success(self) -> bool
```

```python
def convert_decimals(raw: str | int, decimals: int, separator: str = '.') -> str
```

## phantasma_py.transaction

Source: `src/phantasma_py/transaction.py`

### Declarations

```python
class Transaction
```

### Fields

- `SDK_PAYLOAD`
- `Transaction.chain_name: str`
- `Transaction.expiration: int`
- `Transaction.nexus_name: str`
- `Transaction.payload: bytes`
- `Transaction.script: bytes`
- `Transaction.signatures: list[Ed25519Signature]`

### Methods

```python
Transaction.from_bytes(cls, data: bytes) -> Transaction
```

```python
Transaction.hash(self) -> Hash
```

```python
Transaction.is_signed_by(self, key_pair: PhantasmaKeys) -> bool
```

```python
Transaction.mine(self, difficulty: int) -> None
```

```python
Transaction.sign(self, key_pair: PhantasmaKeys) -> Ed25519Signature
```

```python
Transaction.to_bytes(self, *, with_signatures: bool = True) -> bytes
```

```python
def tx_state_is_fault(state: str) -> bool
```

```python
def tx_state_is_success(state: str) -> bool
```

## phantasma_py.vm

Source: `src/phantasma_py/vm.py`

### Declarations

```python
class Opcode(IntEnum)
```

```python
class VMType(IntEnum)
```

```python
class VMObject
```

```python
class ScriptBuilder
```

### Fields

- `Opcode.ABS`
- `Opcode.ADD`
- `Opcode.AND`
- `Opcode.CALL`
- `Opcode.CAST`
- `Opcode.CAT`
- `Opcode.CLEAR`
- `Opcode.COPY`
- `Opcode.COUNT`
- `Opcode.CTX`
- `Opcode.DEBUG`
- `Opcode.DEC`
- `Opcode.DIV`
- `Opcode.EQUAL`
- `Opcode.EVM`
- `Opcode.EXTCALL`
- `Opcode.GET`
- `Opcode.GT`
- `Opcode.GTE`
- `Opcode.INC`
- `Opcode.JMP`
- `Opcode.JMPIF`
- `Opcode.JMPNOT`
- `Opcode.LEFT`
- `Opcode.LOAD`
- `Opcode.LT`
- `Opcode.LTE`
- `Opcode.MAX`
- `Opcode.MIN`
- `Opcode.MOD`
- `Opcode.MOVE`
- `Opcode.MUL`
- `Opcode.NEGATE`
- `Opcode.NOP`
- `Opcode.NOT`
- `Opcode.OR`
- `Opcode.PACK`
- `Opcode.POP`
- `Opcode.POW`
- `Opcode.PUSH`
- `Opcode.PUT`
- `Opcode.RANGE`
- `Opcode.REMOVE`
- `Opcode.RET`
- `Opcode.RIGHT`
- `Opcode.SHL`
- `Opcode.SHR`
- `Opcode.SIGN`
- `Opcode.SIZE`
- `Opcode.SUB`
- `Opcode.SUBSTR`
- `Opcode.SWAP`
- `Opcode.SWITCH`
- `Opcode.THROW`
- `Opcode.UNPACK`
- `Opcode.XOR`
- `ScriptBuilder.MAX_REGISTER_COUNT`
- `VMObject.data: Any`
- `VMObject.type: VMType`
- `VMType.BOOL`
- `VMType.BYTES`
- `VMType.ENUM`
- `VMType.NONE`
- `VMType.NUMBER`
- `VMType.OBJECT`
- `VMType.STRING`
- `VMType.STRUCT`
- `VMType.TIMESTAMP`

### Methods

```python
ScriptBuilder.__init__(self) -> None
```

```python
ScriptBuilder.allow_gas(self, from_address: Address, to_address: Address, gas_price: int, gas_limit: int) -> ScriptBuilder
```

```python
ScriptBuilder.allow_gas_text(self, from_address: str, to_address: str, gas_price: int, gas_limit: int) -> ScriptBuilder
```

```python
ScriptBuilder.begin(cls) -> ScriptBuilder
```

```python
ScriptBuilder.call_contract(self, contract_name: str, method: str, *args) -> ScriptBuilder
```

```python
ScriptBuilder.call_interop(self, method: str, *args) -> ScriptBuilder
```

```python
ScriptBuilder.call_nft(self, symbol: str, series_id: int, method: str, *args) -> ScriptBuilder
```

```python
ScriptBuilder.cross_transfer_nft(self, destination_chain: Address, symbol: str, from_address: Address, to_address: Address, token_id: int) -> ScriptBuilder
```

```python
ScriptBuilder.cross_transfer_nft_text(self, destination_chain: str, symbol: str, from_address: str, to_address: str, token_id: int) -> ScriptBuilder
```

```python
ScriptBuilder.cross_transfer_nft_to_text(self, destination_chain: Address, symbol: str, from_address: Address, to_address: str, token_id: int) -> ScriptBuilder
```

```python
ScriptBuilder.cross_transfer_token(self, destination_chain: Address, symbol: str, from_address: Address, to_address: Address, amount: int) -> ScriptBuilder
```

```python
ScriptBuilder.cross_transfer_token_text(self, destination_chain: str, symbol: str, from_address: str, to_address: str, amount: int) -> ScriptBuilder
```

```python
ScriptBuilder.cross_transfer_token_to_text(self, destination_chain: Address, symbol: str, from_address: Address, to_address: str, amount: int) -> ScriptBuilder
```

```python
ScriptBuilder.current_size(self) -> int
```

```python
ScriptBuilder.emit(self, opcode: Opcode) -> ScriptBuilder
```

```python
ScriptBuilder.emit_call(self, label: str, register_count: int) -> ScriptBuilder
```

```python
ScriptBuilder.emit_conditional_jump(self, opcode: Opcode, src_reg: int, label: str) -> ScriptBuilder
```

```python
ScriptBuilder.emit_copy(self, src_reg: int, dst_reg: int) -> ScriptBuilder
```

```python
ScriptBuilder.emit_ext_call(self, method: str, reg: int = 0) -> ScriptBuilder
```

```python
ScriptBuilder.emit_jump(self, opcode: Opcode, label: str, reg: int = 0) -> ScriptBuilder
```

```python
ScriptBuilder.emit_label(self, label: str) -> ScriptBuilder
```

```python
ScriptBuilder.emit_load(self, reg: int, data: bytes, vm_type: VMType) -> ScriptBuilder
```

```python
ScriptBuilder.emit_load_bool(self, reg: int, value: bool) -> ScriptBuilder
```

```python
ScriptBuilder.emit_load_number(self, reg: int, value: int) -> ScriptBuilder
```

```python
ScriptBuilder.emit_load_string(self, reg: int, value: str) -> ScriptBuilder
```

```python
ScriptBuilder.emit_load_time(self, reg: int, value: datetime) -> ScriptBuilder
```

```python
ScriptBuilder.emit_move(self, src_reg: int, dst_reg: int) -> ScriptBuilder
```

```python
ScriptBuilder.emit_pop(self, reg: int) -> ScriptBuilder
```

```python
ScriptBuilder.emit_push(self, reg: int) -> ScriptBuilder
```

```python
ScriptBuilder.emit_raw(self, data: bytes) -> ScriptBuilder
```

```python
ScriptBuilder.emit_throw(self, reg: int) -> ScriptBuilder
```

```python
ScriptBuilder.emit_var_bytes(self, value: int) -> ScriptBuilder
```

```python
ScriptBuilder.end_script(self) -> bytes
```

```python
ScriptBuilder.end_script_hex(self) -> str
```

```python
ScriptBuilder.end_script_with_error(self) -> tuple[bytes, Exception | None]
```

```python
ScriptBuilder.mint_tokens(self, symbol: str, from_address: Address, to_address: Address, amount: int) -> ScriptBuilder
```

```python
ScriptBuilder.mint_tokens_text(self, symbol: str, from_address: str, to_address: str, amount: int) -> ScriptBuilder
```

```python
ScriptBuilder.spend_gas(self, address: Address) -> ScriptBuilder
```

```python
ScriptBuilder.spend_gas_text(self, address: str) -> ScriptBuilder
```

```python
ScriptBuilder.stake(self, address: Address, amount: int) -> ScriptBuilder
```

```python
ScriptBuilder.stake_text(self, address: str, amount: int) -> ScriptBuilder
```

```python
ScriptBuilder.to_script(self) -> bytes
```

```python
ScriptBuilder.transfer_balance(self, symbol: str, from_address: Address, to_address: Address) -> ScriptBuilder
```

```python
ScriptBuilder.transfer_balance_text(self, symbol: str, from_address: str, to_address: str) -> ScriptBuilder
```

```python
ScriptBuilder.transfer_nft(self, symbol: str, from_address: Address, to_address: Address, token_id: int) -> ScriptBuilder
```

```python
ScriptBuilder.transfer_nft_text(self, symbol: str, from_address: str, to_address: str, token_id: int) -> ScriptBuilder
```

```python
ScriptBuilder.transfer_nft_to_text(self, symbol: str, from_address: Address, to_address: str, token_id: int) -> ScriptBuilder
```

```python
ScriptBuilder.transfer_tokens(self, symbol: str, from_address: Address, to_address: Address, amount: int) -> ScriptBuilder
```

```python
ScriptBuilder.transfer_tokens_text(self, symbol: str, from_address: str, to_address: str, amount: int) -> ScriptBuilder
```

```python
ScriptBuilder.transfer_tokens_to_text(self, symbol: str, from_address: Address, to_address: str, amount: int) -> ScriptBuilder
```

```python
ScriptBuilder.unstake(self, address: Address, amount: int) -> ScriptBuilder
```

```python
ScriptBuilder.unstake_text(self, address: str, amount: int) -> ScriptBuilder
```

```python
VMObject.array_type(self) -> VMType
```

```python
VMObject.as_bool(self) -> bool
```

```python
VMObject.as_bytes(self) -> bytes
```

```python
VMObject.as_number(self) -> int
```

```python
VMObject.as_string(self) -> str
```

```python
VMObject.cast_to(self, target: VMType) -> VMObject
```

```python
VMObject.from_bytes(cls, data: bytes) -> VMObject
```

```python
VMObject.read(cls, reader: BinaryReader) -> VMObject
```

```python
VMObject.to_bytes(self) -> bytes
```

```python
VMObject.write(self, writer: BinaryWriter) -> None
```
