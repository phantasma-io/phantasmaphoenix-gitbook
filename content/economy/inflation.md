---
title: "Supply And Issuance"
weight: 50
---

SOUL and KCAL have no maximum supply. SOUL supply grows by a monthly issuance
and falls when SOUL is burned. KCAL supply grows when stakers claim their
rewards and falls by the burned share of gas fees. `getToken` returns the
current and the burned supply of each token.

## SOUL Supply

SOUL is the staking and governance asset. New SOUL is issued on a fixed monthly
schedule, on the first day of each month (UTC).

Each month the protocol applies two issuances, in this order:

1. A proportional issuance of `0.25%` of the current SOUL supply (about `3%` per
   year).
2. A fixed `125,000 SOUL`, shared equally among eligible Soul Masters.

The `0.25%` is computed from the supply before the month's issuance, so it does
not include the `125,000 SOUL` of the same month. The next month's `0.25%` is
computed from the resulting supply, which includes both of the previous month's
issuances. When an issuance is due, the validator producing blocks submits the
transaction that applies it.

### Soul Master Distribution

The fixed `125,000 SOUL` is split equally among the Soul Masters that held the
Soul Master staking threshold (`50,000 SOUL` staked, see [SOUL](soul.md)) for the
entire preceding month, without interruption.

An account that reaches the threshold partway through a month, or whose staked
balance drops below the threshold at any point during the month, does not receive
that month's share. It becomes eligible from the first full month it holds the
threshold continuously. The share each eligible Soul Master receives therefore
depends on how many accounts were eligible for that month.

## KCAL Supply

KCAL is the resource asset used for transaction gas. The chain mints KCAL when
stakers claim their staking rewards; the reward rate is described on the
[SOUL](soul.md#staking-metadata) page.

Every gas bill is divided into shares, and the burned share leaves the supply;
see [Block Producers](block-producer.md#fee-shares). The unused part of a
`maxGas` reservation returns to the fee payer and does not change the supply.

## Related Pages

- [SOUL](soul.md)
- [KCAL](kcal.md)
- [Fees](fees.md)
