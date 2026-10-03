# Fees And Gas

Every transaction pays a gas bill in KCAL. A transaction that adds stored data also escrows SOUL for it. Mainnet computes both under gas model v2, active since 2026-08-27. The SDK fee planners apply the same rules; see [SDKs](/developers/sdks/README.md#fees-under-gas-model-v2).

## Units

| Unit | Meaning |
| --- | --- |
| Gas unit | The unit in which the chain prices work and block data. |
| KCAL atom | 1 KCAL is 10,000,000,000 atoms. Bills, `maxGas`, `minimumGasOffer`, `minimumGasBill`, and the operation fees are in KCAL atoms. |
| SOUL atom | 1 SOUL is 100,000,000 atoms. `maxData` and the storage escrow are in SOUL atoms. |
| Storage quantum | 1024 bytes of a stored row, key and value together. Every row is rounded up to whole quanta. |

The chain converts gas units to KCAL atoms with two fields of the gas configuration:

```text
KCAL atoms = (gas units * feeMultiplier) >> feeShift
```

## The Gas Configuration

The gas configuration is chain state, set by a special resolution of the validators. Every block records the configuration it was settled under. The `getGasConfig` RPC method returns the configuration of the latest block:

| Field | Meaning |
| --- | --- |
| `gasModelVersion` | `2` when `gasConfig.version` is `1` or higher, otherwise `1`. |
| `blockRateTarget` | The target time between blocks, in milliseconds. |
| `expiryWindow` | How far in the future a transaction's expiry may lie, in milliseconds. |
| `unitsPerBlockDataByte` | The gas units charged per byte of block data: `25`. It is a constant of gas model v2, not a configuration field. |
| `gasConfig.feeMultiplier`, `gasConfig.feeShift` | The conversion from gas units to KCAL atoms. |
| `gasConfig.gasTokenId`, `gasConfig.dataTokenId` | The token that pays gas (`1`, KCAL) and the token of the storage escrow (`2`, SOUL). |
| `gasConfig.minimumGasOffer` | The smallest `maxGas` a transaction may state. |
| `gasConfig.minimumGasBill` | The smallest bill. Every settled bill is raised to it, so a `maxGas` below it is also refused. |
| `gasConfig.gasFeeTransfer`, `gasConfig.gasFeeQuery` | The gas units that native module methods charge: `gasFeeTransfer` for transfers and most writes, `gasFeeQuery` for reads. |
| `gasConfig.policyFeeCreateTokenBase`, `policyFeeCreateTokenSymbol`, `policyFeeCreateTokenSeries`, `policyFeeRegisterName` | Operation fees in KCAL atoms; see [Operation Fees](#operation-fees). |
| `gasConfig.dataEscrowPerRow` | The SOUL atoms escrowed per storage quantum. |
| `gasConfig.legacyDataEscrowPerRow` | The escrow per quantum of the rows that existed before gas model v2. Releasing such a quantum refunds this amount. |
| `gasConfig.gasBurnRatioMul`, `gasBurnRatioShift` | The burned share of each bill. |
| `gasConfig.gasProducerRatioMul`, `gasProducerRatioShift` | The block producer share of each bill. |
| `gasConfig.gasDappRatioMul`, `gasDappRatioShift` | The dApp share of each bill. |
| `gasConfig.maxNameLength`, `maxTokenSymbolLength` | The longest account name and token symbol. |
| `gasConfig.maxStructureSize` | The largest structure the chain accepts, in bytes. |
| `gasConfig.gasFeeCreateTokenBase`, `gasFeeCreateTokenSymbol`, `gasFeeCreateTokenSeries`, `gasFeeRegisterName`, `gasFeePerByte` | Prices of gas model v1, kept so that old blocks replay the same way. Gas model v2 does not use them. |

The response carries the 64-bit values as decimal strings. A rejected transaction comes back from the RPC as `Transaction was rejected: Rejection type: <type>, error: <reason>`, with the types and reasons named below.

## Admission

A node checks every transaction before it queues it:

1. `maxGas` is at least `minimumGasOffer` and at least `minimumGasBill`. Otherwise the transaction is rejected with `GasFees` (`below minimum gas` or `below minimum gas bill`).
2. The transaction carries witnesses, and the fee payer is one of them. Otherwise it is rejected with `Witnesses` (`no witnesses` or `not signed by gas payer`).
3. The fee payer holds `maxGas` in KCAL and, when the transaction sets `maxData`, `maxData` in SOUL. Otherwise the node rejects it with `GasFees` (`gas payer balance below offered maxGas/maxData`). This is the node setting `chain.mempool_balance_precheck`, on by default.

## Queue Order

A node orders its queue by `maxGas`, the highest offer first and in arrival order among equal offers. When the queue is full, a new transaction with a higher offer takes the place of the lowest offer. This is the node setting `chain.mempool_priority`, on by default.

The bill does not depend on the offer. A higher `maxGas` buys an earlier place, and the part of it that the bill does not use returns at settlement.

## Reservation

When a block executes the transaction, the chain first reserves `maxGas` KCAL and, when `maxData` is set, `maxData` SOUL from the fee payer. A fee payer who cannot cover the reservation is rejected with `GasFees` or `DataFees` (`FeeEscrow failure`), and the transaction does not enter the block.

## The Gas Bill

During execution the chain adds to the bill:

| Source | Charge |
| --- | --- |
| VM instructions | A flat cost per instruction: `0` for `NOP` and `RET`, `5` for `GET`, `PUT`, `CALL`, and `LOAD`, `10` for `EXTCALL` and `CTX`, `100` for `SWITCH`, and `1` for every other opcode. |
| VM data and arithmetic | Units by size; see [The Work Table](#the-work-table). |
| Interop calls | A cost per call from the VM configuration: `gasStandard` for most interops, and `gasNexus`, `gasOrganization`, `gasAccount`, `gasOracle`, or `gasConstructor` for some. |
| Native module methods | `gasFeeTransfer` or `gasFeeQuery` units per call. Methods that mint, burn, or transfer NFTs charge `gasFeeTransfer` per NFT. |
| Operation fees | KCAL atoms, added without the conversion; see [Operation Fees](#operation-fees). |

The `getPhantasmaVmConfig` RPC method returns the interop costs. Every charge in gas units goes through the conversion to KCAL atoms. If the bill passes `maxGas` during execution, execution stops with a `gasLimit` error and the transaction aborts.

After execution the chain adds the block data of the transaction:

```text
block data = envelope bytes
           + result bytes
           + 4 bytes per event + event bytes
           + the net storage quanta the transaction adds, if any
block data fee = (block data * 25 * feeMultiplier) >> feeShift
```

The envelope is the transaction as the block stores it, witnesses included. A bill below `minimumGasBill` is then raised to it.

## The Work Table

On top of the flat cost per instruction, these instructions charge by the size of their data:

| Instructions | Gas units |
| --- | --- |
| `COPY`, `PUSH`, `CAST`, `LOAD`, `CAT`, `ADD` of two strings, `PUT`, `GET`, `UNPACK` | 1 per 1024 bytes moved, rounded up. |
| `CALL` | 1 per 16 registers of the new frame, rounded up. |
| `ADD`, `SUB`, `SHL`, `SHR`, `MIN`, `MAX` on numbers | 1 per 512 bits of the larger operand, rounded up. |
| `MUL`, `DIV`, `MOD` | `(aWords * bWords) / 8`, where the words of an operand are its bit length / 64 + 1. |
| `POW` | `72 + resultWords * resultWords / 24`, where `resultBits` is the base's bit length times the exponent, at most 16384, and `resultWords` is `resultBits` / 64 + 1. A base or an exponent of 0 costs 72. |

Divisions are integer divisions. The table is part of gas model v2, not of the gas configuration.

## Operation Fees

These fees are set in KCAL atoms by the gas configuration and are added to the bill without the conversion:

| Operation | Fee |
| --- | --- |
| Create a token | `policyFeeCreateTokenBase`, plus `policyFeeCreateTokenSymbol >> (symbol length - 1)`. The symbol fee halves with every character after the first. |
| Create a token series | `policyFeeCreateTokenSeries`. |
| Register an account name | `policyFeeRegisterName >> (name length - 1)`. |

A token creation takes the base fee before it checks the symbol. When the symbol is taken, the transaction aborts and still pays the base fee.

## Settlement

After the bill is complete, the chain settles the transaction:

1. If the bill exceeds `maxGas`, or the storage escrow exceeds `maxData`, the transaction aborts.
2. The chain charges the bill and the storage escrow and returns the rest of the reservation to the fee payer.
3. The chain divides the bill into shares, in this order: burned, block producer, dApp. Each share is `(bill * mul) >> shift` with the share's two fields, capped by what the earlier shares leave. The rest stays in the gas pool.

The block producer share goes to the block's `producerAddress`. The dApp share goes to the `to` address of the script's `AllowGas` call. When that address is a system address, or when the transaction is a structured one, which has no `AllowGas`, no dApp share is taken and the amount stays in the gas pool.

## Aborted Transactions

A transaction aborts when its execution fails, when its bill passes `maxGas`, or when its storage escrow passes `maxData`. An aborted transaction:

- keeps none of its state changes, results, or events
- enters the block with the state `Break`
- pays a bill made of its execution charges and the block data of its envelope, raised to `minimumGasBill` and capped at `maxGas`

If an aborted transaction used no gas during execution, it is rejected instead. It does not enter the block and pays nothing.

## Storage Escrow

The chain counts the storage of every row that a transaction creates, grows, shrinks, or deletes:

```text
quanta of a row = ceil((key bytes + value bytes) / 1024)
```

For every row whose quanta grow, the chain escrows `dataEscrowPerRow` SOUL atoms per new quantum. For every row whose quanta shrink, it refunds the escrow of the released quanta to the fee payer of the transaction that shrinks the row. Each row keeps its own record of the quanta it holds and the atoms they paid, so a refund returns the price that was paid even after `dataEscrowPerRow` changes:

- A row that releases all the quanta it gained under gas model v2 gets back every atom they paid.
- A row that releases part of them gets back their average price per quantum, rounded down.
- Quanta that existed before gas model v2 are released after the newer ones and refund `legacyDataEscrowPerRow` each.

The escrow of a transaction is the sum over its rows, escrows minus refunds. A positive escrow is charged to the fee payer; a negative one is paid to the fee payer.

These rows cost no escrow: KCAL and SOUL balances, staked SOUL, the burn counters of KCAL and SOUL, and the rows of the governance module and of the chain's internal records.

## Script Transactions

A script transaction sent with `sendRawTransaction` carries no `maxGas` or `maxData` field. The chain reads both from the script:

- `maxGas` is `gasPrice * gasLimit` of the script's `AllowGas` call, and the `from` address of that call is the fee payer. A script without `AllowGas` is rejected.
- There is no `maxData`. Nothing is reserved for storage; the chain charges the escrow from the fee payer's SOUL at settlement, and rejects the transaction if the fee payer does not hold it.
- `SpendGas` has no effect. The chain settles the bill after the script either way.

## Fee Estimation

The `estimateTransaction` RPC method runs a serialized transaction against the current chain state without recording it. The signatures may be zero-filled dummies of the correct length: the run skips signature checks, and the dummies keep the envelope length that the bill depends on. The run uses the `maxGas` and `maxData` of the transaction and the fee payer's real balances.

| Field | Meaning |
| --- | --- |
| `wouldAbort` | The transaction would be rejected or would abort. |
| `abortReason` | The reason, when it would. |
| `gasBillKcalBase` | The bill in KCAL atoms. |
| `dataRows` | The storage quanta the transaction would add. |
| `dataEscrowAtoms`, `dataRefundAtoms` | The escrow and the refund in SOUL atoms. |
| `recommendedMaxGas` | The bill plus 15%, rounded up, and at least `minimumGasOffer` and `minimumGasBill`. |
| `recommendedMaxData` | The net escrow plus 15%, rounded up to a multiple of `dataEscrowPerRow`. `0` when the transaction adds no net storage. |

The recommendations come only from a run that completes; a run that would abort answers `0` for both. An aborted run settles at the declared `maxGas`, so its bill does not show the true cost: raise `maxGas` and estimate again.

A chain node serves estimates only when its setting `chain.estimate_tx` is on, and it stops a run after `chain.estimate_tx_budget` gas units of work, 10,000 by default. When no node serves estimates, the RPC answers with the error `Estimate service unavailable`. The public mainnet RPC nodes serve estimates.

## Related Pages

{% content-ref url="/developers/blockchain/smart-contracts/storage-and-data-escrow.md" %}
Storage And Data Escrow
{% endcontent-ref %}

{% content-ref url="/developers/script-builder/README.md" %}
Script Builder
{% endcontent-ref %}

{% content-ref url="/about/economy/fees.md" %}
Fees
{% endcontent-ref %}

{% content-ref url="/about/economy/block-producer.md" %}
Block Producers
{% endcontent-ref %}
