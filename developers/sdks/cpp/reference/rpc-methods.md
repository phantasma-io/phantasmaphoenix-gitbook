# C++ SDK RPC Client

`PhantasmaAPI.h` is generated and exposes both low-level JSON helpers and a
high-level adapter-backed facade.

## Construction

| API | Purpose |
| --- | ------- |
| `PhantasmaAPI(httpClient)` | High-level facade. Requires `PHANTASMA_HTTPCLIENT` from an adapter. |
| `PhantasmaJsonAPI::Uri()` | Returns the RPC URI used by the JSON API layer. |
| `PhantasmaJsonAPI::Make...Request(builder, ...)` | Writes a JSON-RPC request. |
| `PhantasmaJsonAPI::Parse...Response(json, out, err)` | Parses a node response into a typed result. |

High-level methods return default-constructed values when a parse or RPC
failure occurs. Pass a `PhantasmaError*` and check it before using the returned
value. Low-level `Parse...Response` helpers use the same error channel.

Each `Make...Request` helper now assigns a generated JSON-RPC id. Use
`PhantasmaJsonAPI::UseRequestId(request)` before parsing a response built from
that request; `Parse...Response` rejects missing or mismatched response ids.
The bundled cURL and cpprest adapters cap RPC response bodies at
`PHANTASMA_DEFAULT_MAX_RPC_RESPONSE_BYTES`, 16 MiB, unless the adapter
is configured otherwise.

## Low-Level Lifecycle

`PhantasmaJsonAPI` builds requests and parses responses; the application owns
the transport.

1. Create a `JSONBuilder` and call the `Make...Request` helper.
2. POST the builder's text to the node at `PhantasmaJsonAPI::Uri()`, which is
   `/rpc` on the node host.
3. Parse the HTTP body into a `JSONValue` with the JSON adapter.
4. Call the matching `Parse...Response` helper, which fills the result struct
   and reports failures through `PhantasmaError`.

With the RapidJSON adapter the builder's text is `req.buf.GetString()`:

```cpp
JSONBuilder req;
phantasma::rpc::PhantasmaJsonAPI::MakeGetAccountInfoRequest(req, "P2K...");
const char* body = req.buf.GetString(); // POST this to <host>/rpc

phantasma::rpc::AccountInfo out{};
phantasma::rpc::PhantasmaError err{};
bool ok = phantasma::rpc::PhantasmaJsonAPI::ParseGetAccountInfoResponse(value, out, &err);
if (!ok) {
    // err.code and err.message say what failed
}
```

`value` is the `JSONValue` the application parsed from the response body.

## Errors

`PhantasmaError` carries `code` and `message`. The codes the SDK itself sets:

| Code | Constant | Meaning |
| --- | --- | --- |
| `-1` | `PhantasmaError::InvalidJSON` | The response body is not JSON. |
| `-2` | `PhantasmaError::HttpError` | The transport failed. The adapters call `OnHttpError(err, message)`. |
| `-3` | `PhantasmaError::InvalidRpcResponse` | The JSON is not a JSON-RPC response, or its id does not match the request. |
| `-4` | `PhantasmaError::RpcMessage` | The node answered an error object; `message` holds its text. |

A high-level method returns a default-constructed value on any failure, so
read `err.code` before the value.

## Common Calls

```cpp
phantasma::rpc::PhantasmaError err{};

// Numeric pagination of address transactions.
phantasma::rpc::AccountTransactions txs = api.GetAddressTransactions("P2K...", 0, 50, &err);

// Broadcast a signed script transaction.
phantasma::String hashText = api.SendRawTransaction(phantasma::Base16::Encode(tx.ToByteArray(true)).c_str(), &err);

// Run a script against the current state without committing anything.
phantasma::rpc::Script res = api.InvokeRawScript("main", phantasma::Base16::Encode(scriptBytes).c_str(), &err);
```

## Method Groups

| Group | High-level methods |
| ----- | ------------------ |
| Accounts | `GetAccountInfo`, `GetAccountInfos`, `LookUpName`, `GetAddressTransactions`, `GetAddressTransactionCount`. `GetAccount` and `GetAccounts` are deprecated |
| Blocks | `GetBlockHeight`, `GetBlockByHash`, `GetBlockByHeight`, `GetLatestBlock`, `GetBlockTransactionCountByHash` |
| Transactions | `GetTransaction`, `GetTransactionByBlockHashAndIndex`, `SendRawTransaction`, `SendCarbonTransaction`, `InvokeRawScript` |
| Chain metadata | `GetChains`, `GetChain`, `GetNexus`, `GetVersion`, `GetPhantasmaVmConfig` |
| Contracts | `GetContracts`, `GetContract`, `GetContractByAddress` |
| Organizations and leaderboards | `GetOrganization`, `GetOrganizations`, `GetOrganizationMembers`, `GetOrganizationMember`, `GetLeaderboard` |
| Tokens | `GetTokens`, `GetToken`, `GetTokenSeries`, `GetTokenSeriesById`, `GetTokenNFTs`, `GetTokenBalance`. `GetTokenData` is deprecated, and `GetNFT` covers it |
| Fees | `GetGasConfig`, `EstimateTransaction` |
| Account token inventory | `GetAccountFungibleTokens`, `GetAccountNFTs`, `GetAccountOwnedTokens`, `GetAccountOwnedTokenSeries` |
| NFT and marketplace | `GetNFT`, `GetNFTs`, `GetAuctionsCount`, `GetAuctions`, `GetAuction` |
| Archive | `GetArchive`, `WriteArchive`, `ReadArchive` |

`GetGasConfig` returns the on-chain gas configuration and the chain parameters
fee estimation needs. `EstimateTransaction` dry-runs a serialized envelope
against current chain state. A node with the estimate service switched off answers a standard RPC error.

{% content-ref url="/developers/sdks/cpp/fees-and-broadcasting.md" %}
[Fees And Broadcasting](/developers/sdks/cpp/fees-and-broadcasting.md)
{% endcontent-ref %}

## Chain Argument

`GetBlockTransactionCountByHash(chainAddressOrName, blockHash, err)` and
`GetTransactionByBlockHashAndIndex(chainAddressOrName, blockHash, index, err)`
take the chain first. There is no overload that defaults it.

## Cursor Parameters

Carbon inventory methods use `pageSize` and `cursor` where the node returns
`CursorPaginatedResult<T>`. Keep passing the returned cursor until it is empty.

## Broadcast Methods

`SendRawTransaction` expects signed VM script transaction hex.
`SendCarbonTransaction` expects signed Carbon message hex. Both return the hash
reported by the node and do not poll for execution state; call `GetTransaction`
and check `state` before parsing `result`.

`Utils/RpcUtils.h` adds `SignAndSendTransaction(api, keys, nexus, chain,
script, payload, outError, expiration)`, which builds, signs and broadcasts a
script transaction. An `expiration` left at its default `Timestamp()` becomes
`DefaultScriptExpiration()`, which is `carbon::DefaultExpiryMs` (45 seconds)
from now, the same lifetime a Carbon message gets. The same header has
`SendTransaction(api, tx, outHash)`, `CheckConfirmation` and
`WaitForConfirmation`.

## Stubbed Methods

The header marks these wrappers as stubbed node methods:

| Wrapper | Documented return behavior |
| ------- | -------------------------- |
| `GetChains` | empty array |
| `GetChain` | default chain object |
| `GetNexus` | default nexus object |
| `GetLeaderboard` | default leaderboard object |
| `GetArchive` | default archive object |
| `WriteArchive` | false without persistence |
| `ReadArchive` | empty string |

Do not use these wrappers as proof of live chain state without verifying the
connected node behavior.

## Facade Methods

Every method of `PhantasmaAPI`, from the header at the commit named on the
[Public API Inventory](public-api.md) page. `out_error` is omitted from the
parameter lists.

<!-- generated:cpp-facade-methods -->
| Method | Returns | Notes from the header |
| --- | --- | --- |
| `GetAccountInfo(const Char* account, PhantasmaError* out_error = nullptr)` | `AccountInfo` | Returns the account name and staking info of given address. Cost is independent of how much the address holds, which makes this the call to use in wallet refresh loops; balances and NFTs are fetched separately through the cursor-paginated account endpoints. |
| `GetAccountInfos(const String* addresses, int addressCount, PhantasmaError* out_error = nullptr)` | `PHANTASMA_VECTOR<AccountInfo>` |  |
| `GetAccount(const Char* account, PhantasmaError* out_error = nullptr)` | `Account` | Deprecated. Returns the account name and balance of given address. |
| `GetAccounts(const Char* accountText, bool extended, bool checkAddressReservedByte, PhantasmaError* out_error = nullptr)` | `PHANTASMA_VECTOR<Account>` | Deprecated. Returns data about several accounts. |
| `LookUpName(const Char* name, PhantasmaError* out_error = nullptr)` | `String` | Returns the address that owns a given name. |
| `GetBlockHeight(const Char* chainInput, PhantasmaError* out_error = nullptr)` | `Int32` | Returns the height of a chain. |
| `GetBlockTransactionCountByHash(const Char* chainAddressOrName, const Char* blockHash, PhantasmaError* out_error = nullptr)` | `Int32` | Returns the number of transactions of given block hash or error if given hash is invalid or is not found. |
| `GetBlockByHash(const Char* blockHash, PhantasmaError* out_error = nullptr)` | `Block` | Returns information about a block by hash. |
| `GetBlockByHeight(const Char* chainInput, const Char* height, PhantasmaError* out_error = nullptr)` | `Block` | Returns information about a block by height and chain. |
| `GetLatestBlock(const Char* chainInput, PhantasmaError* out_error = nullptr)` | `Block` | Returns information about the latest block in a chain. |
| `GetTransactionByBlockHashAndIndex(const Char* chainAddressOrName, const Char* blockHash, Int32 index, PhantasmaError* out_error = nullptr)` | `Transaction` | Returns the information about a transaction requested by a block hash and transaction index. |
| `GetAddressTransactions(const Char* account, UInt32 page, UInt32 pageSize, PhantasmaError* out_error = nullptr)` | `AccountTransactions` | Returns last X transactions of given address. (paginated call) |
| `GetAddressTransactionCount(const Char* account, const Char* chainInput, PhantasmaError* out_error = nullptr)` | `Int32` | Get number of transactions in a specific address and chain |
| `SendRawTransaction(const Char* txData, PhantasmaError* out_error = nullptr)` | `String` | Allows to broadcast a signed operation on the network, but it&apos;s required to build it manually. |
| `SendCarbonTransaction(const Char* txData, PhantasmaError* out_error = nullptr)` | `String` | Allows to broadcast a signed Carbon transaction. |
| `InvokeRawScript(const Char* chainInput, const Char* scriptData, PhantasmaError* out_error = nullptr)` | `Script` | Allows to invoke script based on network state, without state changes. |
| `GetTransaction(const Char* hashText, PhantasmaError* out_error = nullptr)` | `Transaction` | Returns information about a transaction by hash. |
| `GetChains(PhantasmaError* out_error = nullptr)` | `PHANTASMA_VECTOR<Chain>` | Returns an array of all chains deployed in Phantasma. Warning: this Phantasma RPC method is currently stubbed and returns an empty array. |
| `GetChain(const Char* name, bool extended, PhantasmaError* out_error = nullptr)` | `Chain` | Returns info about a specific chain. Warning: this Phantasma RPC method is currently stubbed and returns a default chain object. |
| `GetGasConfig(PhantasmaError* out_error = nullptr)` | `GasConfigResult` | Returns the current on-chain gas configuration, gas model version and fee-estimation chain parameters. Changes only via governance resolutions, so the result is cacheable. |
| `EstimateTransaction(const Char* txData, PhantasmaError* out_error = nullptr)` | `EstimateTransactionResult` | Dry-runs a serialized transaction envelope against current chain state and returns its exact fee bill with recommended maxGas/maxData ceilings (gas-model-v2 Tier-2 estimate). Signatures inside the envelope may be zero-filled dummies of the correct length - the simulation skips signature checks, and dummies preserve the exact envelope byte length the bill depends on. Until the estimate service is launched this returns a standard RPC error; use Carbon::EstimateNativeFee with GetGasConfig as the fallback. |
| `GetNexus(bool extended, PhantasmaError* out_error = nullptr)` | `Nexus` | Returns info about the nexus. Warning: this Phantasma RPC method is currently stubbed and returns a default nexus object. |
| `GetOrganization(const Char* name, PhantasmaError* out_error = nullptr)` | `Organization` | Returns info about an organization by registered name. |
| `GetOrganization(const Char* name, bool includeMemberCount, PhantasmaError* out_error = nullptr)` | `Organization` |  |
| `GetOrganizations(UInt32 pageSize, const Char* cursor, bool includeMemberCount, PhantasmaError* out_error = nullptr)` | `CursorPaginatedResult<Organization>` | Returns organizations with cursor pagination. |
| `GetOrganizationMembers(const Char* name, UInt32 pageSize, const Char* cursor, bool includeMemberTime, PhantasmaError* out_error = nullptr)` | `CursorPaginatedResult<OrganizationMember>` | Returns organization members by registered name. |
| `GetOrganizationMember(const Char* name, const Char* address, bool checkAddressReservedByte, const Char* addressType, PhantasmaError* out_error = nullptr)` | `OrganizationMember` | Returns one organization membership by registered name. |
| `GetOrganizationMember(const Char* name, const Char* address, bool checkAddressReservedByte, AddressType addressType, PhantasmaError* out_error = nullptr)` | `OrganizationMember` |  |
| `GetLeaderboard(const Char* name, PhantasmaError* out_error = nullptr)` | `Leaderboard` | Returns content of a Phantasma leaderboard. Warning: this Phantasma RPC method is currently stubbed and returns a default leaderboard object. |
| `GetTokens(bool extended, PhantasmaError* out_error = nullptr)` | `PHANTASMA_VECTOR<Token>` | Returns an array of tokens deployed in Phantasma. The extended flag is deprecated server-side and slated for removal. |
| `GetTokens(bool extended, const Char* ownerAddress, PhantasmaError* out_error = nullptr)` | `PHANTASMA_VECTOR<Token>` | Returns an array of tokens deployed in Phantasma filtered by owner address. The extended flag is deprecated server-side and slated for removal. |
| `GetToken(const Char* symbol, bool extended, PhantasmaError* out_error = nullptr)` | `Token` | Returns info about a specific token deployed in Phantasma. |
| `GetToken(const Char* symbol, bool extended, UInt64 carbonTokenId, PhantasmaError* out_error = nullptr)` | `Token` | Returns info about a specific token by symbol or carbon token id. |
| `GetTokenSeries(const Char* symbol, UInt64 carbonTokenId, UInt32 pageSize, const Char* cursor, PhantasmaError* out_error = nullptr)` | `CursorPaginatedResult<TokenSeries>` | Returns list of series for a specific token (cursor pagination). |
| `GetTokenSeriesById(const Char* symbol, UInt64 carbonTokenId, const Char* seriesId, UInt32 carbonSeriesId, PhantasmaError* out_error = nullptr)` | `TokenSeries` | Returns one token series by Phantasma or Carbon identifiers. |
| `GetTokenNFTs(UInt64 carbonTokenId, UInt32 carbonSeriesId, UInt32 pageSize, const Char* cursor, bool extended, PhantasmaError* out_error = nullptr)` | `CursorPaginatedResult<TokenData>` | Returns an array of NFTs for a token (cursor pagination). |
| `GetTokenData(const Char* symbol, const Char* IDtext, PhantasmaError* out_error = nullptr)` | `TokenData` | Deprecated. Returns data of a non-fungible token, in hexadecimal format. Deprecated: the node serves this as a strict subset of getNFT - same response, with property loading forced off - so GetNFT covers it entirely. |
| `GetNFT(const Char* symbol, const Char* IDtext, bool extended, PhantasmaError* out_error = nullptr)` | `TokenData` | Returns data of a non-fungible token, in hexadecimal format. |
| `GetNFTs(const Char* symbol, const Char* IDtext, bool extended, PhantasmaError* out_error = nullptr)` | `PHANTASMA_VECTOR<TokenData>` | Returns data of non-fungible tokens by ID list. |
| `GetTokenBalance(const Char* account, const Char* tokenSymbol, const Char* chainInput, PhantasmaError* out_error = nullptr)` | `Balance` | Returns the balance for a specific token and chain, given an address. |
| `GetTokenBalance(const Char* account, const Char* tokenSymbol, const Char* chainInput, bool checkAddressReservedByte, AddressType addressType, PhantasmaError* out_error = nullptr)` | `Balance` | The same query against an account named by its address TYPE. Pass "Carbon" with a 64-hex Carbon account key, which is how an NFT instance's own address is asked about; pass "Phantasma" for an ordinary address, which is what the other overload sends. |
| `GetAccountFungibleTokens(const Char* account, const Char* tokenSymbol, UInt64 carbonTokenId, UInt32 pageSize, const Char* cursor, bool checkAddressReservedByte, PhantasmaError* out_error = nullptr)` | `CursorPaginatedResult<Balance>` | Returns fungible token balances owned by an address (cursor pagination). |
| `GetAccountFungibleTokens(const Char* account, const Char* tokenSymbol, UInt64 carbonTokenId, UInt32 pageSize, const Char* cursor, bool checkAddressReservedByte, AddressType addressType, PhantasmaError* out_error = nullptr)` | `CursorPaginatedResult<Balance>` |  |
| `GetAccountNFTs(const Char* account, const Char* tokenSymbol, UInt64 carbonTokenId, UInt32 carbonSeriesId, UInt32 pageSize, const Char* cursor, bool extended, bool checkAddressReservedByte, PhantasmaError* out_error = nullptr)` | `CursorPaginatedResult<TokenData>` | Returns NFTs owned by an address (cursor pagination). |
| `GetAccountNFTs(const Char* account, const Char* tokenSymbol, UInt64 carbonTokenId, UInt32 carbonSeriesId, UInt32 pageSize, const Char* cursor, bool extended, bool checkAddressReservedByte, AddressType addressType, PhantasmaError* out_error = nullptr)` | `CursorPaginatedResult<TokenData>` |  |
| `GetAccountOwnedTokens(const Char* account, const Char* tokenSymbol, UInt64 carbonTokenId, UInt32 pageSize, const Char* cursor, bool checkAddressReservedByte, PhantasmaError* out_error = nullptr)` | `CursorPaginatedResult<Token>` | Returns NFT tokens for which the account owns at least one NFT instance (cursor pagination). |
| `GetAccountOwnedTokens(const Char* account, const Char* tokenSymbol, UInt64 carbonTokenId, UInt32 pageSize, const Char* cursor, bool checkAddressReservedByte, AddressType addressType, PhantasmaError* out_error = nullptr)` | `CursorPaginatedResult<Token>` |  |
| `GetAccountOwnedTokenSeries(const Char* account, const Char* tokenSymbol, UInt64 carbonTokenId, UInt32 pageSize, const Char* cursor, bool checkAddressReservedByte, PhantasmaError* out_error = nullptr)` | `CursorPaginatedResult<TokenSeries>` | Returns NFT series for which the account owns at least one NFT instance (cursor pagination). |
| `GetAccountOwnedTokenSeries(const Char* account, const Char* tokenSymbol, UInt64 carbonTokenId, UInt32 pageSize, const Char* cursor, bool checkAddressReservedByte, AddressType addressType, PhantasmaError* out_error = nullptr)` | `CursorPaginatedResult<TokenSeries>` |  |
| `GetAuctionsCount(const Char* chainAddressOrName, const Char* symbol, PhantasmaError* out_error = nullptr)` | `Int32` | Returns the number of active auctions. |
| `GetAuctions(const Char* chainAddressOrName, const Char* symbol, UInt32 page, UInt32 pageSize, PhantasmaError* out_error = nullptr)` | `PHANTASMA_VECTOR<Auction>` | Returns the auctions available in the market. (paginated call) |
| `GetAuction(const Char* chainAddressOrName, const Char* symbol, const Char* IDtext, PhantasmaError* out_error = nullptr)` | `Auction` | Returns the auction for a specific token. |
| `GetArchive(const Char* hashText, PhantasmaError* out_error = nullptr)` | `Archive` | Returns info about a specific archive. Warning: this Phantasma RPC method is currently stubbed and returns a default archive object. |
| `WriteArchive(const Char* hashText, Int32 blockIndex, const Char* blockContent, PhantasmaError* out_error = nullptr)` | `bool` | Writes the contents of an incomplete archive. Warning: this Phantasma RPC method is currently stubbed and returns false without persisting data. |
| `ReadArchive(const Char* hashText, Int32 blockIndex, PhantasmaError* out_error = nullptr)` | `String` | Reads given archive block. Warning: this Phantasma RPC method is currently stubbed and returns an empty string. |
| `GetContract(const Char* chainAddressOrName, const Char* contractName, PhantasmaError* out_error = nullptr)` | `Contract` | Returns the ABI interface of specific contract. |
| `GetContracts(const Char* chainAddressOrName, bool extended, PhantasmaError* out_error = nullptr)` | `PHANTASMA_VECTOR<Contract>` | Returns the ABI interface of specific contract (list). The extended flag is deprecated server-side and slated for removal. |
| `GetContractByAddress(const Char* chainAddressOrName, const Char* contractAddress, PhantasmaError* out_error = nullptr)` | `Contract` | Returns the ABI interface of specific contract by address. |
| `GetVersion(PhantasmaError* out_error = nullptr)` | `BuildInfoResult` | Returns build metadata for the node. |
| `GetPhantasmaVmConfig(const Char* chainAddressOrName, PhantasmaError* out_error = nullptr)` | `PhantasmaVmConfig` | Returns the current Phantasma VM config applied by the chain. |
<!-- /generated -->

## Low-Level Helpers

The `PhantasmaJsonAPI` request builders and response parsers.

<!-- generated:cpp-low-level-helpers -->
| Helper | Returns |
| --- | --- |
| `MakeGetAccountInfoRequest(JSONBuilder&, const Char* account)` | `void` |
| `ParseGetAccountInfoResponse(const JSONValue&, AccountInfo& out, PhantasmaError* err = 0)` | `bool` |
| `MakeGetAccountInfosRequest(JSONBuilder&, const String* addresses, int addressCount)` | `void` |
| `MakeGetAccountInfosRequest(JSONBuilder&, const String* addresses, int addressCount, bool checkAddressReservedByte, const Char* addressType)` | `void` |
| `MakeGetAccountInfosRequest(JSONBuilder&, const String* addresses, int addressCount, bool checkAddressReservedByte, AddressType addressType)` | `void` |
| `ParseGetAccountInfosResponse(const JSONValue&, PHANTASMA_VECTOR<AccountInfo>& out, PhantasmaError* err = 0)` | `bool` |
| `MakeGetAccountRequest(JSONBuilder&, const Char* account)` | `void` |
| `ParseGetAccountResponse(const JSONValue&, Account& out, PhantasmaError* err = 0)` | `bool` |
| `MakeGetAccountsRequest(JSONBuilder&, const Char* accountText, bool extended, bool checkAddressReservedByte)` | `void` |
| `ParseGetAccountsResponse(const JSONValue&, PHANTASMA_VECTOR<Account>& out, PhantasmaError* err = 0)` | `bool` |
| `MakeLookUpNameRequest(JSONBuilder&, const Char* name)` | `void` |
| `ParseLookUpNameResponse(const JSONValue&, String& out, PhantasmaError* err = 0)` | `bool` |
| `MakeGetBlockHeightRequest(JSONBuilder&, const Char* chainInput)` | `void` |
| `ParseGetBlockHeightResponse(const JSONValue&, Int32& out, PhantasmaError* err = 0)` | `bool` |
| `MakeGetBlockTransactionCountByHashRequest(JSONBuilder&, const Char* chainAddressOrName, const Char* blockHash)` | `void` |
| `ParseGetBlockTransactionCountByHashResponse(const JSONValue&, Int32& out, PhantasmaError* err = 0)` | `bool` |
| `MakeGetBlockByHashRequest(JSONBuilder&, const Char* blockHash)` | `void` |
| `ParseGetBlockByHashResponse(const JSONValue&, Block& out, PhantasmaError* err = 0)` | `bool` |
| `MakeGetBlockByHeightRequest(JSONBuilder&, const Char* chainInput, const Char* height)` | `void` |
| `ParseGetBlockByHeightResponse(const JSONValue&, Block& out, PhantasmaError* err = 0)` | `bool` |
| `MakeGetLatestBlockRequest(JSONBuilder&, const Char* chainInput)` | `void` |
| `ParseGetLatestBlockResponse(const JSONValue&, Block& out, PhantasmaError* err = 0)` | `bool` |
| `MakeGetTransactionByBlockHashAndIndexRequest(JSONBuilder&, const Char* chainAddressOrName, const Char* blockHash, Int32 index)` | `void` |
| `ParseGetTransactionByBlockHashAndIndexResponse(const JSONValue&, Transaction& out, PhantasmaError* err = 0)` | `bool` |
| `MakeGetAddressTransactionsRequest(JSONBuilder&, const Char* account, UInt32 page, UInt32 pageSize)` | `void` |
| `ParseGetAddressTransactionsResponse(const JSONValue&, AccountTransactions& out, PhantasmaError* err = 0)` | `bool` |
| `MakeGetAddressTransactionCountRequest(JSONBuilder&, const Char* account, const Char* chainInput)` | `void` |
| `ParseGetAddressTransactionCountResponse(const JSONValue&, Int32& out, PhantasmaError* err = 0)` | `bool` |
| `MakeSendRawTransactionRequest(JSONBuilder&, const Char* txData)` | `void` |
| `ParseSendRawTransactionResponse(const JSONValue&, String& out, PhantasmaError* err = 0)` | `bool` |
| `MakeSendCarbonTransactionRequest(JSONBuilder&, const Char* txData)` | `void` |
| `ParseSendCarbonTransactionResponse(const JSONValue&, String& out, PhantasmaError* err = 0)` | `bool` |
| `MakeInvokeRawScriptRequest(JSONBuilder&, const Char* chainInput, const Char* scriptData)` | `void` |
| `ParseInvokeRawScriptResponse(const JSONValue&, Script& out, PhantasmaError* err = 0)` | `bool` |
| `MakeGetTransactionRequest(JSONBuilder&, const Char* hashText)` | `void` |
| `ParseGetTransactionResponse(const JSONValue&, Transaction& out, PhantasmaError* err = 0)` | `bool` |
| `MakeGetChainsRequest(JSONBuilder&)` | `void` |
| `ParseGetChainsResponse(const JSONValue&, PHANTASMA_VECTOR<Chain>& out, PhantasmaError* err = 0)` | `bool` |
| `MakeGetChainRequest(JSONBuilder&, const Char* name, bool extended)` | `void` |
| `ParseGetChainResponse(const JSONValue&, Chain& out, PhantasmaError* err = 0)` | `bool` |
| `MakeGetGasConfigRequest(JSONBuilder&)` | `void` |
| `ParseGetGasConfigResponse(const JSONValue&, GasConfigResult& out, PhantasmaError* err = 0)` | `bool` |
| `MakeEstimateTransactionRequest(JSONBuilder&, const Char* txData)` | `void` |
| `ParseEstimateTransactionResponse(const JSONValue&, EstimateTransactionResult& out, PhantasmaError* err = 0)` | `bool` |
| `MakeGetNexusRequest(JSONBuilder&, bool extended)` | `void` |
| `ParseGetNexusResponse(const JSONValue&, Nexus& out, PhantasmaError* err = 0)` | `bool` |
| `MakeGetOrganizationRequest(JSONBuilder&, const Char* name, bool includeMemberCount)` | `void` |
| `ParseGetOrganizationResponse(const JSONValue&, Organization& out, PhantasmaError* err = 0)` | `bool` |
| `MakeGetOrganizationsRequest(JSONBuilder&, UInt32 pageSize, const Char* cursor, bool includeMemberCount)` | `void` |
| `ParseGetOrganizationsResponse(const JSONValue&, CursorPaginatedResult<Organization>& out, PhantasmaError* err = 0)` | `bool` |
| `MakeGetOrganizationMembersRequest(JSONBuilder&, const Char* name, UInt32 pageSize, const Char* cursor, bool includeMemberTime)` | `void` |
| `ParseGetOrganizationMembersResponse(const JSONValue&, CursorPaginatedResult<OrganizationMember>& out, PhantasmaError* err = 0)` | `bool` |
| `MakeGetOrganizationMemberRequest(JSONBuilder&, const Char* name, const Char* address, bool checkAddressReservedByte, const Char* addressType)` | `void` |
| `MakeGetOrganizationMemberRequest(JSONBuilder&, const Char* name, const Char* address, bool checkAddressReservedByte, AddressType addressType)` | `void` |
| `ParseGetOrganizationMemberResponse(const JSONValue&, OrganizationMember& out, PhantasmaError* err = 0)` | `bool` |
| `MakeGetLeaderboardRequest(JSONBuilder&, const Char* name)` | `void` |
| `ParseGetLeaderboardResponse(const JSONValue&, Leaderboard& out, PhantasmaError* err = 0)` | `bool` |
| `MakeGetTokensRequest(JSONBuilder&, bool extended, const Char* ownerAddress = nullptr)` | `void` |
| `ParseGetTokensResponse(const JSONValue&, PHANTASMA_VECTOR<Token>& out, PhantasmaError* err = 0)` | `bool` |
| `MakeGetTokenRequest(JSONBuilder&, const Char* symbol, bool extended, UInt64 carbonTokenId = 0)` | `void` |
| `ParseGetTokenResponse(const JSONValue&, Token& out, PhantasmaError* err = 0)` | `bool` |
| `MakeGetTokenSeriesRequest(JSONBuilder&, const Char* symbol, UInt64 carbonTokenId, UInt32 pageSize, const Char* cursor)` | `void` |
| `ParseGetTokenSeriesResponse(const JSONValue&, CursorPaginatedResult<TokenSeries>& out, PhantasmaError* err = 0)` | `bool` |
| `MakeGetTokenSeriesByIdRequest(JSONBuilder&, const Char* symbol, UInt64 carbonTokenId, const Char* seriesId, UInt32 carbonSeriesId)` | `void` |
| `ParseGetTokenSeriesByIdResponse(const JSONValue&, TokenSeries& out, PhantasmaError* err = 0)` | `bool` |
| `MakeGetTokenNFTsRequest(JSONBuilder&, UInt64 carbonTokenId, UInt32 carbonSeriesId, UInt32 pageSize, const Char* cursor, bool extended)` | `void` |
| `ParseGetTokenNFTsResponse(const JSONValue&, CursorPaginatedResult<TokenData>& out, PhantasmaError* err = 0)` | `bool` |
| `MakeGetTokenDataRequest(JSONBuilder&, const Char* symbol, const Char* IDtext)` | `void` |
| `ParseGetTokenDataResponse(const JSONValue&, TokenData& out, PhantasmaError* err = 0)` | `bool` |
| `MakeGetNFTRequest(JSONBuilder&, const Char* symbol, const Char* IDtext, bool extended)` | `void` |
| `ParseGetNFTResponse(const JSONValue&, TokenData& out, PhantasmaError* err = 0)` | `bool` |
| `MakeGetNFTsRequest(JSONBuilder&, const Char* symbol, const Char* IDtext, bool extended)` | `void` |
| `ParseGetNFTsResponse(const JSONValue&, PHANTASMA_VECTOR<TokenData>& out, PhantasmaError* err = 0)` | `bool` |
| `MakeGetTokenBalanceRequest(JSONBuilder&, const Char* account, const Char* tokenSymbol, const Char* chainInput)` | `void` |
| `MakeGetTokenBalanceRequest(JSONBuilder&, const Char* account, const Char* tokenSymbol, const Char* chainInput, bool checkAddressReservedByte, AddressType addressType)` | `void` |
| `ParseGetTokenBalanceResponse(const JSONValue&, Balance& out, PhantasmaError* err = 0)` | `bool` |
| `MakeGetAccountFungibleTokensRequest(JSONBuilder&, const Char* account, const Char* tokenSymbol, UInt64 carbonTokenId, UInt32 pageSize, const Char* cursor, bool checkAddressReservedByte)` | `void` |
| `MakeGetAccountFungibleTokensRequest(JSONBuilder&, const Char* account, const Char* tokenSymbol, UInt64 carbonTokenId, UInt32 pageSize, const Char* cursor, bool checkAddressReservedByte, AddressType addressType)` | `void` |
| `ParseGetAccountFungibleTokensResponse(const JSONValue&, CursorPaginatedResult<Balance>& out, PhantasmaError* err = 0)` | `bool` |
| `MakeGetAccountNFTsRequest(JSONBuilder&, const Char* account, const Char* tokenSymbol, UInt64 carbonTokenId, UInt32 carbonSeriesId, UInt32 pageSize, const Char* cursor, bool extended, bool checkAddressReservedByte)` | `void` |
| `MakeGetAccountNFTsRequest(JSONBuilder&, const Char* account, const Char* tokenSymbol, UInt64 carbonTokenId, UInt32 carbonSeriesId, UInt32 pageSize, const Char* cursor, bool extended, bool checkAddressReservedByte, AddressType addressType)` | `void` |
| `ParseGetAccountNFTsResponse(const JSONValue&, CursorPaginatedResult<TokenData>& out, PhantasmaError* err = 0)` | `bool` |
| `MakeGetAccountOwnedTokensRequest(JSONBuilder&, const Char* account, const Char* tokenSymbol, UInt64 carbonTokenId, UInt32 pageSize, const Char* cursor, bool checkAddressReservedByte)` | `void` |
| `MakeGetAccountOwnedTokensRequest(JSONBuilder&, const Char* account, const Char* tokenSymbol, UInt64 carbonTokenId, UInt32 pageSize, const Char* cursor, bool checkAddressReservedByte, AddressType addressType)` | `void` |
| `ParseGetAccountOwnedTokensResponse(const JSONValue&, CursorPaginatedResult<Token>& out, PhantasmaError* err = 0)` | `bool` |
| `MakeGetAccountOwnedTokenSeriesRequest(JSONBuilder&, const Char* account, const Char* tokenSymbol, UInt64 carbonTokenId, UInt32 pageSize, const Char* cursor, bool checkAddressReservedByte)` | `void` |
| `MakeGetAccountOwnedTokenSeriesRequest(JSONBuilder&, const Char* account, const Char* tokenSymbol, UInt64 carbonTokenId, UInt32 pageSize, const Char* cursor, bool checkAddressReservedByte, AddressType addressType)` | `void` |
| `ParseGetAccountOwnedTokenSeriesResponse(const JSONValue&, CursorPaginatedResult<TokenSeries>& out, PhantasmaError* err = 0)` | `bool` |
| `MakeGetAuctionsCountRequest(JSONBuilder&, const Char* chainAddressOrName, const Char* symbol)` | `void` |
| `ParseGetAuctionsCountResponse(const JSONValue&, Int32& out, PhantasmaError* err = 0)` | `bool` |
| `MakeGetAuctionsRequest(JSONBuilder&, const Char* chainAddressOrName, const Char* symbol, UInt32 page, UInt32 pageSize)` | `void` |
| `ParseGetAuctionsResponse(const JSONValue&, PHANTASMA_VECTOR<Auction>& out, PhantasmaError* err = 0)` | `bool` |
| `MakeGetAuctionRequest(JSONBuilder&, const Char* chainAddressOrName, const Char* symbol, const Char* IDtext)` | `void` |
| `ParseGetAuctionResponse(const JSONValue&, Auction& out, PhantasmaError* err = 0)` | `bool` |
| `MakeGetArchiveRequest(JSONBuilder&, const Char* hashText)` | `void` |
| `ParseGetArchiveResponse(const JSONValue&, Archive& out, PhantasmaError* err = 0)` | `bool` |
| `MakeWriteArchiveRequest(JSONBuilder&, const Char* hashText, Int32 blockIndex, const Char* blockContent)` | `void` |
| `ParseWriteArchiveResponse(const JSONValue&, bool& out, PhantasmaError* err = 0)` | `bool` |
| `MakeReadArchiveRequest(JSONBuilder&, const Char* hashText, Int32 blockIndex)` | `void` |
| `ParseReadArchiveResponse(const JSONValue&, String& out, PhantasmaError* err = 0)` | `bool` |
| `MakeGetContractRequest(JSONBuilder&, const Char* chainAddressOrName, const Char* contractName)` | `void` |
| `ParseGetContractResponse(const JSONValue&, Contract& out, PhantasmaError* err = 0)` | `bool` |
| `MakeGetContractsRequest(JSONBuilder&, const Char* chainAddressOrName, bool extended)` | `void` |
| `ParseGetContractsResponse(const JSONValue&, PHANTASMA_VECTOR<Contract>& out, PhantasmaError* err = 0)` | `bool` |
| `MakeGetContractByAddressRequest(JSONBuilder&, const Char* chainAddressOrName, const Char* contractAddress)` | `void` |
| `ParseGetContractByAddressResponse(const JSONValue&, Contract& out, PhantasmaError* err = 0)` | `bool` |
| `MakeGetVersionRequest(JSONBuilder&)` | `void` |
| `ParseGetVersionResponse(const JSONValue&, BuildInfoResult& out, PhantasmaError* err = 0)` | `bool` |
| `MakeGetPhantasmaVmConfigRequest(JSONBuilder&, const Char* chainAddressOrName)` | `void` |
| `ParseGetPhantasmaVmConfigResponse(const JSONValue&, PhantasmaVmConfig& out, PhantasmaError* err = 0)` | `bool` |
<!-- /generated -->
