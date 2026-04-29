# Data Models (RPC DTOs) — All Models, Enriched
Parsed strictly from `PhantasmaAPI.h` (namespace `phantasma::rpc`). Comments shown only if meaningful. Where the context is clear, added short descriptions; otherwise left blank (no placeholders).

# ABIEvent
*Type:* `struct`

## Fields
- **value** — Numeric as string
  *type:* `Int32`
- **name** — String
  *type:* `String`
- **returnType**
  *type:* `String`
- **description**
  *type:* `String`

---

# ABIMethod
*Type:* `struct`

## Fields
- **name** — String
  *type:* `String`
- **returnType**
  *type:* `String`
- **parameters**
  *type:* `PHANTASMA_VECTOR<ABIParameter>`

---

# ABIParameter
*Type:* `struct`

## Fields
- **name** — String
  *type:* `String`
- **type**
  *type:* `String`

---

# Account
*Type:* `struct`

## Fields
- **address** — Account address (P2K...)
  *type:* `String`
- **name** — String
  *type:* `String`
- **stakes** — Stake info
  *type:* `Stake`
- **stake**
  *type:* `String`
- **unclaimed** — Unclaimed rewards/fees
  *type:* `String`
- **relay**
  *type:* `String`
- **validator**
  *type:* `String`
- **storage**
  *type:* `Storage`
- **balances** — Per-token balances
  *type:* `PHANTASMA_VECTOR<Balance>`
- **txs**
  *type:* `PHANTASMA_VECTOR<String>`

---

# AccountTransactions
*Type:* `struct`

## Fields
- **address** — Account address (P2K...)
  *type:* `String`
- **txs**
  *type:* `PHANTASMA_VECTOR<Transaction>`

---

# Archive
*Type:* `struct`

## Fields
- **name** — String
  *type:* `String`
- **hash** — Hex-encoded hash
  *type:* `String`
- **time** — Unix timestamp (seconds)
  *type:* `UInt32`
- **size**
  *type:* `UInt32`
- **encryption**
  *type:* `String`
- **blockCount**
  *type:* `Int32`
- **missingBlocks**
  *type:* `PHANTASMA_VECTOR<Int32>`
- **owners**
  *type:* `PHANTASMA_VECTOR<String>`

---

# Auction
*Type:* `struct`

## Fields
- **creatorAddress**
  *type:* `String`
- **chainAddress**
  *type:* `String`
- **startDate** — Auction start/end timestamp
  *type:* `UInt32`
- **endDate** — Auction start/end timestamp
  *type:* `UInt32`
- **baseSymbol**
  *type:* `String`
- **quoteSymbol**
  *type:* `String`
- **tokenId** — Identifier
  *type:* `String`
- **price** — Numeric as string
  *type:* `String`
- **rom**
  *type:* `String`
- **ram**
  *type:* `String`

---

# Balance
*Type:* `struct`

## Fields
- **chain** — Chain name
  *type:* `String`
- **amount** — Numeric as string
  *type:* `String`
- **symbol** — String
  *type:* `String`
- **decimals** — Token decimals
  *type:* `UInt32`
- **ids** — NFT IDs owned for this symbol on the chain
  *type:* `PHANTASMA_VECTOR<String>`

---

# VmVariableSchemaResult
*Type:* `struct`

## Fields
- **type**
  *type:* `String`
- **schema**
  *type:* `std::shared_ptr<VmStructSchemaResult>`

---

# VmNamedVariableSchemaResult
*Type:* `struct`

## Fields
- **name**
  *type:* `String`
- **schema**
  *type:* `VmVariableSchemaResult`

---

# VmStructSchemaResult
*Type:* `struct`

## Fields
- **fields**
  *type:* `PHANTASMA_VECTOR<VmNamedVariableSchemaResult>`
- **flags**
  *type:* `Int32`

---

# TokenSchemas
*Type:* `struct`

## Fields
- **seriesMetadata**
  *type:* `VmStructSchemaResult`
- **rom**
  *type:* `VmStructSchemaResult`
- **ram**
  *type:* `VmStructSchemaResult`

---

# Block
*Type:* `struct`

## Fields
- **hash** — Hex-encoded hash
  *type:* `String`
- **previousHash**
  *type:* `String`
- **timestamp** — Unix timestamp (seconds)
  *type:* `UInt32`
- **height** — Block or chain height
  *type:* `UInt32`
- **chainAddress**
  *type:* `String`
- **protocol**
  *type:* `UInt32`
- **txs**
  *type:* `PHANTASMA_VECTOR<Transaction>`
- **validatorAddress**
  *type:* `String`
- **reward**
  *type:* `String`
- **events**
  *type:* `PHANTASMA_VECTOR<Event>`
- **oracles**
  *type:* `PHANTASMA_VECTOR<Oracle>`

---

# Chain
*Type:* `struct`

## Fields
- **name** — String
  *type:* `String`
- **address** — Account address (P2K...)
  *type:* `String`
- **parent**
  *type:* `String`
- **height** — Block or chain height
  *type:* `UInt32`
- **organization**
  *type:* `String`
- **contracts**
  *type:* `PHANTASMA_VECTOR<String>`
- **dapps**
  *type:* `PHANTASMA_VECTOR<String>`

---

# Channel
*Type:* `struct`

## Fields
- **creatorAddress**
  *type:* `String`
- **targetAddress**
  *type:* `String`
- **name** — String
  *type:* `String`
- **chain**
  *type:* `String`
- **creationTime**
  *type:* `UInt32`
- **symbol** — String
  *type:* `String`
- **fee**
  *type:* `String`
- **balance** — Numeric as string
  *type:* `String`
- **active**
  *type:* `bool`
- **index**
  *type:* `Int32`

---

# Contract
*Type:* `struct`

## Fields
- **name** — String
  *type:* `String`
- **address** — Account address (P2K...)
  *type:* `String`
- **script**
  *type:* `String`
- **methods**
  *type:* `PHANTASMA_VECTOR<ABIMethod>`
- **events**
  *type:* `PHANTASMA_VECTOR<ABIEvent>`

---

# Dapp
*Type:* `struct`

## Fields
- **name** — String
  *type:* `String`
- **address** — Account address (P2K...)
  *type:* `String`
- **chain**
  *type:* `String`

---

# Event
*Type:* `struct`

## Fields
- **address** — Account address (P2K...)
  *type:* `String`
- **contract** — String
  *type:* `String`
- **kind**
  *type:* `String`
- **name**
  *type:* `String`
- **data** — Event payload (hex)
  *type:* `String`

---

# TokenCreateData
*Type:* `struct`

## Fields
- **symbol**
  *type:* `String`
- **maxSupply**
  *type:* `String`
- **decimals**
  *type:* `UInt32`
- **isNonFungible**
  *type:* `bool`
- **carbonTokenId**
  *type:* `UInt64`
- **metadata**
  *type:* `PHANTASMA_MAP<String, String>`

---

# TokenSeriesCreateData
*Type:* `struct`

## Fields
- **symbol**
  *type:* `String`
- **seriesId**
  *type:* `String`
- **maxMint**
  *type:* `UInt32`
- **maxSupply**
  *type:* `UInt32`
- **owner**
  *type:* `String`
- **carbonTokenId**
  *type:* `UInt64`
- **carbonSeriesId**
  *type:* `UInt32`
- **metadata**
  *type:* `PHANTASMA_MAP<String, String>`

---

# TokenMintData
*Type:* `struct`

## Fields
- **symbol**
  *type:* `String`
- **tokenId**
  *type:* `String`
- **seriesId**
  *type:* `String`
- **mintNumber**
  *type:* `UInt32`
- **carbonTokenId**
  *type:* `UInt64`
- **carbonSeriesId**
  *type:* `UInt32`
- **carbonInstanceId**
  *type:* `UInt64`
- **owner**
  *type:* `String`
- **metadata**
  *type:* `PHANTASMA_MAP<String, String>`

---

# MarketOrderData
*Type:* `struct`

## Fields
- **baseSymbol**
  *type:* `String`
- **quoteSymbol**
  *type:* `String`
- **tokenId**
  *type:* `String`
- **carbonBaseTokenId**
  *type:* `UInt64`
- **carbonQuoteTokenId**
  *type:* `UInt64`
- **carbonInstanceId**
  *type:* `UInt64`
- **seller**
  *type:* `String`
- **buyer**
  *type:* `String`
- **price**
  *type:* `String`
- **endPrice**
  *type:* `String`
- **startDate**
  *type:* `Int64`
- **endDate**
  *type:* `Int64`
- **type**
  *type:* `String`

---

# SpecialResolutionCall
*Type:* `struct`

## Fields
- **moduleId**
  *type:* `UInt32`
- **module**
  *type:* `String`
- **methodId**
  *type:* `UInt32`
- **method**
  *type:* `String`
- **arguments**
  *type:* `PHANTASMA_MAP<String, String>`
- **calls**
  *type:* `PHANTASMA_VECTOR<SpecialResolutionCall>`

---

# SpecialResolutionData
*Type:* `struct`

## Fields
- **resolutionId**
  *type:* `UInt64`
- **description**
  *type:* `String`
- **calls**
  *type:* `PHANTASMA_VECTOR<SpecialResolutionCall>`

---

# EventExtended
*Type:* `struct`

`type` uses `ExtendedEventType`: `Unknown`, `TokenCreate`, `TokenSeriesCreate`, `TokenMint`, `MarketOrder`, or `SpecialResolution`.

## Fields
- **address**
  *type:* `String`
- **contract**
  *type:* `String`
- **kind**
  *type:* `String`
- **type**
  *type:* `ExtendedEventType`
- **tokenCreate**
  *type:* `TokenCreateData`
- **tokenSeriesCreate**
  *type:* `TokenSeriesCreateData`
- **tokenMint**
  *type:* `TokenMintData`
- **marketOrder**
  *type:* `MarketOrderData`
- **specialResolution**
  *type:* `SpecialResolutionData`

---

# Governance
*Type:* `struct`

## Fields
- **name** — String
  *type:* `String`
- **value** — Numeric as string
  *type:* `String`

---

# Interop
*Type:* `struct`

## Fields
- **local**
  *type:* `String`
- **external**
  *type:* `String`

---

# Leaderboard
*Type:* `struct`

## Fields
- **name** — String
  *type:* `String`
- **rows**
  *type:* `PHANTASMA_VECTOR<LeaderboardRow>`

---

# LeaderboardRow
*Type:* `struct`

## Fields
- **address** — Account address (P2K...)
  *type:* `String`
- **value** — Numeric as string
  *type:* `String`

---

# Nexus
*Type:* `struct`

## Fields
- **name** — String
  *type:* `String`
- **platforms** — Interop platforms registered in the nexus
  *type:* `PHANTASMA_VECTOR<Platform>`
- **tokens** — Deployed tokens
  *type:* `PHANTASMA_VECTOR<Token>`
- **chains** — Chains in the nexus
  *type:* `PHANTASMA_VECTOR<Chain>`
- **governance**
  *type:* `PHANTASMA_VECTOR<Governance>`
- **organizations**
  *type:* `PHANTASMA_VECTOR<String>`

---

# Oracle
*Type:* `struct`

## Fields
- **url**
  *type:* `String`
- **content**
  *type:* `String`

---

# Organization
*Type:* `struct`

## Fields
- **id** — Identifier
  *type:* `String`
- **name** — String
  *type:* `String`
- **members**
  *type:* `PHANTASMA_VECTOR<String>`

---

# Paginated
*Type:* `struct`

## Fields
- **page**
  *type:* `UInt32`
- **pageSize**
  *type:* `UInt32`
- **total**
  *type:* `UInt32`
- **totalPages**
  *type:* `UInt32`
- **result**
  *type:* `JSONValue`

---

# CursorPaginatedResult
*Type:* `template<class T> struct`

## Fields
- **result**
  *type:* `PHANTASMA_VECTOR<T>`
- **cursor**
  *type:* `String`

---

# Peer
*Type:* `struct`

## Fields
- **url**
  *type:* `String`
- **version**
  *type:* `String`
- **flags**
  *type:* `String`
- **fee**
  *type:* `String`
- **pow**
  *type:* `UInt32`

---

# PhantasmaError
*Type:* `struct`

## Fields
- **code**
  *type:* `int`
- **message**
  *type:* `String`

Static error codes: `InvalidJSON = -1`, `HttpError = -2`, `InvalidRpcResponse = -3`, `RpcMessage = -4`.

---

# Platform
*Type:* `struct`

## Fields
- **platform**
  *type:* `String`
- **chain**
  *type:* `String`
- **fuel**
  *type:* `String`
- **tokens**
  *type:* `PHANTASMA_VECTOR<String>`
- **interop**
  *type:* `PHANTASMA_VECTOR<Interop>`

---

# Receipt
*Type:* `struct`

## Fields
- **nexus**
  *type:* `String`
- **channel**
  *type:* `String`
- **index**
  *type:* `String`
- **timestamp** — Unix timestamp (seconds)
  *type:* `UInt32`
- **sender**
  *type:* `String`
- **receiver**
  *type:* `String`
- **script**
  *type:* `String`

---

# Script
*Type:* `struct`

## Fields
- **events**
  *type:* `PHANTASMA_VECTOR<Event>`
- **result**
  *type:* `String`
- **results**
  *type:* `PHANTASMA_VECTOR<String>`
- **oracles**
  *type:* `PHANTASMA_VECTOR<Oracle>`

---

# SendRawTx
*Type:* `struct`

## Fields
- **hash** — Hex-encoded hash
  *type:* `String`
- **error**
  *type:* `String`

---

# SendCarbonTx
*Type:* `struct`

## Fields
- **hash** — Hex-encoded hash
  *type:* `String`
- **error**
  *type:* `String`

---

# Signature
*Type:* `struct`

## Fields
- **Kind**
  *type:* `String`
- **Data**
  *type:* `String`

---

# Stake
*Type:* `struct`

## Fields
- **amount** — Numeric as string
  *type:* `String`
- **time** — Unix timestamp (seconds)
  *type:* `UInt32`
- **unclaimed**
  *type:* `String`

---

# Storage
*Type:* `struct`

## Fields
- **available**
  *type:* `UInt32`
- **used**
  *type:* `UInt32`
- **avatar**
  *type:* `String`
- **archives**
  *type:* `PHANTASMA_VECTOR<Archive>`

---

# Swap
*Type:* `struct`

## Fields
- **sourcePlatform** — Cross-chain platform names
  *type:* `String`
- **sourceChain**
  *type:* `String`
- **sourceHash**
  *type:* `String`
- **sourceAddress**
  *type:* `String`
- **destinationPlatform**
  *type:* `String`
- **destinationChain**
  *type:* `String`
- **destinationHash**
  *type:* `String`
- **destinationAddress**
  *type:* `String`
- **symbol** — String
  *type:* `String`
- **value** — Numeric as string
  *type:* `String`

---

# Token
*Type:* `struct`

## Fields
- **symbol** — String
  *type:* `String`
- **name** — String
  *type:* `String`
- **decimals** — Token decimals
  *type:* `Int32`
- **currentSupply** — Numeric as string
  *type:* `String`
- **maxSupply** — Numeric as string
  *type:* `String`
- **carbonId**
  *type:* `String`
- **burnedSupply**
  *type:* `String`
- **address** — Account address (P2K...)
  *type:* `String`
- **owner** — Account address (P2K...)
  *type:* `String`
- **flags** — Token flags (fungible, transferable, etc.)
  *type:* `String`
- **script**
  *type:* `String`
- **series**
  *type:* `PHANTASMA_VECTOR<TokenSeries>`
- **metadata**
  *type:* `PHANTASMA_VECTOR<TokenProperty>`
- **tokenSchemas**
  *type:* `TokenSchemas`

---

# TokenData
*Type:* `struct`

## Fields
- **ID** — Identifier
  *type:* `String`
- **series**
  *type:* `String`
- **mint**
  *type:* `String`
- **chainName**
  *type:* `String`
- **ownerAddress**
  *type:* `String`
- **creatorAddress**
  *type:* `String`
- **ram**
  *type:* `String`
- **rom**
  *type:* `String`
- **status**
  *type:* `String`
- **infusion**
  *type:* `PHANTASMA_VECTOR<TokenProperty>`
- **properties**
  *type:* `PHANTASMA_VECTOR<TokenProperty>`

---

# TokenProperty
*Type:* `struct`

## Fields
- **Key**
  *type:* `String`
- **Value** — Numeric as string
  *type:* `String`

---

# TokenSeries
*Type:* `struct`

## Fields
- **seriesID** — Identifier
  *type:* `UInt32`
- **currentSupply** — Numeric as string
  *type:* `String`
- **maxSupply** — Numeric as string
  *type:* `String`
- **burnedSupply**
  *type:* `String`
- **mode**
  *type:* `TokenSeriesMode`
- **carbonTokenId**
  *type:* `String`
- **carbonSeriesId**
  *type:* `String`
- **script**
  *type:* `String`
- **methods**
  *type:* `PHANTASMA_VECTOR<ABIMethod>`
- **metadata**
  *type:* `PHANTASMA_VECTOR<TokenProperty>`

---

# BuildInfoResult
*Type:* `struct`

## Fields
- **version**
  *type:* `String`
- **commit**
  *type:* `String`
- **buildTimeUtc**
  *type:* `String`

---

# PhantasmaVmConfig
*Type:* `struct`

## Fields
- **isStored**
  *type:* `bool`
- **featureLevel**
  *type:* `Int32`
- **gasConstructor**
  *type:* `String`
- **gasNexus**
  *type:* `String`
- **gasOrganization**
  *type:* `String`
- **gasAccount**
  *type:* `String`
- **gasLeaderboard**
  *type:* `String`
- **gasStandard**
  *type:* `String`
- **gasOracle**
  *type:* `String`
- **fuelPerContractDeploy**
  *type:* `String`

---

# Transaction
*Type:* `struct`

## Fields
- **hash** — Hex-encoded hash
  *type:* `String`
- **chainAddress**
  *type:* `String`
- **timestamp** — Unix timestamp (seconds)
  *type:* `UInt32`
- **blockHeight**
  *type:* `Int32`
- **blockHash**
  *type:* `String`
- **script** — Raw script (hex)
  *type:* `String`
- **payload** — Opaque payload (hex)
  *type:* `String`
- **events**
  *type:* `PHANTASMA_VECTOR<Event>`
- **extendedEvents**
  *type:* `PHANTASMA_VECTOR<EventExtended>`
- **result**
  *type:* `String`
- **debugComment**
  *type:* `String`
- **fee**
  *type:* `String`
- **signatures** — Attached signatures
  *type:* `PHANTASMA_VECTOR<Signature>`
- **expiration**
  *type:* `UInt32`
- **state**
  *type:* `String`
- **sender**
  *type:* `String`
- **gasPayer**
  *type:* `String`
- **gasTarget**
  *type:* `String`
- **gasPrice**
  *type:* `String`
- **gasLimit**
  *type:* `String`

---

# Validator
*Type:* `struct`

## Fields
- **address** — Account address (P2K...)
  *type:* `String`
- **type**
  *type:* `String`

---
