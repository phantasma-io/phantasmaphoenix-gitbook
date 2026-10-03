# C++ SDK Token Deployment

A token is created by one structured transaction that calls
`Token.CreateToken`. An NFT token then needs at least one series before
anything can be minted, and each series is one more transaction. The builders
live in `Carbon/Contracts/Token.h`, `Carbon/Contracts/TokenSchemas.h` and
`Carbon/Tx.h`, in the namespace `phantasma::carbon`.

## What The Chain Checks And Charges

| Rule | Detail |
| ---- | ------ |
| Symbol | Uppercase letters `A` to `Z` only, at most 255 characters, not used by another token. `TokenInfoBuilder::Build` applies the same rule. |
| Metadata | `name`, `icon`, `url` and `description` are required, and `icon` is a base64 data URI of a PNG, JPEG or WebP image. `TokenMetadataBuilder::BuildAndSerialize` checks both. |
| Owner | The owner signs the creation and becomes the token owner. A new series needs the token owner's signature. A mint needs the signature of the series owner, the account given to `SeriesInfoBuilder::Build`. |
| Fungible token | `decimals` up to 64, no schemas. |
| NFT token | `decimals` is `0`, and the schemas are required. |
| Supply | `maxSupply` `0` means no limit. `TokenInfoBuilder::Build` then marks a fungible token as big-fungible, because the chain refuses an unlimited token with 64-bit balances; it does the same for a supply beyond the `int64` range. An NFT supply must fit an `int64`. |

A token creation pays two policy fees from the gas config:
`policyFeeCreateTokenBase`, and `policyFeeCreateTokenSymbol` halved once for
every letter after the first, so short symbols cost more. A series pays
`policyFeeCreateTokenSeries`. Read the current values with `GetGasConfig`. The
chain takes the base fee before it checks the symbol, so a taken symbol costs
the base fee and creates nothing. `SendTransaction` asks the chain first and
refuses a taken symbol; see
[The Pre-Flight Before A Token Creation](/developers/sdks/cpp/fees-and-broadcasting.md#the-pre-flight-before-a-token-creation).

Every builder answers `false` and fills `error` when an input is refused; with
`PHANTASMA_EXCEPTION_ENABLE` it throws instead.

## Create A Fungible Token

```cpp
using namespace phantasma::carbon;

const Bytes32 owner(keys.GetPublicKey());
std::string error;

ByteArray metadata;
if( !TokenMetadataBuilder::BuildAndSerialize({
        { "name", "Example Coin" },
        { "icon", "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mNkYAAAAAYAAjCB0C8AAAAASUVORK5CYII=" },
        { "url", "https://example.invalid" },
        { "description", "A fungible example token" },
    }, metadata, error) )
    return;

// 1,000,000 whole units with 8 decimals, so 10^14 atoms at most.
TokenInfoOwned info;
if( !TokenInfoBuilder::Build("EXCOIN", intx((int64_t)100000000000000), false, 8, owner, metadata, info, error) )
    return;

TxEnvelope env = CreateTokenTxHelper::BuildTx(info.View(), owner);
String hash;
if( !SendTransaction(api, env.msg, { &keys }, config, SendOptions{}, hash, error) )
    return;
```

`SendTransaction` checks the symbol, plans the fee against `config`, signs and
sends. `config` is `ToGasConfig(api.GetGasConfig().gasConfig)`. After the
transaction is in a block, its result holds the new token id:

```cpp
rpc::Transaction tx = api.GetTransaction(hash.c_str(), &err);
if( err.code == 0 && tx.state == "Halt" )
{
    auto carbonTokenId = CreateTokenTxHelper::ParseResult(tx.result);
}
```

`WaitForConfirmation` in `Utils/RpcUtils.h` waits for the hash; see
[The Result Of A Transaction](/developers/sdks/cpp/vm-and-transactions.md#the-result-of-a-transaction).
The owner mints the supply afterwards with `NativeTxHelper::MintFungible`; see
[Carbon](/developers/sdks/cpp/carbon.md#native-builders).

## Create An NFT Token And A Series

An NFT token carries three schemas: one for the series metadata, one for the
read-only part of each NFT (ROM) and one for its mutable part (RAM).
`TokenSchemasBuilder::PrepareStandardTokenSchemas()` returns the standard set
with the NFT fields in each NFT; [Schemas And Metadata](/developers/sdks/cpp/schemas-and-metadata.md)
explains the choices.

```cpp
using namespace phantasma::carbon;

const Bytes32 owner(keys.GetPublicKey());
std::string error;

const TokenSchemasOwned schemas = TokenSchemasBuilder::PrepareStandardTokenSchemas();
const ByteArray schemaBytes = TokenSchemasBuilder::Serialize(schemas.View());

ByteArray metadata;
if( !TokenMetadataBuilder::BuildAndSerialize({
        { "name", "Example Art" },
        { "icon", "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mNkYAAAAAYAAjCB0C8AAAAASUVORK5CYII=" },
        { "url", "https://example.invalid/art" },
        { "description", "An example NFT collection" },
    }, metadata, error) )
    return;

TokenInfoOwned info;
if( !TokenInfoBuilder::Build("EXART", intx((int64_t)0), true, 0, owner, metadata, schemaBytes, info, error) )
    return;
TxEnvelope tokenEnv = CreateTokenTxHelper::BuildTx(info.View(), owner);
// Send it, wait for it, and read carbonTokenId with CreateTokenTxHelper::ParseResult.

// A series with its own id, no mint limit and no supply limit. The key's account owns it.
const uint256 seriesId = IdHelper::GetRandomPhantasmaId();
SeriesInfoOwned series;
if( !SeriesInfoBuilder::Build(schemas.View().seriesMetadata, seriesId, 0, 0, owner, {}, series, error) )
    return;
TxEnvelope seriesEnv = CreateTokenSeriesTxHelper::BuildTx(carbonTokenId, series.View(), owner);
// Send it, wait for it, and read the Carbon series id with CreateTokenSeriesTxHelper::ParseResult.
```

A series has two ids. `seriesId` is the 256-bit id the application chooses,
here a random one, unique within the token; mints name the series by it.
The Carbon series id is the 32-bit id the chain assigns; RPC methods such as
`GetTokenNFTs` take it.

`maxMint` caps how many instances the series can ever mint; burns do not lower
that count. `maxSupply` caps how many exist at once; burns lower it. `0` means
no limit for either.

The empty metadata list suits the per-NFT standard schemas, whose series
metadata holds only the series id. A token created with
`PrepareStandardTokenSchemas(true)` keeps the NFT fields in the series, and its
series list carries them; see
[Series Metadata](/developers/sdks/cpp/schemas-and-metadata.md#series-metadata).

`TokenInfoOwned`, `SeriesInfoOwned` and `TokenSchemasOwned` own the bytes their
`View()` points into. Keep them alive until the message is signed.

## Sign Without Sending

A process that signs offline plans the message against a gas config it carries,
then signs:

```cpp
FeePlanOptions options;
options.witnessCount = 1;
options.infusionsRead = true; // nothing is burned
FeePlan plan;
if( !PlanFees(env.msg, config, options, plan) )
    return;

env.msg = plan.Apply(env.msg);
ByteArray signedTx = SignAndSerialize(env, keys);
```

`api.SendCarbonTransaction(Base16::Encode(signedTx).c_str(), &err)` sends it
later. This path does not run the symbol check, and the expiry runs from the
moment the message was built: 45 seconds unless `TxLimits::expiry` says
otherwise.

## Read The Token Back

```cpp
rpc::Token token = api.GetToken("EXART", false, &err);
// token.carbonId is the token id.

rpc::CursorPaginatedResult<rpc::TokenSeries> page = api.GetTokenSeries("EXART", 0, 10, "", &err);
for( const rpc::TokenSeries& s : page.result )
{
    // s.seriesId, s.carbonSeriesId, s.mintCount
}
```

`GetTokenSeries` returns the series page by page. Pass `page.cursor` back to
read the next page, until it is empty. `GetTokenSeriesById` returns one series
by its id or its Carbon series id.

## Related Pages

{% content-ref url="/developers/sdks/cpp/nft-minting.md" %}
[NFT Minting](/developers/sdks/cpp/nft-minting.md)
{% endcontent-ref %}

{% content-ref url="/developers/sdks/cpp/schemas-and-metadata.md" %}
[Schemas And Metadata](/developers/sdks/cpp/schemas-and-metadata.md)
{% endcontent-ref %}

{% content-ref url="/developers/sdks/cpp/fees-and-broadcasting.md" %}
[Fees And Broadcasting](/developers/sdks/cpp/fees-and-broadcasting.md)
{% endcontent-ref %}
