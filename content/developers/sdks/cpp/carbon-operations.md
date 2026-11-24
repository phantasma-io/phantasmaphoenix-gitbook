---
title: "C++ SDK Carbon Operations"
linkTitle: "Carbon Operations"
weight: 100
---

The builders on [Carbon](carbon.md) cover transfers,
mints, burns, token and series creation, and NFT mints. Every other module
method is called with a `Call` message: a module id, a method id and the
serialized arguments.

## Builders Or A Call

| Need | Use |
| ---- | --- |
| A transfer, mint or burn | `NativeTxHelper`; see [Carbon](carbon.md#native-builders). |
| A token, a series, an NFT mint | The token module builders; see [Carbon](carbon.md#token-module-builders). |
| Any other module method | A `Blockchain::TxMsgCall` with arguments written by hand. |
| Several calls in one transaction | A `Blockchain::TxMsgCall_Multi`. |
| Tokens moving between several accounts at once | A `Blockchain::TxMsgTrade`. |

## A Module Call

The arguments are written with the `Write...` functions of `Carbon/Carbon.h`
in the order the method reads them. This call deletes a series that holds no
NFT:

```cpp
using namespace phantasma::carbon;

// Token.DeleteTokenSeries reads the token id, then the Carbon series id.
ByteArray args;
WriteView w(args);
Write8u(carbonTokenId, w);
Write4u(carbonSeriesId, w);

Blockchain::TxMsg msg{};
msg.type = Blockchain::TxTypes::Call;
msg.expiry = DefaultExpiry();
msg.gasFrom = owner;
msg.call = Blockchain::TxMsgCall{ (uint32_t)ModuleId::Token, (uint32_t)TokenContract_Methods::DeleteTokenSeries, ByteView{ args.data(), args.size() }, {} };

// The message points into args, which has to outlive it.
String hash;
std::string error;
if( !SendTransaction(api, msg, { &keys }, config, SendOptions{}, hash, error) )
    return;
```

A `Call` takes its witnesses from the keys it is signed with, in that order,
and the gas payer must be one of them. Each witness adds 96 bytes the chain
bills; `SendTransaction` plans the call for the number of keys it is given.

## Token Module Methods

`ModuleId::Token` (1). The method ids are the `TokenContract_Methods` values.

| Method | Arguments, in order | Signed by |
| ------ | ------------------- | --------- |
| `TransferFungible` | to (`Bytes32`), from (`Bytes32`), token id (`uint64_t`), amount (`intx`) | from. |
| `TransferNonFungible` | to, from, token id, a count (`int32_t`) and that many instance ids (`uint64_t`) | from. |
| `CreateToken` | `TokenInfo` | The owner; see [Token Deployment](token-deployment.md). |
| `MintFungible` | token id, to, amount (`intx`) | The token owner. |
| `BurnFungible` | token id, from, amount (`intx`) | from. |
| `CreateTokenSeries` | token id, `SeriesInfo` | The token owner. |
| `MintPhantasmaNonFungible` | token id, to, a count and that many `PhantasmaNftMintInfo` | The series owner; see [NFT Minting](nft-minting.md). |
| `BurnNonFungible` | token id, from, a count and that many instance ids | from, who owns the instances. |
| `UpdateTokenMetadata` | token id, a `VmDynamicStruct` of fields | The token owner. The fields replace the fields of the same name or are added; the chain checks the result. |
| `UpdateSeriesMetadata` | token id, Carbon series id (`uint32_t`), metadata as a byte array | The series owner. The bytes replace the series metadata; build them with `TokenSeriesMetadataBuilder`. |
| `DeleteTokenSeries` | token id, Carbon series id | The token owner or the series owner, once no NFT of the series exists. |
| `ApplyInflation` | token id | Anyone. It mints the token's scheduled inflation when a period is due. |
| `MintNonFungible`, `CreateMintedTokenSeries` | | Refused: both take an NFT id chosen by the caller, which the token configuration disables. |
| `SetTokensConfig` | `TokensConfig` | Governance only. |

The `Get...` method ids read state; the RPC methods on
[RPC](rpc.md) return the same data without a transaction.

## Market Module Methods

Module id 4; `ModuleId` has no name for it. A listing sells one NFT for a
fungible token at a fixed price.

| Method id | Method | Arguments, in order | Rules |
| --------- | ------ | ------------------- | ----- |
| 0 | `SellToken` | from (`Bytes32`), token id, instance id, quote token id (`uint64_t`), price (`intx`), end date (`int64_t`, milliseconds) | Signed by the NFT owner. The NFT moves to the market until it is bought or the listing is cancelled. The quote token must be fungible, the end date in the future, the price not negative and, with the `PriceRequired` rule, above zero. |
| 4 | `BuyToken` | from, token id, instance id | Signed by the buyer, who pays the price in the quote token. Without the `CanPurchaseLate` rule, only before the end date. |
| 2 | `CancelSale` | token id, instance id | Without the `CanCancelEarly` rule, only after the end date. Signed by the seller, or by anyone once the delisting grace after the end date has passed. The NFT returns to the seller. |

Methods 1, 3 and 5 are the same three by token symbol and Phantasma NFT id; 6,
7 and 8 read listings.

With the `EnforceRoyalties` rule, a sale pays up to three royalties out of the
price, at 10,000,000 per 1%:

1. The `royalties` value of the token metadata, to the token owner.
2. The `royalties` value of the series metadata, to the series owner.
3. The `royalties` value of the NFT's ROM, to the account the NFT was minted to.

Each is a share of what remains of the price after the ones before it. The
seller receives the rest. The chain's defaults turn on `PriceRequired` and
`EnforceRoyalties` and set a delisting grace of one day. `TokenListing` in `Carbon/Contracts/Market.h` is the
listing a read returns.

## Governance Module Methods

`ModuleId::Governance` (0). `GovernanceContract_Methods::RegisterName` takes
the address (`Bytes32`) and the name (`SmallString`) and is signed by that
address. One name per address, at most `maxNameLength` characters, lowercase
ASCII letters, digits and `_`. The fee is `policyFeeRegisterName` halved for
every character after the first, so short names cost more. A registered name
cannot be removed. The other governance methods are for governance only.

## Several Calls In One Transaction

A `TxMsgCall_Multi` holds `numCalls` calls and runs them in order, in one
transaction: they all complete or none does. A call can take part of its
arguments from the result of an earlier call. Its `sections` then hold
`numArgSections_negative`, the negated number of sections. Each section holds
either bytes or a negative `registerOffset`, where `-1` means the result of the
call before. The sections are joined into the arguments.

## Trades

A `TxMsgTrade` moves tokens of several accounts in one transaction: fungible
mints, NFT mints, fungible transfers, NFT transfers, fungible burns and NFT
burns, run in that order. Each entry names its own `from`, and every such
account signs. Two accounts can swap tokens this way without trusting each
other. NFT mints in a trade take an NFT id chosen by the caller and are refused.

## Read A Message Back

```cpp
using namespace phantasma::carbon;

Allocator storage;
Blockchain::SignedTxMsg signedMsg;
ByteView signedPortion;
const ByteView bytes{ signedTx.data(), signedTx.size() };
if( !Blockchain::ParseSignedTx(signedMsg, signedPortion, bytes, storage) )
    return; // cut short, an unknown type, or a field that does not fit

uint64_t offer = signedMsg.msg.maxGas;
```

`ParseTx(msg, bytes, storage)` reads an unsigned message. Both read the bytes
the way the chain reads them and refuse a message that is cut short. The
`Allocator` and the bytes must outlive the parsed message, which points into
them.

## Related Pages

- [Carbon](carbon.md)
- [Fees And Broadcasting](fees-and-broadcasting.md)
- [Carbon API and Wire Format](reference/carbon-wire.md)
