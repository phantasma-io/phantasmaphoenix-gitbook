# Python SDK RPC Client

`PhantasmaRPC` is the typed JSON-RPC facade in `phantasma_py.rpc`. Each wrapper
sends positional JSON-RPC parameters to the configured endpoint and decodes the
response into the result dataclasses documented in [RPC Result Models](rpc-models.md).

All typed RPC methods can raise `RPCError` when the endpoint returns an HTTP
error, invalid JSON, a JSON-RPC error object, a mismatched response id, a missing
`result`, or a response shape that cannot be decoded into the expected result
type. Methods that submit transactions return the transaction hash reported by
the node; they do not wait for final execution state. Poll `get_transaction(...)`
after broadcasting when the caller needs the final `state`, `result`, events, or
fees.

Common parameters:

| Parameter | Meaning |
| --------- | ------- |
| `chain` | Chain name passed to chain-scoped RPCs. Wrappers that define a chain default use `"main"`. |
| `extended` | Requests nested data from RPC methods that support a compact and expanded response shape. Use `False` for list views and `True` when the caller needs balances, metadata, series, ABI, or other nested fields. |
| `page`, `page_size` | Numeric pagination for older RPC methods. The response is a `PaginatedResult`. |
| `cursor` | Opaque cursor returned by cursor-based token and NFT inventory methods. Reuse the same filters and pass the returned cursor to read the next page. |
| `check_address_reserved_byte`, `address_type` | Address validation controls forwarded to RPC methods that expose them. Use the default form unless the caller deliberately needs the node's address-type variants. |

## Construction And Raw Calls

| API | Purpose and parameters | Returns and failures | Use it when |
| --- | ---------------------- | -------------------- | ----------- |
| `PhantasmaRPC(endpoint, session=None, timeout=30.0)` | Creates a typed RPC client for `endpoint`. `session` can be a requests-compatible object for tests or custom transport; `timeout` is passed to `session.post`. | Returns a client. Construction itself does not call the node. Later calls raise `RPCError` for transport or JSON-RPC failures. | Application code has an explicit RPC URL, including local nodes and private infrastructure. |
| `PhantasmaRPC.mainnet()` | Creates a client for `https://pharpc1.phantasma.info/rpc`. | Returns `PhantasmaRPC`. | A script or tool intentionally targets the default public mainnet endpoint. |
| `PhantasmaRPC.testnet()` | Creates a client for `https://testnet.phantasma.info/rpc`. | Returns `PhantasmaRPC`. | A script or tool intentionally targets the default public testnet endpoint. |
| `PhantasmaRPC.call(method, *params)` | Sends a raw positional JSON-RPC call through the typed client's underlying `JsonRpcClient`. | Returns the raw `result` value. Raises `RPCError` for transport, JSON, JSON-RPC, id, or missing-result failures. | A node method is needed before the SDK has a typed wrapper. Prefer typed wrappers when they exist. |
| `JsonRpcClient(endpoint, session=None, timeout=30.0)` | Low-level JSON-RPC 2.0 client used by `PhantasmaRPC`. It tracks request ids and validates response objects. | Returns a raw client. Later calls return raw `result` values or raise `RPCError`. | You are implementing a new wrapper or testing transport behavior directly. |
| `JsonRpcClient.call(method, *params)` | Sends `{"jsonrpc": "2.0", "id": <string>, "method": method, "params": list(params)}`. | Returns raw `result`. Raises `RPCError` if the response is not an object, has a mismatched id, contains `error`, or omits `result`. | Wrapper code needs raw JSON-RPC without typed dataclass decoding. |

Example:

```python
from phantasma_py.rpc import PhantasmaRPC

rpc = PhantasmaRPC("http://localhost:5172/rpc")
height = rpc.get_block_height("main")
```

## Build And VM Configuration

| API | Purpose and parameters | Returns and failures | Use it when |
| --- | ---------------------- | -------------------- | ----------- |
| `get_version()` | Calls `getVersion` with no parameters. | Returns `BuildInfoResult` with `version`, `commit`, and `build_time_utc`. Raises `RPCError` on RPC or decode failure. | Health checks, support logs, endpoint diagnostics, and version display. |
| `get_phantasma_vm_config(chain="main")` | Calls `getPhantasmaVmConfig` for a chain. | Returns `PhantasmaVMConfigResult` with VM gas configuration fields. Raises `RPCError` if the endpoint cannot return the config object. | Tooling needs current VM gas cost settings before showing or validating contract execution costs. |

## Accounts, Names, And Balances

| API | Purpose and parameters | Returns and failures | Use it when |
| --- | ---------------------- | -------------------- | ----------- |
| `get_platforms()` | Calls `getPlatforms` to read configured external platforms and interop mappings. | Returns `list[PlatformResult]`. Raises `RPCError` if the endpoint does not return an array. | Explorer or bridge tooling needs platform metadata. |
| `get_account(address, *, extended=False, check_address_reserved_byte=None, address_type=None)` | Reads one account. `extended` controls nested account data. The optional address controls are forwarded only when provided. | Returns `AccountResult`. Raises `RPCError` when the node rejects the address or returns a non-object result. | A wallet, dashboard, or backend needs profile, staking, storage, and balances for one address. |
| `get_accounts(addresses, *, extended=False, check_address_reserved_byte=None, address_type=None)` | Reads multiple accounts. `addresses` can be a comma-separated string or a sequence that the SDK joins with commas. | Returns `list[AccountResult]`. Raises `RPCError` for RPC failure or non-array results. | Batch account reads are cheaper for the caller than issuing one request per address. |
| `get_accounts_text(addresses, *, extended=False)` | Compatibility form of `get_accounts(...)` for a prebuilt comma-separated address string. | Returns `list[AccountResult]`. Same failure behavior as `get_accounts(...)`. | The caller already has the comma-separated wire-format address list. |
| `get_account_with_address_type(address, extended, check_address_reserved_byte, address_type)` | Explicit variant of `get_account(...)` that always passes the address reserved-byte and address-type controls. | Returns `AccountResult`. Raises `RPCError` for node or decode failures. | Infrastructure code must exercise the node's address-type parameters directly. |
| `get_accounts_with_address_type(addresses, extended, check_address_reserved_byte, address_type)` | Explicit variant of `get_accounts(...)` with address reserved-byte and type controls. | Returns `list[AccountResult]`. Raises `RPCError` for node or decode failures. | Batch account reads need the node's address-type parameters. |
| `lookup_name(name)` | Calls `lookUpName` and converts the result to `str`. | Returns the resolved address string. Raises `RPCError` if the name lookup fails at the node. | User input is a Phantasma name and the application needs the address. |
| `look_up_name(name)` | Alias that delegates to `lookup_name(...)`. | Returns the same string result and has the same failures. | Code uses the older snake-case spelling and should not change call sites. |
| `get_address_transactions(address, page, page_size)` | Reads one page of transaction hashes for an address with numeric pagination. | Returns `PaginatedResult[AddressTransactionsResult]`. Raises `RPCError` if the result is not a paginated object. | Transaction history UI needs address-level transaction ids. |
| `get_address_transaction_count(address, chain="main")` | Reads the total number of address transactions on a chain. | Returns `int`; the SDK coerces integer-compatible node values. Raises `RPCError` if coercion fails. | UI needs total counts before or alongside paginated transaction history. |
| `get_token_balance(address, symbol, chain="main", *, check_address_reserved_byte=None, address_type=None)` | Reads one token balance for an address without loading the full account. Optional address controls are forwarded when provided. | Returns `BalanceResult`. Raises `RPCError` for node or decode failures. | A page needs exactly one balance row and does not need account profile, storage, stake, or all balances. |
| `get_token_balance_checked(address, symbol, chain, check_address_reserved_byte)` | Compatibility helper that passes `check_address_reserved_byte` to `get_token_balance(...)`. | Returns `BalanceResult`. Same failures as `get_token_balance(...)`. | Code needs the reserved-byte control but not an address type. |
| `get_token_balance_with_address_type(address, symbol, chain, check_address_reserved_byte, address_type)` | Explicit helper that passes both address validation controls to `get_token_balance(...)`. | Returns `BalanceResult`. Same failures as `get_token_balance(...)`. | Node-specific address-type behavior matters for this balance read. |

Example:

```python
account = rpc.get_account("P...", extended=True)
soul = account.get_token_balance("SOUL", decimals=8)
print(soul.decimal_amount())
```

## Blocks And Transactions

| API | Purpose and parameters | Returns and failures | Use it when |
| --- | ---------------------- | -------------------- | ----------- |
| `get_block_height(chain="main")` | Calls `getBlockHeight` for a chain. | Returns `int`; the SDK coerces string or numeric integer-compatible node values. Raises `RPCError` if coercion fails. | A sync loop or status panel needs the current chain height. |
| `get_block_by_height(chain, height)` | Reads a block by chain and height. `height` may be `int` or `str` because the node accepts positional JSON-RPC values. | Returns `BlockResult`. Raises `RPCError` if the block is unavailable or the response is not a block object. | Ledger navigation starts from a known chain height. |
| `get_block_by_hash(block_hash)` | Reads a block by block hash. | Returns `BlockResult`. Raises `RPCError` for node or decode failures. | The caller already has a block hash from another result. |
| `get_latest_block(chain="main")` | Reads the latest block object for a chain. | Returns `BlockResult`. Raises `RPCError` for node or decode failures. | A status page needs both height and latest block metadata. |
| `get_block_transaction_count_by_hash(block_hash, chain="main")` | Calls the chain-aware `getBlockTransactionCountByHash` wire method with `chain` and `block_hash`. | Returns `int`; raises `RPCError` if the node value cannot be coerced to an integer. | A block view needs transaction count without loading or trusting the full block transaction list. |
| `get_block_transaction_count_by_hash_on_chain(chain, block_hash)` | Chain-first alias for `get_block_transaction_count_by_hash(...)`. | Returns `int`. Same failures as `get_block_transaction_count_by_hash(...)`. | Code style prefers the chain-first argument order used by the wire method. |
| `get_transaction(tx_hash)` | Reads a transaction by hash. | Returns `TransactionResult` with state, result hex, events, signatures, fee, and block placement. Raises `RPCError` if the transaction is not available or the result cannot be decoded. | Poll after broadcasting or display a known transaction. |
| `get_transaction_by_block_hash_and_index(block_hash, index, *, chain="main")` | Reads the transaction at `index` inside a block identified by hash and chain. | Returns `TransactionResult`. Raises `RPCError` for node errors, invalid index, or decode failure. | A block explorer is iterating transactions by block position. |
| `get_transaction_by_block_hash_and_index_on_chain(chain, block_hash, index)` | Chain-first alias for `get_transaction_by_block_hash_and_index(...)`. | Returns `TransactionResult`. Same failures as the alias target. | Code style follows the wire method's chain-first argument order. |

## Chain, Contract, Organization, And Leaderboard Metadata

| API | Purpose and parameters | Returns and failures | Use it when |
| --- | ---------------------- | -------------------- | ----------- |
| `get_chains(*, extended=True)` | Reads the chain list from the nexus. `extended` controls nested contract and dapp detail. | Returns `list[ChainResult]`. Raises `RPCError` if the node does not return an array. | Explorer or infrastructure code needs all chain metadata. |
| `get_chain(name="main", *, extended=True)` | Reads one chain by name. | Returns `ChainResult`. Raises `RPCError` for node or decode failures. | A page needs metadata for a specific chain. |
| `get_nexus(*, extended=True)` | Reads nexus metadata, including platforms, tokens, chains, governance, and organizations when the node returns them. | Returns `NexusResult`. Raises `RPCError` for node or decode failures. | Tooling needs a topology snapshot for the configured nexus. |
| `get_contract(contract_name, chain="main")` | Reads a contract by name on a chain. | Returns `ContractResult`, including script, ABI methods, and ABI events when available. Raises `RPCError` for node or decode failures. | Client tooling needs ABI information before constructing a VM call. |
| `get_contract_by_name(chain, contract_name)` | Chain-first alias that delegates to `get_contract(...)`. | Returns `ContractResult`. Same failures as `get_contract(...)`. | Existing code uses the chain-first spelling. |
| `get_contract_by_address(chain, contract_address)` | Reads a contract by address instead of name. | Returns `ContractResult`. Raises `RPCError` for node or decode failures. | The caller has a contract address from chain metadata or an event. |
| `get_contracts(chain="main", *, extended=True)` | Reads contracts deployed on a chain. | Returns `list[ContractResult]`. Raises `RPCError` if the result is not an array. | Explorer or developer tooling needs all chain contracts. |
| `get_organization(organization_id, *, extended=True)` | Reads organization metadata by id. | Returns `OrganizationResult`. Raises `RPCError` for node or decode failures. | Governance or validator tooling works with an organization id. |
| `get_organization_by_name(name, *, extended=True)` | Reads organization metadata by name. | Returns `OrganizationResult`. Raises `RPCError` for node or decode failures. | UI or CLI receives a human-readable organization name. |
| `get_organizations(*, extended=False)` | Reads the organization list. | Returns `list[OrganizationResult]`. Raises `RPCError` if the result is not an array. | A page needs a compact organization list; pass `extended=True` only when nested data is needed. |
| `get_leaderboard(name)` | Reads a leaderboard by name. | Returns `LeaderboardResult`. Raises `RPCError` for node or decode failures. | A dapp or explorer displays leaderboard rows from the chain. |

## Tokens, Series, And NFT Reads

| API | Purpose and parameters | Returns and failures | Use it when |
| --- | ---------------------- | -------------------- | ----------- |
| `get_token(symbol, *, extended=True, carbon_token_id=0)` | Reads one token definition by symbol and optional Carbon token id. | Returns `TokenResult`. Raises `RPCError` for node or decode failures. | The caller needs token flags, supply, owner, metadata, series, schemas, external mappings, or price rows. |
| `get_token_with_id(symbol, extended, carbon_token_id)` | Compatibility helper that delegates to `get_token(...)` with an explicit Carbon token id. | Returns `TokenResult`. Same failures as `get_token(...)`. | Code already has both symbol and Carbon token id. |
| `get_tokens(*, extended=True, owner_address=None, address_type=None)` | Reads token definitions. Optional owner and address type filters are forwarded when provided. | Returns `list[TokenResult]`. Raises `RPCError` if the endpoint does not return an array. | Token browser pages need token definitions, optionally filtered by owner. |
| `get_tokens_by_owner(owner_address, *, extended=True)` | Convenience filter for `get_tokens(...)` by owner address. | Returns `list[TokenResult]`. Same failures as `get_tokens(...)`. | Code wants owner filtering without manually passing optional parameters. |
| `get_tokens_by_owner_with_address_type(owner_address, address_type, *, extended=True)` | Owner-filtered token read that also forwards address type. | Returns `list[TokenResult]`. Same failures as `get_tokens(...)`. | Node-specific address-type filtering matters for owner token reads. |
| `get_tokens_as_map(*, extended=True)` | Loads tokens and maps them by `TokenResult.symbol`. | Returns `dict[str, TokenResult]`. Raises `RPCError` if `get_tokens(...)` fails. Duplicate symbols would be overwritten by later entries. | Callers repeatedly look up token definitions by symbol. |
| `get_token_data(symbol, nft_id)` | Calls `getTokenData` for a token symbol and NFT id. | Returns `TokenDataResult`. Raises `RPCError` for node or decode failures. | Code needs one NFT instance and already knows the legacy NFT id. |
| `get_token_series(symbol, carbon_token_id=0, page_size=100, cursor="")` | Reads one cursor page of NFT series for a token symbol and optional Carbon token id. | Returns `CursorPaginatedResult[list[TokenSeriesResult]]`. Raises `RPCError` if the response is not cursor-paginated. | The result set can be large and the UI must page through series. |
| `get_token_series_by_id(symbol, *, carbon_token_id=0, series_id="", carbon_series_id=0)` | Reads one series by Phantasma series id, Carbon token id, Carbon series id, or a combination accepted by the node. | Returns `TokenSeriesResult`. Raises `RPCError` for node or decode failures. | The caller has a specific series identifier and does not need a cursor page. |
| `get_token_nfts(carbon_token_id, carbon_series_id=0, *, series_id="", page_size=100, cursor="", extended=True)` | Reads one cursor page of NFTs under a Carbon token and optional Carbon or Phantasma series id. | Returns `CursorPaginatedResult[list[TokenDataResult]]`. Raises `RPCError` if the response is not cursor-paginated. | A collection page needs NFT instances for a token or series. |
| `get_token_nfts_with_series_id(carbon_token_id, carbon_series_id, series_id, page_size, cursor, extended)` | Positional variant that delegates to `get_token_nfts(...)`. | Returns `CursorPaginatedResult[list[TokenDataResult]]`. Same failures as `get_token_nfts(...)`. | Existing code passes all NFT filters positionally. |
| `get_nft(symbol, nft_id, *, extended=True)` | Calls `getNFT` for one NFT id under a symbol. | Returns `TokenDataResult`. Raises `RPCError` for node or decode failures. | The caller has one NFT id and does not need account or series paging. |
| `get_nfts(symbol, nft_ids, *, extended=True)` | Reads multiple NFT ids. `nft_ids` can be a comma-separated string or a sequence joined by the SDK. | Returns `list[TokenDataResult]`. Raises `RPCError` if the endpoint does not return an array. | Batch NFT reads are preferred over one request per id. |
| `get_nfts_text(symbol, nft_ids, *, extended=True)` | Compatibility form for a prebuilt comma-separated NFT id string. | Returns `list[TokenDataResult]`. Same failures as `get_nfts(...)`. | The caller already has the wire-format id list. |

Cursor example:

```python
cursor = ""
while True:
    page = rpc.get_token_series("ART", page_size=100, cursor=cursor)
    for series in page.result:
        print(series.series_id, series.carbon_series_id)
    if not page.cursor:
        break
    cursor = page.cursor
```

## Account Token And NFT Inventory Cursors

| API | Purpose and parameters | Returns and failures | Use it when |
| --- | ---------------------- | -------------------- | ----------- |
| `get_account_fungible_tokens(account, token_symbol="", carbon_token_id=0, *, page_size=100, cursor="", check_address_reserved_byte=False, address_type=None)` | Reads a cursor page of fungible balances for an account. Optional symbol or Carbon token id filters narrow the result. | Returns `CursorPaginatedResult[list[BalanceResult]]`. Raises `RPCError` if the response is not cursor-paginated. | Wallet inventory needs fungible balances without loading unrelated account data. |
| `get_account_fungible_tokens_with_address_type(account, token_symbol, carbon_token_id, page_size, cursor, check_address_reserved_byte, address_type)` | Positional variant that includes the address-type control. | Returns `CursorPaginatedResult[list[BalanceResult]]`. Same failures as `get_account_fungible_tokens(...)`. | Infrastructure must pass all address validation controls explicitly. |
| `get_account_nfts(account, token_symbol="", carbon_token_id=0, carbon_series_id=0, *, page_size=100, cursor="", extended=True, check_address_reserved_byte=False, address_type=None)` | Reads a cursor page of NFT instances held by an account, optionally filtered by symbol, Carbon token id, or Carbon series id. | Returns `CursorPaginatedResult[list[TokenDataResult]]`. Raises `RPCError` if the response is not cursor-paginated. | Wallet inventory or owner dashboard needs account-owned NFT rows. |
| `get_account_nfts_with_address_type(account, token_symbol, carbon_token_id, carbon_series_id, page_size, cursor, extended, check_address_reserved_byte, address_type)` | Positional variant that includes the address-type control. | Returns `CursorPaginatedResult[list[TokenDataResult]]`. Same failures as `get_account_nfts(...)`. | Address-type controls are required for account-owned NFT reads. |
| `get_account_owned_tokens(account, token_symbol="", carbon_token_id=0, *, page_size=100, cursor="", check_address_reserved_byte=False, address_type=None)` | Reads a cursor page of token definitions owned by an account. | Returns `CursorPaginatedResult[list[TokenResult]]`. Raises `RPCError` if the response is not cursor-paginated. | Creator or owner dashboards list tokens controlled by an account. |
| `get_account_owned_tokens_with_address_type(account, token_symbol, carbon_token_id, page_size, cursor, check_address_reserved_byte, address_type)` | Positional variant with address-type control. | Returns `CursorPaginatedResult[list[TokenResult]]`. Same failures as `get_account_owned_tokens(...)`. | Owner-token reads require explicit address-type handling. |
| `get_account_owned_token_series(account, token_symbol="", carbon_token_id=0, *, page_size=100, cursor="", check_address_reserved_byte=False, address_type=None)` | Reads a cursor page of token series owned by an account. | Returns `CursorPaginatedResult[list[TokenSeriesResult]]`. Raises `RPCError` if the response is not cursor-paginated. | Creator dashboards need series-level ownership, not individual NFT instances. |
| `get_account_owned_token_series_with_address_type(account, token_symbol, carbon_token_id, page_size, cursor, check_address_reserved_byte, address_type)` | Positional variant with address-type control. | Returns `CursorPaginatedResult[list[TokenSeriesResult]]`. Same failures as `get_account_owned_token_series(...)`. | Series ownership reads require explicit address-type handling. |

## Auctions, Archives, Scripts, And Broadcasting

| API | Purpose and parameters | Returns and failures | Use it when |
| --- | ---------------------- | -------------------- | ----------- |
| `get_auctions_count(chain, symbol)` | Reads the number of auctions for a token symbol on a chain. | Returns `int`; raises `RPCError` if the node value cannot be coerced to an integer. | Marketplace pagination needs a total count before reading pages. |
| `get_auctions(chain, symbol, page, page_size)` | Reads one numeric page of auctions for a token symbol. | Returns `PaginatedResult[list[AuctionResult]]`. Raises `RPCError` if the response is not a paginated object. | Marketplace UI lists auctions with page/page-size pagination. |
| `get_auction(chain, symbol, token_id)` | Reads one auction by chain, token symbol, and token id. | Returns `AuctionResult`. Raises `RPCError` for node or decode failures. | A detail page needs one auction listing. |
| `get_archive(archive_hash)` | Reads archive metadata by archive hash. | Returns `ArchiveResult`. Raises `RPCError` for node or decode failures. | Storage tooling needs archive size, owners, block count, or missing block data. |
| `write_archive(archive_hash, block_index, block_content)` | Writes one archive block. `bytes` content is base64-encoded by the SDK; `str` content is passed as already encoded content. | Returns `bool`; raises `RPCError` if the node value is not boolean-compatible. | Storage tooling has raw block bytes or already encoded block content to submit. |
| `write_archive_base64(archive_hash, block_index, block_content)` | Alias for `write_archive(...)` when `block_content` is already a base64 string. | Returns `bool`. Same failures as `write_archive(...)`. | The caller already stores archive block content as base64 text. |
| `read_archive(archive_hash, block_index)` | Reads one archive block by archive hash and block index. | Returns `str` exactly as reported by the node. Raises `RPCError` for node failures. | Storage tooling needs archive block content. |
| `invoke_raw_script(chain, script_hex)` | Executes a VM script as a read-only invocation on a chain. It does not create or broadcast a transaction. | Returns `ScriptResult`; decode `result` or indexed `results` with model helpers. Raises `RPCError` for node or decode failures. | The caller needs read-only contract output before deciding whether to build a transaction. |
| `send_raw_transaction(tx)` | Broadcasts a signed VM transaction. `tx` can be a `Transaction`, raw bytes, or hex string; `Transaction` and bytes are converted to hex. | Returns the transaction hash from a string response or response object `hash` field. Raises `RPCError` if the response has an embedded error or no hash. | The caller already has a signed VM transaction or wants the SDK to serialize a signed `Transaction`. |
| `send_carbon_transaction(tx)` | Broadcasts a serialized signed Carbon transaction. `bytes` are converted to hex; `str` is sent as provided. | Returns the transaction hash from a string response or response object `hash` field. Raises `RPCError` if no hash is returned. | The caller already has signed Carbon transaction bytes or hex. |

Broadcast example:

```python
tx_hash = rpc.send_raw_transaction(signed_transaction)
final = rpc.get_transaction(tx_hash)
if final.state_is_success:
    print(final.result)
```

## Local Signing Helpers And Carbon Result Parsers

These helpers hold or use private keys in the current process. Use them for
trusted backend tooling, CLIs, tests, or local scripts. Browser and wallet flows
should request wallet signatures instead of passing private keys into the SDK.

| API | Purpose and parameters | Returns and failures | Use it when |
| --- | ---------------------- | -------------------- | ----------- |
| `sign_and_send_transaction(keys, nexus, script, chain="main", payload=b"", *, expiration=None)` | Builds a VM `Transaction` from a script, payload, nexus, chain, and expiration. If `expiration` is omitted, the SDK uses current Unix time plus 20 minutes. The transaction is signed with `keys` and sent with `send_raw_transaction(...)`. | Returns the transaction hash. Raises `RPCError` for send failures; transaction construction or signing can raise SDK crypto/serialization errors from the underlying types. | Trusted code has a VM script and wants one call for transaction construction, signing, and broadcast. |
| `sign_and_send_built_transaction(tx, keys)` | Signs an existing `Transaction` object and broadcasts it with `send_raw_transaction(...)`. | Returns the transaction hash. Raises `RPCError` for send failures and propagates signing errors from the transaction/key types. | Code has already set transaction fields such as nexus, chain, payload, and expiration. |
| `sign_carbon_transaction(msg, keys)` | Signs an unsigned Carbon `TxMsg` with `keys`. | Returns `SignedTxMsg`. Propagates signing or serialization-related SDK errors from Carbon helpers. | A caller needs the signed Carbon message object before deciding how to serialize or send it. |
| `sign_and_send_carbon_transaction(msg, keys)` | Signs a Carbon `TxMsg`, serializes the signed message, and broadcasts it with `send_carbon_transaction(...)`. | Returns the transaction hash. Raises `RPCError` for send failures and propagates Carbon signing/serialization errors. | Trusted code owns the private key and wants to broadcast an unsigned Carbon message. |
| `parse_create_token_result(result_hex)` | Delegates to the Carbon create-token result parser. `result_hex` should be `TransactionResult.result` from a finalized successful transaction. | Returns the created Carbon token id as `int`. Parser errors are raised by the Carbon parser when the result hex is malformed or not the expected shape. | After `get_transaction(...)` reports success for a create-token transaction, the caller needs the new token id. |
| `parse_create_token_series_result(result_hex)` | Delegates to the Carbon create-series result parser. `result_hex` should be `TransactionResult.result` from a finalized successful transaction. | Returns the created Carbon series id as `int`. Parser errors are raised by the Carbon parser when the result hex is malformed or not the expected shape. | After `get_transaction(...)` reports success for a create-series transaction, the caller needs the new series id. |
