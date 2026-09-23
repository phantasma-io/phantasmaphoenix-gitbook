# TypeScript SDK RPC Result Models

RPC interfaces are exported from `phantasma-sdk-ts/public` as TypeScript types.
They mirror the JSON-RPC response shape and preserve encoded fields where the
node returns encoded strings.

## Common Field Rules

| Field pattern | Meaning |
| ------------- | ------- |
| `amount`, `currentSupply`, `maxSupply`, `fee`, `price` | Base-unit strings unless a helper explicitly formats decimals. |
| `hash`, `blockHash`, `script`, `payload`, `result`, `rom`, `ram` | Encoded strings returned by the node. |
| `carbonId`, `carbonTokenId`, `carbonSeriesId`, `carbonNftAddress` | Carbon identifiers used by current token/NFT workflows. |
| `state` | Execution state. Check transaction state before parsing operation results. |

## Pagination

| Type | Fields |
| ---- | ------ |
| `Paginated<T>` | page/page-size style result data for older endpoints. |
| `CursorPaginatedResult<T>` | `result`, `cursor` for Carbon token/NFT inventory reads. |

Keep passing the returned cursor with the same filters until it is empty.

## Account And Balance Models

| Type | Fields |
| ---- | ------ |
| `Balance` | `chain`, `amount`, `symbol`, `decimals`, optional `ids`. |
| `Stake` | `amount`, `time`, `unclaimed`. |
| `Storage` | `available`, `used`, `avatar`, `archives`. |
| `AccountInfo` | `address`, `name`, `stake`. |
| `Account` | `address`, `name`, `stakes`, `stake`, `unclaimed`, optional `relay`, `validator`, `storage`, `balances`, optional `txs`. |
| `AccountTransactions` | `address`, `txs`. |

`AccountInfo` is the result of `getAccountInfo` and `getAccountInfos`. `name` is
the registered name, or `anonymous` when the address has none. Its `stake` field
carries the staking object. `Account` carries the same object under `stakes` and
uses `stake` for a deprecated flat scalar.

## Chain, Contract, And Organization Models

| Type | Fields |
| ---- | ------ |
| `Platform`, `Interop`, `Governance` | Nexus platform and governance metadata. |
| `Chain` | name, address, parent, height, organization, contracts, dapps. |
| `Nexus` | name, protocol, platforms, tokens, chains, governance, organizations. |
| `Organization` | id, name, members. |
| `Leaderboard`, `LeaderboardRow` | named leaderboard rows. |
| `ABIContract`, `ABIMethod`, `ABIEvent`, `ABIParameter` | Contract ABI structures. |

## Block, Transaction, Event, And Script Models

| Type | Fields |
| ---- | ------ |
| `RpcEvent`, `EventExtended`, `EventExtendedTyped` | Event address, contract, kind, data, and typed extension fields. `RpcEvent` also carries `name`. |
| `Oracle` | URL and content fields. |
| `SignatureResult` | signature kind and data. |
| `TransactionData` | `hash`, `chainAddress`, `timestamp`, `blockHeight`, `blockHash`, `script`, `payload`, `carbonTxType`, `carbonTxData`, `events`, optional `extendedEvents`, `result`, optional `debugComment`, `fee`, `state`, `signatures`, `sender`, `gasPayer`, `gasTarget`, `gasPrice`, `gasLimit`, `expiration`. |
| `Block` | `hash`, `previousHash`, `timestamp`, `height`, `chainAddress`, `protocol`, `txs`, `validatorAddress`, optional `producerAddress`, `reward`, optional `events`, optional `oracles`. |
| `Script` | `events`, `result`, `results`, `oracles`, optional `error`. |
| `VmValue` | A value decoded from VM storage: a scalar, an array or a struct. |

For a contract event, `kind` is `Custom_V2` and `name` is the event name the
contract declared. For every other event, `name` repeats `kind`.

Use `decodeVMObject` or `Decoder` helpers where a script result contains VM
object bytes.

`producerAddress` is the fee payout address the block producer stamped inside
the hashed block input. It is present on gas model v2 blocks and absent on
earlier ones. It is a different field from `validatorAddress`, which names the
consensus-log leader. The two are usually equal today, and a configurable payout
address is a planned extension, so do not assume they are equal.

`VmValue` is `string | VmValue[] | { [field: string]: VmValue }`. The wire
carries the plain JSON value, so the shape itself says which of the three it is.
Narrow it with `typeof value === 'string'` for a scalar and `Array.isArray` for
an array. Scalars are always strings, because chain numbers are big integers and
JSON numbers lose precision above 2^53. Byte values arrive as hex.

`EventExtendedTyped` is `EventExtended<ExtendedEventData>`, and
`ExtendedEventData` is the union of the typed payloads: `TokenCreateData`,
`TokenSeriesCreateData`, `MarketOrderData` and `SpecialResolutionData`. A
special resolution call carries its arguments typed per method.

## Token, NFT, Schema, And Price Models

| Type | Fields |
| ---- | ------ |
| `Token` | `symbol`, `name`, `decimals`, `currentSupply`, `maxSupply`, `burnedSupply`, `address`, `owner`, `flags`, optional `script`, `series`, `carbonId`, optional `metadata`, optional `tokenSchemas`, optional `external`, optional `price`. |
| `TokenData` / `NFT` | `id`, `series`, `carbonTokenId`, `carbonSeriesId`, `carbonNftAddress`, `mint`, `chainName`, `ownerAddress`, `creatorAddress`, `ram`, `rom`, `status`, `infusion`, `properties`. |
| `TokenSeries`, `TokenSeriesResult` | `seriesId`, `carbonTokenId`, `carbonSeriesId`, `ownerAddress`, `maxMint`, `mintCount`, `currentSupply`, `maxSupply`, optional `burnedSupply`, optional `mode`, optional `script`, optional `methods`, `metadata`. |
| `TokenSchemasResult`, `VmStructSchemaResult`, `VmVariableSchemaResult`, `VmNamedVariableSchemaResult` | RPC schema shape. |
| `TokenExternal`, `TokenPrice` | external mappings and price rows. |

Convert RPC schema payloads with `vmStructSchemaFromRpcResult` and
`vmVariableSchemaFromRpcResult` before passing them into Carbon schema builders.

## Fee And Gas Configuration Models

| Type | Fields |
| ---- | ------ |
| `GasConfigResult` | `gasModelVersion`, optional `gasConfig`, `blockRateTarget`, `expiryWindow`, optional `unitsPerBlockDataByte`. |
| `GasConfigData` | The JSON shape of the on-chain gas configuration. |
| `EstimateTransactionResult` | `wouldAbort`, optional `abortReason`, `gasBillKcalBase`, `dataRows`, `dataEscrowAtoms`, `dataRefundAtoms`, `recommendedMaxGas`, `recommendedMaxData`. |

`gasModelVersion` is `1` for the original fee model and `2` for gas model v2.
The fields of `GasConfigData` after `gasBurnRatioShift` exist only when
`GasConfigData.version` is 1 or higher. A gas model v1 response omits them.

64-bit values in both models arrive as decimal strings, because they can exceed
the 2^53 precision of a JSON number.

`gasConfigFromRpc(result)` converts a `GasConfigResult` into the `GasConfig` the
fee planner uses. It throws on a malformed numeric string, on a v2 response that
is missing its tail fields, and on a byte price this SDK does not implement.

`feeEstimateFromRpc(result)` converts a completed estimate into the same
`FeeQuote` a local plan produces. It throws when `wouldAbort` is set, because an
aborted simulation carries no recommendation.

## Auction, Archive, And Network Models

| Type | Use |
| ---- | --- |
| `Auction` | Marketplace listing data. |
| `Archive` | optional `name`, optional `hash`, `time`, `size`, optional `encryption`, `blockCount`, optional `missingBlocks`, optional `owners`. |
| `BuildInfoResult` | Node version, commit, and build time. |
| `PhantasmaVmConfig` | VM gas and deployment configuration values. |
| `Peer`, `Validator`, `Swap`, `Receipt`, `Channel`, `Dapp` | Explorer, status, and operational tooling data. |
