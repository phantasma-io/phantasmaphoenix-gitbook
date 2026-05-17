# Go SDK RPC Result Models

RPC wrappers decode node responses into structs under `pkg/rpc/response`. Large
chain amounts are exposed as strings when the node result uses string values.

## Common Field Rules

| Field pattern | Meaning |
| ------------- | ------- |
| `Amount`, `CurrentSupply`, `MaxSupply`, `Fee`, `Price` | Base-unit numeric strings unless a helper formats decimals. |
| `Decimals` | Number of decimal places used for display formatting. |
| `Hash`, `BlockHash`, `Script`, `Payload`, `Result`, `Rom`, `Ram` | Hex or encoded strings returned by the node. |
| `CarbonID`, `CarbonTokenID`, `CarbonSeriesID`, `CarbonNFTAddress` | Carbon identifiers used to reconcile RPC reads with Carbon transaction results. |
| `State` | Execution state. Use `StateIsSuccess()` and `StateIsFault()` instead of comparing one spelling. |

## Helpers

| Helper | Purpose |
| ------ | ------- |
| `BalanceResult.Clone()` | Returns a deep copy of a balance row. |
| `BalanceResult.ConvertDecimals()` | Formats `Amount` with the row's `Decimals`. |
| `BalanceResult.ConvertDecimalsToFloat()` | Returns the formatted amount as `*big.Float`. |
| `StakeResult.ConvertDecimals()` | Formats stake amount with 8 decimals. |
| `AccountResult.Clone()` | Deep-copy account balances. |
| `AccountResult.GetTokenBalance(token)` | Finds a token balance or appends a zero row using token decimals. |
| `TransactionResult.StateIsSuccess()` | Returns true for success states. |
| `TransactionResult.StateIsFault()` | Returns true for fault/break states. |
| `TokenResult.IsBurnable()` and related helpers | Checks comma-separated token flags. |
| `ScriptResult.DecodeResultWithError()` | Decodes the single VM result hex string into `VMObject`. |
| `ScriptResult.DecodeResultsWithError(index)` | Decodes an indexed VM result. |

## Pagination

| Model | Fields |
| ----- | ------ |
| `PaginatedResult[T]` | `Page`, `PageSize`, `Total`, `TotalPages`, `Result` |
| `CursorPaginatedResult[T]` | `Result`, `Cursor` |

Use cursor pagination for Carbon inventory reads and numeric pagination for
older page/page-size endpoints such as auctions and address transaction history.

## Account And Balance Models

| Model | Fields and helpers |
| ----- | ------------------ |
| `BalanceResult` | `Chain`, `Amount`, `Symbol`, `Decimals`, `Ids`; helpers: `Clone`, `ConvertDecimals`, `ConvertDecimalsToFloat` |
| `StakeResult` | `Amount`, `Time`, `Unclaimed`; helpers: decimal formatting |
| `StorageResult` | `Available`, `Used`, `Avatar`, `Archives` |
| `AccountResult` | `Address`, `Name`, `Stakes`, `Stake`, `Unclaimed`, `Relay`, `Validator`, `Storage`, `Balances`; helpers: `Clone`, `GetTokenBalance` |
| `AddressTransactionsResult` | `Address`, `Txs` |

## Chain, Nexus, And Organization Models

| Model | Fields |
| ----- | ------ |
| `InteropResult` | `Local`, `External` |
| `PlatformResult` | `Platform`, `Chain`, `Fuel`, `Tokens`, `Interop` |
| `GovernanceResult` | `Name`, `Value` |
| `OrganizationResult` | `ID`, `Name`, `Members` |
| `CrowdsaleResult` | `Hash`, `Name`, `Creator`, `Flags`, `StartDate`, `EndDate`, `SellSymbol`, `ReceiveSymbol`, `Price`, cap fields |
| `ChainResult` | `Name`, `Address`, `Parent`, `Height`, `Organization`, `Contracts`, `Dapps` |
| `NexusResult` | `Name`, `Protocol`, `Platforms`, `Tokens`, `Chains`, `Governance`, `Organizations` |
| `LeaderboardResult` | `Name`, `Rows` |

## Block, Transaction, Event, And Script Models

| Model | Fields and helpers |
| ----- | ------------------ |
| `EventResult` | `Address`, `Contract`, `Kind`, `Data` |
| `OracleResult` | `URL`, `Content` |
| `SignatureResult` | `Kind`, `Data` |
| `TransactionResult` | `Hash`, `ChainAddress`, `Timestamp`, `BlockHeight`, `BlockHash`, `Script`, `Payload`, `Events`, `State`, `Result`, `Fee`, `Signatures`, `Expiration`; helpers: `StateIsSuccess`, `StateIsFault` |
| `BlockResult` | `Hash`, `PreviousHash`, `Timestamp`, `Height`, `ChainAddress`, `Protocol`, `Txs`, `ValidatorAddress`, `Reward`, `Events`, `Oracles` |
| `ScriptResult` | `Events`, `Result`, `Results`, `Oracles`; helpers: VM result decoding |

## Token, NFT, Schema, And Price Models

| Model | Fields and helpers |
| ----- | ------------------ |
| `TokenPropertyResult` | `Key`, `Value` |
| `TokenExternalResult` | `Platform`, `Hash` |
| `TokenPriceResult` | `Timestamp`, `Open`, `High`, `Low`, `Close` |
| `VMVariableSchemaResult` | `Type`, `Schema` |
| `VMNamedVariableSchemaResult` | `Name`, `Schema` |
| `VMStructSchemaResult` | `Fields`, `Flags` |
| `TokenSchemasResult` | `SeriesMetadata`, `Rom`, `Ram` |
| `TokenSeriesResult` | `SeriesID`, `CarbonTokenID`, `CarbonSeriesID`, owner and supply fields, `Mode`, `Script`, `Methods`, `Metadata` |
| `TokenResult` | token definition fields, `CarbonID`, metadata, schemas, external mappings, price rows; helpers: `IsBurnable`, `IsDivisible`, `IsFiat`, `IsFinite`, `IsFuel`, `IsFungible`, `IsMintable`, `IsStakable`, `IsTransferable` |
| `TokenDataResult` | NFT id, series, Carbon identifiers, owner/creator, ROM/RAM, status, infusion, properties |

Keep token definition, series metadata, and NFT instance data separate in
application storage. They have different identities and update paths.

## Contract, Auction, Archive, And Network Models

| Model | Fields |
| ----- | ------ |
| `ABIParameterResult`, `ABIMethodResult`, `ABIEventResult` | Contract ABI field, method, and event shapes. |
| `ContractResult` | `Name`, `Address`, `Script`, `Methods`, `Events` |
| `AuctionResult` | creator/chain addresses, dates, base/quote symbols, token id, prices, type, ROM/RAM, listing fee, current winner |
| `ArchiveResult` | `Name`, `Hash`, `Time`, `Size`, `Encryption`, `BlockCount`, `MissingBlocks`, `Owners` |
| `BuildInfoResult` | `Version`, `Commit`, `BuildTimeUTC` |
| `PhantasmaVMConfigResult` | stored flag, feature level, gas settings, and deploy fuel setting |

Auction and archive models are for marketplace/storage endpoints. Network
models such as peers, validators, swaps, and receipts are mostly used by
explorers and operational tooling.
