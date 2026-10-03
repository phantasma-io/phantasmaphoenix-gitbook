# Node RPC Methods

Every node serves these methods. Call a method with JSON-RPC at `/rpc` or as REST at `/api/v1/<Method>`; the routes `/rpc/v2` and `/api/v2` serve the same methods with structured property values. [Node RPC](README.md) describes the routes, the request format, the limits, and the errors. Method names are case-insensitive in JSON-RPC; a REST path takes the parameters as query parameters under the names in the tables.

| Area | Methods |
| --- | --- |
| Node | [`getVersion`](#getversion) |
| Chain | [`getChain`](#getchain), [`getChains`](#getchains), [`getGasConfig`](#getgasconfig) |
| Blocks | [`getBlockByHash`](#getblockbyhash), [`getBlockByHeight`](#getblockbyheight), [`getBlockHeight`](#getblockheight), [`getBlockTransactionCountByHash`](#getblocktransactioncountbyhash), [`getLatestBlock`](#getlatestblock) |
| Transactions | [`estimateTransaction`](#estimatetransaction), [`getAddressTransactionCount`](#getaddresstransactioncount), [`getAddressTransactions`](#getaddresstransactions), [`getTransaction`](#gettransaction), [`getTransactionByBlockHashAndIndex`](#gettransactionbyblockhashandindex), [`invokeRawScript`](#invokerawscript), [`sendCarbonTransaction`](#sendcarbontransaction), [`sendRawTransaction`](#sendrawtransaction) |
| Accounts | [`getAccount`](#getaccount), [`getAccountFungibleTokens`](#getaccountfungibletokens), [`getAccountInfo`](#getaccountinfo), [`getAccountInfos`](#getaccountinfos), [`getAccountNFTs`](#getaccountnfts), [`getAccountOwnedTokens`](#getaccountownedtokens), [`getAccountOwnedTokenSeries`](#getaccountownedtokenseries), [`getAccounts`](#getaccounts), [`lookUpName`](#lookupname) |
| Tokens And NFTs | [`getNFT`](#getnft), [`getNFTs`](#getnfts), [`getToken`](#gettoken), [`getTokenBalance`](#gettokenbalance), [`getTokenData`](#gettokendata), [`getTokenNFTs`](#gettokennfts), [`getTokens`](#gettokens), [`getTokenSeries`](#gettokenseries), [`getTokenSeriesById`](#gettokenseriesbyid) |
| Contracts | [`getContract`](#getcontract), [`getContractByAddress`](#getcontractbyaddress), [`getContracts`](#getcontracts), [`getPhantasmaVmConfig`](#getphantasmavmconfig) |
| Organizations | [`getOrganization`](#getorganization), [`getOrganizationMember`](#getorganizationmember), [`getOrganizationMembers`](#getorganizationmembers), [`getOrganizations`](#getorganizations) |
| Auctions | [`getAuction`](#getauction), [`getAuctions`](#getauctions), [`getAuctionsCount`](#getauctionscount) |
| Nexus | [`getNexus`](#getnexus) |
| Leaderboards | [`getLeaderboard`](#getleaderboard) |
| Archives | [`getArchive`](#getarchive), [`readArchive`](#readarchive), [`writeArchive`](#writearchive) |

## Node

### getVersion

Returns the version, the Git commit, and the build time of the RPC node software.

| JSON-RPC | REST |
| --- | --- |
| `getVersion` | `GET /api/v1/GetVersion` |

No parameters.

Returns [`BuildInfoResult`](models.md#buildinforesult).

```json
{"jsonrpc": "2.0", "method": "getVersion", "params": [], "id": 1}
```

## Chain

The node serves one chain, `main`. Every chain argument accepts only `main`.

### getChain

**Not implemented.**

Answers an empty chain object.

| JSON-RPC | REST |
| --- | --- |
| `getChain` | `GET /api/v1/GetChain` |

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `name` | string | `main` | The chain name. Only `main` is accepted. |
| `extended` | boolean | `true` | Has no effect. |

Returns [`ChainResult`](models.md#chainresult).

### getChains

**Not implemented.**

Answers an empty array.

| JSON-RPC | REST |
| --- | --- |
| `getChains` | `GET /api/v1/GetChains` |

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `extended` | boolean | `true` | Deprecated. Has no effect. |

Returns an array of [`ChainResult`](models.md#chainresult).

### getGasConfig

Returns the gas configuration of the latest block, the gas model version, and the chain parameters that fee calculation needs. [Fees And Gas](/developers/blockchain/chain/fees-and-gas.md) explains every field.

| JSON-RPC | REST |
| --- | --- |
| `getGasConfig` | `GET /api/v1/GetGasConfig` |

No parameters.

Returns [`GasConfigResult`](models.md#gasconfigresult).

```json
{"jsonrpc": "2.0", "method": "getGasConfig", "params": [], "id": 1}
```

## Blocks

### getBlockByHash

Returns a block and its transactions by block hash.

| JSON-RPC | REST |
| --- | --- |
| `getBlockByHash` | `GET /api/v1/GetBlockByHash` |

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `blockHash` | string | required | The block hash, 64 hexadecimal characters. |

Returns [`BlockResult`](models.md#blockresult).

```json
{"jsonrpc": "2.0", "method": "getBlockByHash", "params": ["129B054E2B2CB51686060A2C8A543F120D5E08FEE02D0B4178B50F607FBA80A6"], "id": 1}
```

### getBlockByHeight

Returns a block and its transactions by height. Height `0` is refused.

| JSON-RPC | REST |
| --- | --- |
| `getBlockByHeight` | `GET /api/v1/GetBlockByHeight` |

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `chainInput` | string | required | The chain name. Only `main` is accepted. |
| `height` | string | required | The block height, as a decimal string. |

Returns [`BlockResult`](models.md#blockresult).

```json
{"jsonrpc": "2.0", "method": "getBlockByHeight", "params": ["main", "1"], "id": 1}
```

### getBlockHeight

Returns the height of the latest block, as a decimal string.

| JSON-RPC | REST |
| --- | --- |
| `getBlockHeight` | `GET /api/v1/GetBlockHeight` |

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `chainInput` | string | required | The chain name. Only `main` is accepted. |

Returns string.

```json
{"jsonrpc": "2.0", "method": "getBlockHeight", "params": ["main"], "id": 1}
```

### getBlockTransactionCountByHash

Returns the number of transactions in a block. An unknown hash answers the error `block not found`.

| JSON-RPC | REST |
| --- | --- |
| `getBlockTransactionCountByHash` | `GET /api/v1/GetBlockTransactionCountByHash` |

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `chainAddressOrName` | string | required | The chain name. Only `main` is accepted. |
| `blockHash` | string | required | The block hash, 64 hexadecimal characters. |

Returns number.

```json
{"jsonrpc": "2.0", "method": "getBlockTransactionCountByHash", "params": ["main", "129B054E2B2CB51686060A2C8A543F120D5E08FEE02D0B4178B50F607FBA80A6"], "id": 1}
```

### getLatestBlock

Returns the latest block and its transactions.

| JSON-RPC | REST |
| --- | --- |
| `getLatestBlock` | `GET /api/v1/GetLatestBlock` |

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `chainInput` | string | required | The chain name. Only `main` is accepted. |

Returns [`BlockResult`](models.md#blockresult).

```json
{"jsonrpc": "2.0", "method": "getLatestBlock", "params": ["main"], "id": 1}
```

## Transactions

### estimateTransaction

Runs a serialized transaction against the current chain state without recording it, and returns its gas bill, its storage escrow, and recommended `maxGas` and `maxData`. The signatures may be zero-filled bytes of the correct length. See [Fee Estimation](/developers/blockchain/chain/fees-and-gas.md#fee-estimation).

| JSON-RPC | REST |
| --- | --- |
| `estimateTransaction` | `GET /api/v1/EstimateTransaction` |

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `txData` | string | required | The serialized transaction, in hexadecimal. |

Returns [`EstimateTransactionResult`](models.md#estimatetransactionresult).

### getAddressTransactionCount

Returns the number of transactions recorded for an address.

| JSON-RPC | REST |
| --- | --- |
| `getAddressTransactionCount` | `GET /api/v1/GetAddressTransactionCount` |

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `account` | string | required | The address. |
| `chainInput` | string | `main` | The chain name. Only `main` is accepted. |
| `checkAddressResevedByte` | boolean | `true` | Whether to refuse an address that fails the reserved-byte check. Keep it `true`. The parameter name is spelled this way. |

Returns number.

```json
{"jsonrpc": "2.0", "method": "getAddressTransactionCount", "params": ["P2KJC8TB6XyY9sr1s4GprPD2XjnnUggRq86pwsFZjUEqCXt"], "id": 1}
```

### getAddressTransactions

Returns the transactions of an address, newest first, one page at a time.

| JSON-RPC | REST |
| --- | --- |
| `getAddressTransactions` | `GET /api/v1/GetAddressTransactions` |

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `account` | string | required | The address. |
| `page` | integer | `1` | The page number, starting at 1. |
| `pageSize` | integer | `10` | Entries per page, from 1 to 100. |
| `checkAddressResevedByte` | boolean | `true` | Whether to refuse an address that fails the reserved-byte check. Keep it `true`. The parameter name is spelled this way. |

Returns a page, [`PaginatedResult`](models.md#paginatedresult), whose `result` is [`AccountTransactionsResult`](models.md#accounttransactionsresult).

```json
{"jsonrpc": "2.0", "method": "getAddressTransactions", "params": ["P2KJC8TB6XyY9sr1s4GprPD2XjnnUggRq86pwsFZjUEqCXt"], "id": 1}
```

### getTransaction

Returns a transaction by hash. A transaction that is still in the queue or not yet final answers the error `pending`; an unknown hash answers `Transaction not found`. A rejected transaction returns its hash, its state `Fault`, and the reason in `debugComment`.

| JSON-RPC | REST |
| --- | --- |
| `getTransaction` | `GET /api/v1/GetTransaction` |

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `hashText` | string | required | The transaction hash. |

Returns [`TransactionResult`](models.md#transactionresult).

```json
{"jsonrpc": "2.0", "method": "getTransaction", "params": ["07D5F8CEDB96C11CFE2923F5D370CB4E9C98BB65B8C0ACD9F56E358077D73A0D"], "id": 1}
```

### getTransactionByBlockHashAndIndex

Returns the transaction at a position in a block. Positions start at `0`.

| JSON-RPC | REST |
| --- | --- |
| `getTransactionByBlockHashAndIndex` | `GET /api/v1/GetTransactionByBlockHashAndIndex` |

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `chainAddressOrName` | string | required | The chain name. Only `main` is accepted. |
| `blockHash` | string | required | The block hash, 64 hexadecimal characters. |
| `index` | integer | required | The position of the transaction in the block, starting at 0. |

Returns [`TransactionResult`](models.md#transactionresult).

```json
{"jsonrpc": "2.0", "method": "getTransactionByBlockHashAndIndex", "params": ["main", "129B054E2B2CB51686060A2C8A543F120D5E08FEE02D0B4178B50F607FBA80A6", 0], "id": 1}
```

### invokeRawScript

Runs a VM script against the current chain state without recording anything, and returns its results and events. Use it to call read methods of contracts. A script that fails answers the error `Execution failed: <type>: <reason>`.

| JSON-RPC | REST |
| --- | --- |
| `invokeRawScript` | `GET /api/v1/InvokeRawScript` |

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `chainInput` | string | required | The chain name. Only `main` is accepted. |
| `scriptData` | string | required | The script, in hexadecimal. |

Returns [`ScriptResult`](models.md#scriptresult).

### sendCarbonTransaction

Sends a signed structured transaction and returns its hash. The node refuses an expired transaction before sending it; the chain's own refusals come back as `Transaction was rejected: Rejection type: <type>, error: <reason>`. A returned hash means the transaction was queued, not that it succeeded: read its result with `getTransaction`.

| JSON-RPC | REST |
| --- | --- |
| `sendCarbonTransaction` | `GET /api/v1/SendCarbonTransaction` |

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `txData` | string | required | The signed transaction, in hexadecimal. |

Returns string.

### sendRawTransaction

Sends a signed script transaction in the script transaction format and returns its hash. The node refuses an expired transaction and a transaction for another nexus before sending it; the chain's own refusals come back as `Transaction was rejected: Rejection type: <type>, error: <reason>`. A returned hash means the transaction was queued, not that it succeeded.

| JSON-RPC | REST |
| --- | --- |
| `sendRawTransaction` | `GET /api/v1/SendRawTransaction` |

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `txData` | string | required | The signed transaction, in hexadecimal. |

Returns string.

## Accounts

### getAccount

**Deprecated.** Use `getAccountInfo` for the name and the stake, and `getAccountFungibleTokens` and `getAccountNFTs` for the balances.

Returns the name, the stake, and every balance of an address. Each NFT balance lists at most 10,000 NFT ids; `amount` carries the true count.

| JSON-RPC | REST |
| --- | --- |
| `getAccount` | `GET /api/v1/GetAccount` |

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `account` | string | required | The address. |
| `extended` | boolean | `true` | Deprecated. Has no effect. |
| `checkAddressReservedByte` | boolean | `true` | Whether to refuse an address that fails the reserved-byte check. Keep it `true`. |
| `addressType` | `Phantasma` or `Carbon` | `Phantasma` | How `account` is written: `Phantasma` for a Phantasma address, `Carbon` for a 32-byte account key in 64 hexadecimal characters. |

Returns [`AccountResult`](models.md#accountresult).

```json
{"jsonrpc": "2.0", "method": "getAccount", "params": ["P2KJC8TB6XyY9sr1s4GprPD2XjnnUggRq86pwsFZjUEqCXt"], "id": 1}
```

### getAccountFungibleTokens

Returns the fungible token balances of an address, one page at a time.

| JSON-RPC | REST |
| --- | --- |
| `getAccountFungibleTokens` | `GET /api/v1/GetAccountFungibleTokens` |

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `account` | string | required | The address. |
| `tokenSymbol` | string | `""` | Only this token, by symbol. Do not combine with `carbonTokenId`. |
| `carbonTokenId` | integer | `0` | Only this token, by its Carbon token id. `0` means no filter. Do not combine with `tokenSymbol`. |
| `pageSize` | integer | `10` | Entries per page, from 1 to 100. |
| `cursor` | string | `""` | The `cursor` of the previous page; empty for the first page. |
| `checkAddressReservedByte` | boolean | `true` | Whether to refuse an address that fails the reserved-byte check. Keep it `true`. |
| `addressType` | `Phantasma` or `Carbon` | `Phantasma` | How `account` is written: `Phantasma` for a Phantasma address, `Carbon` for a 32-byte account key in 64 hexadecimal characters. |

Returns a page, [`CursorPaginatedResult`](models.md#cursorpaginatedresult), whose `result` is an array of [`BalanceResult`](models.md#balanceresult).

```json
{"jsonrpc": "2.0", "method": "getAccountFungibleTokens", "params": ["P2KJC8TB6XyY9sr1s4GprPD2XjnnUggRq86pwsFZjUEqCXt"], "id": 1}
```

### getAccountInfo

Returns the registered name and the SOUL stake of an address: the staked amount, the staking timestamp, and the KCAL earned and not yet claimed. It carries no balances; read them with `getAccountFungibleTokens`, `getAccountNFTs`, or `getTokenBalance`.

| JSON-RPC | REST |
| --- | --- |
| `getAccountInfo` | `GET /api/v1/GetAccountInfo` |

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `account` | string | required | The address. |
| `checkAddressReservedByte` | boolean | `true` | Whether to refuse an address that fails the reserved-byte check. Keep it `true`. |
| `addressType` | `Phantasma` or `Carbon` | `Phantasma` | How `account` is written: `Phantasma` for a Phantasma address, `Carbon` for a 32-byte account key in 64 hexadecimal characters. |

Returns [`AccountInfoResult`](models.md#accountinforesult).

```json
{"jsonrpc": "2.0", "method": "getAccountInfo", "params": ["P2KJC8TB6XyY9sr1s4GprPD2XjnnUggRq86pwsFZjUEqCXt"], "id": 1}
```

### getAccountInfos

Returns `getAccountInfo` results for up to 100 addresses, in request order, read from one state snapshot. One malformed address fails the whole request.

| JSON-RPC | REST |
| --- | --- |
| `getAccountInfos` | `GET /api/v1/GetAccountInfos` |

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `accounts` | array of strings | required | From 1 to 100 addresses: a JSON array in JSON-RPC, a repeated `accounts` query parameter in REST. |
| `checkAddressReservedByte` | boolean | `true` | Whether to refuse an address that fails the reserved-byte check. Keep it `true`. |
| `addressType` | `Phantasma` or `Carbon` | `Phantasma` | How `every address` is written: `Phantasma` for a Phantasma address, `Carbon` for a 32-byte account key in 64 hexadecimal characters. |

Returns an array of [`AccountInfoResult`](models.md#accountinforesult).

```json
{"jsonrpc": "2.0", "method": "getAccountInfos", "params": [["P2KJC8TB6XyY9sr1s4GprPD2XjnnUggRq86pwsFZjUEqCXt"]], "id": 1}
```

### getAccountNFTs

Returns the NFTs that an address holds, one page at a time.

| JSON-RPC | REST |
| --- | --- |
| `getAccountNFTs` | `GET /api/v1/GetAccountNFTs` |

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `account` | string | required | The address. |
| `tokenSymbol` | string | `""` | Only this token, by symbol. Do not combine with `carbonTokenId`. |
| `carbonTokenId` | integer | `0` | Only this token, by its Carbon token id. `0` means no filter. Do not combine with `tokenSymbol`. |
| `carbonSeriesId` | integer | `0` | Only this series, by its Carbon series id; needs `tokenSymbol` or `carbonTokenId`. `0` means no filter. |
| `pageSize` | integer | `10` | Entries per page, from 1 to 100, or from 1 to 50 when `extended` is `true`. |
| `cursor` | string | `""` | The `cursor` of the previous page; empty for the first page. |
| `extended` | boolean | `false` | Whether to include the NFT properties and infusions. |
| `checkAddressReservedByte` | boolean | `true` | Whether to refuse an address that fails the reserved-byte check. Keep it `true`. |
| `addressType` | `Phantasma` or `Carbon` | `Phantasma` | How `account` is written: `Phantasma` for a Phantasma address, `Carbon` for a 32-byte account key in 64 hexadecimal characters. |

Returns a page, [`CursorPaginatedResult`](models.md#cursorpaginatedresult), whose `result` is an array of [`TokenDataResult`](models.md#tokendataresult).

```json
{"jsonrpc": "2.0", "method": "getAccountNFTs", "params": ["P2KJC8TB6XyY9sr1s4GprPD2XjnnUggRq86pwsFZjUEqCXt"], "id": 1}
```

### getAccountOwnedTokens

Returns the NFT tokens of which an address holds at least one NFT, one page at a time.

| JSON-RPC | REST |
| --- | --- |
| `getAccountOwnedTokens` | `GET /api/v1/GetAccountOwnedTokens` |

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `account` | string | required | The address. |
| `tokenSymbol` | string | `""` | Only this token, by symbol. Do not combine with `carbonTokenId`. |
| `carbonTokenId` | integer | `0` | Only this token, by its Carbon token id. `0` means no filter. Do not combine with `tokenSymbol`. |
| `pageSize` | integer | `10` | Entries per page, from 1 to 100. |
| `cursor` | string | `""` | The `cursor` of the previous page; empty for the first page. |
| `checkAddressReservedByte` | boolean | `true` | Whether to refuse an address that fails the reserved-byte check. Keep it `true`. |
| `addressType` | `Phantasma` or `Carbon` | `Phantasma` | How `account` is written: `Phantasma` for a Phantasma address, `Carbon` for a 32-byte account key in 64 hexadecimal characters. |

Returns a page, [`CursorPaginatedResult`](models.md#cursorpaginatedresult), whose `result` is an array of [`TokenResult`](models.md#tokenresult).

```json
{"jsonrpc": "2.0", "method": "getAccountOwnedTokens", "params": ["P2KJC8TB6XyY9sr1s4GprPD2XjnnUggRq86pwsFZjUEqCXt"], "id": 1}
```

### getAccountOwnedTokenSeries

Returns the NFT series of which an address holds at least one NFT, one page at a time.

| JSON-RPC | REST |
| --- | --- |
| `getAccountOwnedTokenSeries` | `GET /api/v1/GetAccountOwnedTokenSeries` |

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `account` | string | required | The address. |
| `tokenSymbol` | string | `""` | Only this token, by symbol. Do not combine with `carbonTokenId`. |
| `carbonTokenId` | integer | `0` | Only this token, by its Carbon token id. `0` means no filter. Do not combine with `tokenSymbol`. |
| `pageSize` | integer | `10` | Entries per page, from 1 to 100. |
| `cursor` | string | `""` | The `cursor` of the previous page; empty for the first page. |
| `checkAddressReservedByte` | boolean | `true` | Whether to refuse an address that fails the reserved-byte check. Keep it `true`. |
| `addressType` | `Phantasma` or `Carbon` | `Phantasma` | How `account` is written: `Phantasma` for a Phantasma address, `Carbon` for a 32-byte account key in 64 hexadecimal characters. |

Returns a page, [`CursorPaginatedResult`](models.md#cursorpaginatedresult), whose `result` is an array of [`TokenSeriesResult`](models.md#tokenseriesresult).

```json
{"jsonrpc": "2.0", "method": "getAccountOwnedTokenSeries", "params": ["P2KJC8TB6XyY9sr1s4GprPD2XjnnUggRq86pwsFZjUEqCXt"], "id": 1}
```

### getAccounts

**Deprecated.** Use `getAccountInfos`, and `getAccountFungibleTokens` and `getAccountNFTs` per address.

Returns `getAccount` results for several addresses.

| JSON-RPC | REST |
| --- | --- |
| `getAccounts` | `GET /api/v1/GetAccounts` |

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `accountText` | string | required | Addresses, separated by commas. |
| `extended` | boolean | `false` | Deprecated. Has no effect. |
| `checkAddressReservedByte` | boolean | `true` | Whether to refuse an address that fails the reserved-byte check. Keep it `true`. |
| `addressType` | `Phantasma` or `Carbon` | `Phantasma` | How `each address` is written: `Phantasma` for a Phantasma address, `Carbon` for a 32-byte account key in 64 hexadecimal characters. |

Returns an array of [`AccountResult`](models.md#accountresult).

```json
{"jsonrpc": "2.0", "method": "getAccounts", "params": ["P2KJC8TB6XyY9sr1s4GprPD2XjnnUggRq86pwsFZjUEqCXt, P2KBh1rkUZXNj7i1SfegUEg26YfrcYDRBt69fj6izVAPbtc"], "id": 1}
```

### lookUpName

Returns the address that registered an account name.

| JSON-RPC | REST |
| --- | --- |
| `lookUpName` | `GET /api/v1/LookUpName` |

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `name` | string | required | The registered account name. |

Returns string.

```json
{"jsonrpc": "2.0", "method": "lookUpName", "params": ["beyondtheneon"], "id": 1}
```

## Tokens And NFTs

### getNFT

Returns one NFT by token symbol and NFT id.

| JSON-RPC | REST |
| --- | --- |
| `getNFT` | `GET /api/v1/GetNFT` |

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `symbol` | string | required | The token symbol. |
| `IDtext` | string | required | The NFT id, in decimal. |
| `extended` | boolean | `false` | Whether to include the NFT properties and infusions. |

Returns [`TokenDataResult`](models.md#tokendataresult).

```json
{"jsonrpc": "2.0", "method": "getNFT", "params": ["CROWN", "102027540816489236327796452815702733520646114324490783683230488899035835189818"], "id": 1}
```

### getNFTs

Returns several NFTs of one token by NFT id.

| JSON-RPC | REST |
| --- | --- |
| `getNFTs` | `GET /api/v1/GetNFTs` |

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `symbol` | string | required | The token symbol. |
| `IDText` | string | required | NFT ids in decimal, separated by commas. |
| `extended` | boolean | `false` | Whether to include the NFT properties and infusions. |

Returns an array of [`TokenDataResult`](models.md#tokendataresult).

```json
{"jsonrpc": "2.0", "method": "getNFTs", "params": ["CROWN", "102027540816489236327796452815702733520646114324490783683230488899035835189818"], "id": 1}
```

### getToken

Returns a token by symbol or by Carbon token id. The token metadata and, for an NFT token, its schemas come only with `extended` set to `true`.

| JSON-RPC | REST |
| --- | --- |
| `getToken` | `GET /api/v1/GetToken` |

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `symbol` | string | `""` | The token symbol. Leave it empty when `carbonTokenId` is set. |
| `extended` | boolean | `false` | Whether to include the token metadata and, for an NFT token, its schemas. |
| `carbonTokenId` | integer | `0` | The Carbon token id. `0` means the token is named by `symbol`. |

Returns [`TokenResult`](models.md#tokenresult).

```json
{"jsonrpc": "2.0", "method": "getToken", "params": ["SOUL"], "id": 1}
```

### getTokenBalance

Returns the balance of one token held by an address. For an NFT token, `amount` is the number of NFTs and `ids` lists at most 10,000 of them; page through the NFTs with `getAccountNFTs`.

| JSON-RPC | REST |
| --- | --- |
| `getTokenBalance` | `GET /api/v1/GetTokenBalance` |

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `account` | string | required | The address. |
| `tokenSymbol` | string | required | The token symbol. |
| `chainInput` | string | required | The chain name. Only `main` is accepted. |
| `checkAddressResevedByte` | boolean | `true` | Whether to refuse an address that fails the reserved-byte check. Keep it `true`. The parameter name is spelled this way. |
| `addressType` | `Phantasma` or `Carbon` | `Phantasma` | How `account` is written: `Phantasma` for a Phantasma address, `Carbon` for a 32-byte account key in 64 hexadecimal characters. |

Returns [`BalanceResult`](models.md#balanceresult).

```json
{"jsonrpc": "2.0", "method": "getTokenBalance", "params": ["P2KJC8TB6XyY9sr1s4GprPD2XjnnUggRq86pwsFZjUEqCXt", "SOUL", "main"], "id": 1}
```

### getTokenData

**Deprecated.** Use `getNFT`.

Returns one NFT by token symbol and NFT id, without properties.

| JSON-RPC | REST |
| --- | --- |
| `getTokenData` | `GET /api/v1/GetTokenData` |

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `symbol` | string | required | The token symbol. |
| `IDtext` | string | required | The NFT id, in decimal. |

Returns [`TokenDataResult`](models.md#tokendataresult).

```json
{"jsonrpc": "2.0", "method": "getTokenData", "params": ["CROWN", "102027540816489236327796452815702733520646114324490783683230488899035835189818"], "id": 1}
```

### getTokenNFTs

Returns the NFTs of a token, or of one of its series, one page at a time.

| JSON-RPC | REST |
| --- | --- |
| `getTokenNFTs` | `GET /api/v1/GetTokenNFTs` |

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `carbonTokenId` | integer | required | The Carbon token id. |
| `carbonSeriesId` | integer | `0` | Only this series, by its Carbon series id. `0` means the whole token. Do not combine with `seriesId`. |
| `pageSize` | integer | `10` | Entries per page, from 1 to 100, or from 1 to 50 when `extended` is `true`. |
| `cursor` | string | `""` | The `cursor` of the previous page; empty for the first page. |
| `extended` | boolean | `false` | Whether to include the NFT properties and infusions. |
| `seriesId` | string | `""` | Only this series, by its Phantasma series id in decimal. Do not combine with `carbonSeriesId`. |

Returns a page, [`CursorPaginatedResult`](models.md#cursorpaginatedresult), whose `result` is an array of [`TokenDataResult`](models.md#tokendataresult).

```json
{"jsonrpc": "2.0", "method": "getTokenNFTs", "params": [4, 1], "id": 1}
```

### getTokens

Returns every token, or the tokens of one owner.

| JSON-RPC | REST |
| --- | --- |
| `getTokens` | `GET /api/v1/GetTokens` |

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `extended` | boolean | `false` | Deprecated. Whether to include the metadata of each token and the schemas of each NFT token. |
| `ownerAddress` | string | none | Only the tokens of this owner. |
| `addressType` | `Phantasma` or `Carbon` | `Phantasma` | How `ownerAddress` is written: `Phantasma` for a Phantasma address, `Carbon` for a 32-byte account key in 64 hexadecimal characters. |

Returns an array of [`TokenResult`](models.md#tokenresult).

```json
{"jsonrpc": "2.0", "method": "getTokens", "params": [], "id": 1}
```

### getTokenSeries

Returns the series of an NFT token, one page at a time.

| JSON-RPC | REST |
| --- | --- |
| `getTokenSeries` | `GET /api/v1/GetTokenSeries` |

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `symbol` | string | `""` | The token symbol. Leave it empty when `carbonTokenId` is set. |
| `carbonTokenId` | integer | `0` | The Carbon token id. `0` means the token is named by `symbol`. |
| `pageSize` | integer | `10` | Entries per page, from 1 to 100. |
| `cursor` | string | `""` | The `cursor` of the previous page; empty for the first page. |

Returns a page, [`CursorPaginatedResult`](models.md#cursorpaginatedresult), whose `result` is an array of [`TokenSeriesResult`](models.md#tokenseriesresult).

```json
{"jsonrpc": "2.0", "method": "getTokenSeries", "params": ["CROWN"], "id": 1}
```

### getTokenSeriesById

Returns one series. Name the token by `symbol` or `carbonTokenId`, and the series by `seriesId` or `carbonSeriesId`.

| JSON-RPC | REST |
| --- | --- |
| `getTokenSeriesById` | `GET /api/v1/GetTokenSeriesById` |

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `symbol` | string | `""` | The token symbol. Do not combine with `carbonTokenId`. |
| `carbonTokenId` | integer | `0` | The Carbon token id. Do not combine with `symbol`. |
| `seriesId` | string | `""` | The Phantasma series id, in decimal. Do not combine with `carbonSeriesId`. |
| `carbonSeriesId` | integer | `0` | The Carbon series id. Do not combine with `seriesId`. |

Returns [`TokenSeriesResult`](models.md#tokenseriesresult).

```json
{"jsonrpc": "2.0", "method": "getTokenSeriesById", "params": ["", 4, "", 1], "id": 1}
```

## Contracts

### getContract

Returns a deployed contract by name. An unknown name answers the error `Contract not found`.

| JSON-RPC | REST |
| --- | --- |
| `getContract` | `GET /api/v1/GetContract` |

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `chainAddressOrName` | string | required | The chain name. Only `main` is accepted. |
| `contractName` | string | required | The contract name. |

Returns [`ContractResult`](models.md#contractresult).

```json
{"jsonrpc": "2.0", "method": "getContract", "params": ["main", "account"], "id": 1}
```

### getContractByAddress

Returns a deployed contract by address. An unknown address answers the error `Contract not found`.

| JSON-RPC | REST |
| --- | --- |
| `getContractByAddress` | `GET /api/v1/GetContractByAddress` |

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `chainAddressOrName` | string | required | The chain name. Only `main` is accepted. |
| `contractAddress` | string | required | The contract address. |

Returns [`ContractResult`](models.md#contractresult).

```json
{"jsonrpc": "2.0", "method": "getContractByAddress", "params": ["main", "S3dGz1deZweAiMVPHL328X3pVNpANQVjgX4MoRGpbNNAfrB"], "id": 1}
```

### getContracts

Returns every deployed contract.

| JSON-RPC | REST |
| --- | --- |
| `getContracts` | `GET /api/v1/GetContracts` |

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `chainAddressOrName` | string | required | The chain name. Only `main` is accepted. |
| `extended` | boolean | `true` | Deprecated. Whether to include the scripts, methods, and events of the contracts. |

Returns an array of [`ContractResult`](models.md#contractresult).

```json
{"jsonrpc": "2.0", "method": "getContracts", "params": ["main"], "id": 1}
```

### getPhantasmaVmConfig

Returns the configuration of the Phantasma VM: its feature level and the gas cost of each interop group. See [The Gas Bill](/developers/blockchain/chain/fees-and-gas.md#the-gas-bill).

| JSON-RPC | REST |
| --- | --- |
| `getPhantasmaVmConfig` | `GET /api/v1/GetPhantasmaVmConfig` |

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `chainAddressOrName` | string | required | The chain name. Only `main` is accepted. |

Returns [`PhantasmaVmConfigResult`](models.md#phantasmavmconfigresult).

```json
{"jsonrpc": "2.0", "method": "getPhantasmaVmConfig", "params": ["main"], "id": 1}
```

## Organizations

### getOrganization

Returns an organization by name, such as `masters`. An unknown name answers the error `invalid organization`.

| JSON-RPC | REST |
| --- | --- |
| `getOrganization` | `GET /api/v1/GetOrganization` |

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `name` | string | required | The organization name. |
| `includeMemberCount` | boolean | `false` | Whether to count the members. Counting reads every member row. |

Returns [`OrganizationResult`](models.md#organizationresult).

```json
{"jsonrpc": "2.0", "method": "getOrganization", "params": ["masters"], "id": 1}
```

### getOrganizationMember

Returns whether an address is a member of an organization, and since when.

| JSON-RPC | REST |
| --- | --- |
| `getOrganizationMember` | `GET /api/v1/GetOrganizationMember` |

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `name` | string | required | The organization name. |
| `address` | string | required | The address to look up. |
| `checkAddressReservedByte` | boolean | `true` | Whether to refuse an address that fails the reserved-byte check. Keep it `true`. |
| `addressType` | `Phantasma` or `Carbon` | `Phantasma` | How `address` is written: `Phantasma` for a Phantasma address, `Carbon` for a 32-byte account key in 64 hexadecimal characters. |

Returns [`OrganizationMemberResult`](models.md#organizationmemberresult).

```json
{"jsonrpc": "2.0", "method": "getOrganizationMember", "params": ["masters", "P2KJC8TB6XyY9sr1s4GprPD2XjnnUggRq86pwsFZjUEqCXt"], "id": 1}
```

### getOrganizationMembers

Returns the members of an organization, one page at a time.

| JSON-RPC | REST |
| --- | --- |
| `getOrganizationMembers` | `GET /api/v1/GetOrganizationMembers` |

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `name` | string | required | The organization name. |
| `pageSize` | integer | `10` | Entries per page, from 1 to 100. |
| `cursor` | string | `""` | The `cursor` of the previous page; empty for the first page. |
| `includeMemberTime` | boolean | `true` | Whether to include the time each member joined. |

Returns a page, [`CursorPaginatedResult`](models.md#cursorpaginatedresult), whose `result` is an array of [`OrganizationMemberResult`](models.md#organizationmemberresult).

```json
{"jsonrpc": "2.0", "method": "getOrganizationMembers", "params": ["masters"], "id": 1}
```

### getOrganizations

Returns the organizations of the chain, one page at a time.

| JSON-RPC | REST |
| --- | --- |
| `getOrganizations` | `GET /api/v1/GetOrganizations` |

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `pageSize` | integer | `10` | Entries per page, from 1 to 100. |
| `cursor` | string | `""` | The `cursor` of the previous page; empty for the first page. |
| `includeMemberCount` | boolean | `false` | Whether to count the members of each organization. Counting reads every member row. |

Returns a page, [`CursorPaginatedResult`](models.md#cursorpaginatedresult), whose `result` is an array of [`OrganizationResult`](models.md#organizationresult).

```json
{"jsonrpc": "2.0", "method": "getOrganizations", "params": [], "id": 1}
```

## Auctions

Auctions are the fixed-price NFT listings of the chain market. Each listing sells one NFT for a fungible token.

### getAuction

Returns the market listing of one NFT, by token symbol and NFT id.

| JSON-RPC | REST |
| --- | --- |
| `getAuction` | `GET /api/v1/GetAuction` |

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `chainAddressOrName` | string | required | The chain name. Only `main` is accepted. |
| `symbol` | string | required | The symbol of the NFT token. |
| `IDtext` | string | required | The NFT id, in decimal. |

Returns [`AuctionResult`](models.md#auctionresult).

### getAuctions

Returns the market listings, one page at a time.

| JSON-RPC | REST |
| --- | --- |
| `getAuctions` | `GET /api/v1/GetAuctions` |

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `chainAddressOrName` | string | required | The chain name. Only `main` is accepted. |
| `symbol` | string | none | Only listings of this NFT token, by symbol. |
| `page` | integer | `1` | The page number, starting at 1. |
| `pageSize` | integer | `10` | Entries per page, from 1 to 100. |

Returns a page, [`PaginatedResult`](models.md#paginatedresult), whose `result` is an array of [`AuctionResult`](models.md#auctionresult).

```json
{"jsonrpc": "2.0", "method": "getAuctions", "params": ["main"], "id": 1}
```

### getAuctionsCount

Returns the number of market listings.

| JSON-RPC | REST |
| --- | --- |
| `getAuctionsCount` | `GET /api/v1/GetAuctionsCount` |

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `chainAddressOrName` | string | `main` | The chain name. Only `main` is accepted. |
| `symbol` | string | none | Only listings of this NFT token, by symbol. |

Returns number.

```json
{"jsonrpc": "2.0", "method": "getAuctionsCount", "params": [], "id": 1}
```

## Nexus

This method reads nothing and answers a default object.

### getNexus

**Not implemented.**

Answers an empty nexus object.

| JSON-RPC | REST |
| --- | --- |
| `getNexus` | `GET /api/v1/GetNexus` |

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `extended` | boolean | `false` | Has no effect. |

Returns [`NexusResult`](models.md#nexusresult).

## Leaderboards

This method reads nothing and answers a default object.

### getLeaderboard

**Not implemented.**

Answers an empty leaderboard object.

| JSON-RPC | REST |
| --- | --- |
| `getLeaderboard` | `GET /api/v1/GetLeaderboard` |

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `name` | string | required | The leaderboard name. |

Returns [`LeaderboardResult`](models.md#leaderboardresult).

## Archives

The chain keeps no archives. These methods read and store nothing.

### getArchive

**Not implemented.**

Answers an empty archive object.

| JSON-RPC | REST |
| --- | --- |
| `getArchive` | `GET /api/v1/GetArchive` |

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `hashText` | string | required | The archive hash, in hexadecimal. |

Returns [`ArchiveResult`](models.md#archiveresult).

### readArchive

**Not implemented.**

Answers an empty string.

| JSON-RPC | REST |
| --- | --- |
| `readArchive` | `GET /api/v1/ReadArchive` |

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `hashText` | string | required | The archive hash, in hexadecimal. |
| `blockIndex` | integer | required | The archive block, starting at 0. |

Returns string.

### writeArchive

**Not implemented.**

Answers `false` and stores nothing.

| JSON-RPC | REST |
| --- | --- |
| `writeArchive` | `GET /api/v1/WriteArchive` |

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `hashText` | string | required | The archive hash, in hexadecimal. |
| `blockIndex` | integer | required | The archive block, starting at 0. |
| `blockContent` | string | required | The block content, in base64. |

Returns boolean.
