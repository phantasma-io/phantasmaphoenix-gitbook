---
title: "C++ SDK NFT Minting"
linkTitle: "NFT Minting"
weight: 70
---

An NFT is minted into a series of an NFT token. The token and the series come
first; see [Token Deployment](token-deployment.md). One
`Token.MintPhantasmaNonFungible` call mints one or more instances for one
recipient, and the chain derives the id of each NFT. The builders live in
`Carbon/Contracts/Token.h` and `Carbon/Tx.h`, in the namespace
`phantasma::carbon`.

## Required Inputs

| Input | Where it comes from |
| ----- | ------------------- |
| The token id | `CreateTokenTxHelper::ParseResult` after the token creation, or `carbonId` of `GetToken`. |
| The series id | The 256-bit id the series was created with. Not the Carbon series id. |
| The ROM schema | The one the token was created with. |
| The series owner's key | It signs the mint and pays the gas. |
| The recipient | A `Bytes32`, for example `FromPhantasmaAddress(address)`. |

## Build The ROM

The ROM is the read-only data of an NFT.
`PhantasmaNftRomBuilder::BuildAndSerialize(romSchema, fields, out, error)`
writes one value for every field of the token's ROM schema and checks each
value against the field's type. The chain derives the NFT id itself, so the
builder leaves out `_i` and `rom` and refuses those names. With the standard
schemas, the ROM carries the five standard fields:

| Field | Type | Meaning |
| ----- | ---- | ------- |
| `name` | string | The name of the NFT. |
| `description` | string | Its description. |
| `imageURL` | string | The URL of the image. |
| `infoURL` | string | A page about the NFT. |
| `royalties` | 32-bit integer | The royalty a sale on the chain market pays to the account the NFT was minted to, in units of 10,000,000 per 1%. |

```cpp
using namespace phantasma::carbon;

const TokenSchemasOwned schemas = TokenSchemasBuilder::PrepareStandardTokenSchemas();
ByteArray rom;
std::string error;
if( !PhantasmaNftRomBuilder::BuildAndSerialize(schemas.View().rom, {
        MetadataField{ "name", MetadataValue::FromString("Example NFT #1") },
        MetadataField{ "description", MetadataValue::FromString("The first example NFT") },
        MetadataField{ "imageURL", MetadataValue::FromString("https://example.invalid/nft/1.png") },
        MetadataField{ "infoURL", MetadataValue::FromString("https://example.invalid/nft/1") },
        MetadataField{ "royalties", MetadataValue::FromInt64(50000000) }, // 5%
    }, rom, error) )
    return;
```

For the standard fields only, the overload
`BuildAndSerialize(name, description, imageURL, infoURL, royalties, schemas, out, error)`
takes them as arguments; a null `schemas` means the per-NFT standard set.

In a series with `mode` `0`, the chain derives the NFT id from the ROM, so two
NFTs of one token with the same ROM cannot both exist: the second mint fails
with `token ID already in use`. Give every NFT something of its own, such as its
name or number. In a series whose NFTs share one ROM (`mode` `1`), the id also
covers the mint number.

## Mint

```cpp
using namespace phantasma::carbon;

// The id the series was created with, for example from IdHelper::GetRandomPhantasmaId().
const intx seriesIdX(seriesId);

std::vector<PhantasmaNftMintInfo> tokens;
tokens.push_back(PhantasmaNftMintInfo{ (const intx_pod&)seriesIdX, ByteView{ rom.data(), rom.size() }, ByteView{} });

TxEnvelope env;
std::string error;
if( !MintPhantasmaNonFungibleTxHelper::BuildTx(carbonTokenId, senderPublicKey, receiverPublicKey, tokens, env, error) )
    return; // an empty list

String hash;
if( !SendTransaction(api, env.msg, { &keys }, config, SendOptions{}, hash, error) )
    return;
```

`senderPublicKey` is the series owner's key; it pays the gas and signs. Each
entry of `tokens` is one instance, and entries may name different series of the
same token; every instance goes to the one recipient. The third member of an
entry is the RAM, empty with the standard schemas. `rom` must outlive the
message, which points at it.

The mint fee depends on three facts the message does not carry: whether the
recipient already holds the token, whether the supply row still exists, and
whether the series mints duplicates. `SendTransaction` plans each at the reading
that costs more, so the offer can exceed the bill; the rest returns. See
[Stating A Fact](fees-and-broadcasting.md#stating-a-fact).

## Parse The Result

After the transaction is in a block, its result names every minted instance:

```cpp
using namespace phantasma::carbon;

rpc::Transaction minted = api.GetTransaction(hash.c_str(), &err);
if( err.code != 0 || minted.state != "Halt" )
    return;

for( const PhantasmaNftMintResult& m : MintPhantasmaNonFungibleTxHelper::ParseResult(minted.result) )
{
    // The NFT id is stored little-endian; RPC methods take it as a decimal number.
    const std::string nftId = uint256::FromBytes(ByteView{ m.phantasmaNftId.bytes, Bytes32::length }).ToString();
    const uint32_t carbonSeriesId = (uint32_t)(m.carbonInstanceId & 0xFFFFFFFFu);
    const uint32_t mintNumber = (uint32_t)(m.carbonInstanceId >> 32);
}
```

`phantasmaNftId` is the 256-bit id the chain derived for the NFT; `GetNFT` and
the script interops such as `Runtime.TransferToken` name the NFT by it.
`carbonInstanceId` is the id that structured transfers and burns take, for
example `NativeTxHelper::TransferNonFungible`.

## Read NFTs Back

| Call | Returns |
| ---- | ------- |
| `GetTokenNFTs(tokenId, carbonSeriesId, pageSize, cursor, extended, &err)` | The NFTs of a token, or of one series when `carbonSeriesId` is not `0`, page by page. |
| `GetAccountNFTs(account, symbol, tokenId, carbonSeriesId, pageSize, cursor, extended, checkAddressReservedByte, &err)` | The NFTs an account holds. |
| `GetNFT(symbol, nftId, extended, &err)` | One NFT by its id in decimal text. |
| `GetNFTs(symbol, nftIds, extended, &err)` | Several NFTs by id. |

The paged calls return a `CursorPaginatedResult`: pass its `cursor` back to read
the next page, until it is empty. With `extended` set, a page holds at most 50
entries, otherwise 100.

`MintNonFungibleTxHelper` builds a direct `MintNonFungible`, which takes an NFT
id chosen by the caller. The chain refuses it while its configuration disables
such ids, as it does on mainnet.

## Related Pages

- [Token Deployment](token-deployment.md)
- [Schemas And Metadata](schemas-and-metadata.md)
- [Carbon](carbon.md)
