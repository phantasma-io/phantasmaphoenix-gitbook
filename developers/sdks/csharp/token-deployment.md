---
description: Create fungible tokens, NFT tokens and NFT series in C#.
---

# Token Deployment

A token is created by one structured transaction that calls `Token.CreateToken`. An NFT token then needs at least one series before anything can be minted, and each series is one more transaction. The builders live in the namespaces `PhantasmaPhoenix.Protocol.Carbon.Blockchain.Modules.Builders` and `PhantasmaPhoenix.Protocol.Carbon.Blockchain.TxHelpers`.

## What The Chain Checks And Charges

| Rule | Detail |
| --- | --- |
| Symbol | Uppercase letters `A` to `Z` only, at most 255 characters, not used by another token. `TokenInfoBuilder.Build` applies the same rule and throws on a bad symbol. |
| Metadata | `name`, `icon`, `url` and `description` are required. `icon` is a base64 data URI of a PNG, JPEG or WebP image. `TokenMetadataBuilder.BuildAndSerialize` checks both. |
| Owner | The owner signs the creation and becomes the token owner. A new series needs the token owner's signature. A mint needs the signature of the series owner, the account given to `SeriesInfoBuilder.Build`. |
| Fungible token | `decimals` up to 64, no schemas. |
| NFT token | `decimals` is `0`. `TokenInfoBuilder.Build` requires the schemas. |
| Supply | `maxSupply` `0` means no limit. The builder then marks a fungible token as big-fungible, because the chain refuses an unlimited token with 64-bit balances. |

A token creation pays two policy fees from the gas config: `policyFeeCreateTokenBase`, and `policyFeeCreateTokenSymbol` halved once for every letter after the first, so short symbols cost more. A series pays `policyFeeCreateTokenSeries`. Read the current values with `getGasConfig`. The chain takes the base fee before it checks the symbol, so a taken symbol costs the base fee and creates nothing. `SendTransactionAsync` asks the chain first and refuses a taken symbol; see [The Pre-Flight Before A Token Creation](/developers/sdks/csharp/fees-and-broadcasting.md#the-pre-flight-before-a-token-creation).

## Create A Fungible Token

```csharp
using PhantasmaPhoenix.Cryptography;
using PhantasmaPhoenix.Protocol.Carbon;
using PhantasmaPhoenix.Protocol.Carbon.Blockchain.Modules.Builders;
using PhantasmaPhoenix.Protocol.Carbon.Blockchain.TxHelpers;
using PhantasmaPhoenix.RPC;

using var api = new PhantasmaAPI("https://testnet.phantasma.info/rpc");
var keys = PhantasmaKeys.FromWIF(Environment.GetEnvironmentVariable("WIF")!);
var owner = new Bytes32(keys.PublicKey);

var metadata = TokenMetadataBuilder.BuildAndSerialize(new Dictionary<string, string>
{
	["name"] = "Example Coin",
	["icon"] = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mNkYAAAAAYAAjCB0C8AAAAASUVORK5CYII=",
	["url"] = "https://example.invalid",
	["description"] = "A fungible example token",
});

// 1,000,000 whole units with 8 decimals, so 10^14 atoms at most.
var info = TokenInfoBuilder.Build("EXCOIN", new IntX(100_000_000_000_000L), isNFT: false, decimals: 8, owner, metadata);

var hash = await api.SendTransactionAsync(CreateTokenTxHelper.BuildTx(info, owner), keys);
```

`SendTransactionAsync` plans the fee from the message, runs the symbol check, signs and sends. After the transaction is in a block, its result holds the new token id:

```csharp
using PhantasmaPhoenix.Protocol.Carbon.Blockchain.TxHelpers;
using PhantasmaPhoenix.RPC;

using var api = new PhantasmaAPI("https://testnet.phantasma.info/rpc");
var hash = Environment.GetEnvironmentVariable("TX_HASH")!;

var tx = await api.GetTransactionAsync(hash);
var tokenId = CreateTokenTxHelper.ParseResult(tx!.Result!);
```

The [Check Transaction State](/developers/sdks/csharp/examples/check-transaction-state.md) example waits for a hash until it reaches a final state. The owner mints the supply afterwards with `NativeTxHelper.MintFungible`; see [Structured Transactions](/developers/sdks/csharp/carbon.md).

## Create An NFT Token And A Series

An NFT token carries three schemas: one for the series metadata, one for the read-only part of each NFT (ROM) and one for its mutable part (RAM). `TokenSchemasBuilder.PrepareStandardTokenSchemas()` returns the standard set; [Schemas And Metadata](/developers/sdks/csharp/schemas-and-metadata.md) explains the choices.

```csharp
using PhantasmaPhoenix.Cryptography;
using PhantasmaPhoenix.Protocol.Carbon;
using PhantasmaPhoenix.Protocol.Carbon.Blockchain.Modules.Builders;
using PhantasmaPhoenix.Protocol.Carbon.Blockchain.TxHelpers;
using PhantasmaPhoenix.RPC;

using var api = new PhantasmaAPI("https://testnet.phantasma.info/rpc");
var keys = PhantasmaKeys.FromWIF(Environment.GetEnvironmentVariable("WIF")!);
var owner = new Bytes32(keys.PublicKey);

var schemas = TokenSchemasBuilder.PrepareStandardTokenSchemas();
var metadata = TokenMetadataBuilder.BuildAndSerialize(new Dictionary<string, string>
{
	["name"] = "Example Art",
	["icon"] = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mNkYAAAAAYAAjCB0C8AAAAASUVORK5CYII=",
	["url"] = "https://example.invalid/art",
	["description"] = "An example NFT collection",
});

var info = TokenInfoBuilder.Build("EXART", new IntX(0L), isNFT: true, decimals: 0, owner, metadata, TokenSchemasBuilder.Serialize(schemas));
var tokenHash = await api.SendTransactionAsync(CreateTokenTxHelper.BuildTx(info, owner), keys);

// After the token transaction is in a block:
var tokenId = CreateTokenTxHelper.ParseResult((await api.GetTransactionAsync(tokenHash))!.Result!);

// A series with its own 256-bit id, no mint limit and no supply limit.
var seriesId = IdHelper.GetRandomPhantasmaId();
var series = SeriesInfoBuilder.Build(seriesId, maxMint: 0, maxSupply: 0, owner);
var seriesHash = await api.SendTransactionAsync(CreateTokenSeriesTxHelper.BuildTx(tokenId, series, owner), keys);

// After the series transaction is in a block:
var carbonSeriesId = CreateTokenSeriesTxHelper.ParseResult((await api.GetTransactionAsync(seriesHash))!.Result!);
```

A series has two ids. `seriesId` is the 256-bit id the application chooses, here a random one; mints name the series by it. `carbonSeriesId` is the 32-bit id the chain assigns; RPC methods such as `GetTokenNFTsAsync` take it.

`maxMint` caps how many instances the series can ever mint; burns do not lower that count. `maxSupply` caps how many exist at once; burns lower it. `0` means no limit for either.

`SeriesInfoBuilder.Build` writes series metadata for the standard schemas, which keep the NFT fields in each NFT. A token created with shared series metadata needs the series metadata built from its own schema: `TokenSeriesMetadataBuilder.BuildAndSerialize(schemas.seriesMetadata, seriesId, fields)`, passed as the last argument of `SeriesInfoBuilder.Build`.

## Sign Without Sending

Each helper also builds, plans and signs in one call against a gas config the caller provides, for a process that signs offline:

```csharp
var config = (await api.GetGasConfigAsync())!.ToGasConfig();
var signedHex = CreateTokenTxHelper.BuildTxAndSignHex(info, keys, config);
```

`api`, `keys` and `info` are the ones of the examples above. `CreateTokenSeriesTxHelper` and `MintPhantasmaNonFungibleTxHelper` have the same `BuildTxAndSign` and `BuildTxAndSignHex` methods.

`api.SendCarbonTransactionAsync(signedHex)` sends it later. This path does not run the symbol check, and the expiry runs from the moment of signing.

## Read The Token Back

```csharp
using PhantasmaPhoenix.RPC;

using var api = new PhantasmaAPI("https://testnet.phantasma.info/rpc");

var token = await api.GetTokenAsync("EXART");
var series = await api.GetTokenSeriesAsync("EXART", pageSize: 10);

Console.WriteLine($"{token!.Symbol}: token id {token.CarbonId}");
foreach (var s in series!.Result!)
{
	Console.WriteLine($"series {s.SeriesId}, chain id {s.carbonSeriesId}");
}
```

## Related Pages

{% content-ref url="/developers/sdks/csharp/nft-minting.md" %}
NFT Minting
{% endcontent-ref %}

{% content-ref url="/developers/sdks/csharp/schemas-and-metadata.md" %}
Schemas And Metadata
{% endcontent-ref %}

{% content-ref url="/developers/sdks/csharp/fees-and-broadcasting.md" %}
Fees And Broadcasting
{% endcontent-ref %}
