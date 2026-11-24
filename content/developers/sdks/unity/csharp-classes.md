---
title: "Keys, Scripts, Tokens And NFTs"
weight: 50
description: "Keys, scripts, tokens and NFTs in Unity with the C# SDK classes and the Unity API."
---

`PhantasmaPhoenix.Unity.Core` ships the assemblies of the C# SDK in its `Runtime/Plugins` folder. Their classes work in Unity as they do in .NET, so the C# guides apply: keys, script builders, message builders, schemas and metadata. Only the network calls differ. Unity calls the node through the coroutines of its own `PhantasmaAPI`, in the namespace `PhantasmaPhoenix.Unity.Core`.

| Assembly in `PhantasmaPhoenix.Unity.Core` 0.13.2 | Version | Contents |
| --- | --- | --- |
| `PhantasmaPhoenix.Core` | 0.2.7 | `Timestamp` and shared helpers |
| `PhantasmaPhoenix.Cryptography` | 0.3.1 | Keys, addresses, signatures, hashes, seed phrases |
| `PhantasmaPhoenix.Protocol` | 0.6.1 | Script transactions, enums, the Phantasma Link v5 wallet classes |
| `PhantasmaPhoenix.Protocol.Carbon` | 0.6.0 | Structured transactions, token and NFT builders, the fee planner |
| `PhantasmaPhoenix.VM` | 0.1.7 | `ScriptBuilder` and `VMObject` |
| `PhantasmaPhoenix.RPC` | 0.16.1 | The result models the Unity API returns |

`PhantasmaPhoenix.Link`, with the WebSocket server and the relay socket of a wallet, is not included.

## Where Each C# Guide Applies

| Task | C# guide | In Unity |
| --- | --- | --- |
| Create and import keys, parse addresses, sign messages | [Keys And Addresses](../csharp/keys-and-addresses.md) | The same classes; no network call. |
| Build a script, send it, run a read-only script | [Script Transactions](../csharp/vm-and-transactions.md) | `SignAndSendTransaction` sends the script; `InvokeRawScript` runs a read-only one. |
| Build transfers, mints and burns | [Structured Transactions](../csharp/carbon.md) | `SignAndSendCarbonTransaction`; see [Carbon Transactions And Fees](carbon-transactions.md). |
| Create a token and a series | [Token Deployment](../csharp/token-deployment.md) | The same builders; `SignAndSendCarbonTransaction` sends them. |
| Mint NFTs | [NFT Minting](../csharp/nft-minting.md) | The same builders; `SignAndSendCarbonTransaction` sends the mint. |
| Choose schemas, build metadata | [Schemas And Metadata](../csharp/schemas-and-metadata.md) | The same classes; no network call. |

## The Unity Calls

Each call is a coroutine. It reports through a success callback and an optional error callback, which receives an `EPHANTASMA_SDK_ERROR_TYPE` (`API_ERROR`, `WEB_REQUEST_ERROR`, `FAILED_PARSING_JSON`, `MALFORMED_RESPONSE`) and a message.

| Coroutine | Does |
| --- | --- |
| `SignAndSendTransaction(keys, nexus, script, chain, payload, callback, errorHandlingCallback, ..., expiration)` | Signs a script transaction and sends it. Without `expiration` it expires `TxLimits.DefaultExpiryMs` (45 seconds) after signing. The callback receives the hash and the encoded transaction. |
| `SignAndSendCarbonTransaction(keys, message, callback, errorHandlingCallback)` | Plans a message whose `maxGas` is `0` from the chain's gas config, checks the symbol of a token creation, signs and sends. |
| `SignAndSendCarbonTransaction(keys[], message, options, callback, errorHandlingCallback, preflight)` | The same with one key per witness, for example a separate gas payer, and with `PlanAndSignOptions`. `preflight: false` skips the symbol check. |
| `InvokeRawScript(chain, scriptHex, callback, errorHandlingCallback)` | Runs a read-only script and returns a `ScriptResult`. |
| `GetTransaction(hash, callback, errorHandlingCallback)` | Returns the transaction with its `State` and `Result` once it is in a block. |

## Example: Mint An NFT

The message is built with the C# builders, exactly as in [NFT Minting](../csharp/nft-minting.md), and sent with the coroutine:

```csharp
using System.Numerics;
using PhantasmaPhoenix.Cryptography;
using PhantasmaPhoenix.Protocol.Carbon;
using PhantasmaPhoenix.Protocol.Carbon.Blockchain.Modules;
using PhantasmaPhoenix.Protocol.Carbon.Blockchain.Modules.Builders;
using PhantasmaPhoenix.Protocol.Carbon.Blockchain.TxHelpers;
using PhantasmaPhoenix.Unity.Core;
using UnityEngine;

public class MintExample : MonoBehaviour
{
	private readonly PhantasmaAPI _api = new PhantasmaAPI("https://testnet.phantasma.info/rpc");

	/// <summary>Mints one NFT of a token with the standard schemas into a series, for the key's own account.</summary>
	public void Mint(PhantasmaKeys keys, ulong tokenId, BigInteger seriesId)
	{
		var owner = new Bytes32(keys.PublicKey);
		var rom = PhantasmaNftRomBuilder.BuildAndSerialize(TokenSchemasBuilder.PrepareStandardTokenSchemas().rom, new[]
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
			Sender = owner,
			To = owner,
			Tokens = new[] { new PhantasmaNftMintInfo { phantasmaSeriesId = new IntX(seriesId), rom = rom, ram = System.Array.Empty<byte>() } },
		});

		StartCoroutine(_api.SignAndSendCarbonTransaction(keys, mint,
			(hash, encoded) => Debug.Log($"Mint sent: {hash}"),
			(type, message) => Debug.LogError($"[{type}] {message}")));
	}
}
```

After the transaction is in a block, `GetTransaction` returns it, and `MintPhantasmaNonFungibleTxHelper.ParseResult(result.Result)` names the minted instances. The [Check Transaction State](examples/check-transaction-state.md) example waits for a hash until it reaches a final state.

## Related Pages

- [Carbon Transactions And Fees](carbon-transactions.md)
- [Phantasma API](features-and-functionality/phantasmaapi.md)
- [Token Deployment](../csharp/token-deployment.md)
