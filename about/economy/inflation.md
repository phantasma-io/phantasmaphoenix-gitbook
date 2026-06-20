# Supply And Issuance

SOUL and KCAL are native Phantasma assets with live on-chain supply accounting.
Current supply, burned supply, and metadata should be read from the chain rather
than copied from static documentation.

Neither SOUL nor KCAL uses a fixed maximum supply field in native token metadata.
Their supply is live protocol state: SOUL changes through scheduled issuance and
reward accounting, while KCAL changes through staking rewards and fee burns.

## SOUL Supply

SOUL is the staking and governance asset. It has no fixed maximum supply; new
SOUL is issued on a fixed monthly schedule, on the first of each month.

Each month the protocol applies two issuances, in this order:

1. A proportional issuance of `0.25%` of the current SOUL supply (`3%` per year).
2. A fixed `125,000 SOUL`, shared equally among eligible Soul Masters.

The order matters for the amounts. The `0.25%` is computed from the SOUL supply
before the fixed `125,000 SOUL` is added, not after. The next month's `0.25%` is
then computed from the resulting supply, which already includes both of the
previous month's issuances. The chain tracks when the next issuance is due and
applies it through the scheduled issuance flow.

### Soul Master Distribution

The fixed `125,000 SOUL` is split equally among the Soul Masters that held the
Soul Master staking threshold (`50,000 SOUL` staked, see [SOUL](soul.md)) for the
entire preceding month, without interruption.

An account that reaches the threshold partway through a month, or whose staked
balance drops below the threshold at any point during the month, does not receive
that month's share. It becomes eligible from the first full month it holds the
threshold continuously. The share each eligible Soul Master receives therefore
depends on how many accounts were eligible for that month.

The current supply is queryable through token RPC methods such as `getToken`.
Applications, explorers, and reports should use live chain data when presenting
SOUL supply.

## KCAL Supply

KCAL is the resource asset used for transaction gas. KCAL is minted when SOUL
staking rewards are claimed. Transaction fee settlement can burn KCAL according
to the current gas configuration. Refunds return unused prepaid KCAL to the fee
payer and are not a separate issuance path.

Because KCAL is minted by staking reward claims and reduced by fee burns, current
supply should be read from the chain.

## Staking Rewards

Current mainnet SOUL staking metadata defines KCAL as the reward token and sets
the base reward rate to `0.002 KCAL` per staked SOUL per day before configured
boosters.

Reward metadata is protocol state. Wallets and applications should query live
stake data and unclaimed KCAL rather than relying only on a copied formula.

## Related Pages

{% content-ref url="soul.md" %}
SOUL
{% endcontent-ref %}

{% content-ref url="kcal.md" %}
KCAL
{% endcontent-ref %}

{% content-ref url="fees.md" %}
Fees
{% endcontent-ref %}
