# Go SDK Fees And Broadcasting

A Carbon transaction is built, planned, signed and sent as four separate steps.
The same message works whether the key sits in memory, in a hardware wallet, or
in a wallet reached over Phantasma Link.

Builders carry no prices. A message built without a `MaxGas` has a zero gas
offer, and that marks it as not yet planned. Signing such a message is refused,
because the chain never admits an offer of zero.

## Transaction Families

| Family | Build with | Broadcast with | Result handling |
| ------ | ---------- | -------------- | --------------- |
| VM script transaction | `script_builder` + `blockchain.Transaction` | `PhantasmaRPC.SendRawTransaction` or the signing helpers | `GetTransaction`, `TransactionResult.StateIsSuccess()` |
| Carbon transaction | `carbon.TxMsg` and the builders | `PhantasmaRPC.SendTransaction` or `SendCarbonTransaction` | `GetTransaction`, Carbon result parser helpers |

## The Four Steps

```go
owner := carbon.MustBytes32FromPublicKey(keyPair.PublicKey())

// 1. Build the message.
msg := carbon.BuildTransferFungibleTx(carbon.TransferFungibleParams{
    From:    owner,
    To:      receiver,
    TokenID: 1, // KCAL
    Amount:  100_000_000,
})

// 2. Plan it against the chain.
plan, err := client.Fees().Plan(ctx, msg, rpc.PlanRequestOptions{})
if err != nil {
    return err
}
summary := carbon.SummarizeFeePlan(plan)
fmt.Printf("gas %s KCAL, storage deposit up to %s SOUL\n", summary.GasBill, summary.StorageCeiling)

// 3 and 4. Sign and send.
hash, err := client.SendTransaction(ctx, msg, carbon.KeyPairSigners(keyPair), rpc.SendTransactionOptions{})
if err != nil {
    return err
}
```

`SendTransaction` runs steps 2 to 4 in one call, plus the pre-flight. A message
whose `MaxGas` is still zero is planned. A message the caller already planned is
sent as it is.

## What The Chain Bills

The chain charges for every byte the transaction puts in the block. It also
escrows every storage row the transaction creates. A message therefore carries
two ceilings, and both have to be set before it is signed:

| Field | Meaning |
| ----- | ------- |
| `TxMsg.MaxGas` | The gas offer, in KCAL atoms. Unused gas is refunded. A short offer is rejected. |
| `TxMsg.MaxData` | The storage escrow ceiling, in SOUL atoms. It prices every new row at the current row price. |

## The Fee Planner

`client.Fees()` returns the `*rpc.FeePlanner` of the chain this client talks to.
It reads `getGasConfig` through the client and keeps the answer for a minute.

| Member | What it does |
| ------ | ------------ |
| `Plan(ctx, msg, options)` | Prices one message and returns a `carbon.FeePlan`. |
| `Config(ctx, refresh)` | Returns the cached `carbon.GasConfig`. |
| `ChainParams(ctx, refresh)` | Returns `ExpiryWindow`, `BlockRateTarget` and `GasModelVersion`. |
| `PlanWith(config, msg, options)` | Prices a message against a config the caller already holds. It touches no network. |
| `Invalidate()` | Drops the cached config, so the next call reads it again. |

`carbon.PlanFees(msg, config, options)` is the same calculation as a plain
function. Use it when the config is already in hand and no client is available.

### The Plan

| Field | Meaning |
| ----- | ------- |
| `MaxGas` | The gas offer that covers the bill. |
| `MaxData` | The storage escrow ceiling. |
| `ExpectedGasBill` | The bill the chain formula yields for these inputs. |
| `Kinds` | The operations the message was recognised as, in call order. |
| `Exact` | Whether the bill is a prediction or a ceiling. |
| `EnvelopeBytes` | The signed size the plan was computed for. |
| `Apply(msg)` | Returns a copy of the message with `MaxGas` and `MaxData` set. The input is left untouched. |

`carbon.SummarizeFeePlan(plan)` renders the amounts in KCAL and SOUL through
`GasBill`, `GasOffer` and `StorageCeiling`.
`carbon.SummarizeFeePlanWithDecimals` takes the decimals explicitly.

### A Prediction Or A Ceiling

Part of the price depends on chain state that the message does not carry. One
example is whether the recipient already holds the token. Every such fact is
taken at the reading that costs more.

`plan.Exact` reports the result. It is `true` when nothing the plan had to
assume could have changed the number. It is `false` when a costlier reading
decided part of the price, or when part of the message had to be budgeted. A
wallet shows the amount when the flag is `true`, and "up to" in front of the
amount when it is `false`.

A Go `bool` cannot say "unstated". The zero value of each option is the costlier
reading, so a caller that states the costlier value and a caller that states
nothing arrive at the same plan. Stating a costlier fact buys nothing.

### Stating A Fact

`carbon.FeePlanOptions`, which `rpc.PlanRequestOptions` embeds, is where a
caller tells the planner a fact it would otherwise assume.

| Field | What it states |
| ----- | -------------- |
| `RecipientHoldsToken` | The recipient already has a balance row for this token. |
| `Int64Balances` | The balance fits the narrow answer. `false` prices the widest one. |
| `TokenBurnedBefore` | The token's burnt counter already exists. |
| `SupplyRowExists` | The supply row still exists and does not have to be recreated. |
| `UniqueSeries` | The series does not mint duplicates. |
| `RomWithoutMetaID` | The ROM carries no `_i` id. |
| `SeriesWithoutMetaID` | The series metadata carries no `_i` id. |
| `Infusions` | What the burned NFTs hold. Nil is unstated. An empty non-nil slice states that they hold nothing. |
| `ScriptUnitsAllowance`, `ScriptEventBytes`, `ScriptStorageQuanta` | The allowance for a VM script. |
| `WitnessCount` | How many witnesses will sign a `Call`, `CallMulti`, `Trade` or `Phantasma` message. |

### Which Operation Reads Which Fact

| `NativeFeeKind` | Facts it reads |
| --------------- | -------------- |
| `NativeFeeTransferFungible` | `RecipientHoldsToken` |
| `NativeFeeTransferNonFungible` | `RecipientHoldsToken` |
| `NativeFeeMintFungible` | `RecipientHoldsToken`, `SupplyRowExists`, `Int64Balances` |
| `NativeFeeMintNonFungible` | `RecipientHoldsToken`, `SupplyRowExists`, `RomWithoutMetaID` |
| `NativeFeeMintPhantasmaNonFungible` | `RecipientHoldsToken`, `SupplyRowExists`, `UniqueSeries` |
| `NativeFeeBurnFungible` | `TokenBurnedBefore`, `SupplyRowExists`, `Int64Balances` |
| `NativeFeeBurnNonFungible` | `TokenBurnedBefore`, `SupplyRowExists`, and `Infusions`, which is required |
| `NativeFeeCreateToken` | none |
| `NativeFeeCreateTokenSeries` | `SeriesWithoutMetaID` |
| `NativeFeeRegisterName` | none |
| `NativeFeeScript` | none |

Balance rows of the gas and data tokens are free, so `RecipientHoldsToken`
cannot move the price of a KCAL or SOUL transfer.

`NativeFeeScript` covers VM scripts and calls the SDK does not model. Their work
depends on execution, so they are budgeted and never predicted. `plan.Exact` is
`false` whenever one is present.

A `CallMulti` performs several operations. Each one is priced and then summed,
because the chain bills a batch as the sum of its calls with the envelope
counted once.

## Burning An NFT

A burn returns whatever the NFT holds at its own address, and the chain charges
for each returned asset. That set is chain state with no costlier bound, so
`carbon.PlanFees` demands the list. `client.Fees().Plan` reads it from the chain
for you, and so does `SendTransaction`.

`carbon.BurnedInstances(msg)` names the NFT instances a message burns, in any
shape. It covers the native burn types, a `Token.BurnNonFungible` call, and
every such call inside a `CallMulti`. An empty answer means no list is needed.

## The Pre-Flight Before A Token Creation

A token creation pays its base policy fee before the chain looks at the symbol, and
that fee is the largest single price in the protocol. `SendTransaction`
therefore asks whether the symbol is taken, and refuses to send unless the chain
answered that it is free.

`rpc.PreflightTransaction(ctx, source, msg)` reports that verdict to a caller
that wants to decide for itself. The verdicts are free, taken, unknown and not
applicable. A verdict of unknown means the lookup established nothing.

## Signing

| Call | What it does |
| ---- | ------------ |
| `carbon.SignTxMsg(msg, keys...)` | Signs with in-memory key pairs. |
| `carbon.SignTxMsgWith(ctx, msg, signers...)` | Signs with any set of `carbon.TxSigner` witnesses, such as a hardware wallet. |
| `carbon.KeyPairSigners(keys...)` | Wraps key pairs as `carbon.TxSigner` values. |

A gas-payer transfer takes the payer's and the owner's keys. The SDK puts them
in the order the chain reads.

A contract call chooses its own witness set, and each witness is 96 bytes the
chain bills, so those messages need `WitnessCount` in the plan options.
`SendTransaction` and the `Build...TxAndSign` helpers fill it in from the
signers they are given.

## Expiry

A message keeps a default lifetime of 45 seconds, which is `carbon.DefaultTxExpiry`.
When a person sits between building and signing, set `TxLimits.Expiry` from the
chain's own window:

```go
params, err := client.Fees().ChainParams(ctx, false)
if err != nil {
    return err
}
expiry, err := carbon.ExpiryWithin(params.ExpiryWindow, 0)
if err != nil {
    return err
}
```

A margin of `0` means five seconds of headroom for clock skew.

## Reading The Prices Directly

| Call | What it returns |
| ---- | --------------- |
| `client.GetGasConfig(ctx)` | The on-chain gas configuration and the chain parameters. `ToGasConfig()` converts it. |
| `client.EstimateTransaction(ctx, txData)` | A dry run of a serialized envelope against current chain state. |

`getGasConfig` changes only through a governance resolution, so its result is
safe to cache. `EstimateTransaction` gives the exact bill of a script, which the
local planner can only budget. A node with the estimate service switched off answers a standard RPC error.

## Broadcast And Confirmation

```go
hash, err := client.SendCarbonTransaction(ctx, signedTxHex)
if err != nil {
    return err
}

tx, err := client.GetTransaction(ctx, hash)
if err != nil {
    return err
}
if !tx.StateIsSuccess() {
    return fmt.Errorf("transaction failed: %s", tx.State)
}
```

Broadcast methods return the transaction hash reported by the endpoint. They do
not wait for final execution or parse Carbon results.

## Errors

A node that refuses a request with an HTTP error and a JSON-RPC body surfaces
the body as a `*jsonrpc.RPCError`, so `errors.As` tells the node's refusal from
a transport failure.

A transaction message that arrives truncated is refused rather than read as a
shorter message.
