# C++ SDK Fees And Broadcasting

A Carbon transaction is built, planned, signed and sent as four separate steps.
The message is the same whether the key is in memory or in a hardware wallet.

Builders carry no prices. A message leaves a builder with `maxGas` at `0`, and
that marks it as not yet planned. The chain never admits a message that offers
zero gas.

## The Four Steps

```cpp
#include "Carbon/FeePlan.h"
#include "Carbon/FeePlanSummary.h"
using namespace phantasma::carbon;

// 1. Build the message.
TxEnvelope env = CreateTokenTxHelper::BuildTx(tokenInfo, creatorPublicKey);

// 2. Read the chain's prices once, then plan this message against them.
const Blockchain::GasConfig config = ToGasConfig(api.GetGasConfig().gasConfig);
FeePlanOptions options;
options.witnessCount = 1;      // a Call chooses its own witnesses
options.infusionsRead = true;  // nothing is burned here
FeePlan plan;
if( !PlanFees(env.msg, config, options, plan) )
    return; // the message cannot be priced; the planner has reported why

const FeePlanSummary summary = SummarizeFeePlan(plan);
// summary.gasBill "0.00426", summary.gasOffer "0.00426", summary.storageCeiling "0"

// 3 and 4. Sign and send the planned message.
env.msg = plan.Apply(env.msg);
const ByteArray signedTx = SignAndSerialize(env, keys);
```

`SendTransaction` in `Carbon/Send.h` does all four in one call, plus the
pre-flight and the infusion read:

```cpp
#include "Carbon/Send.h"

String hash;
std::string error;
if( !SendTransaction(api, env.msg, { &keys }, config, SendOptions{}, hash, error) )
    return; // error says what stopped it
```

`SendOptions` carries the plan facts, `preflight`, `controlTokenId` and
`readInfusions`.

## Native Builders

The transfers, mints and burns that need no VM script are built by
`NativeTxHelper`:

```cpp
Blockchain::TxMsg msg = NativeTxHelper::TransferFungible({ owner }, recipient, tokenId, 100);

// Naming a gas payer selects the two-signature form of the same operation.
Blockchain::TxMsg paid = NativeTxHelper::TransferFungible({ owner, &gasPayer }, recipient, tokenId, 100);
```

`TransferNonFungible` moves whole instances. One instance uses the
single-instance type and several use the multi-instance one, which is what the
chain prices differently. The `instanceIds` array has to outlive the message,
because the multi-instance forms point at it.

A big-fungible token whose balances pass int64 needs a module call instead,
because the native transfer carries the amount as a u64.

## What The Chain Bills

The chain charges for every byte the transaction puts in the block. It also
escrows every storage row the transaction creates. A message therefore carries
two ceilings, and both have to be set before it is signed:

| Field | Meaning |
| ----- | ------- |
| `TxMsg::maxGas` | The gas offer, in KCAL atoms. Unused gas is refunded. A short offer is rejected. |
| `TxMsg::maxData` | The storage escrow ceiling, in SOUL atoms. It prices every new row at the current row price. |

## The Planner

`PlanFees(msg, config, options, out)` prices a message from the message itself.
It touches no network. The signed size is computed without a key.

`ChainFeePlanner` in `Carbon/ChainFeePlan.h` is the same plan against a chain.
It holds the gas config, refreshes it when it goes stale, and reads what a
burned NFT holds instead of demanding it:

```cpp
#include "Carbon/ChainFeePlan.h"

ChainFeePlanner planner(api);
FeePlan plan;
std::string error;
if( !planner.Plan(env.msg, FeePlanOptions{}, plan, error) )
    return; // error says what the chain could not answer
```

| Member | What it does |
| ------ | ------------ |
| `Plan(msg, options, out, outError)` | Prices one message against the held config. |
| `Config(out, outError, refresh)` | Returns the gas config, reading it again when it is stale. |
| `Invalidate()` | Forgets the held config, so the next plan reads it again. |

The constructor takes `configTtlMs`, which defaults to 60,000 milliseconds. The
config changes only when a governance resolution changes it.

### The Plan

| Field | Meaning |
| ----- | ------- |
| `maxGas` | The gas offer that covers the bill. |
| `maxData` | The storage escrow ceiling. |
| `expectedGasBill` | The bill the chain formula yields for these inputs. |
| `kinds` | The operations the message was recognised as, in call order. |
| `exact` | Whether the bill is a prediction or a ceiling. |
| `envelopeBytes` | The signed size the plan was computed for. |
| `Apply(msg)` | Returns a copy of the message with `maxGas` and `maxData` set. |

`SummarizeFeePlan(plan)` renders the amounts in KCAL and SOUL through
`gasBill`, `gasOffer` and `storageCeiling`.

`FormatTokenAmount(atoms, decimals)` renders an atom count as a decimal string,
and `ParseTokenAmount(text, decimals, out)` reads one back. KCAL has 10 decimals
and SOUL has 8. The reader refuses an amount with more fractional digits than
the token holds, because those digits would be dropped and the caller would send
something it never wrote.

`EstimateNativeFee` and `EstimateNativeFeeBatch` are the calculator underneath.
Call them directly when you hold sizes rather than a message.

### A Prediction Or A Ceiling

Part of the price depends on chain state that the message does not carry. One
example is whether the recipient already holds the token. Every such fact is
taken at the reading that costs more.

`plan.exact` reports the result. It is `true` when nothing the plan had to
assume could have changed the number. It is `false` when an assumed fact decided
part of the price, or when part of the message had to be budgeted. A wallet
shows the amount when the flag is `true`, and "up to" in front of the amount
when it is `false`.

`bigFungible = true` is the one fact that claims nothing about chain state. It
asks the model to price the widest answer a variable-length balance can have. A
plan that rests on it reports `false` however it was arrived at.

### Stating A Fact

`FeePlanOptions` is where a caller tells the planner a fact it would otherwise
assume. Every field has a default and most callers change none. A plain `bool`
cannot say "unstated", so each default is the reading that costs more.

| Field | What it states |
| ----- | -------------- |
| `recipientHoldsToken` | The recipient already has a balance row for this token. |
| `bigFungible` | `false` prices the narrow balance answer. The default `true` prices the widest. |
| `tokenBurnedBefore` | The token's burnt counter already exists. |
| `supplyRowExists` | The supply row still exists and does not have to be recreated. |
| `duplicatedSeries` | `false` states that the series does not mint duplicates. |
| `romHasMetaId` | `false` states that the ROM carries no `_i` id. |
| `seriesHasMetaId` | `false` states that the series metadata carries no `_i` id. |
| `infusions`, `numInfusions`, `infusionsRead` | What the burned NFTs hold. A burn cannot be planned without it. |
| `scriptUnitsAllowance` and its neighbours | The allowance for a VM script. |
| `witnessCount` | How many witnesses will sign a `Call`, `Call_Multi`, `Trade` or `Phantasma` message. |

### Which Operation Reads Which Fact

| `NativeFeeKind` | Facts it reads |
| --------------- | -------------- |
| `TransferFungible` | `recipientHoldsToken` |
| `TransferNonFungible` | `recipientHoldsToken` |
| `MintFungible` | `recipientHoldsToken`, `supplyRowExists`, `bigFungible` |
| `MintNonFungible` | `recipientHoldsToken`, `supplyRowExists`, `romHasMetaId` |
| `MintPhantasmaNonFungible` | `recipientHoldsToken`, `supplyRowExists`, `duplicatedSeries` |
| `BurnFungible` | `tokenBurnedBefore`, `supplyRowExists`, `bigFungible` |
| `BurnNonFungible` | `tokenBurnedBefore`, `supplyRowExists`, and `infusions`, which is required |
| `CreateToken` | none |
| `CreateTokenSeries` | `seriesHasMetaId` |
| `RegisterName` | none |
| `Script` | none |

Balance rows of the gas and data tokens are free, so `recipientHoldsToken`
cannot move the price of a KCAL or SOUL transfer.

`NativeFeeKind::Script` covers VM scripts and unmodelled calls. Their work
depends on execution, so they are budgeted and never predicted. `plan.exact` is
`false` whenever one is present.

A `Call_Multi` performs several operations. Each one is priced and then summed,
because the chain bills a batch as the sum of its calls with the envelope
counted once.

## Burning An NFT

A burn returns whatever the NFT holds at its own address, and the chain charges
for each returned asset: a transfer fee and an owner lookup per fungible token,
an instance query, a transfer per instance and that lookup per NFT token, plus a
balance row for a returned token the burner does not hold. That set is chain
state with no costlier bound, so `PlanFees` demands it.

```cpp
#include "Carbon/FeeInfusions.h"

PHANTASMA_VECTOR<InfusedAsset> infusions;
if( !ReadInfusedAssets(api, env.msg, infusions) )
    return; // a query failed; the plan would be a guess
options.infusions = infusions.empty() ? nullptr : &infusions.front();
options.numInfusions = (uint32_t)infusions.size();
options.infusionsRead = true;
```

An empty list states that the instances hold nothing. `ReadInfusedAssets` asks
the account queries about the NFT's own address, which is
`TokenHelper::GetNftAddress(tokenId, instanceId)`, with `AddressType::Carbon`.
`BurnedInstances` names the instances a message burns, if you would rather read
them one at a time.

`AddressType` is what every account query takes to say how the node should read
the address text: `Phantasma` for the base58 form, `Carbon` for a 64-hex account
key.

## The Pre-Flight Before A Token Creation

`Token.CreateToken` is charged its policy fee before the contract looks at the
symbol, and that fee is the largest single price in the protocol. Sending a
symbol that is already taken pays the fee and gets nothing back.

```cpp
#include "Carbon/Preflight.h"

const PreflightResult check = PreflightTransaction(api, env.msg, gasTokenId);
if( check.verdict == PreflightVerdict::Taken )
    return; // sending this would pay the policy fee and get nothing back
```

The check costs one query and no fee. Every message that is not a token
creation answers `NotApplicable`.

## Signing

A message that takes more than one signature is signed through the signer. A
`_GasPayer` message is signed twice, the gas payer first. A call carries as many
witnesses as it was planned for, and the gas payer has to be one of them.

```cpp
ByteArray signedTx;
std::string error;
if( !Blockchain::TxMsgSigner::SignAndSerialize(env.msg, { &gasPayerKeys, &ownerKeys }, signedTx, error) )
    return; // the signer list does not match what this message names
```

A contract call chooses its own witnesses, and each one is 96 bytes the chain
bills, so `PlanFees` asks for `witnessCount`. An assumed single witness would
under-offer every multi-party transaction by 96 bytes per extra signature.

## Expiry

`TxLimits` carries `maxGas`, `maxData` and `expiry`. An `expiry` of `0` becomes
`DefaultExpiryMs` from now, which is 45,000 milliseconds.

When a person sits between building and signing, take the chain's whole window
with `ExpiryWithin(expiryWindowMs, marginMs)`. The margin defaults to 5,000
milliseconds. The chain reports its own window as `expiryWindow` in
`getGasConfig`.

## Reading A Carbon Transaction Back

`ParseTx` and `ParseSignedTx` read a message the way the chain reads it. Use
them to show an incoming transaction, to check what a signer is about to sign,
or to plan a fee for a message somebody else built.

```cpp
#include "Carbon/DataBlockchain.h"
using namespace phantasma::carbon;

const ByteView envelope{ bytes.data(), bytes.size() };

Allocator storage;
Blockchain::SignedTxMsg parsed;
ByteView signedPortion;
if( !Blockchain::ParseSignedTx(parsed, signedPortion, envelope, storage) )
    return; // truncated, or a transaction type this SDK does not know
```

Two lifetimes matter. The message keeps views into `storage`, so the allocator
has to outlive it. `signedPortion` points into the bytes you passed in, so those
have to outlive it too.

## Broadcast And Confirmation

Serialize a signed Carbon envelope, hex-encode the bytes for the RPC endpoint,
then call `SendCarbonTransaction`. After broadcast, fetch the transaction and
parse the result with the matching helper only if the transaction state is
successful.

For classic VM transactions, sign `Transaction`, serialize with signatures, and
broadcast with `SendRawTransaction`.
