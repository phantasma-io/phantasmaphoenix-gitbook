# Fees

Phantasma fees have two native dimensions:

- **KCAL gas** through `maxGas`
- **SOUL data escrow** through `maxData`

KCAL pays for execution and block data. SOUL is escrowed when a transaction
creates or expands persistent chain state. A transaction can need one or both,
depending on what it does.

## KCAL Gas

`maxGas` is the maximum KCAL a transaction is allowed to spend. The fee payer
must sign the transaction and must have enough available KCAL to cover the final
gas bill.

The validator computes the gas bill from:

- execution work performed by the transaction
- native operation fees from the current gas configuration
- payload, result, and event data written into the block

Unused prepaid KCAL is refunded. If the final bill exceeds `maxGas`, or the fee
payer cannot cover the bill, the transaction is rejected or aborted according to
the transaction path.

VM transactions also include `AllowGas` and `SpendGas` calls in the script. For
those transactions, gas price multiplied by gas limit must match the
transaction's `maxGas` value.

## SOUL Data Escrow

`maxData` is the maximum SOUL a transaction is allowed to escrow for permanent
state growth. It is not a byte count and it is not a contract storage allowance.

The validator measures the transaction's actual state changes and charges net
positive storage growth in rounded storage rows:

```text
SOUL data escrow = charged storage rows * dataEscrowPerRow
```

`dataEscrowPerRow` is part of the chain gas configuration. Unused prepaid data
escrow is refunded. Deleting or shrinking charged state can also produce a SOUL
data escrow refund.

## Fee Configuration

Fee values are protocol configuration, not constants that applications should
hardcode. The gas configuration controls values such as:

- minimum gas offer
- transfer and query fees
- token and series creation fees
- per-byte block data fee
- data escrow per storage row
- gas fee settlement and burn parameters

Wallets and developer tools should calculate fees from the current chain
configuration and show the final estimate before signing.

## Related Pages

{% content-ref url="kcal.md" %}
KCAL
{% endcontent-ref %}

{% content-ref url="soul.md" %}
SOUL
{% endcontent-ref %}

{% content-ref url="/developers/blockchain/smart-contracts/storage-and-data-escrow.md" %}
Storage And Data Escrow
{% endcontent-ref %}

{% content-ref url="/developers/token-deployment-frontend.md" %}
Token Deployment UI
{% endcontent-ref %}
