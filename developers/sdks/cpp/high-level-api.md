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

Returns the number of transactions of given block hash or error if given hash is invalid or is not found.

**Returns:** `Int32`

**Parameters**

- `blockHash`  
  *type:* `const Char*`
- `nullptr`  
  *type:* `PhantasmaError* out_error =`
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

Returns the information about a transaction requested by a block hash and transaction index.

**Returns:** `Transaction`

**Parameters**

- `blockHash`  
  *type:* `const Char*`
- `index`  
  *type:* `Int32`
- `nullptr`  
  *type:* `PhantasmaError* out_error =`
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


## Tokens

### GetTokens

Returns an array of tokens deployed in Phantasma.

**Returns:** `PHANTASMA_VECTOR<Token>`

**Parameters**

- `extended`  
  *type:* `bool`
- `nullptr`  
  *type:* `PhantasmaError* out_error =`
### GetToken

Returns info about a specific token deployed in Phantasma.

**Returns:** `Token`

**Parameters**

- `symbol`  
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

