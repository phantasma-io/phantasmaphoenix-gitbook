# SOUL

SOUL is the primary native staking and governance asset of Phantasma mainnet. It
is maintained by the protocol token module, so normal SOUL balances, transfers,
staking state, supply accounting, and data escrow are native chain state rather
than application-level token logic.

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
- **KCAL generation.** Staked SOUL accrues claimable KCAL over time. Claiming,
  staking more SOUL, or unstaking can materialize accrued KCAL into the account's
  available KCAL balance.
- **Data escrow.** SOUL is the chain's data token. Transactions that grow
  permanent chain state use SOUL data escrow through the transaction `maxData`
  limit.

SOUL is also used by protocol-level organization membership. The current mainnet
staking metadata links the Soul Master threshold to the `masters` organization.

## Protocol Surfaces

SOUL behavior is split across native protocol modules:

- the token module stores SOUL metadata, balances, transfers, staked balances,
  and supply accounting
- the stake contract exposes VM-facing staking methods such as `Stake`,
  `Unstake`, `Claim`, and `GetUnclaimed`
- the chain gas configuration identifies SOUL as the data token used by
  `maxData`
- token metadata and issuance schedule state define scheduled SOUL issuance

## Staking Metadata

Current mainnet token metadata defines these staking parameters:

| Parameter | Current value |
| --- | --- |
| Reward token | `KCAL` |
| Base reward period | `1 day` |
| Base reward rate | `0.002 KCAL` per staked SOUL per day |
| Minimum stake duration before unstake | `60 seconds` |
| Soul Master threshold | `50,000 SOUL` staked |
| Reward booster token | `CROWN` |
| Reward booster rate | `5%` per CROWN, up to `20` CROWNs |

These values are protocol metadata. Applications should query the chain for
live metadata and unclaimed KCAL instead of hardcoding reward calculations in
user-facing balances.

## Staking Flow

When SOUL is staked, the protocol moves the amount from the account's available
SOUL balance into staked SOUL accounting and records a staking timestamp. If the
account already had SOUL staked, the previous staking interval can trigger an
automatic KCAL claim before the new staking timestamp is recorded.

When SOUL is unstaked, the protocol checks the staking lock, claims any eligible
KCAL for the previous staking interval, and moves the unstaked SOUL back into
the account's available SOUL balance.

A direct KCAL claim can be made without changing the staked SOUL amount. The
claim operation mints the accrued KCAL reward into the staking account's
available KCAL balance.

## SOUL Data Escrow

Phantasma uses SOUL for persistent state growth. A transaction that creates or
expands charged chain state must set a `maxData` limit and the fee payer must
have enough available SOUL to cover the resulting data escrow.

The chain measures the transaction's actual state change, rounds charged storage
rows to the protocol storage quantum, and applies the current
`dataEscrowPerRow` value. Unused prepaid data escrow is refunded. Transactions
that delete or shrink charged state can also produce a SOUL data escrow refund.

This is separate from staking. Staking SOUL to an account or contract does not
increase a contract storage quota. Storage growth is paid by the transaction
fee payer through `maxData`.

## Supply

SOUL does not use a fixed maximum supply field in native token metadata. SOUL
supply changes through scheduled protocol issuance and reward accounting.

The chain tracks current supply, burned supply, and token metadata as live
protocol state, so documentation and applications should read current values
from RPC instead of copying fixed totals.

## Working With SOUL

APIs usually return SOUL amounts as integer strings in base units. Convert using
8 decimals when showing user-facing amounts.

For balances and metadata, use token and account RPC methods such as `getToken`,
`getTokenBalance`, and `getAccount`. For staking, use the native stake contract
methods exposed by the SDKs: `Stake`, `Unstake`, `Claim`, and read methods for
staked and unclaimed amounts.

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

{% content-ref url="/developers/sdks/csharp/examples/stake-soul.md" %}
Stake SOUL
{% endcontent-ref %}

{% content-ref url="/developers/sdks/csharp/examples/unstake-soul.md" %}
Unstake SOUL
{% endcontent-ref %}

{% content-ref url="/developers/sdks/csharp/examples/claim-kcal.md" %}
Claim KCAL
{% endcontent-ref %}
