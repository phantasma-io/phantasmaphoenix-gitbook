# Dual Token System

Phantasma uses two native assets with separate roles: SOUL and KCAL.

SOUL is the staking and governance asset. It is also the data escrow asset used
when a transaction grows permanent chain state. KCAL is the resource asset used
for transaction execution, VM gas, and block data.

Separating these roles lets users and applications reason about two different
costs:

- KCAL is paid for computation, VM execution, and transaction data in blocks.
- SOUL is escrowed when a transaction creates or expands persistent chain state.

Staking SOUL generates claimable KCAL. Users who want network participation can
stake SOUL and claim KCAL over time. Users or applications that only need to pay
for transactions can hold KCAL directly.

## Native Assets

{% content-ref url="soul.md" %}
SOUL
{% endcontent-ref %}

{% content-ref url="kcal.md" %}
KCAL
{% endcontent-ref %}

## Developer Notes

Developers should plan for both fee dimensions:

- `maxGas` limits the KCAL a transaction can spend on execution and block data.
- `maxData` limits the SOUL a transaction can escrow for persistent state growth.

For storage-specific behavior, see the storage and data escrow page.

{% content-ref url="/developers/blockchain/smart-contracts/storage-and-data-escrow.md" %}
Storage And Data Escrow
{% endcontent-ref %}
