# Node RPC Models

The objects that the [methods](methods.md) return, with their fields as they appear in the JSON answer. A field whose value is null is left out. Amounts are integer strings in the smallest unit of their token. Hashes and binary data are hexadecimal strings.

## ABIEventResult

An event that a contract declares in its ABI.

| Field | Type | Description |
| --- | --- | --- |
| `value` | number | The event kind number. |
| `name` | string | The event name. |
| `returnType` | string | The type of the event data, a VM type name such as `Number`, `String`, `Bytes`, or `None`. |
| `description` | string | The description script of the event, in hexadecimal. |

## ABIMethodResult

A method that a contract declares in its ABI.

| Field | Type | Description |
| --- | --- | --- |
| `name` | string | The method name. |
| `returnType` | string | The return type, a VM type name such as `Number`, `String`, `Bytes`, `Bool`, `Timestamp`, `Struct`, or `None`. |
| `parameters` | array of [`ABIParameterResult`](#abiparameterresult) | The parameters, in order. |

## ABIParameterResult

A parameter of a contract method.

| Field | Type | Description |
| --- | --- | --- |
| `name` | string | The parameter name. |
| `type` | string | The parameter type, a VM type name. |

## AccountInfoResult

The registered name and the SOUL stake of an address. `getAccountInfo` and `getAccountInfos` return it.

| Field | Type | Description |
| --- | --- | --- |
| `address` | string | The address, as given in the request; for a `Carbon` request, its Phantasma form. |
| `name` | string | The registered name, or `anonymous`. |
| `stake` | [`StakeResult`](#stakeresult) | The SOUL stake. All zero when the address does not stake. |

## AccountResult

The name, the stake, and the balances of an address. The deprecated `getAccount` and `getAccounts` return it.

| Field | Type | Description |
| --- | --- | --- |
| `address` | string | The address, as given in the request. |
| `name` | string | The registered name, or `anonymous`. |
| `stakes` | [`StakeResult`](#stakeresult) | The SOUL stake. |
| `stake` | string | The staked SOUL, the same value as `stakes.amount`. |
| `unclaimed` | string | The KCAL earned and not yet claimed, the same value as `stakes.unclaimed`. |
| `relay` | string | Not filled by the node. |
| `validator` | string | Always `Invalid`. |
| `storage` | [`StorageResult`](#storageresult) | Always empty. |
| `balances` | array of [`BalanceResult`](#balanceresult) | Every token balance of the address, staked SOUL excluded. |
| `txs` | array of string | Not filled by the node. |

## AccountTransactionsResult

The transactions of an address, the `result` of a `getAddressTransactions` page.

| Field | Type | Description |
| --- | --- | --- |
| `address` | string | The address, as given in the request. |
| `txs` | array of [`TransactionResult`](#transactionresult) | The transactions of the page, newest first. |

## ArchiveResult

The node answers this object with every field empty.

## AuctionResult

A market listing that sells one NFT at a fixed price.

| Field | Type | Description |
| --- | --- | --- |
| `creatorAddress` | string | The seller. |
| `chainAddress` | string | The main chain address, `S3d7TbZxtNPdXy11hfmBLJLYn67gZTG2ibL7fJBcVdihWU4`. |
| `startDate` | number | When the listing started, in Unix seconds. |
| `endDate` | number | When the listing ends, in Unix seconds. |
| `baseSymbol` | string | The symbol of the NFT token. |
| `quoteSymbol` | string | The symbol of the token the price is paid in. |
| `tokenId` | string | The NFT id. |
| `price` | string | The price, in the smallest unit of the quote token. |
| `endPrice` | string | Always `0`. |
| `extensionPeriod` | string | Always `0`. |
| `type` | string | Always `Fixed`. |
| `rom` | string | The ROM of the NFT, in hexadecimal. |
| `ram` | string | The RAM of the NFT, in hexadecimal. |
| `listingFee` | string | Always `0`. |
| `currentWinner` | string | Always empty. |

## BalanceResult

The balance of one token held by an address.

| Field | Type | Description |
| --- | --- | --- |
| `chain` | string | The chain: `main` from `getAccountFungibleTokens`, the main chain address `S3d7TbZxtNPdXy11hfmBLJLYn67gZTG2ibL7fJBcVdihWU4` from `getTokenBalance`, `getAccount`, and `getAccounts`. |
| `amount` | string | The balance in the smallest unit of the token; for an NFT token, the number of NFTs. |
| `symbol` | string | The token symbol. |
| `decimals` | number | The decimals of the token. |
| `ids` | array of string | For an NFT token, at most 10,000 of the NFT ids the address holds. Not present for a fungible token. |

## BlockResult

A block and its transactions.

| Field | Type | Description |
| --- | --- | --- |
| `hash` | string | The block hash. |
| `previousHash` | string | The hash of the block before. |
| `timestamp` | number | The block time, in Unix seconds. |
| `height` | number | The block height. |
| `chainAddress` | string | The main chain address, `S3d7TbZxtNPdXy11hfmBLJLYn67gZTG2ibL7fJBcVdihWU4`. |
| `protocol` | number | The protocol version number, `19` on current blocks. |
| `txs` | array of [`TransactionResult`](#transactionresult) | The transactions of the block, in block order. |
| `validatorAddress` | string | The validator that produced the block. |
| `producerAddress` | string | The payout address of the block producer, written into the block. Present on blocks produced under gas model v2. See [Block Producers](/about/economy/block-producer.md). |
| `reward` | string | `0` on current blocks. |
| `events` | array of [`EventResult`](#eventresult) | The block events of a block from before Phantasma Phoenix. |
| `oracles` | array of [`OracleResult`](#oracleresult) | The oracle reads of a block from before Phantasma Phoenix. |

## BuildInfoResult

The build of the RPC node software.

| Field | Type | Description |
| --- | --- | --- |
| `version` | string | The version of the RPC node software. |
| `commit` | string | The Git commit of the build. |
| `buildTimeUtc` | string | The build time, in UTC. |

## ChainResult

The node answers this object with every field empty.

## ContractResult

A deployed contract.

| Field | Type | Description |
| --- | --- | --- |
| `name` | string | The contract name. |
| `address` | string | The contract address. |
| `script` | string | The contract bytecode, in hexadecimal. Empty when `getContracts` is called without `extended`. |
| `owner` | string | Not filled by the node. |
| `methods` | array of [`ABIMethodResult`](#abimethodresult) | The methods of the contract ABI. |
| `events` | array of [`ABIEventResult`](#abieventresult) | The events of the contract ABI. |

## CursorPaginatedResult

One page of a list read by cursor. Pass `cursor` back with the same filters to read the next page. The last page carries no `cursor`.

| Field | Type | Description |
| --- | --- | --- |
| `result` | see the method | The entries of the page. |
| `cursor` | string | The cursor of the next page. Not present on the last page. |

## EstimateTransactionResult

The outcome of a dry run of a transaction. See [Fee Estimation](/developers/blockchain/chain/fees-and-gas.md#fee-estimation).

| Field | Type | Description |
| --- | --- | --- |
| `wouldAbort` | boolean | `true` when the transaction would be rejected or would abort. |
| `abortReason` | string | The reason when `wouldAbort` is `true`; empty otherwise. |
| `gasBillKcalBase` | string | The gas bill in KCAL atoms, after the minimum bill and the `maxGas` cap. |
| `dataRows` | string | The storage quanta the transaction would add. |
| `dataEscrowAtoms` | string | The storage escrow it would pay, in SOUL atoms. |
| `dataRefundAtoms` | string | The storage escrow it would get back, in SOUL atoms. |
| `recommendedMaxGas` | string | The bill plus 15%, rounded up, and at least the minimum gas offer and the minimum gas bill. `0` when `wouldAbort` is `true`. |
| `recommendedMaxData` | string | The net escrow plus 15%, rounded up to a multiple of `dataEscrowPerRow`. `0` when `wouldAbort` is `true` or when the transaction adds no net storage. |

## EventExResult

An event with its data decoded into a JSON object, for the event kinds that the node decodes.

| Field | Type | Description |
| --- | --- | --- |
| `address` | string | The address the event refers to. |
| `contract` | string | The contract or chain module that emitted the event, such as `market` or `governance`. |
| `kind` | string, the event kind | The event kind. |
| `data` | any JSON value | The event data as a JSON object; its fields depend on the kind. |

## EventResult

An event that a transaction emitted.

| Field | Type | Description |
| --- | --- | --- |
| `address` | string | The address the event refers to, such as the sender of a `TokenSend` or the recipient of a `TokenReceive`. |
| `contract` | string | The contract or chain module that emitted the event. |
| `kind` | string | The event kind, such as `TokenSend`, `TokenReceive`, `TokenMint`, `GasEscrow`, or `GasPayment`. |
| `name` | string | The name of a custom event; the kind for the other events. |
| `data` | string | The event data, serialized, in hexadecimal; its layout depends on the kind. |

## ExecutionState

The outcome of a transaction.

| Value | Meaning |
| --- | --- |
| `Halt` | The transaction completed. |
| `Break` | The transaction aborted. It changed nothing, and the fee payer paid the gas bill. |
| `Fault` | The chain rejected the transaction. |
| `Running` | The transaction is not final yet. |

## GasConfigDataResult

The gas configuration fields. [Fees And Gas](/developers/blockchain/chain/fees-and-gas.md#the-gas-configuration) explains each one.

| Field | Type | Description |
| --- | --- | --- |
| `version` | number | `1` or higher under gas model v2. |
| `maxNameLength` | number | The longest account name. |
| `maxTokenSymbolLength` | number | The longest token symbol. |
| `feeShift` | number | The right shift after the fee multiplier. |
| `maxStructureSize` | number | The largest structure the chain accepts, in bytes. |
| `feeMultiplier` | string | The KCAL atoms per gas unit, before `feeShift`. |
| `gasTokenId` | string | The Carbon token id of the gas token, `1` (KCAL). |
| `dataTokenId` | string | The Carbon token id of the storage escrow token, `2` (SOUL). |
| `minimumGasOffer` | string | The smallest `maxGas` a transaction may state, in KCAL atoms. |
| `dataEscrowPerRow` | string | The SOUL atoms escrowed per 1024-byte storage quantum. |
| `gasFeeTransfer` | string | The gas units of a transfer and of most native writes. |
| `gasFeeQuery` | string | The gas units of a native read. |
| `gasFeeCreateTokenBase` | string | A price of gas model v1. Not used under gas model v2. |
| `gasFeeCreateTokenSymbol` | string | A price of gas model v1. Not used under gas model v2. |
| `gasFeeCreateTokenSeries` | string | A price of gas model v1. Not used under gas model v2. |
| `gasFeePerByte` | string | A price of gas model v1. Not used under gas model v2. |
| `gasFeeRegisterName` | string | A price of gas model v1. Not used under gas model v2. |
| `gasBurnRatioMul` | string | The multiplier of the burned share of each bill. |
| `gasBurnRatioShift` | number | The right shift of the burned share of each bill. |
| `minimumGasBill` | string | The smallest settled bill, in KCAL atoms. |
| `gasProducerRatioMul` | string | The multiplier of the block producer share of each bill. |
| `gasProducerRatioShift` | number | The right shift of the block producer share of each bill. |
| `gasDappRatioMul` | string | The multiplier of the dApp share of each bill. |
| `gasDappRatioShift` | number | The right shift of the dApp share of each bill. |
| `policyFeeCreateTokenBase` | string | The token creation fee, in KCAL atoms. |
| `policyFeeCreateTokenSymbol` | string | The symbol fee of a token creation, in KCAL atoms, halved for every character after the first. |
| `policyFeeCreateTokenSeries` | string | The series creation fee, in KCAL atoms. |
| `policyFeeRegisterName` | string | The name registration fee, in KCAL atoms, halved for every character after the first. |
| `legacyDataEscrowPerRow` | string | The refund per quantum of the storage that existed before gas model v2, in SOUL atoms. |

## GasConfigResult

The gas configuration of the latest block and the chain parameters that fee calculation needs.

| Field | Type | Description |
| --- | --- | --- |
| `gasModelVersion` | number | `2` when `gasConfig.version` is `1` or higher, otherwise `1`. |
| `gasConfig` | [`GasConfigDataResult`](#gasconfigdataresult) | The gas configuration. |
| `blockRateTarget` | number | The target time between blocks, in milliseconds. |
| `expiryWindow` | number | How far in the future a transaction's expiry may lie, in milliseconds. |
| `unitsPerBlockDataByte` | number | The gas units per byte of block data, `25`. Present under gas model v2. |

## GovernanceResult

The node answers this object with every field empty.

## LeaderboardResult

The node answers this object with every field empty.

## LeaderboardRowResult

The node answers this object with every field empty.

## NexusResult

The node answers this object with every field empty.

## OracleResult

An oracle read of a block from before Phantasma Phoenix.

| Field | Type | Description |
| --- | --- | --- |
| `url` | string | The URL the oracle read. |
| `content` | string | The content it read, in hexadecimal. |

## OrganizationMemberResult

The membership of one address in an organization.

| Field | Type | Description |
| --- | --- | --- |
| `address` | string | The address, in Phantasma form. |
| `carbonAddress` | string | The 32-byte account key, in hexadecimal. |
| `isMember` | boolean | Whether the address is a member. |
| `memberTime` | number | When the address joined, in Unix milliseconds. Present for a member when the request asks for it. |

## OrganizationResult

An organization, such as `masters`.

| Field | Type | Description |
| --- | --- | --- |
| `name` | string | The organization name. |
| `owner` | string | The owner, in Phantasma form. |
| `carbonOwner` | string | The owner's 32-byte account key, in hexadecimal. |
| `metadata` | array of [`TokenPropertyResult`](#tokenpropertyresult) | The organization metadata. |
| `memberCount` | string | The number of members. Present when the request asks for it. |

## PaginatedResult

One page of a list read by page number.

| Field | Type | Description |
| --- | --- | --- |
| `page` | number | The page number. |
| `pageSize` | number | The page size. |
| `total` | number | The number of entries in all pages. |
| `totalPages` | number | The number of pages. |
| `result` | see the method | The entries of the page. |

## PhantasmaVmConfigResult

The configuration of the Phantasma VM.

| Field | Type | Description |
| --- | --- | --- |
| `isStored` | boolean | `true` when the configuration is stored on the chain; `false` when the validators use the built-in defaults. |
| `featureLevel` | number | The feature level of the Phantasma VM. |
| `gasConstructor` | string | The gas units of `ABI()`, `Address()`, `Hash()`, and `Timestamp()`. |
| `gasNexus` | string | The gas units of `Nexus.CreateToken`, `Nexus.CreateTokenSeries`, `Nexus.AttachTokenContract`, and `Nexus.SetPlatformTokenHash`. |
| `gasOrganization` | string | The gas units of `Organization.Kill`. |
| `gasAccount` | string | The gas units of `Account.Name` and `Account.Transactions`. |
| `gasLeaderboard` | string | Stored in the configuration; no interop charges it. |
| `gasStandard` | string | The gas units of every other interop. |
| `gasOracle` | string | The gas units of `Oracle.Quote`. |
| `fuelPerContractDeploy` | string | Stored in the configuration; the chain does not charge it. |

## ScriptResult

The outcome of a script run by `invokeRawScript`.

| Field | Type | Description |
| --- | --- | --- |
| `events` | array of [`EventResult`](#eventresult) | The events the script emitted. |
| `result` | string | The last value the script left on the stack, serialized, in hexadecimal. Empty when the script failed. |
| `error` | string | Empty when the script completed; otherwise the failure reason. |
| `results` | array of string | Every value the script left on the stack, serialized, in hexadecimal, the last one at the end. |
| `oracles` | array of [`OracleResult`](#oracleresult) | Always empty. |
| `state` | string | Not filled by the node. |
| `gas` | string | Not filled by the node. |

## StakeResult

The SOUL stake of an address.

| Field | Type | Description |
| --- | --- | --- |
| `amount` | string | The staked SOUL, in SOUL atoms. |
| `time` | number | The staking timestamp, in Unix seconds. Stake, unstake, and claim each set it. |
| `unclaimed` | string | The KCAL earned and not yet claimed, in KCAL atoms, boosters included. |

## StorageResult

The node answers this object with every field empty.

## TokenDataResult

An NFT.

| Field | Type | Description |
| --- | --- | --- |
| `id` | string | The Phantasma NFT id, in decimal. |
| `series` | string | The Phantasma series id, in decimal; `0` when the series has none. |
| `carbonTokenId` | string | The Carbon token id. |
| `carbonSeriesId` | string | The Carbon series id. |
| `carbonNftAddress` | string | The 32-byte address of the NFT, in hexadecimal. Assets sent to it are infused into the NFT. |
| `mint` | string | The mint number within the series. |
| `chainName` | string | Always `main`. |
| `ownerAddress` | string | The current owner. When the NFT is infused into another NFT, the address of that NFT. |
| `creatorAddress` | string | The address the NFT was minted to. |
| `ram` | string | The RAM of the NFT, in hexadecimal. |
| `rom` | string | The ROM data, in hexadecimal: the `rom` field of the ROM when the ROM has one, otherwise the whole ROM. An NFT of a series that shares one ROM shows the series ROM. |
| `status` | string, see [`TokenStatus`](#tokenstatus) | `Infused` when the NFT is infused into another NFT, otherwise `Active`. |
| `infusion` | array of [`TokenPropertyResult`](#tokenpropertyresult) | The assets infused into the NFT: the token symbol as `key`, and the amount of a fungible token or the id of an NFT as `value`. |
| `properties` | array of [`TokenPropertyResult`](#tokenpropertyresult) | With `extended` set to `true`: the ROM fields, the series metadata fields, and, when the series has a contract, the values of its property methods, by name. |

## TokenExternalResult

The node does not fill this object.

## TokenPriceResult

The node does not fill this object.

## TokenPropertyResult

A named value: a metadata field, an NFT property, or an infusion.

| Field | Type | Description |
| --- | --- | --- |
| `key` | string | The name. |
| `value` | [property value](README.md#property-values) | The value. |

## TokenResult

A token.

| Field | Type | Description |
| --- | --- | --- |
| `symbol` | string | The token symbol. |
| `name` | string | The token name, from its metadata. |
| `decimals` | number | The decimals of the token. |
| `currentSupply` | string | The supply, in the smallest unit; for an NFT token, the number of NFTs. |
| `maxSupply` | string | The maximum supply; `0` means no maximum. |
| `burnedSupply` | string | The burned amount. For KCAL it includes the 9,242,814,271,535,702 atoms burned before Phantasma Phoenix. |
| `address` | string | The token address, derived from the symbol. |
| `owner` | string | The token owner. A token without an owner shows the main chain address `S3d7TbZxtNPdXy11hfmBLJLYn67gZTG2ibL7fJBcVdihWU4`. |
| `flags` | string | The token properties as text, separated by commas: always `Transferable, Burnable`, then `Fungible` for a fungible token, `Divisible` when it has decimals, `Stakable` for SOUL, and `Finite` when it has a maximum supply. |
| `script` | string | Not filled by the node. |
| `series` | array of [`TokenSeriesResult`](#tokenseriesresult) | Always empty; read the series with `getTokenSeries`. |
| `carbonId` | string | The Carbon token id. |
| `metadata` | array of [`TokenPropertyResult`](#tokenpropertyresult) | With `extended` set to `true`: the token metadata fields. |
| `tokenSchemas` | [`TokenSchemasResult`](#tokenschemasresult) | With `extended` set to `true`, for an NFT token: its schemas. |
| `external` | array of [`TokenExternalResult`](#tokenexternalresult) | Not filled by the node. |
| `price` | array of [`TokenPriceResult`](#tokenpriceresult) | Not filled by the node. |

## TokenSchemasResult

The three schemas of an NFT token: series metadata, ROM, and RAM.

| Field | Type | Description |
| --- | --- | --- |
| `seriesMetadata` | [`VmStructSchemaResult`](#vmstructschemaresult) | The schema of the series metadata. |
| `rom` | [`VmStructSchemaResult`](#vmstructschemaresult) | The schema of the ROM of each NFT. |
| `ram` | [`VmStructSchemaResult`](#vmstructschemaresult) | The schema of the RAM of each NFT. |

## TokenSeriesResult

A series of an NFT token.

| Field | Type | Description |
| --- | --- | --- |
| `seriesId` | string | The Phantasma series id, in decimal; `0` when the series has none. |
| `carbonTokenId` | string | The Carbon token id. |
| `carbonSeriesId` | string | The Carbon series id. |
| `ownerAddress` | string | The series owner, who can mint into it. |
| `maxMint` | string | The most NFTs the series may mint; `0` means no limit. |
| `mintCount` | string | The NFTs minted so far. |
| `currentSupply` | string | The NFTs of the series that exist now. |
| `maxSupply` | string | The most NFTs of the series that may exist at once; `0` means no limit. |
| `burnedSupply` | string | Not filled by the node. |
| `mode` | string | Not filled by the node. |
| `script` | string | Not filled by the node. |
| `methods` | array of [`ABIMethodResult`](#abimethodresult) | Not filled by the node. |
| `metadata` | array of [`TokenPropertyResult`](#tokenpropertyresult) | The series metadata fields, by name. |

## TokenStatus

The status of an NFT.

| Value | Meaning |
| --- | --- |
| `Active` | The NFT is held by an account. |
| `Infused` | The NFT is infused into another NFT. |

## TransactionResult

A transaction. Transactions of blocks from before Phantasma Phoenix carry their original fields and leave out the fields that only structured transactions have.

| Field | Type | Description |
| --- | --- | --- |
| `hash` | string | The transaction hash. |
| `chainAddress` | string | The main chain address, `S3d7TbZxtNPdXy11hfmBLJLYn67gZTG2ibL7fJBcVdihWU4`. |
| `timestamp` | number | The block time, in Unix seconds. |
| `blockHeight` | number | The height of the block that holds the transaction. |
| `blockHash` | string | The hash of that block. |
| `script` | string | The script, in hexadecimal, of a script transaction that completed; empty otherwise. |
| `carbonTxType` | number | The transaction type number: `0` to `14` for the structured types, `15` and `16` for script transactions. |
| `carbonTxData` | hex string | The body of the transaction, serialized, in hexadecimal. |
| `payload` | string | The payload, in hexadecimal. |
| `debugComment` | string | Empty when the transaction completed. Otherwise why it aborted or was rejected; a rejection starts with its type, such as `GasFees: below minimum gas bill`. |
| `events` | array of [`EventResult`](#eventresult) | The events the transaction emitted. |
| `extendedEvents` | array of [`EventExResult`](#eventexresult) | Events with decoded data, for the kinds that the node decodes. |
| `result` | string | The result, in hexadecimal. |
| `fee` | string | The gas bill paid, in KCAL atoms. |
| `state` | string, see [`ExecutionState`](#executionstate) | The outcome of the transaction. |
| `signatures` | array of [`TransactionSignatureResult`](#transactionsignatureresult) | The signatures. |
| `sender` | string | The fee payer. |
| `gasPayer` | string | The fee payer. |
| `gasTarget` | string | The main chain address, `S3d7TbZxtNPdXy11hfmBLJLYn67gZTG2ibL7fJBcVdihWU4`. |
| `gasPrice` | string | Always `1`. |
| `gasLimit` | string | The `maxGas` of the transaction, in KCAL atoms. |
| `expiration` | number | The expiry of the transaction, in Unix seconds. |

## TransactionSignatureResult

A signature of a transaction.

| Field | Type | Description |
| --- | --- | --- |
| `kind` | string | The signature kind, `Ed25519`. |
| `data` | string | The signature, in hexadecimal. |

## VmNamedVariableSchemaResult

A named field of a schema.

| Field | Type | Description |
| --- | --- | --- |
| `name` | string | The field name. |
| `schema` | [`VmVariableSchemaResult`](#vmvariableschemaresult) | The field type. |

## VmStructSchemaResult

A schema: its fields and its flags.

| Field | Type | Description |
| --- | --- | --- |
| `fields` | array of [`VmNamedVariableSchemaResult`](#vmnamedvariableschemaresult) | The fields, in order. |
| `flags` | number | Bit flags: `1` means the struct may carry fields that the schema does not name; `2` means the fields are stored sorted by name. |

## VmType

A field type of a schema.

| Value | Meaning |
| --- | --- |
| `Dynamic` | Any type. |
| `Array` | An array of any type. |
| `Bytes` | A byte array. |
| `Struct` | A struct with its own schema. |
| `Int8` | An 8-bit integer. |
| `Int16` | A 16-bit integer. |
| `Int32` | A 32-bit integer. |
| `Int64` | A 64-bit integer. |
| `Int256` | A 256-bit integer. |
| `Bytes16` | 16 bytes. |
| `Bytes32` | 32 bytes. |
| `Bytes64` | 64 bytes. |
| `String` | A string. |
| `Array_Dynamic` | An array of values of any type. |
| `Array_Bytes` | An array of byte arrays. |
| `Array_Struct` | An array of structs. |
| `Array_Int8` | An array of 8-bit integers. |
| `Array_Int16` | An array of 16-bit integers. |
| `Array_Int32` | An array of 32-bit integers. |
| `Array_Int64` | An array of 64-bit integers. |
| `Array_Int256` | An array of 256-bit integers. |
| `Array_Bytes16` | An array of 16-byte values. |
| `Array_Bytes32` | An array of 32-byte values. |
| `Array_Bytes64` | An array of 64-byte values. |
| `Array_String` | An array of strings. |

## VmVariableSchemaResult

The type of a schema field.

| Field | Type | Description |
| --- | --- | --- |
| `type` | string, see [`VmType`](#vmtype) | The type. |
| `schema` | [`VmStructSchemaResult`](#vmstructschemaresult) | For a `Struct` or a struct array, the schema of the struct. |
