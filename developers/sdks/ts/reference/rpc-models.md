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
| `Account` | `address`, `name`, `stakes`, `stake`, `unclaimed`, optional `relay`, `validator`, `storage`, `balances`, optional `txs`. |
| `AccountTransactions` | `address`, `txs`. |

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
| `RpcEvent`, `EventExtended`, `EventExtendedTyped` | Event address, contract, kind, data, and typed extension fields. |
| `Oracle` | URL and content fields. |
| `SignatureResult` | signature kind and data. |
| `TransactionData` | `hash`, `chainAddress`, `timestamp`, `blockHeight`, `blockHash`, `script`, `payload`, `carbonTxType`, `carbonTxData`, `events`, optional `extendedEvents`, `result`, optional `debugComment`, `fee`, `state`, `signatures`, `sender`, `gasPayer`, `gasTarget`, `gasPrice`, `gasLimit`, `expiration`. |
| `Block` | `hash`, `previousHash`, `timestamp`, `height`, `chainAddress`, `protocol`, `txs`, `validatorAddress`, `reward`, optional `events`, optional `oracles`. |
| `Script` | `events`, `result`, `results`, `oracles`, optional `error`. |

Use `decodeVMObject` or `Decoder` helpers where a script result contains VM
object bytes.

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

## Auction, Archive, And Network Models

| Type | Use |
| ---- | --- |
| `Auction` | Marketplace listing data. |
| `Archive` | optional `name`, optional `hash`, `time`, `size`, optional `encryption`, `blockCount`, optional `missingBlocks`, optional `owners`. |
| `BuildInfoResult` | Node version, commit, and build time. |
| `PhantasmaVmConfig` | VM gas and deployment configuration values. |
| `Peer`, `Validator`, `Swap`, `Receipt`, `Channel`, `Dapp` | Explorer, status, and operational tooling data. |
