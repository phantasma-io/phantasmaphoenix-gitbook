# SOUL

SOUL is the primary native staking and governance asset of Phantasma mainnet. It
is maintained by the protocol token module, so normal SOUL balances, transfers,
staking state, supply accounting, and data escrow are native chain state.

SOUL works together with KCAL. SOUL represents long-term network participation
and is used for staking and data escrow. KCAL is the resource asset used for gas
and execution fees.

## Token Identity

| Field | Value |
| --- | --- |
| Symbol | `SOUL` |
| Native name | `Phantasma Stake` |
| Native network | Phantasma mainnet |
| Root chain | `main` |
| Asset type | Native fungible, divisible, stakable asset |
| Carbon token ID | `2` |
| Decimals | `8` |
| Base units | `1 SOUL = 100,000,000` |
| Displayed token address | `S3dJWaLDKYhhTHf28EfsP6ateZ5w5TeZUSV8wM9JNfaD79E` |

For protocol logic, the Carbon token ID is the stable internal identifier.
Wallets, RPC responses, and explorers can also display the token address above.

## What SOUL Does

SOUL has three core roles on Phantasma:

- **Staking and governance participation.** SOUL can be staked through the
  native stake contract. Staked SOUL is tracked separately from available SOUL
  and must be unstaked before it can be transferred or spent.
- **KCAL generation.** Staked SOUL earns KCAL over time. A claim, a further
  stake, or an unstake pays the earned KCAL into the account's KCAL balance.
- **Data escrow.** SOUL is the chain's data token. A transaction that grows
  permanent chain state escrows SOUL for the growth.

SOUL staking also decides who belongs to the `masters` organization. An account
joins it when its stake reaches the Soul Master threshold and leaves it when an
unstake takes the stake below the threshold.

## Protocol Modules

SOUL behavior is split across native protocol modules:

- the token module stores SOUL metadata, balances, transfers, staked balances,
  and supply accounting
- the stake contract serves `Stake`, `Unstake`, `Claim`, and `GetUnclaimed` to
  VM scripts
- the chain gas configuration identifies SOUL as the data token
- token metadata and issuance schedule state define scheduled SOUL issuance

## Staking Metadata

The SOUL token metadata defines these staking parameters:

| Parameter | Value |
| --- | --- |
| Reward token | `KCAL` |
| Base reward period | `1 day` |
| Base reward rate | `0.002 KCAL` per staked SOUL per day |
| Minimum stake duration before unstake | `60 seconds` |
| Soul Master threshold | `50,000 SOUL` staked |
| Reward booster token | `CROWN` |
| Reward booster rate | `5%` of the base reward per CROWN, up to `20` CROWNs |

A CROWN boosts the reward only for the time the staking account has held it
within the current staking interval, which starts at the last stake, unstake,
or claim. A CROWN that arrived during the interval counts from its arrival, and
a CROWN that has left the account adds nothing. With more than 20 CROWNs, the 20
held longest count.

`getToken` with `extended` set to `true` returns these parameters as part of
the SOUL metadata.
`getAccountInfo` returns the KCAL an account has earned and not yet claimed,
boosters included.

## Staking Flow

When SOUL is staked, the chain moves the amount from the account's available
SOUL balance into its stake and records a staking timestamp. If the account
already had SOUL staked, the chain first claims the KCAL earned since the
previous timestamp.

When SOUL is unstaked, the chain checks the minimum stake duration: the unstake
fails until that time has passed since the staking timestamp. The chain then
claims the KCAL earned since the timestamp and moves the unstaked SOUL back into
the account's available balance.

A claim pays the earned KCAL without changing the staked amount. The chain mints
the reward into the staking account's KCAL balance.

Stake, unstake, and claim each record a new staking timestamp, so an unstake
right after a claim waits for the minimum stake duration again.

## SOUL Data Escrow

Phantasma uses SOUL for persistent state growth. The chain counts storage in
quanta of 1024 bytes. A transaction that adds quanta escrows `dataEscrowPerRow`
SOUL for each of them from its fee payer. A transaction that deletes or shrinks
storage receives the escrow that the released quanta paid. A structured
transaction limits its escrow with `maxData`; a script transaction has no such
limit and pays the escrow after the script runs. [Fees](fees.md#soul-data-escrow)
gives the full rules.

This is separate from staking. Staking SOUL on an account or a contract does not
give it storage. Storage growth is paid by the fee payer of the transaction that
writes it.

## Supply

SOUL has no maximum supply. The supply grows by a monthly issuance and falls
when SOUL is burned; see [Supply And Issuance](inflation.md). `getToken` returns
the current and the burned supply.

## Working With SOUL

APIs usually return SOUL amounts as integer strings in base units. Convert using
8 decimals when showing user-facing amounts.

`getToken` returns the SOUL token data and supply, and with `extended` set to
`true` also the SOUL metadata, which holds the staking parameters.
`getTokenBalance` returns the SOUL balance of an account, and
`getAccountFungibleTokens` all fungible balances of an account. `getAccountInfo`
returns an account's staked SOUL, its staking timestamp, and the KCAL it has
earned and not yet claimed. To stake, unstake, and claim, call `Stake`,
`Unstake`, and `Claim` of the stake contract; the SDK guides show the calls.

## Related Pages

{% content-ref url="kcal.md" %}
KCAL
{% endcontent-ref %}

{% content-ref url="dual-token-system.md" %}
Dual Token System
{% endcontent-ref %}

{% content-ref url="/developers/blockchain/smart-contracts/storage-and-data-escrow.md" %}
Storage And Data Escrow
{% endcontent-ref %}

{% content-ref url="/developers/sdks/README.md" %}
SDKs
{% endcontent-ref %}
