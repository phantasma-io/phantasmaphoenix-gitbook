# Go SDK Public API Inventory

This page lists public classes, methods, functions, enum values, fields, and
constants from the cited source baseline. Use it to check exact names when
working with lower-level SDK APIs.

Source baseline:

| Item | Value |
| ---- | ----- |
| Source repo | `phantasma-sdk-go` |
| Source commit | `7630d54796b8dd23655b39fa01109e4bfc08461b` |
| Scope | exported identifiers in non-test Go files under `pkg/**` |

## github.com/phantasma-io/phantasma-sdk-go/pkg/blockchain

Source: `pkg/blockchain`

### Declarations

```go
const MaxTransactionSignatureCount = 1024
```

```go
type Transaction struct {
```

### Fields

- `ChainName string`
- `Expiration uint32`
- `Hash crypto.Hash`
- `NexusName string`
- `Payload []byte`
- `Script []byte`
- `Signatures []crypto.Signature`

### Methods

```go
func (tx *Transaction) Bytes() []byte
```

```go
func (tx *Transaction) BytesEx(withSignatures bool) []byte
```

```go
func (tx *Transaction) Deserialize(reader *io.BinReader)
```

```go
func (tx *Transaction) HasSignatures() bool
```

```go
func (tx *Transaction) IsSignedBy(addresses []crypto.Address) bool
```

```go
func (tx *Transaction) Mine(difficulty int)
```

```go
func (tx *Transaction) Serialize(writer *io.BinWriter)
```

```go
func (tx *Transaction) SerializeEx(writer *io.BinWriter, withSignatures bool)
```

```go
func (tx *Transaction) Sign(keyPair crypto.KeyPair) error
```

```go
func (tx *Transaction) String() string
```

```go
func NewTransaction(nexusName, chainName string, script []byte, timestamp uint32, payload []byte) Transaction
```

```go
func TxStateIsFault(state string) bool
```

```go
func TxStateIsSuccess(state string) bool
```

## github.com/phantasma-io/phantasma-sdk-go/pkg/carbon

Source: `pkg/carbon`

### Declarations

```go
const ListingTypeFixedPrice ListingType = 0
```

```go
const MarketConfigFlagsCanCancelEarly MarketConfigFlags = 1 << 2
```

```go
const MarketConfigFlagsCanPurchaseLate MarketConfigFlags = 1 << 3
```

```go
const MarketConfigFlagsEnforceRoyalties MarketConfigFlags = 1 << 1
```

```go
const MarketConfigFlagsNone MarketConfigFlags = 0
```

```go
const MarketConfigFlagsPriceRequired MarketConfigFlags = 1 << 0
```

```go
const MarketDelistingGraceMS uint64 = 1000 * 60 * 60 * 24
```

```go
const MarketMaximumListingTimeMS uint64 = 1000 * 60 * 60 * 24 * 90
```

```go
const MarketMethodBuyToken
```

```go
const MarketMethodBuyTokenByID
```

```go
const MarketMethodCancelSale
```

```go
const MarketMethodCancelSaleByID
```

```go
const MarketMethodGetTokenListingCount
```

```go
const MarketMethodGetTokenListingInfo
```

```go
const MarketMethodGetTokenListingInfoByID
```

```go
const MarketMethodSellToken MarketContractMethod = iota
```

```go
const MarketMethodSellTokenByID
```

```go
const MarketMinimumListingTimeMS uint64 = 1000
```

```go
const MarketRoyaltyHundredPercent uint64 = 100 * MarketRoyaltyOnePercent
```

```go
const MarketRoyaltyOnePercent uint64 = 10_000_000
```

```go
const ModuleIDGovernance ModuleID = 0
```

```go
const ModuleIDInternal ModuleID = 0xffffffff
```

```go
const ModuleIDMarket ModuleID = 4
```

```go
const ModuleIDOrg ModuleID = 3
```

```go
const ModuleIDPhantasma ModuleID = 2
```

```go
const ModuleIDPhantasmaVM = ModuleIDPhantasma
```

```go
const ModuleIDToken ModuleID = 1
```

```go
const StandardMetaID = "_i"
```

```go
const TokenFlagsBigFungible TokenFlags = 1 << 0
```

```go
const TokenFlagsNonFungible TokenFlags = 1 << 1
```

```go
const TokenFlagsNone TokenFlags = 0
```

```go
const TokenMethodApplyInflation
```

```go
const TokenMethodBurnFungible
```

```go
const TokenMethodBurnNonFungible
```

```go
const TokenMethodCreateMintedTokenSeries
```

```go
const TokenMethodCreateToken
```

```go
const TokenMethodCreateTokenSeries
```

```go
const TokenMethodDeleteTokenSeries
```

```go
const TokenMethodGetBalance
```

```go
const TokenMethodGetBalances
```

```go
const TokenMethodGetInstances
```

```go
const TokenMethodGetNextTokenInflation
```

```go
const TokenMethodGetNonFungibleInfo
```

```go
const TokenMethodGetNonFungibleInfoByRomID
```

```go
const TokenMethodGetSeriesInfo
```

```go
const TokenMethodGetSeriesInfoByMetaID
```

```go
const TokenMethodGetSeriesSupply
```

```go
const TokenMethodGetTokenIDBySymbol
```

```go
const TokenMethodGetTokenInfo
```

```go
const TokenMethodGetTokenInfoBySymbol
```

```go
const TokenMethodGetTokenSupply
```

```go
const TokenMethodMintFungible
```

```go
const TokenMethodMintNonFungible
```

```go
const TokenMethodMintPhantasmaNonFungible
```

```go
const TokenMethodSetTokensConfig
```

```go
const TokenMethodTransferFungible TokenContractMethod = iota
```

```go
const TokenMethodTransferNonFungible
```

```go
const TokenMethodUpdateSeriesMetadata
```

```go
const TokenMethodUpdateTokenMetadata
```

```go
const TokensConfigFlagsAllowExplicitNFTMetaIDMint TokensConfigFlags = 1 << 4
```

```go
const TokensConfigFlagsNone TokensConfigFlags = 0
```

```go
const TokensConfigFlagsRequireMetadata TokensConfigFlags = 1 << 0
```

```go
const TokensConfigFlagsRequireNFTMetaID TokensConfigFlags = 1 << 2
```

```go
const TokensConfigFlagsRequireNFTStandard TokensConfigFlags = 1 << 3
```

```go
const TokensConfigFlagsRequireSymbol TokensConfigFlags = 1 << 1
```

```go
const TxTypeBurnFungible
```

```go
const TxTypeBurnFungibleGasPayer
```

```go
const TxTypeBurnNonFungible
```

```go
const TxTypeBurnNonFungibleGasPayer
```

```go
const TxTypeCall TxType = iota
```

```go
const TxTypeCallMulti
```

```go
const TxTypeMintFungible
```

```go
const TxTypeMintNonFungible
```

```go
const TxTypePhantasma
```

```go
const TxTypePhantasmaRaw
```

```go
const TxTypeTrade
```

```go
const TxTypeTransferFungible
```

```go
const TxTypeTransferFungibleGasPayer
```

```go
const TxTypeTransferNonFungibleMulti
```

```go
const TxTypeTransferNonFungibleMultiGasPayer
```

```go
const TxTypeTransferNonFungibleSingle
```

```go
const TxTypeTransferNonFungibleSingleGasPayer
```

```go
const VMStructFlagsDynamicExtras VMStructFlags = 1 << 0
```

```go
const VMStructFlagsIsSorted VMStructFlags = 1 << 1
```

```go
const VMStructFlagsNone VMStructFlags = 0
```

```go
const VMTypeArray VMType = 1
```

```go
const VMTypeArrayBytes VMType = VMTypeArray | VMTypeBytes
```

```go
const VMTypeArrayBytes16 VMType = VMTypeArray | VMTypeBytes16
```

```go
const VMTypeArrayBytes32 VMType = VMTypeArray | VMTypeBytes32
```

```go
const VMTypeArrayBytes64 VMType = VMTypeArray | VMTypeBytes64
```

```go
const VMTypeArrayDynamic VMType = VMTypeArray | VMTypeDynamic
```

```go
const VMTypeArrayInt16 VMType = VMTypeArray | VMTypeInt16
```

```go
const VMTypeArrayInt256 VMType = VMTypeArray | VMTypeInt256
```

```go
const VMTypeArrayInt32 VMType = VMTypeArray | VMTypeInt32
```

```go
const VMTypeArrayInt64 VMType = VMTypeArray | VMTypeInt64
```

```go
const VMTypeArrayInt8 VMType = VMTypeArray | VMTypeInt8
```

```go
const VMTypeArrayString VMType = VMTypeArray | VMTypeString
```

```go
const VMTypeArrayStruct VMType = VMTypeArray | VMTypeStruct
```

```go
const VMTypeBytes VMType = 1 << 1
```

```go
const VMTypeBytes16 VMType = 8 << 1
```

```go
const VMTypeBytes32 VMType = 9 << 1
```

```go
const VMTypeBytes64 VMType = 10 << 1
```

```go
const VMTypeDynamic VMType = 0
```

```go
const VMTypeInt16 VMType = 4 << 1
```

```go
const VMTypeInt256 VMType = 7 << 1
```

```go
const VMTypeInt32 VMType = 5 << 1
```

```go
const VMTypeInt64 VMType = 6 << 1
```

```go
const VMTypeInt8 VMType = 3 << 1
```

```go
const VMTypeString VMType = 11 << 1
```

```go
const VMTypeStruct VMType = 2 << 1
```

```go
type Blob interface {
```

```go
type BurnFungibleArgs struct {
```

```go
type BurnNonFungibleArgs struct {
```

```go
type Bytes16 [16]byte
```

```go
type Bytes32 [32]byte
```

```go
type Bytes64 [64]byte
```

```go
type CallArgSection struct {
```

```go
type ChainConfig struct {
```

```go
type CreateMintedTokenSeriesArgs struct {
```

```go
type CreateSeriesFeeOptions struct {
```

```go
type CreateTokenFeeOptions struct {
```

```go
type CreateTokenSeriesArgs struct {
```

```go
type FeeOptions struct {
```

```go
type FieldType struct {
```

```go
type GasConfig struct {
```

```go
type IntX struct {
```

```go
type ListingType byte
```

```go
type MarketBuyTokenArgs struct {
```

```go
type MarketBuyTokenByIDArgs struct {
```

```go
type MarketCancelSaleArgs struct {
```

```go
type MarketCancelSaleByIDArgs struct {
```

```go
type MarketConfig struct {
```

```go
type MarketConfigFlags uint32
```

```go
type MarketContractMethod uint32
```

```go
type MarketGetTokenListingCountArgs struct {
```

```go
type MarketGetTokenListingInfoArgs struct {
```

```go
type MarketGetTokenListingInfoByIDArgs struct {
```

```go
type MarketSellTokenArgs struct {
```

```go
type MarketSellTokenByIDArgs struct {
```

```go
type MetadataField struct {
```

```go
type MintFungibleArgs struct {
```

```go
type MintNFTFeeOptions struct {
```

```go
type MintNonFungibleArgs struct {
```

```go
type MintPhantasmaNonFungibleArgs struct {
```

```go
type ModuleID uint32
```

```go
type MsgCallArgSections struct {
```

```go
type NFTMintInfo struct {
```

```go
type PhantasmaNFTMintInfo struct {
```

```go
type PhantasmaNFTMintResult struct {
```

```go
type Reader struct {
```

```go
type SeriesInfo struct {
```

```go
type SignedTxMsg struct {
```

```go
type SmallString string
```

```go
type TokenContractMethod uint32
```

```go
type TokenFlags byte
```

```go
type TokenInfo struct {
```

```go
type TokenListing struct {
```

```go
type TokenSchemas struct {
```

```go
type TokenSchemasJSON struct {
```

```go
type TokensConfig struct {
```

```go
type TokensConfigFlags byte
```

```go
type TransferFungibleArgs struct {
```

```go
type TransferNonFungibleArgs struct {
```

```go
type TxMsg struct {
```

```go
type TxMsgBurnFungible struct {
```

```go
type TxMsgBurnFungibleGasPayer struct {
```

```go
type TxMsgBurnNonFungible struct {
```

```go
type TxMsgBurnNonFungibleGasPayer struct {
```

```go
type TxMsgCall struct {
```

```go
type TxMsgCallMulti struct {
```

```go
type TxMsgMintFungible struct {
```

```go
type TxMsgMintNonFungible struct {
```

```go
type TxMsgPhantasma struct {
```

```go
type TxMsgPhantasmaRaw struct {
```

```go
type TxMsgTrade struct {
```

```go
type TxMsgTransferFungible struct {
```

```go
type TxMsgTransferFungibleGasPayer struct {
```

```go
type TxMsgTransferNonFungibleMulti struct {
```

```go
type TxMsgTransferNonFungibleMultiGasPayer struct {
```

```go
type TxMsgTransferNonFungibleSingle struct {
```

```go
type TxMsgTransferNonFungibleSingleGasPayer struct {
```

```go
type TxPayload interface {
```

```go
type TxType byte
```

```go
type UpdateSeriesMetadataArgs struct {
```

```go
type UpdateTokenMetadataArgs struct {
```

```go
type VMDynamicStruct struct {
```

```go
type VMDynamicVariable struct {
```

```go
type VMNamedDynamicVariable struct {
```

```go
type VMNamedVariableSchema struct {
```

```go
type VMStructArray struct {
```

```go
type VMStructFlags byte
```

```go
type VMStructSchema struct {
```

```go
type VMType byte
```

```go
type VMVariableSchema struct {
```

```go
type Witness struct {
```

```go
type Writer struct {
```

```go
var EmptyBytes16 Bytes16
```

```go
var EmptyBytes32 Bytes32
```

```go
var EmptyBytes64 Bytes64
```

```go
var SystemAddressDataPool = systemAddress(2)
```

```go
var SystemAddressGasPool = systemAddress(1)
```

```go
var SystemAddressNull = systemAddress(0)
```

### Fields

- `Address   Bytes32`
- `Address Bytes32`
- `AllowedTxTypes  uint32`
- `Amount  IntX`
- `Amount  uint64`
- `Args           []byte`
- `Args     []byte`
- `Blob`
- `BlockRateTarget uint32`
- `BurnF     []TxMsgBurnFungibleGasPayer`
- `BurnN     []TxMsgBurnNonFungibleGasPayer`
- `Calls []TxMsgCall`
- `CarbonInstanceID uint64`
- `Chain  SmallString`
- `Data any`
- `DataEscrowPerRow        uint64`
- `DataTokenID             uint64`
- `Decimals     byte`
- `DelistingGrace     uint64`
- `EndDate      int64`
- `EndDate     int64`
- `Expiry  int64`
- `ExpiryWindow    uint32`
- `FeeMultiplier           uint64`
- `FeeMultiplier          uint64`
- `FeeMultiplier uint64`
- `FeeShift                byte`
- `Fields []VMNamedDynamicVariable`
- `Fields []VMNamedVariableSchema`
- `Flags              MarketConfigFlags`
- `Flags        TokenFlags`
- `Flags  VMStructFlags`
- `Flags TokensConfigFlags`
- `From         Bytes32`
- `From        Bytes32`
- `From       Bytes32`
- `From    Bytes32`
- `GasBurnRatioMul         uint64`
- `GasBurnRatioShift       byte`
- `GasFeeBase              uint64`
- `GasFeeBase             uint64`
- `GasFeeBase    uint64`
- `GasFeeCreateSeriesBase uint64`
- `GasFeeCreateTokenBase   uint64`
- `GasFeeCreateTokenSeries uint64`
- `GasFeeCreateTokenSymbol uint64`
- `GasFeePerByte           uint64`
- `GasFeeQuery             uint64`
- `GasFeeRegisterName      uint64`
- `GasFeeTransfer          uint64`
- `GasFrom Bytes32`
- `GasTokenID              uint64`
- `Info    SeriesInfo`
- `InstanceID   uint64`
- `InstanceID  VMDynamicVariable`
- `InstanceID VMDynamicVariable`
- `InstanceID uint64`
- `InstanceIDs []uint64`
- `MaxData uint64`
- `MaxGas  uint64`
- `MaxMint   uint32`
- `MaxNameLength           byte`
- `MaxStructureSize        uint32`
- `MaxSupply    IntX`
- `MaxSupply uint32`
- `MaxTokenSymbolLength    byte`
- `MaximumListingTime uint64`
- `Metadata     []byte`
- `Metadata  []byte`
- `Metadata VMDynamicStruct`
- `Metadata []byte`
- `MethodID uint32`
- `MinimumGasOffer         uint64`
- `MinimumListingTime uint64`
- `MintF     []TxMsgMintFungible`
- `MintN     []TxMsgMintNonFungible`
- `ModuleID uint32`
- `Msg       TxMsg`
- `Msg     TxPayload`
- `Name   SmallString`
- `Name  SmallString`
- `Name  string`
- `Name string `json:"name"``
- `Nexus  SmallString`
- `Owner        Bytes32`
- `Owner     Bytes32`
- `Payload SmallString`
- `PhantasmaNFTID   Bytes32`
- `PhantasmaSeriesID IntX`
- `Price        IntX`
- `Price       IntX`
- `QuoteSymbol SmallString`
- `QuoteTokenID uint64`
- `RAM               []byte`
- `RAM            VMStructSchema`
- `RAM            []FieldType `json:"ram"``
- `RAM       VMStructSchema`
- `RAM      []byte`
- `RAMs    [][]byte`
- `ROM               []byte`
- `ROM            VMStructSchema`
- `ROM            []FieldType `json:"rom"``
- `ROM       VMStructSchema`
- `ROM      []byte`
- `ROMs    [][]byte`
- `ReadCarbon(*Reader)`
- `RegisterOffset int32`
- `Reserved1       byte`
- `Reserved2       byte`
- `Reserved3       byte`
- `Schema  VMStructSchema`
- `Schema VMVariableSchema`
- `Script []byte`
- `Sections *MsgCallArgSections`
- `Sections []CallArgSection`
- `Seller       Bytes32`
- `SeriesID uint32`
- `SeriesMetadata VMStructSchema`
- `SeriesMetadata []FieldType `json:"seriesMetadata"``
- `Signature Bytes64`
- `StartDate    int64`
- `StructDef *VMStructSchema`
- `Structs []VMDynamicStruct`
- `Symbol       SmallString`
- `Symbol      SmallString`
- `Symbol     SmallString`
- `To          Bytes32`
- `To         Bytes32`
- `To       Bytes32`
- `To      Bytes32`
- `TokenID      uint64`
- `TokenID     uint64`
- `TokenID    uint64`
- `TokenID  uint64`
- `TokenID uint64`
- `TokenSchemas []byte`
- `Tokens  []NFTMintInfo`
- `Tokens  []PhantasmaNFTMintInfo`
- `Transaction []byte`
- `TransferF []TxMsgTransferFungibleGasPayer`
- `TransferN []TxMsgTransferNonFungibleSingleGasPayer`
- `Type         ListingType`
- `Type      VMType`
- `Type    TxType`
- `Type VMType`
- `Type VMType `json:"type"``
- `Value VMDynamicVariable`
- `Value any`
- `Version                 byte`
- `Version         byte`
- `Witnesses []Witness`
- `WriteCarbon(*Writer)`

### Methods

```go
func (a *BurnFungibleArgs) ReadCarbon(r *Reader)
```

```go
func (a *BurnFungibleArgs) WriteCarbon(w *Writer)
```

```go
func (a *BurnNonFungibleArgs) ReadCarbon(r *Reader)
```

```go
func (a *BurnNonFungibleArgs) WriteCarbon(w *Writer)
```

```go
func (a *CreateMintedTokenSeriesArgs) ReadCarbon(r *Reader)
```

```go
func (a *CreateMintedTokenSeriesArgs) WriteCarbon(w *Writer)
```

```go
func (a *CreateTokenSeriesArgs) ReadCarbon(r *Reader)
```

```go
func (a *CreateTokenSeriesArgs) WriteCarbon(w *Writer)
```

```go
func (a *MarketBuyTokenArgs) ReadCarbon(r *Reader)
```

```go
func (a *MarketBuyTokenArgs) WriteCarbon(w *Writer)
```

```go
func (a *MarketBuyTokenByIDArgs) ReadCarbon(r *Reader)
```

```go
func (a *MarketBuyTokenByIDArgs) WriteCarbon(w *Writer)
```

```go
func (a *MarketCancelSaleArgs) ReadCarbon(r *Reader)
```

```go
func (a *MarketCancelSaleArgs) WriteCarbon(w *Writer)
```

```go
func (a *MarketCancelSaleByIDArgs) ReadCarbon(r *Reader)
```

```go
func (a *MarketCancelSaleByIDArgs) WriteCarbon(w *Writer)
```

```go
func (a *MarketGetTokenListingCountArgs) ReadCarbon(r *Reader)
```

```go
func (a *MarketGetTokenListingCountArgs) WriteCarbon(w *Writer)
```

```go
func (a *MarketGetTokenListingInfoArgs) ReadCarbon(r *Reader)
```

```go
func (a *MarketGetTokenListingInfoArgs) WriteCarbon(w *Writer)
```

```go
func (a *MarketGetTokenListingInfoByIDArgs) ReadCarbon(r *Reader)
```

```go
func (a *MarketGetTokenListingInfoByIDArgs) WriteCarbon(w *Writer)
```

```go
func (a *MarketSellTokenArgs) ReadCarbon(r *Reader)
```

```go
func (a *MarketSellTokenArgs) WriteCarbon(w *Writer)
```

```go
func (a *MarketSellTokenByIDArgs) ReadCarbon(r *Reader)
```

```go
func (a *MarketSellTokenByIDArgs) WriteCarbon(w *Writer)
```

```go
func (a *MintFungibleArgs) ReadCarbon(r *Reader)
```

```go
func (a *MintFungibleArgs) WriteCarbon(w *Writer)
```

```go
func (a *MintNonFungibleArgs) ReadCarbon(r *Reader)
```

```go
func (a *MintNonFungibleArgs) WriteCarbon(w *Writer)
```

```go
func (a *MintPhantasmaNonFungibleArgs) ReadCarbon(r *Reader)
```

```go
func (a *MintPhantasmaNonFungibleArgs) WriteCarbon(w *Writer)
```

```go
func (a *TransferFungibleArgs) ReadCarbon(r *Reader)
```

```go
func (a *TransferFungibleArgs) WriteCarbon(w *Writer)
```

```go
func (a *TransferNonFungibleArgs) ReadCarbon(r *Reader)
```

```go
func (a *TransferNonFungibleArgs) WriteCarbon(w *Writer)
```

```go
func (a *UpdateSeriesMetadataArgs) ReadCarbon(r *Reader)
```

```go
func (a *UpdateSeriesMetadataArgs) WriteCarbon(w *Writer)
```

```go
func (a *UpdateTokenMetadataArgs) ReadCarbon(r *Reader)
```

```go
func (a *UpdateTokenMetadataArgs) WriteCarbon(w *Writer)
```

```go
func (b *Bytes16) ReadCarbon(r *Reader)
```

```go
func (b *Bytes32) ReadCarbon(r *Reader)
```

```go
func (b *Bytes64) ReadCarbon(r *Reader)
```

```go
func (b Bytes16) Bytes() []byte
```

```go
func (b Bytes16) String() string
```

```go
func (b Bytes16) WriteCarbon(w *Writer)
```

```go
func (b Bytes32) Bytes() []byte
```

```go
func (b Bytes32) String() string
```

```go
func (b Bytes32) WriteCarbon(w *Writer)
```

```go
func (b Bytes64) Bytes() []byte
```

```go
func (b Bytes64) String() string
```

```go
func (b Bytes64) WriteCarbon(w *Writer)
```

```go
func (c *ChainConfig) ReadCarbon(r *Reader)
```

```go
func (c *ChainConfig) WriteCarbon(w *Writer)
```

```go
func (c *GasConfig) ReadCarbon(r *Reader)
```

```go
func (c *GasConfig) WriteCarbon(w *Writer)
```

```go
func (c *MarketConfig) ReadCarbon(r *Reader)
```

```go
func (c *MarketConfig) WriteCarbon(w *Writer)
```

```go
func (c *TokensConfig) ReadCarbon(r *Reader)
```

```go
func (c *TokensConfig) WriteCarbon(w *Writer)
```

```go
func (f *FieldType) UnmarshalJSON(data []byte) error
```

```go
func (f CreateSeriesFeeOptions) CalculateMaxGas() uint64
```

```go
func (f CreateTokenFeeOptions) CalculateMaxGas(symbol SmallString) uint64
```

```go
func (f FeeOptions) CalculateMaxGas() uint64
```

```go
func (f FeeOptions) CalculateMaxGasForCount(count uint64) (uint64, error)
```

```go
func (f FieldType) MarshalJSON() ([]byte, error)
```

```go
func (f MintNFTFeeOptions) CalculateMaxGasForCount(count uint64) (uint64, error)
```

```go
func (i *NFTMintInfo) ReadCarbon(r *Reader)
```

```go
func (i *NFTMintInfo) WriteCarbon(w *Writer)
```

```go
func (i *PhantasmaNFTMintInfo) ReadCarbon(r *Reader)
```

```go
func (i *PhantasmaNFTMintInfo) WriteCarbon(w *Writer)
```

```go
func (l *TokenListing) ReadCarbon(r *Reader)
```

```go
func (l *TokenListing) WriteCarbon(w *Writer)
```

```go
func (m *SignedTxMsg) ReadCarbon(r *Reader)
```

```go
func (m *SignedTxMsg) WriteCarbon(w *Writer)
```

```go
func (m *TxMsg) ReadCarbon(r *Reader)
```

```go
func (m *TxMsg) WriteCarbon(w *Writer)
```

```go
func (m *TxMsgBurnFungible) ReadCarbon(r *Reader)
```

```go
func (m *TxMsgBurnFungible) WriteCarbon(w *Writer)
```

```go
func (m *TxMsgBurnFungibleGasPayer) ReadCarbon(r *Reader)
```

```go
func (m *TxMsgBurnFungibleGasPayer) WriteCarbon(w *Writer)
```

```go
func (m *TxMsgBurnNonFungible) ReadCarbon(r *Reader)
```

```go
func (m *TxMsgBurnNonFungible) WriteCarbon(w *Writer)
```

```go
func (m *TxMsgBurnNonFungibleGasPayer) ReadCarbon(r *Reader)
```

```go
func (m *TxMsgBurnNonFungibleGasPayer) WriteCarbon(w *Writer)
```

```go
func (m *TxMsgCall) ReadCarbon(r *Reader)
```

```go
func (m *TxMsgCall) WriteCarbon(w *Writer)
```

```go
func (m *TxMsgCallMulti) ReadCarbon(r *Reader)
```

```go
func (m *TxMsgCallMulti) WriteCarbon(w *Writer)
```

```go
func (m *TxMsgMintFungible) ReadCarbon(r *Reader)
```

```go
func (m *TxMsgMintFungible) WriteCarbon(w *Writer)
```

```go
func (m *TxMsgMintNonFungible) ReadCarbon(r *Reader)
```

```go
func (m *TxMsgMintNonFungible) WriteCarbon(w *Writer)
```

```go
func (m *TxMsgPhantasma) ReadCarbon(r *Reader)
```

```go
func (m *TxMsgPhantasma) WriteCarbon(w *Writer)
```

```go
func (m *TxMsgPhantasmaRaw) ReadCarbon(r *Reader)
```

```go
func (m *TxMsgPhantasmaRaw) WriteCarbon(w *Writer)
```

```go
func (m *TxMsgTrade) ReadCarbon(r *Reader)
```

```go
func (m *TxMsgTrade) WriteCarbon(w *Writer)
```

```go
func (m *TxMsgTransferFungible) ReadCarbon(r *Reader)
```

```go
func (m *TxMsgTransferFungible) WriteCarbon(w *Writer)
```

```go
func (m *TxMsgTransferFungibleGasPayer) ReadCarbon(r *Reader)
```

```go
func (m *TxMsgTransferFungibleGasPayer) WriteCarbon(w *Writer)
```

```go
func (m *TxMsgTransferNonFungibleMulti) ReadCarbon(r *Reader)
```

```go
func (m *TxMsgTransferNonFungibleMulti) WriteCarbon(w *Writer)
```

```go
func (m *TxMsgTransferNonFungibleMultiGasPayer) ReadCarbon(r *Reader)
```

```go
func (m *TxMsgTransferNonFungibleMultiGasPayer) WriteCarbon(w *Writer)
```

```go
func (m *TxMsgTransferNonFungibleSingle) ReadCarbon(r *Reader)
```

```go
func (m *TxMsgTransferNonFungibleSingle) WriteCarbon(w *Writer)
```

```go
func (m *TxMsgTransferNonFungibleSingleGasPayer) ReadCarbon(r *Reader)
```

```go
func (m *TxMsgTransferNonFungibleSingleGasPayer) WriteCarbon(w *Writer)
```

```go
func (r *Reader) AssertEOF()
```

```go
func (r *Reader) Read1() byte
```

```go
func (r *Reader) Read16() Bytes16
```

```go
func (r *Reader) Read2() int16
```

```go
func (r *Reader) Read32() Bytes32
```

```go
func (r *Reader) Read4() int32
```

```go
func (r *Reader) Read4U() uint32
```

```go
func (r *Reader) Read64() Bytes64
```

```go
func (r *Reader) Read8() int64
```

```go
func (r *Reader) Read8U() uint64
```

```go
func (r *Reader) ReadBigInt() *big.Int
```

```go
func (r *Reader) ReadBigIntArray() []*big.Int
```

```go
func (r *Reader) ReadBigIntWithHeader(preReadHeader int) *big.Int
```

```go
func (r *Reader) ReadByteArray() []byte
```

```go
func (r *Reader) ReadByteArrays() [][]byte
```

```go
func (r *Reader) ReadInt16Array() []int16
```

```go
func (r *Reader) ReadInt32Array() []int32
```

```go
func (r *Reader) ReadInt64Array() []int64
```

```go
func (r *Reader) ReadInt8Array() []int8
```

```go
func (r *Reader) ReadLength() int
```

```go
func (r *Reader) ReadRaw(count int) []byte
```

```go
func (r *Reader) ReadStringZ() string
```

```go
func (r *Reader) ReadStringZArray() []string
```

```go
func (r *Reader) ReadUint64Array() []uint64
```

```go
func (r0 *PhantasmaNFTMintResult) ReadCarbon(r *Reader)
```

```go
func (r0 *PhantasmaNFTMintResult) WriteCarbon(w *Writer)
```

```go
func (s *MsgCallArgSections) ReadWithCount(r *Reader, countNegative int32)
```

```go
func (s *SeriesInfo) ReadCarbon(r *Reader)
```

```go
func (s *SeriesInfo) WriteCarbon(w *Writer)
```

```go
func (s *SmallString) ReadCarbon(r *Reader)
```

```go
func (s *TokenSchemas) ReadCarbon(r *Reader)
```

```go
func (s *TokenSchemas) WriteCarbon(w *Writer)
```

```go
func (s *VMDynamicStruct) Get(name string) *VMDynamicVariable
```

```go
func (s *VMDynamicStruct) ReadCarbon(r *Reader)
```

```go
func (s *VMDynamicStruct) ReadWithSchema(schema *VMStructSchema, r *Reader)
```

```go
func (s *VMDynamicStruct) WriteCarbon(w *Writer)
```

```go
func (s *VMDynamicStruct) WriteWithSchema(schema *VMStructSchema, w *Writer) bool
```

```go
func (s *VMNamedVariableSchema) ReadCarbon(r *Reader)
```

```go
func (s *VMNamedVariableSchema) WriteCarbon(w *Writer)
```

```go
func (s *VMStructSchema) ReadCarbon(r *Reader)
```

```go
func (s *VMStructSchema) WriteCarbon(w *Writer)
```

```go
func (s *VMVariableSchema) ReadCarbon(r *Reader)
```

```go
func (s *VMVariableSchema) WriteCarbon(w *Writer)
```

```go
func (s MsgCallArgSections) HasSections() bool
```

```go
func (s MsgCallArgSections) WriteCarbon(w *Writer)
```

```go
func (s SmallString) Bytes() []byte
```

```go
func (s SmallString) String() string
```

```go
func (s SmallString) WriteCarbon(w *Writer)
```

```go
func (t *TokenInfo) ReadCarbon(r *Reader)
```

```go
func (t *TokenInfo) WriteCarbon(w *Writer)
```

```go
func (v *VMDynamicVariable) ReadCarbon(r *Reader)
```

```go
func (v *VMDynamicVariable) ReadWithSchema(schema *VMVariableSchema, r *Reader)
```

```go
func (v *VMDynamicVariable) WriteCarbon(w *Writer)
```

```go
func (v *VMNamedDynamicVariable) ReadCarbon(r *Reader)
```

```go
func (v *VMNamedDynamicVariable) WriteCarbon(w *Writer)
```

```go
func (w *Writer) Bytes() []byte
```

```go
func (w *Writer) Write1(v byte)
```

```go
func (w *Writer) Write16(data Bytes16)
```

```go
func (w *Writer) Write2(v int16)
```

```go
func (w *Writer) Write32(data Bytes32)
```

```go
func (w *Writer) Write4(v int32)
```

```go
func (w *Writer) Write4U(v uint32)
```

```go
func (w *Writer) Write64(data Bytes64)
```

```go
func (w *Writer) Write8(v int64)
```

```go
func (w *Writer) Write8U(v uint64)
```

```go
func (w *Writer) WriteBigInt(value *big.Int)
```

```go
func (w *Writer) WriteBigIntArray(values []*big.Int)
```

```go
func (w *Writer) WriteBlob(blob Blob)
```

```go
func (w *Writer) WriteBlobArray(items []Blob)
```

```go
func (w *Writer) WriteByteArray(data []byte)
```

```go
func (w *Writer) WriteByteArrays(values [][]byte)
```

```go
func (w *Writer) WriteFixed(data []byte, count int)
```

```go
func (w *Writer) WriteInt16Array(values []int16)
```

```go
func (w *Writer) WriteInt32Array(values []int32)
```

```go
func (w *Writer) WriteInt64Array(values []int64)
```

```go
func (w *Writer) WriteInt8Array(values []int8)
```

```go
func (w *Writer) WriteRaw(data []byte)
```

```go
func (w *Writer) WriteStringZ(value string)
```

```go
func (w *Writer) WriteStringZArray(values []string)
```

```go
func (w *Writer) WriteUint64Array(values []uint64)
```

```go
func (witness *Witness) ReadCarbon(r *Reader)
```

```go
func (witness *Witness) WriteCarbon(w *Writer)
```

```go
func (x *IntX) ReadCarbon(r *Reader)
```

```go
func (x IntX) BigInt() *big.Int
```

```go
func (x IntX) Is8ByteSafe() bool
```

```go
func (x IntX) String() string
```

```go
func (x IntX) WriteCarbon(w *Writer)
```

```go
func BuildAndSerializeTokenSchemas(schemas *TokenSchemas) []byte
```

```go
func BuildCreateTokenSeriesTx(tokenID uint64, seriesInfo SeriesInfo, creator Bytes32, fees CreateSeriesFeeOptions, maxData uint64, expiry int64) TxMsg
```

```go
func BuildCreateTokenSeriesTxAndSign(tokenID uint64, seriesInfo SeriesInfo, signer cryptography.KeyPair, fees CreateSeriesFeeOptions, maxData uint64, expiry int64) ([]byte, error)
```

```go
func BuildCreateTokenSeriesTxAndSignHex(tokenID uint64, seriesInfo SeriesInfo, signer cryptography.KeyPair, fees CreateSeriesFeeOptions, maxData uint64, expiry int64) (string, error)
```

```go
func BuildCreateTokenTx(tokenInfo TokenInfo, creator Bytes32, fees CreateTokenFeeOptions, maxData uint64, expiry int64) TxMsg
```

```go
func BuildCreateTokenTxAndSign(tokenInfo TokenInfo, signer cryptography.KeyPair, fees CreateTokenFeeOptions, maxData uint64, expiry int64) ([]byte, error)
```

```go
func BuildCreateTokenTxAndSignHex(tokenInfo TokenInfo, signer cryptography.KeyPair, fees CreateTokenFeeOptions, maxData uint64, expiry int64) (string, error)
```

```go
func BuildMintNonFungibleTx(tokenID uint64, seriesID uint32, sender Bytes32, receiver Bytes32, rom []byte, ram []byte, fees MintNFTFeeOptions, maxData uint64, expiry int64) TxMsg
```

```go
func BuildMintNonFungibleTxAndSign(tokenID uint64, seriesID uint32, signer cryptography.KeyPair, receiver Bytes32, rom []byte, ram []byte, fees MintNFTFeeOptions, maxData uint64, expiry int64) ([]byte, error)
```

```go
func BuildMintNonFungibleTxAndSignHex(tokenID uint64, seriesID uint32, signer cryptography.KeyPair, receiver Bytes32, rom []byte, ram []byte, fees MintNFTFeeOptions, maxData uint64, expiry int64) (string, error)
```

```go
func BuildMintPhantasmaNonFungibleSingleTx(tokenID uint64, phantasmaSeriesID *big.Int, sender Bytes32, receiver Bytes32, publicRom []byte, ram []byte, fees MintNFTFeeOptions, maxData uint64, expiry int64) (TxMsg, error)
```

```go
func BuildMintPhantasmaNonFungibleSingleTxAndSign(tokenID uint64, phantasmaSeriesID *big.Int, signer cryptography.KeyPair, receiver Bytes32, publicRom []byte, ram []byte, fees MintNFTFeeOptions, maxData uint64, expiry int64) ([]byte, error)
```

```go
func BuildMintPhantasmaNonFungibleSingleTxAndSignHex(tokenID uint64, phantasmaSeriesID *big.Int, signer cryptography.KeyPair, receiver Bytes32, publicRom []byte, ram []byte, fees MintNFTFeeOptions, maxData uint64, expiry int64) (string, error)
```

```go
func BuildMintPhantasmaNonFungibleTx(tokenID uint64, sender Bytes32, receiver Bytes32, tokens []PhantasmaNFTMintInfo, fees MintNFTFeeOptions, maxData uint64, expiry int64) (TxMsg, error)
```

```go
func BuildMintPhantasmaNonFungibleTxAndSign(tokenID uint64, signer cryptography.KeyPair, receiver Bytes32, tokens []PhantasmaNFTMintInfo, fees MintNFTFeeOptions, maxData uint64, expiry int64) ([]byte, error)
```

```go
func BuildMintPhantasmaNonFungibleTxAndSignHex(tokenID uint64, signer cryptography.KeyPair, receiver Bytes32, tokens []PhantasmaNFTMintInfo, fees MintNFTFeeOptions, maxData uint64, expiry int64) (string, error)
```

```go
func BuildNFTRom(schema VMStructSchema, phantasmaNFTID *big.Int, metadata []MetadataField) ([]byte, error)
```

```go
func BuildPhantasmaNFTPublicMintSchema(nftRomSchema VMStructSchema) VMStructSchema
```

```go
func BuildPhantasmaNFTRom(nftRomSchema VMStructSchema, metadata []MetadataField) ([]byte, error)
```

```go
func BuildSeriesInfo(phantasmaSeriesID *big.Int, maxMint uint32, maxSupply uint32, owner Bytes32) (SeriesInfo, error)
```

```go
func BuildTokenInfo(symbol string, maxSupply IntX, isNFT bool, decimals byte, owner Bytes32, metadata []byte, schemas []byte) (TokenInfo, error)
```

```go
func BuildTokenMetadata(fields map[string]string) ([]byte, error)
```

```go
func BuildTokenSchemasFromFields(seriesMetadata []FieldType, rom []FieldType, ram []FieldType) (TokenSchemas, error)
```

```go
func BuildTokenSeriesMetadata(schema VMStructSchema, phantasmaSeriesID *big.Int, metadata []MetadataField) ([]byte, error)
```

```go
func Bytes16FromHex(value string) (Bytes16, error)
```

```go
func Bytes32FromHex(value string) (Bytes32, error)
```

```go
func Bytes32FromPhantasmaAddress(address cryptography.Address) (Bytes32, error)
```

```go
func Bytes32FromPhantasmaAddressText(text string) (Bytes32, error)
```

```go
func Bytes32FromPublicKey(publicKey []byte) (Bytes32, error)
```

```go
func Bytes64FromHex(value string) (Bytes64, error)
```

```go
func CheckTokenSymbol(symbol string) error
```

```go
func DecodeHex(value string) ([]byte, error)
```

```go
func DefaultCreateSeriesFeeOptions() CreateSeriesFeeOptions
```

```go
func DefaultCreateTokenFeeOptions() CreateTokenFeeOptions
```

```go
func DefaultFeeOptions() FeeOptions
```

```go
func DefaultMarketConfig() MarketConfig
```

```go
func DefaultMintNFTFeeOptions() MintNFTFeeOptions
```

```go
func GetNFTAddress(carbonTokenID uint64, instanceID uint64) Bytes32
```

```go
func IntXFromInt64(value int64) IntX
```

```go
func MustBuildMintPhantasmaNonFungibleSingleTx(tokenID uint64, phantasmaSeriesID *big.Int, sender Bytes32, receiver Bytes32, publicRom []byte, ram []byte, fees MintNFTFeeOptions, maxData uint64, expiry int64) TxMsg
```

```go
func MustBuildNFTRom(schema VMStructSchema, phantasmaNFTID *big.Int, metadata []MetadataField) []byte
```

```go
func MustBuildPhantasmaNFTRom(nftRomSchema VMStructSchema, metadata []MetadataField) []byte
```

```go
func MustBuildSeriesInfo(phantasmaSeriesID *big.Int, maxMint uint32, maxSupply uint32, owner Bytes32) SeriesInfo
```

```go
func MustBuildTokenMetadata(fields map[string]string) []byte
```

```go
func MustBuildTokenSeriesMetadata(schema VMStructSchema, phantasmaSeriesID *big.Int, metadata []MetadataField) []byte
```

```go
func MustBytes16(data []byte) Bytes16
```

```go
func MustBytes16FromHex(value string) Bytes16
```

```go
func MustBytes32(data []byte) Bytes32
```

```go
func MustBytes32FromHex(value string) Bytes32
```

```go
func MustBytes32FromPhantasmaAddress(address cryptography.Address) Bytes32
```

```go
func MustBytes32FromPhantasmaAddressText(text string) Bytes32
```

```go
func MustBytes32FromPublicKey(publicKey []byte) Bytes32
```

```go
func MustBytes64(data []byte) Bytes64
```

```go
func MustBytes64FromHex(value string) Bytes64
```

```go
func MustDecodeHex(value string) []byte
```

```go
func MustIntXFromString(value string) IntX
```

```go
func MustParseCreateTokenResult(resultHex string) uint64
```

```go
func MustParseCreateTokenSeriesResult(resultHex string) uint32
```

```go
func MustParseMintNonFungibleResult(carbonTokenID uint64, resultHex string) []Bytes32
```

```go
func MustParseMintPhantasmaNonFungibleResult(resultHex string) []PhantasmaNFTMintResult
```

```go
func MustSmallString(value string) SmallString
```

```go
func MustTokenSchemasFromJSON(data string) TokenSchemas
```

```go
func MustVMNamedDynamicVariable(name string, vmType VMType, value any) VMNamedDynamicVariable
```

```go
func MustVMNamedVariableSchema(name string, vmType VMType) VMNamedVariableSchema
```

```go
func NewBytes16(data []byte) (Bytes16, error)
```

```go
func NewBytes32(data []byte) (Bytes32, error)
```

```go
func NewBytes64(data []byte) (Bytes64, error)
```

```go
func NewCreateSeriesFeeOptions(gasFeeBase, feeMultiplier, createSeriesBase uint64) CreateSeriesFeeOptions
```

```go
func NewCreateTokenFeeOptions(gasFeeBase, feeMultiplier, createTokenBase, createTokenSymbol uint64) CreateTokenFeeOptions
```

```go
func NewFeeOptions(gasFeeBase, feeMultiplier uint64) FeeOptions
```

```go
func NewIntX(value *big.Int) IntX
```

```go
func NewMintNFTFeeOptions(gasFeeBase, feeMultiplier uint64) MintNFTFeeOptions
```

```go
func NewReader(data []byte) *Reader
```

```go
func NewSmallString(value string) (SmallString, error)
```

```go
func NewVMDynamicVariable(vmType VMType, value any) VMDynamicVariable
```

```go
func NewVMNamedDynamicVariable(name string, vmType VMType, value any) (VMNamedDynamicVariable, error)
```

```go
func NewVMNamedVariableSchema(name string, vmType VMType) (VMNamedVariableSchema, error)
```

```go
func NewVMVariableSchema(vmType VMType, structDef *VMStructSchema) VMVariableSchema
```

```go
func NewWriter() *Writer
```

```go
func NowUnixMillis() int64
```

```go
func ParseCreateTokenResult(resultHex string) (uint64, error)
```

```go
func ParseCreateTokenSeriesResult(resultHex string) (uint32, error)
```

```go
func ParseMintNonFungibleResult(carbonTokenID uint64, resultHex string) ([]Bytes32, error)
```

```go
func ParseMintPhantasmaNonFungibleResult(resultHex string) ([]PhantasmaNFTMintResult, error)
```

```go
func ParseTokenSchemasJSON(data string) (TokenSchemasJSON, error)
```

```go
func PrepareStandardTokenSchemas(sharedMetadata bool) TokenSchemas
```

```go
func Serialize(blob Blob) []byte
```

```go
func SerializeTokenSchemas(schemas TokenSchemas) []byte
```

```go
func SerializeTokenSchemasHex(schemas TokenSchemas) string
```

```go
func SignAndSerializeTxMsg(msg TxMsg, keys cryptography.KeyPair) ([]byte, error)
```

```go
func SignAndSerializeTxMsgHex(msg TxMsg, keys cryptography.KeyPair) (string, error)
```

```go
func SignTxMsg(msg TxMsg, keys cryptography.KeyPair) (SignedTxMsg, error)
```

```go
func TokenSchemasFromJSON(data string) (TokenSchemas, error)
```

```go
func UnpackNFTInstanceID(instanceID uint64) (seriesID uint32, mintNumber uint32)
```

```go
func VMTypeFromString(value string) (VMType, error)
```

```go
func VMTypeName(vmType VMType) (string, error)
```

```go
func VerifyTokenSchemas(schemas TokenSchemas) error
```

## github.com/phantasma-io/phantasma-sdk-go/pkg/cryptography

Source: `pkg/cryptography`

### Declarations

```go
const ECDSA
```

```go
const Ed25519
```

```go
const HashLength = 32
```

```go
const HexPrefix = "0x"
```

```go
const Interop AddressKind = 0x03
```

```go
const Invalid AddressKind = 0x00
```

```go
const Length = 34
```

```go
const None SignatureKind = iota
```

```go
const PrivateKeyLength = 32
```

```go
const Ring
```

```go
const System AddressKind = 0x02
```

```go
const User AddressKind = 0x01
```

```go
type Address struct {
```

```go
type AddressKind byte
```

```go
type Ed25519Signature struct {
```

```go
type Hash struct {
```

```go
type Hashable interface {
```

```go
type KeyPair interface {
```

```go
type PhantasmaKeys struct {
```

```go
type Signature interface {
```

```go
type SignatureKind uint
```

### Fields

- `Address() Address`
- `Bytes() []byte`
- `Deserialize(*io.BinReader)`
- `ExpandedPrivateKey() []byte`
- `Hash() Hash`
- `Kind() SignatureKind`
- `PrivateKey() []byte`
- `PublicKey() []byte`
- `Serialize(*io.BinWriter)`
- `Sign(msg []byte) (Signature, error)`
- `Verify(message []byte, addresses []Address) bool`

### Methods

```go
func (a *Address) Deserialize(reader *io.BinReader)
```

```go
func (a *Address) GetPublicKey() ([]byte, error)
```

```go
func (a *Address) Serialize(writer *io.BinWriter)
```

```go
func (a Address) Bytes() []byte
```

```go
func (a Address) BytesPrefixed() []byte
```

```go
func (a Address) IsNull() bool
```

```go
func (a Address) IsUser() bool
```

```go
func (a Address) Kind() AddressKind
```

```go
func (a Address) String() string
```

```go
func (a Address) Text() string
```

```go
func (h *Hash) Deserialize(reader *io.BinReader)
```

```go
func (h *Hash) Serialize(writer *io.BinWriter)
```

```go
func (h Hash) Bytes() []byte
```

```go
func (h Hash) FromUnpaddedHex(s string) (Hash, error)
```

```go
func (h Hash) GetDifficulty() int
```

```go
func (h Hash) IsNull() bool
```

```go
func (h Hash) Size() int
```

```go
func (h Hash) String() string
```

```go
func (k PhantasmaKeys) Address() Address
```

```go
func (k PhantasmaKeys) ExpandedPrivateKey() []byte
```

```go
func (k PhantasmaKeys) PrivateKey() []byte
```

```go
func (k PhantasmaKeys) PublicKey() []byte
```

```go
func (k PhantasmaKeys) Sign(msg []byte) (Signature, error)
```

```go
func (k PhantasmaKeys) String() string
```

```go
func (k PhantasmaKeys) WIF() string
```

```go
func (sig *Ed25519Signature) Deserialize(reader *io.BinReader)
```

```go
func (sig Ed25519Signature) Bytes() []byte
```

```go
func (sig Ed25519Signature) Kind() SignatureKind
```

```go
func (sig Ed25519Signature) Serialize(writer *io.BinWriter)
```

```go
func (sig Ed25519Signature) Verify(message []byte, addresses []Address) bool
```

```go
func FromKey(keyPair KeyPair) (Address, error)
```

```go
func FromString(s string) (Address, error)
```

```go
func FromWIF(wif string) (PhantasmaKeys, error)
```

```go
func GeneratePhantasmaKeys() (PhantasmaKeys, error)
```

```go
func HashFromBytes(data []byte) (Hash, error)
```

```go
func HashFromString(s string) Hash
```

```go
func IsValidAddress(text string) bool
```

```go
func MustAddressFromString(s string) Address
```

```go
func NewAddress(pubKey []byte) (Address, error)
```

```go
func NewEd25519Signature(bytes []byte) (*Ed25519Signature, error)
```

```go
func NewPhantasmaKeys(seed []byte) (PhantasmaKeys, error)
```

```go
func NullAddress() Address
```

```go
func ParseHash(s string) (Hash, error)
```

## github.com/phantasma-io/phantasma-sdk-go/pkg/cryptography/ecdsa

Source: `pkg/cryptography/ecdsa`

### Declarations

```go
const CompressedPublicKeySize = 33
```

```go
const PrefixedUncompressedPublicKeySize = 65
```

```go
const PrivateKeySize = 32
```

```go
const RecoverableSignatureSize = 65
```

```go
const Secp256k1 Curve = 1
```

```go
const Secp256r1 Curve = 0
```

```go
const SignatureSize = 64
```

```go
const UncompressedPublicKeySize = 64
```

```go
type Curve uint
```

### Methods

```go
func CompressPublicKey(uncompressedPublicKey []byte) ([]byte, error)
```

```go
func PrivateKeyUnmarshal(privKey []byte, curve elliptic.Curve) (*ecdsa.PrivateKey, error)
```

```go
func PublicKeyUnmarshal(pubKey []byte, curve elliptic.Curve) (*ecdsa.PublicKey, error)
```

```go
func RSToSignatureWithoutRecoveryID(r, s *big.Int) []byte
```

```go
func Sign(message, prikey []byte, curve Curve) ([]byte, error)
```

```go
func SignatureDropRecoveryID(signature []byte) []byte
```

```go
func SignatureToRS(signature []byte) (*big.Int, *big.Int, error)
```

```go
func UncompressedPublicKeyTo65Bytes(pubkey []byte) ([]byte, error)
```

```go
func Verify(message, signature, pubkey []byte, curve Curve) (bool, error)
```

## github.com/phantasma-io/phantasma-sdk-go/pkg/cryptography/neoLegacy

Source: `pkg/cryptography/neoLegacy`

### Declarations

```go
var Prefix = byte(0x17)
```

### Methods

```go
func Address(pubKey []byte) string
```

## github.com/phantasma-io/phantasma-sdk-go/pkg/cryptography/proofOfAddress

Source: `pkg/cryptography/proofOfAddress`

### Declarations

```go
type ProofOfAddressesVerifier struct {
```

### Fields

- `EthAddress        string`
- `EthPublicKey      string`
- `EthPublicKeyBytes []byte`
- `EthSignature       string`
- `EthSignatureBytes  []byte`
- `Message            string`
- `Neo2Address        string`
- `Neo2PublicKey      string`
- `Neo2PublicKeyBytes []byte`
- `Neo2Signature      string`
- `Neo2SignatureBytes []byte`
- `PhaAddress        string`
- `PhaPublicKeyBytes []byte`
- `PhaSignature       string`
- `PhaSignatureBytes  []byte`
- `SignedMessage      string`
- `SignedMessageBytes []byte`

### Methods

```go
func (v *ProofOfAddressesVerifier) VerifyMessage() (bool, string, error)
```

```go
func NewProofOfAddressesVerifier(message string) (*ProofOfAddressesVerifier, error)
```

## github.com/phantasma-io/phantasma-sdk-go/pkg/domain

Source: `pkg/domain`

### Declarations

```go
var SDKPayload []byte = []byte("GO-SDK-v0.9.0")
```

## github.com/phantasma-io/phantasma-sdk-go/pkg/domain/contract

Source: `pkg/domain/contract`

### Declarations

```go
const Duplicated TokenSeriesMode = 2
```

```go
const Unique TokenSeriesMode = 1
```

```go
type ContractEvent struct {
```

```go
type ContractInterface struct {
```

```go
type ContractInterface_S struct {
```

```go
type ContractMethod struct {
```

```go
type ContractMethod_S struct {
```

```go
type ContractParameter struct {
```

```go
type TokenContent struct {
```

```go
type TokenContent_S struct {
```

```go
type TokenInfusion struct {
```

```go
type TokenInfusion_S struct {
```

```go
type TokenSeries struct {
```

```go
type TokenSeriesMode uint
```

```go
type TokenSeries_S struct {
```

### Fields

- `ABI       ContractInterface`
- `Creator      string`
- `CurrentChain string`
- `CurrentOwner string`
- `Description []byte`
- `Events []ContractEvent`
- `Infusion     []TokenInfusion`
- `Infusion     []TokenInfusion_S`
- `MaxSupply *big.Int`
- `MaxSupply string`
- `Methods *orderedmap.OrderedMap[string, ContractMethod]`
- `Methods *orderedmap.OrderedMap[string, ContractMethod_S]`
- `MintCount *big.Int`
- `MintCount string`
- `MintID       *big.Int`
- `MintID       string`
- `Mode      TokenSeriesMode`
- `Name        string`
- `Name       string`
- `Name string`
- `Offset     int32`
- `Parameters []ContractParameter`
- `RAM          []byte`
- `ROM          []byte`
- `ROM       []byte`
- `ReturnType  vm.VMType`
- `ReturnType string`
- `ReturnType vm.VMType`
- `Script    []byte`
- `SeriesID     *big.Int`
- `SeriesID     string`
- `SeriesID *big.Int`
- `SeriesID string`
- `Symbol   string`
- `Symbol  string`
- `Symbol string`
- `Timestamp    *types.Timestamp`
- `TokenID *big.Int`
- `TokenID string`
- `Type vm.VMType`
- `Value       byte`
- `Value  *big.Int`
- `Value  string`

### Methods

```go
func (c *TokenContent) Deserialize(reader *io.BinReader)
```

```go
func (c *TokenContent) Serialize(writer *io.BinWriter)
```

```go
func (c *TokenContent_S) Deserialize(reader *io.BinReader)
```

```go
func (c *TokenContent_S) Serialize(writer *io.BinWriter)
```

```go
func (e *ContractEvent) Deserialize(reader *io.BinReader)
```

```go
func (e *ContractEvent) Serialize(writer *io.BinWriter)
```

```go
func (i *ContractInterface) Deserialize(reader *io.BinReader)
```

```go
func (i *ContractInterface) Serialize(writer *io.BinWriter)
```

```go
func (i *ContractInterface_S) Deserialize(reader *io.BinReader)
```

```go
func (i *ContractInterface_S) Serialize(writer *io.BinWriter)
```

```go
func (i *TokenInfusion) Deserialize(reader *io.BinReader)
```

```go
func (i *TokenInfusion) Serialize(writer *io.BinWriter)
```

```go
func (i *TokenInfusion_S) Deserialize(reader *io.BinReader)
```

```go
func (i *TokenInfusion_S) Serialize(writer *io.BinWriter)
```

```go
func (m *ContractMethod) Deserialize(reader *io.BinReader)
```

```go
func (m *ContractMethod) Serialize(writer *io.BinWriter)
```

```go
func (m *ContractMethod_S) Deserialize(reader *io.BinReader)
```

```go
func (m *ContractMethod_S) Serialize(writer *io.BinWriter)
```

```go
func (s *TokenSeries) Deserialize(reader *io.BinReader)
```

```go
func (s *TokenSeries) Serialize(writer *io.BinWriter)
```

```go
func (s *TokenSeries_S) Deserialize(reader *io.BinReader)
```

```go
func (s *TokenSeries_S) Serialize(writer *io.BinWriter)
```

## github.com/phantasma-io/phantasma-sdk-go/pkg/domain/event

Source: `pkg/domain/event`

### Declarations

```go
const AddressLink EventKind = 10
```

```go
const AddressMigration EventKind = 46
```

```go
const AddressRegister EventKind = 9
```

```go
const AddressUnlink EventKind = 11
```

```go
const AddressUnregister EventKind = 17
```

```go
const ChainCreate EventKind = 1
```

```go
const ChainSwap EventKind = 43
```

```go
const ChannelCreate EventKind = 36
```

```go
const ChannelRefill EventKind = 37
```

```go
const ChannelSettle EventKind = 38
```

```go
const Classic TypeAuction = 1
```

```go
const ContractDeploy EventKind = 45
```

```go
const ContractRegister EventKind = 44
```

```go
const ContractUpgrade EventKind = 47
```

```go
const Crowdsale EventKind = 58
```

```go
const CrownRewards EventKind = 56
```

```go
const Custom EventKind = 64
```

```go
const DomainCreate EventKind = 52
```

```go
const DomainDelete EventKind = 53
```

```go
const Dutch TypeAuction = 3
```

```go
const FeedCreate EventKind = 22
```

```go
const FeedUpdate EventKind = 23
```

```go
const FileCreate EventKind = 24
```

```go
const FileDelete EventKind = 25
```

```go
const Fixed TypeAuction = 0
```

```go
const GasEscrow EventKind = 15
```

```go
const GasPayment EventKind = 16
```

```go
const Inflation EventKind = 49
```

```go
const Infusion EventKind = 57
```

```go
const LeaderboardCreate EventKind = 39
```

```go
const LeaderboardInsert EventKind = 40
```

```go
const LeaderboardReset EventKind = 41
```

```go
const Log EventKind = 48
```

```go
const OrderBid EventKind = 59
```

```go
const OrderCancelled EventKind = 19
```

```go
const OrderClosed EventKind = 21
```

```go
const OrderCreated EventKind = 18
```

```go
const OrderFilled EventKind = 20
```

```go
const OrganizationAdd EventKind = 13
```

```go
const OrganizationCreate EventKind = 12
```

```go
const OrganizationRemove EventKind = 14
```

```go
const OwnerAdded EventKind = 50
```

```go
const OwnerRemoved EventKind = 51
```

```go
const PackedNFT EventKind = 30
```

```go
const PlatformCreate EventKind = 42
```

```go
const PollClosed EventKind = 34
```

```go
const PollCreated EventKind = 33
```

```go
const PollVote EventKind = 35
```

```go
const Reserve TypeAuction = 2
```

```go
const TaskStart EventKind = 54
```

```go
const TaskStop EventKind = 55
```

```go
const TokenBurn EventKind = 6
```

```go
const TokenClaim EventKind = 8
```

```go
const TokenCreate EventKind = 2
```

```go
const TokenMint EventKind = 5
```

```go
const TokenReceive EventKind = 4
```

```go
const TokenSend EventKind = 3
```

```go
const TokenStake EventKind = 7
```

```go
const Unknown EventKind = 0
```

```go
const ValidatorElect EventKind = 27
```

```go
const ValidatorPropose EventKind = 26
```

```go
const ValidatorRemove EventKind = 28
```

```go
const ValidatorSwitch EventKind = 29
```

```go
const ValueCreate EventKind = 31
```

```go
const ValueUpdate EventKind = 32
```

```go
type ChainValueEventData struct {
```

```go
type Event struct {
```

```go
type EventKind uint
```

```go
type GasEventData struct {
```

```go
type InfusionEventData struct {
```

```go
type MarketEventData struct {
```

```go
type OrganizationEventData struct {
```

```go
type TokenEventData struct {
```

```go
type TransactionSettleEventData struct {
```

```go
type TypeAuction uint
```

### Fields

- `Address  crypto.Address`
- `Address crypto.Address`
- `Amount  big.Int`
- `BaseSymbol    string`
- `BaseSymbol  string`
- `Chain    string`
- `ChainName     string`
- `ChainName string`
- `Contract string`
- `Data     []byte`
- `EndPrice    *big.Int`
- `Hash     crypto.Hash`
- `ID          *big.Int`
- `InfusedSymbol string`
- `InfusedValue  big.Int`
- `Kind     EventKind`
- `MemberAddress crypto.Address`
- `Name  string`
- `Organization  string`
- `Platform string`
- `Price       *big.Int`
- `Price   big.Int`
- `QuoteSymbol string`
- `Symbol    string`
- `TokenID       big.Int`
- `Type        TypeAuction`
- `Value     *big.Int`
- `Value big.Int`

### Methods

```go
func (d *MarketEventData) Deserialize(reader *io.BinReader)
```

```go
func (d *MarketEventData) Serialize(writer *io.BinWriter)
```

```go
func (e *Event) Deserialize(reader *io.BinReader)
```

```go
func (e *Event) Serialize(writer *io.BinWriter)
```

```go
func (e Event) String() string
```

```go
func (k *EventKind) SetString(eventKind string)
```

```go
func (k EventKind) IsMarketEvent() bool
```

```go
func (k EventKind) IsTokenEvent() bool
```

```go
func (k EventKind) String() string
```

```go
func (te *TokenEventData) Deserialize(reader *io.BinReader)
```

```go
func (te *TokenEventData) Serialize(writer *io.BinWriter)
```

## github.com/phantasma-io/phantasma-sdk-go/pkg/domain/stake

Source: `pkg/domain/stake`

### Declarations

```go
type EnergyClaim struct {
```

```go
type EnergyClaim_S struct {
```

```go
type EnergyStake struct {
```

```go
type EnergyStake_S struct {
```

### Fields

- `ClaimDate   *types.Timestamp`
- `IsNew       bool`
- `StakeAmount *big.Int`
- `StakeAmount string`
- `StakeTime   *types.Timestamp`

### Methods

```go
func (ec *EnergyClaim) Deserialize(reader *io.BinReader)
```

```go
func (ec *EnergyClaim) Serialize(writer *io.BinWriter)
```

```go
func (ec *EnergyClaim_S) Deserialize(reader *io.BinReader)
```

```go
func (ec *EnergyClaim_S) Serialize(writer *io.BinWriter)
```

```go
func (es *EnergyStake) Deserialize(reader *io.BinReader)
```

```go
func (es *EnergyStake) Serialize(writer *io.BinWriter)
```

```go
func (es *EnergyStake_S) Deserialize(reader *io.BinReader)
```

```go
func (es *EnergyStake_S) Serialize(writer *io.BinWriter)
```

## github.com/phantasma-io/phantasma-sdk-go/pkg/domain/token

Source: `pkg/domain/token`

### Declarations

```go
const Burnable TokenFlags = 1 << 8
```

```go
const Divisible TokenFlags = 1 << 3
```

```go
const Fiat TokenFlags = 1 << 6
```

```go
const Finite TokenFlags = 1 << 2
```

```go
const Fuel TokenFlags = 1 << 4
```

```go
const Fungible TokenFlags = 1 << 1
```

```go
const Mintable TokenFlags = 1 << 9
```

```go
const None TokenFlags = 0
```

```go
const Stakable TokenFlags = 1 << 5
```

```go
const Swappable TokenFlags = 1 << 7
```

```go
const Transferable TokenFlags = 1 << 0
```

```go
type TokenFlags uint
```

```go
type TokenInfo struct {
```

```go
type TokenInfo_S struct {
```

### Fields

- `ABI       contract.ContractInterface`
- `ABI       contract.ContractInterface_S`
- `Decimals  int32`
- `Flags     TokenFlags`
- `Flags     []string`
- `MaxSupply *big.Int`
- `MaxSupply string`
- `Name      string`
- `Owner     cryptography.Address`
- `Script    []byte`
- `Symbol    string`

### Methods

```go
func (tf TokenFlags) FromSlice(flagsSlice []string) TokenFlags
```

```go
func (tf TokenFlags) ToSlice() []string
```

```go
func (ti *TokenInfo) Deserialize(reader *io.BinReader)
```

```go
func (ti *TokenInfo) Serialize(writer *io.BinWriter)
```

```go
func (ti *TokenInfo_S) Deserialize(reader *io.BinReader)
```

```go
func (ti *TokenInfo_S) Serialize(writer *io.BinWriter)
```

## github.com/phantasma-io/phantasma-sdk-go/pkg/domain/types

Source: `pkg/domain/types`

### Declarations

```go
type Timestamp struct {
```

### Fields

- `Value uint32`

### Methods

```go
func NewTimestamp(value uint32) *Timestamp
```

## github.com/phantasma-io/phantasma-sdk-go/pkg/encoding/base58

Source: `pkg/encoding/base58`

### Methods

```go
func CheckDecode(s string) (b []byte, err error)
```

```go
func CheckEncode(b []byte) string
```

```go
func Decode(s string) (b []byte, err error)
```

```go
func Encode(b []byte) string
```

## github.com/phantasma-io/phantasma-sdk-go/pkg/io

Source: `pkg/io`

### Declarations

```go
const MaxArraySize = 0x1000000
```

```go
type BinReader struct {
```

```go
type BinWriter struct {
```

```go
type BufBinWriter struct {
```

```go
type Serializer interface {
```

### Fields

- `Count int`
- `Deserialize(*BinReader)`
- `Err   error`
- `Err error`
- `Serialize(*BinWriter)`

### Methods

```go
func (bw *BufBinWriter) Bytes() []byte
```

```go
func (bw *BufBinWriter) Len() int
```

```go
func (bw *BufBinWriter) Reset()
```

```go
func (cw *counterWriter) Write(p []byte) (int, error)
```

```go
func (r *BinReader) ReadArray(t interface{}, maxSize ...int)
```

```go
func (r *BinReader) ReadB() byte
```

```go
func (r *BinReader) ReadBigInteger() *big.Int
```

```go
func (r *BinReader) ReadBigIntegerToString() string
```

```go
func (r *BinReader) ReadBool() bool
```

```go
func (r *BinReader) ReadBytes(buf []byte)
```

```go
func (r *BinReader) ReadString() string
```

```go
func (r *BinReader) ReadTimestamp() *types.Timestamp
```

```go
func (r *BinReader) ReadU16BE() uint16
```

```go
func (r *BinReader) ReadU16LE() uint16
```

```go
func (r *BinReader) ReadU32LE() uint32
```

```go
func (r *BinReader) ReadU64LE() uint64
```

```go
func (r *BinReader) ReadVarBytes(maxSize ...int) []byte
```

```go
func (r *BinReader) ReadVarUint() uint64
```

```go
func (w *BinWriter) WriteArray(arr interface{})
```

```go
func (w *BinWriter) WriteB(u8 byte)
```

```go
func (w *BinWriter) WriteBigInteger(n *big.Int)
```

```go
func (w *BinWriter) WriteBigIntegerFromString(n string)
```

```go
func (w *BinWriter) WriteBool(b bool)
```

```go
func (w *BinWriter) WriteBytes(b []byte)
```

```go
func (w *BinWriter) WriteOp(value byte)
```

```go
func (w *BinWriter) WriteString(s string)
```

```go
func (w *BinWriter) WriteTimestamp(t *types.Timestamp)
```

```go
func (w *BinWriter) WriteU16BE(u16 uint16)
```

```go
func (w *BinWriter) WriteU16LE(u16 uint16)
```

```go
func (w *BinWriter) WriteU32LE(u32 uint32)
```

```go
func (w *BinWriter) WriteU64LE(u64 uint64)
```

```go
func (w *BinWriter) WriteVarBytes(b []byte)
```

```go
func (w *BinWriter) WriteVarUint(val uint64)
```

```go
func GetVarSize(value interface{}) int
```

```go
func MakeDirForFile(filePath string, creator string) error
```

```go
func NewBinReaderFromBuf(b []byte) *BinReader
```

```go
func NewBinReaderFromIO(ior io.Reader) *BinReader
```

```go
func NewBinWriterFromIO(iow io.Writer) *BinWriter
```

```go
func NewBufBinWriter() *BufBinWriter
```

## github.com/phantasma-io/phantasma-sdk-go/pkg/jsonrpc

Source: `pkg/jsonrpc`

### Declarations

```go
type HTTPError struct {
```

```go
type RPCClient interface {
```

```go
type RPCClientOpts struct {
```

```go
type RPCError struct {
```

```go
type RPCRequest struct {
```

```go
type RPCRequests []*RPCRequest
```

```go
type RPCResponse struct {
```

```go
type RPCResponses []*RPCResponse
```

### Fields

- `AllowUnknownFields bool`
- `Code    int         `json:"code"``
- `Code int`
- `CustomHeaders      map[string]string`
- `Data    interface{} `json:"data,omitempty"``
- `DefaultRequestID   int`
- `Error   *RPCError   `json:"error,omitempty"``
- `HTTPClient         *http.Client`
- `ID      int         `json:"id"``
- `ID      string      `json:"id"``
- `JSONRPC string      `json:"jsonrpc"``
- `Message string      `json:"message"``
- `Method  string      `json:"method"``
- `Params  interface{} `json:"params,omitempty"``
- `Result  interface{} `json:"result,omitempty"``

### Methods

```go
func (RPCResponse *RPCResponse) GetBool() (bool, error)
```

```go
func (RPCResponse *RPCResponse) GetFloat() (float64, error)
```

```go
func (RPCResponse *RPCResponse) GetInt() (int64, error)
```

```go
func (RPCResponse *RPCResponse) GetObject(toType interface{}) error
```

```go
func (RPCResponse *RPCResponse) GetString() (string, error)
```

```go
func (client *rpcClient) Call(ctx context.Context, method string, params ...interface{}) (*RPCResponse, error)
```

```go
func (client *rpcClient) CallBatch(ctx context.Context, requests RPCRequests) (RPCResponses, error)
```

```go
func (client *rpcClient) CallBatchRaw(ctx context.Context, requests RPCRequests) (RPCResponses, error)
```

```go
func (client *rpcClient) CallFor(ctx context.Context, out interface{}, method string, params ...interface{}) error
```

```go
func (client *rpcClient) CallRaw(ctx context.Context, request *RPCRequest) (*RPCResponse, error)
```

```go
func (e *HTTPError) Error() string
```

```go
func (e *RPCError) Error() string
```

```go
func (id *rpcResponseID) UnmarshalJSON(data []byte) error
```

```go
func (res RPCResponses) AsMap() map[int]*RPCResponse
```

```go
func (res RPCResponses) GetByID(id int) *RPCResponse
```

```go
func (res RPCResponses) HasError() bool
```

```go
func NewClient(endpoint string) RPCClient
```

```go
func NewClientWithOpts(endpoint string, opts *RPCClientOpts) RPCClient
```

```go
func NewRequest(method string, params ...interface{}) *RPCRequest
```

```go
func NewRequestWithID(id int, method string, params ...interface{}) *RPCRequest
```

```go
func Params(params ...interface{}) interface
```

## github.com/phantasma-io/phantasma-sdk-go/pkg/rpc

Source: `pkg/rpc`

### Declarations

```go
const AddressTypeCarbon
```

```go
const AddressTypePhantasma AddressType = iota
```

```go
type AddressType int
```

```go
type PhantasmaRPC struct {
```

### Methods

```go
func (rpc PhantasmaRPC) Call(ctx context.Context, method string, params ...interface{}) (*jsonrpc.RPCResponse, error)
```

```go
func (rpc PhantasmaRPC) GetAccount(ctx context.Context, address string) (resp.AccountResult, error)
```

```go
func (rpc PhantasmaRPC) GetAccountFungibleTokens(ctx context.Context, account string, tokenSymbol string, carbonTokenID uint64, pageSize int, cursor string, checkAddressReservedByte bool) (resp.CursorPaginatedResult[[]resp.BalanceResult], error)
```

```go
func (rpc PhantasmaRPC) GetAccountFungibleTokensWithAddressType(ctx context.Context, account string, tokenSymbol string, carbonTokenID uint64, pageSize int, cursor string, checkAddressReservedByte bool, addressType AddressType) (resp.CursorPaginatedResult[[]resp.BalanceResult], error)
```

```go
func (rpc PhantasmaRPC) GetAccountNFTs(ctx context.Context, account string, tokenSymbol string, carbonTokenID uint64, carbonSeriesID uint32, pageSize int, cursor string, extended bool, checkAddressReservedByte bool) (resp.CursorPaginatedResult[[]resp.TokenDataResult], error)
```

```go
func (rpc PhantasmaRPC) GetAccountNFTsWithAddressType(ctx context.Context, account string, tokenSymbol string, carbonTokenID uint64, carbonSeriesID uint32, pageSize int, cursor string, extended bool, checkAddressReservedByte bool, addressType AddressType) (resp.CursorPaginatedResult[[]resp.TokenDataResult], error)
```

```go
func (rpc PhantasmaRPC) GetAccountOwnedTokenSeries(ctx context.Context, account string, tokenSymbol string, carbonTokenID uint64, pageSize int, cursor string, checkAddressReservedByte bool) (resp.CursorPaginatedResult[[]resp.TokenSeriesResult], error)
```

```go
func (rpc PhantasmaRPC) GetAccountOwnedTokenSeriesWithAddressType(ctx context.Context, account string, tokenSymbol string, carbonTokenID uint64, pageSize int, cursor string, checkAddressReservedByte bool, addressType AddressType) (resp.CursorPaginatedResult[[]resp.TokenSeriesResult], error)
```

```go
func (rpc PhantasmaRPC) GetAccountOwnedTokens(ctx context.Context, account string, tokenSymbol string, carbonTokenID uint64, pageSize int, cursor string, checkAddressReservedByte bool) (resp.CursorPaginatedResult[[]resp.TokenResult], error)
```

```go
func (rpc PhantasmaRPC) GetAccountOwnedTokensWithAddressType(ctx context.Context, account string, tokenSymbol string, carbonTokenID uint64, pageSize int, cursor string, checkAddressReservedByte bool, addressType AddressType) (resp.CursorPaginatedResult[[]resp.TokenResult], error)
```

```go
func (rpc PhantasmaRPC) GetAccountWithAddressType(ctx context.Context, address string, extended bool, checkAddressReservedByte bool, addressType AddressType) (resp.AccountResult, error)
```

```go
func (rpc PhantasmaRPC) GetAccounts(ctx context.Context, addresses ...string) ([]resp.AccountResult, error)
```

```go
func (rpc PhantasmaRPC) GetAccountsText(ctx context.Context, addresses string) ([]resp.AccountResult, error)
```

```go
func (rpc PhantasmaRPC) GetAccountsWithAddressType(ctx context.Context, addresses []string, extended bool, checkAddressReservedByte bool, addressType AddressType) ([]resp.AccountResult, error)
```

```go
func (rpc PhantasmaRPC) GetAddressTransactionCount(ctx context.Context, address string, chainName string) (int, error)
```

```go
func (rpc PhantasmaRPC) GetAddressTransactions(ctx context.Context, address string, page int, pageSize int) (resp.PaginatedResult[resp.AddressTransactionsResult], error)
```

```go
func (rpc PhantasmaRPC) GetArchive(ctx context.Context, hash string) (resp.ArchiveResult, error)
```

```go
func (rpc PhantasmaRPC) GetAuction(ctx context.Context, chainAddressOrName string, symbol string, tokenID string) (resp.AuctionResult, error)
```

```go
func (rpc PhantasmaRPC) GetAuctions(ctx context.Context, chainAddressOrName string, symbol string, page int, pageSize int) (resp.PaginatedResult[[]resp.AuctionResult], error)
```

```go
func (rpc PhantasmaRPC) GetAuctionsCount(ctx context.Context, chainAddressOrName string, symbol string) (int, error)
```

```go
func (rpc PhantasmaRPC) GetBlockByHash(ctx context.Context, blockHash string) (resp.BlockResult, error)
```

```go
func (rpc PhantasmaRPC) GetBlockByHeight(ctx context.Context, chain string, height string) (resp.BlockResult, error)
```

```go
func (rpc PhantasmaRPC) GetBlockHeight(ctx context.Context, chainName string) (*big.Int, error)
```

```go
func (rpc PhantasmaRPC) GetBlockTransactionCountByHash(ctx context.Context, blockHash string) (int, error)
```

```go
func (rpc PhantasmaRPC) GetBlockTransactionCountByHashOnChain(ctx context.Context, chainAddressOrName string, blockHash string) (int, error)
```

```go
func (rpc PhantasmaRPC) GetChain(ctx context.Context, name string, extended bool) (resp.ChainResult, error)
```

```go
func (rpc PhantasmaRPC) GetChains(ctx context.Context, extended bool) ([]resp.ChainResult, error)
```

```go
func (rpc PhantasmaRPC) GetContract(ctx context.Context, name, chainName string) (resp.ContractResult, error)
```

```go
func (rpc PhantasmaRPC) GetContractByAddress(ctx context.Context, chainAddressOrName string, contractAddress string) (resp.ContractResult, error)
```

```go
func (rpc PhantasmaRPC) GetContractByName(ctx context.Context, chainAddressOrName string, contractName string) (resp.ContractResult, error)
```

```go
func (rpc PhantasmaRPC) GetContracts(ctx context.Context, chainAddressOrName string, extended bool) ([]resp.ContractResult, error)
```

```go
func (rpc PhantasmaRPC) GetLatestBlock(ctx context.Context, chainAddressOrName string) (resp.BlockResult, error)
```

```go
func (rpc PhantasmaRPC) GetLeaderboard(ctx context.Context, name string) (resp.LeaderboardResult, error)
```

```go
func (rpc PhantasmaRPC) GetNFT(ctx context.Context, symbol string, tokenID string, extended bool) (resp.TokenDataResult, error)
```

```go
func (rpc PhantasmaRPC) GetNFTs(ctx context.Context, symbol string, tokenIDs []string, extended bool) ([]resp.TokenDataResult, error)
```

```go
func (rpc PhantasmaRPC) GetNFTsText(ctx context.Context, symbol string, tokenIDs string, extended bool) ([]resp.TokenDataResult, error)
```

```go
func (rpc PhantasmaRPC) GetNexus(ctx context.Context, extended bool) (resp.NexusResult, error)
```

```go
func (rpc PhantasmaRPC) GetOrganization(ctx context.Context, id string, extended bool) (resp.OrganizationResult, error)
```

```go
func (rpc PhantasmaRPC) GetOrganizationByName(ctx context.Context, name string, extended bool) (resp.OrganizationResult, error)
```

```go
func (rpc PhantasmaRPC) GetOrganizations(ctx context.Context, extended bool) ([]resp.OrganizationResult, error)
```

```go
func (rpc PhantasmaRPC) GetPhantasmaVMConfig(ctx context.Context, chainAddressOrName string) (resp.PhantasmaVMConfigResult, error)
```

```go
func (rpc PhantasmaRPC) GetPlatforms(ctx context.Context) ([]resp.PlatformResult, error)
```

```go
func (rpc PhantasmaRPC) GetToken(ctx context.Context, symbol string, extended bool) (resp.TokenResult, error)
```

```go
func (rpc PhantasmaRPC) GetTokenBalance(ctx context.Context, address string, tokenSymbol string, chainAddressOrName string) (resp.BalanceResult, error)
```

```go
func (rpc PhantasmaRPC) GetTokenBalanceChecked(ctx context.Context, address string, tokenSymbol string, chainAddressOrName string, checkAddressReservedByte bool) (resp.BalanceResult, error)
```

```go
func (rpc PhantasmaRPC) GetTokenBalanceWithAddressType(ctx context.Context, address string, tokenSymbol string, chainAddressOrName string, checkAddressReservedByte bool, addressType AddressType) (resp.BalanceResult, error)
```

```go
func (rpc PhantasmaRPC) GetTokenData(ctx context.Context, symbol string, tokenID string) (resp.TokenDataResult, error)
```

```go
func (rpc PhantasmaRPC) GetTokenNFTs(ctx context.Context, carbonTokenID uint64, carbonSeriesID uint32, pageSize int, cursor string, extended bool) (resp.CursorPaginatedResult[[]resp.TokenDataResult], error)
```

```go
func (rpc PhantasmaRPC) GetTokenNFTsWithSeriesID(ctx context.Context, carbonTokenID uint64, carbonSeriesID uint32, seriesID string, pageSize int, cursor string, extended bool) (resp.CursorPaginatedResult[[]resp.TokenDataResult], error)
```

```go
func (rpc PhantasmaRPC) GetTokenSeries(ctx context.Context, symbol string, carbonTokenID uint64, pageSize int, cursor string) (resp.CursorPaginatedResult[[]resp.TokenSeriesResult], error)
```

```go
func (rpc PhantasmaRPC) GetTokenSeriesByID(ctx context.Context, symbol string, carbonTokenID uint64, seriesID string, carbonSeriesID uint32) (resp.TokenSeriesResult, error)
```

```go
func (rpc PhantasmaRPC) GetTokenWithID(ctx context.Context, symbol string, extended bool, carbonTokenID uint64) (resp.TokenResult, error)
```

```go
func (rpc PhantasmaRPC) GetTokens(ctx context.Context, extended bool) ([]resp.TokenResult, error)
```

```go
func (rpc PhantasmaRPC) GetTokensAsMap(ctx context.Context, extended bool) (map[string]resp.TokenResult, error)
```

```go
func (rpc PhantasmaRPC) GetTokensByOwner(ctx context.Context, extended bool, ownerAddress string) ([]resp.TokenResult, error)
```

```go
func (rpc PhantasmaRPC) GetTokensByOwnerWithAddressType(ctx context.Context, extended bool, ownerAddress string, addressType AddressType) ([]resp.TokenResult, error)
```

```go
func (rpc PhantasmaRPC) GetTransaction(ctx context.Context, txHash string) (resp.TransactionResult, error)
```

```go
func (rpc PhantasmaRPC) GetTransactionByBlockHashAndIndex(ctx context.Context, blockHash string, index int) (resp.TransactionResult, error)
```

```go
func (rpc PhantasmaRPC) GetTransactionByBlockHashAndIndexOnChain(ctx context.Context, chainAddressOrName string, blockHash string, index int) (resp.TransactionResult, error)
```

```go
func (rpc PhantasmaRPC) GetVersion(ctx context.Context) (resp.BuildInfoResult, error)
```

```go
func (rpc PhantasmaRPC) InvokeRawScript(ctx context.Context, chain, script string) (resp.ScriptResult, error)
```

```go
func (rpc PhantasmaRPC) LookupName(ctx context.Context, name string) (string, error)
```

```go
func (rpc PhantasmaRPC) ReadArchive(ctx context.Context, hash string, blockIndex int) (string, error)
```

```go
func (rpc PhantasmaRPC) SendCarbonTransaction(ctx context.Context, txData string) (string, error)
```

```go
func (rpc PhantasmaRPC) SendRawTransaction(ctx context.Context, txData string) (string, error)
```

```go
func (rpc PhantasmaRPC) SignAndSendBuiltTransaction(ctx context.Context, tx chain.Transaction, keys cryptography.KeyPair) (string, error)
```

```go
func (rpc PhantasmaRPC) SignAndSendCarbonTransaction(ctx context.Context, msg carbon.TxMsg, keys cryptography.KeyPair) (string, error)
```

```go
func (rpc PhantasmaRPC) SignAndSendTransaction(ctx context.Context, keys cryptography.KeyPair, nexus string, script []byte, chainName string, payload []byte) (string, error)
```

```go
func (rpc PhantasmaRPC) SignAndSendTransactionTextPayload(ctx context.Context, keys cryptography.KeyPair, nexus string, script []byte, chainName string, payload string) (string, error)
```

```go
func (rpc PhantasmaRPC) SignAndSendTransactionWithExpiration(ctx context.Context, keys cryptography.KeyPair, nexus string, script []byte, chainName string, payload []byte, expiration uint32) (string, error)
```

```go
func (rpc PhantasmaRPC) WriteArchive(ctx context.Context, hash string, blockIndex int, blockContent []byte) (bool, error)
```

```go
func (rpc PhantasmaRPC) WriteArchiveBase64(ctx context.Context, hash string, blockIndex int, blockContent string) (bool, error)
```

```go
func NewRPC(endpoint string) PhantasmaRPC
```

```go
func NewRPCMainnet() PhantasmaRPC
```

```go
func NewRPCSetMainnet() []PhantasmaRPC
```

```go
func NewRPCTestnet() PhantasmaRPC
```

## github.com/phantasma-io/phantasma-sdk-go/pkg/rpc/response

Source: `pkg/rpc/response`

### Declarations

```go
type ABIEventResult struct {
```

```go
type ABIMethodResult struct {
```

```go
type ABIParameterResult struct {
```

```go
type AccountResult struct {
```

```go
type AddressTransactionsResult struct {
```

```go
type ArchiveResult struct {
```

```go
type AuctionResult struct {
```

```go
type BalanceResult struct {
```

```go
type BlockResult struct {
```

```go
type BuildInfoResult struct {
```

```go
type ChainResult struct {
```

```go
type ChannelResult struct {
```

```go
type ContractResult struct {
```

```go
type CrowdsaleResult struct {
```

```go
type DappResult struct {
```

```go
type ErrorResult struct {
```

```go
type EventResult struct {
```

```go
type GovernanceResult struct {
```

```go
type InteropResult struct {
```

```go
type LeaderboardResult struct {
```

```go
type LeaderboardRowResult struct {
```

```go
type NexusResult struct {
```

```go
type OracleResult struct {
```

```go
type OrganizationResult struct {
```

```go
type PeerResult struct {
```

```go
type PhantasmaVMConfigResult struct {
```

```go
type PlatformResult struct {
```

```go
type ReceiptResult struct {
```

```go
type ScriptResult struct {
```

```go
type SendRawTxResult struct {
```

```go
type SignatureResult struct {
```

```go
type SingleResult struct {
```

```go
type StakeResult struct {
```

```go
type StorageResult struct {
```

```go
type SwapResult struct {
```

```go
type TokenDataResult struct {
```

```go
type TokenExternalResult struct {
```

```go
type TokenPriceResult struct {
```

```go
type TokenPropertyResult struct {
```

```go
type TokenResult struct {
```

```go
type TokenSchemasResult struct {
```

```go
type TokenSeriesResult struct {
```

```go
type TransactionResult struct {
```

```go
type VMNamedVariableSchemaResult struct {
```

```go
type VMStructSchemaResult struct {
```

```go
type VMVariableSchemaResult struct {
```

```go
type ValidatorResult struct {
```

### Fields

- `Active         bool   `json:"active"``
- `Address       string                `json:"address"``
- `Address      string   `json:"address"``
- `Address   string          `json:"address"``
- `Address  string `json:"address"``
- `Address string              `json:"address"``
- `Address string            `json:"address"``
- `Address string `json:"address"``
- `Amount    string `json:"amount"``
- `Amount   string   `json:"amount"``
- `Archives  []ArchiveResult `json:"archives"``
- `Available uint            `json:"available"``
- `Avatar    string          `json:"avatar"``
- `Balance        string `json:"balance"``
- `Balances  []BalanceResult `json:"balances"``
- `BaseSymbol      string `json:"baseSymbol"``
- `BlockCount    int      `json:"blockCount"``
- `BlockHash    string            `json:"blockHash"``
- `BlockHeight  int               `json:"blockHeight"``
- `BuildTimeUTC string `json:"buildTimeUtc"``
- `BurnedSupply   string                `json:"burnedSupply"``
- `BurnedSupply  string                `json:"burnedSupply"``
- `CarbonID      string                `json:"carbonId"``
- `CarbonNFTAddress string                `json:"carbonNftAddress"``
- `CarbonSeriesID   string                `json:"carbonSeriesId"``
- `CarbonSeriesID string                `json:"carbonSeriesId"``
- `CarbonTokenID    string                `json:"carbonTokenId"``
- `CarbonTokenID  string                `json:"carbonTokenId"``
- `Chain          string `json:"chain"``
- `Chain    string          `json:"chain"``
- `Chain    string   `json:"chain"``
- `Chain   string `json:"chain"``
- `ChainAddress     string              `json:"chainAddress"``
- `ChainAddress    string `json:"chainAddress"``
- `ChainAddress string            `json:"chainAddress"``
- `ChainName        string                `json:"chainName"``
- `Chains        []ChainResult      `json:"chains"``
- `Channel   string `json:"channel"``
- `Close     string `json:"Close"``
- `Commit       string `json:"commit"``
- `Content string `json:"content"``
- `Contract string `json:"contract"``
- `Contracts    []string `json:"contracts"``
- `CreationTime   uint   `json:"creationTime"``
- `Creator       string `json:"creator"``
- `CreatorAddress   string                `json:"creatorAddress"``
- `CreatorAddress  string `json:"creatorAddress"``
- `CreatorAddress string `json:"creatorAddress"``
- `CurrentSupply  string                `json:"currentSupply"``
- `CurrentSupply string                `json:"currentSupply"``
- `CurrentWinner   string `json:"currentWinner"``
- `Dapps        []string `json:"dapps"``
- `Data     string `json:"data"``
- `Data string `json:"Data"``
- `Decimals      int                   `json:"decimals"``
- `Decimals uint     `json:"decimals"``
- `Description string `json:"description"``
- `DestinationAddress  string `json:"destinationAddress"``
- `DestinationChain    string `json:"destinationChain"``
- `DestinationHash     string `json:"destinationHash"``
- `DestinationPlatform string `json:"destinationPlatform"``
- `Encryption    string   `json:"encryption"``
- `EndDate         uint   `json:"endDate"``
- `EndDate       uint   `json:"endDate"``
- `EndPrice        string `json:"endPrice"``
- `Error string `json:"error"``
- `Events           []EventResult       `json:"events"``
- `Events       []EventResult     `json:"events"``
- `Events  []ABIEventResult  `json:"events"``
- `Events  []EventResult  `json:"events"``
- `Expiration   uint              `json:"expiration"``
- `ExtensionPeriod string `json:"extensionPeriod"``
- `External      []TokenExternalResult `json:"external"``
- `External string `json:"external"``
- `FeatureLevel          int    `json:"featureLevel"``
- `Fee            string `json:"fee"``
- `Fee          string            `json:"fee"``
- `Fee     string `json:"fee"``
- `Fields []VMNamedVariableSchemaResult `json:"fields"``
- `Flags         string                `json:"flags"``
- `Flags         string `json:"flags"``
- `Flags   string `json:"flags"``
- `Flags  uint                          `json:"flags"``
- `Fuel     string          `json:"fuel"``
- `FuelPerContractDeploy string `json:"fuelPerContractDeploy"``
- `GasAccount            string `json:"gasAccount"``
- `GasConstructor        string `json:"gasConstructor"``
- `GasLeaderboard        string `json:"gasLeaderboard"``
- `GasNexus              string `json:"gasNexus"``
- `GasOracle             string `json:"gasOracle"``
- `GasOrganization       string `json:"gasOrganization"``
- `GasStandard           string `json:"gasStandard"``
- `GlobalHardCap string `json:"globalHardCap"``
- `GlobalSoftCap string `json:"globalSoftCap"``
- `Governance    []GovernanceResult `json:"governance"``
- `Hash             string              `json:"hash"``
- `Hash          string   `json:"hash"``
- `Hash          string `json:"hash"``
- `Hash         string            `json:"hash"``
- `Hash     string `json:"hash"``
- `Hash  string `json:"hash"``
- `Height           uint                `json:"height"``
- `Height       uint     `json:"height"``
- `High      string `json:"High"``
- `ID               string                `json:"ID"``
- `ID      string   `json:"id"``
- `Ids      []string `json:"ids"``
- `Index          int    `json:"index"``
- `Index     string `json:"index"``
- `Infusion         []TokenPropertyResult `json:"infusion"``
- `Interop  []InteropResult `json:"interop"``
- `IsStored              bool   `json:"isStored"``
- `Key   string `json:"Key"``
- `Kind     string `json:"kind"``
- `Kind string `json:"Kind"``
- `ListingFee      string `json:"listingFee"``
- `Local    string `json:"local"``
- `Low       string `json:"Low"``
- `MaxMint        string                `json:"maxMint"``
- `MaxSupply      string                `json:"maxSupply"``
- `MaxSupply     string                `json:"maxSupply"``
- `Members []string `json:"members"``
- `Metadata       []TokenPropertyResult `json:"metadata"``
- `Metadata      []TokenPropertyResult `json:"metadata"``
- `Methods        []ABIMethodResult     `json:"methods"``
- `Methods []ABIMethodResult `json:"methods"``
- `Mint             string                `json:"mint"``
- `MintCount      string                `json:"mintCount"``
- `MissingBlocks []int    `json:"missingBlocks"``
- `Mode           string                `json:"mode"``
- `Name           string `json:"name"``
- `Name          string                `json:"name"``
- `Name          string             `json:"name"``
- `Name          string   `json:"name"``
- `Name          string `json:"name"``
- `Name         string   `json:"name"``
- `Name        string `json:"name"``
- `Name       string               `json:"name"``
- `Name      string          `json:"name"``
- `Name    string            `json:"name"``
- `Name    string   `json:"name"``
- `Name    string `json:"name"``
- `Name   string                 `json:"name"``
- `Name  string `json:"name"``
- `Name string                 `json:"name"``
- `Name string `json:"name"``
- `Nexus     string `json:"nexus"``
- `Open      string `json:"Open"``
- `Oracles          []OracleResult      `json:"oracles"``
- `Oracles []OracleResult `json:"oracles"``
- `Organization string   `json:"organization"``
- `Organizations []string           `json:"organizations"``
- `Owner         string                `json:"owner"``
- `OwnerAddress     string                `json:"ownerAddress"``
- `OwnerAddress   string                `json:"ownerAddress"``
- `Owners        []string `json:"owners"``
- `Parameters []ABIParameterResult `json:"parameters"``
- `Parent       string   `json:"parent"``
- `Payload      string            `json:"payload"``
- `Platform string          `json:"platform"``
- `Platform string `json:"platform"``
- `Platforms     []PlatformResult   `json:"platforms"``
- `Pow     uint   `json:"pow"``
- `PreviousHash     string              `json:"previousHash"``
- `Price           string `json:"price"``
- `Price         []TokenPriceResult    `json:"price"``
- `Price         uint   `json:"price"``
- `Properties       []TokenPropertyResult `json:"properties"``
- `Protocol         uint                `json:"protocol"``
- `Protocol      uint               `json:"protocol"``
- `QuoteSymbol     string `json:"quoteSymbol"``
- `RAM              string                `json:"ram"``
- `RAM             string `json:"ram"``
- `RAM            VMStructSchemaResult `json:"ram"``
- `ROM              string                `json:"rom"``
- `ROM             string `json:"rom"``
- `ROM            VMStructSchemaResult `json:"rom"``
- `ReceiveSymbol string `json:"receiveSymbol"``
- `Receiver  string `json:"receiver"``
- `Relay     string          `json:"relay"``
- `Result       string            `json:"result"``
- `Result  string         `json:"result"``
- `Results []string       `json:"results"``
- `ReturnType  string `json:"returnType"``
- `ReturnType string               `json:"returnType"``
- `Reward           string              `json:"reward"``
- `Rows []LeaderboardRowResult `json:"rows"``
- `Schema *VMStructSchemaResult `json:"schema,omitempty"``
- `Schema VMVariableSchemaResult `json:"schema"``
- `Script         string                `json:"script"``
- `Script        string                `json:"script"``
- `Script       string            `json:"script"``
- `Script    string `json:"script"``
- `Script  string            `json:"script"``
- `SellSymbol    string `json:"sellSymbol"``
- `Sender    string `json:"sender"``
- `Series           string                `json:"series"``
- `Series        []TokenSeriesResult   `json:"series"``
- `SeriesID       string                `json:"seriesId"``
- `SeriesMetadata VMStructSchemaResult `json:"seriesMetadata"``
- `Signatures   []SignatureResult `json:"signatures"``
- `Size          uint     `json:"size"``
- `SourceAddress       string `json:"sourceAddress"``
- `SourceChain         string `json:"sourceChain"``
- `SourceHash          string `json:"sourceHash"``
- `SourcePlatform      string `json:"sourcePlatform"``
- `Stake     string          `json:"stake"``
- `Stakes    StakeResult     `json:"stakes"``
- `StartDate       uint   `json:"startDate"``
- `StartDate     uint   `json:"startDate"``
- `State        string            `json:"state"``
- `Status           string                `json:"status"``
- `Storage   StorageResult   `json:"storage"``
- `Symbol              string `json:"symbol"``
- `Symbol         string `json:"symbol"``
- `Symbol        string                `json:"symbol"``
- `Symbol   string   `json:"symbol"``
- `TargetAddress  string `json:"targetAddress"``
- `Time          uint     `json:"time"``
- `Time      uint   `json:"time"``
- `Timestamp        uint                `json:"timestamp"``
- `Timestamp    uint              `json:"timestamp"``
- `Timestamp uint   `json:"Timestamp"``
- `Timestamp uint   `json:"timestamp"``
- `TokenID         string `json:"tokenId"``
- `TokenSchemas  *TokenSchemasResult   `json:"tokenSchemas"``
- `Tokens        []TokenResult      `json:"tokens"``
- `Tokens   []string        `json:"tokens"``
- `Txs              []TransactionResult `json:"txs"``
- `Txs     []TransactionResult `json:"txs"``
- `Type            string `json:"type"``
- `Type    string `json:"type"``
- `Type   string                `json:"type"``
- `Type string `json:"type"``
- `URL     string `json:"url"``
- `Unclaimed string          `json:"unclaimed"``
- `Unclaimed string `json:"unclaimed"``
- `Used      uint            `json:"used"``
- `UserHardCap   string `json:"userHardCap"``
- `UserSoftCap   string `json:"userSoftCap"``
- `Validator string          `json:"validator"``
- `ValidatorAddress string              `json:"validatorAddress"``
- `Value               string `json:"value"``
- `Value       int    `json:"value"``
- `Value   string `json:"value"``
- `Value interface{} `json:"error"``
- `Value string `json:"Value"``
- `Value string `json:"value"``
- `Version      string `json:"version"``
- `Version string `json:"version"``

### Methods

```go
func (a *AccountResult) GetTokenBalance(t TokenResult) *BalanceResult
```

```go
func (a AccountResult) Clone() *AccountResult
```

```go
func (b BalanceResult) Clone() *BalanceResult
```

```go
func (b BalanceResult) ConvertDecimals() string
```

```go
func (b BalanceResult) ConvertDecimalsToFloat() *big.Float
```

```go
func (s ScriptResult) DecodeResultWithError() (*vm.VMObject, error)
```

```go
func (s ScriptResult) DecodeResultsWithError(index int) (*vm.VMObject, error)
```

```go
func (s StakeResult) ConvertDecimals() string
```

```go
func (s StakeResult) ConvertDecimalsToFloat() *big.Float
```

```go
func (t TokenResult) IsBurnable() bool
```

```go
func (t TokenResult) IsDivisible() bool
```

```go
func (t TokenResult) IsFiat() bool
```

```go
func (t TokenResult) IsFinite() bool
```

```go
func (t TokenResult) IsFuel() bool
```

```go
func (t TokenResult) IsFungible() bool
```

```go
func (t TokenResult) IsMintable() bool
```

```go
func (t TokenResult) IsStakable() bool
```

```go
func (t TokenResult) IsTransferable() bool
```

```go
func (t TransactionResult) StateIsFault() bool
```

```go
func (t TransactionResult) StateIsSuccess() bool
```

## github.com/phantasma-io/phantasma-sdk-go/pkg/util

Source: `pkg/util`

### Methods

```go
func BigIntBytesFromCsharpOrPhantasmaByteArray(bytes []byte) ([]byte, int)
```

```go
func BigIntFromCsharpOrPhantasmaByteArray(bytes []byte) *big.Int
```

```go
func BigIntToCsharpByteArray(n *big.Int) []byte
```

```go
func BigIntToPhantasmaByteArray(n *big.Int) []byte
```

```go
func ConvertDecimals(number *big.Int, decimals int) string
```

```go
func ConvertDecimalsBack(number string, decimals int) (*big.Int, error)
```

```go
func ConvertDecimalsBackEx(number string, decimals int, separator string) (string, error)
```

```go
func ConvertDecimalsEx(number string, decimals int, separator string) string
```

```go
func ErrorDetect(s string) bool
```

```go
func TwosComplementConvertFrom(bytes []byte)
```

```go
func TwosComplementConvertTo(bytes []byte)
```

## github.com/phantasma-io/phantasma-sdk-go/pkg/util/hashing

Source: `pkg/util/hashing`

### Methods

```go
func Checksum(data []byte) []byte
```

```go
func DoubleSha256(data []byte) []byte
```

```go
func Sha256(data []byte) []byte
```

## github.com/phantasma-io/phantasma-sdk-go/pkg/vm

Source: `pkg/vm`

### Declarations

```go
const ABS
```

```go
const ADD
```

```go
const AND
```

```go
const Bool
```

```go
const Bytes
```

```go
const CALL
```

```go
const CAST
```

```go
const CAT
```

```go
const CLEAR // clears a register
```

```go
const COPY // copy by value
```

```go
const COUNT
```

```go
const CTX
```

```go
const DEBUG
```

```go
const DEC
```

```go
const DIV
```

```go
const EQUAL
```

```go
const EVM = 255
```

```go
const EXTCALL
```

```go
const Enum
```

```go
const GET // lookups a key and copies a reference into register
```

```go
const GT
```

```go
const GTE
```

```go
const INC
```

```go
const JMP
```

```go
const JMPIF
```

```go
const JMPNOT
```

```go
const LEFT
```

```go
const LOAD
```

```go
const LT
```

```go
const LTE
```

```go
const MAX
```

```go
const MIN
```

```go
const MOD
```

```go
const MOVE // copy reference
```

```go
const MUL
```

```go
const NEGATE
```

```go
const NOP Opcode = iota
```

```go
const NOT
```

```go
const None VMType = iota
```

```go
const Number
```

```go
const OR
```

```go
const Object
```

```go
const PACK // unused for now
```

```go
const POP
```

```go
const POW
```

```go
const PUSH
```

```go
const PUT
```

```go
const RANGE
```

```go
const REMOVE = 54
```

```go
const RET
```

```go
const RIGHT
```

```go
const SHL
```

```go
const SHR
```

```go
const SIGN
```

```go
const SIZE
```

```go
const SUB
```

```go
const SUBSTR
```

```go
const SWAP
```

```go
const SWITCH
```

```go
const String
```

```go
const Struct
```

```go
const THROW
```

```go
const Timestamp
```

```go
const UNPACK // unpacks serialized struct based on ref struct
```

```go
const XOR
```

```go
type Opcode byte
```

```go
type VMObject struct {
```

```go
type VMObjectPair struct {
```

```go
type VMObjectStruct []VMObjectPair
```

```go
type VMType byte
```

```go
var VMTypeLookup = map[VMType]string
```

### Fields

- `Data interface{}`
- `Key   VMObject`
- `Type VMType`
- `Value VMObject`

### Methods

```go
func (t VMType) FromString(vmType string) VMType
```

```go
func (v *VMObject) AsBool() bool
```

```go
func (v *VMObject) AsBytes() []byte
```

```go
func (v *VMObject) AsNumber() *big.Int
```

```go
func (v *VMObject) AsString() string
```

```go
func (v *VMObject) CastTo(vmtype VMType) *VMObject
```

```go
func (v *VMObject) Copy(other *VMObject)
```

```go
func (v *VMObject) Deserialize(reader *io.BinReader)
```

```go
func (v *VMObject) GetArrayType() VMType
```

```go
func (v *VMObject) Serialize(writer *io.BinWriter)
```

```go
func (v *VMObject) SetValue(val []byte, vmtype VMType) *VMObject
```

```go
func (v *VMObject) String() string
```

```go
func ValidateStructKey(key *VMObject)
```

## github.com/phantasma-io/phantasma-sdk-go/pkg/vm/script_builder

Source: `pkg/vm/script_builder`

### Declarations

```go
type ScriptBuilder struct {
```

### Methods

```go
func (s ScriptBuilder) AllowGas(from, to cryptography.Address, gasPrice, gasLimit *big.Int) ScriptBuilder
```

```go
func (s ScriptBuilder) AllowGasText(from, to string, gasPrice, gasLimit *big.Int) ScriptBuilder
```

```go
func (s ScriptBuilder) CallContract(contractName, method string, args ...interface{}) ScriptBuilder
```

```go
func (s ScriptBuilder) CallInterop(method string, args ...interface{}) ScriptBuilder
```

```go
func (s ScriptBuilder) CallNFT(symbol string, seriesID *big.Int, method string, args ...interface{}) ScriptBuilder
```

```go
func (s ScriptBuilder) CrossTransferNFT(destinationChain cryptography.Address, symbol string, from, to cryptography.Address, tokenID *big.Int) ScriptBuilder
```

```go
func (s ScriptBuilder) CrossTransferNFTText(destinationChain string, symbol string, from string, to string, tokenID *big.Int) ScriptBuilder
```

```go
func (s ScriptBuilder) CrossTransferNFTToText(destinationChain cryptography.Address, symbol string, from cryptography.Address, to string, tokenID *big.Int) ScriptBuilder
```

```go
func (s ScriptBuilder) CrossTransferToken(destinationChain cryptography.Address, symbol string, from, to cryptography.Address, amount *big.Int) ScriptBuilder
```

```go
func (s ScriptBuilder) CrossTransferTokenText(destinationChain string, symbol string, from string, to string, amount *big.Int) ScriptBuilder
```

```go
func (s ScriptBuilder) CrossTransferTokenToText(destinationChain cryptography.Address, symbol string, from cryptography.Address, to string, amount *big.Int) ScriptBuilder
```

```go
func (s ScriptBuilder) CurrentSize() int
```

```go
func (s ScriptBuilder) EmitCall(label string, regCnt byte) ScriptBuilder
```

```go
func (s ScriptBuilder) EmitConditionalJump(opcode vm.Opcode, srcReg byte, label string) ScriptBuilder
```

```go
func (s ScriptBuilder) EmitCopy(srcReg byte, dstReg byte) ScriptBuilder
```

```go
func (s ScriptBuilder) EmitExtCall(method string, reg byte) ScriptBuilder
```

```go
func (s ScriptBuilder) EmitJump(opcode vm.Opcode, label string, reg byte) ScriptBuilder
```

```go
func (s ScriptBuilder) EmitLabel(label string) ScriptBuilder
```

```go
func (s ScriptBuilder) EmitLoad(reg byte, bytes []byte, _type vm.VMType) ScriptBuilder
```

```go
func (s ScriptBuilder) EmitLoadBool(reg byte, toLoad bool) ScriptBuilder
```

```go
func (s ScriptBuilder) EmitLoadInt(reg byte, toLoad int) ScriptBuilder
```

```go
func (s ScriptBuilder) EmitLoadNumberAsBinary(reg byte, toLoad *big.Int) ScriptBuilder
```

```go
func (s ScriptBuilder) EmitLoadString(reg byte, toLoad string) ScriptBuilder
```

```go
func (s ScriptBuilder) EmitLoadTime(reg byte, toLoad time.Time) ScriptBuilder
```

```go
func (s ScriptBuilder) EmitM(opcode vm.Opcode, bytes []byte) ScriptBuilder
```

```go
func (s ScriptBuilder) EmitMove(srcReg byte, dstReg byte) ScriptBuilder
```

```go
func (s ScriptBuilder) EmitPop(reg byte) ScriptBuilder
```

```go
func (s ScriptBuilder) EmitPush(reg byte) ScriptBuilder
```

```go
func (s ScriptBuilder) EmitRaw(value []byte) ScriptBuilder
```

```go
func (s ScriptBuilder) EmitS(opcode vm.Opcode) ScriptBuilder
```

```go
func (s ScriptBuilder) EmitThrow(reg byte) ScriptBuilder
```

```go
func (s ScriptBuilder) EmitVarBytes(value int) ScriptBuilder
```

```go
func (s ScriptBuilder) EndScript() []byte
```

```go
func (s ScriptBuilder) EndScriptWithError() ([]byte, error)
```

```go
func (s ScriptBuilder) MintTokens(symbol string, from, to cryptography.Address, amount *big.Int) ScriptBuilder
```

```go
func (s ScriptBuilder) MintTokensText(symbol string, from, to string, amount *big.Int) ScriptBuilder
```

```go
func (s ScriptBuilder) SpendGas(address cryptography.Address) ScriptBuilder
```

```go
func (s ScriptBuilder) SpendGasText(address string) ScriptBuilder
```

```go
func (s ScriptBuilder) Stake(address cryptography.Address, amount *big.Int) ScriptBuilder
```

```go
func (s ScriptBuilder) StakeText(address string, amount *big.Int) ScriptBuilder
```

```go
func (s ScriptBuilder) ToScript() ([]byte, error)
```

```go
func (s ScriptBuilder) TransferBalance(symbol string, from, to cryptography.Address) ScriptBuilder
```

```go
func (s ScriptBuilder) TransferBalanceText(symbol string, from, to string) ScriptBuilder
```

```go
func (s ScriptBuilder) TransferNFT(symbol string, from, to cryptography.Address, tokenID *big.Int) ScriptBuilder
```

```go
func (s ScriptBuilder) TransferNFTText(symbol string, from, to string, tokenID *big.Int) ScriptBuilder
```

```go
func (s ScriptBuilder) TransferNFTToText(symbol string, from cryptography.Address, to string, tokenID *big.Int) ScriptBuilder
```

```go
func (s ScriptBuilder) TransferTokens(symbol string, from, to cryptography.Address, amount *big.Int) ScriptBuilder
```

```go
func (s ScriptBuilder) TransferTokensText(symbol string, from, to string, amount *big.Int) ScriptBuilder
```

```go
func (s ScriptBuilder) TransferTokensToText(symbol string, from cryptography.Address, to string, amount *big.Int) ScriptBuilder
```

```go
func (s ScriptBuilder) Unstake(address cryptography.Address, amount *big.Int) ScriptBuilder
```

```go
func (s ScriptBuilder) UnstakeText(address string, amount *big.Int) ScriptBuilder
```

```go
func BeginScript() ScriptBuilder
```

```go
func NewScriptBuilder() ScriptBuilder
```
