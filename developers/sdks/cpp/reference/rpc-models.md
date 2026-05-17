# C++ SDK RPC Result Models

Generated RPC result models live in `PhantasmaAPI.h`. The existing data-models
page lists the generated structs and fields:

{% content-ref url="../data-models.md" %}
Data models
{% endcontent-ref %}

## Model Groups

| Group | Representative structs |
| ----- | ---------------------- |
| Accounts and balances | `Account`, `Balance`, `AccountTransactions`, `Stake`, `Storage` |
| Blocks and transactions | `Block`, `Transaction`, `Event`, `Oracle`, `Signature` |
| Chain metadata | `Chain`, `Nexus`, `Platform`, `Interop`, `Governance`, `Organization`, `Leaderboard` |
| Contracts | `Contract`, ABI method/event/parameter structures |
| Tokens and NFTs | `Token`, `TokenSeries`, `TokenData`, `TokenSchemas`, schema result structures |
| Archives and auctions | `Archive`, `Auction` |
| Network and config | `BuildInfoResult`, `PhantasmaVmConfig`, peer/validator/swap-style results where exposed |

## Field Rules

| Field pattern | Meaning |
| ------------- | ------- |
| Amount, supply, fee, and price fields | Base-unit strings or integer-like values matching the node response. Convert using token decimals where required. |
| `carbonTokenId`, `carbonSeriesId`, `carbonNftAddress` | Carbon identifiers used by current token/NFT workflows. |
| `script`, `payload`, `result`, `rom`, `ram` | Encoded byte fields returned by the node. Decode only for APIs that expect bytes. |
| `state` | Final transaction execution state. Check success/fault before parsing a Carbon result. |

## Error Handling

High-level methods write parse or RPC failures to `PhantasmaError*` when a
pointer is provided. Low-level parse methods also accept `PhantasmaError*`.
Check `err.code` before using returned default-constructed objects.

## Pagination

Older endpoints use page/page-size result models. Current Carbon inventory
methods use cursor-paginated result wrappers. Cursor values are opaque; pass
them back unchanged with the same filters.
