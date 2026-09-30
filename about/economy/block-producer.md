# Block Producers

Block producers are the validator nodes that assemble transactions into blocks on the Phantasma mainnet.

## How Blocks Are Produced

The validator nodes keep one shared, replicated transaction log. At any time one validator is the leader. The leader takes the pending transactions from its queue, executes them, and publishes the result as the next block. The other validators re-execute the block against the same chain state and confirm it.

Every block exposes two addresses through the RPC block methods:

- `validatorAddress`: the leader that produced the block.
- `producerAddress`: the payout address the leader stamped into the block. It is present on blocks produced under gas model v2 and absent on earlier blocks.

The node software stamps the leader's own address, so the two fields hold the same value on current blocks. The fields have different meanings. Applications should read the one they need and should not assume that one equals the other.

## Running A Validator

Running a validator is not open to the public on the current network. A public procedure for joining the validator set is planned for the near future.

## Fee Shares

The chain gas configuration defines three shares of every gas bill:

| Share | Configuration fields |
| --- | --- |
| Burned | `gasBurnRatioMul`, `gasBurnRatioShift` |
| Block producer | `gasProducerRatioMul`, `gasProducerRatioShift` |
| dApp | `gasDappRatioMul`, `gasDappRatioShift` |

Each share is a fraction of the whole bill. The shares are taken in the order of the table, and each one is capped by what the earlier shares leave. The block producer share of every gas bill in a block is credited to that block's `producerAddress`. The dApp share goes to the dApp fee target named by the transaction, when the transaction names one.

The share ratios are protocol configuration. Read the current values from the chain with the `getGasConfig` RPC method. The gas bill itself is described on the [Fees](fees.md) page.

## Related Pages

{% content-ref url="fees.md" %}
Fees
{% endcontent-ref %}

{% content-ref url="inflation.md" %}
Supply And Issuance
{% endcontent-ref %}
