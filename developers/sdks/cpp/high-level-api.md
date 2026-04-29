# High‑Level API — `phantasma::rpc::PhantasmaAPI`

This guide explains how to use the **typed RPC client** to talk to a Phantasma node.
It covers adapter setup, error handling, data types, and groups endpoints by domain with examples you can copy‑paste.

> For raw JSON building/parsing, see the separate **Low‑Level JSON API** document.

## Include order & setup

Choose one backend:

**RapidJSON + libcurl** (most common)
```cpp
#include "Adapters/PhantasmaAPI_rapidjson.h"
#include "Adapters/PhantasmaAPI_curl.h"
#include "PhantasmaAPI.h"
using namespace phantasma;
using namespace phantasma::rpc;
HttpClient http("https://node-url");
PhantasmaAPI api(http);
```

**CppRestSDK** (all‑in‑one)
```cpp
#include "Adapters/PhantasmaAPI_cpprest.h"
#include "PhantasmaAPI.h"
using namespace phantasma; using namespace phantasma::rpc;
HttpClient http("https://node-url");
PhantasmaAPI api(http);
```

## Errors

Most methods accept an optional `PhantasmaError*` and return a default/empty result on error.
Check `err.code` and `err.message` when provided.

```cpp
PhantasmaError err{};
Account acc = api.GetAccount("P2K...", &err);
if (err.code != 0) { /* handle err.message */ }
```

## Common patterns

**Pagination** (e.g., `GetAddressTransactions`)
```cpp
UInt32 page = 0, pageSize = 50;
AccountTransactions txs = api.GetAddressTransactions("P2K...", page, pageSize);
```

**Send a signed transaction**
```cpp
String rawTx = Base16::Encode(tx.ToByteArray(true));
PhantasmaError err{};
String hash = api.SendRawTransaction(rawTx.c_str(), &err);
```

**Dry‑run a script against state (no commit)**
```cpp
Script res = api.InvokeRawScript("main", Base16::Encode(scriptBytes).c_str());
```

## Accounts

### GetAccount

Returns the account name and balance of given address.

**Returns:** `Account`

**Parameters**

- `account`
  *type:* `const Char*`
- `nullptr`
  *type:* `PhantasmaError* out_error =`

**Example**
```cpp
PhantasmaError err{};
Account acc = api.GetAccount("P2K...", &err);
```

### LookUpName

Returns the address that owns a given name.

**Returns:** `String`

**Parameters**

- `name`
  *type:* `const Char*`
- `nullptr`
  *type:* `PhantasmaError* out_error =`
### GetAddressTransactions

Returns last X transactions of given address. (paginated call)

**Returns:** `AccountTransactions`

**Parameters**

- `account`
  *type:* `const Char*`
- `page`
  *type:* `UInt32`
- `pageSize`
  *type:* `UInt32`
- `nullptr`
  *type:* `PhantasmaError* out_error =`

**Example**
```cpp
AccountTransactions txs = api.GetAddressTransactions("P2K...", /*page*/0, /*pageSize*/50);
```

### GetAddressTransactionCount

Get number of transactions in a specific address and chain

**Returns:** `Int32`

**Parameters**

- `account`
  *type:* `const Char*`
- `chainInput`
  *type:* `const Char*`
- `nullptr`
  *type:* `PhantasmaError* out_error =`
### GetEvents

Reads pending messages from the relay network.

**Returns:** `PHANTASMA_VECTOR<Event>`

**Parameters**

- `account`
  *type:* `const Char*`
- `nullptr`
  *type:* `PhantasmaError* out_error =`


## Blocks

### GetBlockHeight

Returns the height of a chain.

**Returns:** `Int32`

**Parameters**

- `chainInput`
  *type:* `const Char*`
- `nullptr`
  *type:* `PhantasmaError* out_error =`
### GetBlockTransactionCountByHash

Returns the number of transactions in a block. The current RPC call is chain-aware.
The one-argument overload is kept for compatibility and uses `"main"` as the chain.

**Returns:** `Int32`

**Signatures**

```cpp
Int32 GetBlockTransactionCountByHash(const Char* blockHash, PhantasmaError* out_error = nullptr);
Int32 GetBlockTransactionCountByHash(const Char* chainAddressOrName, const Char* blockHash, PhantasmaError* out_error = nullptr);
```

**Parameters**

- `chainAddressOrName`
  *type:* `const Char*`
  Chain name or address. Omit this parameter only when you intentionally want the legacy `"main"` default.
- `blockHash`
  *type:* `const Char*`
- `nullptr`
  *type:* `PhantasmaError* out_error =`

**Example**
```cpp
PhantasmaError err{};
Int32 count = api.GetBlockTransactionCountByHash("main", "ABCD...blockhash", &err);
```
### GetBlockByHash

Returns information about a block by hash.

**Returns:** `Block`

**Parameters**

- `blockHash`
  *type:* `const Char*`
- `nullptr`
  *type:* `PhantasmaError* out_error =`

**Example**
```cpp
Block b = api.GetBlockByHash("ABCD...hash");
```

### GetRawBlockByHash

Returns a serialized string, containing information about a block by hash.

**Returns:** `String`

**Parameters**

- `blockHash`
  *type:* `const Char*`
- `nullptr`
  *type:* `PhantasmaError* out_error =`
### GetBlockByHeight

Returns information about a block by height and chain.

**Returns:** `Block`

**Parameters**

- `chainInput`
  *type:* `const Char*`
- `height`
  *type:* `const Char*`
- `nullptr`
  *type:* `PhantasmaError* out_error =`
### GetRawBlockByHeight

Returns a serialized string, in hex format, containing information about a block by height and chain.

**Returns:** `String`

**Parameters**

- `chainInput`
  *type:* `const Char*`
- `height`
  *type:* `const Char*`
- `nullptr`
  *type:* `PhantasmaError* out_error =`


## Transactions

### GetTransactionByBlockHashAndIndex

Returns the transaction at a block index. The current RPC call is chain-aware.
The two-argument overload is kept for compatibility and uses `"main"` as the chain.

**Returns:** `Transaction`

**Signatures**

```cpp
Transaction GetTransactionByBlockHashAndIndex(const Char* blockHash, Int32 index, PhantasmaError* out_error = nullptr);
Transaction GetTransactionByBlockHashAndIndex(const Char* chainAddressOrName, const Char* blockHash, Int32 index, PhantasmaError* out_error = nullptr);
```

**Parameters**

- `chainAddressOrName`
  *type:* `const Char*`
  Chain name or address. Omit this parameter only when you intentionally want the legacy `"main"` default.
- `blockHash`
  *type:* `const Char*`
- `index`
  *type:* `Int32`
- `nullptr`
  *type:* `PhantasmaError* out_error =`

**Example**
```cpp
Transaction tx = api.GetTransactionByBlockHashAndIndex("main", "ABCD...blockhash", 0);
```
### SendRawTransaction

Allows to broadcast a signed operation on the network, but it&apos;s required to build it manually.

**Returns:** `String`

**Parameters**

- `txData`
  *type:* `const Char*`
- `nullptr`
  *type:* `PhantasmaError* out_error =`

**Example**
```cpp
String rawTx = Base16::Encode(tx.ToByteArray(true));
String hash = api.SendRawTransaction(rawTx.c_str());
```

### GetTransaction

Returns information about a transaction by hash.

**Returns:** `Transaction`

**Parameters**

- `hashText`
  *type:* `const Char*`
- `nullptr`
  *type:* `PhantasmaError* out_error =`

**Example**
```cpp
Transaction tx = api.GetTransaction("ABCD...txhash");
```

### CancelTransaction

Removes a pending transaction from the mempool.

**Returns:** `String`

**Parameters**

- `hashText`
  *type:* `const Char*`
- `nullptr`
  *type:* `PhantasmaError* out_error =`


## Scripting

### InvokeRawScript

Allows to invoke script based on network state, without state changes.

**Returns:** `Script`

**Parameters**

- `chainInput`
  *type:* `const Char*`
- `scriptData`
  *type:* `const Char*`
- `nullptr`
  *type:* `PhantasmaError* out_error =`

**Example**
```cpp
Script out = api.InvokeRawScript("main", Base16::Encode(scriptBytes).c_str());
```



## Nexus/Chains

### GetChains

Returns an array of all chains deployed in Phantasma.

**Returns:** `PHANTASMA_VECTOR<Chain>`

**Parameters**

- `nullptr`
  *type:* `PhantasmaError* out_error =`
### GetNexus

Returns info about the nexus.

**Returns:** `Nexus`

**Parameters**

- `extended`
  *type:* `bool`
- `nullptr`
  *type:* `PhantasmaError* out_error =`
### GetContract

Returns the ABI interface of specific contract.

**Returns:** `Contract`

**Parameters**

- `chainAddressOrName`
  *type:* `const Char*`
- `contractName`
  *type:* `const Char*`
- `nullptr`
  *type:* `PhantasmaError* out_error =`

### GetContracts

Returns the contract list for a chain.

**Returns:** `PHANTASMA_VECTOR<Contract>`

**Parameters**

- `chainAddressOrName`
  *type:* `const Char*`
- `extended`
  *type:* `bool`
- `nullptr`
  *type:* `PhantasmaError* out_error =`

### GetContractByAddress

Returns the ABI interface of a contract by address.

**Returns:** `Contract`

**Parameters**

- `chainAddressOrName`
  *type:* `const Char*`
- `contractAddress`
  *type:* `const Char*`
- `nullptr`
  *type:* `PhantasmaError* out_error =`


## Tokens

### GetTokens

Returns an array of tokens deployed in Phantasma.

**Returns:** `PHANTASMA_VECTOR<Token>`

**Parameters**

- `extended`
  *type:* `bool`
- `ownerAddress`
  *type:* `const Char*`
  Optional overload parameter for filtering tokens by owner address.
- `nullptr`
  *type:* `PhantasmaError* out_error =`

**Signatures**

```cpp
PHANTASMA_VECTOR<Token> GetTokens(bool extended, PhantasmaError* out_error = nullptr);
PHANTASMA_VECTOR<Token> GetTokens(bool extended, const Char* ownerAddress, PhantasmaError* out_error = nullptr);
```
### GetToken

Returns info about a specific token deployed in Phantasma. The Carbon-aware overload accepts `carbonTokenId`; pass `0` when resolving by symbol only.

**Returns:** `Token`

**Signatures**

```cpp
Token GetToken(const Char* symbol, bool extended, PhantasmaError* out_error = nullptr);
Token GetToken(const Char* symbol, bool extended, UInt64 carbonTokenId, PhantasmaError* out_error = nullptr);
```

**Parameters**

- `symbol`
  *type:* `const Char*`
- `extended`
  *type:* `bool`
- `carbonTokenId`
  *type:* `UInt64`
- `nullptr`
  *type:* `PhantasmaError* out_error =`

### GetTokenSeries

Returns token series for a token using cursor pagination.

**Returns:** `CursorPaginatedResult<TokenSeries>`

**Parameters**

- `symbol`
  *type:* `const Char*`
- `carbonTokenId`
  *type:* `UInt64`
- `pageSize`
  *type:* `UInt32`
- `cursor`
  *type:* `const Char*`
- `nullptr`
  *type:* `PhantasmaError* out_error =`

### GetTokenSeriesById

Returns one token series by Phantasma or Carbon identifiers.

**Returns:** `TokenSeries`

**Parameters**

- `symbol`
  *type:* `const Char*`
- `carbonTokenId`
  *type:* `UInt64`
- `seriesId`
  *type:* `const Char*`
- `carbonSeriesId`
  *type:* `UInt32`
- `nullptr`
  *type:* `PhantasmaError* out_error =`

**Example**
```cpp
TokenSeries series = api.GetTokenSeriesById("CROWN", 0, "1", 0);
```

### GetTokenNFTs

Returns NFTs for a token series using cursor pagination.

**Returns:** `CursorPaginatedResult<TokenData>`

**Parameters**

- `carbonTokenId`
  *type:* `UInt64`
- `carbonSeriesId`
  *type:* `UInt32`
- `pageSize`
  *type:* `UInt32`
- `cursor`
  *type:* `const Char*`
- `extended`
  *type:* `bool`
- `nullptr`
  *type:* `PhantasmaError* out_error =`
### GetTokenData

Returns data of a non-fungible token, in hexadecimal format.

**Returns:** `TokenData`

**Parameters**

- `symbol`
  *type:* `const Char*`
- `IDtext`
  *type:* `const Char*`
- `nullptr`
  *type:* `PhantasmaError* out_error =`

### GetNFTs

Returns data for multiple non-fungible token IDs.

**Returns:** `PHANTASMA_VECTOR<TokenData>`

**Parameters**

- `symbol`
  *type:* `const Char*`
- `IDtext`
  *type:* `const Char*`
- `extended`
  *type:* `bool`
- `nullptr`
  *type:* `PhantasmaError* out_error =`

### GetAccountFungibleTokens

Returns fungible token balances owned by an address using cursor pagination.

**Returns:** `CursorPaginatedResult<Balance>`

**Parameters**

- `account`
  *type:* `const Char*`
- `tokenSymbol`
  *type:* `const Char*`
- `carbonTokenId`
  *type:* `UInt64`
- `pageSize`
  *type:* `UInt32`
- `cursor`
  *type:* `const Char*`
- `checkAddressReservedByte`
  *type:* `bool`
- `nullptr`
  *type:* `PhantasmaError* out_error =`

### GetAccountNFTs

Returns NFTs owned by an address using cursor pagination.

**Returns:** `CursorPaginatedResult<TokenData>`

**Parameters**

- `account`
  *type:* `const Char*`
- `tokenSymbol`
  *type:* `const Char*`
- `carbonTokenId`
  *type:* `UInt64`
- `carbonSeriesId`
  *type:* `UInt32`
- `pageSize`
  *type:* `UInt32`
- `cursor`
  *type:* `const Char*`
- `extended`
  *type:* `bool`
- `checkAddressReservedByte`
  *type:* `bool`
- `nullptr`
  *type:* `PhantasmaError* out_error =`

### GetAccountOwnedTokens

Returns NFT token definitions for which the account owns at least one NFT instance.

**Returns:** `CursorPaginatedResult<Token>`

**Parameters**

- `account`
  *type:* `const Char*`
- `tokenSymbol`
  *type:* `const Char*`
- `carbonTokenId`
  *type:* `UInt64`
- `pageSize`
  *type:* `UInt32`
- `cursor`
  *type:* `const Char*`
- `checkAddressReservedByte`
  *type:* `bool`
- `nullptr`
  *type:* `PhantasmaError* out_error =`

### GetAccountOwnedTokenSeries

Returns NFT series for which the account owns at least one NFT instance.

**Returns:** `CursorPaginatedResult<TokenSeries>`

**Parameters**

- `account`
  *type:* `const Char*`
- `tokenSymbol`
  *type:* `const Char*`
- `carbonTokenId`
  *type:* `UInt64`
- `pageSize`
  *type:* `UInt32`
- `cursor`
  *type:* `const Char*`
- `checkAddressReservedByte`
  *type:* `bool`
- `nullptr`
  *type:* `PhantasmaError* out_error =`
### GetNFT

Returns data of a non-fungible token, in hexadecimal format.

**Returns:** `TokenData`

**Parameters**

- `symbol`
  *type:* `const Char*`
- `IDtext`
  *type:* `const Char*`
- `extended`
  *type:* `bool`
- `nullptr`
  *type:* `PhantasmaError* out_error =`
### GetTokenBalance

Returns the balance for a specific token and chain, given an address.

**Returns:** `Balance`

**Parameters**

- `account`
  *type:* `const Char*`
- `tokenSymbol`
  *type:* `const Char*`
- `chainInput`
  *type:* `const Char*`
- `nullptr`
  *type:* `PhantasmaError* out_error =`

**Example**
```cpp
Balance bal = api.GetTokenBalance("P2K...", "SOUL", "main");
```



## Auctions

### GetAuctionsCount

Returns the number of active auctions.

**Returns:** `Int32`

**Parameters**

- `chainAddressOrName`
  *type:* `const Char*`
- `symbol`
  *type:* `const Char*`
- `nullptr`
  *type:* `PhantasmaError* out_error =`
### GetAuctions

Returns the auctions available in the market. (paginated call)

**Returns:** `PHANTASMA_VECTOR<Auction>`

**Parameters**

- `chainAddressOrName`
  *type:* `const Char*`
- `symbol`
  *type:* `const Char*`
- `page`
  *type:* `UInt32`
- `pageSize`
  *type:* `UInt32`
- `nullptr`
  *type:* `PhantasmaError* out_error =`
### GetAuction

Returns the auction for a specific token.

**Returns:** `Auction`

**Parameters**

- `chainAddressOrName`
  *type:* `const Char*`
- `symbol`
  *type:* `const Char*`
- `IDtext`
  *type:* `const Char*`
- `nullptr`
  *type:* `PhantasmaError* out_error =`


## Archives

### GetArchive

Returns info about a specific archive.

**Returns:** `Archive`

**Parameters**

- `hashText`
  *type:* `const Char*`
- `nullptr`
  *type:* `PhantasmaError* out_error =`
### WriteArchive

Writes the contents of an incomplete archive.

**Returns:** `bool`

**Parameters**

- `hashText`
  *type:* `const Char*`
- `blockIndex`
  *type:* `Int32`
- `blockContent`
  *type:* `const Char*`
- `nullptr`
  *type:* `PhantasmaError* out_error =`
### ReadArchive

Reads given archive block.

**Returns:** `String`

**Parameters**

- `hashText`
  *type:* `const Char*`
- `blockIndex`
  *type:* `Int32`
- `nullptr`
  *type:* `PhantasmaError* out_error =`


## Node Metadata

### GetVersion

Returns build metadata reported by the node.

**Returns:** `BuildInfoResult`

**Parameters**

- `nullptr`
  *type:* `PhantasmaError* out_error =`

**Example**
```cpp
BuildInfoResult build = api.GetVersion();
```

### GetPhantasmaVmConfig

Returns the current VM configuration applied by a chain.

**Returns:** `PhantasmaVmConfig`

**Parameters**

- `chainAddressOrName`
  *type:* `const Char*`
- `nullptr`
  *type:* `PhantasmaError* out_error =`

**Example**
```cpp
PhantasmaVmConfig vm = api.GetPhantasmaVmConfig("main");
```


## Relay/Networking

### GetPeers

Returns list of known peers.

**Returns:** `PHANTASMA_VECTOR<Peer>`

**Parameters**

- `nullptr`
  *type:* `PhantasmaError* out_error =`
### RelaySend

Writes a message to the relay network.

**Returns:** `bool`

**Parameters**

- `receiptHex`
  *type:* `const Char*`
- `nullptr`
  *type:* `PhantasmaError* out_error =`
### RelayReceive

Receives messages from the relay network.

**Returns:** `PHANTASMA_VECTOR<Receipt>`

**Parameters**

- `account`
  *type:* `const Char*`
- `nullptr`
  *type:* `PhantasmaError* out_error =`


## Interop/Validators/Swaps

### GetPlatforms

Returns an array of available interop platforms.

**Returns:** `PHANTASMA_VECTOR<Platform>`

**Parameters**

- `nullptr`
  *type:* `PhantasmaError* out_error =`
### GetValidators

Returns an array of available validators.

**Returns:** `PHANTASMA_VECTOR<Validator>`

**Parameters**

- `nullptr`
  *type:* `PhantasmaError* out_error =`
### SettleSwap

Tries to settle a pending swap for a specific hash.

**Returns:** `String`

**Parameters**

- `sourcePlatform`
  *type:* `const Char*`
- `destPlatform`
  *type:* `const Char*`
- `hashText`
  *type:* `const Char*`
- `nullptr`
  *type:* `PhantasmaError* out_error =`
### GetSwapsForAddress

Returns platform swaps for a specific address.

**Returns:** `PHANTASMA_VECTOR<Swap>`

**Parameters**

- `account`
  *type:* `const Char*`
- `nullptr`
  *type:* `PhantasmaError* out_error =`


## Organizations/Governance/Leaderboards

### GetOrganization

Returns info about an organization.

**Returns:** `Organization`

**Parameters**

- `ID`
  *type:* `const Char*`
- `nullptr`
  *type:* `PhantasmaError* out_error =`
### GetLeaderboard

Returns content of a Phantasma leaderboard.

**Returns:** `Leaderboard`

**Parameters**

- `name`
  *type:* `const Char*`
- `nullptr`
  *type:* `PhantasmaError* out_error =`
