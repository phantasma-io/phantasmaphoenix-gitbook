---
title: "Structured Transactions"
weight: 60
description: "Build structured transactions in C#: transfers, mints, burns and token module calls."
---

A structured transaction carries a typed message, a `TxMsg`, that the chain executes without a VM script. Transfers, mints and burns of tokens and NFTs, and calls into the token module such as a token creation, use it. The types live in `PhantasmaPhoenix.Protocol.Carbon` and its namespaces `PhantasmaPhoenix.Protocol.Carbon.Blockchain` and `PhantasmaPhoenix.Protocol.Carbon.Blockchain.TxHelpers`.

A message goes through four steps: build, plan the fee, sign, send. `PhantasmaAPI.SendTransactionAsync` runs the last three. Planning, signing and sending are described on [Fees And Broadcasting](fees-and-broadcasting.md).

## The Message

| `TxMsg` field | Meaning |
| --- | --- |
| `type` | The message type, a `TxTypes` value. |
| `expiry` | The last moment the chain accepts the message, in milliseconds since 1970. |
| `maxGas` | The gas offer in KCAL atoms. A builder leaves it at `0`; planning sets it. |
| `maxData` | The storage escrow ceiling in SOUL atoms. A builder leaves it at `0`; planning sets it. |
| `gasFrom` | The 32-byte public key of the account that pays the gas. |
| `payload` | A short text the transaction carries. |
| `msg` | The body of the type, for example `TxMsgTransferFungible`. |

Accounts are 32-byte public keys, `Bytes32`: `new Bytes32(keys.PublicKey)` for a key pair, `new Bytes32(address.GetPublicKey())` for a parsed address.

## Builders

`NativeTxHelper` builds the native types:

| Builder | Parameters | Message types |
| --- | --- | --- |
| `TransferFungible` | `From`, `To`, `TokenId`, `Amount` (u64 atoms), optional `GasPayer` | `TransferFungible`, `TransferFungible_GasPayer` |
| `TransferNonFungible` | `From`, `To`, `TokenId`, `InstanceIds`, optional `GasPayer` | `TransferNonFungible_Single` for one instance, `TransferNonFungible_Multi` for several, and their `_GasPayer` forms |
| `MintFungible` | `Owner`, `To`, `TokenId`, `Amount` (`IntX`) | `MintFungible` |
| `BurnFungible` | `From`, `TokenId`, `Amount` (`IntX`), optional `GasPayer` | `BurnFungible`, `BurnFungible_GasPayer` |
| `BurnNonFungible` | `From`, `TokenId`, `InstanceId`, optional `GasPayer` | `BurnNonFungible`, `BurnNonFungible_GasPayer` |

The account named in `From` or `Owner` signs. With `GasPayer` set, a second account pays the gas and signs as well; see [Who Pays The Gas](fees-and-broadcasting.md#who-pays-the-gas).

A transfer amount is a u64, also for a big-fungible token, whose balances can exceed that range. A larger amount moves with a script transfer, whose amount is a big integer. Mints and burns carry an `IntX`; `new IntX(long)` wraps an ordinary amount. Only the token owner can mint.

Every builder parameter class also takes the limits of `TxLimits`: `MaxGas`, `MaxData` and `Expiry`. Without `Expiry` the builder stamps `TxLimits.DefaultExpiryMs` (45 seconds) from now. See [Expiry](fees-and-broadcasting.md#expiry) for a longer lifetime.

Token module calls have their own builders, each with a `ParseResult` for the transaction result:

| Builder | Call | Page |
| --- | --- | --- |
| `CreateTokenTxHelper.BuildTx` | `Token.CreateToken` | [Token Deployment](token-deployment.md) |
| `CreateTokenSeriesTxHelper.BuildTx` | `Token.CreateTokenSeries` | [Token Deployment](token-deployment.md) |
| `MintPhantasmaNonFungibleTxHelper.BuildTx` | `Token.MintPhantasmaNonFungible` | [NFT Minting](nft-minting.md) |

## Example: Send An NFT, Burn Tokens

```csharp
using PhantasmaPhoenix.Cryptography;
using PhantasmaPhoenix.Protocol.Carbon;
using PhantasmaPhoenix.Protocol.Carbon.Blockchain.TxHelpers;
using PhantasmaPhoenix.RPC;

using var api = new PhantasmaAPI("https://testnet.phantasma.info/rpc");
var owner = PhantasmaKeys.FromWIF(Environment.GetEnvironmentVariable("OWNER_WIF")!);
var payer = PhantasmaKeys.FromWIF(Environment.GetEnvironmentVariable("PAYER_WIF")!);
var receiver = Address.Parse(Environment.GetEnvironmentVariable("TO")!);

// Two NFT instances of token 77 move to the receiver. The payer pays the gas.
var send = NativeTxHelper.TransferNonFungible(new TransferNonFungibleParams
{
	From = new Bytes32(owner.PublicKey),
	GasPayer = new Bytes32(payer.PublicKey),
	To = new Bytes32(receiver.GetPublicKey()),
	TokenId = 77,
	InstanceIds = new ulong[] { 1001, 1002 },
});
var sendHash = await api.SendTransactionAsync(send, new IKeyPair[] { owner, payer });

// The owner burns 5 whole units of a token with 8 decimals and pays the gas itself.
var burn = NativeTxHelper.BurnFungible(new BurnFungibleParams
{
	From = new Bytes32(owner.PublicKey),
	TokenId = 2,
	Amount = new IntX(5 * 100_000_000L),
});
var burnHash = await api.SendTransactionAsync(burn, owner);
```

`SendTransactionAsync` plans each message from the chain's current prices, signs it with the given keys and sends it. It returns the transaction hash. Token `2` is SOUL; the token ids and the instance ids come from `GetTokenAsync` and `GetAccountNFTsAsync`.

## Serialization

`CarbonBlob.Serialize(msg)` returns the bytes of a message, and `CarbonBlob.New<TxMsg>(bytes)` reads them back. A signed message is a `SignedTxMsg`: the message and one `Witness` per signer, each a 32-byte address and a 64-byte Ed25519 signature. `TxMsgSigner.Sign(msg, keys)` returns its bytes, and `PhantasmaAPI.SendCarbonTransactionAsync` sends them as hex. The wire types are listed on [Carbon and NFT Types](reference/carbon-and-nft-types.md).

## Related Pages

- [Fees And Broadcasting](fees-and-broadcasting.md)
- [Token Deployment](token-deployment.md)
- [Carbon and NFT Types](reference/carbon-and-nft-types.md)
