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

- **Transaction gas.** Every transaction pays KCAL for the work it performs and
  for the bytes it adds to the block: the transaction itself, its result, and
  its events.
- **Application resource use.** Contract calls, token and NFT operations, and
  token deployments are paid in KCAL. The fee payer must hold the transaction's
  whole `maxGas` before the transaction runs.

KCAL does not pay for permanent state growth. Storage growth is paid separately
in SOUL; see [SOUL Data Escrow](fees.md#soul-data-escrow).

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

Every transaction states `maxGas`, the most KCAL it may spend. A script
transaction states it in its `AllowGas` call, as the gas price multiplied by the
gas limit. The fee payer signs the transaction, and the chain reserves the whole
`maxGas` from the fee payer's KCAL before the transaction runs. If the fee payer
cannot cover it, the transaction is rejected.

After the transaction runs, the chain computes the gas bill from the work, the
block data, and the operation fees, charges it, and returns the rest of the
reservation. A transaction that fails, or whose bill would exceed `maxGas`, keeps
none of its changes and still pays its bill. [Fees](fees.md) gives the full
rules.

The gas configuration sets the fee values and the share of each bill that is
burned. Wallets and developer tools should read it and show the fee estimate
before signing.

## KCAL From SOUL Staking

Staked SOUL earns KCAL over time. The reward rate and the CROWN booster are
described on the [SOUL](soul.md#staking-metadata) page.

The chain mints the earned KCAL when the staking account claims it, with an
explicit `Claim` call or as part of a stake or an unstake, which claim first.

## Supply

KCAL has no maximum supply. Staking reward claims add to it, and the burned
share of gas fees removes from it; see [Supply And Issuance](inflation.md#kcal-supply).
`getToken` returns the current and the burned supply.

## Working With KCAL

APIs usually return KCAL amounts as integer strings in base units. Convert using
10 decimals when showing user-facing amounts.

`getToken` returns the KCAL metadata and supply, `getTokenBalance` the KCAL
balance of an account, and `getAccountFungibleTokens` all fungible balances of
an account. `getAccountInfo` returns the KCAL that an account's SOUL stake has
earned and not yet claimed. For transaction fees, build transactions with
explicit gas settings and confirm the wallet or tooling fee estimate before
signing.

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
