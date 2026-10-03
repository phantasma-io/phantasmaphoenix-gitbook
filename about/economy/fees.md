# Fees

Phantasma fees have two native dimensions:

- **KCAL gas** through `maxGas`
- **SOUL data escrow** through `maxData`

KCAL pays for execution and block data. SOUL is escrowed when a transaction
creates or expands persistent chain state. A transaction can need one or both,
depending on what it does.

## KCAL Gas

`maxGas` is the most KCAL a transaction may spend. The fee payer signs the
transaction. Before the transaction runs, the chain reserves the whole `maxGas`
from the fee payer's KCAL. If the fee payer cannot cover it, the transaction is
rejected and does not enter a block.

The gas bill is the sum of:

- the work the transaction performs, priced in gas units
- the block data, priced at 25 gas units per byte: the bytes of the
  transaction, of its result, and of its events
- the operation fees that the gas configuration sets directly in KCAL, such as
  the fees for creating a token or registering a name

The fee multiplier of the gas configuration converts gas units to KCAL. A bill
below the minimum gas bill is raised to it. After the transaction runs, the
chain charges the bill and returns the rest of the reservation to the fee payer.

VM transactions also include `AllowGas` and `SpendGas` calls in the script. For
those transactions, gas price multiplied by gas limit must match the
transaction's `maxGas` value.

## Failed Transactions

A transaction aborts when its execution fails, when its gas bill would exceed
`maxGas`, or when its data escrow would exceed `maxData`. An aborted transaction
keeps none of its state changes, but it still enters the block, and the fee
payer pays its gas bill, at most `maxGas`. RPC methods report it with the state
`Break`.

A transaction that aborts before it has used any gas is rejected instead. It
does not enter a block and costs nothing.

## SOUL Data Escrow

`maxData` is the most SOUL a transaction may escrow for permanent state growth.
It is not a byte count and it is not a contract storage allowance. When a
transaction sets `maxData`, the chain reserves it from the fee payer's SOUL
before the transaction runs, in the same way as `maxGas`.

The chain counts storage in quanta of 1024 bytes. Each row of chain state takes
as many quanta as its key and value need together. The transaction escrows SOUL
for every quantum it adds:

```text
SOUL data escrow = quanta added * dataEscrowPerRow
```

When a transaction deletes or shrinks a row, the escrow that the released quanta
paid goes back to the fee payer of that transaction. The unused part of the
reservation also returns.

A script transaction has no `maxData`. The chain charges its escrow from the
fee payer's SOUL after the script runs, and rejects the transaction if the fee
payer does not hold enough SOUL.

## Fee Configuration

The chain gas configuration holds the fee values, including:

- the fee multiplier that converts gas units to KCAL
- the minimum gas offer, the smallest `maxGas` a transaction may state, and the
  minimum gas bill
- the gas units of basic reads and writes, `gasFeeQuery` and `gasFeeTransfer`
- the operation fees for creating a token and its symbol, for creating a
  series, and for registering a name
- the escrow per storage quantum, `dataEscrowPerRow`
- the burned, block producer, and dApp shares of each gas bill

The `getGasConfig` RPC method returns the configuration. Wallets and developer
tools should calculate fees from it and show the final estimate before signing.

## Related Pages

{% content-ref url="kcal.md" %}
KCAL
{% endcontent-ref %}

{% content-ref url="soul.md" %}
SOUL
{% endcontent-ref %}

{% content-ref url="block-producer.md" %}
Block Producers
{% endcontent-ref %}

{% content-ref url="/developers/blockchain/smart-contracts/storage-and-data-escrow.md" %}
Storage And Data Escrow
{% endcontent-ref %}

{% content-ref url="/developers/token-deployment-frontend.md" %}
Token Deployment UI
{% endcontent-ref %}
