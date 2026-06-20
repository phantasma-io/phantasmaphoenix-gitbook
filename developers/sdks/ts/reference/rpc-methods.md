# TypeScript SDK RPC Client

`PhantasmaAPI` is the high-level JSON-RPC client. The public methods return
`Promise<T>` and throw on transport or JSON-RPC failures through the underlying
call path. Code that needs explicit result objects can call `JSONRPCResult<T>`.

## Construction And Endpoint Selection

| API | Purpose |
| --- | ------- |
| `new PhantasmaAPI(defHost, peersUrlJson, nexus, options?)` | Creates a client with default host, optional peers URL, nexus name, and `options` (RPC response size limit and API key). |
| `pingAsync(host)` | Measures endpoint latency. |
| `setRpcHost(rpcHost)` | Sets the active RPC host directly. |
| `setRpcByName(rpcName)` | Selects an RPC host by configured name. |
| `setNexus(nexus)` | Sets the nexus name used by the client. |
| `setMaxRpcResponseBytes(maxBytes)` | Replaces the maximum accepted JSON-RPC response body size. |
| `setApiKey(apiKey)` | Sets the API key sent in the `X-Api-Key` header on every request. |
| `updateRpc()` | Refreshes the active RPC host selection. |
| `convertDecimals(amount, decimals)` | Decimal conversion helper retained on the client. |

`options.maxRpcResponseBytes` and `setMaxRpcResponseBytes(...)` default to
`DEFAULT_MAX_RPC_RESPONSE_BYTES`, currently 16 MiB. Values must be positive.
`options.apiKey` and `setApiKey(...)` send the key as the `X-Api-Key` header.

## Raw JSON-RPC

| API | Purpose |
| --- | ------- |
| `JSONRPC(method, params)` | Sends a positional JSON-RPC call and returns the raw result value. |
| `JSONRPCResult<T>(method, params)` | Sends a call and returns `RpcResult<T>` with success or error shape. |
| `isRpcErrorResult(result)` | Type guard for JSON-RPC error results. |
| `getRpcErrorMessage(result)` | Extracts an error message. |
| `unwrapRpcResult(result)` | Returns the success value or throws for an error result. |

Use typed methods when they exist. Use raw calls for endpoint diagnostics or
node methods that do not yet have wrappers.

`JSONRPC(...)` unwraps successful JSON-RPC responses. It returns an
`{ error: ... }` object when the endpoint returns a JSON-RPC error object, and
throws when the endpoint omits `result`, returns invalid JSON, exceeds the
configured response-size limit, or echoes a mismatched JSON-RPC id.
`JSONRPCResult(...)` keeps the response as a success/error union so callers can
inspect node errors without exceptions; it uses the same request-id and
response-size validation.

## Accounts, Names, And Balances

| API | Purpose |
| --- | ------- |
| `getAccount(account, extended?)` | Reads one account. |
| `getAccounts(accounts, extended?)` | Reads multiple accounts from a string array. |
| `lookUpName(name)` | Resolves a registered name to address text. |
| `getAddressTransactions(account, page, pageSize)` | Reads address transaction history with page pagination. |
| `getAddressTransactionCount(account, chainInput)` | Reads address transaction count. |
| `getTokenBalance(account, tokenSymbol, chainInput, checkAddressResevedByte?)` | Reads one token balance. |

## Blocks And Transactions

| API | Purpose |
| --- | ------- |
| `getBlockHeight(chainInput)` | Reads the current chain height. |
| `getBlockTransactionCountByHash(chainAddressOrName, blockHash)` | Reads transaction count for a block hash on a chain. |
| `getBlockByHash(blockHash)` | Reads a block by hash. |
| `getBlockByHeight(chainInput, height)` | Reads a block by chain and height. |
| `getLatestBlock(chainInput)` | Reads the latest block object. |
| `getTransactionByBlockHashAndIndex(chainAddressOrName, blockHash, index)` | Reads a transaction at a block position. |
| `getTransaction(hashText)` | Reads a transaction by hash. |
| `sendRawTransaction(txData)` | Broadcasts signed VM transaction hex. |
| `sendCarbonTransaction(txData)` | Broadcasts signed Carbon transaction hex. |
| `invokeRawScript(chainInput, scriptData)` | Executes a read-only VM script. |

Broadcast methods return the transaction hash reported by the node. They do not
wait for execution; call `getTransaction(hash)` and check `state` before parsing
operation results.

## Chain, Contract, Organization, And Leaderboard Metadata

| API | Purpose |
| --- | ------- |
| `getChains(extended?)` | Reads all chains. |
| `getChain(name, extended?)` | Reads one chain by name. |
| `getNexus(extended?)` | Reads nexus metadata. |
| `getContracts(chainAddressOrName?, extended?)` | Reads contracts on a chain. |
| `getContract(chainAddressOrName, contractName)` | Reads a contract by name. |
| `getContractByAddress(chainAddressOrName, contractAddress)` | Reads a contract by address. |
| `getOrganization(name, includeMemberCount?)` | Reads one organization by name. |
| `getOrganizations(pageSize?, cursor?, includeMemberCount?)` | Lists organizations with cursor pagination. |
| `getOrganizationMembers(name, pageSize?, cursor?, includeMemberTime?)` | Lists organization members with cursor pagination. |
| `getOrganizationMember(name, address, checkAddressReservedByte?, addressType?)` | Checks one address's membership in an organization. |
| `getLeaderboard(name)` | Reads leaderboard rows. |
| `getVersion()` | Reads node build metadata. |
| `getPhantasmaVmConfig(chainAddressOrName)` | Reads VM gas/config values. |

## Tokens, Series, And NFTs

| API | Purpose |
| --- | ------- |
| `getTokens(ownerAddress, extended?)` | Reads token definitions, optionally filtered by owner. |
| `getToken(symbol, extended?, carbonTokenId?)` | Reads one token by symbol and optional Carbon token id. |
| `getTokenData(symbol, IDtext)` | Reads token data by symbol and Phantasma NFT id. |
| `getTokenSeries(symbol, carbonTokenId, pageSize?, cursor?)` | Reads cursor-paginated token series. |
| `getTokenSeriesById(symbol, carbonTokenId, seriesId, carbonSeriesId)` | Reads one series by Phantasma or Carbon id. |
| `getTokenNFTs(carbonTokenId, carbonSeriesId?, pageSize?, cursor?, extended?)` | Reads NFTs for a Carbon token with cursor pagination. |
| `getAccountFungibleTokens(...)` | Reads account fungible balances with cursor pagination. |
| `getAccountNFTs(...)` | Reads account-owned NFTs with cursor pagination. |
| `getAccountOwnedTokens(...)` | Reads token definitions owned by an account. |
| `getAccountOwnedTokenSeries(...)` | Reads token series owned by an account. |
| `getNFT(symbol, nftId, extended?)` | Reads one NFT. |
| `getNFTs(symbol, nftIDs, extended?)` | Reads multiple NFTs. |

Carbon token ids are `bigint`; Carbon series ids are `number`. Use `0n` or `0`
when a node method should run without that Carbon id filter.

## Auctions And Archives

| API | Purpose |
| --- | ------- |
| `getAuctionsCount(chainAddressOrName, symbol)` | Reads auction count. |
| `getAuctions(chainAddressOrName, symbol, page, pageSize)` | Reads auction page data. |
| `getAuction(chainAddressOrName, symbol, IDtext)` | Reads one auction. |
| `getArchive(hashText)` | Reads archive metadata. |
| `writeArchive(hashText, blockIndex, blockContent)` | Writes archive block content. |

`writeArchive(...)` accepts already encoded block content as a string. The
TypeScript client does not expose a `readArchive` wrapper.
