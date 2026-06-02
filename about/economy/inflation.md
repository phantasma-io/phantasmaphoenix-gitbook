# Supply And Issuance

SOUL and KCAL are native Phantasma assets with live on-chain supply accounting.
Current supply, burned supply, and metadata should be read from the chain rather
than copied from static documentation.

Neither SOUL nor KCAL uses a fixed maximum supply field in native token metadata.
Their supply is live protocol state: SOUL changes through scheduled issuance and
reward accounting, while KCAL changes through staking rewards and fee burns.

## SOUL Supply

SOUL is the staking and governance asset. SOUL issuance follows the protocol
schedule and reward accounting. The chain tracks when issuance is due and
applies SOUL rewards through the scheduled issuance flow.

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
