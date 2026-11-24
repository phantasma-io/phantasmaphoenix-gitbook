---
title: "NFT Minting"
weight: 80
description: "Mint NFTs into a series and read them back in C#."
---

An NFT is minted into a series of an NFT token. The token and the series come first; see [Token Deployment](token-deployment.md). One `Token.MintPhantasmaNonFungible` call mints one or more instances for one recipient. The builders live in the namespaces `PhantasmaPhoenix.Protocol.Carbon.Blockchain.Modules.Builders` and `PhantasmaPhoenix.Protocol.Carbon.Blockchain.TxHelpers`.

## Build The ROM

The ROM is the read-only data of an NFT. `PhantasmaNftRomBuilder.BuildAndSerialize(romSchema, fields)` writes one value for every field of the token's ROM schema, in the schema's order, and checks each value against the field's type. A missing field, or a field name in the wrong case, throws. The chain adds the NFT id `_i` and the `rom` bytes itself, so those two names are refused.

With the standard schemas, the ROM carries the five standard fields:

| Field | Type | Meaning |
| --- | --- | --- |
| `name` | string | The name of the NFT. |
| `description` | string | Its description. |
| `imageURL` | string | The URL of the image. |
| `infoURL` | string | A page about the NFT. |
| `royalties` | 32-bit integer | The royalty taken on a sale on the chain market, in units of 10,000,000 per 1%. |

A token with custom schemas has its own fields; [Schemas And Metadata](schemas-and-metadata.md) describes them.

## Mint

```csharp
using System.Numerics;
using PhantasmaPhoenix.Cryptography;
using PhantasmaPhoenix.Protocol.Carbon;
using PhantasmaPhoenix.Protocol.Carbon.Blockchain.Modules;
using PhantasmaPhoenix.Protocol.Carbon.Blockchain.Modules.Builders;
using PhantasmaPhoenix.Protocol.Carbon.Blockchain.TxHelpers;
using PhantasmaPhoenix.RPC;

using var api = new PhantasmaAPI("https://testnet.phantasma.info/rpc");
var keys = PhantasmaKeys.FromWIF(Environment.GetEnvironmentVariable("WIF")!);
var owner = new Bytes32(keys.PublicKey);

ulong tokenId = ulong.Parse(Environment.GetEnvironmentVariable("TOKEN_ID")!);      // from CreateTokenTxHelper.ParseResult
var seriesId = BigInteger.Parse(Environment.GetEnvironmentVariable("SERIES_ID")!); // the id the series was created with

// The ROM schema the token was created with.
var romSchema = TokenSchemasBuilder.PrepareStandardTokenSchemas().rom;
var rom = PhantasmaNftRomBuilder.BuildAndSerialize(romSchema, new[]
{
	new MetadataField("name", "Example NFT #1"),
	new MetadataField("description", "The first example NFT"),
	new MetadataField("imageURL", "https://example.invalid/nft/1.png"),
	new MetadataField("infoURL", "https://example.invalid/nft/1"),
	new MetadataField("royalties", 50_000_000), // 5%
});

var mint = MintPhantasmaNonFungibleTxHelper.BuildTx(new PhantasmaNftMintParams
{
	TokenId = tokenId,
	Sender = owner, // pays the gas and signs; the series owner
	To = owner,     // receives every instance of this call
	Tokens = new[]
	{
		new PhantasmaNftMintInfo { phantasmaSeriesId = new IntX(seriesId), rom = rom, ram = Array.Empty<byte>() },
	},
});

var hash = await api.SendTransactionAsync(mint, keys);
```

Each entry of `Tokens` is one instance. Entries of several series of the same token can share one call. `ram` is the mutable part; it stays empty with the standard schemas.

The mint fee depends on three facts the message does not carry: whether the recipient already holds the token, whether the supply row exists, and whether the series mints duplicates. The planner takes the more expensive reading of each, so the plan can offer more gas than the bill; the rest returns. See [Stating A Fact](fees-and-broadcasting.md#stating-a-fact).

## Parse The Result

After the transaction is in a block, its result names every minted instance:

```csharp
using PhantasmaPhoenix.Protocol;
using PhantasmaPhoenix.Protocol.Carbon.Blockchain.TxHelpers;
using PhantasmaPhoenix.RPC;

using var api = new PhantasmaAPI("https://testnet.phantasma.info/rpc");
var tx = await api.GetTransactionAsync(Environment.GetEnvironmentVariable("TX_HASH")!);

if (tx?.State == ExecutionState.Halt)
{
	foreach (var minted in MintPhantasmaNonFungibleTxHelper.ParseResult(tx.Result!))
	{
		Console.WriteLine($"NFT id {minted.phantasmaNftId.ToHex()}, instance id {minted.carbonInstanceId}");
	}
}
```

`phantasmaNftId` is the 256-bit id the chain derived for the NFT, here printed in hex. `carbonInstanceId` is the instance id that transfers and burns name, for example `TransferNonFungibleParams.InstanceIds`.

## Read NFTs Back

| Call | Returns |
| --- | --- |
| `GetTokenNFTsAsync(carbonTokenId, carbonSeriesId, pageSize, cursor, extended)` | The NFTs of a token, or of one series, page by page. |
| `GetAccountNFTsAsync(account, tokenSymbol, carbonTokenId, carbonSeriesId, pageSize, cursor, extended)` | The NFTs an account holds. |
| `GetNFTAsync(symbol, tokenId, loadProperties)` | One NFT by its 256-bit id in decimal text. |
| `GetNFTsAsync(symbol, tokenIds, extended)` | Several NFTs by id. |

The paged calls return a `CursorPaginatedResult`: pass its `Cursor` back to read the next page, until it is `null` or empty. With `extended` set, a page holds at most 50 entries, otherwise 100.

## Related Pages

- [Token Deployment](token-deployment.md)
- [Schemas And Metadata](schemas-and-metadata.md)
- [Structured Transactions](carbon.md)
