# KCAL

KCAL is the native resource asset of Phantasma mainnet. It is used to pay for
transaction execution, VM gas, and block data. SOUL staking generates claimable
KCAL, while accounts and applications pay KCAL when they submit transactions.

KCAL is maintained by the protocol token module. Normal balances, transfers,
fee settlement, supply accounting, and staking rewards are native chain state.

## Token Identity

| Field | Value |
| --- | --- |
| Symbol | `KCAL` |
| Native name | `Phantasma Energy` |
| Native network | Phantasma mainnet |
| Root chain | `main` |
| Asset type | Native fungible, divisible resource asset |
| Carbon token ID | `1` |
| Decimals | `10` |
| Base units | `1 KCAL = 10,000,000,000` |
| Displayed token address | `S3dP6LRC3f3xw4ZZ2HH9BQHzYNHuHS8vetbCQpkMFvRmVEF` |

For protocol logic, the Carbon token ID is the stable internal identifier.
Wallets, RPC responses, and explorers can also display the token address above.

## What KCAL Does

KCAL has two core roles on Phantasma:

- **Transaction gas.** Transactions pay KCAL for execution and for data written
  into the block result, such as payload, result, and event data.
- **Application resource use.** Contract calls, native token operations, NFT
  operations, and deployment workflows all require enough KCAL on the transaction
  fee payer to cover the final gas bill.

KCAL is not the data escrow asset for permanent state growth. Persistent storage
growth is covered separately by SOUL through the transaction `maxData` limit.

## Protocol Surfaces

KCAL behavior is split across native protocol modules:

- the token module stores KCAL metadata, balances, transfers, and supply
  accounting
- the gas contract exposes VM-facing gas methods such as `AllowGas` and
  `SpendGas`
- the stake contract mints KCAL when SOUL staking rewards are claimed
- the chain gas configuration identifies KCAL as the gas token used by `maxGas`
  and defines current fee settlement parameters

## Gas Flow

A transaction sets a maximum KCAL gas amount through `maxGas`. VM transactions
also include an `AllowGas` instruction, where gas price multiplied by gas limit
must match the transaction's `maxGas` value. The fee payer must sign the
transaction and must have enough available KCAL.

The validator executes the transaction, measures the gas used, adds the
configured block-data fee, and settles the final gas bill. Unused prepaid gas is
refunded. If the final gas bill is above `maxGas`, or the payer cannot cover the
bill, the transaction is rejected or aborted according to the transaction path.

The current gas configuration controls fee constants and fee settlement,
including the configured fee burn. Wallets and developer tools should show
the final fee estimate before signing and should not assume fixed fee values.

## KCAL From SOUL Staking

Staked SOUL accrues KCAL over time. The current mainnet SOUL staking metadata
sets the base reward to `0.002 KCAL` per staked SOUL per day before configured
boosters.

KCAL rewards are minted when the staking account claims them. Claiming can happen
through an explicit `Claim` call, or as part of stake and unstake flows that close
the previous staking interval.

## Supply

KCAL does not use a fixed maximum supply field in native token metadata. Current
supply and burned supply should be read from the chain because they are live
protocol state.

KCAL supply changes through native protocol accounting. Staking reward claims
mint new KCAL into accounts. Transaction fee settlement can burn KCAL according
to the current gas configuration; refunds return unused prepaid KCAL and are not
an issuance path.

## Working With KCAL

APIs usually return KCAL amounts as integer strings in base units. Convert using
10 decimals when showing user-facing amounts.

For balances and metadata, use token and account RPC methods such as `getToken`,
`getTokenBalance`, and `getAccount`. For staking rewards, query the stake state
or use SDK helpers that call the native stake contract. For transaction fees,
build transactions with explicit gas settings and confirm the wallet or tooling
fee estimate before signing.

## Related Pages

{% content-ref url="soul.md" %}
SOUL
{% endcontent-ref %}

{% content-ref url="dual-token-system.md" %}
Dual Token System
{% endcontent-ref %}

{% content-ref url="fees.md" %}
Fees
{% endcontent-ref %}

{% content-ref url="/developers/token-deployment-frontend.md" %}
Token Deployment UI
{% endcontent-ref %}

{% content-ref url="/developers/sdks/csharp/examples/claim-kcal.md" %}
Claim KCAL
{% endcontent-ref %}
