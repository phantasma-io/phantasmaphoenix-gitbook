# Low‑Level JSON API (PhantasmaJsonAPI)

The **low‑level API** lets you build RPC requests as raw JSON and parse responses **without** any built‑in HTTP transport. 
You are responsible for POSTing the request body to the node and passing the JSON back for parsing.

- Namespace/class: `phantasma::PhantasmaJsonAPI`
- RPC endpoint path: `PhantasmaJsonAPI::Uri()` → `"/rpc"` (append to your host)
- Types:
  - `JSONBuilder` — a minimal JSON builder (or adapter‑provided builder)
  - `JSONValue` — an adapter‑specific JSON value/view type
  - `PhantasmaError` — `{ code, message }`, with codes: `InvalidJSON`, `HttpError`, `InvalidRpcResponse`, `RpcMessage`

> Tip: For production, include an adapter like **RapidJSON** or **CppRestSDK** to supply robust `JSONValue` and friends. The built‑in `JSONBuilder` is intentionally simple.

## Request/Response lifecycle

1. Create a `JSONBuilder` and call the corresponding `Make*Request` function.  
2. Send an **HTTP POST** to `https://<host>` + `PhantasmaJsonAPI::Uri()` with the builder contents as the body.  
3. Parse the HTTP response into a `JSONValue` (adapter‑specific).  
4. Call the matching `Parse*Response` function to populate your output structure (e.g., `Account`, `Transaction`, `Block`).  

```cpp
// Pseudocode
JSONBuilder req;
PhantasmaJsonAPI::MakeGetAccountRequest(req, "P2K...");

auto body = req.s.str();        // Request body (JSON)
auto respJson = HttpPost("/rpc", body); // Your HTTP code returns JSONValue

Account out{};
PhantasmaError err{};
bool ok = PhantasmaJsonAPI::ParseGetAccountResponse(respJson, out, &err);
if (!ok) {
    // handle err.code / err.message
}
``` 

## Error handling

- Most `Parse*Response` return `bool` and optionally fill `PhantasmaError`  
- `CheckResponse(JSONValue, PhantasmaError&)` normalizes RPC errors (internal)  
- On transport errors, call `OnHttpError(err, "message")` before returning  

## Endpoints

Each endpoint exposes a **pair**: `Make<Name>Request(JSONBuilder, ...)` and `Parse<Name>Response(JSONValue, OutType&, PhantasmaError*)`.

### Cancel Transaction Request

Removes a pending transaction from the mempool.

**Request builder**

```cpp
static void PhantasmaJsonAPI::MakeCancelTransactionRequestRequest(JSONBuilder&, const Char* hashText);
```

**Parameters (request):**

- `JSONBuilder&` — Request builder (writes JSON into an internal buffer)  
  *type:* `JSONBuilder&`
- `hashText` — Transaction or archive hash (hex)  
  *type:* `const Char*`


### Cancel Transaction Response


**Response parser**

```cpp
static bool PhantasmaJsonAPI::ParseCancelTransactionResponseResponse(const JSONValue&, String& out, PhantasmaError* err=0);
```

**Parameters (response):**

- `JSONValue&` — Parameter  
  *type:* `const`
- `out` — Output object populated from the response  
  *type:* `String&`
- `err=0` — Optional error output (code/message)  
  *type:* `PhantasmaError*`


### Get Account Request

Returns the account name and balance of given address.

**Request builder**

```cpp
static void PhantasmaJsonAPI::MakeGetAccountRequestRequest(JSONBuilder&, const Char* account);
```

**Parameters (request):**

- `JSONBuilder&` — Request builder (writes JSON into an internal buffer)  
  *type:* `JSONBuilder&`
- `account` — Account address (P2K...) or name  
  *type:* `const Char*`


### Get Account Response


**Response parser**

```cpp
static bool PhantasmaJsonAPI::ParseGetAccountResponseResponse(const JSONValue&, Account& out, PhantasmaError* err=0);
```

**Parameters (response):**

- `JSONValue&` — Parameter  
  *type:* `const`
- `out` — Output object populated from the response  
  *type:* `Account&`
- `err=0` — Optional error output (code/message)  
  *type:* `PhantasmaError*`


### Get Address Transaction Count Request

Get number of transactions in a specific address and chain

**Request builder**

```cpp
static void PhantasmaJsonAPI::MakeGetAddressTransactionCountRequestRequest(JSONBuilder&, const Char* account, const Char* chainInput);
```

**Parameters (request):**

- `JSONBuilder&` — Request builder (writes JSON into an internal buffer)  
  *type:* `JSONBuilder&`
- `account` — Account address (P2K...) or name  
  *type:* `const Char*`
- `chainInput` — Chain name or address  
  *type:* `const Char*`


### Get Address Transaction Count Response


**Response parser**

```cpp
static bool PhantasmaJsonAPI::ParseGetAddressTransactionCountResponseResponse(const JSONValue&, Int32& out, PhantasmaError* err=0);
```

**Parameters (response):**

- `JSONValue&` — Parameter  
  *type:* `const`
- `out` — Output object populated from the response  
  *type:* `Int32&`
- `err=0` — Optional error output (code/message)  
  *type:* `PhantasmaError*`


### Get Address Transactions Request

Returns last X transactions of given address. (paginated call)

**Request builder**

```cpp
static void PhantasmaJsonAPI::MakeGetAddressTransactionsRequestRequest(JSONBuilder&, const Char* account, UInt32 page, UInt32 pageSize);
```

**Parameters (request):**

- `JSONBuilder&` — Request builder (writes JSON into an internal buffer)  
  *type:* `JSONBuilder&`
- `account` — Account address (P2K...) or name  
  *type:* `const Char*`
- `page` — Page number (0‑based)  
  *type:* `UInt32`
- `pageSize` — Max results per page  
  *type:* `UInt32`


### Get Address Transactions Response


**Response parser**

```cpp
static bool PhantasmaJsonAPI::ParseGetAddressTransactionsResponseResponse(const JSONValue&, AccountTransactions& out, PhantasmaError* err=0);
```

**Parameters (response):**

- `JSONValue&` — Parameter  
  *type:* `const`
- `out` — Output object populated from the response  
  *type:* `AccountTransactions&`
- `err=0` — Optional error output (code/message)  
  *type:* `PhantasmaError*`


### Get Archive Request

Returns info about a specific archive.

**Request builder**

```cpp
static void PhantasmaJsonAPI::MakeGetArchiveRequestRequest(JSONBuilder&, const Char* hashText);
```

**Parameters (request):**

- `JSONBuilder&` — Request builder (writes JSON into an internal buffer)  
  *type:* `JSONBuilder&`
- `hashText` — Transaction or archive hash (hex)  
  *type:* `const Char*`


### Get Archive Response


**Response parser**

```cpp
static bool PhantasmaJsonAPI::ParseGetArchiveResponseResponse(const JSONValue&, Archive& out, PhantasmaError* err=0);
```

**Parameters (response):**

- `JSONValue&` — Parameter  
  *type:* `const`
- `out` — Output object populated from the response  
  *type:* `Archive&`
- `err=0` — Optional error output (code/message)  
  *type:* `PhantasmaError*`


### Get Auction Request

Returns the auction for a specific token.

**Request builder**

```cpp
static void PhantasmaJsonAPI::MakeGetAuctionRequestRequest(JSONBuilder&, const Char* chainAddressOrName, const Char* symbol, const Char* IDtext);
```

**Parameters (request):**

- `JSONBuilder&` — Request builder (writes JSON into an internal buffer)  
  *type:* `JSONBuilder&`
- `chainAddressOrName` — Chain address or name  
  *type:* `const Char*`
- `symbol` — Token symbol (e.g., SOUL, KCAL)  
  *type:* `const Char*`
- `IDtext` — Token ID (string form)  
  *type:* `const Char*`


### Get Auction Response


**Response parser**

```cpp
static bool PhantasmaJsonAPI::ParseGetAuctionResponseResponse(const JSONValue&, Auction& out, PhantasmaError* err=0);
```

**Parameters (response):**

- `JSONValue&` — Parameter  
  *type:* `const`
- `out` — Output object populated from the response  
  *type:* `Auction&`
- `err=0` — Optional error output (code/message)  
  *type:* `PhantasmaError*`


### Get Auctions Count Request

Returns the number of active auctions.

**Request builder**

```cpp
static void PhantasmaJsonAPI::MakeGetAuctionsCountRequestRequest(JSONBuilder&, const Char* chainAddressOrName, const Char* symbol);
```

**Parameters (request):**

- `JSONBuilder&` — Request builder (writes JSON into an internal buffer)  
  *type:* `JSONBuilder&`
- `chainAddressOrName` — Chain address or name  
  *type:* `const Char*`
- `symbol` — Token symbol (e.g., SOUL, KCAL)  
  *type:* `const Char*`


### Get Auctions Count Response


**Response parser**

```cpp
static bool PhantasmaJsonAPI::ParseGetAuctionsCountResponseResponse(const JSONValue&, Int32& out, PhantasmaError* err=0);
```

**Parameters (response):**

- `JSONValue&` — Parameter  
  *type:* `const`
- `out` — Output object populated from the response  
  *type:* `Int32&`
- `err=0` — Optional error output (code/message)  
  *type:* `PhantasmaError*`


### Get Auctions Request

Returns the auctions available in the market. (paginated call)

**Request builder**

```cpp
static void PhantasmaJsonAPI::MakeGetAuctionsRequestRequest(JSONBuilder&, const Char* chainAddressOrName, const Char* symbol, UInt32 page, UInt32 pageSize);
```

**Parameters (request):**

- `JSONBuilder&` — Request builder (writes JSON into an internal buffer)  
  *type:* `JSONBuilder&`
- `chainAddressOrName` — Chain address or name  
  *type:* `const Char*`
- `symbol` — Token symbol (e.g., SOUL, KCAL)  
  *type:* `const Char*`
- `page` — Page number (0‑based)  
  *type:* `UInt32`
- `pageSize` — Max results per page  
  *type:* `UInt32`


### Get Auctions Response


**Response parser**

```cpp
static bool PhantasmaJsonAPI::ParseGetAuctionsResponseResponse(const JSONValue&, PHANTASMA_VECTOR<Auction>& out, PhantasmaError* err=0);
```

**Parameters (response):**

- `JSONValue&` — Parameter  
  *type:* `const`
- `out` — Output object populated from the response  
  *type:* `PHANTASMA_VECTOR<Auction>&`
- `err=0` — Optional error output (code/message)  
  *type:* `PhantasmaError*`


### Get Block By Hash Request

Returns information about a block by hash.

**Request builder**

```cpp
static void PhantasmaJsonAPI::MakeGetBlockByHashRequestRequest(JSONBuilder&, const Char* blockHash);
```

**Parameters (request):**

- `JSONBuilder&` — Request builder (writes JSON into an internal buffer)  
  *type:* `JSONBuilder&`
- `blockHash` — Block hash (hex)  
  *type:* `const Char*`


### Get Block By Hash Response


**Response parser**

```cpp
static bool PhantasmaJsonAPI::ParseGetBlockByHashResponseResponse(const JSONValue&, Block& out, PhantasmaError* err=0);
```

**Parameters (response):**

- `JSONValue&` — Parameter  
  *type:* `const`
- `out` — Output object populated from the response  
  *type:* `Block&`
- `err=0` — Optional error output (code/message)  
  *type:* `PhantasmaError*`


### Get Block By Height Request

Returns information about a block by height and chain.

**Request builder**

```cpp
static void PhantasmaJsonAPI::MakeGetBlockByHeightRequestRequest(JSONBuilder&, const Char* chainInput, const Char* height);
```

**Parameters (request):**

- `JSONBuilder&` — Request builder (writes JSON into an internal buffer)  
  *type:* `JSONBuilder&`
- `chainInput` — Chain name or address  
  *type:* `const Char*`
- `height` — Block height (decimal string)  
  *type:* `const Char*`


### Get Block By Height Response


**Response parser**

```cpp
static bool PhantasmaJsonAPI::ParseGetBlockByHeightResponseResponse(const JSONValue&, Block& out, PhantasmaError* err=0);
```

**Parameters (response):**

- `JSONValue&` — Parameter  
  *type:* `const`
- `out` — Output object populated from the response  
  *type:* `Block&`
- `err=0` — Optional error output (code/message)  
  *type:* `PhantasmaError*`


### Get Block Height Request

Returns the height of a chain.

**Request builder**

```cpp
static void PhantasmaJsonAPI::MakeGetBlockHeightRequestRequest(JSONBuilder&, const Char* chainInput);
```

**Parameters (request):**

- `JSONBuilder&` — Request builder (writes JSON into an internal buffer)  
  *type:* `JSONBuilder&`
- `chainInput` — Chain name or address  
  *type:* `const Char*`


### Get Block Height Response


**Response parser**

```cpp
static bool PhantasmaJsonAPI::ParseGetBlockHeightResponseResponse(const JSONValue&, Int32& out, PhantasmaError* err=0);
```

**Parameters (response):**

- `JSONValue&` — Parameter  
  *type:* `const`
- `out` — Output object populated from the response  
  *type:* `Int32&`
- `err=0` — Optional error output (code/message)  
  *type:* `PhantasmaError*`


### Get Block Transaction Count By Hash Request

Returns the number of transactions of given block hash or error if given hash is invalid or is not found.

**Request builder**

```cpp
static void PhantasmaJsonAPI::MakeGetBlockTransactionCountByHashRequestRequest(JSONBuilder&, const Char* blockHash);
```

**Parameters (request):**

- `JSONBuilder&` — Request builder (writes JSON into an internal buffer)  
  *type:* `JSONBuilder&`
- `blockHash` — Block hash (hex)  
  *type:* `const Char*`


### Get Block Transaction Count By Hash Response


**Response parser**

```cpp
static bool PhantasmaJsonAPI::ParseGetBlockTransactionCountByHashResponseResponse(const JSONValue&, Int32& out, PhantasmaError* err=0);
```

**Parameters (response):**

- `JSONValue&` — Parameter  
  *type:* `const`
- `out` — Output object populated from the response  
  *type:* `Int32&`
- `err=0` — Optional error output (code/message)  
  *type:* `PhantasmaError*`


### Get Chains Request

Returns an array of all chains deployed in Phantasma.

**Request builder**

```cpp
static void PhantasmaJsonAPI::MakeGetChainsRequestRequest(JSONBuilder&);
```

**Parameters (request):**

- `JSONBuilder&` — Request builder (writes JSON into an internal buffer)  
  *type:* `JSONBuilder&`


### Get Chains Response


**Response parser**

```cpp
static bool PhantasmaJsonAPI::ParseGetChainsResponseResponse(const JSONValue&, PHANTASMA_VECTOR<Chain>& out, PhantasmaError* err=0);
```

**Parameters (response):**

- `JSONValue&` — Parameter  
  *type:* `const`
- `out` — Output object populated from the response  
  *type:* `PHANTASMA_VECTOR<Chain>&`
- `err=0` — Optional error output (code/message)  
  *type:* `PhantasmaError*`


### Get Contract Request

Returns the ABI interface of specific contract.

**Request builder**

```cpp
static void PhantasmaJsonAPI::MakeGetContractRequestRequest(JSONBuilder&, const Char* chainAddressOrName, const Char* contractName);
```

**Parameters (request):**

- `JSONBuilder&` — Request builder (writes JSON into an internal buffer)  
  *type:* `JSONBuilder&`
- `chainAddressOrName` — Chain address or name  
  *type:* `const Char*`
- `contractName` — String parameter  
  *type:* `const Char*`


### Get Contract Response


**Response parser**

```cpp
static bool PhantasmaJsonAPI::ParseGetContractResponseResponse(const JSONValue&, Contract& out, PhantasmaError* err=0);
```

**Parameters (response):**

- `JSONValue&` — Parameter  
  *type:* `const`
- `out` — Output object populated from the response  
  *type:* `Contract&`
- `err=0` — Optional error output (code/message)  
  *type:* `PhantasmaError*`


### Get Events Request

Reads pending messages from the relay network.

**Request builder**

```cpp
static void PhantasmaJsonAPI::MakeGetEventsRequestRequest(JSONBuilder&, const Char* account);
```

**Parameters (request):**

- `JSONBuilder&` — Request builder (writes JSON into an internal buffer)  
  *type:* `JSONBuilder&`
- `account` — Account address (P2K...) or name  
  *type:* `const Char*`


### Get Events Response


**Response parser**

```cpp
static bool PhantasmaJsonAPI::ParseGetEventsResponseResponse(const JSONValue&, PHANTASMA_VECTOR<Event>& out, PhantasmaError* err=0);
```

**Parameters (response):**

- `JSONValue&` — Parameter  
  *type:* `const`
- `out` — Output object populated from the response  
  *type:* `PHANTASMA_VECTOR<Event>&`
- `err=0` — Optional error output (code/message)  
  *type:* `PhantasmaError*`


### Get Leaderboard Request

Returns content of a Phantasma leaderboard.

**Request builder**

```cpp
static void PhantasmaJsonAPI::MakeGetLeaderboardRequestRequest(JSONBuilder&, const Char* name);
```

**Parameters (request):**

- `JSONBuilder&` — Request builder (writes JSON into an internal buffer)  
  *type:* `JSONBuilder&`
- `name` — Account name (lookup)  
  *type:* `const Char*`


### Get Leaderboard Response


**Response parser**

```cpp
static bool PhantasmaJsonAPI::ParseGetLeaderboardResponseResponse(const JSONValue&, Leaderboard& out, PhantasmaError* err=0);
```

**Parameters (response):**

- `JSONValue&` — Parameter  
  *type:* `const`
- `out` — Output object populated from the response  
  *type:* `Leaderboard&`
- `err=0` — Optional error output (code/message)  
  *type:* `PhantasmaError*`


### Get N F T Request

Returns data of a non-fungible token, in hexadecimal format.

**Request builder**

```cpp
static void PhantasmaJsonAPI::MakeGetNFTRequestRequest(JSONBuilder&, const Char* symbol, const Char* IDtext, bool extended);
```

**Parameters (request):**

- `JSONBuilder&` — Request builder (writes JSON into an internal buffer)  
  *type:* `JSONBuilder&`
- `symbol` — Token symbol (e.g., SOUL, KCAL)  
  *type:* `const Char*`
- `IDtext` — Token ID (string form)  
  *type:* `const Char*`
- `extended` — If true, include extended fields  
  *type:* `bool`


### Get N F T Response


**Response parser**

```cpp
static bool PhantasmaJsonAPI::ParseGetNFTResponseResponse(const JSONValue&, TokenData& out, PhantasmaError* err=0);
```

**Parameters (response):**

- `JSONValue&` — Parameter  
  *type:* `const`
- `out` — Output object populated from the response  
  *type:* `TokenData&`
- `err=0` — Optional error output (code/message)  
  *type:* `PhantasmaError*`


### Get Nexus Request

Returns info about the nexus.

**Request builder**

```cpp
static void PhantasmaJsonAPI::MakeGetNexusRequestRequest(JSONBuilder&, bool extended);
```

**Parameters (request):**

- `JSONBuilder&` — Request builder (writes JSON into an internal buffer)  
  *type:* `JSONBuilder&`
- `extended` — If true, include extended fields  
  *type:* `bool`


### Get Nexus Response


**Response parser**

```cpp
static bool PhantasmaJsonAPI::ParseGetNexusResponseResponse(const JSONValue&, Nexus& out, PhantasmaError* err=0);
```

**Parameters (response):**

- `JSONValue&` — Parameter  
  *type:* `const`
- `out` — Output object populated from the response  
  *type:* `Nexus&`
- `err=0` — Optional error output (code/message)  
  *type:* `PhantasmaError*`


### Get Organization Request

Returns info about an organization.

**Request builder**

```cpp
static void PhantasmaJsonAPI::MakeGetOrganizationRequestRequest(JSONBuilder&, const Char* ID);
```

**Parameters (request):**

- `JSONBuilder&` — Request builder (writes JSON into an internal buffer)  
  *type:* `JSONBuilder&`
- `ID` — String parameter  
  *type:* `const Char*`


### Get Organization Response


**Response parser**

```cpp
static bool PhantasmaJsonAPI::ParseGetOrganizationResponseResponse(const JSONValue&, Organization& out, PhantasmaError* err=0);
```

**Parameters (response):**

- `JSONValue&` — Parameter  
  *type:* `const`
- `out` — Output object populated from the response  
  *type:* `Organization&`
- `err=0` — Optional error output (code/message)  
  *type:* `PhantasmaError*`


### Get Peers Request

Returns list of known peers.

**Request builder**

```cpp
static void PhantasmaJsonAPI::MakeGetPeersRequestRequest(JSONBuilder&);
```

**Parameters (request):**

- `JSONBuilder&` — Request builder (writes JSON into an internal buffer)  
  *type:* `JSONBuilder&`


### Get Peers Response


**Response parser**

```cpp
static bool PhantasmaJsonAPI::ParseGetPeersResponseResponse(const JSONValue&, PHANTASMA_VECTOR<Peer>& out, PhantasmaError* err=0);
```

**Parameters (response):**

- `JSONValue&` — Parameter  
  *type:* `const`
- `out` — Output object populated from the response  
  *type:* `PHANTASMA_VECTOR<Peer>&`
- `err=0` — Optional error output (code/message)  
  *type:* `PhantasmaError*`


### Get Platforms Request

Returns an array of available interop platforms.

**Request builder**

```cpp
static void PhantasmaJsonAPI::MakeGetPlatformsRequestRequest(JSONBuilder&);
```

**Parameters (request):**

- `JSONBuilder&` — Request builder (writes JSON into an internal buffer)  
  *type:* `JSONBuilder&`


### Get Platforms Response


**Response parser**

```cpp
static bool PhantasmaJsonAPI::ParseGetPlatformsResponseResponse(const JSONValue&, PHANTASMA_VECTOR<Platform>& out, PhantasmaError* err=0);
```

**Parameters (response):**

- `JSONValue&` — Parameter  
  *type:* `const`
- `out` — Output object populated from the response  
  *type:* `PHANTASMA_VECTOR<Platform>&`
- `err=0` — Optional error output (code/message)  
  *type:* `PhantasmaError*`


### Get Raw Block By Hash Request

Returns a serialized string, containing information about a block by hash.

**Request builder**

```cpp
static void PhantasmaJsonAPI::MakeGetRawBlockByHashRequestRequest(JSONBuilder&, const Char* blockHash);
```

**Parameters (request):**

- `JSONBuilder&` — Request builder (writes JSON into an internal buffer)  
  *type:* `JSONBuilder&`
- `blockHash` — Block hash (hex)  
  *type:* `const Char*`


### Get Raw Block By Hash Response


**Response parser**

```cpp
static bool PhantasmaJsonAPI::ParseGetRawBlockByHashResponseResponse(const JSONValue&, String& out, PhantasmaError* err=0);
```

**Parameters (response):**

- `JSONValue&` — Parameter  
  *type:* `const`
- `out` — Output object populated from the response  
  *type:* `String&`
- `err=0` — Optional error output (code/message)  
  *type:* `PhantasmaError*`


### Get Raw Block By Height Request

Returns a serialized string, in hex format, containing information about a block by height and chain.

**Request builder**

```cpp
static void PhantasmaJsonAPI::MakeGetRawBlockByHeightRequestRequest(JSONBuilder&, const Char* chainInput, const Char* height);
```

**Parameters (request):**

- `JSONBuilder&` — Request builder (writes JSON into an internal buffer)  
  *type:* `JSONBuilder&`
- `chainInput` — Chain name or address  
  *type:* `const Char*`
- `height` — Block height (decimal string)  
  *type:* `const Char*`


### Get Raw Block By Height Response


**Response parser**

```cpp
static bool PhantasmaJsonAPI::ParseGetRawBlockByHeightResponseResponse(const JSONValue&, String& out, PhantasmaError* err=0);
```

**Parameters (response):**

- `JSONValue&` — Parameter  
  *type:* `const`
- `out` — Output object populated from the response  
  *type:* `String&`
- `err=0` — Optional error output (code/message)  
  *type:* `PhantasmaError*`


### Get Swaps For Address Request

Returns platform swaps for a specific address.

**Request builder**

```cpp
static void PhantasmaJsonAPI::MakeGetSwapsForAddressRequestRequest(JSONBuilder&, const Char* account);
```

**Parameters (request):**

- `JSONBuilder&` — Request builder (writes JSON into an internal buffer)  
  *type:* `JSONBuilder&`
- `account` — Account address (P2K...) or name  
  *type:* `const Char*`


### Get Swaps For Address Response


**Response parser**

```cpp
static bool PhantasmaJsonAPI::ParseGetSwapsForAddressResponseResponse(const JSONValue&, PHANTASMA_VECTOR<Swap>& out, PhantasmaError* err=0);
```

**Parameters (response):**

- `JSONValue&` — Parameter  
  *type:* `const`
- `out` — Output object populated from the response  
  *type:* `PHANTASMA_VECTOR<Swap>&`
- `err=0` — Optional error output (code/message)  
  *type:* `PhantasmaError*`


### Get Token Balance Request

Returns the balance for a specific token and chain, given an address.

**Request builder**

```cpp
static void PhantasmaJsonAPI::MakeGetTokenBalanceRequestRequest(JSONBuilder&, const Char* account, const Char* tokenSymbol, const Char* chainInput);
```

**Parameters (request):**

- `JSONBuilder&` — Request builder (writes JSON into an internal buffer)  
  *type:* `JSONBuilder&`
- `account` — Account address (P2K...) or name  
  *type:* `const Char*`
- `tokenSymbol` — Token symbol (e.g., SOUL, KCAL)  
  *type:* `const Char*`
- `chainInput` — Chain name or address  
  *type:* `const Char*`


### Get Token Balance Response


**Response parser**

```cpp
static bool PhantasmaJsonAPI::ParseGetTokenBalanceResponseResponse(const JSONValue&, Balance& out, PhantasmaError* err=0);
```

**Parameters (response):**

- `JSONValue&` — Parameter  
  *type:* `const`
- `out` — Output object populated from the response  
  *type:* `Balance&`
- `err=0` — Optional error output (code/message)  
  *type:* `PhantasmaError*`


### Get Token Data Request

Returns data of a non-fungible token, in hexadecimal format.

**Request builder**

```cpp
static void PhantasmaJsonAPI::MakeGetTokenDataRequestRequest(JSONBuilder&, const Char* symbol, const Char* IDtext);
```

**Parameters (request):**

- `JSONBuilder&` — Request builder (writes JSON into an internal buffer)  
  *type:* `JSONBuilder&`
- `symbol` — Token symbol (e.g., SOUL, KCAL)  
  *type:* `const Char*`
- `IDtext` — Token ID (string form)  
  *type:* `const Char*`


### Get Token Data Response


**Response parser**

```cpp
static bool PhantasmaJsonAPI::ParseGetTokenDataResponseResponse(const JSONValue&, TokenData& out, PhantasmaError* err=0);
```

**Parameters (response):**

- `JSONValue&` — Parameter  
  *type:* `const`
- `out` — Output object populated from the response  
  *type:* `TokenData&`
- `err=0` — Optional error output (code/message)  
  *type:* `PhantasmaError*`


### Get Token Request

Returns info about a specific token deployed in Phantasma.

**Request builder**

```cpp
static void PhantasmaJsonAPI::MakeGetTokenRequestRequest(JSONBuilder&, const Char* symbol, bool extended);
```

**Parameters (request):**

- `JSONBuilder&` — Request builder (writes JSON into an internal buffer)  
  *type:* `JSONBuilder&`
- `symbol` — Token symbol (e.g., SOUL, KCAL)  
  *type:* `const Char*`
- `extended` — If true, include extended fields  
  *type:* `bool`


### Get Token Response


**Response parser**

```cpp
static bool PhantasmaJsonAPI::ParseGetTokenResponseResponse(const JSONValue&, Token& out, PhantasmaError* err=0);
```

**Parameters (response):**

- `JSONValue&` — Parameter  
  *type:* `const`
- `out` — Output object populated from the response  
  *type:* `Token&`
- `err=0` — Optional error output (code/message)  
  *type:* `PhantasmaError*`


### Get Tokens Request

Returns an array of tokens deployed in Phantasma.

**Request builder**

```cpp
static void PhantasmaJsonAPI::MakeGetTokensRequestRequest(JSONBuilder&, bool extended);
```

**Parameters (request):**

- `JSONBuilder&` — Request builder (writes JSON into an internal buffer)  
  *type:* `JSONBuilder&`
- `extended` — If true, include extended fields  
  *type:* `bool`


### Get Tokens Response


**Response parser**

```cpp
static bool PhantasmaJsonAPI::ParseGetTokensResponseResponse(const JSONValue&, PHANTASMA_VECTOR<Token>& out, PhantasmaError* err=0);
```

**Parameters (response):**

- `JSONValue&` — Parameter  
  *type:* `const`
- `out` — Output object populated from the response  
  *type:* `PHANTASMA_VECTOR<Token>&`
- `err=0` — Optional error output (code/message)  
  *type:* `PhantasmaError*`


### Get Transaction By Block Hash And Index Request

Returns the information about a transaction requested by a block hash and transaction index.

**Request builder**

```cpp
static void PhantasmaJsonAPI::MakeGetTransactionByBlockHashAndIndexRequestRequest(JSONBuilder&, const Char* blockHash, Int32 index);
```

**Parameters (request):**

- `JSONBuilder&` — Request builder (writes JSON into an internal buffer)  
  *type:* `JSONBuilder&`
- `blockHash` — Block hash (hex)  
  *type:* `const Char*`
- `index` — Transaction index within the block  
  *type:* `Int32`


### Get Transaction By Block Hash And Index Response


**Response parser**

```cpp
static bool PhantasmaJsonAPI::ParseGetTransactionByBlockHashAndIndexResponseResponse(const JSONValue&, Transaction& out, PhantasmaError* err=0);
```

**Parameters (response):**

- `JSONValue&` — Parameter  
  *type:* `const`
- `out` — Output object populated from the response  
  *type:* `Transaction&`
- `err=0` — Optional error output (code/message)  
  *type:* `PhantasmaError*`


### Get Transaction Request

Returns information about a transaction by hash.

**Request builder**

```cpp
static void PhantasmaJsonAPI::MakeGetTransactionRequestRequest(JSONBuilder&, const Char* hashText);
```

**Parameters (request):**

- `JSONBuilder&` — Request builder (writes JSON into an internal buffer)  
  *type:* `JSONBuilder&`
- `hashText` — Transaction or archive hash (hex)  
  *type:* `const Char*`


### Get Transaction Response


**Response parser**

```cpp
static bool PhantasmaJsonAPI::ParseGetTransactionResponseResponse(const JSONValue&, Transaction& out, PhantasmaError* err=0);
```

**Parameters (response):**

- `JSONValue&` — Parameter  
  *type:* `const`
- `out` — Output object populated from the response  
  *type:* `Transaction&`
- `err=0` — Optional error output (code/message)  
  *type:* `PhantasmaError*`


### Get Validators Request

Returns an array of available validators.

**Request builder**

```cpp
static void PhantasmaJsonAPI::MakeGetValidatorsRequestRequest(JSONBuilder&);
```

**Parameters (request):**

- `JSONBuilder&` — Request builder (writes JSON into an internal buffer)  
  *type:* `JSONBuilder&`


### Get Validators Response


**Response parser**

```cpp
static bool PhantasmaJsonAPI::ParseGetValidatorsResponseResponse(const JSONValue&, PHANTASMA_VECTOR<Validator>& out, PhantasmaError* err=0);
```

**Parameters (response):**

- `JSONValue&` — Parameter  
  *type:* `const`
- `out` — Output object populated from the response  
  *type:* `PHANTASMA_VECTOR<Validator>&`
- `err=0` — Optional error output (code/message)  
  *type:* `PhantasmaError*`


### Invoke Raw Script Request

Allows to invoke script based on network state, without state changes.

**Request builder**

```cpp
static void PhantasmaJsonAPI::MakeInvokeRawScriptRequestRequest(JSONBuilder&, const Char* chainInput, const Char* scriptData);
```

**Parameters (request):**

- `JSONBuilder&` — Request builder (writes JSON into an internal buffer)  
  *type:* `JSONBuilder&`
- `chainInput` — Chain name or address  
  *type:* `const Char*`
- `scriptData` — Raw script bytes (hex/Base16)  
  *type:* `const Char*`


### Invoke Raw Script Response


**Response parser**

```cpp
static bool PhantasmaJsonAPI::ParseInvokeRawScriptResponseResponse(const JSONValue&, Script& out, PhantasmaError* err=0);
```

**Parameters (response):**

- `JSONValue&` — Parameter  
  *type:* `const`
- `out` — Output object populated from the response  
  *type:* `Script&`
- `err=0` — Optional error output (code/message)  
  *type:* `PhantasmaError*`


### Look Up Name Request

Returns the address that owns a given name.

**Request builder**

```cpp
static void PhantasmaJsonAPI::MakeLookUpNameRequestRequest(JSONBuilder&, const Char* name);
```

**Parameters (request):**

- `JSONBuilder&` — Request builder (writes JSON into an internal buffer)  
  *type:* `JSONBuilder&`
- `name` — Account name (lookup)  
  *type:* `const Char*`


### Look Up Name Response


**Response parser**

```cpp
static bool PhantasmaJsonAPI::ParseLookUpNameResponseResponse(const JSONValue&, String& out, PhantasmaError* err=0);
```

**Parameters (response):**

- `JSONValue&` — Parameter  
  *type:* `const`
- `out` — Output object populated from the response  
  *type:* `String&`
- `err=0` — Optional error output (code/message)  
  *type:* `PhantasmaError*`


### Read Archive Request

Reads given archive block.

**Request builder**

```cpp
static void PhantasmaJsonAPI::MakeReadArchiveRequestRequest(JSONBuilder&, const Char* hashText, Int32 blockIndex);
```

**Parameters (request):**

- `JSONBuilder&` — Request builder (writes JSON into an internal buffer)  
  *type:* `JSONBuilder&`
- `hashText` — Transaction or archive hash (hex)  
  *type:* `const Char*`
- `blockIndex` — Archive block index  
  *type:* `Int32`


### Read Archive Response


**Response parser**

```cpp
static bool PhantasmaJsonAPI::ParseReadArchiveResponseResponse(const JSONValue&, String& out, PhantasmaError* err=0);
```

**Parameters (response):**

- `JSONValue&` — Parameter  
  *type:* `const`
- `out` — Output object populated from the response  
  *type:* `String&`
- `err=0` — Optional error output (code/message)  
  *type:* `PhantasmaError*`


### Relay Receive Request

Receives messages from the relay network.

**Request builder**

```cpp
static void PhantasmaJsonAPI::MakeRelayReceiveRequestRequest(JSONBuilder&, const Char* account);
```

**Parameters (request):**

- `JSONBuilder&` — Request builder (writes JSON into an internal buffer)  
  *type:* `JSONBuilder&`
- `account` — Account address (P2K...) or name  
  *type:* `const Char*`


### Relay Receive Response


**Response parser**

```cpp
static bool PhantasmaJsonAPI::ParseRelayReceiveResponseResponse(const JSONValue&, PHANTASMA_VECTOR<Receipt>& out, PhantasmaError* err=0);
```

**Parameters (response):**

- `JSONValue&` — Parameter  
  *type:* `const`
- `out` — Output object populated from the response  
  *type:* `PHANTASMA_VECTOR<Receipt>&`
- `err=0` — Optional error output (code/message)  
  *type:* `PhantasmaError*`


### Relay Send Request

Writes a message to the relay network.

**Request builder**

```cpp
static void PhantasmaJsonAPI::MakeRelaySendRequestRequest(JSONBuilder&, const Char* receiptHex);
```

**Parameters (request):**

- `JSONBuilder&` — Request builder (writes JSON into an internal buffer)  
  *type:* `JSONBuilder&`
- `receiptHex` — String parameter  
  *type:* `const Char*`


### Relay Send Response


**Response parser**

```cpp
static bool PhantasmaJsonAPI::ParseRelaySendResponseResponse(const JSONValue&, bool& out, PhantasmaError* err=0);
```

**Parameters (response):**

- `JSONValue&` — Parameter  
  *type:* `const`
- `out` — Output object populated from the response  
  *type:* `bool&`
- `err=0` — Optional error output (code/message)  
  *type:* `PhantasmaError*`


### Send Raw Transaction Request

Allows to broadcast a signed operation on the network, but it&apos;s required to build it manually.

**Request builder**

```cpp
static void PhantasmaJsonAPI::MakeSendRawTransactionRequestRequest(JSONBuilder&, const Char* txData);
```

**Parameters (request):**

- `JSONBuilder&` — Request builder (writes JSON into an internal buffer)  
  *type:* `JSONBuilder&`
- `txData` — Raw transaction data (hex/Base16)  
  *type:* `const Char*`


### Send Raw Transaction Response


**Response parser**

```cpp
static bool PhantasmaJsonAPI::ParseSendRawTransactionResponseResponse(const JSONValue&, String& out, PhantasmaError* err=0);
```

**Parameters (response):**

- `JSONValue&` — Parameter  
  *type:* `const`
- `out` — Output object populated from the response  
  *type:* `String&`
- `err=0` — Optional error output (code/message)  
  *type:* `PhantasmaError*`


### Settle Swap Request

Tries to settle a pending swap for a specific hash.

**Request builder**

```cpp
static void PhantasmaJsonAPI::MakeSettleSwapRequestRequest(JSONBuilder&, const Char* sourcePlatform, const Char* destPlatform, const Char* hashText);
```

**Parameters (request):**

- `JSONBuilder&` — Request builder (writes JSON into an internal buffer)  
  *type:* `JSONBuilder&`
- `sourcePlatform` — Source platform name  
  *type:* `const Char*`
- `destPlatform` — Destination platform name  
  *type:* `const Char*`
- `hashText` — Transaction or archive hash (hex)  
  *type:* `const Char*`


### Settle Swap Response


**Response parser**

```cpp
static bool PhantasmaJsonAPI::ParseSettleSwapResponseResponse(const JSONValue&, String& out, PhantasmaError* err=0);
```

**Parameters (response):**

- `JSONValue&` — Parameter  
  *type:* `const`
- `out` — Output object populated from the response  
  *type:* `String&`
- `err=0` — Optional error output (code/message)  
  *type:* `PhantasmaError*`


### Write Archive Request

Writes the contents of an incomplete archive.

**Request builder**

```cpp
static void PhantasmaJsonAPI::MakeWriteArchiveRequestRequest(JSONBuilder&, const Char* hashText, Int32 blockIndex, const Char* blockContent);
```

**Parameters (request):**

- `JSONBuilder&` — Request builder (writes JSON into an internal buffer)  
  *type:* `JSONBuilder&`
- `hashText` — Transaction or archive hash (hex)  
  *type:* `const Char*`
- `blockIndex` — Archive block index  
  *type:* `Int32`
- `blockContent` — Archive block contents (hex/Base16)  
  *type:* `const Char*`


### Write Archive Response


**Response parser**

```cpp
static bool PhantasmaJsonAPI::ParseWriteArchiveResponseResponse(const JSONValue&, bool& out, PhantasmaError* err=0);
```

**Parameters (response):**

- `JSONValue&` — Parameter  
  *type:* `const`
- `out` — Output object populated from the response  
  *type:* `bool&`
- `err=0` — Optional error output (code/message)  
  *type:* `PhantasmaError*`

