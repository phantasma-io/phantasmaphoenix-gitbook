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
| `Balance` | chain, amount, symbol, decimals, ids. |
| `Stake` | amount, time, unclaimed. |
| `Storage` | available, used, avatar, archives. |
| `Account` | address, name, stake/stakes, relay, validator, storage, balances. |
| `AccountTransactions` | address and transaction rows. |

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
| `TransactionData` | hash, chain address, timestamp, block position, script, payload, events, state, result, fee, signatures, expiration. |
| `Block` | hash, previous hash, timestamp, height, chain address, protocol, transactions, validator, reward, events, oracles. |
| `Script` | read-only VM invocation result fields. |

Use `decodeVMObject` or `Decoder` helpers where a script result contains VM
object bytes.

## Token, NFT, Schema, And Price Models

| Type | Fields |
| ---- | ------ |
| `Token` | token definition, flags, supplies, owner, script, series, Carbon id, metadata, schemas, external mappings, prices. |
| `TokenData` / `NFT` | NFT id, series, Carbon ids, owner/creator, ROM, RAM, status, infusion, properties. |
| `TokenSeries`, `TokenSeriesResult` | series identifiers, owner, supplies, mode, methods, metadata. |
| `TokenSchemasResult`, `VmStructSchemaResult`, `VmVariableSchemaResult`, `VmNamedVariableSchemaResult` | RPC schema shape. |
| `TokenExternal`, `TokenPrice` | external mappings and price rows. |

Convert RPC schema payloads with `vmStructSchemaFromRpcResult` and
`vmVariableSchemaFromRpcResult` before passing them into Carbon schema builders.

## Auction, Archive, And Network Models

| Type | Use |
| ---- | --- |
| `Auction` | Marketplace listing data. |
| `Archive` | Storage archive metadata. |
| `BuildInfoResult` | Node version, commit, and build time. |
| `PhantasmaVmConfig` | VM gas and deployment configuration values. |
| `Peer`, `Validator`, `Swap`, `Receipt`, `Channel`, `Dapp` | Explorer, status, and operational tooling data. |
