# Low‑Level JSON API (PhantasmaJsonAPI)

The **low‑level API** lets you build RPC requests as raw JSON and parse responses **without** any built‑in HTTP transport.
You are responsible for POSTing the request body to the node and passing the JSON back for parsing.

- Namespace/class: `phantasma::rpc::PhantasmaJsonAPI`
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
static void PhantasmaJsonAPI::MakeCancelTransactionRequest(JSONBuilder&, const Char* hashText);
```

**Parameters (request):**

- `JSONBuilder&` — Request builder (writes JSON into an internal buffer)
  *type:* `JSONBuilder&`
- `hashText` — Transaction or archive hash (hex)
  *type:* `const Char*`


### Cancel Transaction Response


**Response parser**

```cpp
static bool PhantasmaJsonAPI::ParseCancelTransactionResponse(const JSONValue&, String& out, PhantasmaError* err=0);
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
static void PhantasmaJsonAPI::MakeGetAccountRequest(JSONBuilder&, const Char* account);
```

**Parameters (request):**

- `JSONBuilder&` — Request builder (writes JSON into an internal buffer)
  *type:* `JSONBuilder&`
- `account` — Account address (P2K...) or name
  *type:* `const Char*`


### Get Account Response


**Response parser**

```cpp
static bool PhantasmaJsonAPI::ParseGetAccountResponse(const JSONValue&, Account& out, PhantasmaError* err=0);
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
static void PhantasmaJsonAPI::MakeGetAddressTransactionCountRequest(JSONBuilder&, const Char* account, const Char* chainInput);
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
static bool PhantasmaJsonAPI::ParseGetAddressTransactionCountResponse(const JSONValue&, Int32& out, PhantasmaError* err=0);
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
static void PhantasmaJsonAPI::MakeGetAddressTransactionsRequest(JSONBuilder&, const Char* account, UInt32 page, UInt32 pageSize);
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
static bool PhantasmaJsonAPI::ParseGetAddressTransactionsResponse(const JSONValue&, AccountTransactions& out, PhantasmaError* err=0);
```

**Parameters (response):**

- `JSONValue&` — Parameter
  *type:* `const`
- `out` — Output object populated from the response
  *type:* `AccountTransactions&`
- `err=0` — Optional error output (code/message)
  *type:* `PhantasmaError*`


### Get Account Fungible Tokens Request

Returns fungible token balances owned by an address using cursor pagination.

**Request builder**

```cpp
static void PhantasmaJsonAPI::MakeGetAccountFungibleTokensRequest(JSONBuilder&, const Char* account, const Char* tokenSymbol, UInt64 carbonTokenId, UInt32 pageSize, const Char* cursor, bool checkAddressReservedByte);
```

**Parameters (request):**

- `JSONBuilder&` — Request builder (writes JSON into an internal buffer)
  *type:* `JSONBuilder&`
- `account` — Account address or name
  *type:* `const Char*`
- `tokenSymbol` — Optional token symbol filter
  *type:* `const Char*`
- `carbonTokenId` — Carbon token id. Use `0` when resolving by symbol only.
  *type:* `UInt64`
- `pageSize` — Maximum number of items to return
  *type:* `UInt32`
- `cursor` — Cursor returned by the previous page, or an empty string for the first page
  *type:* `const Char*`
- `checkAddressReservedByte` — Validate the address reserved byte when true
  *type:* `bool`


### Get Account Fungible Tokens Response

**Response parser**

```cpp
static bool PhantasmaJsonAPI::ParseGetAccountFungibleTokensResponse(const JSONValue&, CursorPaginatedResult<Balance>& out, PhantasmaError* err=0);
```

**Parameters (response):**

- `JSONValue&` — Parameter
  *type:* `const`
- `out` — Output object populated from the response
  *type:* `CursorPaginatedResult<Balance>&`
- `err=0` — Optional error output (code/message)
  *type:* `PhantasmaError*`


### Get Account NFTs Request

Returns NFTs owned by an address using cursor pagination.

**Request builder**

```cpp
static void PhantasmaJsonAPI::MakeGetAccountNFTsRequest(JSONBuilder&, const Char* account, const Char* tokenSymbol, UInt64 carbonTokenId, UInt32 carbonSeriesId, UInt32 pageSize, const Char* cursor, bool extended, bool checkAddressReservedByte);
```

**Parameters (request):**

- `JSONBuilder&` — Request builder (writes JSON into an internal buffer)
  *type:* `JSONBuilder&`
- `account` — Account address or name
  *type:* `const Char*`
- `tokenSymbol` — Optional token symbol filter
  *type:* `const Char*`
- `carbonTokenId` — Carbon token id. Use `0` when resolving by symbol only.
  *type:* `UInt64`
- `carbonSeriesId` — Carbon series id
  *type:* `UInt32`
- `pageSize` — Maximum number of items to return
  *type:* `UInt32`
- `cursor` — Cursor returned by the previous page, or an empty string for the first page
  *type:* `const Char*`
- `extended` — If true, include extended fields
  *type:* `bool`
- `checkAddressReservedByte` — Validate the address reserved byte when true
  *type:* `bool`


### Get Account NFTs Response

**Response parser**

```cpp
static bool PhantasmaJsonAPI::ParseGetAccountNFTsResponse(const JSONValue&, CursorPaginatedResult<TokenData>& out, PhantasmaError* err=0);
```

**Parameters (response):**

- `JSONValue&` — Parameter
  *type:* `const`
- `out` — Output object populated from the response
  *type:* `CursorPaginatedResult<TokenData>&`
- `err=0` — Optional error output (code/message)
  *type:* `PhantasmaError*`


### Get Account Owned Tokens Request

Returns NFT token definitions for which the account owns at least one NFT instance.

**Request builder**

```cpp
static void PhantasmaJsonAPI::MakeGetAccountOwnedTokensRequest(JSONBuilder&, const Char* account, const Char* tokenSymbol, UInt64 carbonTokenId, UInt32 pageSize, const Char* cursor, bool checkAddressReservedByte);
```

**Parameters (request):**

- `JSONBuilder&` — Request builder (writes JSON into an internal buffer)
  *type:* `JSONBuilder&`
- `account` — Account address or name
  *type:* `const Char*`
- `tokenSymbol` — Optional token symbol filter
  *type:* `const Char*`
- `carbonTokenId` — Carbon token id. Use `0` when resolving by symbol only.
  *type:* `UInt64`
- `pageSize` — Maximum number of items to return
  *type:* `UInt32`
- `cursor` — Cursor returned by the previous page, or an empty string for the first page
  *type:* `const Char*`
- `checkAddressReservedByte` — Validate the address reserved byte when true
  *type:* `bool`


### Get Account Owned Tokens Response

**Response parser**

```cpp
static bool PhantasmaJsonAPI::ParseGetAccountOwnedTokensResponse(const JSONValue&, CursorPaginatedResult<Token>& out, PhantasmaError* err=0);
```

**Parameters (response):**

- `JSONValue&` — Parameter
  *type:* `const`
- `out` — Output object populated from the response
  *type:* `CursorPaginatedResult<Token>&`
- `err=0` — Optional error output (code/message)
  *type:* `PhantasmaError*`


### Get Account Owned Token Series Request

Returns NFT series for which the account owns at least one NFT instance.

**Request builder**

```cpp
static void PhantasmaJsonAPI::MakeGetAccountOwnedTokenSeriesRequest(JSONBuilder&, const Char* account, const Char* tokenSymbol, UInt64 carbonTokenId, UInt32 pageSize, const Char* cursor, bool checkAddressReservedByte);
```

**Parameters (request):**

- `JSONBuilder&` — Request builder (writes JSON into an internal buffer)
  *type:* `JSONBuilder&`
- `account` — Account address or name
  *type:* `const Char*`
- `tokenSymbol` — Optional token symbol filter
  *type:* `const Char*`
- `carbonTokenId` — Carbon token id. Use `0` when resolving by symbol only.
  *type:* `UInt64`
- `pageSize` — Maximum number of items to return
  *type:* `UInt32`
- `cursor` — Cursor returned by the previous page, or an empty string for the first page
  *type:* `const Char*`
- `checkAddressReservedByte` — Validate the address reserved byte when true
  *type:* `bool`


### Get Account Owned Token Series Response

**Response parser**

```cpp
static bool PhantasmaJsonAPI::ParseGetAccountOwnedTokenSeriesResponse(const JSONValue&, CursorPaginatedResult<TokenSeries>& out, PhantasmaError* err=0);
```

**Parameters (response):**

- `JSONValue&` — Parameter
  *type:* `const`
- `out` — Output object populated from the response
  *type:* `CursorPaginatedResult<TokenSeries>&`
- `err=0` — Optional error output (code/message)
  *type:* `PhantasmaError*`


### Get Archive Request

Returns info about a specific archive.

**Request builder**

```cpp
static void PhantasmaJsonAPI::MakeGetArchiveRequest(JSONBuilder&, const Char* hashText);
```

**Parameters (request):**

- `JSONBuilder&` — Request builder (writes JSON into an internal buffer)
  *type:* `JSONBuilder&`
- `hashText` — Transaction or archive hash (hex)
  *type:* `const Char*`


### Get Archive Response


**Response parser**

```cpp
static bool PhantasmaJsonAPI::ParseGetArchiveResponse(const JSONValue&, Archive& out, PhantasmaError* err=0);
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
static void PhantasmaJsonAPI::MakeGetAuctionRequest(JSONBuilder&, const Char* chainAddressOrName, const Char* symbol, const Char* IDtext);
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
static bool PhantasmaJsonAPI::ParseGetAuctionResponse(const JSONValue&, Auction& out, PhantasmaError* err=0);
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
static void PhantasmaJsonAPI::MakeGetAuctionsCountRequest(JSONBuilder&, const Char* chainAddressOrName, const Char* symbol);
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
static bool PhantasmaJsonAPI::ParseGetAuctionsCountResponse(const JSONValue&, Int32& out, PhantasmaError* err=0);
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
static void PhantasmaJsonAPI::MakeGetAuctionsRequest(JSONBuilder&, const Char* chainAddressOrName, const Char* symbol, UInt32 page, UInt32 pageSize);
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
static bool PhantasmaJsonAPI::ParseGetAuctionsResponse(const JSONValue&, PHANTASMA_VECTOR<Auction>& out, PhantasmaError* err=0);
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
static void PhantasmaJsonAPI::MakeGetBlockByHashRequest(JSONBuilder&, const Char* blockHash);
```

**Parameters (request):**

- `JSONBuilder&` — Request builder (writes JSON into an internal buffer)
  *type:* `JSONBuilder&`
- `blockHash` — Block hash (hex)
  *type:* `const Char*`


### Get Block By Hash Response


**Response parser**

```cpp
static bool PhantasmaJsonAPI::ParseGetBlockByHashResponse(const JSONValue&, Block& out, PhantasmaError* err=0);
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
static void PhantasmaJsonAPI::MakeGetBlockByHeightRequest(JSONBuilder&, const Char* chainInput, const Char* height);
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
static bool PhantasmaJsonAPI::ParseGetBlockByHeightResponse(const JSONValue&, Block& out, PhantasmaError* err=0);
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
static void PhantasmaJsonAPI::MakeGetBlockHeightRequest(JSONBuilder&, const Char* chainInput);
```

**Parameters (request):**

- `JSONBuilder&` — Request builder (writes JSON into an internal buffer)
  *type:* `JSONBuilder&`
- `chainInput` — Chain name or address
  *type:* `const Char*`


### Get Block Height Response


**Response parser**

```cpp
static bool PhantasmaJsonAPI::ParseGetBlockHeightResponse(const JSONValue&, Int32& out, PhantasmaError* err=0);
```

**Parameters (response):**

- `JSONValue&` — Parameter
  *type:* `const`
- `out` — Output object populated from the response
  *type:* `Int32&`
- `err=0` — Optional error output (code/message)
  *type:* `PhantasmaError*`


### Get Block Transaction Count By Hash Request

Returns the number of transactions of a block. The chain-aware overload matches the current RPC contract; the legacy overload defaults to `"main"`.

**Request builder**

```cpp
static void PhantasmaJsonAPI::MakeGetBlockTransactionCountByHashRequest(JSONBuilder&, const Char* blockHash);
static void PhantasmaJsonAPI::MakeGetBlockTransactionCountByHashRequest(JSONBuilder&, const Char* chainAddressOrName, const Char* blockHash);
```

**Parameters (request):**

- `JSONBuilder&` — Request builder (writes JSON into an internal buffer)
  *type:* `JSONBuilder&`
- `chainAddressOrName` — Chain name or address. Omit only when using the legacy `"main"` default.
  *type:* `const Char*`
- `blockHash` — Block hash (hex)
  *type:* `const Char*`


### Get Block Transaction Count By Hash Response


**Response parser**

```cpp
static bool PhantasmaJsonAPI::ParseGetBlockTransactionCountByHashResponse(const JSONValue&, Int32& out, PhantasmaError* err=0);
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
static void PhantasmaJsonAPI::MakeGetChainsRequest(JSONBuilder&);
```

**Parameters (request):**

- `JSONBuilder&` — Request builder (writes JSON into an internal buffer)
  *type:* `JSONBuilder&`


### Get Chains Response


**Response parser**

```cpp
static bool PhantasmaJsonAPI::ParseGetChainsResponse(const JSONValue&, PHANTASMA_VECTOR<Chain>& out, PhantasmaError* err=0);
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
static void PhantasmaJsonAPI::MakeGetContractRequest(JSONBuilder&, const Char* chainAddressOrName, const Char* contractName);
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
static bool PhantasmaJsonAPI::ParseGetContractResponse(const JSONValue&, Contract& out, PhantasmaError* err=0);
```

**Parameters (response):**

- `JSONValue&` — Parameter
  *type:* `const`
- `out` — Output object populated from the response
  *type:* `Contract&`
- `err=0` — Optional error output (code/message)
  *type:* `PhantasmaError*`


### Get Contracts Request

Returns the contract list for a chain.

**Request builder**

```cpp
static void PhantasmaJsonAPI::MakeGetContractsRequest(JSONBuilder&, const Char* chainAddressOrName, bool extended);
```

**Parameters (request):**

- `JSONBuilder&` — Request builder (writes JSON into an internal buffer)
  *type:* `JSONBuilder&`
- `chainAddressOrName` — Chain address or name
  *type:* `const Char*`
- `extended` — If true, include extended fields
  *type:* `bool`


### Get Contracts Response

**Response parser**

```cpp
static bool PhantasmaJsonAPI::ParseGetContractsResponse(const JSONValue&, PHANTASMA_VECTOR<Contract>& out, PhantasmaError* err=0);
```

**Parameters (response):**

- `JSONValue&` — Parameter
  *type:* `const`
- `out` — Output object populated from the response
  *type:* `PHANTASMA_VECTOR<Contract>&`
- `err=0` — Optional error output (code/message)
  *type:* `PhantasmaError*`


### Get Contract By Address Request

Returns the ABI interface of a contract by address.

**Request builder**

```cpp
static void PhantasmaJsonAPI::MakeGetContractByAddressRequest(JSONBuilder&, const Char* chainAddressOrName, const Char* contractAddress);
```

**Parameters (request):**

- `JSONBuilder&` — Request builder (writes JSON into an internal buffer)
  *type:* `JSONBuilder&`
- `chainAddressOrName` — Chain address or name
  *type:* `const Char*`
- `contractAddress` — Contract address
  *type:* `const Char*`


### Get Contract By Address Response

**Response parser**

```cpp
static bool PhantasmaJsonAPI::ParseGetContractByAddressResponse(const JSONValue&, Contract& out, PhantasmaError* err=0);
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
static void PhantasmaJsonAPI::MakeGetEventsRequest(JSONBuilder&, const Char* account);
```

**Parameters (request):**

- `JSONBuilder&` — Request builder (writes JSON into an internal buffer)
  *type:* `JSONBuilder&`
- `account` — Account address (P2K...) or name
  *type:* `const Char*`


### Get Events Response


**Response parser**

```cpp
static bool PhantasmaJsonAPI::ParseGetEventsResponse(const JSONValue&, PHANTASMA_VECTOR<Event>& out, PhantasmaError* err=0);
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
static void PhantasmaJsonAPI::MakeGetLeaderboardRequest(JSONBuilder&, const Char* name);
```

**Parameters (request):**

- `JSONBuilder&` — Request builder (writes JSON into an internal buffer)
  *type:* `JSONBuilder&`
- `name` — Account name (lookup)
  *type:* `const Char*`


### Get Leaderboard Response


**Response parser**

```cpp
static bool PhantasmaJsonAPI::ParseGetLeaderboardResponse(const JSONValue&, Leaderboard& out, PhantasmaError* err=0);
```

**Parameters (response):**

- `JSONValue&` — Parameter
  *type:* `const`
- `out` — Output object populated from the response
  *type:* `Leaderboard&`
- `err=0` — Optional error output (code/message)
  *type:* `PhantasmaError*`


### Get NFT Request

Returns data of a non-fungible token, in hexadecimal format.

**Request builder**

```cpp
static void PhantasmaJsonAPI::MakeGetNFTRequest(JSONBuilder&, const Char* symbol, const Char* IDtext, bool extended);
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


### Get NFT Response


**Response parser**

```cpp
static bool PhantasmaJsonAPI::ParseGetNFTResponse(const JSONValue&, TokenData& out, PhantasmaError* err=0);
```

**Parameters (response):**

- `JSONValue&` — Parameter
  *type:* `const`
- `out` — Output object populated from the response
  *type:* `TokenData&`
- `err=0` — Optional error output (code/message)
  *type:* `PhantasmaError*`


### Get NFTs Request

Returns data for multiple non-fungible token IDs.

**Request builder**

```cpp
static void PhantasmaJsonAPI::MakeGetNFTsRequest(JSONBuilder&, const Char* symbol, const Char* IDtext, bool extended);
```

**Parameters (request):**

- `JSONBuilder&` — Request builder (writes JSON into an internal buffer)
  *type:* `JSONBuilder&`
- `symbol` — Token symbol
  *type:* `const Char*`
- `IDtext` — Token ID list in string form
  *type:* `const Char*`
- `extended` — If true, include extended fields
  *type:* `bool`


### Get NFTs Response

**Response parser**

```cpp
static bool PhantasmaJsonAPI::ParseGetNFTsResponse(const JSONValue&, PHANTASMA_VECTOR<TokenData>& out, PhantasmaError* err=0);
```

**Parameters (response):**

- `JSONValue&` — Parameter
  *type:* `const`
- `out` — Output object populated from the response
  *type:* `PHANTASMA_VECTOR<TokenData>&`
- `err=0` — Optional error output (code/message)
  *type:* `PhantasmaError*`


### Get Nexus Request

Returns info about the nexus.

**Request builder**

```cpp
static void PhantasmaJsonAPI::MakeGetNexusRequest(JSONBuilder&, bool extended);
```

**Parameters (request):**

- `JSONBuilder&` — Request builder (writes JSON into an internal buffer)
  *type:* `JSONBuilder&`
- `extended` — If true, include extended fields
  *type:* `bool`


### Get Nexus Response


**Response parser**

```cpp
static bool PhantasmaJsonAPI::ParseGetNexusResponse(const JSONValue&, Nexus& out, PhantasmaError* err=0);
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
static void PhantasmaJsonAPI::MakeGetOrganizationRequest(JSONBuilder&, const Char* ID);
```

**Parameters (request):**

- `JSONBuilder&` — Request builder (writes JSON into an internal buffer)
  *type:* `JSONBuilder&`
- `ID` — String parameter
  *type:* `const Char*`


### Get Organization Response


**Response parser**

```cpp
static bool PhantasmaJsonAPI::ParseGetOrganizationResponse(const JSONValue&, Organization& out, PhantasmaError* err=0);
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
static void PhantasmaJsonAPI::MakeGetPeersRequest(JSONBuilder&);
```

**Parameters (request):**

- `JSONBuilder&` — Request builder (writes JSON into an internal buffer)
  *type:* `JSONBuilder&`


### Get Peers Response


**Response parser**

```cpp
static bool PhantasmaJsonAPI::ParseGetPeersResponse(const JSONValue&, PHANTASMA_VECTOR<Peer>& out, PhantasmaError* err=0);
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
static void PhantasmaJsonAPI::MakeGetPlatformsRequest(JSONBuilder&);
```

**Parameters (request):**

- `JSONBuilder&` — Request builder (writes JSON into an internal buffer)
  *type:* `JSONBuilder&`


### Get Platforms Response


**Response parser**

```cpp
static bool PhantasmaJsonAPI::ParseGetPlatformsResponse(const JSONValue&, PHANTASMA_VECTOR<Platform>& out, PhantasmaError* err=0);
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
static void PhantasmaJsonAPI::MakeGetRawBlockByHashRequest(JSONBuilder&, const Char* blockHash);
```

**Parameters (request):**

- `JSONBuilder&` — Request builder (writes JSON into an internal buffer)
  *type:* `JSONBuilder&`
- `blockHash` — Block hash (hex)
  *type:* `const Char*`


### Get Raw Block By Hash Response


**Response parser**

```cpp
static bool PhantasmaJsonAPI::ParseGetRawBlockByHashResponse(const JSONValue&, String& out, PhantasmaError* err=0);
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
static void PhantasmaJsonAPI::MakeGetRawBlockByHeightRequest(JSONBuilder&, const Char* chainInput, const Char* height);
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
static bool PhantasmaJsonAPI::ParseGetRawBlockByHeightResponse(const JSONValue&, String& out, PhantasmaError* err=0);
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
static void PhantasmaJsonAPI::MakeGetSwapsForAddressRequest(JSONBuilder&, const Char* account);
```

**Parameters (request):**

- `JSONBuilder&` — Request builder (writes JSON into an internal buffer)
  *type:* `JSONBuilder&`
- `account` — Account address (P2K...) or name
  *type:* `const Char*`


### Get Swaps For Address Response


**Response parser**

```cpp
static bool PhantasmaJsonAPI::ParseGetSwapsForAddressResponse(const JSONValue&, PHANTASMA_VECTOR<Swap>& out, PhantasmaError* err=0);
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
static void PhantasmaJsonAPI::MakeGetTokenBalanceRequest(JSONBuilder&, const Char* account, const Char* tokenSymbol, const Char* chainInput);
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
static bool PhantasmaJsonAPI::ParseGetTokenBalanceResponse(const JSONValue&, Balance& out, PhantasmaError* err=0);
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
static void PhantasmaJsonAPI::MakeGetTokenDataRequest(JSONBuilder&, const Char* symbol, const Char* IDtext);
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
static bool PhantasmaJsonAPI::ParseGetTokenDataResponse(const JSONValue&, TokenData& out, PhantasmaError* err=0);
```

**Parameters (response):**

- `JSONValue&` — Parameter
  *type:* `const`
- `out` — Output object populated from the response
  *type:* `TokenData&`
- `err=0` — Optional error output (code/message)
  *type:* `PhantasmaError*`


### Get Token Request

Returns info about a specific token deployed in Phantasma. The optional Carbon token id is emitted only when non-zero.

**Request builder**

```cpp
static void PhantasmaJsonAPI::MakeGetTokenRequest(JSONBuilder&, const Char* symbol, bool extended, UInt64 carbonTokenId = 0);
```

**Parameters (request):**

- `JSONBuilder&` — Request builder (writes JSON into an internal buffer)
  *type:* `JSONBuilder&`
- `symbol` — Token symbol (e.g., SOUL, KCAL)
  *type:* `const Char*`
- `extended` — If true, include extended fields
  *type:* `bool`
- `carbonTokenId` — Carbon token id. Use `0` when resolving by symbol only.
  *type:* `UInt64`


### Get Token Response


**Response parser**

```cpp
static bool PhantasmaJsonAPI::ParseGetTokenResponse(const JSONValue&, Token& out, PhantasmaError* err=0);
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
static void PhantasmaJsonAPI::MakeGetTokensRequest(JSONBuilder&, bool extended, const Char* ownerAddress = nullptr);
```

**Parameters (request):**

- `JSONBuilder&` — Request builder (writes JSON into an internal buffer)
  *type:* `JSONBuilder&`
- `extended` — If true, include extended fields
  *type:* `bool`
- `ownerAddress` — Optional owner address filter
  *type:* `const Char*`


### Get Tokens Response


**Response parser**

```cpp
static bool PhantasmaJsonAPI::ParseGetTokensResponse(const JSONValue&, PHANTASMA_VECTOR<Token>& out, PhantasmaError* err=0);
```

**Parameters (response):**

- `JSONValue&` — Parameter
  *type:* `const`
- `out` — Output object populated from the response
  *type:* `PHANTASMA_VECTOR<Token>&`
- `err=0` — Optional error output (code/message)
  *type:* `PhantasmaError*`


### Get Token Series Request

Returns token series for a token using cursor pagination.

**Request builder**

```cpp
static void PhantasmaJsonAPI::MakeGetTokenSeriesRequest(JSONBuilder&, const Char* symbol, UInt64 carbonTokenId, UInt32 pageSize, const Char* cursor);
```

**Parameters (request):**

- `JSONBuilder&` — Request builder (writes JSON into an internal buffer)
  *type:* `JSONBuilder&`
- `symbol` — Token symbol
  *type:* `const Char*`
- `carbonTokenId` — Carbon token id. Use `0` when resolving by symbol only.
  *type:* `UInt64`
- `pageSize` — Maximum number of items to return
  *type:* `UInt32`
- `cursor` — Cursor returned by the previous page, or an empty string for the first page
  *type:* `const Char*`


### Get Token Series Response

**Response parser**

```cpp
static bool PhantasmaJsonAPI::ParseGetTokenSeriesResponse(const JSONValue&, CursorPaginatedResult<TokenSeries>& out, PhantasmaError* err=0);
```

**Parameters (response):**

- `JSONValue&` — Parameter
  *type:* `const`
- `out` — Output object populated from the response
  *type:* `CursorPaginatedResult<TokenSeries>&`
- `err=0` — Optional error output (code/message)
  *type:* `PhantasmaError*`


### Get Token Series By Id Request

Returns one token series by Phantasma or Carbon identifiers.

**Request builder**

```cpp
static void PhantasmaJsonAPI::MakeGetTokenSeriesByIdRequest(JSONBuilder&, const Char* symbol, UInt64 carbonTokenId, const Char* seriesId, UInt32 carbonSeriesId);
```

**Parameters (request):**

- `JSONBuilder&` — Request builder (writes JSON into an internal buffer)
  *type:* `JSONBuilder&`
- `symbol` — Token symbol
  *type:* `const Char*`
- `carbonTokenId` — Carbon token id. Use `0` when resolving by symbol only.
  *type:* `UInt64`
- `seriesId` — Phantasma series id in string form
  *type:* `const Char*`
- `carbonSeriesId` — Carbon series id. Use `0` when resolving by Phantasma series id only.
  *type:* `UInt32`


### Get Token Series By Id Response

**Response parser**

```cpp
static bool PhantasmaJsonAPI::ParseGetTokenSeriesByIdResponse(const JSONValue&, TokenSeries& out, PhantasmaError* err=0);
```

**Parameters (response):**

- `JSONValue&` — Parameter
  *type:* `const`
- `out` — Output object populated from the response
  *type:* `TokenSeries&`
- `err=0` — Optional error output (code/message)
  *type:* `PhantasmaError*`


### Get Token NFTs Request

Returns NFTs for a token series using cursor pagination.

**Request builder**

```cpp
static void PhantasmaJsonAPI::MakeGetTokenNFTsRequest(JSONBuilder&, UInt64 carbonTokenId, UInt32 carbonSeriesId, UInt32 pageSize, const Char* cursor, bool extended);
```

**Parameters (request):**

- `JSONBuilder&` — Request builder (writes JSON into an internal buffer)
  *type:* `JSONBuilder&`
- `carbonTokenId` — Carbon token id
  *type:* `UInt64`
- `carbonSeriesId` — Carbon series id
  *type:* `UInt32`
- `pageSize` — Maximum number of items to return
  *type:* `UInt32`
- `cursor` — Cursor returned by the previous page, or an empty string for the first page
  *type:* `const Char*`
- `extended` — If true, include extended fields
  *type:* `bool`


### Get Token NFTs Response

**Response parser**

```cpp
static bool PhantasmaJsonAPI::ParseGetTokenNFTsResponse(const JSONValue&, CursorPaginatedResult<TokenData>& out, PhantasmaError* err=0);
```

**Parameters (response):**

- `JSONValue&` — Parameter
  *type:* `const`
- `out` — Output object populated from the response
  *type:* `CursorPaginatedResult<TokenData>&`
- `err=0` — Optional error output (code/message)
  *type:* `PhantasmaError*`


### Get Transaction By Block Hash And Index Request

Returns the transaction at a block index. The chain-aware overload matches the current RPC contract; the legacy overload defaults to `"main"`.

**Request builder**

```cpp
static void PhantasmaJsonAPI::MakeGetTransactionByBlockHashAndIndexRequest(JSONBuilder&, const Char* blockHash, Int32 index);
static void PhantasmaJsonAPI::MakeGetTransactionByBlockHashAndIndexRequest(JSONBuilder&, const Char* chainAddressOrName, const Char* blockHash, Int32 index);
```

**Parameters (request):**

- `JSONBuilder&` — Request builder (writes JSON into an internal buffer)
  *type:* `JSONBuilder&`
- `chainAddressOrName` — Chain name or address. Omit only when using the legacy `"main"` default.
  *type:* `const Char*`
- `blockHash` — Block hash (hex)
  *type:* `const Char*`
- `index` — Transaction index within the block
  *type:* `Int32`


### Get Transaction By Block Hash And Index Response


**Response parser**

```cpp
static bool PhantasmaJsonAPI::ParseGetTransactionByBlockHashAndIndexResponse(const JSONValue&, Transaction& out, PhantasmaError* err=0);
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
static void PhantasmaJsonAPI::MakeGetTransactionRequest(JSONBuilder&, const Char* hashText);
```

**Parameters (request):**

- `JSONBuilder&` — Request builder (writes JSON into an internal buffer)
  *type:* `JSONBuilder&`
- `hashText` — Transaction or archive hash (hex)
  *type:* `const Char*`


### Get Transaction Response


**Response parser**

```cpp
static bool PhantasmaJsonAPI::ParseGetTransactionResponse(const JSONValue&, Transaction& out, PhantasmaError* err=0);
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
static void PhantasmaJsonAPI::MakeGetValidatorsRequest(JSONBuilder&);
```

**Parameters (request):**

- `JSONBuilder&` — Request builder (writes JSON into an internal buffer)
  *type:* `JSONBuilder&`


### Get Validators Response


**Response parser**

```cpp
static bool PhantasmaJsonAPI::ParseGetValidatorsResponse(const JSONValue&, PHANTASMA_VECTOR<Validator>& out, PhantasmaError* err=0);
```

**Parameters (response):**

- `JSONValue&` — Parameter
  *type:* `const`
- `out` — Output object populated from the response
  *type:* `PHANTASMA_VECTOR<Validator>&`
- `err=0` — Optional error output (code/message)
  *type:* `PhantasmaError*`


### Get Version Request

Returns build metadata reported by the node.

**Request builder**

```cpp
static void PhantasmaJsonAPI::MakeGetVersionRequest(JSONBuilder&);
```

**Parameters (request):**

- `JSONBuilder&` — Request builder (writes JSON into an internal buffer)
  *type:* `JSONBuilder&`


### Get Version Response

**Response parser**

```cpp
static bool PhantasmaJsonAPI::ParseGetVersionResponse(const JSONValue&, BuildInfoResult& out, PhantasmaError* err=0);
```

**Parameters (response):**

- `JSONValue&` — Parameter
  *type:* `const`
- `out` — Output object populated from the response
  *type:* `BuildInfoResult&`
- `err=0` — Optional error output (code/message)
  *type:* `PhantasmaError*`


### Get Phantasma VM Config Request

Returns the current VM configuration applied by a chain.

**Request builder**

```cpp
static void PhantasmaJsonAPI::MakeGetPhantasmaVmConfigRequest(JSONBuilder&, const Char* chainAddressOrName);
```

**Parameters (request):**

- `JSONBuilder&` — Request builder (writes JSON into an internal buffer)
  *type:* `JSONBuilder&`
- `chainAddressOrName` — Chain address or name
  *type:* `const Char*`


### Get Phantasma VM Config Response

**Response parser**

```cpp
static bool PhantasmaJsonAPI::ParseGetPhantasmaVmConfigResponse(const JSONValue&, PhantasmaVmConfig& out, PhantasmaError* err=0);
```

**Parameters (response):**

- `JSONValue&` — Parameter
  *type:* `const`
- `out` — Output object populated from the response
  *type:* `PhantasmaVmConfig&`
- `err=0` — Optional error output (code/message)
  *type:* `PhantasmaError*`


### Invoke Raw Script Request

Allows to invoke script based on network state, without state changes.

**Request builder**

```cpp
static void PhantasmaJsonAPI::MakeInvokeRawScriptRequest(JSONBuilder&, const Char* chainInput, const Char* scriptData);
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
static bool PhantasmaJsonAPI::ParseInvokeRawScriptResponse(const JSONValue&, Script& out, PhantasmaError* err=0);
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
static void PhantasmaJsonAPI::MakeLookUpNameRequest(JSONBuilder&, const Char* name);
```

**Parameters (request):**

- `JSONBuilder&` — Request builder (writes JSON into an internal buffer)
  *type:* `JSONBuilder&`
- `name` — Account name (lookup)
  *type:* `const Char*`


### Look Up Name Response


**Response parser**

```cpp
static bool PhantasmaJsonAPI::ParseLookUpNameResponse(const JSONValue&, String& out, PhantasmaError* err=0);
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
static void PhantasmaJsonAPI::MakeReadArchiveRequest(JSONBuilder&, const Char* hashText, Int32 blockIndex);
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
static bool PhantasmaJsonAPI::ParseReadArchiveResponse(const JSONValue&, String& out, PhantasmaError* err=0);
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
static void PhantasmaJsonAPI::MakeRelayReceiveRequest(JSONBuilder&, const Char* account);
```

**Parameters (request):**

- `JSONBuilder&` — Request builder (writes JSON into an internal buffer)
  *type:* `JSONBuilder&`
- `account` — Account address (P2K...) or name
  *type:* `const Char*`


### Relay Receive Response


**Response parser**

```cpp
static bool PhantasmaJsonAPI::ParseRelayReceiveResponse(const JSONValue&, PHANTASMA_VECTOR<Receipt>& out, PhantasmaError* err=0);
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
static void PhantasmaJsonAPI::MakeRelaySendRequest(JSONBuilder&, const Char* receiptHex);
```

**Parameters (request):**

- `JSONBuilder&` — Request builder (writes JSON into an internal buffer)
  *type:* `JSONBuilder&`
- `receiptHex` — String parameter
  *type:* `const Char*`


### Relay Send Response


**Response parser**

```cpp
static bool PhantasmaJsonAPI::ParseRelaySendResponse(const JSONValue&, bool& out, PhantasmaError* err=0);
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
static void PhantasmaJsonAPI::MakeSendRawTransactionRequest(JSONBuilder&, const Char* txData);
```

**Parameters (request):**

- `JSONBuilder&` — Request builder (writes JSON into an internal buffer)
  *type:* `JSONBuilder&`
- `txData` — Raw transaction data (hex/Base16)
  *type:* `const Char*`


### Send Raw Transaction Response


**Response parser**

```cpp
static bool PhantasmaJsonAPI::ParseSendRawTransactionResponse(const JSONValue&, String& out, PhantasmaError* err=0);
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
static void PhantasmaJsonAPI::MakeSettleSwapRequest(JSONBuilder&, const Char* sourcePlatform, const Char* destPlatform, const Char* hashText);
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
static bool PhantasmaJsonAPI::ParseSettleSwapResponse(const JSONValue&, String& out, PhantasmaError* err=0);
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
static void PhantasmaJsonAPI::MakeWriteArchiveRequest(JSONBuilder&, const Char* hashText, Int32 blockIndex, const Char* blockContent);
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
static bool PhantasmaJsonAPI::ParseWriteArchiveResponse(const JSONValue&, bool& out, PhantasmaError* err=0);
```

**Parameters (response):**

- `JSONValue&` — Parameter
  *type:* `const`
- `out` — Output object populated from the response
  *type:* `bool&`
- `err=0` — Optional error output (code/message)
  *type:* `PhantasmaError*`
