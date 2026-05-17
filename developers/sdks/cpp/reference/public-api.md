# C++ SDK Public API Inventory

This page lists public classes, methods, functions, enum values, fields, and
constants from the cited source baseline. Use it to check exact names when
working with lower-level SDK APIs.

Source baseline:

| Item | Value |
| ---- | ----- |
| Source repo | `phantasma-sdk-cpp` |
| Source commit | `b9b755c6e456214f65c1ff8168d5ad41eace302f` |
| Scope | public headers under `include/**` |

## Adapters/PhantasmaAPI_cpprest.h

Source: `include/Adapters/PhantasmaAPI_cpprest.h`

### Declarations

```cpp
#define PHANTASMA_CHAR char
```

```cpp
#define PHANTASMA_CHAR wchar_t
```

```cpp
#define PHANTASMA_CPPREST_JSON
```

```cpp
#define PHANTASMA_EXCEPTION_ENABLE
```

```cpp
#define PHANTASMA_HTTPCLIENT web::http::client::http_client
```

```cpp
#define PHANTASMA_JSONARRAY web::json::array
```

```cpp
#define PHANTASMA_JSONBUILDER web::json::value
```

```cpp
#define PHANTASMA_JSONDOCUMENT web::json::value
```

```cpp
#define PHANTASMA_JSONVALUE web::json::value
```

```cpp
#define PHANTASMA_STRING std::string
```

```cpp
#define PHANTASMA_STRING std::wstring
```

```cpp
struct PhantasmaError
```

```cpp
typedef PHANTASMA_CHAR Char
```

```cpp
typedef PHANTASMA_STRING String
```

## Adapters/PhantasmaAPI_curl.h

Source: `include/Adapters/PhantasmaAPI_curl.h`

### Declarations

```cpp
#define PHANTASMA_CHAR char
```

```cpp
#define PHANTASMA_CHAR wchar_t
```

```cpp
#define PHANTASMA_CURL
```

```cpp
#define PHANTASMA_HTTPCLIENT CurlClient
```

```cpp
#define PHANTASMA_STRING std::string
```

```cpp
#define PHANTASMA_STRING std::wstring
```

```cpp
#define PHANTASMA_STRINGBUILDER std::stringstream
```

```cpp
#define PHANTASMA_STRINGBUILDER std::wstringstream
```

```cpp
class CurlClient
```

```cpp
struct PhantasmaError
```

### Methods

```cpp
CurlClient::ReallocBuffer result
```

```cpp
CurlClient::const PHANTASMA_STRING host
```

```cpp
CurlClient::rapidjson::Document doc
```

## Adapters/PhantasmaAPI_openssl.h

Source: `include/Adapters/PhantasmaAPI_openssl.h`

### Declarations

```cpp
#define PHANTASMA_Ed25519_PrivateKeyFromSeed(output, outputLength, seed, seedLength) \
```

```cpp
#define PHANTASMA_Ed25519_PublicKeyFromSeed(output, outputLength, seed, seedLength) \
```

```cpp
#define PHANTASMA_Ed25519_SignAttached(output, outputLength, message, messageLength, privateKey, privateKeyLength) \
```

```cpp
#define PHANTASMA_Ed25519_SignDetached(output, outputLength, message, messageLength, privateKey, privateKeyLength) \
```

```cpp
#define PHANTASMA_Ed25519_ValidateAttached(message, messageLength, publicKey, publicKeyLength) \
```

```cpp
#define PHANTASMA_Ed25519_ValidateDetached(signature, signatureLength, message, messageLength, publicKey, publicKeyLength) \
```

```cpp
#define PHANTASMA_LOCKMEM(pointer, size) Phantasma_LockMemory((void*)(pointer), (size_t)(size))
```

```cpp
#define PHANTASMA_RANDOMBYTES(buffer, size) RAND_bytes((unsigned char*)(buffer), (int)(size))
```

```cpp
#define PHANTASMA_SECURE_ALLOC(size) OPENSSL_malloc(size)
```

```cpp
#define PHANTASMA_SECURE_ALLOC(size) OPENSSL_secure_malloc(size)
```

```cpp
#define PHANTASMA_SECURE_FREE(ptr) OPENSSL_free(ptr)
```

```cpp
#define PHANTASMA_SECURE_FREE(ptr) OPENSSL_secure_free(ptr)
```

```cpp
#define PHANTASMA_SECURE_NOACCESS(ptr, sz) ((void)(ptr), (void)(sz), 0)
```

```cpp
#define PHANTASMA_SECURE_NOACCESS(ptr, sz) OPENSSL_secure_clear_free(ptr, sz)
```

```cpp
#define PHANTASMA_SECURE_READONLY(ptr, size) ((void)(ptr), (void)(size), 0)
```

```cpp
#define PHANTASMA_SECURE_READWRITE(ptr, size) ((void)(ptr), (void)(size), 0)
```

```cpp
#define PHANTASMA_SHA256(output, outputSize, input, inputSize) ::phantasma::Phantasma_SHA256((Byte*)(output), (int)(outputSize), (const Byte*)(input), (int)(inputSize))
```

```cpp
#define PHANTASMA_UNLOCKMEM(pointer, size) Phantasma_UnlockMemory((void*)(pointer), (size_t)(size))
```

```cpp
#define PHANTASMA_WIPEMEM(buffer, size) OPENSSL_cleanse((buffer), (size))
```

## Adapters/PhantasmaAPI_rapidjson.h

Source: `include/Adapters/PhantasmaAPI_rapidjson.h`

### Declarations

```cpp
#define PHANTASMA_CHAR char
```

```cpp
#define PHANTASMA_CHAR wchar_t
```

```cpp
#define PHANTASMA_JSONARRAY rapidjson::Value
```

```cpp
#define PHANTASMA_JSONBUILDER RapidJsonBufferWriter
```

```cpp
#define PHANTASMA_JSONDOCUMENT rapidjson::Document
```

```cpp
#define PHANTASMA_JSONVALUE RapidJsonValueRef
```

```cpp
#define PHANTASMA_RAPIDJSON
```

```cpp
#define PHANTASMA_STRING std::string
```

```cpp
#define PHANTASMA_STRING std::wstring
```

```cpp
struct RapidJsonBufferWriter
```

```cpp
typedef PHANTASMA_CHAR Char
```

```cpp
typedef PHANTASMA_STRING String
```

```cpp
typedef RapidJsonBufferWriter Builder
```

```cpp
typedef const rapidjson::Value& RapidJsonValueRef
```

### Methods

```cpp
RapidJsonBufferWriter::rapidjson::StringBuffer buf
```

```cpp
RapidJsonBufferWriter::rapidjson::Writer<rapidjson::StringBuffer> w
```

## Adapters/PhantasmaAPI_sodium.h

Source: `include/Adapters/PhantasmaAPI_sodium.h`

### Declarations

```cpp
#define PHANTASMA_AuthenticatedDecrypt Phantasma_Decrypt
```

```cpp
#define PHANTASMA_AuthenticatedEncrypt Phantasma_Encrypt
```

```cpp
#define PHANTASMA_AuthenticatedKeyLength crypto_secretbox_KEYBYTES
```

```cpp
#define PHANTASMA_AuthenticatedNonceLength crypto_secretbox_NONCEBYTES
```

```cpp
#define PHANTASMA_Ed25519_PrivateKeyFromSeed(output, outputLength, seed, seedLength) \
```

```cpp
#define PHANTASMA_Ed25519_PublicKeyFromSeed(output, outputLength, seed, seedLength) \
```

```cpp
#define PHANTASMA_Ed25519_SignAttached(output, outputLength, message, messageLength, privateKey, privateKeyLength) \
```

```cpp
#define PHANTASMA_Ed25519_SignDetached(output, outputLength, message, messageLength, privateKey, privateKeyLength) \
```

```cpp
#define PHANTASMA_Ed25519_ValidateAttached(message, messageLength, publicKey, publicKeyLength) \
```

```cpp
#define PHANTASMA_Ed25519_ValidateDetached(signature, signatureLength, message, messageLength, publicKey, publicKeyLength) \
```

```cpp
#define PHANTASMA_LOCKMEM(pointer, size) sodium_mlock(pointer, size)
```

```cpp
#define PHANTASMA_PasswordSaltLength crypto_pwhash_SALTBYTES
```

```cpp
#define PHANTASMA_PasswordToKey Phantasma_PasswordToKey
```

```cpp
#define PHANTASMA_RANDOMBYTES(buffer, size) randombytes_buf(buffer, size)
```

```cpp
#define PHANTASMA_SECURE_ALLOC(size) sodium_malloc(size)
```

```cpp
#define PHANTASMA_SECURE_FREE(ptr) sodium_free(ptr)
```

```cpp
#define PHANTASMA_SECURE_NOACCESS(ptr, size) sodium_mprotect_noaccess(ptr)
```

```cpp
#define PHANTASMA_SECURE_READONLY(ptr, size) sodium_mprotect_readonly(ptr)
```

```cpp
#define PHANTASMA_SECURE_READWRITE(ptr, size) sodium_mprotect_readwrite(ptr)
```

```cpp
#define PHANTASMA_SHA256(output, outputSize, input, inputSize) crypto_hash_sha256(output, input, inputSize)
```

```cpp
#define PHANTASMA_UNLOCKMEM(pointer, size) sodium_munlock(pointer, size)
```

```cpp
#define PHANTASMA_WIPEMEM(buffer, size) sodium_memzero(buffer, size)
```

## Adapters/PhantasmaAPI_wincrypt.h

Source: `include/Adapters/PhantasmaAPI_wincrypt.h`

### Declarations

```cpp
#define PHANTASMA_DECRYPT_SESSION_DATA(r, m, ml, p, pl) phantasma::Phantasma_DecryptSessionData(r, m, ml, p, pl)
```

```cpp
#define PHANTASMA_ENCRYPT_SESSION_DATA(r, m, ml, p, pl) phantasma::Phantasma_EncryptSessionData(r, m, ml, p, pl)
```

```cpp
#define PHANTASMA_SECURE_ALLOC_ALIGNMENT CRYPTPROTECTMEMORY_BLOCK_SIZE
```

```cpp
#define PHANTASMA_SECURE_DECRYPT_MEMORY(p, s) phantasma::Phantasma_DecryptMemory(p, s)
```

```cpp
#define PHANTASMA_SECURE_ENCRYPT_MEMORY(p, s) phantasma::Phantasma_EncryptMemory(p, s)
```

```cpp
#define PHANTASMA_WIPEMEM(buffer, size) SecureZeroMemory(buffer, size)
```

## Blockchain/Transaction.h

Source: `include/Blockchain/Transaction.h`

### Declarations

```cpp
class Transaction : public Serializable
```

## Carbon/Alloc.h

Source: `include/Carbon/Alloc.h`

### Declarations

```cpp
ByteView Compress(ByteView input, Bytes& buffer, int compressionLevel = 3)
```

```cpp
ByteView Decompress(ByteView input, Bytes& buffer)
```

```cpp
ByteView FromHex(const char* sz, Allocator& c)
```

```cpp
ByteView FromHex(const char* sz, Bytes& c)
```

```cpp
ByteView FromHexBe(const char* sz, Bytes& c)
```

```cpp
SmallString str(tag, true)
```

```cpp
char* Format(Allocator& a, const char* fmt, ...)
```

```cpp
char* VFormat(Allocator& a, const char* fmt, va_list& v)
```

```cpp
char* VFormat(vector<char>& a, const char* fmt, va_list& v)
```

```cpp
class Allocator
```

```cpp
class BytesKey
```

```cpp
class ReadView : public ByteView
```

```cpp
class WriteView
```

```cpp
const char* ToHex(ByteView k, Allocator& c)
```

```cpp
const char* ToHex(ByteView k, vector<char>& c)
```

```cpp
const char* ToHexBe(ByteView k, Allocator& c)
```

```cpp
const char* ToHexBe(ByteView k, vector<char>& c)
```

```cpp
std::lock_guard lk(s.m)
```

```cpp
struct AllocLog
```

```cpp
struct BytesHash
```

```cpp
struct SmallStringHash
```

```cpp
typedef vector<uint8_t> Bytes
```

```cpp
using vector = PHANTASMA_VECTOR<T>
```

```cpp
using vector = std::vector<T, StdAllocator<T>>
```

```cpp
using vector = std::vector<T>
```

```cpp
void Clone(T& output, const T& input, Allocator& a)
```

### Methods

```cpp
AllocLog::std::recursive_mutex m
```

```cpp
AllocLog::std::unordered_map<SmallString, Usage, SmallStringHash> usage
```

```cpp
AllocLog::std::unordered_map<const void*, Owner> owners
```

```cpp
AllocLog::}
```

```cpp
Allocator::explicit Allocator(const char* tag = "?") CARBON_MEMORY_DBG( : tag(tag)) { Clear(); } ~Allocator() { Clear(); } Allocator(Allocator&& o) CARBON_MEMORY_DBG( : tag(o.tag)), m_head(std::move(o.m_head)) {} void Swap(Allocator& o) } void Clear()
```

```cpp
ReadView::bool AllowNonStandard() const { return flags & Relaxed; } bool StrictMode() const { return !AllowNonStandard(); } bool AllowInPlace() const { return flags & InPlace; } bool ExtendLifetimes() const { return !AllowInPlace(); } ReadView(void* v, size_t s) : flags(InPlace) } ReadView(void* v, size_t s, Allocator& a, Flags f) : allocator(&a), flags(f) } ReadView(const Bytes& v, Allocator& a, Flags f) : allocator(&a), flags(f) { static_cast<ByteView&>(*this) = View(v); } ReadView(const ByteView& v, Allocator& a, Flags f) : allocator(&a), flags(f) { static_cast<ByteView&>(*this) = v; } explicit ReadView(const ReadView& o) : allocator(o.allocator), fail(o.fail), flags(o.flags) } void operator=(const ReadView&) = delete
```

```cpp
ReadView::const Flags flags
```

```cpp
ReadView::enum Flags }
```

```cpp
WriteView::WriteView(Bytes& buf) : m(buf) {}
```

## Carbon/Carbon.h

Source: `include/Carbon/Carbon.h`

### Declarations

```cpp
ReadView r(bytes.empty() ? nullptr : (void*)(&bytes.front() + offset), bytes.size() - offset)
```

```cpp
WriteView w(buffer)
```

```cpp
struct Throw
```

## Carbon/Contracts/Market.h

Source: `include/Carbon/Contracts/Market.h`

### Declarations

```cpp
enum class ListingType : uint8_t
```

```cpp
struct TokenListing
```

### Methods

```cpp
TokenListing::Bytes32 seller{}
```

```cpp
TokenListing::ListingType type = ListingType::FixedPrice
```

```cpp
TokenListing::int64_t endDate = 0
```

```cpp
TokenListing::int64_t startDate = 0
```

```cpp
TokenListing::intx price{}
```

```cpp
TokenListing::uint64_t quoteTokenId = 0
```

### Variants

- `ListingType::FixedPrice`

## Carbon/Contracts/Token.h

Source: `include/Carbon/Contracts/Token.h`

### Declarations

```cpp
enum NftInstanceFlags : uint8_t
```

```cpp
enum TokenFlags
```

```cpp
enum TokensConfigFlags
```

```cpp
struct GasConfigWithTokens
```

```cpp
struct NftImport
```

```cpp
struct NftInfo
```

```cpp
struct NftInstance
```

```cpp
struct NftMintInfo
```

```cpp
struct NftRomBuilder
```

```cpp
struct NftSchema
```

```cpp
struct NftState
```

```cpp
struct PhantasmaNftMintInfo
```

```cpp
struct PhantasmaNftMintResult
```

```cpp
struct PhantasmaNftRomBuilder
```

```cpp
struct SeriesImport
```

```cpp
struct SeriesInfo
```

```cpp
struct SeriesInfoBuilder
```

```cpp
struct SeriesInfoOwned
```

```cpp
struct SeriesSupply
```

```cpp
struct TokenInfo
```

```cpp
struct TokenInfoBuilder
```

```cpp
struct TokenInfoOwned
```

```cpp
struct TokenInfo_FlagsOnly
```

```cpp
struct TokenMetadataBuilder
```

```cpp
struct TokenSeriesMetadataBuilder
```

```cpp
struct TokensConfig
```

### Methods

```cpp
GasConfigWithTokens::Blockchain::GasConfig config{}
```

```cpp
GasConfigWithTokens::TokenInfo dataToken{}
```

```cpp
GasConfigWithTokens::TokenInfo gasToken{}
```

```cpp
NftImport::ByteView ram{}
```

```cpp
NftImport::ByteView rom{}
```

```cpp
NftImport::Bytes32 originator{}
```

```cpp
NftImport::Bytes32 owner{}
```

```cpp
NftImport::int64_t created = 0
```

```cpp
NftImport::uint32_t mintNumber = 0
```

```cpp
NftInfo::ByteView ram{}
```

```cpp
NftInfo::ByteView rom{}
```

```cpp
NftInfo::Bytes32 originator{}
```

```cpp
NftInfo::Bytes32 owner{}
```

```cpp
NftInfo::NftInstanceFlags flags = NftInstance_None
```

```cpp
NftInfo::int64_t created = 0
```

```cpp
NftInfo::uint32_t mintNumber = 0
```

```cpp
NftInfo::uint32_t seriesId = 0
```

```cpp
NftInstance::ByteView rom{}
```

```cpp
NftInstance::Bytes32 originator{}
```

```cpp
NftInstance::NftInstanceFlags flags = NftInstance_None
```

```cpp
NftInstance::int64_t created = 0
```

```cpp
NftMintInfo::ByteView ram{}
```

```cpp
NftMintInfo::ByteView rom{}
```

```cpp
NftMintInfo::uint32_t seriesId = 0
```

```cpp
NftSchema::ByteView seriesMetadataValue{}
```

```cpp
NftSchema::ByteView tokenMetadata{}
```

```cpp
NftSchema::SmallString tokenSymbol{}
```

```cpp
NftSchema::VmStructSchema seriesMetadataSchema{}
```

```cpp
NftSchema::VmStructSchema seriesRam{}
```

```cpp
NftSchema::VmStructSchema seriesRom{}
```

```cpp
NftSchema::VmStructSchema tokenRam{}
```

```cpp
NftSchema::VmStructSchema tokenRom{}
```

```cpp
NftState::NftInstanceFlags flags = NftInstance_None
```

```cpp
NftState::VmDynamicVariable metaId{}
```

```cpp
NftState::int64_t lastTransfer = 0
```

```cpp
PhantasmaNftMintInfo::ByteView ram{}
```

```cpp
PhantasmaNftMintInfo::ByteView rom{}
```

```cpp
PhantasmaNftMintInfo::intx_pod phantasmaSeriesId{}
```

```cpp
PhantasmaNftMintResult::Bytes32 phantasmaNftId{}
```

```cpp
PhantasmaNftMintResult::uint64_t carbonInstanceId = 0
```

```cpp
SeriesImport::SeriesInfo info{}
```

```cpp
SeriesImport::const NftImport* imports = nullptr
```

```cpp
SeriesImport::uint32_t numImports = 0
```

```cpp
SeriesImport::uint64_t tokenId = 0
```

```cpp
SeriesInfo::ByteView metadata{}
```

```cpp
SeriesInfo::Bytes32 owner{}
```

```cpp
SeriesInfo::VmStructSchema ram{}
```

```cpp
SeriesInfo::VmStructSchema rom{}
```

```cpp
SeriesInfo::uint32_t maxMint = 0
```

```cpp
SeriesInfo::uint32_t maxSupply = 0
```

```cpp
SeriesInfoOwned::ByteArray metadataStorage
```

```cpp
SeriesInfoOwned::SeriesInfo view{}
```

```cpp
SeriesSupply::uint32_t currentSupply = 0
```

```cpp
SeriesSupply::uint32_t mintCount = 0
```

```cpp
TokenInfo::ByteView metadata{}
```

```cpp
TokenInfo::ByteView tokenSchemas{}
```

```cpp
TokenInfo::Bytes32 owner{}
```

```cpp
TokenInfo::SmallString symbol{}
```

```cpp
TokenInfo::TokenFlags flags = TokenFlags_None
```

```cpp
TokenInfo::intx_pod maxSupply{}
```

```cpp
TokenInfo::uint8_t decimals = 0
```

```cpp
TokenInfoOwned::ByteArray metadataStorage
```

```cpp
TokenInfoOwned::ByteArray schemasStorage
```

```cpp
TokenInfoOwned::TokenInfo view{}
```

```cpp
TokenInfo_FlagsOnly::TokenFlags flags = TokenFlags_None
```

```cpp
TokensConfig::uint8_t flags = TokensConfigFlags_None
```

### Variants

- `NftInstanceFlags::NftInstance_HasMetaId = 1 << 0`
- `NftInstanceFlags::NftInstance_HasRam = 1 << 1`
- `NftInstanceFlags::NftInstance_None = 0`
- `NftInstanceFlags::NftInstance_Staked = 1 << 2`
- `TokenFlags::TokenFlags_BigFungible = 1 << 0`
- `TokenFlags::TokenFlags_NonFungible = 1 << 1`
- `TokenFlags::TokenFlags_None = 0`
- `TokensConfigFlags::TokensConfigFlags_None = 0`
- `TokensConfigFlags::TokensConfigFlags_RequireMetadata = 1 << 0`
- `TokensConfigFlags::TokensConfigFlags_RequireNftMetaId = 1 << 2`
- `TokensConfigFlags::TokensConfigFlags_RequireNftStandard = 1 << 3`
- `TokensConfigFlags::TokensConfigFlags_RequireSymbol = 1 << 1`

## Carbon/Contracts/TokenSchemas.h

Source: `include/Carbon/Contracts/TokenSchemas.h`

### Declarations

```cpp
inline void Write(const TokenSchemas& in, WriteView& w)
```

```cpp
struct FieldType
```

```cpp
struct IdHelper
```

```cpp
struct MetadataField
```

```cpp
struct MetadataHelper
```

```cpp
struct MetadataValue
```

```cpp
struct TokenSchemas
```

```cpp
struct TokenSchemasBuilder
```

```cpp
struct TokenSchemasOwned
```

### Methods

```cpp
FieldType::VmType type = VmType::Dynamic
```

```cpp
FieldType::std::string name
```

```cpp
MetadataField::MetadataValue value
```

```cpp
MetadataField::std::string name
```

```cpp
MetadataHelper::}
```

```cpp
MetadataValue::ByteArray bytesValue{}
```

```cpp
MetadataValue::Bytes16 bytes16Value{}
```

```cpp
MetadataValue::Bytes32 bytes32Value{}
```

```cpp
MetadataValue::Bytes64 bytes64Value{}
```

```cpp
MetadataValue::Kind kind = Kind::Null
```

```cpp
MetadataValue::enum class Kind }
```

```cpp
MetadataValue::int256 int256Value{}
```

```cpp
MetadataValue::int64_t int64Value = 0
```

```cpp
MetadataValue::std::string stringValue{}
```

```cpp
MetadataValue::std::vector<MetadataValue> arrayValue{}
```

```cpp
MetadataValue::std::vector<std::pair<std::string, MetadataValue>> structValue{}
```

```cpp
MetadataValue::uint256 uint256Value{}
```

```cpp
MetadataValue::uint64_t uint64Value = 0
```

```cpp
TokenSchemas::VmStructSchema ram{}
```

```cpp
TokenSchemas::VmStructSchema rom{}
```

```cpp
TokenSchemas::VmStructSchema seriesMetadata{}
```

```cpp
TokenSchemasOwned::TokenSchemas view{}
```

```cpp
TokenSchemasOwned::TokenSchemasOwned() = default
```

```cpp
TokenSchemasOwned::std::vector<VmNamedVariableSchema> ramFields
```

```cpp
TokenSchemasOwned::std::vector<VmNamedVariableSchema> romFields
```

```cpp
TokenSchemasOwned::std::vector<VmNamedVariableSchema> seriesFields
```

## Carbon/DataBlockchain.h

Source: `include/Carbon/DataBlockchain.h`

### Declarations

```cpp
WriteView w(buffer)
```

```cpp
enum class TxRejection
```

```cpp
enum class TxState : uint8_t
```

```cpp
enum class TxTypes : uint8_t
```

```cpp
struct ChainConfig
```

```cpp
struct GasConfig
```

```cpp
struct MsgCallArgSections
```

```cpp
struct MsgCallArgs
```

```cpp
struct SignedTxMsg
```

```cpp
struct TxMsg
```

```cpp
struct TxMsgBurnFungible
```

```cpp
struct TxMsgBurnFungible_GasPayer
```

```cpp
struct TxMsgBurnNonFungible
```

```cpp
struct TxMsgBurnNonFungible_GasPayer
```

```cpp
struct TxMsgCall
```

```cpp
struct TxMsgCall_Multi
```

```cpp
struct TxMsgMintFungible
```

```cpp
struct TxMsgMintNonFungible
```

```cpp
struct TxMsgPhantasma
```

```cpp
struct TxMsgPhantasma_Raw
```

```cpp
struct TxMsgSigner
```

```cpp
struct TxMsgSpecialResolution
```

```cpp
struct TxMsgTrade
```

```cpp
struct TxMsgTransferFungible
```

```cpp
struct TxMsgTransferFungible_GasPayer
```

```cpp
struct TxMsgTransferNonFungible_Multi
```

```cpp
struct TxMsgTransferNonFungible_Multi_GasPayer
```

```cpp
struct TxMsgTransferNonFungible_Single
```

```cpp
struct TxMsgTransferNonFungible_Single_GasPayer
```

### Methods

```cpp
ChainConfig::uint32_t allowedTxTypes = 0
```

```cpp
ChainConfig::uint32_t blockRateTarget = 0
```

```cpp
ChainConfig::uint32_t expiryWindow = 0
```

```cpp
ChainConfig::uint8_t reserved1 = 0
```

```cpp
ChainConfig::uint8_t reserved2 = 0
```

```cpp
ChainConfig::uint8_t reserved3 = 0
```

```cpp
ChainConfig::uint8_t version = 0
```

```cpp
GasConfig::uint32_t maxStructureSize = 0
```

```cpp
GasConfig::uint64_t dataEscrowPerRow = 0
```

```cpp
GasConfig::uint64_t dataTokenId = 0
```

```cpp
GasConfig::uint64_t feeMultiplier = 0
```

```cpp
GasConfig::uint64_t gasBurnRatioMul = 0
```

```cpp
GasConfig::uint64_t gasFeeCreateTokenBase = 0
```

```cpp
GasConfig::uint64_t gasFeeCreateTokenSeries = 0
```

```cpp
GasConfig::uint64_t gasFeeCreateTokenSymbol = 0
```

```cpp
GasConfig::uint64_t gasFeePerByte = 0
```

```cpp
GasConfig::uint64_t gasFeeQuery = 0
```

```cpp
GasConfig::uint64_t gasFeeRegisterName = 0
```

```cpp
GasConfig::uint64_t gasFeeTransfer = 0
```

```cpp
GasConfig::uint64_t gasTokenId = 0
```

```cpp
GasConfig::uint64_t minimumGasOffer = 0
```

```cpp
GasConfig::uint8_t feeShift = 0
```

```cpp
GasConfig::uint8_t gasBurnRatioShift = 0
```

```cpp
GasConfig::uint8_t maxNameLength = 0
```

```cpp
GasConfig::uint8_t maxTokenSymbolLength = 0
```

```cpp
GasConfig::uint8_t version = 0
```

```cpp
MsgCallArgSections::MsgCallArgs* argSections = nullptr
```

```cpp
MsgCallArgSections::int32_t numArgSections_negative = 0
```

```cpp
MsgCallArgs::ByteView args{}
```

```cpp
MsgCallArgs::int32_t registerOffset = 0
```

```cpp
SignedTxMsg::TxMsg msg
```

```cpp
SignedTxMsg::Witnesses witnesses{}
```

```cpp
TxMsg::Bytes32 gasFrom{}
```

```cpp
TxMsg::SmallString payload{}
```

```cpp
TxMsg::TxTypes type = TxTypes::Call
```

```cpp
TxMsg::constexpr static uint64_t NoMaxData = (uint64_t)-1
```

```cpp
TxMsg::constexpr static uint64_t NoMaxGas = (uint64_t)-1
```

```cpp
TxMsg::int64_t expiry = 0
```

```cpp
TxMsg::uint64_t maxData = 0
```

```cpp
TxMsg::uint64_t maxGas = 0
```

```cpp
TxMsg::union }
```

```cpp
TxMsgBurnFungible::intx_pod amount{}
```

```cpp
TxMsgBurnFungible::uint64_t tokenId = 0
```

```cpp
TxMsgBurnFungible_GasPayer::Bytes32 from
```

```cpp
TxMsgBurnFungible_GasPayer::intx_pod amount{}
```

```cpp
TxMsgBurnFungible_GasPayer::uint64_t tokenId = 0
```

```cpp
TxMsgBurnNonFungible::uint64_t instanceId = 0
```

```cpp
TxMsgBurnNonFungible::uint64_t tokenId = 0
```

```cpp
TxMsgBurnNonFungible_GasPayer::Bytes32 from
```

```cpp
TxMsgBurnNonFungible_GasPayer::uint64_t instanceId = 0
```

```cpp
TxMsgBurnNonFungible_GasPayer::uint64_t tokenId = 0
```

```cpp
TxMsgCall::ByteView args{}
```

```cpp
TxMsgCall::MsgCallArgSections sections{}
```

```cpp
TxMsgCall::uint32_t methodId = 0
```

```cpp
TxMsgCall::uint32_t moduleId = 0
```

```cpp
TxMsgCall_Multi::TxMsgCall* calls = nullptr
```

```cpp
TxMsgCall_Multi::uint32_t numCalls = 0
```

```cpp
TxMsgMintFungible::Bytes32 to
```

```cpp
TxMsgMintFungible::intx_pod amount{}
```

```cpp
TxMsgMintFungible::uint64_t tokenId = 0
```

```cpp
TxMsgMintNonFungible::ByteView ram{}
```

```cpp
TxMsgMintNonFungible::ByteView rom{}
```

```cpp
TxMsgMintNonFungible::Bytes32 to
```

```cpp
TxMsgMintNonFungible::uint32_t seriesId = 0
```

```cpp
TxMsgMintNonFungible::uint64_t tokenId = 0
```

```cpp
TxMsgPhantasma::ByteView script{}
```

```cpp
TxMsgPhantasma::SmallString chain
```

```cpp
TxMsgPhantasma::SmallString nexus
```

```cpp
TxMsgPhantasma_Raw::ByteView transaction{}
```

```cpp
TxMsgSpecialResolution::TxMsgCall_Multi calls{}
```

```cpp
TxMsgSpecialResolution::uint64_t resolutionId = 0
```

```cpp
TxMsgTrade::TxMsgBurnFungible_GasPayer* burnF = nullptr
```

```cpp
TxMsgTrade::TxMsgBurnNonFungible_GasPayer* burnN = nullptr
```

```cpp
TxMsgTrade::TxMsgMintFungible* mintF = nullptr
```

```cpp
TxMsgTrade::TxMsgMintNonFungible* mintN = nullptr
```

```cpp
TxMsgTrade::TxMsgTransferFungible_GasPayer* transferF = nullptr
```

```cpp
TxMsgTrade::TxMsgTransferNonFungible_Single_GasPayer* transferN = nullptr
```

```cpp
TxMsgTrade::uint32_t numBurnF = 0
```

```cpp
TxMsgTrade::uint32_t numBurnN = 0
```

```cpp
TxMsgTrade::uint32_t numMintF = 0
```

```cpp
TxMsgTrade::uint32_t numMintN = 0
```

```cpp
TxMsgTrade::uint32_t numTransferF = 0
```

```cpp
TxMsgTrade::uint32_t numTransferN = 0
```

```cpp
TxMsgTransferFungible::Bytes32 to
```

```cpp
TxMsgTransferFungible::uint64_t amount = 0
```

```cpp
TxMsgTransferFungible::uint64_t tokenId = 0
```

```cpp
TxMsgTransferFungible_GasPayer::Bytes32 from
```

```cpp
TxMsgTransferFungible_GasPayer::Bytes32 to
```

```cpp
TxMsgTransferFungible_GasPayer::uint64_t amount = 0
```

```cpp
TxMsgTransferFungible_GasPayer::uint64_t tokenId = 0
```

```cpp
TxMsgTransferNonFungible_Multi::Bytes32 to
```

```cpp
TxMsgTransferNonFungible_Multi::const uint64_t* instanceIds = nullptr
```

```cpp
TxMsgTransferNonFungible_Multi::uint32_t numInstanceIds = 0
```

```cpp
TxMsgTransferNonFungible_Multi::uint64_t tokenId = 0
```

```cpp
TxMsgTransferNonFungible_Multi_GasPayer::Bytes32 from
```

```cpp
TxMsgTransferNonFungible_Multi_GasPayer::Bytes32 to
```

```cpp
TxMsgTransferNonFungible_Multi_GasPayer::const uint64_t* instanceIds = nullptr
```

```cpp
TxMsgTransferNonFungible_Multi_GasPayer::uint32_t numInstanceIds = 0
```

```cpp
TxMsgTransferNonFungible_Multi_GasPayer::uint64_t tokenId = 0
```

```cpp
TxMsgTransferNonFungible_Single::Bytes32 to
```

```cpp
TxMsgTransferNonFungible_Single::uint64_t instanceId = 0
```

```cpp
TxMsgTransferNonFungible_Single::uint64_t tokenId = 0
```

```cpp
TxMsgTransferNonFungible_Single_GasPayer::Bytes32 from
```

```cpp
TxMsgTransferNonFungible_Single_GasPayer::Bytes32 to
```

```cpp
TxMsgTransferNonFungible_Single_GasPayer::uint64_t instanceId = 0
```

```cpp
TxMsgTransferNonFungible_Single_GasPayer::uint64_t tokenId = 0
```

### Variants

- `TxRejection::Contract = 6`
- `TxRejection::DataFees = 3`
- `TxRejection::DataFormat = 1`
- `TxRejection::Expired = 5`
- `TxRejection::GasFees = 2`
- `TxRejection::Payload = 7`
- `TxRejection::Valid = 0`
- `TxRejection::Witnesses = 4`
- `TxState::Aborted = 2`
- `TxState::Completed = 1`
- `TxState::Pending = 3`
- `TxState::Rejected = 0`
- `TxState::Unknown = 0xFF`
- `TxTypes::BurnFungible = 10`
- `TxTypes::BurnFungible_GasPayer = 11`
- `TxTypes::BurnNonFungible = 13`
- `TxTypes::BurnNonFungible_GasPayer = 14`
- `TxTypes::Call = 0`
- `TxTypes::Call_Multi = 1`
- `TxTypes::MintFungible = 9`
- `TxTypes::MintNonFungible = 12`
- `TxTypes::Phantasma = 15`
- `TxTypes::Phantasma_Raw = 16`
- `TxTypes::Trade = 2`
- `TxTypes::TransferFungible = 3`
- `TxTypes::TransferFungible_GasPayer = 4`
- `TxTypes::TransferNonFungible_Multi = 7`
- `TxTypes::TransferNonFungible_Multi_GasPayer = 8`
- `TxTypes::TransferNonFungible_Single = 5`
- `TxTypes::TransferNonFungible_Single_GasPayer = 6`

## Carbon/DataCommon.h

Source: `include/Carbon/DataCommon.h`

### Declarations

```cpp
inline void OS_ClearPinned(uint8_t*, size_t)
```

```cpp
inline void OS_FillRandom(uint8_t*, size_t)
```

```cpp
inline void OS_PinMemory(uint8_t*, size_t)
```

```cpp
struct ByteView
```

```cpp
struct BytesHasher
```

```cpp
struct BytesN
```

```cpp
struct BytesUpToN
```

```cpp
struct HashedByteView : public ByteView
```

```cpp
struct SmallString
```

```cpp
struct Witness
```

```cpp
struct Witnesses
```

```cpp
struct alignas(16) PrivateBytes : BytesN<N, B>
```

```cpp
typedef ::size_t size_t
```

```cpp
typedef BytesHasher<32> Bytes32Hasher
```

```cpp
typedef BytesN<16> Bytes16
```

```cpp
typedef BytesN<32> Bytes32
```

```cpp
typedef BytesN<64> Bytes64
```

```cpp
typedef PHANTASMA_VECTOR<uint8_t>::size_type size_t
```

```cpp
typedef PrivateBytes<32> Private32
```

```cpp
typedef PrivateBytes<64> Private64
```

```cpp
void OS_Assert(bool condition, const char* format, ...)
```

### Methods

```cpp
ByteView::const uint8_t* bytes
```

```cpp
ByteView::size_t length
```

```cpp
BytesN::Byte bytes[N]
```

```cpp
BytesN::BytesN() = default
```

```cpp
BytesN::constexpr static int length = N
```

```cpp
BytesUpToN::Byte bytes[N]
```

```cpp
BytesUpToN::constexpr static int max_length = N
```

```cpp
BytesUpToN::uint32_t length = 0
```

```cpp
HashedByteView::HashedByteView& operator=(const HashedByteView&)
```

```cpp
HashedByteView::HashedByteView()
```

```cpp
HashedByteView::HashedByteView(ByteView v)
```

```cpp
HashedByteView::HashedByteView(const HashedByteView&)
```

```cpp
HashedByteView::uint64_t hash
```

```cpp
SmallString::SmallString(const char* sz, size_t length)
```

```cpp
SmallString::mutable char bytes[256]
```

```cpp
SmallString::static SmallString Null() { return SmallString{ 0 }; } SmallString() = default
```

```cpp
SmallString::template<int N> constexpr SmallString(const char (&sz)[N]) : length(N - 1) } explicit SmallString(const char* sz, bool truncate = false)
```

```cpp
SmallString::uint8_t length
```

```cpp
Witness::Bytes32 address
```

```cpp
Witness::Bytes64 signature
```

```cpp
Witnesses::const Witness* witnesses
```

```cpp
Witnesses::uint32_t numWitnesses
```

```cpp
alignas::PrivateBytes() { OS_PinMemory((uint8_t*)this->bytes, this->length); } ~PrivateBytes() { OS_ClearPinned((uint8_t*)this->bytes, this->length); } PrivateBytes(const PrivateBytes& o) : PrivateBytes() } PrivateBytes& operator=(const PrivateBytes&) = default
```

## Carbon/DataVm.h

Source: `include/Carbon/DataVm.h`

### Declarations

```cpp
enum class VmType : uint8_t
```

```cpp
inline bool Read(VmDynamicStruct& out, const VmStructSchema& schema, ReadView& reader, Allocator& alloc)
```

```cpp
inline bool Read(VmDynamicVariable& out, ReadView& reader, Allocator& alloc)
```

```cpp
inline bool Read(VmDynamicVariable& out, const VmVariableSchema& schema, ReadView& reader, Allocator& alloc)
```

```cpp
inline bool Read(VmNamedDynamicVariable& out, ReadView& reader, Allocator& alloc)
```

```cpp
inline bool Read(VmNamedVariableSchema& out, ReadView& reader, Allocator& alloc)
```

```cpp
inline bool Read(VmType type, VmDynamicVariable& out, const VmStructSchema* schema, ReadView& reader, Allocator& alloc)
```

```cpp
inline bool Write(VmType type, const VmDynamicVariable& in, const VmStructSchema* schema, WriteView& writer)
```

```cpp
inline bool Write(const VmDynamicStruct& in, const VmStructSchema& schema, WriteView& writer)
```

```cpp
inline bool Write(const VmDynamicVariable& in, const VmVariableSchema& schema, WriteView& writer)
```

```cpp
inline void Write(const VmDynamicVariable& in, WriteView& writer)
```

```cpp
inline void Write(const VmNamedDynamicVariable& in, WriteView& writer)
```

```cpp
inline void Write(const VmNamedVariableSchema& in, WriteView& writer)
```

```cpp
std::vector<VmNamedDynamicVariable> sorted(in.fields, in.fields + in.numFields)
```

```cpp
struct NameLessThan
```

```cpp
struct StandardMeta
```

```cpp
struct VmDynamicVariable
```

```cpp
struct VmNamedDynamicVariable
```

```cpp
struct VmNamedVariableSchema
```

```cpp
struct VmStructArray
```

```cpp
struct VmVariableSchema
```

### Methods

```cpp
StandardMeta::inline static const SmallString id{ "_i" }
```

```cpp
StandardMeta::}
```

```cpp
VmDynamicVariable::VmDynamicVariable& operator=(const VmDynamicVariable&)
```

```cpp
VmDynamicVariable::VmDynamicVariable() = default
```

```cpp
VmDynamicVariable::VmDynamicVariable(ByteView v) : type(VmType::Bytes), arrayLength(1) { data.bytes = v; } VmDynamicVariable(const VmDynamicStruct& v) : type(VmType::Struct), arrayLength(1) { data.structure = v; } VmDynamicVariable(uint8_t v) : type(VmType::Int8), arrayLength(1) { data.int8 = v; } VmDynamicVariable(int8_t v) : type(VmType::Int8), arrayLength(1) { data.int8 = (uint8_t)v; } VmDynamicVariable(uint16_t v) : type(VmType::Int16), arrayLength(1) { data.int16 = v; } VmDynamicVariable(int16_t v) : type(VmType::Int16), arrayLength(1) { data.int16 = (uint16_t)v; } VmDynamicVariable(uint32_t v) : type(VmType::Int32), arrayLength(1) { data.int32 = v; } VmDynamicVariable(int32_t v) : type(VmType::Int32), arrayLength(1) { data.int32 = (uint32_t)v; } VmDynamicVariable(uint64_t v) : type(VmType::Int64), arrayLength(1) { data.int64 = v; } VmDynamicVariable(int64_t v) : type(VmType::Int64), arrayLength(1) { data.int64 = (uint64_t)v; } VmDynamicVariable(const int256& v) : type(VmType::Int256), arrayLength(1) { data.int256 = v.Unsigned(); } VmDynamicVariable(const uint256& v) : type(VmType::Int256), arrayLength(1) { data.int256 = v; } VmDynamicVariable(const Bytes16& v) : type(VmType::Bytes16), arrayLength(1) { data.bytes16 = v; } VmDynamicVariable(const Bytes32& v) : type(VmType::Bytes32), arrayLength(1) { data.bytes32 = v; } VmDynamicVariable(const Bytes64& v) : type(VmType::Bytes64), arrayLength(1) { data.bytes64 = v; } VmDynamicVariable(const char* v) : type(VmType::String), arrayLength(1) { data.string = v; } template<int N> VmDynamicVariable(const Bytes32 (&v)[N]) : type(VmType::Array_Bytes32), arrayLength(N) { data.bytes32Array = v; } template<int N> VmDynamicVariable(const VmDynamicStruct (&v)[N]) : type(VmType::Array_Struct), arrayLength(N) { data.structureArray = { {}, v }; } VmDynamicVariable& operator=(VmDynamicVariable&&) = default
```

```cpp
VmDynamicVariable::VmDynamicVariable(VmDynamicVariable&&) = default
```

```cpp
VmDynamicVariable::VmDynamicVariable(const VmDynamicVariable&)
```

```cpp
VmDynamicVariable::VmType type = VmType::Dynamic
```

```cpp
VmDynamicVariable::uint32_t arrayLength = 0
```

```cpp
VmDynamicVariable::union } data{}
```

```cpp
VmNamedDynamicVariable::SmallString name
```

```cpp
VmNamedDynamicVariable::VmDynamicVariable value
```

```cpp
VmNamedDynamicVariable::VmDynamicVariable* operator[](const SmallString&)
```

```cpp
VmNamedDynamicVariable::VmNamedDynamicVariable* fields = nullptr
```

```cpp
VmNamedDynamicVariable::const VmDynamicVariable* operator[](const SmallString&) const
```

```cpp
VmNamedDynamicVariable::static VmDynamicStruct Merge(const VmDynamicStruct& old, const VmDynamicStruct& updates, Allocator& a)
```

```cpp
VmNamedDynamicVariable::static bool IsSorted(uint32_t numFields, VmNamedDynamicVariable* fields)
```

```cpp
VmNamedDynamicVariable::template<int N> static VmDynamicStruct Sort(VmNamedDynamicVariable (&arr)[N]) { return Sort(N, arr); } static VmDynamicStruct Sort(uint32_t numFields, VmNamedDynamicVariable* fields)
```

```cpp
VmNamedDynamicVariable::uint32_t numFields = 0
```

```cpp
VmNamedDynamicVariable::void Erase(const VmDynamicVariable*)
```

```cpp
VmNamedVariableSchema::SchemaFlags flags = Flag_None
```

```cpp
VmNamedVariableSchema::SmallString name
```

```cpp
VmNamedVariableSchema::VmVariableSchema schema
```

```cpp
VmNamedVariableSchema::const VmNamedVariableSchema* fields = nullptr
```

```cpp
VmNamedVariableSchema::const VmNamedVariableSchema* operator[](const SmallString&) const
```

```cpp
VmNamedVariableSchema::enum SchemaFlags }
```

```cpp
VmNamedVariableSchema::static VmStructSchema Sort(uint32_t numFields, VmNamedVariableSchema* fields, bool allowDynamicExtras)
```

```cpp
VmNamedVariableSchema::static bool IsSorted(uint32_t numFields, VmNamedVariableSchema* fields)
```

```cpp
VmNamedVariableSchema::uint32_t numFields = 0
```

```cpp
VmStructArray::VmStructSchema schema{}
```

```cpp
VmStructArray::const VmDynamicStruct* structs = nullptr
```

```cpp
VmVariableSchema::VmStructSchema structure{}
```

```cpp
VmVariableSchema::VmType type = VmType::Dynamic
```

### Variants

- `VmType::Array = 1`
- `VmType::Array_Bytes = Array | Bytes`
- `VmType::Array_Bytes16 = Array | Bytes16`
- `VmType::Array_Bytes32 = Array | Bytes32`
- `VmType::Array_Bytes64 = Array | Bytes64`
- `VmType::Array_Int16 = Array | Int16`
- `VmType::Array_Int256 = Array | Int256`
- `VmType::Array_Int32 = Array | Int32`
- `VmType::Array_Int64 = Array | Int64`
- `VmType::Array_Int8 = Array | Int8`
- `VmType::Array_String = Array | String`
- `VmType::Array_Struct = Array | Struct`
- `VmType::Bytes = 1 << 1`
- `VmType::Bytes16 = 8 << 1`
- `VmType::Bytes32 = 9 << 1`
- `VmType::Bytes64 = 10 << 1`
- `VmType::Dynamic = 0`
- `VmType::Int16 = 4 << 1`
- `VmType::Int256 = 7 << 1`
- `VmType::Int32 = 5 << 1`
- `VmType::Int64 = 6 << 1`
- `VmType::Int8 = 3 << 1`
- `VmType::String = 11 << 1`
- `VmType::Struct = 2 << 1`

## Carbon/External/tiny-bignum-c/bn.h

Source: `include/Carbon/External/tiny-bignum-c/bn.h`

### Declarations

```cpp
int bignum_to_int(struct bn* n)
```

```cpp
struct bn
```

```cpp
void bignum_from_int(struct bn* n, DTYPE_TMP i)
```

```cpp
void bignum_from_string(struct bn* n, char* str, int nbytes)
```

```cpp
void bignum_init(struct bn* n)
```

```cpp
void bignum_to_string(struct bn* n, char* str, int maxsize)
```

### Methods

```cpp
bn::DTYPE array[BN_ARRAY_SIZE]
```

## Carbon/External/tiny-bignum-c/bn_impl.h

Source: `include/Carbon/External/tiny-bignum-c/bn_impl.h`

### Declarations

```cpp
static inline void _lshift_one_bit(struct bn* a)
```

```cpp
static inline void _lshift_word(struct bn* a, int nwords)
```

```cpp
static inline void _rshift_one_bit(struct bn* a)
```

```cpp
static inline void _rshift_word(struct bn* a, int nwords)
```

```cpp
struct bn current
```

```cpp
struct bn d
```

```cpp
struct bn low, high, mid, tmp
```

```cpp
struct bn row
```

```cpp
struct bn tmp
```

### Methods

```cpp
bn::_lshift_one_bit(&denom)
```

```cpp
bn::_rshift_one_bit(&mid)
```

```cpp
bn::bignum_add(&low, &mid, &mid)
```

```cpp
bn::bignum_assign(&tmp, c)
```

```cpp
bn::bignum_dec(&bcopy)
```

```cpp
bn::bignum_inc(&mid)
```

```cpp
bn::bignum_inc(c)
```

```cpp
bn::bignum_init(&row)
```

```cpp
bn::bignum_mul(&mid, &mid, &tmp)
```

```cpp
bn::for( int j = 0; j < BN_ARRAY_SIZE; ++j ) } bignum_add(c, &row, c)
```

```cpp
bn::if( bignum_cmp(&tmp, a) > 0 ) } else } bignum_sub(&high, &low, &mid)
```

```cpp
bn::if( denom.array[BN_ARRAY_SIZE - 1] >= half_max ) } _lshift_one_bit(&current)
```

```cpp
bn::if( iterations++ > maxIterations ) } bignum_mul(&tmp, a, c)
```

## Carbon/Int256.h

Source: `include/Carbon/Int256.h`

### Declarations

```cpp
class ReadView
```

```cpp
struct int256
```

```cpp
struct intx_pod
```

### Methods

```cpp
int256::ByteView Bytes() const
```

```cpp
int256::bool Is8ByteSafe() const
```

```cpp
int256::bool IsNegative() const
```

```cpp
int256::bool operator<(const int256& o) const { return Compare(o) < 0; } bool operator<=(const int256& o) const { return Compare(o) <= 0; } bool operator>(const int256& o) const { return Compare(o) > 0; } bool operator>=(const int256& o) const { return Compare(o) >= 0; } bool operator==(const int256& o) const { return Compare(o) == 0; } bool operator!=(const int256& o) const { return Compare(o) != 0; } bool operator!() const
```

```cpp
int256::const uint256& Unsigned() const
```

```cpp
int256::explicit int256(const uint256&)
```

```cpp
int256::explicit int256(int64_t)
```

```cpp
int256::explicit operator bool() const
```

```cpp
int256::explicit operator int64_t() const
```

```cpp
int256::int Compare(const int256&) const
```

```cpp
int256::int256 Abs() const
```

```cpp
int256::int256 operator%(const int256&) const
```

```cpp
int256::int256 operator&(const int256&) const
```

```cpp
int256::int256 operator*(const int256&) const
```

```cpp
int256::int256 operator+(const int256&) const
```

```cpp
int256::int256 operator++(int)
```

```cpp
int256::int256 operator-() const
```

```cpp
int256::int256 operator-(const int256&) const
```

```cpp
int256::int256 operator--(int)
```

```cpp
int256::int256 operator/(const int256&) const
```

```cpp
int256::int256 operator<<(int nbits) const
```

```cpp
int256::int256 operator>>(int nbits) const
```

```cpp
int256::int256 operator^(const int256&) const
```

```cpp
int256::int256 operator|(const int256&) const
```

```cpp
int256::int256 operator~() const
```

```cpp
int256::int256& operator%=(const int256&)
```

```cpp
int256::int256& operator&=(const int256&)
```

```cpp
int256::int256& operator*=(const int256&)
```

```cpp
int256::int256& operator++()
```

```cpp
int256::int256& operator+=(const int256&)
```

```cpp
int256::int256& operator--()
```

```cpp
int256::int256& operator-=(const int256&)
```

```cpp
int256::int256& operator/=(const int256&)
```

```cpp
int256::int256& operator<<=(int nbits)
```

```cpp
int256::int256& operator=(const int256&)
```

```cpp
int256::int256& operator>>=(int nbits)
```

```cpp
int256::int256& operator^=(const int256&)
```

```cpp
int256::int256& operator|=(const int256&)
```

```cpp
int256::int256() = default
```

```cpp
int256::int256(const int256&)
```

```cpp
int256::static int256 FromBytes(const ByteView&)
```

```cpp
int256::static int256 FromString(const char*, int length = 0, uint32_t base = 10)
```

```cpp
int256::std::string ToString(uint32_t base = 10, const char* customDictionary = 0, char negative = '-') const
```

```cpp
int256::uint256& Unsigned()
```

```cpp
intx_pod::bool operator!() const { return isBig ? !big : !normal; } explicit operator bool() const { return isBig ? (bool)big : (bool)normal; } explicit operator uint64_t() const { return isBig ? (uint64_t)big : normal; } explicit operator int64_t() const { return isBig ? (int64_t)big.Signed() : (int64_t)normal; } operator const uint256&() const { return Uint256(); } operator const int256&() const { return Int256(); } const uint256& Uint256() const } const int256& Int256() const } intx operator+(const intx& o) const
```

```cpp
intx_pod::bool operator==(const intx& o) const
```

```cpp
intx_pod::bool operator>(const intx& o) const
```

```cpp
intx_pod::intx operator-(const intx& o) const
```

```cpp
intx_pod::intx() = default
```

```cpp
intx_pod::intx(const intx& o) : isBig(o.isBig) } intx& operator=(const intx& o) } intx(const int256& o) : isBig(true) { big = o.Unsigned(); } intx(const uint256& o) : isBig(true) { big = o; } intx(int o) : isBig(false) { normal = (uint64_t)(int64_t)o; } intx(uint64_t o) : isBig(false) { normal = o; } intx(int64_t o) : isBig(false) { normal = (uint64_t)o; } static intx FromBytes(const ByteView&, bool isSigned = true)
```

```cpp
intx_pod::mutable bool isBig
```

```cpp
intx_pod::static intx Zero() { return intx((uint64_t)0); } static intx FromString(const char*, uint32_t length = 0, uint32_t base = 10, bool* out_error = 0)
```

```cpp
intx_pod::std::string ToString() const
```

```cpp
intx_pod::std::string ToStringUnsigned() const
```

```cpp
intx_pod::uint64_t data[(sizeof(intx) + 7) / 8]
```

```cpp
intx_pod::union }
```

## Carbon/Tx.h

Source: `include/Carbon/Tx.h`

### Declarations

```cpp
enum class ModuleId : uint32_t
```

```cpp
enum class TokenContract_Methods : uint32_t
```

```cpp
struct CreateSeriesFeeOptions : public FeeOptions
```

```cpp
struct CreateTokenFeeOptions : public FeeOptions
```

```cpp
struct CreateTokenSeriesTxHelper
```

```cpp
struct CreateTokenTxHelper
```

```cpp
struct FeeOptions
```

```cpp
struct MintNftFeeOptions : public FeeOptions
```

```cpp
struct MintNonFungibleTxHelper
```

```cpp
struct MintPhantasmaNonFungibleTxHelper
```

```cpp
struct TokenHelper
```

```cpp
struct TxEnvelope
```

```cpp
using namespace std::chrono
```

### Methods

```cpp
CreateSeriesFeeOptions::uint64_t gasFeeCreateSeriesBase
```

```cpp
CreateTokenFeeOptions::uint64_t gasFeeCreateTokenBase
```

```cpp
CreateTokenFeeOptions::uint64_t gasFeeCreateTokenSymbol
```

```cpp
FeeOptions::explicit FeeOptions(uint64_t base = 10000, uint64_t multiplier = 1000) : gasFeeBase(base), feeMultiplier(multiplier) } virtual ~FeeOptions() = default
```

```cpp
FeeOptions::uint64_t feeMultiplier
```

```cpp
FeeOptions::uint64_t gasFeeBase
```

```cpp
TxEnvelope::phantasma::carbon::Blockchain::TxMsg msg{}
```

```cpp
TxEnvelope::std::vector<ByteArray> buffers
```

### Variants

- `ModuleId::Governance = 0u`
- `ModuleId::Internal = 0xFFFFFFFFu`
- `ModuleId::Organization = 3u`
- `ModuleId::PhantasmaVm = 2u`
- `ModuleId::Token = 1u`
- `TokenContract_Methods::ApplyInflation = 22`
- `TokenContract_Methods::BurnFungible = 4`
- `TokenContract_Methods::BurnNonFungible = 9`
- `TokenContract_Methods::CreateMintedTokenSeries = 21`
- `TokenContract_Methods::CreateToken = 2`
- `TokenContract_Methods::CreateTokenSeries = 6`
- `TokenContract_Methods::DeleteTokenSeries = 7`
- `TokenContract_Methods::GetBalance = 5`
- `TokenContract_Methods::GetBalances = 20`
- `TokenContract_Methods::GetInstances = 10`
- `TokenContract_Methods::GetNextTokenInflation = 24`
- `TokenContract_Methods::GetNonFungibleInfo = 11`
- `TokenContract_Methods::GetNonFungibleInfoByRomId = 12`
- `TokenContract_Methods::GetSeriesInfo = 13`
- `TokenContract_Methods::GetSeriesInfoByMetaId = 14`
- `TokenContract_Methods::GetSeriesSupply = 18`
- `TokenContract_Methods::GetTokenIdBySymbol = 19`
- `TokenContract_Methods::GetTokenInfo = 15`
- `TokenContract_Methods::GetTokenInfoBySymbol = 16`
- `TokenContract_Methods::GetTokenSupply = 17`
- `TokenContract_Methods::MintFungible = 3`
- `TokenContract_Methods::MintNonFungible = 8`
- `TokenContract_Methods::MintPhantasmaNonFungible = 27`
- `TokenContract_Methods::SetTokensConfig = 25`
- `TokenContract_Methods::TransferFungible = 0`
- `TokenContract_Methods::TransferNonFungible = 1`
- `TokenContract_Methods::UpdateSeriesMetadata = 26`
- `TokenContract_Methods::UpdateTokenMetadata = 23`

## Carbon/Types.h

Source: `include/Carbon/Types.h`

### Declarations

```cpp
using IntX = intx
```

## Cryptography/Address.h

Source: `include/Cryptography/Address.h`

### Declarations

```cpp
class Address : public Serializable
```

```cpp
enum class AddressKind
```

### Methods

```cpp
Address::bool IsSystem() const } bool IsInterop() const { return Kind() == AddressKind::Interop; } bool IsUser() const { return Kind() == AddressKind::User; } bool operator==(const Address& B) const { return PHANTASMA_EQUAL(_bytes, _bytes + LengthInBytes, B._bytes); } bool operator!=(const Address& B) const { return !PHANTASMA_EQUAL(_bytes, _bytes + LengthInBytes, B._bytes); } String ToString() const } static Address FromWIF(const SecureString& wif) } static Address FromWIF(const Char* wif, int wifStringLength)
```

```cpp
Address::const String& Text() const } Address() } Address(const Address& o) } Address& operator=(const Address& o) } Address(const Byte* publicKey, int length) } Address(const ByteArray& publicKey) : Address(&publicKey.front(), (int)publicKey.size()) {} template<class IKeyPair> static Address FromKey(const IKeyPair& key) } static Address FromKey(const ByteArray& input) } static Address FromKey(const Byte* publicKeyBytes, int publicKeyLength) } static Address FromHash(const String& str) } static Address ForTokenContract(const Char* symbol) } static Address FromHash(const Byte* input, int inputLength) } AddressKind Kind() const { return IsNull() ? AddressKind::System : (AddressKind)_bytes[0]; } bool IsNull() const { return PHANTASMA_EQUAL(_bytes + 1, _bytes + LengthInBytes - 1, NullPublicKey); }
```

```cpp
Address::static constexpr Byte NullPublicKey[LengthInBytes] = {}
```

```cpp
Address::static constexpr int LengthInBytes = 34
```

```cpp
Address::static constexpr int MaxPlatformNameLength = 10
```

```cpp
Address::static constexpr int TextLength = 47
```

### Variants

- `AddressKind::Interop = 3`
- `AddressKind::Invalid = 0`
- `AddressKind::System = 2`
- `AddressKind::User = 1`

## Cryptography/EdDSA/Ed25519Signature.h

Source: `include/Cryptography/EdDSA/Ed25519Signature.h`

### Declarations

```cpp
class Ed25519Signature
```

### Methods

```cpp
Ed25519Signature::Ed25519Signature() } Ed25519Signature(const Byte* signature, int signatureLength) : Ed25519Signature() } Ed25519Signature(const ByteArray& signature) : Ed25519Signature(signature.empty() ? 0 : &signature.front(), (int)signature.size()) } Ed25519Signature& operator=(const Ed25519Signature& o) } constexpr static int Length = 64
```

```cpp
Ed25519Signature::constexpr static SignatureKind Kind = SignatureKind::Ed25519
```

## Cryptography/EncryptedKeyPair.h

Source: `include/Cryptography/EncryptedKeyPair.h`

### Declarations

```cpp
class EncryptedKeyPair
```

## Cryptography/Hash.h

Source: `include/Cryptography/Hash.h`

### Declarations

```cpp
class Hash : public Serializable
```

### Methods

```cpp
Hash::constexpr static int Length = 32
```

## Cryptography/KeyPair.h

Source: `include/Cryptography/KeyPair.h`

### Declarations

```cpp
class PhantasmaKeys
```

## Cryptography/PoW.h

Source: `include/Cryptography/PoW.h`

### Declarations

```cpp
enum class ProofOfWork
```

### Variants

- `ProofOfWork::Extreme = 30`
- `ProofOfWork::Hard = 19`
- `ProofOfWork::Heavy = 24`
- `ProofOfWork::Minimal = 5`
- `ProofOfWork::Moderate = 15`
- `ProofOfWork::None = 0`

## Cryptography/PrivateKey.h

Source: `include/Cryptography/PrivateKey.h`

### Declarations

```cpp
class PrivateKey
```

### Methods

```cpp
PrivateKey::constexpr static int Length = 32
```

## Cryptography/SHA.h

Source: `include/Cryptography/SHA.h`

### Declarations

```cpp
#define PHANTASMA_SHA256_LENGTH 32
```

## Cryptography/Signature.h

Source: `include/Cryptography/Signature.h`

### Declarations

```cpp
class Signature : public Serializable
```

## Cryptography/SignatureKind.h

Source: `include/Cryptography/SignatureKind.h`

### Declarations

```cpp
enum class SignatureKind
```

### Variants

- `SignatureKind::ECDSA`
- `SignatureKind::Ed25519`
- `SignatureKind::None`
- `SignatureKind::Ring`

## Domain/DomainSettings.h

Source: `include/Domain/DomainSettings.h`

### Declarations

```cpp
struct DomainSettings
```

### Methods

```cpp
DomainSettings::static const PHANTASMA_VECTOR<String>& SystemTokens() } static constexpr const char* RootChainName = "main"
```

```cpp
DomainSettings::static constexpr const char* FiatTokenName = "Dollars"
```

```cpp
DomainSettings::static constexpr const char* FiatTokenSymbol = "USD"
```

```cpp
DomainSettings::static constexpr const char* FuelPerContractDeployTag = "nexus.contract.cost"
```

```cpp
DomainSettings::static constexpr const char* FuelPerOrganizationDeployTag = "nexus.organization.cost"
```

```cpp
DomainSettings::static constexpr const char* FuelPerTokenDeployTag = "nexus.token.cost"
```

```cpp
DomainSettings::static constexpr const char* FuelTokenName = "Phantasma Energy"
```

```cpp
DomainSettings::static constexpr const char* FuelTokenSymbol = "KCAL"
```

```cpp
DomainSettings::static constexpr const char* InfusionName = "infusion"
```

```cpp
DomainSettings::static constexpr const char* LiquidityTokenName = "Phantasma Liquidity"
```

```cpp
DomainSettings::static constexpr const char* LiquidityTokenSymbol = "LP"
```

```cpp
DomainSettings::static constexpr const char* MastersOrganizationName = "masters"
```

```cpp
DomainSettings::static constexpr const char* NexusMainnet = "mainnet"
```

```cpp
DomainSettings::static constexpr const char* NexusTestnet = "testnet"
```

```cpp
DomainSettings::static constexpr const char* PhantomForceOrganizationName = "phantom_force"
```

```cpp
DomainSettings::static constexpr const char* PlatformName = "phantasma"
```

```cpp
DomainSettings::static constexpr const char* RewardTokenName = "Phantasma Crown"
```

```cpp
DomainSettings::static constexpr const char* RewardTokenSymbol = "CROWN"
```

```cpp
DomainSettings::static constexpr const char* StakersOrganizationName = "stakers"
```

```cpp
DomainSettings::static constexpr const char* StakingTokenName = "Phantasma Stake"
```

```cpp
DomainSettings::static constexpr const char* StakingTokenSymbol = "SOUL"
```

```cpp
DomainSettings::static constexpr const char* ValidatorsOrganizationName = "validators"
```

```cpp
DomainSettings::static constexpr int AddressMaxSize = 34
```

```cpp
DomainSettings::static constexpr int ArchiveMaxSize = 104857600
```

```cpp
DomainSettings::static constexpr int ArchiveMinSize = 64
```

```cpp
DomainSettings::static constexpr int ArgsMax = 64
```

```cpp
DomainSettings::static constexpr int DefaultMinimumGasFee = 100000
```

```cpp
DomainSettings::static constexpr int FiatTokenDecimals = 8
```

```cpp
DomainSettings::static constexpr int FieldMaxLength = 80
```

```cpp
DomainSettings::static constexpr int FieldMinLength = 1
```

```cpp
DomainSettings::static constexpr int FuelTokenDecimals = 10
```

```cpp
DomainSettings::static constexpr int InitialValidatorCount = 4
```

```cpp
DomainSettings::static constexpr int LatestKnownProtocol = 19
```

```cpp
DomainSettings::static constexpr int LiquidityTokenDecimals = 8
```

```cpp
DomainSettings::static constexpr int MAX_TOKEN_DECIMALS = 18
```

```cpp
DomainSettings::static constexpr int MaxEventsPerBlock = 2048
```

```cpp
DomainSettings::static constexpr int MaxEventsPerTx = 8096
```

```cpp
DomainSettings::static constexpr int MaxOracleEntriesPerBlock = 5120
```

```cpp
DomainSettings::static constexpr int MaxTriggerLoop = 5
```

```cpp
DomainSettings::static constexpr int MaxTxPerBlock = 1024
```

```cpp
DomainSettings::static constexpr int NameMaxLength = 255
```

```cpp
DomainSettings::static constexpr int Phantasma20Protocol = 7
```

```cpp
DomainSettings::static constexpr int Phantasma30Protocol = 8
```

```cpp
DomainSettings::static constexpr int ScriptMaxSize = 32767
```

```cpp
DomainSettings::static constexpr int StakingTokenDecimals = 8
```

```cpp
DomainSettings::static constexpr int UrlMaxLength = 2048
```

## Domain/Event.h

Source: `include/Domain/Event.h`

### Declarations

```cpp
class ChainValueEventData
```

```cpp
class Event
```

```cpp
class GasEventData
```

```cpp
class InfusionEventData : public Serializable
```

```cpp
class TokenEventData : public Serializable
```

```cpp
class TransactionSettleEventData
```

```cpp
enum class EventKind
```

### Methods

```cpp
ChainValueEventData::BigInteger value
```

```cpp
ChainValueEventData::String name
```

```cpp
Event::const Address address
```

```cpp
Event::const ByteArray data
```

```cpp
Event::const EventKind kind
```

```cpp
Event::const String contract
```

```cpp
Event::const String name
```

```cpp
GasEventData::const Address address
```

```cpp
GasEventData::const BigInteger amount
```

```cpp
GasEventData::const BigInteger price
```

```cpp
InfusionEventData::BigInteger infusedValue
```

```cpp
InfusionEventData::BigInteger tokenID
```

```cpp
InfusionEventData::InfusionEventData() = default
```

```cpp
InfusionEventData::String baseSymbol
```

```cpp
InfusionEventData::String chainName
```

```cpp
InfusionEventData::String infusedSymbol
```

```cpp
TokenEventData::const BigInteger value
```

```cpp
TokenEventData::const String chainName
```

```cpp
TokenEventData::const String symbol
```

```cpp
TransactionSettleEventData::const Hash hash
```

```cpp
TransactionSettleEventData::const String chain
```

```cpp
TransactionSettleEventData::const String platform
```

### Variants

- `EventKind::AddressLink = 10`
- `EventKind::AddressMigration = 46`
- `EventKind::AddressRegister = 9`
- `EventKind::AddressUnlink = 11`
- `EventKind::AddressUnregister = 17`
- `EventKind::ChainCreate = 1`
- `EventKind::ChainSwap = 43`
- `EventKind::ChannelCreate = 36`
- `EventKind::ChannelRefill = 37`
- `EventKind::ChannelSettle = 38`
- `EventKind::ContractDeploy = 45`
- `EventKind::ContractKill = 60`
- `EventKind::ContractRegister = 44`
- `EventKind::ContractUpgrade = 47`
- `EventKind::Crowdsale = 58`
- `EventKind::CrownRewards = 56`
- `EventKind::Custom = 64`
- `EventKind::Custom_V2 = 65`
- `EventKind::DomainCreate = 52`
- `EventKind::DomainDelete = 53`
- `EventKind::ExecutionFailure = 63`
- `EventKind::FeedCreate = 22`
- `EventKind::FeedUpdate = 23`
- `EventKind::FileCreate = 24`
- `EventKind::FileDelete = 25`
- `EventKind::GasEscrow = 15`
- `EventKind::GasPayment = 16`
- `EventKind::GovernanceSetChainConfig = 67`
- `EventKind::GovernanceSetGasConfig = 66`
- `EventKind::Inflation = 49`
- `EventKind::Infusion = 57`
- `EventKind::LeaderboardCreate = 39`
- `EventKind::LeaderboardInsert = 40`
- `EventKind::LeaderboardReset = 41`
- `EventKind::Log = 48`
- `EventKind::MasterClaim = 62`
- `EventKind::OrderBid = 59`
- `EventKind::OrderCancelled = 19`
- `EventKind::OrderClosed = 21`
- `EventKind::OrderCreated = 18`
- `EventKind::OrderFilled = 20`
- `EventKind::OrganizationAdd = 13`
- `EventKind::OrganizationCreate = 12`
- `EventKind::OrganizationKill = 61`
- `EventKind::OrganizationRemove = 14`
- `EventKind::OwnerAdded = 50`
- `EventKind::OwnerRemoved = 51`
- `EventKind::PackedNFT = 30`
- `EventKind::PlatformCreate = 42`
- `EventKind::PollClosed = 34`
- `EventKind::PollCreated = 33`
- `EventKind::PollVote = 35`
- `EventKind::SpecialResolution = 69`
- `EventKind::TaskStart = 54`
- `EventKind::TaskStop = 55`
- `EventKind::TokenBurn = 6`
- `EventKind::TokenClaim = 8`
- `EventKind::TokenCreate = 2`
- `EventKind::TokenMint = 5`
- `EventKind::TokenReceive = 4`
- `EventKind::TokenSend = 3`
- `EventKind::TokenSeriesCreate = 68`
- `EventKind::TokenStake = 7`
- `EventKind::Unknown = 0`
- `EventKind::ValidatorElect = 27`
- `EventKind::ValidatorPropose = 26`
- `EventKind::ValidatorRemove = 28`
- `EventKind::ValidatorSwitch = 29`
- `EventKind::ValueCreate = 31`
- `EventKind::ValueUpdate = 32`

## Domain/Token.h

Source: `include/Domain/Token.h`

### Declarations

```cpp
enum class TokenFlags : UInt32
```

### Variants

- `TokenFlags::Burnable = 1 << 8`
- `TokenFlags::Divisible = 1 << 3`
- `TokenFlags::Fiat = 1 << 6`
- `TokenFlags::Finite = 1 << 2`
- `TokenFlags::Foreign = 1 << 7`
- `TokenFlags::Fuel = 1 << 4`
- `TokenFlags::Fungible = 1 << 1`
- `TokenFlags::None = 0`
- `TokenFlags::Stakable = 1 << 5`
- `TokenFlags::Transferable = 1 << 0`

## Domain/ValidationUtils.h

Source: `include/Domain/ValidationUtils.h`

### Declarations

```cpp
struct ValidationUtils
```

### Methods

```cpp
ValidationUtils::static constexpr const char* ANONYMOUS_NAME = "anonymous"
```

```cpp
ValidationUtils::static constexpr const char* ENTRY_CONTEXT_NAME = "entry"
```

```cpp
ValidationUtils::static constexpr const char* GENESIS_NAME = "genesis"
```

```cpp
ValidationUtils::static constexpr const char* NULL_NAME = "null"
```

## Numerics/Base58.h

Source: `include/Numerics/Base58.h`

### Declarations

```cpp
BigInteger value(temp)
```

```cpp
SecureByteArray bufferAlloc(bufferSize, 0, false)
```

```cpp
SecureByteArray byteAllocation(numBytes, 0, false)
```

## Numerics/BigInteger.h

Source: `include/Numerics/BigInteger.h`

### Declarations

```cpp
class SecureVector
```

```cpp
struct SelectType
```

```cpp
struct SelectType<false, True, False>
```

### Methods

```cpp
SelectType::typedef False Type
```

```cpp
SelectType::typedef True Type
```

## PhantasmaAPI.h

Source: `include/PhantasmaAPI.h`

### Declarations

```cpp
#define PHANTASMA_API_INCLUDED
```

```cpp
#define PHANTASMA_CATCH(x) catch( std::runtime_error & x )
```

```cpp
#define PHANTASMA_CATCH(x) else
```

```cpp
#define PHANTASMA_CATCH_ALL() catch( ... )
```

```cpp
#define PHANTASMA_CATCH_ALL() else
```

```cpp
#define PHANTASMA_COPY(src, src_end, dst) std::copy(src, src_end, dst)
```

```cpp
#define PHANTASMA_EQUAL(a, b, c) std::equal(a, b, c)
```

```cpp
#define PHANTASMA_EXCEPTION(literal) \
```

```cpp
#define PHANTASMA_EXCEPTION(literal) throw std::runtime_error(literal)
```

```cpp
#define PHANTASMA_EXCEPTION_ENABLE
```

```cpp
#define PHANTASMA_EXCEPTION_MESSAGE(literal, string) \
```

```cpp
#define PHANTASMA_EXCEPTION_MESSAGE(literal, string) throw std::runtime_error(std::wstring_convert<std::codecvt_utf8<wchar_t>, wchar_t>().to_bytes(string))
```

```cpp
#define PHANTASMA_EXCEPTION_MESSAGE(literal, string) throw std::runtime_error(string)
```

```cpp
#define PHANTASMA_FUNCTION
```

```cpp
#define PHANTASMA_LITERAL(x) L##x
```

```cpp
#define PHANTASMA_LITERAL(x) x
```

```cpp
#define PHANTASMA_MAP std::map
```

```cpp
#define PHANTASMA_MAX(a, b) std::max(a, b)
```

```cpp
#define PHANTASMA_MIN(a, b) std::min(a, b)
```

```cpp
#define PHANTASMA_PAIR std::pair
```

```cpp
#define PHANTASMA_PROTOCOL 6
```

```cpp
#define PHANTASMA_STRLEN(x) strlen(x)
```

```cpp
#define PHANTASMA_STRLEN(x) wcslen(x)
```

```cpp
#define PHANTASMA_STRTOINT(x) std::strtoll(x, 0, 10)
```

```cpp
#define PHANTASMA_STRTOINT(x) std::wcstoll(x, 0, 10)
```

```cpp
#define PHANTASMA_SWAP(a, b) std::swap(a, b)
```

```cpp
#define PHANTASMA_TRY if( true )
```

```cpp
#define PHANTASMA_TRY try
```

```cpp
#define PHANTASMA_VECTOR std::vector
```

```cpp
: String(PHANTASMA_LITERAL(""))
```

```cpp
JSONArray AsArray(const JSONValue&, bool& out_error)
```

```cpp
JSONArray LookupArray(const JSONValue&, const Char* field, bool& out_error)
```

```cpp
JSONValue IndexArray(const JSONArray&, int index, bool& out_error)
```

```cpp
JSONValue LookupValue(const JSONValue&, const Char* field, bool& out_error)
```

```cpp
JSONValue Parse(const JSONDocument&)
```

```cpp
String AsString(const JSONValue&, bool& out_error)
```

```cpp
String LookupString(const JSONValue&, const Char* field, bool& out_error)
```

```cpp
bool AsBool(const JSONValue&, bool& out_error)
```

```cpp
bool HasArrayField(const JSONValue&, const Char* field, bool& out_error)
```

```cpp
bool HasField(const JSONValue&, const Char* field, bool& out_error)
```

```cpp
bool IsArray(const JSONValue&, bool& out_error)
```

```cpp
bool IsObject(const JSONValue&, bool& out_error)
```

```cpp
bool IsString(const JSONValue&, bool& out_error)
```

```cpp
bool LookupBool(const JSONValue&, const Char* field, bool& out_error)
```

```cpp
class PhantasmaAPI
```

```cpp
class PhantasmaJsonAPI
```

```cpp
enum class ExtendedEventType
```

```cpp
inline size_t SkipObject(const JSONValue& v, size_t i, bool& out_error)
```

```cpp
int ArraySize(const JSONArray&, bool& out_error)
```

```cpp
struct ABIEvent
```

```cpp
struct ABIMethod
```

```cpp
struct ABIParameter
```

```cpp
struct Account
```

```cpp
struct AccountTransactions
```

```cpp
struct Archive
```

```cpp
struct Auction
```

```cpp
struct Balance
```

```cpp
struct Block
```

```cpp
struct BuildInfoResult
```

```cpp
struct Chain
```

```cpp
struct Channel
```

```cpp
struct Contract
```

```cpp
struct CursorPaginatedResult
```

```cpp
struct Dapp
```

```cpp
struct Event
```

```cpp
struct EventExtended
```

```cpp
struct Governance
```

```cpp
struct Interop
```

```cpp
struct JSONBuilder
```

```cpp
struct Leaderboard
```

```cpp
struct LeaderboardRow
```

```cpp
struct MarketOrderData
```

```cpp
struct Nexus
```

```cpp
struct Oracle
```

```cpp
struct Organization
```

```cpp
struct Paginated
```

```cpp
struct Peer
```

```cpp
struct PhantasmaError
```

```cpp
struct PhantasmaVmConfig
```

```cpp
struct Platform
```

```cpp
struct Receipt
```

```cpp
struct Script
```

```cpp
struct SendCarbonTx
```

```cpp
struct SendRawTx
```

```cpp
struct Signature
```

```cpp
struct SpecialResolutionCall
```

```cpp
struct SpecialResolutionData
```

```cpp
struct Stake
```

```cpp
struct Storage
```

```cpp
struct Swap
```

```cpp
struct Token
```

```cpp
struct TokenCreateData
```

```cpp
struct TokenData
```

```cpp
struct TokenMintData
```

```cpp
struct TokenProperty
```

```cpp
struct TokenSchemas
```

```cpp
struct TokenSeries
```

```cpp
struct TokenSeriesCreateData
```

```cpp
struct Transaction
```

```cpp
struct Validator
```

```cpp
struct VmNamedVariableSchemaResult
```

```cpp
struct VmStructSchemaResult
```

```cpp
typedef JSONValue JSONArray
```

```cpp
typedef PHANTASMA_BYTE Byte
```

```cpp
typedef PHANTASMA_CHAR Char
```

```cpp
typedef PHANTASMA_HTTPCLIENT HttpClient
```

```cpp
typedef PHANTASMA_INT32 Int32
```

```cpp
typedef PHANTASMA_INT64 Int64
```

```cpp
typedef PHANTASMA_JSONARRAY JSONArray
```

```cpp
typedef PHANTASMA_JSONBUILDER JSONBuilder
```

```cpp
typedef PHANTASMA_JSONDOCUMENT JSONDocument
```

```cpp
typedef PHANTASMA_JSONVALUE JSONValue
```

```cpp
typedef PHANTASMA_STRING String
```

```cpp
typedef PHANTASMA_STRINGBUILDER StringBuilder
```

```cpp
typedef PHANTASMA_UINT32 UInt32
```

```cpp
typedef PHANTASMA_UINT64 UInt64
```

```cpp
typedef PHANTASMA_VECTOR<Byte> ByteArray
```

```cpp
typedef String JSONDocument
```

```cpp
typedef String JSONValue
```

```cpp
typedef char Char
```

```cpp
typedef int32_t Int32
```

```cpp
typedef int64_t Int64
```

```cpp
typedef std::string String
```

```cpp
typedef std::string_view JSONValue
```

```cpp
typedef std::stringstream StringBuilder
```

```cpp
typedef std::wstring String
```

```cpp
typedef std::wstring_view JSONValue
```

```cpp
typedef std::wstringstream StringBuilder
```

```cpp
typedef uint32_t UInt32
```

```cpp
typedef uint64_t UInt64
```

```cpp
typedef uint8_t Byte
```

```cpp
typedef wchar_t Char
```

```cpp
void AddArray(JSONBuilder&, const Char* key, Args... args)
```

```cpp
void AddString(JSONBuilder&, const Char* key, const Char* value)
```

```cpp
void BeginObject(JSONBuilder&)
```

```cpp
void EndObject(JSONBuilder&)
```

### Methods

```cpp
ABIEvent::Int32 value
```

```cpp
ABIEvent::String description
```

```cpp
ABIEvent::String name
```

```cpp
ABIEvent::String returnType
```

```cpp
ABIMethod::PHANTASMA_VECTOR<ABIParameter> parameters
```

```cpp
ABIMethod::String name
```

```cpp
ABIMethod::String returnType
```

```cpp
ABIParameter::String name
```

```cpp
ABIParameter::String type
```

```cpp
Account::PHANTASMA_VECTOR<Balance> balances
```

```cpp
Account::PHANTASMA_VECTOR<String> txs
```

```cpp
Account::Stake stakes
```

```cpp
Account::Storage storage
```

```cpp
Account::String address
```

```cpp
Account::String name
```

```cpp
Account::String relay
```

```cpp
Account::String stake
```

```cpp
Account::String unclaimed
```

```cpp
Account::String validator
```

```cpp
AccountTransactions::PHANTASMA_VECTOR<Transaction> txs
```

```cpp
AccountTransactions::String address
```

```cpp
Archive::Int32 blockCount
```

```cpp
Archive::PHANTASMA_VECTOR<Int32> missingBlocks
```

```cpp
Archive::PHANTASMA_VECTOR<String> owners
```

```cpp
Archive::String encryption
```

```cpp
Archive::String hash
```

```cpp
Archive::String name
```

```cpp
Archive::UInt32 size
```

```cpp
Archive::UInt32 time
```

```cpp
Auction::String baseSymbol
```

```cpp
Auction::String chainAddress
```

```cpp
Auction::String creatorAddress
```

```cpp
Auction::String price
```

```cpp
Auction::String quoteSymbol
```

```cpp
Auction::String ram
```

```cpp
Auction::String rom
```

```cpp
Auction::String tokenId
```

```cpp
Auction::UInt32 endDate
```

```cpp
Auction::UInt32 startDate
```

```cpp
Balance::PHANTASMA_VECTOR<String> ids
```

```cpp
Balance::String amount
```

```cpp
Balance::String chain
```

```cpp
Balance::String symbol
```

```cpp
Balance::UInt32 decimals
```

```cpp
Block::PHANTASMA_VECTOR<Event> events
```

```cpp
Block::PHANTASMA_VECTOR<Oracle> oracles
```

```cpp
Block::PHANTASMA_VECTOR<Transaction> txs
```

```cpp
Block::String chainAddress
```

```cpp
Block::String hash
```

```cpp
Block::String previousHash
```

```cpp
Block::String reward
```

```cpp
Block::String validatorAddress
```

```cpp
Block::UInt32 height
```

```cpp
Block::UInt32 protocol
```

```cpp
Block::UInt32 timestamp
```

```cpp
BuildInfoResult::String buildTimeUtc
```

```cpp
BuildInfoResult::String commit
```

```cpp
BuildInfoResult::String version
```

```cpp
Chain::PHANTASMA_VECTOR<String> contracts
```

```cpp
Chain::PHANTASMA_VECTOR<String> dapps
```

```cpp
Chain::String address
```

```cpp
Chain::String name
```

```cpp
Chain::String organization
```

```cpp
Chain::String parent
```

```cpp
Chain::UInt32 height
```

```cpp
Channel::Int32 index
```

```cpp
Channel::String balance
```

```cpp
Channel::String chain
```

```cpp
Channel::String creatorAddress
```

```cpp
Channel::String fee
```

```cpp
Channel::String name
```

```cpp
Channel::String symbol
```

```cpp
Channel::String targetAddress
```

```cpp
Channel::UInt32 creationTime
```

```cpp
Channel::bool active
```

```cpp
Contract::PHANTASMA_VECTOR<ABIEvent> events
```

```cpp
Contract::PHANTASMA_VECTOR<ABIMethod> methods
```

```cpp
Contract::String address
```

```cpp
Contract::String name
```

```cpp
Contract::String script
```

```cpp
CursorPaginatedResult::PHANTASMA_VECTOR<T> result
```

```cpp
CursorPaginatedResult::String cursor
```

```cpp
Dapp::String address
```

```cpp
Dapp::String chain
```

```cpp
Dapp::String name
```

```cpp
Event::String address
```

```cpp
Event::String contract
```

```cpp
Event::String data
```

```cpp
Event::String kind
```

```cpp
Event::String name
```

```cpp
EventExtended::ExtendedEventType type
```

```cpp
EventExtended::MarketOrderData marketOrder
```

```cpp
EventExtended::SpecialResolutionData specialResolution
```

```cpp
EventExtended::String address
```

```cpp
EventExtended::String contract
```

```cpp
EventExtended::String kind
```

```cpp
EventExtended::TokenCreateData tokenCreate
```

```cpp
EventExtended::TokenMintData tokenMint
```

```cpp
EventExtended::TokenSeriesCreateData tokenSeriesCreate
```

```cpp
Governance::String name
```

```cpp
Governance::String value
```

```cpp
Interop::String external
```

```cpp
Interop::String local
```

```cpp
JSONBuilder::StringBuilder s
```

```cpp
JSONBuilder::bool empty = true
```

```cpp
Leaderboard::PHANTASMA_VECTOR<LeaderboardRow> rows
```

```cpp
Leaderboard::String name
```

```cpp
LeaderboardRow::String address
```

```cpp
LeaderboardRow::String value
```

```cpp
MarketOrderData::Int64 endDate
```

```cpp
MarketOrderData::Int64 startDate
```

```cpp
MarketOrderData::String baseSymbol
```

```cpp
MarketOrderData::String buyer
```

```cpp
MarketOrderData::String endPrice
```

```cpp
MarketOrderData::String price
```

```cpp
MarketOrderData::String quoteSymbol
```

```cpp
MarketOrderData::String seller
```

```cpp
MarketOrderData::String tokenId
```

```cpp
MarketOrderData::String type
```

```cpp
MarketOrderData::UInt64 carbonBaseTokenId
```

```cpp
MarketOrderData::UInt64 carbonInstanceId
```

```cpp
MarketOrderData::UInt64 carbonQuoteTokenId
```

```cpp
Nexus::PHANTASMA_VECTOR<Chain> chains
```

```cpp
Nexus::PHANTASMA_VECTOR<Governance> governance
```

```cpp
Nexus::PHANTASMA_VECTOR<Platform> platforms
```

```cpp
Nexus::PHANTASMA_VECTOR<String> organizations
```

```cpp
Nexus::PHANTASMA_VECTOR<Token> tokens
```

```cpp
Nexus::String name
```

```cpp
Oracle::String content
```

```cpp
Oracle::String url
```

```cpp
Organization::PHANTASMA_VECTOR<String> members
```

```cpp
Organization::String id
```

```cpp
Organization::String name
```

```cpp
Paginated::JSONValue result
```

```cpp
Paginated::UInt32 page
```

```cpp
Paginated::UInt32 pageSize
```

```cpp
Paginated::UInt32 total
```

```cpp
Paginated::UInt32 totalPages
```

```cpp
Peer::String fee
```

```cpp
Peer::String flags
```

```cpp
Peer::String url
```

```cpp
Peer::String version
```

```cpp
Peer::UInt32 pow
```

```cpp
PhantasmaAPI::AccountTransactions GetAddressTransactions(const Char* account, UInt32 page, UInt32 pageSize, PhantasmaError* out_error = nullptr)
```

```cpp
PhantasmaAPI::Archive GetArchive(const Char* hashText, PhantasmaError* out_error = nullptr)
```

```cpp
PhantasmaAPI::Auction GetAuction(const Char* chainAddressOrName, const Char* symbol, const Char* IDtext, PhantasmaError* out_error = nullptr)
```

```cpp
PhantasmaAPI::Balance GetTokenBalance(const Char* account, const Char* tokenSymbol, const Char* chainInput, PhantasmaError* out_error = nullptr)
```

```cpp
PhantasmaAPI::Block GetBlockByHash(const Char* blockHash, PhantasmaError* out_error = nullptr)
```

```cpp
PhantasmaAPI::Block GetBlockByHeight(const Char* chainInput, const Char* height, PhantasmaError* out_error = nullptr)
```

```cpp
PhantasmaAPI::Block GetLatestBlock(const Char* chainInput, PhantasmaError* out_error = nullptr)
```

```cpp
PhantasmaAPI::BuildInfoResult GetVersion(PhantasmaError* out_error = nullptr)
```

```cpp
PhantasmaAPI::Chain GetChain(const Char* name, bool extended, PhantasmaError* out_error = nullptr)
```

```cpp
PhantasmaAPI::Contract GetContract(const Char* chainAddressOrName, const Char* contractName, PhantasmaError* out_error = nullptr)
```

```cpp
PhantasmaAPI::Contract GetContractByAddress(const Char* chainAddressOrName, const Char* contractAddress, PhantasmaError* out_error = nullptr)
```

```cpp
PhantasmaAPI::CursorPaginatedResult<Balance> GetAccountFungibleTokens(const Char* account, const Char* tokenSymbol, UInt64 carbonTokenId, UInt32 pageSize, const Char* cursor, bool checkAddressReservedByte, PhantasmaError* out_error = nullptr)
```

```cpp
PhantasmaAPI::CursorPaginatedResult<Token> GetAccountOwnedTokens(const Char* account, const Char* tokenSymbol, UInt64 carbonTokenId, UInt32 pageSize, const Char* cursor, bool checkAddressReservedByte, PhantasmaError* out_error = nullptr)
```

```cpp
PhantasmaAPI::CursorPaginatedResult<TokenData> GetAccountNFTs(const Char* account, const Char* tokenSymbol, UInt64 carbonTokenId, UInt32 carbonSeriesId, UInt32 pageSize, const Char* cursor, bool extended, bool checkAddressReservedByte, PhantasmaError* out_error = nullptr)
```

```cpp
PhantasmaAPI::CursorPaginatedResult<TokenData> GetTokenNFTs(UInt64 carbonTokenId, UInt32 carbonSeriesId, UInt32 pageSize, const Char* cursor, bool extended, PhantasmaError* out_error = nullptr)
```

```cpp
PhantasmaAPI::CursorPaginatedResult<TokenSeries> GetAccountOwnedTokenSeries(const Char* account, const Char* tokenSymbol, UInt64 carbonTokenId, UInt32 pageSize, const Char* cursor, bool checkAddressReservedByte, PhantasmaError* out_error = nullptr)
```

```cpp
PhantasmaAPI::CursorPaginatedResult<TokenSeries> GetTokenSeries(const Char* symbol, UInt64 carbonTokenId, UInt32 pageSize, const Char* cursor, PhantasmaError* out_error = nullptr)
```

```cpp
PhantasmaAPI::Int32 GetAddressTransactionCount(const Char* account, const Char* chainInput, PhantasmaError* out_error = nullptr)
```

```cpp
PhantasmaAPI::Int32 GetAuctionsCount(const Char* chainAddressOrName, const Char* symbol, PhantasmaError* out_error = nullptr)
```

```cpp
PhantasmaAPI::Int32 GetBlockHeight(const Char* chainInput, PhantasmaError* out_error = nullptr)
```

```cpp
PhantasmaAPI::Int32 GetBlockTransactionCountByHash(const Char* chainAddressOrName, const Char* blockHash, PhantasmaError* out_error = nullptr)
```

```cpp
PhantasmaAPI::Leaderboard GetLeaderboard(const Char* name, PhantasmaError* out_error = nullptr)
```

```cpp
PhantasmaAPI::Nexus GetNexus(bool extended, PhantasmaError* out_error = nullptr)
```

```cpp
PhantasmaAPI::Organization GetOrganization(const Char* ID, PhantasmaError* out_error = nullptr)
```

```cpp
PhantasmaAPI::Organization GetOrganizationByName(const Char* name, bool extended, PhantasmaError* out_error = nullptr)
```

```cpp
PhantasmaAPI::PHANTASMA_VECTOR<Account> GetAccounts(const Char* accountText, bool extended, bool checkAddressReservedByte, PhantasmaError* out_error = nullptr)
```

```cpp
PhantasmaAPI::PHANTASMA_VECTOR<Auction> GetAuctions(const Char* chainAddressOrName, const Char* symbol, UInt32 page, UInt32 pageSize, PhantasmaError* out_error = nullptr)
```

```cpp
PhantasmaAPI::PHANTASMA_VECTOR<Chain> GetChains(PhantasmaError* out_error = nullptr)
```

```cpp
PhantasmaAPI::PHANTASMA_VECTOR<Contract> GetContracts(const Char* chainAddressOrName, bool extended, PhantasmaError* out_error = nullptr)
```

```cpp
PhantasmaAPI::PHANTASMA_VECTOR<Organization> GetOrganizations(bool extended, PhantasmaError* out_error = nullptr)
```

```cpp
PhantasmaAPI::PHANTASMA_VECTOR<Token> GetTokens(bool extended, PhantasmaError* out_error = nullptr)
```

```cpp
PhantasmaAPI::PHANTASMA_VECTOR<Token> GetTokens(bool extended, const Char* ownerAddress, PhantasmaError* out_error = nullptr)
```

```cpp
PhantasmaAPI::PHANTASMA_VECTOR<TokenData> GetNFTs(const Char* symbol, const Char* IDtext, bool extended, PhantasmaError* out_error = nullptr)
```

```cpp
PhantasmaAPI::PhantasmaAPI(HttpClient& client) : m_httpClient(client) {} Account GetAccount(const Char* account, PhantasmaError* out_error = nullptr)
```

```cpp
PhantasmaAPI::PhantasmaVmConfig GetPhantasmaVmConfig(const Char* chainAddressOrName, PhantasmaError* out_error = nullptr)
```

```cpp
PhantasmaAPI::Script InvokeRawScript(const Char* chainInput, const Char* scriptData, PhantasmaError* out_error = nullptr)
```

```cpp
PhantasmaAPI::String LookUpName(const Char* name, PhantasmaError* out_error = nullptr)
```

```cpp
PhantasmaAPI::String ReadArchive(const Char* hashText, Int32 blockIndex, PhantasmaError* out_error = nullptr)
```

```cpp
PhantasmaAPI::String SendCarbonTransaction(const Char* txData, PhantasmaError* out_error = nullptr)
```

```cpp
PhantasmaAPI::String SendRawTransaction(const Char* txData, PhantasmaError* out_error = nullptr)
```

```cpp
PhantasmaAPI::Token GetToken(const Char* symbol, bool extended, PhantasmaError* out_error = nullptr)
```

```cpp
PhantasmaAPI::Token GetToken(const Char* symbol, bool extended, UInt64 carbonTokenId, PhantasmaError* out_error = nullptr)
```

```cpp
PhantasmaAPI::TokenData GetNFT(const Char* symbol, const Char* IDtext, bool extended, PhantasmaError* out_error = nullptr)
```

```cpp
PhantasmaAPI::TokenData GetTokenData(const Char* symbol, const Char* IDtext, PhantasmaError* out_error = nullptr)
```

```cpp
PhantasmaAPI::TokenSeries GetTokenSeriesById(const Char* symbol, UInt64 carbonTokenId, const Char* seriesId, UInt32 carbonSeriesId, PhantasmaError* out_error = nullptr)
```

```cpp
PhantasmaAPI::Transaction GetTransaction(const Char* hashText, PhantasmaError* out_error = nullptr)
```

```cpp
PhantasmaAPI::Transaction GetTransactionByBlockHashAndIndex(const Char* chainAddressOrName, const Char* blockHash, Int32 index, PhantasmaError* out_error = nullptr)
```

```cpp
PhantasmaAPI::bool WriteArchive(const Char* hashText, Int32 blockIndex, const Char* blockContent, PhantasmaError* out_error = nullptr)
```

```cpp
PhantasmaError::String message
```

```cpp
PhantasmaError::const static int HttpError = -2
```

```cpp
PhantasmaError::const static int InvalidJSON = -1
```

```cpp
PhantasmaError::const static int InvalidRpcResponse = -3
```

```cpp
PhantasmaError::const static int RpcMessage = -4
```

```cpp
PhantasmaError::int code = 0
```

```cpp
PhantasmaJsonAPI::static ABIEvent DeserializeABIEvent(const JSONValue& json, bool& jsonError)
```

```cpp
PhantasmaJsonAPI::static ABIMethod DeserializeABIMethod(const JSONValue& json, bool& jsonError)
```

```cpp
PhantasmaJsonAPI::static ABIParameter DeserializeABIParameter(const JSONValue& json, bool& jsonError)
```

```cpp
PhantasmaJsonAPI::static Account DeserializeAccount(const JSONValue& json, bool& jsonError)
```

```cpp
PhantasmaJsonAPI::static AccountTransactions DeserializeAccountTransactions(const JSONValue& json, bool& jsonError)
```

```cpp
PhantasmaJsonAPI::static Archive DeserializeArchive(const JSONValue& json, bool& jsonError)
```

```cpp
PhantasmaJsonAPI::static Auction DeserializeAuction(const JSONValue& json, bool& jsonError)
```

```cpp
PhantasmaJsonAPI::static Balance DeserializeBalance(const JSONValue& json, bool& jsonError)
```

```cpp
PhantasmaJsonAPI::static Block DeserializeBlock(const JSONValue& json, bool& jsonError)
```

```cpp
PhantasmaJsonAPI::static BuildInfoResult DeserializeBuildInfoResult(const JSONValue& json, bool& jsonError)
```

```cpp
PhantasmaJsonAPI::static Chain DeserializeChain(const JSONValue& json, bool& jsonError)
```

```cpp
PhantasmaJsonAPI::static Channel DeserializeChannel(const JSONValue& json, bool& jsonError)
```

```cpp
PhantasmaJsonAPI::static Contract DeserializeContract(const JSONValue& json, bool& jsonError)
```

```cpp
PhantasmaJsonAPI::static Dapp DeserializeDapp(const JSONValue& json, bool& jsonError)
```

```cpp
PhantasmaJsonAPI::static Event DeserializeEvent(const JSONValue& json, bool& jsonError)
```

```cpp
PhantasmaJsonAPI::static EventExtended DeserializeEventExtended(const JSONValue& json, bool& jsonError)
```

```cpp
PhantasmaJsonAPI::static Governance DeserializeGovernance(const JSONValue& json, bool& jsonError)
```

```cpp
PhantasmaJsonAPI::static Int32 DeserializeInt32(const JSONValue& json, bool& jsonError)
```

```cpp
PhantasmaJsonAPI::static Interop DeserializeInterop(const JSONValue& json, bool& jsonError)
```

```cpp
PhantasmaJsonAPI::static JSONValue CheckResponse(JSONValue response, PhantasmaError& out_error)
```

```cpp
PhantasmaJsonAPI::static Leaderboard DeserializeLeaderboard(const JSONValue& json, bool& jsonError)
```

```cpp
PhantasmaJsonAPI::static LeaderboardRow DeserializeLeaderboardRow(const JSONValue& json, bool& jsonError)
```

```cpp
PhantasmaJsonAPI::static MarketOrderData DeserializeMarketOrderData(const JSONValue& json, bool& jsonError)
```

```cpp
PhantasmaJsonAPI::static Nexus DeserializeNexus(const JSONValue& json, bool& jsonError)
```

```cpp
PhantasmaJsonAPI::static Oracle DeserializeOracle(const JSONValue& json, bool& jsonError)
```

```cpp
PhantasmaJsonAPI::static Organization DeserializeOrganization(const JSONValue& json, bool& jsonError)
```

```cpp
PhantasmaJsonAPI::static PHANTASMA_MAP<String, String> DeserializeStringMap(const JSONValue& json, bool& jsonError)
```

```cpp
PhantasmaJsonAPI::static Paginated DeserializePaginated(const JSONValue& json, bool& jsonError)
```

```cpp
PhantasmaJsonAPI::static Peer DeserializePeer(const JSONValue& json, bool& jsonError)
```

```cpp
PhantasmaJsonAPI::static PhantasmaVmConfig DeserializePhantasmaVmConfig(const JSONValue& json, bool& jsonError)
```

```cpp
PhantasmaJsonAPI::static Platform DeserializePlatform(const JSONValue& json, bool& jsonError)
```

```cpp
PhantasmaJsonAPI::static Receipt DeserializeReceipt(const JSONValue& json, bool& jsonError)
```

```cpp
PhantasmaJsonAPI::static Script DeserializeScript(const JSONValue& json, bool& jsonError)
```

```cpp
PhantasmaJsonAPI::static SendCarbonTx DeserializeSendCarbonTx(const JSONValue& json, bool& jsonError)
```

```cpp
PhantasmaJsonAPI::static SendRawTx DeserializeSendRawTx(const JSONValue& json, bool& jsonError)
```

```cpp
PhantasmaJsonAPI::static Signature DeserializeSignature(const JSONValue& json, bool& jsonError)
```

```cpp
PhantasmaJsonAPI::static SpecialResolutionCall DeserializeSpecialResolutionCall(const JSONValue& json, bool& jsonError)
```

```cpp
PhantasmaJsonAPI::static SpecialResolutionData DeserializeSpecialResolutionData(const JSONValue& json, bool& jsonError)
```

```cpp
PhantasmaJsonAPI::static Stake DeserializeStake(const JSONValue& json, bool& jsonError)
```

```cpp
PhantasmaJsonAPI::static Storage DeserializeStorage(const JSONValue& json, bool& jsonError)
```

```cpp
PhantasmaJsonAPI::static Swap DeserializeSwap(const JSONValue& json, bool& jsonError)
```

```cpp
PhantasmaJsonAPI::static Token DeserializeToken(const JSONValue& json, bool& jsonError)
```

```cpp
PhantasmaJsonAPI::static TokenCreateData DeserializeTokenCreateData(const JSONValue& json, bool& jsonError)
```

```cpp
PhantasmaJsonAPI::static TokenData DeserializeTokenData(const JSONValue& json, bool& jsonError)
```

```cpp
PhantasmaJsonAPI::static TokenMintData DeserializeTokenMintData(const JSONValue& json, bool& jsonError)
```

```cpp
PhantasmaJsonAPI::static TokenProperty DeserializeTokenProperty(const JSONValue& json, bool& jsonError)
```

```cpp
PhantasmaJsonAPI::static TokenSchemas DeserializeTokenSchemas(const JSONValue& json, bool& jsonError)
```

```cpp
PhantasmaJsonAPI::static TokenSeries DeserializeTokenSeries(const JSONValue& json, bool& jsonError)
```

```cpp
PhantasmaJsonAPI::static TokenSeriesCreateData DeserializeTokenSeriesCreateData(const JSONValue& json, bool& jsonError)
```

```cpp
PhantasmaJsonAPI::static TokenSeriesMode DeserializeTokenSeriesMode(const JSONValue& json, bool& jsonError)
```

```cpp
PhantasmaJsonAPI::static Transaction DeserializeTransaction(const JSONValue& json, bool& jsonError)
```

```cpp
PhantasmaJsonAPI::static Validator DeserializeValidator(const JSONValue& json, bool& jsonError)
```

```cpp
PhantasmaJsonAPI::static VmNamedVariableSchemaResult DeserializeVmNamedVariableSchemaResult(const JSONValue& json, bool& jsonError)
```

```cpp
PhantasmaJsonAPI::static VmStructSchemaResult DeserializeVmStructSchemaResult(const JSONValue& json, bool& jsonError)
```

```cpp
PhantasmaJsonAPI::static VmVariableSchemaResult DeserializeVmVariableSchemaResult(const JSONValue& json, bool& jsonError)
```

```cpp
PhantasmaJsonAPI::static bool Deserializebool(const JSONValue& json, bool& jsonError)
```

```cpp
PhantasmaJsonAPI::static bool ParseGetAccountFungibleTokensResponse(const JSONValue&, CursorPaginatedResult<Balance>& out, PhantasmaError* err = 0)
```

```cpp
PhantasmaJsonAPI::static bool ParseGetAccountNFTsResponse(const JSONValue&, CursorPaginatedResult<TokenData>& out, PhantasmaError* err = 0)
```

```cpp
PhantasmaJsonAPI::static bool ParseGetAccountOwnedTokenSeriesResponse(const JSONValue&, CursorPaginatedResult<TokenSeries>& out, PhantasmaError* err = 0)
```

```cpp
PhantasmaJsonAPI::static bool ParseGetAccountOwnedTokensResponse(const JSONValue&, CursorPaginatedResult<Token>& out, PhantasmaError* err = 0)
```

```cpp
PhantasmaJsonAPI::static bool ParseGetAccountResponse(const JSONValue&, Account& out, PhantasmaError* err = 0)
```

```cpp
PhantasmaJsonAPI::static bool ParseGetAccountsResponse(const JSONValue&, PHANTASMA_VECTOR<Account>& out, PhantasmaError* err = 0)
```

```cpp
PhantasmaJsonAPI::static bool ParseGetAddressTransactionCountResponse(const JSONValue&, Int32& out, PhantasmaError* err = 0)
```

```cpp
PhantasmaJsonAPI::static bool ParseGetAddressTransactionsResponse(const JSONValue&, AccountTransactions& out, PhantasmaError* err = 0)
```

```cpp
PhantasmaJsonAPI::static bool ParseGetArchiveResponse(const JSONValue&, Archive& out, PhantasmaError* err = 0)
```

```cpp
PhantasmaJsonAPI::static bool ParseGetAuctionResponse(const JSONValue&, Auction& out, PhantasmaError* err = 0)
```

```cpp
PhantasmaJsonAPI::static bool ParseGetAuctionsCountResponse(const JSONValue&, Int32& out, PhantasmaError* err = 0)
```

```cpp
PhantasmaJsonAPI::static bool ParseGetAuctionsResponse(const JSONValue&, PHANTASMA_VECTOR<Auction>& out, PhantasmaError* err = 0)
```

```cpp
PhantasmaJsonAPI::static bool ParseGetBlockByHashResponse(const JSONValue&, Block& out, PhantasmaError* err = 0)
```

```cpp
PhantasmaJsonAPI::static bool ParseGetBlockByHeightResponse(const JSONValue&, Block& out, PhantasmaError* err = 0)
```

```cpp
PhantasmaJsonAPI::static bool ParseGetBlockHeightResponse(const JSONValue&, Int32& out, PhantasmaError* err = 0)
```

```cpp
PhantasmaJsonAPI::static bool ParseGetBlockTransactionCountByHashResponse(const JSONValue&, Int32& out, PhantasmaError* err = 0)
```

```cpp
PhantasmaJsonAPI::static bool ParseGetChainResponse(const JSONValue&, Chain& out, PhantasmaError* err = 0)
```

```cpp
PhantasmaJsonAPI::static bool ParseGetChainsResponse(const JSONValue&, PHANTASMA_VECTOR<Chain>& out, PhantasmaError* err = 0)
```

```cpp
PhantasmaJsonAPI::static bool ParseGetContractByAddressResponse(const JSONValue&, Contract& out, PhantasmaError* err = 0)
```

```cpp
PhantasmaJsonAPI::static bool ParseGetContractResponse(const JSONValue&, Contract& out, PhantasmaError* err = 0)
```

```cpp
PhantasmaJsonAPI::static bool ParseGetContractsResponse(const JSONValue&, PHANTASMA_VECTOR<Contract>& out, PhantasmaError* err = 0)
```

```cpp
PhantasmaJsonAPI::static bool ParseGetLatestBlockResponse(const JSONValue&, Block& out, PhantasmaError* err = 0)
```

```cpp
PhantasmaJsonAPI::static bool ParseGetLeaderboardResponse(const JSONValue&, Leaderboard& out, PhantasmaError* err = 0)
```

```cpp
PhantasmaJsonAPI::static bool ParseGetNFTResponse(const JSONValue&, TokenData& out, PhantasmaError* err = 0)
```

```cpp
PhantasmaJsonAPI::static bool ParseGetNFTsResponse(const JSONValue&, PHANTASMA_VECTOR<TokenData>& out, PhantasmaError* err = 0)
```

```cpp
PhantasmaJsonAPI::static bool ParseGetNexusResponse(const JSONValue&, Nexus& out, PhantasmaError* err = 0)
```

```cpp
PhantasmaJsonAPI::static bool ParseGetOrganizationByNameResponse(const JSONValue&, Organization& out, PhantasmaError* err = 0)
```

```cpp
PhantasmaJsonAPI::static bool ParseGetOrganizationResponse(const JSONValue&, Organization& out, PhantasmaError* err = 0)
```

```cpp
PhantasmaJsonAPI::static bool ParseGetOrganizationsResponse(const JSONValue&, PHANTASMA_VECTOR<Organization>& out, PhantasmaError* err = 0)
```

```cpp
PhantasmaJsonAPI::static bool ParseGetPhantasmaVmConfigResponse(const JSONValue&, PhantasmaVmConfig& out, PhantasmaError* err = 0)
```

```cpp
PhantasmaJsonAPI::static bool ParseGetTokenBalanceResponse(const JSONValue&, Balance& out, PhantasmaError* err = 0)
```

```cpp
PhantasmaJsonAPI::static bool ParseGetTokenDataResponse(const JSONValue&, TokenData& out, PhantasmaError* err = 0)
```

```cpp
PhantasmaJsonAPI::static bool ParseGetTokenNFTsResponse(const JSONValue&, CursorPaginatedResult<TokenData>& out, PhantasmaError* err = 0)
```

```cpp
PhantasmaJsonAPI::static bool ParseGetTokenResponse(const JSONValue&, Token& out, PhantasmaError* err = 0)
```

```cpp
PhantasmaJsonAPI::static bool ParseGetTokenSeriesByIdResponse(const JSONValue&, TokenSeries& out, PhantasmaError* err = 0)
```

```cpp
PhantasmaJsonAPI::static bool ParseGetTokenSeriesResponse(const JSONValue&, CursorPaginatedResult<TokenSeries>& out, PhantasmaError* err = 0)
```

```cpp
PhantasmaJsonAPI::static bool ParseGetTokensResponse(const JSONValue&, PHANTASMA_VECTOR<Token>& out, PhantasmaError* err = 0)
```

```cpp
PhantasmaJsonAPI::static bool ParseGetTransactionByBlockHashAndIndexResponse(const JSONValue&, Transaction& out, PhantasmaError* err = 0)
```

```cpp
PhantasmaJsonAPI::static bool ParseGetTransactionResponse(const JSONValue&, Transaction& out, PhantasmaError* err = 0)
```

```cpp
PhantasmaJsonAPI::static bool ParseGetVersionResponse(const JSONValue&, BuildInfoResult& out, PhantasmaError* err = 0)
```

```cpp
PhantasmaJsonAPI::static bool ParseInvokeRawScriptResponse(const JSONValue&, Script& out, PhantasmaError* err = 0)
```

```cpp
PhantasmaJsonAPI::static bool ParseLookUpNameResponse(const JSONValue&, String& out, PhantasmaError* err = 0)
```

```cpp
PhantasmaJsonAPI::static bool ParseReadArchiveResponse(const JSONValue&, String& out, PhantasmaError* err = 0)
```

```cpp
PhantasmaJsonAPI::static bool ParseSendCarbonTransactionResponse(const JSONValue&, String& out, PhantasmaError* err = 0)
```

```cpp
PhantasmaJsonAPI::static bool ParseSendRawTransactionResponse(const JSONValue&, String& out, PhantasmaError* err = 0)
```

```cpp
PhantasmaJsonAPI::static bool ParseWriteArchiveResponse(const JSONValue&, bool& out, PhantasmaError* err = 0)
```

```cpp
PhantasmaJsonAPI::static const Char* Uri() { return PHANTASMA_LITERAL("/rpc"); } static void MakeGetAccountRequest(JSONBuilder&, const Char* account)
```

```cpp
PhantasmaJsonAPI::static void MakeGetAccountFungibleTokensRequest(JSONBuilder&, const Char* account, const Char* tokenSymbol, UInt64 carbonTokenId, UInt32 pageSize, const Char* cursor, bool checkAddressReservedByte)
```

```cpp
PhantasmaJsonAPI::static void MakeGetAccountNFTsRequest(JSONBuilder&, const Char* account, const Char* tokenSymbol, UInt64 carbonTokenId, UInt32 carbonSeriesId, UInt32 pageSize, const Char* cursor, bool extended, bool checkAddressReservedByte)
```

```cpp
PhantasmaJsonAPI::static void MakeGetAccountOwnedTokenSeriesRequest(JSONBuilder&, const Char* account, const Char* tokenSymbol, UInt64 carbonTokenId, UInt32 pageSize, const Char* cursor, bool checkAddressReservedByte)
```

```cpp
PhantasmaJsonAPI::static void MakeGetAccountOwnedTokensRequest(JSONBuilder&, const Char* account, const Char* tokenSymbol, UInt64 carbonTokenId, UInt32 pageSize, const Char* cursor, bool checkAddressReservedByte)
```

```cpp
PhantasmaJsonAPI::static void MakeGetAccountsRequest(JSONBuilder&, const Char* accountText, bool extended, bool checkAddressReservedByte)
```

```cpp
PhantasmaJsonAPI::static void MakeGetAddressTransactionCountRequest(JSONBuilder&, const Char* account, const Char* chainInput)
```

```cpp
PhantasmaJsonAPI::static void MakeGetAddressTransactionsRequest(JSONBuilder&, const Char* account, UInt32 page, UInt32 pageSize)
```

```cpp
PhantasmaJsonAPI::static void MakeGetArchiveRequest(JSONBuilder&, const Char* hashText)
```

```cpp
PhantasmaJsonAPI::static void MakeGetAuctionRequest(JSONBuilder&, const Char* chainAddressOrName, const Char* symbol, const Char* IDtext)
```

```cpp
PhantasmaJsonAPI::static void MakeGetAuctionsCountRequest(JSONBuilder&, const Char* chainAddressOrName, const Char* symbol)
```

```cpp
PhantasmaJsonAPI::static void MakeGetAuctionsRequest(JSONBuilder&, const Char* chainAddressOrName, const Char* symbol, UInt32 page, UInt32 pageSize)
```

```cpp
PhantasmaJsonAPI::static void MakeGetBlockByHashRequest(JSONBuilder&, const Char* blockHash)
```

```cpp
PhantasmaJsonAPI::static void MakeGetBlockByHeightRequest(JSONBuilder&, const Char* chainInput, const Char* height)
```

```cpp
PhantasmaJsonAPI::static void MakeGetBlockHeightRequest(JSONBuilder&, const Char* chainInput)
```

```cpp
PhantasmaJsonAPI::static void MakeGetBlockTransactionCountByHashRequest(JSONBuilder&, const Char* chainAddressOrName, const Char* blockHash)
```

```cpp
PhantasmaJsonAPI::static void MakeGetChainRequest(JSONBuilder&, const Char* name, bool extended)
```

```cpp
PhantasmaJsonAPI::static void MakeGetChainsRequest(JSONBuilder&)
```

```cpp
PhantasmaJsonAPI::static void MakeGetContractByAddressRequest(JSONBuilder&, const Char* chainAddressOrName, const Char* contractAddress)
```

```cpp
PhantasmaJsonAPI::static void MakeGetContractRequest(JSONBuilder&, const Char* chainAddressOrName, const Char* contractName)
```

```cpp
PhantasmaJsonAPI::static void MakeGetContractsRequest(JSONBuilder&, const Char* chainAddressOrName, bool extended)
```

```cpp
PhantasmaJsonAPI::static void MakeGetLatestBlockRequest(JSONBuilder&, const Char* chainInput)
```

```cpp
PhantasmaJsonAPI::static void MakeGetLeaderboardRequest(JSONBuilder&, const Char* name)
```

```cpp
PhantasmaJsonAPI::static void MakeGetNFTRequest(JSONBuilder&, const Char* symbol, const Char* IDtext, bool extended)
```

```cpp
PhantasmaJsonAPI::static void MakeGetNFTsRequest(JSONBuilder&, const Char* symbol, const Char* IDtext, bool extended)
```

```cpp
PhantasmaJsonAPI::static void MakeGetNexusRequest(JSONBuilder&, bool extended)
```

```cpp
PhantasmaJsonAPI::static void MakeGetOrganizationByNameRequest(JSONBuilder&, const Char* name, bool extended)
```

```cpp
PhantasmaJsonAPI::static void MakeGetOrganizationRequest(JSONBuilder&, const Char* ID)
```

```cpp
PhantasmaJsonAPI::static void MakeGetOrganizationsRequest(JSONBuilder&, bool extended)
```

```cpp
PhantasmaJsonAPI::static void MakeGetPhantasmaVmConfigRequest(JSONBuilder&, const Char* chainAddressOrName)
```

```cpp
PhantasmaJsonAPI::static void MakeGetTokenBalanceRequest(JSONBuilder&, const Char* account, const Char* tokenSymbol, const Char* chainInput)
```

```cpp
PhantasmaJsonAPI::static void MakeGetTokenDataRequest(JSONBuilder&, const Char* symbol, const Char* IDtext)
```

```cpp
PhantasmaJsonAPI::static void MakeGetTokenNFTsRequest(JSONBuilder&, UInt64 carbonTokenId, UInt32 carbonSeriesId, UInt32 pageSize, const Char* cursor, bool extended)
```

```cpp
PhantasmaJsonAPI::static void MakeGetTokenRequest(JSONBuilder&, const Char* symbol, bool extended, UInt64 carbonTokenId = 0)
```

```cpp
PhantasmaJsonAPI::static void MakeGetTokenSeriesByIdRequest(JSONBuilder&, const Char* symbol, UInt64 carbonTokenId, const Char* seriesId, UInt32 carbonSeriesId)
```

```cpp
PhantasmaJsonAPI::static void MakeGetTokenSeriesRequest(JSONBuilder&, const Char* symbol, UInt64 carbonTokenId, UInt32 pageSize, const Char* cursor)
```

```cpp
PhantasmaJsonAPI::static void MakeGetTokensRequest(JSONBuilder&, bool extended, const Char* ownerAddress = nullptr)
```

```cpp
PhantasmaJsonAPI::static void MakeGetTransactionByBlockHashAndIndexRequest(JSONBuilder&, const Char* chainAddressOrName, const Char* blockHash, Int32 index)
```

```cpp
PhantasmaJsonAPI::static void MakeGetTransactionRequest(JSONBuilder&, const Char* hashText)
```

```cpp
PhantasmaJsonAPI::static void MakeGetVersionRequest(JSONBuilder&)
```

```cpp
PhantasmaJsonAPI::static void MakeInvokeRawScriptRequest(JSONBuilder&, const Char* chainInput, const Char* scriptData)
```

```cpp
PhantasmaJsonAPI::static void MakeLookUpNameRequest(JSONBuilder&, const Char* name)
```

```cpp
PhantasmaJsonAPI::static void MakeReadArchiveRequest(JSONBuilder&, const Char* hashText, Int32 blockIndex)
```

```cpp
PhantasmaJsonAPI::static void MakeSendCarbonTransactionRequest(JSONBuilder&, const Char* txData)
```

```cpp
PhantasmaJsonAPI::static void MakeSendRawTransactionRequest(JSONBuilder&, const Char* txData)
```

```cpp
PhantasmaJsonAPI::static void MakeWriteArchiveRequest(JSONBuilder&, const Char* hashText, Int32 blockIndex, const Char* blockContent)
```

```cpp
PhantasmaVmConfig::Int32 featureLevel
```

```cpp
PhantasmaVmConfig::String fuelPerContractDeploy
```

```cpp
PhantasmaVmConfig::String gasAccount
```

```cpp
PhantasmaVmConfig::String gasConstructor
```

```cpp
PhantasmaVmConfig::String gasLeaderboard
```

```cpp
PhantasmaVmConfig::String gasNexus
```

```cpp
PhantasmaVmConfig::String gasOracle
```

```cpp
PhantasmaVmConfig::String gasOrganization
```

```cpp
PhantasmaVmConfig::String gasStandard
```

```cpp
PhantasmaVmConfig::bool isStored
```

```cpp
Platform::PHANTASMA_VECTOR<Interop> interop
```

```cpp
Platform::PHANTASMA_VECTOR<String> tokens
```

```cpp
Platform::String chain
```

```cpp
Platform::String fuel
```

```cpp
Platform::String platform
```

```cpp
Receipt::String channel
```

```cpp
Receipt::String index
```

```cpp
Receipt::String nexus
```

```cpp
Receipt::String receiver
```

```cpp
Receipt::String script
```

```cpp
Receipt::String sender
```

```cpp
Receipt::UInt32 timestamp
```

```cpp
Script::PHANTASMA_VECTOR<Event> events
```

```cpp
Script::PHANTASMA_VECTOR<Oracle> oracles
```

```cpp
Script::PHANTASMA_VECTOR<String> results
```

```cpp
Script::String result
```

```cpp
SendCarbonTx::String error
```

```cpp
SendCarbonTx::String hash
```

```cpp
SendRawTx::String error
```

```cpp
SendRawTx::String hash
```

```cpp
Signature::String Data
```

```cpp
Signature::String Kind
```

```cpp
SpecialResolutionCall::PHANTASMA_MAP<String, String> arguments
```

```cpp
SpecialResolutionCall::PHANTASMA_VECTOR<SpecialResolutionCall> calls
```

```cpp
SpecialResolutionCall::String method
```

```cpp
SpecialResolutionCall::String module
```

```cpp
SpecialResolutionCall::UInt32 methodId
```

```cpp
SpecialResolutionCall::UInt32 moduleId
```

```cpp
SpecialResolutionData::PHANTASMA_VECTOR<SpecialResolutionCall> calls
```

```cpp
SpecialResolutionData::String description
```

```cpp
SpecialResolutionData::UInt64 resolutionId
```

```cpp
Stake::String amount
```

```cpp
Stake::String unclaimed
```

```cpp
Stake::UInt32 time
```

```cpp
Storage::PHANTASMA_VECTOR<Archive> archives
```

```cpp
Storage::String avatar
```

```cpp
Storage::UInt32 available
```

```cpp
Storage::UInt32 used
```

```cpp
Swap::String destinationAddress
```

```cpp
Swap::String destinationChain
```

```cpp
Swap::String destinationHash
```

```cpp
Swap::String destinationPlatform
```

```cpp
Swap::String sourceAddress
```

```cpp
Swap::String sourceChain
```

```cpp
Swap::String sourceHash
```

```cpp
Swap::String sourcePlatform
```

```cpp
Swap::String symbol
```

```cpp
Swap::String value
```

```cpp
Token::Int32 decimals
```

```cpp
Token::PHANTASMA_VECTOR<TokenProperty> metadata
```

```cpp
Token::PHANTASMA_VECTOR<TokenSeries> series
```

```cpp
Token::String address
```

```cpp
Token::String burnedSupply
```

```cpp
Token::String carbonId
```

```cpp
Token::String currentSupply
```

```cpp
Token::String flags
```

```cpp
Token::String maxSupply
```

```cpp
Token::String name
```

```cpp
Token::String owner
```

```cpp
Token::String script
```

```cpp
Token::String symbol
```

```cpp
Token::TokenSchemas tokenSchemas
```

```cpp
TokenCreateData::PHANTASMA_MAP<String, String> metadata
```

```cpp
TokenCreateData::String maxSupply
```

```cpp
TokenCreateData::String symbol
```

```cpp
TokenCreateData::UInt32 decimals
```

```cpp
TokenCreateData::UInt64 carbonTokenId
```

```cpp
TokenCreateData::bool isNonFungible
```

```cpp
TokenData::PHANTASMA_VECTOR<TokenProperty> infusion
```

```cpp
TokenData::PHANTASMA_VECTOR<TokenProperty> properties
```

```cpp
TokenData::String ID
```

```cpp
TokenData::String carbonNftAddress
```

```cpp
TokenData::String carbonSeriesId
```

```cpp
TokenData::String carbonTokenId
```

```cpp
TokenData::String chainName
```

```cpp
TokenData::String creatorAddress
```

```cpp
TokenData::String mint
```

```cpp
TokenData::String ownerAddress
```

```cpp
TokenData::String ram
```

```cpp
TokenData::String rom
```

```cpp
TokenData::String series
```

```cpp
TokenData::String status
```

```cpp
TokenMintData::PHANTASMA_MAP<String, String> metadata
```

```cpp
TokenMintData::String owner
```

```cpp
TokenMintData::String seriesId
```

```cpp
TokenMintData::String symbol
```

```cpp
TokenMintData::String tokenId
```

```cpp
TokenMintData::UInt32 carbonSeriesId
```

```cpp
TokenMintData::UInt32 mintNumber
```

```cpp
TokenMintData::UInt64 carbonInstanceId
```

```cpp
TokenMintData::UInt64 carbonTokenId
```

```cpp
TokenProperty::String Key
```

```cpp
TokenProperty::String Value
```

```cpp
TokenSchemas::VmStructSchemaResult ram
```

```cpp
TokenSchemas::VmStructSchemaResult rom
```

```cpp
TokenSchemas::VmStructSchemaResult seriesMetadata
```

```cpp
TokenSeries::PHANTASMA_VECTOR<ABIMethod> methods
```

```cpp
TokenSeries::PHANTASMA_VECTOR<TokenProperty> metadata
```

```cpp
TokenSeries::String burnedSupply
```

```cpp
TokenSeries::String carbonSeriesId
```

```cpp
TokenSeries::String carbonTokenId
```

```cpp
TokenSeries::String currentSupply
```

```cpp
TokenSeries::String maxMint
```

```cpp
TokenSeries::String maxSupply
```

```cpp
TokenSeries::String mintCount
```

```cpp
TokenSeries::String ownerAddress
```

```cpp
TokenSeries::String script
```

```cpp
TokenSeries::String seriesId
```

```cpp
TokenSeries::TokenSeriesMode mode
```

```cpp
TokenSeriesCreateData::PHANTASMA_MAP<String, String> metadata
```

```cpp
TokenSeriesCreateData::String owner
```

```cpp
TokenSeriesCreateData::String seriesId
```

```cpp
TokenSeriesCreateData::String symbol
```

```cpp
TokenSeriesCreateData::UInt32 carbonSeriesId
```

```cpp
TokenSeriesCreateData::UInt32 maxMint
```

```cpp
TokenSeriesCreateData::UInt32 maxSupply
```

```cpp
TokenSeriesCreateData::UInt64 carbonTokenId
```

```cpp
Transaction::Byte carbonTxType
```

```cpp
Transaction::Int32 blockHeight
```

```cpp
Transaction::PHANTASMA_VECTOR<Event> events
```

```cpp
Transaction::PHANTASMA_VECTOR<EventExtended> extendedEvents
```

```cpp
Transaction::PHANTASMA_VECTOR<Signature> signatures
```

```cpp
Transaction::String blockHash
```

```cpp
Transaction::String carbonTxData
```

```cpp
Transaction::String chainAddress
```

```cpp
Transaction::String debugComment
```

```cpp
Transaction::String fee
```

```cpp
Transaction::String gasLimit
```

```cpp
Transaction::String gasPayer
```

```cpp
Transaction::String gasPrice
```

```cpp
Transaction::String gasTarget
```

```cpp
Transaction::String hash
```

```cpp
Transaction::String payload
```

```cpp
Transaction::String result
```

```cpp
Transaction::String script
```

```cpp
Transaction::String sender
```

```cpp
Transaction::String state
```

```cpp
Transaction::UInt32 expiration
```

```cpp
Transaction::UInt32 timestamp
```

```cpp
Validator::String address
```

```cpp
Validator::String type
```

```cpp
VmNamedVariableSchemaResult::String name
```

```cpp
VmNamedVariableSchemaResult::VmVariableSchemaResult schema
```

```cpp
VmStructSchemaResult::Int32 flags
```

```cpp
VmStructSchemaResult::PHANTASMA_VECTOR<VmNamedVariableSchemaResult> fields
```

```cpp
VmStructSchemaResult::String type
```

```cpp
VmStructSchemaResult::std::shared_ptr<VmStructSchemaResult> schema
```

### Variants

- `ExtendedEventType::MarketOrder`
- `ExtendedEventType::SpecialResolution`
- `ExtendedEventType::TokenCreate`
- `ExtendedEventType::TokenMint`
- `ExtendedEventType::TokenSeriesCreate`
- `ExtendedEventType::Unknown`

## Security/SecureByteArray.h

Source: `include/Security/SecureByteArray.h`

### Declarations

```cpp
class SecureByteReader
```

```cpp
class SecureByteWriter
```

### Methods

```cpp
SecureByteReader::SecureByteArray() {} SecureByteArray(int size, const Byte* data = 0, bool protectAccess = true) : m_size(size), m_protectAccess(protectAccess) } SecureByteArray(SecureByteArray&& other) : m_data(other.m_data), m_size(other.m_size), m_readers(other.m_readers), m_writers(other.m_writers), m_encrypted(other.m_encrypted), m_protectAccess(other.m_protectAccess) } SecureByteArray(const SecureByteArray& other) } ~SecureByteArray() } SecureByteArray& operator=(SecureByteArray&& other) } SecureByteArray& operator=(const SecureByteArray& other)
```

```cpp
SecureByteReader::SecureByteWriter Write()
```

```cpp
SecureByteReader::bool Empty() const { return m_size == 0; } UInt32 Size() const { return (UInt32)m_size; } SecureByteReader Read() const
```

## Security/SecureMemory.h

Source: `include/Security/SecureMemory.h`

### Declarations

```cpp
#define PHANTASMA_LOCKMEM(pointer, size)
```

```cpp
#define PHANTASMA_SECURE_ALLOC(size) malloc(size)
```

```cpp
#define PHANTASMA_SECURE_ALLOC_ALIGNMENT 1
```

```cpp
#define PHANTASMA_SECURE_DECRYPT_MEMORY(m, l) true
```

```cpp
#define PHANTASMA_SECURE_ENCRYPT_MEMORY(m, l) false
```

```cpp
#define PHANTASMA_SECURE_FREE(ptr) free(ptr)
```

```cpp
#define PHANTASMA_SECURE_NOACCESS(ptr, size)
```

```cpp
#define PHANTASMA_SECURE_READONLY(ptr, size)
```

```cpp
#define PHANTASMA_SECURE_READWRITE(ptr, size)
```

```cpp
#define PHANTASMA_UNLOCKMEM(pointer, size) memset(pointer, 0, size)
```

```cpp
#define PHANTASMA_WIPEMEM(buffer, size) memset(buffer, 0, size)
```

```cpp
class MemoryPin
```

```cpp
class PinnedBytes
```

### Methods

```cpp
PinnedBytes::MemoryPin pin
```

```cpp
PinnedBytes::PinnedBytes() : pin(bytes, N) {} Byte bytes[N]
```

```cpp
PinnedBytes::const static int Length = N
```

## Security/SecureString.h

Source: `include/Security/SecureString.h`

### Declarations

```cpp
class SecureString
```

### Methods

```cpp
SecureString::SecureString() } SecureString(const SecureString& o) : data(o.data) } typedef SecureVector<Char>::size_type size_type
```

## Security/SecureVector.h

Source: `include/Security/SecureVector.h`

### Declarations

```cpp
class SecureVector
```

### Methods

```cpp
SecureVector::SecureVector() } ~SecureVector() } SecureVector(const SecureVector& other) } SecureVector& operator=(const SecureVector& other) } typedef typename PHANTASMA_VECTOR<T>::size_type size_type
```

## Utils/BinaryReader.h

Source: `include/Utils/BinaryReader.h`

### Declarations

```cpp
class Hash
```

### Methods

```cpp
Hash::BinaryReader(const ByteArray& stream, int cursor = 0) : stream(stream), cursor((UInt32)cursor) } bool Finished() const { return cursor == stream.size(); } bool Error() const { return error; } const ByteArray& ToArray() { return stream; } UInt32 Position() const { return cursor; } void Seek(UInt32 position) } Byte ReadByte() } bool ReadBool() } void Read(uint8_t& b) } void Read(int8_t& b) } void Read(uint16_t& b) } void Read(int16_t& b) } void Read(uint32_t& b) } void Read(int32_t& b) } void Read(uint64_t& b) } void Read(int64_t& b) } void Read(Byte* b, int size) } void Read(ByteArray& bytes, int size) } void ReadVarInt(Int64& output) } void ReadBigInteger(BigInteger& n) } void ReadUInt32(UInt32& n) } void ReadByteArray(ByteArray& bytes, int maxToRead = 0) } int ReadByteArray(Byte* bytes, int maxToRead) } template<int N> void ReadByteArray(Byte (&bytes)[N]) } template<int N> int ReadFixedByteArray(Byte (&bytes)[N]) } void ReadVarString(String& text) } void ReadAddress(Address& address)
```

```cpp
Hash::void ReadHash(Hash& hash)
```

```cpp
Hash::void ReadSignature(Signature& hash)
```

## Utils/BinaryWriter.h

Source: `include/Utils/BinaryWriter.h`

### Declarations

```cpp
class Hash
```

## Utils/RpcUtils.h

Source: `include/Utils/RpcUtils.h`

### Declarations

```cpp
Transaction tx(nexus, chain, script, Timestamp::Now() + Timespan::FromMinutes(1), payload)
```

```cpp
enum class TransactionState
```

```cpp
struct TxTokenEvent
```

```cpp
typedef void(FnCallback)(void)
```

### Methods

```cpp
TxTokenEvent::TokenEventData data
```

```cpp
TxTokenEvent::const rpc::Event* event
```

### Variants

- `TransactionState::Confirmed`
- `TransactionState::Pending`
- `TransactionState::Rejected`
- `TransactionState::Unknown`

## Utils/Serializable.h

Source: `include/Utils/Serializable.h`

### Declarations

```cpp
class Serializable
```

```cpp
struct Serialization
```

```cpp
struct Serialization<String>
```

## Utils/TextUtils.h

Source: `include/Utils/TextUtils.h`

### Declarations

```cpp
ByteArray temp(requiredSize * 2 + 2)
```

```cpp
ByteArray temp(requiredSize * 2)
```

## Utils/Timestamp.h

Source: `include/Utils/Timestamp.h`

### Declarations

```cpp
class Timespan
```

```cpp
class Timestamp
```

### Methods

```cpp
Timespan::const Int32 Value
```

```cpp
Timestamp::ValueType Value
```

```cpp
Timestamp::typedef UInt32 ValueType
```

## VM/Opcodes.h

Source: `include/VM/Opcodes.h`

### Declarations

```cpp
enum class Opcode
```

### Variants

- `Opcode::ABS`
- `Opcode::ADD`
- `Opcode::AND`
- `Opcode::CALL`
- `Opcode::CAST`
- `Opcode::CAT`
- `Opcode::CLEAR`
- `Opcode::COPY`
- `Opcode::COUNT`
- `Opcode::CTX`
- `Opcode::DEBUG`
- `Opcode::DEC`
- `Opcode::DIV`
- `Opcode::EQUAL`
- `Opcode::EXTCALL`
- `Opcode::GET`
- `Opcode::GT`
- `Opcode::GTE`
- `Opcode::INC`
- `Opcode::JMP`
- `Opcode::JMPIF`
- `Opcode::JMPNOT`
- `Opcode::LEFT`
- `Opcode::LOAD`
- `Opcode::LT`
- `Opcode::LTE`
- `Opcode::MAX`
- `Opcode::MIN`
- `Opcode::MOD`
- `Opcode::MOVE`
- `Opcode::MUL`
- `Opcode::NEGATE`
- `Opcode::NOP`
- `Opcode::NOT`
- `Opcode::OR`
- `Opcode::PACK`
- `Opcode::POP`
- `Opcode::POW`
- `Opcode::PUSH`
- `Opcode::PUT`
- `Opcode::RET`
- `Opcode::RIGHT`
- `Opcode::SHL`
- `Opcode::SHR`
- `Opcode::SIGN`
- `Opcode::SIZE`
- `Opcode::SUB`
- `Opcode::SUBSTR`
- `Opcode::SWAP`
- `Opcode::SWITCH`
- `Opcode::THROW`
- `Opcode::UNPACK`
- `Opcode::XOR`

## VM/ScriptBuilder.h

Source: `include/VM/ScriptBuilder.h`

### Declarations

```cpp
class ScriptBuilder
```

### Methods

```cpp
ScriptBuilder::ScriptBuilder& EmitExtCall(const Char* method, Byte reg = 0) } ScriptBuilder& EmitLoad(Byte reg, const ByteArray& bytes) } ScriptBuilder& EmitLoad(Byte reg, const Byte* bytes, int numBytes, VMType type = VMType::Bytes) } ScriptBuilder& EmitLoad(Byte reg, const String& val) } ScriptBuilder& EmitLoad(Byte reg, const Char* val) } ScriptBuilder& EmitLoad(Byte reg, const BigInteger& val) } ScriptBuilder& EmitLoad(Byte reg, bool val) } template<class T, typename std::enable_if<std::is_enum<T>::value>::type* = nullptr> ScriptBuilder& EmitLoad(Byte reg, T enum_val) } ScriptBuilder& EmitLoad(Byte reg, const Timestamp& val) } template<class TSerializable, typename std::enable_if<std::is_base_of<Serializable, TSerializable>::value>::type* = nullptr> ScriptBuilder& EmitLoad(Byte reg, const TSerializable& val) } ScriptBuilder& EmitMove(Byte src_reg, Byte dst_reg) } ScriptBuilder& EmitCopy(Byte src_reg, Byte dst_reg) } ScriptBuilder& EmitThrow(const ByteArray& data) } ScriptBuilder& EmitLabel(const String& label) } ScriptBuilder& EmitJump(Opcode opcode, const String& label, Byte reg = 0) } ScriptBuilder& EmitCall(const String& label, Byte regCount) } ScriptBuilder& EmitConditionalJump(Opcode opcode, Byte src_reg, const String& label) } ScriptBuilder& EmitVarBytes(long value) } ScriptBuilder& EmitRaw(const Byte* bytes, int numBytes) } ByteArray ToScript() } constexpr static const Char* GasContract = PHANTASMA_LITERAL("gas")
```

```cpp
ScriptBuilder::constexpr static const Char* EnergyContract = PHANTASMA_LITERAL("energy")
```

```cpp
ScriptBuilder::constexpr static const Char* NexusContract = PHANTASMA_LITERAL("nexus")
```

```cpp
ScriptBuilder::constexpr static const Char* StakeContract = PHANTASMA_LITERAL("stake")
```

```cpp
ScriptBuilder::constexpr static const Char* SwapContract = PHANTASMA_LITERAL("swap")
```

```cpp
ScriptBuilder::constexpr static const Char* TokenContract = PHANTASMA_LITERAL("token")
```

## VM/VMObject.h

Source: `include/VM/VMObject.h`

### Declarations

```cpp
#define PHANTASMA_PROFILE(name)
```

```cpp
class VMObject
```

```cpp
enum class VMType
```

### Variants

- `VMType::Bool`
- `VMType::Bytes`
- `VMType::Enum`
- `VMType::None`
- `VMType::Number`
- `VMType::Object`
- `VMType::String`
- `VMType::Struct`
- `VMType::Timestamp`

## VM/VirtualMachine.h

Source: `include/VM/VirtualMachine.h`

### Declarations

```cpp
class VirtualMachine
```

### Methods

```cpp
VirtualMachine::static constexpr int DefaultRegisterCount = 32
```

```cpp
VirtualMachine::static constexpr int MaxRegisterCount = 32
```
