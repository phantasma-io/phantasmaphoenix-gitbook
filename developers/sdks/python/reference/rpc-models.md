# Python SDK RPC Result Models

RPC wrappers decode JSON responses into dataclasses. Large numeric chain
quantities are modeled as strings when the corresponding result fields are
declared as strings in the SDK.

The SDK does not hide the node's data model. Result classes mostly mirror the
JSON-RPC response shape and add small convenience helpers where the chain
returns base-unit amounts or encoded VM object data. Treat fields as snapshots:
after a transaction is broadcast, read the relevant account, token, NFT, or
transaction again to observe finalized state.

## Common Field Rules

| Field pattern | Meaning |
| ------------- | ------- |
| `amount`, `current_supply`, `max_supply`, `fee`, `price` | Base-unit numeric strings unless the model documents a helper. Do not parse them as floating point values. |
| `decimals` | Number of decimal places used to display a base-unit token amount. |
| `hash`, `block_hash`, `script`, `payload`, `result`, `rom`, `ram` | Hex strings returned by the node. Decode only when the consuming API expects bytes. |
| `carbon_id`, `carbon_token_id`, `carbon_series_id`, `carbon_nft_address` | Carbon identifiers used by the current token/NFT flows. Prefer these when correlating RPC reads with Carbon transaction results. |
| `state` | Execution state. Use the SDK helper instead of hardcoding only one success/fault spelling. |

## Helper Methods And Properties

These are the result-model helpers that do more than expose decoded JSON
fields.

| Helper | Purpose | Inputs | Returns and failures |
| ------ | ------- | ------ | -------------------- |
| `convert_decimals(raw, decimals, separator=".")` | Formats a base-unit integer string with a decimal separator. | `raw`: string or int. `decimals`: number of fractional digits. `separator`: output separator. | Returns `str`. It formats by string slicing, zero-fills to at least `decimals + 1` digits, trims trailing fractional zeroes, and preserves a leading `-`. It does not fetch token metadata or validate that `raw` belongs to a token with matching decimals. |
| `BalanceResult.decimal_amount()` | Formats a token balance amount using the balance row decimals. | None. | Returns `convert_decimals(self.amount, self.decimals)`. |
| `StakeResult.decimal_amount()` | Formats stake amount. | None. | Returns `convert_decimals(self.amount, 8)`. Stake formatting uses fixed 8 decimals in the SDK. |
| `AccountResult.get_token_balance(symbol, decimals=0)` | Finds or creates a balance row for a token symbol in an already-loaded account response. | `symbol`: exact token symbol. `decimals`: decimals for the inserted zero row when the symbol is absent. | Returns `BalanceResult`. If no matching row exists, appends `BalanceResult(chain="main", amount="0", symbol=symbol, decimals=decimals)` to `balances` and returns it. |
| `TransactionResult.state_is_success` | Classifies transaction state. | None. | Returns `True` when `tx_state_is_success(self.state)` returns true. It is a property, not a method. |
| `TransactionResult.state_is_fault` | Classifies fault/break transaction state. | None. | Returns `True` when `tx_state_is_fault(self.state)` returns true. It is a property, not a method. |
| `TokenResult.has_flag(flag)` | Checks one comma-separated token flag. | `flag`: exact flag text such as `Fungible` or `Burnable`. | Returns `bool`. The helper splits `flags` on commas and trims each item. |
| `TokenResult.is_burnable()` | Checks token `Burnable` flag. | None. | Returns `has_flag("Burnable")`. |
| `TokenResult.is_divisible()` | Checks token `Divisible` flag. | None. | Returns `has_flag("Divisible")`. |
| `TokenResult.is_fiat()` | Checks token `Fiat` flag. | None. | Returns `has_flag("Fiat")`. |
| `TokenResult.is_finite()` | Checks token `Finite` flag. | None. | Returns `has_flag("Finite")`. |
| `TokenResult.is_fuel()` | Checks token `Fuel` flag. | None. | Returns `has_flag("Fuel")`. |
| `TokenResult.is_fungible()` | Checks token `Fungible` flag. | None. | Returns `has_flag("Fungible")`. |
| `TokenResult.is_mintable()` | Checks token `Mintable` flag. | None. | Returns `has_flag("Mintable")`. |
| `TokenResult.is_stakable()` | Checks token `Stakable` flag. | None. | Returns `has_flag("Stakable")`. |
| `TokenResult.is_transferable()` | Checks token `Transferable` flag. | None. | Returns `has_flag("Transferable")`. |
| `ScriptResult.decode_result()` | Decodes the single VM result hex string. | None. | Returns `VMObject.from_bytes(bytes.fromhex(self.result))`. Invalid hex raises `ValueError`; VM decoding failures come from `VMObject`. |
| `ScriptResult.decode_results(index)` | Decodes one indexed VM result hex string. | `index`: Python list index into `results`. | Returns `VMObject`. An out-of-range index raises `IndexError`; invalid hex raises `ValueError`; VM decoding failures come from `VMObject`. |

## Pagination

| Model | Fields |
| ----- | ------ |
| `PaginatedResult[T]` | `page`, `page_size`, `total`, `total_pages`, `result` |
| `CursorPaginatedResult[T]` | `result`, `cursor` |

For cursor responses, keep passing `cursor` until the returned cursor is empty
or the application has enough results.

Use `PaginatedResult` for older page/page-size RPCs such as auctions and address
transaction history. Use `CursorPaginatedResult` for large token/NFT inventory
queries where the node returns an opaque cursor.

## Account And Balance Models

| Model | Fields and helpers |
| ----- | ------------------ |
| `BalanceResult` | `chain`, `amount`, `symbol`, `decimals`, `ids`; helper: `decimal_amount()` |
| `StakeResult` | `amount`, `time`, `unclaimed`; helper: `decimal_amount()` |
| `StorageResult` | `available`, `used`, `avatar`, `archives` |
| `AccountResult` | `address`, `name`, `stakes`, `stake`, `unclaimed`, `relay`, `validator`, `storage`, `balances`; helper: `get_token_balance(symbol, decimals=0)` |
| `AddressTransactionsResult` | `address`, `txs` |

`AccountResult.get_token_balance(...)` returns a zero balance when the token is
not present in the account response.

Use `get_token_balance(...)` on an account result when the UI already loaded the
full account and only needs to extract one token row. Use the RPC method
`PhantasmaRPC.get_token_balance(...)` when the page needs exactly one balance
and does not need account profile, storage, stake, or other balances.

## Chain, Nexus, And Organization Models

| Model | Fields |
| ----- | ------ |
| `InteropResult` | `local`, `external` |
| `PlatformResult` | `platform`, `chain`, `fuel`, `tokens`, `interop` |
| `GovernanceResult` | `name`, `value` |
| `OrganizationResult` | `id`, `name`, `members` |
| `CrowdsaleResult` | `hash`, `name`, `creator`, `flags`, `start_date`, `end_date`, `sell_symbol`, `receive_symbol`, `price`, `global_soft_cap`, `global_hard_cap`, `user_soft_cap`, `user_hard_cap` |
| `DappResult` | `name`, `address`, `chain` |
| `ChainResult` | `name`, `address`, `parent`, `height`, `organization`, `contracts`, `dapps` |
| `NexusResult` | `name`, `protocol`, `platforms`, `tokens`, `chains`, `governance`, `organizations` |
| `LeaderboardRowResult` | `address`, `value` |
| `LeaderboardResult` | `name`, `rows` |

These models describe chain topology and contract metadata rather than account
state. `ContractResult` and ABI models are for tools, explorers, and contract
inspection flows.

## Block, Transaction, Event, And Script Models

| Model | Fields and helpers |
| ----- | ------------------ |
| `EventResult` | `address`, `contract`, `kind`, `data` |
| `OracleResult` | `url`, `content` |
| `SignatureResult` | `kind`, `data` |
| `TransactionResult` | `hash`, `chain_address`, `timestamp`, `block_height`, `block_hash`, `script`, `payload`, `events`, `state`, `result`, `fee`, `signatures`, `expiration`; helpers: `state_is_success`, `state_is_fault` |
| `BlockResult` | `hash`, `previous_hash`, `timestamp`, `height`, `chain_address`, `protocol`, `txs`, `validator_address`, `reward`, `events`, `oracles` |
| `ScriptResult` | `events`, `result`, `results`, `oracles`; helpers: `decode_result()`, `decode_results(index)` |

`ScriptResult.decode_result()` and `decode_results(index)` decode VM object bytes
with `VMObject`.

`TransactionResult` is the record to poll after broadcasting. Use
`state_is_success` and `state_is_fault` to classify finalized execution state.
`ScriptResult` is returned by read-only script invocation. Use `result` for the
single-result path and `results` for indexed VM results.

## Token, NFT, Schema, And Price Models

| Model | Fields and helpers |
| ----- | ------------------ |
| `TokenPropertyResult` | `key`, `value` |
| `TokenExternalResult` | `platform`, `hash` |
| `TokenPriceResult` | `timestamp`, `open`, `high`, `low`, `close` |
| `VMVariableSchemaResult` | `type`, `schema` |
| `VMNamedVariableSchemaResult` | `name`, `schema` |
| `VMStructSchemaResult` | `fields`, `flags` |
| `TokenSchemasResult` | `series_metadata`, `rom`, `ram` |
| `TokenSeriesResult` | `series_id`, `carbon_token_id`, `carbon_series_id`, `owner_address`, `max_mint`, `mint_count`, `current_supply`, `max_supply`, `burned_supply`, `mode`, `script`, `methods`, `metadata` |
| `TokenResult` | `symbol`, `name`, `decimals`, `current_supply`, `max_supply`, `burned_supply`, `address`, `owner`, `flags`, `script`, `series`, `carbon_id`, `metadata`, `token_schemas`, `external`, `price`; helpers: `has_flag`, `is_burnable`, `is_divisible`, `is_fiat`, `is_finite`, `is_fuel`, `is_fungible`, `is_mintable`, `is_stakable`, `is_transferable` |
| `TokenDataResult` | `id`, `series`, `carbon_token_id`, `carbon_series_id`, `carbon_nft_address`, `mint`, `chain_name`, `owner_address`, `creator_address`, `ram`, `rom`, `status`, `infusion`, `properties` |

Use `carbon_id`, `carbon_token_id`, `carbon_series_id`, and
`carbon_nft_address` when reconciling RPC reads with Carbon transaction results.

`TokenResult` describes the token definition. `TokenSeriesResult` describes one
NFT series under a token. `TokenDataResult` describes a minted NFT instance.
These levels have different persistence and identity semantics; keep token
definition, series metadata, and NFT instance data separate in application
storage.

## Contract And ABI Models

| Model | Fields |
| ----- | ------ |
| `ABIParameterResult` | `name`, `type` |
| `ABIMethodResult` | `name`, `return_type`, `parameters` |
| `ABIEventResult` | `value`, `name`, `return_type`, `description` |
| `ContractResult` | `name`, `address`, `script`, `methods`, `events` |

ABI models are descriptive. They let tooling display callable contract methods
and event shapes, but they do not execute calls by themselves. Use
`ScriptBuilder` or Carbon builders to create the actual script or transaction.

## Auction, Archive, Channel, And Network Models

| Model | Fields |
| ----- | ------ |
| `AuctionResult` | `creator_address`, `chain_address`, `start_date`, `end_date`, `base_symbol`, `quote_symbol`, `token_id`, `price`, `end_price`, `extension_period`, `type`, `rom`, `ram`, `listing_fee`, `current_winner` |
| `ArchiveResult` | `name`, `hash`, `time`, `size`, `encryption`, `block_count`, `missing_blocks`, `owners` |
| `ChannelResult` | `creator_address`, `target_address`, `name`, `chain`, `creation_time`, `symbol`, `fee`, `balance`, `active`, `index` |
| `ReceiptResult` | `nexus`, `channel`, `index`, `timestamp`, `sender`, `receiver`, `script` |
| `PeerResult` | `url`, `version`, `flags`, `fee`, `pow` |
| `ValidatorResult` | `address`, `type` |
| `SwapResult` | `source_platform`, `source_chain`, `source_hash`, `source_address`, `destination_platform`, `destination_chain`, `destination_hash`, `destination_address`, `symbol`, `value` |
| `BuildInfoResult` | `version`, `commit`, `build_time_utc` |
| `PhantasmaVMConfigResult` | `is_stored`, `feature_level`, `gas_constructor`, `gas_nexus`, `gas_organization`, `gas_account`, `gas_leaderboard`, `gas_standard`, `gas_oracle`, `fuel_per_contract_deploy` |

Auction and archive models are used by older marketplace/storage RPCs. Network
models such as `PeerResult`, `ValidatorResult`, and `SwapResult` are mostly for
explorers, status pages, and administrative tooling.
