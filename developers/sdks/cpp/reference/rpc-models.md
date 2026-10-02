# C++ SDK RPC Result Models

The RPC result models are the structs in the `phantasma::rpc` namespace of
`PhantasmaAPI.h`. The groups below say which struct answers which call; the
field lists at the end of the page come from the header.

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

## Result Structs

Every struct of `PhantasmaAPI.h` with its fields and types, in header order.
`PHANTASMA_VECTOR` is `std::vector` unless the adapter configures another
container.

<!-- generated:cpp-result-structs -->
### `Balance`

| Field | Type | Note |
| --- | --- | --- |
| `chain` | `String` |  |
| `amount` | `String` |  |
| `symbol` | `String` |  |
| `decimals` | `UInt32` |  |
| `ids` | `PHANTASMA_VECTOR<String>` |  |

### `Interop`

| Field | Type | Note |
| --- | --- | --- |
| `local` | `String` |  |
| `external` | `String` |  |

### `VmVariableSchemaResult`

| Field | Type | Note |
| --- | --- | --- |
| `type` | `String` |  |
| `schema` | `std::shared_ptr<VmStructSchemaResult>` |  |

### `VmNamedVariableSchemaResult`

| Field | Type | Note |
| --- | --- | --- |
| `name` | `String` |  |
| `schema` | `VmVariableSchemaResult` |  |

### `VmStructSchemaResult`

| Field | Type | Note |
| --- | --- | --- |
| `fields` | `PHANTASMA_VECTOR<VmNamedVariableSchemaResult>` |  |
| `flags` | `Int32` |  |

### `TokenSchemas`

| Field | Type | Note |
| --- | --- | --- |
| `seriesMetadata` | `VmStructSchemaResult` |  |
| `rom` | `VmStructSchemaResult` |  |
| `ram` | `VmStructSchemaResult` |  |

### `Platform`

| Field | Type | Note |
| --- | --- | --- |
| `platform` | `String` |  |
| `chain` | `String` |  |
| `fuel` | `String` |  |
| `tokens` | `PHANTASMA_VECTOR<String>` |  |
| `interop` | `PHANTASMA_VECTOR<Interop>` |  |

### `Governance`

| Field | Type | Note |
| --- | --- | --- |
| `name` | `String` |  |
| `value` | `String` |  |

### `TokenProperty`

| Field | Type | Note |
| --- | --- | --- |
| `key` | `String` |  |
| `value` | `VmValue` |  |

### `Organization`

| Field | Type | Note |
| --- | --- | --- |
| `name` | `String` |  |
| `owner` | `String` |  |
| `carbonOwner` | `String` |  |
| `metadata` | `PHANTASMA_VECTOR<TokenProperty>` |  |
| `memberCount` | `String` |  |

### `OrganizationMember`

| Field | Type | Note |
| --- | --- | --- |
| `address` | `String` |  |
| `carbonAddress` | `String` |  |
| `isMember` | `bool` |  |
| `memberTime` | `UInt64` |  |

### `Nexus`

| Field | Type | Note |
| --- | --- | --- |
| `name` | `String` |  |
| `platforms` | `PHANTASMA_VECTOR<Platform>` |  |
| `tokens` | `PHANTASMA_VECTOR<Token>` |  |
| `chains` | `PHANTASMA_VECTOR<Chain>` |  |
| `governance` | `PHANTASMA_VECTOR<Governance>` |  |
| `organizations` | `PHANTASMA_VECTOR<String>` |  |

### `Stake`

| Field | Type | Note |
| --- | --- | --- |
| `amount` | `String` |  |
| `time` | `UInt32` |  |
| `unclaimed` | `String` |  |

### `Archive`

| Field | Type | Note |
| --- | --- | --- |
| `name` | `String` |  |
| `hash` | `String` |  |
| `time` | `UInt32` |  |
| `size` | `UInt32` |  |
| `encryption` | `String` |  |
| `blockCount` | `Int32` |  |
| `missingBlocks` | `PHANTASMA_VECTOR<Int32>` |  |
| `owners` | `PHANTASMA_VECTOR<String>` |  |

### `Storage`

| Field | Type | Note |
| --- | --- | --- |
| `available` | `UInt32` |  |
| `used` | `UInt32` |  |
| `avatar` | `String` |  |
| `archives` | `PHANTASMA_VECTOR<Archive>` |  |

### `AccountInfo`

| Field | Type | Note |
| --- | --- | --- |
| `address` | `String` |  |
| `name` | `String` |  |
| `stake` | `Stake` |  |

### `Account`

| Field | Type | Note |
| --- | --- | --- |
| `address` | `String` |  |
| `name` | `String` |  |
| `stakes` | `Stake` |  |
| `stake` | `String` |  |
| `unclaimed` | `String` |  |
| `relay` | `String` |  |
| `validator` | `String` |  |
| `storage` | `Storage` |  |
| `balances` | `PHANTASMA_VECTOR<Balance>` |  |
| `txs` | `PHANTASMA_VECTOR<String>` |  |

### `LeaderboardRow`

| Field | Type | Note |
| --- | --- | --- |
| `address` | `String` |  |
| `value` | `String` |  |

### `Leaderboard`

| Field | Type | Note |
| --- | --- | --- |
| `name` | `String` |  |
| `rows` | `PHANTASMA_VECTOR<LeaderboardRow>` |  |

### `Dapp`

| Field | Type | Note |
| --- | --- | --- |
| `name` | `String` |  |
| `address` | `String` |  |
| `chain` | `String` |  |

### `Chain`

| Field | Type | Note |
| --- | --- | --- |
| `name` | `String` |  |
| `address` | `String` |  |
| `parent` | `String` |  |
| `height` | `UInt32` |  |
| `organization` | `String` |  |
| `contracts` | `PHANTASMA_VECTOR<String>` |  |
| `dapps` | `PHANTASMA_VECTOR<String>` |  |

### `GasConfigData`

| Field | Type | Note |
| --- | --- | --- |
| `version` | `UInt32` | config version; >= 1 activates gas-model-v2 billing |
| `maxNameLength` | `UInt32` |  |
| `maxTokenSymbolLength` | `UInt32` |  |
| `feeShift` | `UInt32` | right-shift applied after the fee multiplier stage |
| `maxStructureSize` | `UInt32` |  |
| `feeMultiplier` | `UInt64` | multiplier from gas units to kcal-base |
| `gasTokenId` | `UInt64` |  |
| `dataTokenId` | `UInt64` |  |
| `minimumGasOffer` | `UInt64` | minimum acceptable maxGas offer |
| `dataEscrowPerRow` | `UInt64` | storage escrow price per 1024-byte row quantum, data-token atoms |
| `gasFeeTransfer` | `UInt64` | gas units charged per native transfer-class operation |
| `gasFeeQuery` | `UInt64` |  |
| `gasFeeCreateTokenBase` | `UInt64` |  |
| `gasFeeCreateTokenSymbol` | `UInt64` |  |
| `gasFeeCreateTokenSeries` | `UInt64` |  |
| `gasFeePerByte` | `UInt64` | v1 price of block-carried bytes, kcal-base per byte (unused under v2) |
| `gasFeeRegisterName` | `UInt64` |  |
| `gasBurnRatioMul` | `UInt64` |  |
| `gasBurnRatioShift` | `UInt32` |  |
| `hasV2Fields` | `bool` | true when the v2 tail below was present in the response |
| `minimumGasBill` | `UInt64` | v2: floor applied to every settled gas bill, kcal-base |
| `gasProducerRatioMul` | `UInt64` | v2: producer fee-split ratio numerator |
| `gasProducerRatioShift` | `UInt32` |  |
| `gasDappRatioMul` | `UInt64` | v2: dapp (gasTarget) fee-split ratio numerator |
| `gasDappRatioShift` | `UInt32` |  |
| `policyFeeCreateTokenBase` | `UInt64` | v2: token creation price, kcal-base (no multiplier) |
| `policyFeeCreateTokenSymbol` | `UInt64` | v2: symbol price, halved per char after the first |
| `policyFeeCreateTokenSeries` | `UInt64` |  |
| `policyFeeRegisterName` | `UInt64` | v2: name price, shifted right by (length-1) |
| `legacyDataEscrowPerRow` | `UInt64` | v2: frozen pre-flip dataEscrowPerRow (pre-flip row refunds) |

### `GasConfigResult`

| Field | Type | Note |
| --- | --- | --- |
| `gasModelVersion` | `UInt32` | 1 = original fee model, 2 = gas-model-v2 (config version >= 1) |
| `gasConfig` | `GasConfigData` |  |
| `blockRateTarget` | `UInt32` | chain block rate target in milliseconds |
| `expiryWindow` | `UInt32` | transaction expiry window in milliseconds |
| `unitsPerBlockDataByte` | `UInt32` | v2 price of block bytes in gas units per byte; 0 under v1 |

### `EstimateTransactionResult`

| Field | Type | Note |
| --- | --- | --- |
| `wouldAbort` | `bool` | true when the tx would not complete on-chain as submitted; see abortReason |
| `abortReason` | `String` | rejection or abort reason when wouldAbort is true; empty otherwise |
| `gasBillKcalBase` | `UInt64` | settled bill incl. minimum-bill floor and maxGas clamp (aborts still pay) |
| `dataRows` | `UInt64` | newly paid storage quanta (dataRows * dataEscrowPerRow == dataEscrowAtoms) |
| `dataEscrowAtoms` | `UInt64` | gross storage escrow paid for grown rows, in data-token atoms |
| `dataRefundAtoms` | `UInt64` | gross storage refunds for shrunk rows, in data-token atoms |
| `recommendedMaxGas` | `UInt64` | bill + 15% margin floored at the chain minimums; 0 when wouldAbort |
| `recommendedMaxData` | `UInt64` | net escrow + 15% margin, row-aligned; 0 when wouldAbort or no escrow |

### `Event`

| Field | Type | Note |
| --- | --- | --- |
| `address` | `String` |  |
| `contract` | `String` |  |
| `kind` | `String` |  |
| `name` | `String` |  |
| `data` | `String` |  |

### `Oracle`

| Field | Type | Note |
| --- | --- | --- |
| `url` | `String` |  |
| `content` | `String` |  |

### `Signature`

| Field | Type | Note |
| --- | --- | --- |
| `kind` | `String` |  |
| `data` | `String` |  |

### `Transaction`

| Field | Type | Note |
| --- | --- | --- |
| `hash` | `String` |  |
| `chainAddress` | `String` |  |
| `timestamp` | `UInt32` |  |
| `blockHeight` | `Int32` |  |
| `blockHash` | `String` |  |
| `script` | `String` |  |
| `payload` | `String` |  |
| `carbonTxType` | `Byte` |  |
| `carbonTxData` | `String` |  |
| `events` | `PHANTASMA_VECTOR<Event>` |  |
| `extendedEvents` | `PHANTASMA_VECTOR<EventExtended>` |  |
| `result` | `String` |  |
| `debugComment` | `String` |  |
| `fee` | `String` |  |
| `signatures` | `PHANTASMA_VECTOR<Signature>` |  |
| `expiration` | `UInt32` |  |
| `state` | `String` |  |
| `sender` | `String` |  |
| `gasPayer` | `String` |  |
| `gasTarget` | `String` |  |
| `gasPrice` | `String` |  |
| `gasLimit` | `String` |  |

### `AccountTransactions`

| Field | Type | Note |
| --- | --- | --- |
| `address` | `String` |  |
| `txs` | `PHANTASMA_VECTOR<Transaction>` |  |

### `Paginated`

| Field | Type | Note |
| --- | --- | --- |
| `page` | `UInt32` |  |
| `pageSize` | `UInt32` |  |
| `total` | `UInt32` |  |
| `totalPages` | `UInt32` |  |
| `result` | `JSONValue` |  |

### `CursorPaginatedResult`

| Field | Type | Note |
| --- | --- | --- |
| `result` | `PHANTASMA_VECTOR<T>` |  |
| `cursor` | `String` |  |

### `Block`

| Field | Type | Note |
| --- | --- | --- |
| `hash` | `String` |  |
| `previousHash` | `String` |  |
| `timestamp` | `UInt32` |  |
| `height` | `UInt32` |  |
| `chainAddress` | `String` |  |
| `protocol` | `UInt32` |  |
| `txs` | `PHANTASMA_VECTOR<Transaction>` |  |
| `validatorAddress` | `String` |  |
| `producerAddress` | `String` |  |
| `reward` | `String` |  |
| `events` | `PHANTASMA_VECTOR<Event>` |  |
| `oracles` | `PHANTASMA_VECTOR<Oracle>` |  |

### `ABIParameter`

| Field | Type | Note |
| --- | --- | --- |
| `name` | `String` |  |
| `type` | `String` |  |

### `ABIMethod`

| Field | Type | Note |
| --- | --- | --- |
| `name` | `String` |  |
| `returnType` | `String` |  |
| `parameters` | `PHANTASMA_VECTOR<ABIParameter>` |  |

### `TokenSeries`

| Field | Type | Note |
| --- | --- | --- |
| `seriesId` | `String` |  |
| `currentSupply` | `String` |  |
| `maxSupply` | `String` |  |
| `burnedSupply` | `String` |  |
| `mode` | `TokenSeriesMode` |  |
| `ownerAddress` | `String` |  |
| `maxMint` | `String` |  |
| `mintCount` | `String` |  |
| `carbonTokenId` | `String` |  |
| `carbonSeriesId` | `String` |  |
| `script` | `String` |  |
| `methods` | `PHANTASMA_VECTOR<ABIMethod>` |  |
| `metadata` | `PHANTASMA_VECTOR<TokenProperty>` |  |

### `BuildInfoResult`

| Field | Type | Note |
| --- | --- | --- |
| `version` | `String` |  |
| `commit` | `String` |  |
| `buildTimeUtc` | `String` |  |

### `PhantasmaVmConfig`

| Field | Type | Note |
| --- | --- | --- |
| `isStored` | `bool` |  |
| `featureLevel` | `Int32` |  |
| `gasConstructor` | `String` |  |
| `gasNexus` | `String` |  |
| `gasOrganization` | `String` |  |
| `gasAccount` | `String` |  |
| `gasLeaderboard` | `String` |  |
| `gasStandard` | `String` |  |
| `gasOracle` | `String` |  |
| `fuelPerContractDeploy` | `String` |  |

### `Token`

| Field | Type | Note |
| --- | --- | --- |
| `symbol` | `String` |  |
| `name` | `String` |  |
| `decimals` | `Int32` |  |
| `currentSupply` | `String` |  |
| `maxSupply` | `String` |  |
| `carbonId` | `String` |  |
| `burnedSupply` | `String` |  |
| `address` | `String` |  |
| `owner` | `String` |  |
| `flags` | `String` |  |
| `script` | `String` |  |
| `series` | `PHANTASMA_VECTOR<TokenSeries>` |  |
| `metadata` | `PHANTASMA_VECTOR<TokenProperty>` |  |
| `tokenSchemas` | `TokenSchemas` |  |

### `TokenData`

| Field | Type | Note |
| --- | --- | --- |
| `id` | `String` |  |
| `series` | `String` |  |
| `carbonTokenId` | `String` |  |
| `carbonSeriesId` | `String` |  |
| `carbonNftAddress` | `String` |  |
| `mint` | `String` |  |
| `chainName` | `String` |  |
| `ownerAddress` | `String` |  |
| `creatorAddress` | `String` |  |
| `ram` | `String` |  |
| `rom` | `String` |  |
| `status` | `String` |  |
| `infusion` | `PHANTASMA_VECTOR<TokenProperty>` |  |
| `properties` | `PHANTASMA_VECTOR<TokenProperty>` |  |

### `SendRawTx`

| Field | Type | Note |
| --- | --- | --- |
| `hash` | `String` |  |
| `error` | `String` |  |

### `SendCarbonTx`

| Field | Type | Note |
| --- | --- | --- |
| `hash` | `String` |  |
| `error` | `String` |  |

### `Auction`

| Field | Type | Note |
| --- | --- | --- |
| `creatorAddress` | `String` |  |
| `chainAddress` | `String` |  |
| `startDate` | `UInt32` |  |
| `endDate` | `UInt32` |  |
| `baseSymbol` | `String` |  |
| `quoteSymbol` | `String` |  |
| `tokenId` | `String` |  |
| `price` | `String` |  |
| `rom` | `String` |  |
| `ram` | `String` |  |

### `Script`

| Field | Type | Note |
| --- | --- | --- |
| `events` | `PHANTASMA_VECTOR<Event>` |  |
| `result` | `String` |  |
| `results` | `PHANTASMA_VECTOR<String>` |  |
| `oracles` | `PHANTASMA_VECTOR<Oracle>` |  |

### `ABIEvent`

| Field | Type | Note |
| --- | --- | --- |
| `value` | `Int32` |  |
| `name` | `String` |  |
| `returnType` | `String` |  |
| `description` | `String` |  |

### `Contract`

| Field | Type | Note |
| --- | --- | --- |
| `name` | `String` |  |
| `address` | `String` |  |
| `script` | `String` |  |
| `methods` | `PHANTASMA_VECTOR<ABIMethod>` |  |
| `events` | `PHANTASMA_VECTOR<ABIEvent>` |  |

### `Channel`

| Field | Type | Note |
| --- | --- | --- |
| `creatorAddress` | `String` |  |
| `targetAddress` | `String` |  |
| `name` | `String` |  |
| `chain` | `String` |  |
| `creationTime` | `UInt32` |  |
| `symbol` | `String` |  |
| `fee` | `String` |  |
| `balance` | `String` |  |
| `active` | `bool` |  |
| `index` | `Int32` |  |

### `Receipt`

| Field | Type | Note |
| --- | --- | --- |
| `nexus` | `String` |  |
| `channel` | `String` |  |
| `index` | `String` |  |
| `timestamp` | `UInt32` |  |
| `sender` | `String` |  |
| `receiver` | `String` |  |
| `script` | `String` |  |

### `Peer`

| Field | Type | Note |
| --- | --- | --- |
| `url` | `String` |  |
| `version` | `String` |  |
| `flags` | `String` |  |
| `fee` | `String` |  |
| `pow` | `UInt32` |  |

### `Validator`

| Field | Type | Note |
| --- | --- | --- |
| `address` | `String` |  |
| `type` | `String` |  |

### `Swap`

| Field | Type | Note |
| --- | --- | --- |
| `sourcePlatform` | `String` |  |
| `sourceChain` | `String` |  |
| `sourceHash` | `String` |  |
| `sourceAddress` | `String` |  |
| `destinationPlatform` | `String` |  |
| `destinationChain` | `String` |  |
| `destinationHash` | `String` |  |
| `destinationAddress` | `String` |  |
| `symbol` | `String` |  |
| `value` | `String` |  |

### `PhantasmaError`

| Field | Type | Note |
| --- | --- | --- |
| `code` | `int` |  |
| `message` | `String` |  |
<!-- /generated -->
