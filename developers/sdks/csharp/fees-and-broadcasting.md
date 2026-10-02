# C# SDK Fees And Broadcasting

A Carbon transaction is built, planned, signed and sent as four separate steps.
The same message works whether the key sits in memory, in a hardware wallet, or
in a wallet reached over Phantasma Link.

Builders carry no prices. A message leaves a builder with `MaxGas` at `0`, and
that marks it as not yet planned. The chain never admits a message that offers
zero gas.

## The Four Steps

```csharp
using PhantasmaPhoenix.Cryptography;
using PhantasmaPhoenix.Protocol.Carbon;
using PhantasmaPhoenix.Protocol.Carbon.Blockchain.TxHelpers;
using PhantasmaPhoenix.RPC;

using var api = new PhantasmaAPI("https://testnet.phantasma.info/rpc");
var keys = PhantasmaKeys.FromWIF(Environment.GetEnvironmentVariable("WIF")!);
var receiverPublicKey = new byte[32]; // the recipient's 32-byte public key

// 1. Build the message.
var transfer = NativeTxHelper.TransferFungible(new TransferFungibleParams
{
    From = new Bytes32(keys.PublicKey),
    To = new Bytes32(receiverPublicKey),
    TokenId = 1, // KCAL
    Amount = 100_000_000_000, // 10 KCAL in atoms, because KCAL has ten decimals
});

// 2. Plan the gas offer and the storage ceiling from the chain's own prices.
var plan = await api.Fees.PlanAsync(transfer);
var summary = FeePlanSummary.Summarize(plan);

// 3 and 4. Sign and send.
var hash = await api.SendTransactionAsync(transfer, keys);
```

`SendTransactionAsync` runs steps 2 to 4 in one call. It plans a message whose
`MaxGas` is still zero, signs it with every signer it was given, and broadcasts
it. A message the caller already planned is sent as it is.

## What The Chain Bills

The chain charges for every byte the transaction puts in the block. It also
escrows every storage row the transaction creates. A message therefore carries
two ceilings, and both have to be set before it is signed:

| Field | Meaning |
| ----- | ------- |
| `TxMsg.MaxGas` | The gas offer, in KCAL atoms. Unused gas is refunded. A short offer is rejected. |
| `TxMsg.MaxData` | The storage escrow ceiling, in SOUL atoms. It prices every new row at the current row price. |

## The Fee Planner

`PhantasmaAPI.Fees` is a `ChainFeePlanner` bound to the chain the client talks
to. It reads `getGasConfig` once and keeps the answer for a minute.

| Member | What it does |
| ------ | ------------ |
| `PlanAsync(msg, options?)` | Prices one message and returns a `FeePlan`. |
| `ConfigAsync(refresh?)` | Returns the cached `GasConfig`. |
| `ChainParamsAsync(refresh?)` | Returns `ExpiryWindow`, `BlockRateTarget` and `GasModelVersion`. |
| `PlanWith(config, msg, options?)` | Prices a message against a config the caller already holds. It touches no network. |
| `Invalidate()` | Drops the cached config, so the next call reads it again. |

`FeePlanner.Plan(msg, config, options?)` is the same calculation as a static
method. Use it when the config is already in hand and no client is available.

### The Plan

| Member | Meaning |
| ------ | ------- |
| `MaxGas` | The gas offer that covers the bill. |
| `MaxData` | The storage escrow ceiling. |
| `ExpectedGasBill` | The bill the chain formula yields for these inputs. |
| `Kinds` | The operations the message was recognised as, in call order. |
| `Exact` | Whether the bill is a prediction or a ceiling. |
| `EnvelopeBytes` | The signed size the plan was computed for. |
| `Apply(msg)` | Returns a copy of the message with `MaxGas` and `MaxData` set. The input is left untouched. |

`FeePlanSummary.Summarize(plan)` renders the three amounts as decimal strings
for display, through `GasBill`, `GasOffer` and `StorageCeiling`.

`UnitConversion.ToDecimalString` and `UnitConversion.ToBigInteger` convert
between atoms and decimal amounts. KCAL has 10 decimals and SOUL has 8.

### A Prediction Or A Ceiling

Part of the price depends on chain state that the message does not carry. One
example is whether the recipient already holds the token. Every such fact is
taken at the reading that costs more.

`plan.Exact` reports the result. It is `true` when nothing the plan had to
assume could have changed the number. It is `false` when an unstated fact
decided part of the price, or when part of the message had to be budgeted. A
wallet shows the amount when the flag is `true`, and "up to" in front of the
amount when it is `false`.

The flag says nothing about facts the caller stated. A stated fact that is wrong
produces a wrong bill.

### Stating A Fact

`FeePlanOptions` is where a caller tells the planner a fact it would otherwise
assume. Every property is optional and most callers set none.

| Property | What it states |
| -------- | -------------- |
| `RecipientHoldsToken` | The recipient already has a balance row for this token. |
| `BigFungible` | Price the widest answer a variable length balance can have. |
| `TokenBurnedBefore` | The token's burnt counter already exists. |
| `SupplyRowExists` | The supply row still exists and does not have to be recreated. |
| `DuplicatedSeries` | The series mints duplicates. |
| `RomHasMetaId` | The ROM carries an `_i` id. |
| `SeriesHasMetaId` | The series metadata carries an `_i` id. |
| `Infusions` | What a burned NFT holds. A burn cannot be planned without it. |
| `ScriptUnitsAllowance` and its neighbours | The allowance for a VM script. |
| `WitnessCount` | How many witnesses will sign a `Call`, `Call_Multi`, `Trade` or `Phantasma` message. |

The facts the message itself carries are read out of it: counts, sizes, token
ids and the recipient.

### Which Operation Reads Which Fact

| `NativeFeeKind` | Facts it reads |
| --------------- | -------------- |
| `TransferFungible` | `RecipientHoldsToken` |
| `TransferNonFungible` | `RecipientHoldsToken` |
| `MintFungible` | `RecipientHoldsToken`, `SupplyRowExists`, `BigFungible` |
| `MintNonFungible` | `RecipientHoldsToken`, `SupplyRowExists`, `RomHasMetaId` |
| `MintPhantasmaNonFungible` | `RecipientHoldsToken`, `SupplyRowExists`, `DuplicatedSeries` |
| `BurnFungible` | `TokenBurnedBefore`, `SupplyRowExists`, `BigFungible` |
| `BurnNonFungible` | `TokenBurnedBefore`, `SupplyRowExists`, and `Infusions`, which is required |
| `CreateToken` | none |
| `CreateTokenSeries` | `SeriesHasMetaId` |
| `RegisterName` | none |
| `Script` | none |

Balance rows of the gas and data tokens are free, so `RecipientHoldsToken`
cannot move the price of a KCAL or SOUL transfer.

`NativeFeeKind.Script` covers VM scripts and calls the model does not describe.
Their work depends on execution, so they are budgeted and never predicted.
`plan.Exact` is `false` whenever one is present.

A `Call_Multi` performs several operations. Each one is priced and then summed,
because the chain bills a batch as the sum of its calls with the envelope
counted once.

## Burning An NFT

A burn returns whatever the NFT holds at its own address, and the chain charges
for each returned asset. That set is chain state with no costlier bound, so a
burn cannot be planned without the list:

```csharp
var infusions = await api.InfusedAssetsAsync(tokenId, instanceId);
var plan = await api.Fees.PlanAsync(burn, new PlanRequestOptions { Infusions = infusions });
```

`PlanAsync` reads the list from the chain by itself, and so does
`SendTransactionAsync`. An empty list says the NFT holds nothing.

`FeePlanner.BurnedInstances(msg)` names the NFT instances a message burns, in
any shape. It covers the native burn types, a `Token.BurnNonFungible` call, and
every such call inside a `Call_Multi`. An empty answer means no list is needed.

## The Pre-Flight Before A Token Creation

`Token.CreateToken` is charged its policy fee before the contract looks at the
symbol. That fee is the largest single price in the protocol. Governance sets it
and `getGasConfig` reports it. Sending a symbol that is already taken pays the
fee and gets nothing back.

`SendTransactionAsync` runs one lookup before it signs a token creation. Every
other message goes straight through.

```csharp
var check = await TransactionPreflight.PreflightAsync(api, msg);
// check.Verdict is Free, Taken, Unknown or NotApplicable
```

The check asks a question whose answer it already knows: it fetches the gas
token by its id, and that lookup does not touch symbols. When the node answers
it, the node is serving token lookups and the symbol is `Free`. When the node
does not answer it, the verdict is `Unknown` and nothing was established.

`SendTransactionAsync` refuses on `Taken` and on `Unknown`, and throws
`TransactionPreflightException`. A caller that wants to decide for itself reads
the verdict and sends with `new SendTransactionOptions { Preflight = false }`.

## Signing

Any witness that implements `ITxSigner` can sign. The interface is a
`PublicKey` property and a `SignAsync(message)` method. `KeyPairSigner` wraps an
in-memory key pair, so in-memory keys sign next to external signers in one
witness set.

| Call | What it does |
| ---- | ------------ |
| `TxMsgSigner.SignWithKeys(msg, keys)` | Signs with in-memory key pairs. |
| `TxMsgSigner.SignAndSerializeWithKeys(msg, keys)` | The same, and returns the envelope bytes. |
| `TxMsgSigner.SignWithAsync(msg, signers)` | Signs with any set of `ITxSigner` witnesses. |
| `TxMsgSigner.SignAndSerializeWithAsync(msg, signers)` | The same, and returns the envelope bytes. |

A contract call chooses its own witness set, and each witness is 96 bytes the
chain bills. `FeePlanner.Plan` therefore asks for `WitnessCount` on `Call`,
`Call_Multi`, `Trade` and `Phantasma` messages. `SendTransactionAsync` fills the
count in from the signers it was given. The gas payer has to be one of them,
because the chain rejects a transaction its payer did not sign.

A wallet that signs elsewhere plans the message first and hands `plan.Apply(msg)`
over.

### Who Pays The Gas

The native transaction types come in pairs. In the plain form the account whose
tokens move also pays the gas and signs alone. Setting `GasPayer` in the builder
parameters selects the second form, where a different account pays the gas and
both accounts sign.

```csharp
var transfer = NativeTxHelper.TransferFungible(new TransferFungibleParams
{
    From = new Bytes32(senderPublicKey),
    GasPayer = new Bytes32(payerPublicKey),
    To = new Bytes32(receiverPublicKey),
    TokenId = 1,
    Amount = 100_000_000_000,
});

var hash = await api.SendTransactionAsync(transfer, new IKeyPair[] { payerKeys, senderKeys });
```

For these types the message itself fixes the witness set. The signers are
matched to their slots by public key, so the order they are passed in does not
matter.

## Expiry

Builders stamp `TxLimits.DefaultExpiryMs` from now, which is 45,000
milliseconds. That is sized for a transaction signed on the spot.

When a person has to approve the transaction first, take the chain's whole
window:

```csharp
var chainParams = await api.Fees.ChainParamsAsync();
var transfer = NativeTxHelper.TransferFungible(new TransferFungibleParams
{
    From = new Bytes32(keys.PublicKey),
    To = new Bytes32(receiverPublicKey),
    TokenId = 1,
    Amount = 100_000_000_000,
    Expiry = TxLimits.ExpiryWithin(chainParams.ExpiryWindow),
});
```

`TxLimits.ExpiryWithin(expiryWindowMs, marginMs)` returns the latest expiry the
chain will still admit, less a margin for clock skew. The margin defaults to
5,000 milliseconds.

## Reading The Prices Directly

| Call | What it returns |
| ---- | --------------- |
| `GetGasConfigAsync()` | The on-chain gas configuration and the chain parameters fee estimation needs. |
| `EstimateTransactionAsync(txData)` | A dry run of a serialized envelope against current chain state. |

`getGasConfig` changes only through a governance resolution, so its result is
safe to cache. `GasConfigResult.ToGasConfig()` converts the response into the
`GasConfig` the planner uses, and it throws on a malformed numeric string or on
a v2 response that is missing its tail fields.

`EstimateTransactionAsync` is the node-side estimate. Signatures inside the
envelope may be zero-filled dummies of the correct length, because the
simulation skips signature checks and the dummies keep the byte length the bill
depends on. The method returns a standard RPC error until the estimate service
is launched. The local planner is the fallback.

`EstimateTransactionResult.ToFeeQuote()` converts a completed estimate into the
same `FeeQuote` a local plan produces. It throws when `WouldAbort` is set,
because an aborted simulation carries no recommendation.

## Broadcasting

| Call | Family |
| ---- | ------ |
| `SendTransactionAsync(msg, signers, options?)` | Carbon message, with plan, pre-flight, signatures and broadcast in one step. |
| `SendCarbonTransactionAsync(txHex)` | A Carbon envelope that is already signed and serialized. |
| `SendRawTransactionAsync(txHex)` | A signed VM script transaction. |
| `SignAndSendTransactionAsync(keys, nexus, script, chain, payload, customSignFunction?, expiration?)` | A VM script transaction, signed locally and broadcast. Without `expiration` it gets `TxLimits.DefaultExpiryMs` from now, like a Carbon message. |

Broadcasting only submits the transaction. Read it back before acting on the
result:

```csharp
var tx = await api.GetTransactionAsync(hash);
var carbonTokenId = CreateTokenTxHelper.ParseResult(tx!.Result!);
```

Use the parser that matches the operation:

| Operation | Parser |
| --------- | ------ |
| Create token | `CreateTokenTxHelper.ParseResult(resultHex)` |
| Create token series | `CreateTokenSeriesTxHelper.ParseResult(resultHex)` |
| Phantasma NFT mint | `MintPhantasmaNonFungibleTxHelper.ParseResult(resultHex)` |

## Errors

An RPC call that fails over HTTP still carries the JSON-RPC error the node sent,
and the SDK surfaces it. A transaction message that arrives truncated is refused
rather than read as a shorter message.

## Safety Checklist

- Plan a message before signing it. A zero offer is never admitted.
- Read `plan.Exact` before showing an amount to a person.
- Keep WIF values out of the documentation, the logs and the repository.
- Check the transaction state before parsing its result.
- Use the mainnet, testnet and devnet endpoints intentionally.
