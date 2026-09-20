# TypeScript SDK Fees And Broadcasting

A Carbon transaction is built, planned, signed and sent as four separate steps.
The same message works whether the key sits in memory, in a hardware wallet, or
in a wallet reached over Phantasma Link.

Builders carry no prices. A message leaves a builder with `maxGas` at `0`, and
that marks it as not yet planned. The chain never admits a message that offers
zero gas.

## The Four Steps

```ts
import {
  Bytes32,
  NativeTxHelper,
  PhantasmaAPI,
  PhantasmaKeys,
  parseUnits,
  summarizeFeePlan,
} from 'phantasma-sdk-ts/public';

const api = new PhantasmaAPI('https://testnet.phantasma.info/rpc', null, 'testnet');
const keys = PhantasmaKeys.fromWIF(process.env.WIF!);
const receiverPublicKey = new Uint8Array(32); // the recipient's 32-byte public key

// 1. Build the message.
const transfer = NativeTxHelper.transferFungible({
  from: new Bytes32(keys.publicKey),
  to: new Bytes32(receiverPublicKey),
  tokenId: 1n, // KCAL
  amount: parseUnits('10', 10), // 10 KCAL in atoms
});

// 2. Plan the gas offer and the storage ceiling from the chain's own prices.
const plan = await api.fees.plan(transfer);
console.log(summarizeFeePlan(plan));

// 3 and 4. Sign and send.
const hash = await api.sendTransaction(transfer, keys);
```

`sendTransaction` runs steps 2 to 4 in one call. It plans a message whose
`maxGas` is still zero, signs it with every signer it was given, and broadcasts
it. A message the caller already planned is sent as it is.

## What The Chain Bills

The chain charges for every byte the transaction puts in the block. It also
escrows every storage row the transaction creates. A message therefore carries
two ceilings, and both have to be set before it is signed:

| Field | Meaning |
| ----- | ------- |
| `TxMsg.maxGas` | The gas offer, in KCAL atoms. Unused gas is refunded. A short offer is rejected. |
| `TxMsg.maxData` | The storage escrow ceiling, in SOUL atoms. It prices every new row at the current row price. |

## The Fee Planner

`api.fees` is the fee planner of the chain the client talks to. It reads
`getGasConfig` once and keeps the answer for a minute.

| Member | What it does |
| ------ | ------------ |
| `plan(msg, options?)` | Prices one message and returns a `FeePlan`. |
| `config(options?)` | Returns the cached `GasConfig`. |
| `chainParams(options?)` | Returns `expiryWindow`, `blockRateTarget` and `gasModelVersion`. |
| `planWith(config, msg, options?)` | Prices a message against a config the caller already holds. It touches no network. |
| `invalidate()` | Drops the cached config, so the next call reads it again. |

`planFees(msg, config, options?)` is the same calculation as a plain function.
Use it when the config is already in hand and no client is available.

### The Plan

```ts
const plan = await api.fees.plan(msg);
```

| Field | Meaning |
| ----- | ------- |
| `maxGas` | The gas offer that covers the bill. |
| `maxData` | The storage escrow ceiling. |
| `expectedGasBill` | The bill the chain formula yields for these inputs. |
| `newStorageQuanta` | Storage quanta the operation creates. One quantum is 1024 bytes of a new paid row. |
| `deletedStorageQuanta` | Storage quanta the operation deletes. The field is informational and does not enter the bill. |
| `kinds` | The operations the message was recognised as, in call order. |
| `exact` | Whether the bill is a prediction or a ceiling. |
| `envelopeBytes` | The signed size the plan was computed for. |
| `apply(msg)` | Returns a copy of the message with `maxGas` and `maxData` set. The input is left untouched. |

`summarizeFeePlan(plan)` renders the three amounts as decimal strings for
display:

```ts
const summary = summarizeFeePlan(plan);
// { gasBill: '0.00426', gasOffer: '0.00426', storageCeiling: '0' }
```

`parseUnits` and `formatUnits` convert between decimal amounts and atoms. KCAL
has 10 decimals and SOUL has 8.

### A Prediction Or A Ceiling

Part of the price depends on chain state that the message does not carry. One
example is whether the recipient already holds the token. Every such fact is
taken at the reading that costs more.

`plan.exact` reports the result. It is `true` when nothing the plan had to
assume could have changed the number. It is `false` when an unstated fact
decided part of the price, or when part of the message had to be budgeted. A
wallet shows the amount when the flag is `true`, and "up to" in front of the
amount when it is `false`.

The flag says nothing about facts the caller stated. A stated fact that is wrong
produces a wrong bill.

### Stating A Fact

`FeePlanOptions` is where a caller tells the planner a fact it would otherwise
assume. Every field is optional and most callers pass none.

| Option | What it states |
| ------ | -------------- |
| `recipientHoldsToken` | The recipient already has a balance row for this token. |
| `bigFungible` | Price the widest answer a variable length balance can have. |
| `tokenBurnedBefore` | The token's burnt counter already exists. |
| `supplyRowExists` | The supply row still exists and does not have to be recreated. |
| `duplicatedSeries` | The series mints duplicates. |
| `romHasMetaId` | The ROM carries an `_i` id. |
| `seriesHasMetaId` | The series metadata carries an `_i` id. |
| `infusions` | What a burned NFT holds. A burn cannot be planned without it. |
| `scriptUnitsAllowance`, `scriptEventBytes`, `scriptStorageQuanta` | The allowance for a VM script. |
| `witnessCount` | How many witnesses will sign a `Call`, `Call_Multi`, `Trade` or `Phantasma` message. |

The facts the message itself carries are read out of it: counts, sizes, token
ids and the recipient.

### Which Operation Reads Which Fact

`plan.kinds` names the operations that were priced. A `Call_Multi` performs
several, and each one is priced and then summed.

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

`NativeFeeKind.Script` covers VM scripts and calls the model does not describe.
Their work depends on execution, so they are budgeted and never predicted.
`plan.exact` is `false` whenever one is present.

## Burning An NFT

A burn returns whatever the NFT holds at its own address, and the chain charges
for each returned asset. That set is chain state with no costlier bound, so a
burn cannot be planned without the list:

```ts
const infusions = await api.infusedAssets(tokenId, instanceId);
const plan = await api.fees.plan(burn, { infusions });
```

`api.fees.plan` reads the list from the chain by itself, and so does
`sendTransaction`. An empty list says the NFT holds nothing.

## The Pre-Flight Before A Token Creation

`Token.CreateToken` is charged its policy fee before the contract looks at the
symbol. That fee is the largest single price in the protocol. Governance sets it
and `getGasConfig` reports it. Sending a symbol that is already taken pays the
fee and gets nothing back.

`sendTransaction` runs one lookup before it signs a token creation. Every other
message goes straight through.

```ts
import { preflightTransaction } from 'phantasma-sdk-ts/public';

const check = await preflightTransaction(api, msg);
// check.verdict is 'free', 'taken', 'unknown' or 'not-applicable'
```

The check asks a question whose answer it already knows: it fetches the gas
token by its id, and that lookup does not touch symbols. When the node answers
it, the node is serving token lookups and the symbol is `free`. When the node
does not answer it, the verdict is `unknown` and nothing was established.

`sendTransaction` refuses on `taken` and on `unknown`, and throws
`TransactionPreflightError`. A caller that wants to decide for itself reads the
verdict and sends with `{ preflight: false }`.

## Signing

Any witness that implements `TxSigner` can sign. The interface is a `publicKey`
and a `sign(bytes)` method, and the signature may arrive later. `PhantasmaKeys`
satisfies it without an adapter.

| Call | What it does |
| ---- | ------------ |
| `TxMsgSigner.sign(msg, key)` | Signs with one in-memory key. |
| `TxMsgSigner.signWithKeys(msg, keys)` | Signs with several in-memory keys. |
| `TxMsgSigner.signWith(msg, signers)` | Signs with any set of `TxSigner` witnesses. |
| `TxMsgSigner.signAndSerializeWith(msg, signers)` | The same, and returns the envelope bytes. |

A contract call chooses its own witness set, and each witness is 96 bytes the
chain bills. `planFees` therefore asks for `witnessCount` on `Call`,
`Call_Multi`, `Trade` and `Phantasma` messages. `sendTransaction` fills the
count in from the signers it was given. The gas payer has to be one of them,
because the chain rejects a transaction its payer did not sign.

A wallet that signs elsewhere plans the message first and hands
`plan.apply(msg)` over.

### Who Pays The Gas

The native transaction types come in pairs. In the plain form the account whose
tokens move also pays the gas and signs alone. Naming a `gasPayer` in the
builder parameters selects the second form, where a different account pays the
gas and both accounts sign.

For these types the message itself fixes the witness set. The signers are
matched to their slots by public key, so the order they are passed in does not
matter. A signer that is not a witness of the message is refused.

```ts
const transfer = NativeTxHelper.transferFungible({
  from: new Bytes32(senderPublicKey),
  gasPayer: new Bytes32(payerPublicKey),
  to: new Bytes32(receiverPublicKey),
  tokenId: 1n,
  amount: parseUnits('10', 10),
});

const hash = await api.sendTransaction(transfer, [payerKeys, senderKeys]);
```

## Expiry

Builders stamp `DEFAULT_TX_EXPIRY_MS` from now, which is 45,000 milliseconds.
That is sized for a transaction signed on the spot.

When a person has to approve the transaction first, take the chain's whole
window:

```ts
import { expiryWithin } from 'phantasma-sdk-ts/public';

const params = await api.fees.chainParams();
const transfer = NativeTxHelper.transferFungible({
  from: new Bytes32(keys.publicKey),
  to: new Bytes32(receiverPublicKey),
  tokenId: 1n,
  amount: parseUnits('10', 10),
  expiry: expiryWithin(params.expiryWindow),
});
```

`expiryWithin(windowMs, marginMs?)` returns the latest expiry the chain will
still admit, less a margin for clock skew. The margin defaults to 5,000
milliseconds.

## Reading The Prices Directly

| Call | What it returns |
| ---- | --------------- |
| `api.getGasConfig()` | The on-chain gas configuration and the chain parameters fee estimation needs. |
| `api.estimateTransaction(txData)` | A dry run of a serialized envelope against current chain state. |

`getGasConfig` changes only through a governance resolution, so its result is
safe to cache. `gasConfigFromRpc` turns the result into a `GasConfig`.

`estimateTransaction` is the node-side estimate. Signatures inside the envelope
may be zero-filled dummies of the correct length, because the simulation skips
signature checks and the dummies keep the byte length the bill depends on. The
method returns a standard RPC error until the estimate service is launched. The
local planner is the fallback.

## Broadcasting

| Call | Family |
| ---- | ------ |
| `api.sendTransaction(msg, signers, options?)` | Carbon message, with plan, pre-flight, signatures and broadcast in one step. |
| `api.sendCarbonTransaction(txHex)` | A Carbon envelope that is already signed and serialized. |
| `api.sendRawTransaction(txHex)` | A signed VM script transaction. |

Broadcasting only submits the transaction. Read it back before acting on the
result:

```ts
const tx = await api.getTransaction(hash);
const carbonTokenId = CreateTokenTxHelper.parseResult(tx.result);
```

Use the parser that matches the operation:

| Operation | Parser |
| --------- | ------ |
| Create token | `CreateTokenTxHelper.parseResult(resultHex)` |
| Create token series | `CreateTokenSeriesTxHelper.parseResult(resultHex)` |
| Phantasma NFT mint | `MintPhantasmaNonFungibleTxHelper.parseResult(resultHex)` |

## Errors

An RPC call that fails over HTTP still carries the JSON-RPC error the node sent,
and the SDK surfaces it. A transaction message that arrives truncated is
refused rather than read as a shorter message.

## Safety Checklist

- Plan a message before signing it. A zero offer is never admitted.
- Read `plan.exact` before showing an amount to a person.
- Keep WIF values out of the documentation, the logs and the repository.
- Check the transaction state before parsing its result.
- Use the mainnet, testnet and devnet endpoints intentionally.
