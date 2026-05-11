# Rust SDK RPC Client

`PhantasmaRpc` is the async typed JSON-RPC facade in `phantasma_sdk::rpc`. Each
wrapper sends positional JSON-RPC parameters to the configured endpoint and
deserializes the response into the result structs documented in
[RPC Result Models](rpc-models.md). All fallible methods return
`phantasma_sdk::Result<T>`.

RPC methods can return `PhantasmaError::Http`, `PhantasmaError::Json`, or
`PhantasmaError::Rpc` for transport failures, invalid JSON, JSON-RPC error
objects, mismatched response ids, missing `result` fields, integer/boolean
coercion failures, and typed deserialization failures. Methods that submit
transactions return the transaction hash reported by the node; they do not wait
for final execution state. Poll `get_transaction(...)` after broadcasting when
the caller needs the final `state`, `result`, events, or fees.

Common parameters:

| Parameter | Meaning |
| --------- | ------- |
| `chain` | Chain name passed to chain-scoped RPCs. Rust wrappers require this argument explicitly. |
| `extended` | Requests nested data from RPC methods that support compact and expanded response shapes. Use `false` for list views and `true` when the caller needs balances, metadata, series, ABI, or other nested fields. |
| `page`, `page_size` | Numeric pagination for older RPC methods. The response is a `PaginatedResult<T>`. |
| `cursor` | Opaque cursor returned by cursor-based token and NFT inventory methods. Reuse the same filters and pass the returned cursor to read the next page. |
| `check_address_reserved_byte`, `address_type` | Address validation controls forwarded to RPC methods that expose them. Use the default form unless the caller deliberately needs the node's address-type variants. |

## Construction, Transport, And Raw Calls

| API | Purpose and parameters | Returns and failures | Use it when |
| --- | ---------------------- | -------------------- | ----------- |
| `PhantasmaRpc::new(endpoint)` | Creates a client for `endpoint` with `ReqwestTransport` and a 30-second timeout. | Returns `PhantasmaRpc<ReqwestTransport>`. Construction does not call the node. Later calls return `Result<T>`. | Application code has an explicit RPC URL, including local nodes and private infrastructure. |
| `PhantasmaRpc::mainnet()` | Creates a client for `https://pharpc1.phantasma.info/rpc`. | Returns `PhantasmaRpc<ReqwestTransport>`. | A tool intentionally targets the default public mainnet endpoint. |
| `PhantasmaRpc::testnet()` | Creates a client for `https://testnet.phantasma.info/rpc`. | Returns `PhantasmaRpc<ReqwestTransport>`. | A tool intentionally targets the default public testnet endpoint. |
| `PhantasmaRpc::with_transport(endpoint, transport)` | Creates a client with a caller-provided `RpcTransport`. | Returns `PhantasmaRpc<T>`. Later requests use the provided transport. | Tests, embedded applications, or services need custom HTTP behavior. |
| `with_timeout(timeout)` | Replaces the client's request timeout and returns the updated client. | Returns `Self`. | A caller needs endpoint-specific timeout policy. |
| `call_value(method, params)` | Sends a raw JSON-RPC call with id `"0"` and returns the raw JSON `result`. | Returns `serde_json::Value`. Errors if transport fails, the body is not a valid JSON-RPC response, the id is not `"0"` or `0`, the response contains `error`, or `result` is missing. | A node method is needed before the SDK has a typed wrapper. |
| `call<R>(method, params)` | Calls `call_value(...)` and deserializes the raw result into `R`. | Returns `R`. Converts deserialization failures into `PhantasmaError::Rpc`. | Wrapper code wants typed decoding for a method not yet exposed as a named wrapper. |
| `parse_json_rpc_response(status, body)` | Validates a JSON-RPC response object and extracts `result`. It treats JSON-RPC `error` objects as failures and rejects missing or mismatched ids. | Returns raw `Value` or `PhantasmaError::Rpc`. | Custom transports want to reuse the SDK's JSON-RPC response validation. |
| `convert_decimals(amount, decimals)` | Formats a base-unit integer string with a decimal point. It trims trailing fractional zeroes and does not fetch token metadata. | Returns `String`. It does not validate that `amount` came from a token with matching decimals. | UI code has a base-unit amount and known decimals but does not have a `BalanceResult` helper. |

Example:

```rust
use phantasma_sdk::{PhantasmaRpc, Result};

#[tokio::main]
async fn main() -> Result<()> {
    let rpc = PhantasmaRpc::new("http://localhost:5172/rpc");
    let height = rpc.get_block_height("main").await?;
    println!("{height}");
    Ok(())
}
```

## Build And VM Configuration

| API | Purpose and parameters | Returns and failures | Use it when |
| --- | ---------------------- | -------------------- | ----------- |
| `get_version()` | Calls `getVersion` with no parameters. | Returns `VersionResult`, an alias of `BuildInfoResult`. | Health checks, support logs, endpoint diagnostics, and version display. |
| `get_phantasma_vm_config(chain)` | Calls `getPhantasmaVmConfig` for a chain. | Returns `PhantasmaVmConfigResult`. Errors if the endpoint cannot return or deserialize the config object. | Tooling needs current VM gas cost settings before showing or validating contract execution costs. |

## Accounts, Names, And Balances

| API | Purpose and parameters | Returns and failures | Use it when |
| --- | ---------------------- | -------------------- | ----------- |
| `get_platforms()` | Calls `getPlatforms` to read configured external platforms and interop mappings. | Returns `Vec<PlatformResult>`. Errors if the result is not an array of platform objects. | Explorer or bridge tooling needs platform metadata. |
| `get_account(address)` | Reads one account with `extended=false`. | Returns `AccountResult`. Errors when the node rejects the address or the result cannot be deserialized. | A wallet or backend needs a compact account read. Use `get_account_with_address_type(...)` when extended or address-type controls are required. |
| `get_account_with_address_type(address, extended, check_address_reserved_byte, address_type)` | Reads one account while forwarding `extended`, reserved-byte, and address-type controls. | Returns `AccountResult`. Errors on node or decode failures. | Infrastructure code must exercise the node's address-type parameters directly. |
| `get_accounts(addresses, extended)` | Reads multiple accounts. `addresses` is a slice of string-like values joined with commas by the SDK. | Returns `Vec<AccountResult>`. Errors if the endpoint does not return an array. | Batch account reads are cheaper for the caller than one request per address. |
| `get_accounts_text(addresses, extended)` | Reads multiple accounts from a prebuilt comma-separated address string. | Returns `Vec<AccountResult>`. Same failures as `get_accounts(...)`. | The caller already has the wire-format address list. |
| `get_accounts_with_address_type(addresses, extended, check_address_reserved_byte, address_type)` | Reads multiple accounts from a comma-separated string while forwarding address validation controls. | Returns `Vec<AccountResult>`. Errors on node or decode failures. | Batch account reads need the node's address-type parameters. |
| `lookup_name(name)` | Calls `lookUpName` and deserializes the result as `String`. | Returns the resolved address string. Errors if the name lookup fails at the node. | User input is a Phantasma name and the application needs the address. |
| `look_up_name(name)` | Alias that delegates to `lookup_name(...)`. | Returns the same string result and has the same failures. | Code uses the older snake-case spelling and should not change call sites. |
| `get_address_transactions(address, page, page_size)` | Reads one numeric page of transaction hashes for an address. | Returns `PaginatedResult<AddressTransactionsResult>`. Errors if the result is not a paginated object. | Transaction history UI needs address-level transaction ids. |
| `get_address_transaction_count(address, chain)` | Reads the total number of address transactions on a chain. | Returns `u64`; the SDK accepts JSON numbers or integer-compatible strings. | UI needs total counts before or alongside paginated transaction history. |
| `get_token_balance(address, symbol, chain, extended)` | Reads one token balance for an address. The fourth positional value is sent directly to `getTokenBalance`; use the checked/address-type variants when that flag must mean reserved-byte checking. | Returns `BalanceResult`. Errors on node or decode failures. | A page needs exactly one balance row and does not need account profile, storage, stake, or all balances. |
| `get_token_balance_checked(address, symbol, chain, check_address_reserved_byte)` | Reads one token balance while forwarding the reserved-byte check flag. | Returns `BalanceResult`. Same failures as `get_token_balance(...)`. | Code needs reserved-byte checking but not an address type. |
| `get_token_balance_with_address_type(address, symbol, chain, check_address_reserved_byte, address_type)` | Reads one token balance while forwarding both address validation controls. | Returns `BalanceResult`. Same failures as `get_token_balance(...)`. | Node-specific address-type behavior matters for this balance read. |

## Blocks And Transactions

| API | Purpose and parameters | Returns and failures | Use it when |
| --- | ---------------------- | -------------------- | ----------- |
| `get_block_height(chain)` | Calls `getBlockHeight` for a chain. | Returns `u64`; the SDK accepts JSON numbers or integer-compatible strings. | A sync loop or status panel needs the current chain height. |
| `get_block_by_height(chain, height)` | Reads a block by chain and height. | Returns `BlockResult`. Errors if the block is unavailable or cannot be deserialized. | Ledger navigation starts from a known chain height. |
| `get_block_by_hash(hash)` | Reads a block by block hash. | Returns `BlockResult`. Errors on node or decode failures. | The caller already has a block hash from another result. |
| `get_latest_block(chain)` | Reads the latest block object for a chain. | Returns `BlockResult`. Errors on node or decode failures. | A status page needs both height and latest block metadata. |
| `get_block_transaction_count_by_hash(hash, chain)` | Delegates to the chain-first `get_block_transaction_count_by_hash_on_chain(...)`. | Returns `u64`; errors if the node value cannot be coerced to an integer. | Code uses hash-first argument order. |
| `get_block_transaction_count_by_hash_on_chain(chain, hash)` | Calls the chain-aware `getBlockTransactionCountByHash` wire method. | Returns `u64`; errors if the node value cannot be coerced to an integer. | A block view needs transaction count without loading or trusting the full block transaction list. |
| `get_transaction(hash)` | Reads a transaction by hash. | Returns `TransactionResult` with state, result hex, events, signatures, fee, and block placement. Errors if the transaction is not available or the result cannot be decoded. | Poll after broadcasting or display a known transaction. |
| `get_transaction_by_block_hash_and_index(block_hash, index, chain)` | Reads the transaction at `index` inside a block identified by hash and chain. | Returns `TransactionResult`. Errors for node errors, invalid index, or decode failure. | A block explorer is iterating transactions by block position. |
| `get_transaction_by_block_hash_and_index_on_chain(chain, block_hash, index)` | Chain-first alias for `get_transaction_by_block_hash_and_index(...)`. | Returns `TransactionResult`. Same failures as the alias target. | Code style follows the wire method's chain-first argument order. |

## Chain, Contract, Organization, And Leaderboard Metadata

| API | Purpose and parameters | Returns and failures | Use it when |
| --- | ---------------------- | -------------------- | ----------- |
| `get_chains(extended)` | Reads the chain list from the nexus. `extended` controls nested contract and dapp detail. | Returns `Vec<ChainResult>`. Errors if the result is not an array. | Explorer or infrastructure code needs all chain metadata. |
| `get_chain(chain, extended)` | Reads one chain by name. | Returns `ChainResult`. Errors on node or decode failures. | A page needs metadata for a specific chain. |
| `get_nexus(extended)` | Reads nexus metadata, including platforms, tokens, chains, governance, and organizations when the node returns them. | Returns `NexusResult`. Errors on node or decode failures. | Tooling needs a topology snapshot for the configured nexus. |
| `get_contract(contract_name, chain)` | Reads a contract by name on a chain. | Returns `ContractResult`, including script, ABI methods, and ABI events when available. Errors on node or decode failures. | Client tooling needs ABI information before constructing a VM call. |
| `get_contract_by_name(chain, name)` | Chain-first alias that delegates to `get_contract(...)`. | Returns `ContractResult`. Same failures as `get_contract(...)`. | Existing code uses the chain-first spelling. |
| `get_contract_by_address(chain, address)` | Reads a contract by address instead of name. | Returns `ContractResult`. Errors on node or decode failures. | The caller has a contract address from chain metadata or an event. |
| `get_contracts(chain, extended)` | Reads contracts deployed on a chain. | Returns `Vec<ContractResult>`. Errors if the result is not an array. | Explorer or developer tooling needs all chain contracts. |
| `get_organization(organization_id, extended)` | Reads organization metadata by id. | Returns `OrganizationResult`. Errors on node or decode failures. | Governance or validator tooling works with an organization id. |
| `get_organization_by_name(name, extended)` | Reads organization metadata by name. | Returns `OrganizationResult`. Errors on node or decode failures. | UI or CLI receives a human-readable organization name. |
| `get_organizations(extended)` | Reads the organization list. | Returns `Vec<OrganizationResult>`. Errors if the result is not an array. | A page needs an organization list; pass `true` only when nested data is needed. |
| `get_leaderboard(name)` | Reads a leaderboard by name. | Returns `LeaderboardResult`. Errors on node or decode failures. | A dapp or explorer displays leaderboard rows from the chain. |

## Tokens, Series, And NFT Reads

| API | Purpose and parameters | Returns and failures | Use it when |
| --- | ---------------------- | -------------------- | ----------- |
| `get_token(symbol, extended)` | Reads one token definition by symbol. | Returns `TokenResult`. Errors on node or decode failures. | The caller needs token flags, supply, owner, metadata, series, schemas, external mappings, or price rows. |
| `get_token_with_id(symbol, extended, token_id)` | Reads one token definition by symbol and Carbon token id. | Returns `TokenResult`. Errors on node or decode failures. | Code already has both symbol and Carbon token id. |
| `get_tokens(extended)` | Reads token definitions. | Returns `Vec<TokenResult>`. Errors if the endpoint does not return an array. | Token browser pages need token definitions. |
| `get_tokens_by_owner(owner, extended)` | Reads token definitions filtered by owner address. | Returns `Vec<TokenResult>`. Errors if the endpoint does not return an array. | Creator or owner dashboards list tokens controlled by an address. |
| `get_tokens_by_owner_with_address_type(owner, address_type, extended)` | Owner-filtered token read that also forwards address type. | Returns `Vec<TokenResult>`. Same failures as `get_tokens_by_owner(...)`. | Node-specific address-type filtering matters for owner token reads. |
| `get_tokens_as_map(extended)` | Loads tokens and maps them by `TokenResult.symbol`. | Returns `HashMap<String, TokenResult>`. Errors if `get_tokens(...)` fails. Duplicate symbols would be overwritten by later entries. | Callers repeatedly look up token definitions by symbol. |
| `get_token_data(symbol, token_id)` | Calls `getTokenData` for a token symbol and NFT id. | Returns `TokenDataResult`. Errors on node or decode failures. | Code needs one NFT instance and already knows the legacy NFT id. |
| `get_token_series(symbol, carbon_token_id, page_size, cursor)` | Reads one cursor page of NFT series for a token symbol and Carbon token id. | Returns `CursorPaginatedResult<Vec<TokenSeriesResult>>`. Errors if the response is not cursor-paginated. | The result set can be large and the UI must page through series. |
| `get_token_series_by_id(symbol, series_id)` | Reads one series by Phantasma series id. It delegates to `get_token_series_by_ids(symbol, 0, series_id, 0)`. | Returns `TokenSeriesResult`. Errors on node or decode failures. | The caller has the Phantasma series id and does not need Carbon ids. |
| `get_token_series_by_ids(symbol, carbon_token_id, series_id, carbon_series_id)` | Reads one series using the full identity set accepted by the node. | Returns `TokenSeriesResult`. Errors on node or decode failures. | The caller has Carbon token or series identifiers from Carbon transaction results. |
| `get_token_nfts(carbon_token_id, carbon_series_id, page_size, cursor, extended, series_id)` | Reads one cursor page of NFTs under a Carbon token and optional Carbon or Phantasma series id. | Returns `CursorPaginatedResult<Vec<TokenDataResult>>`. Errors if the response is not cursor-paginated. | A collection page needs NFT instances for a token or series. |
| `get_token_nfts_with_series_id(carbon_token_id, carbon_series_id, series_id, page_size, cursor, extended)` | Positional variant that delegates to `get_token_nfts(...)`. | Returns `CursorPaginatedResult<Vec<TokenDataResult>>`. Same failures as `get_token_nfts(...)`. | Existing code passes all NFT filters positionally. |
| `get_nft(symbol, token_id, extended)` | Calls `getNFT` for one NFT id under a symbol. | Returns `TokenDataResult`. Errors on node or decode failures. | The caller has one NFT id and does not need account or series paging. |
| `get_nfts(symbol, token_ids, extended)` | Reads multiple NFT ids. The slice is joined into a comma-separated string. | Returns `Vec<TokenDataResult>`. Errors if the endpoint does not return an array. | Batch NFT reads are preferred over one request per id. |
| `get_nfts_text(symbol, token_ids, extended)` | Reads multiple NFT ids from a prebuilt comma-separated string. | Returns `Vec<TokenDataResult>`. Same failures as `get_nfts(...)`. | The caller already has the wire-format id list. |

Cursor example:

```rust
let mut cursor = String::new();
loop {
    let page = rpc.get_token_series("ART", 0, 100, &cursor).await?;
    for series in &page.result {
        println!("{} {}", series.series_id, series.carbon_series_id);
    }
    if page.cursor.is_empty() {
        break;
    }
    cursor = page.cursor;
}
```

## Account Token And NFT Inventory Cursors

| API | Purpose and parameters | Returns and failures | Use it when |
| --- | ---------------------- | -------------------- | ----------- |
| `get_account_fungible_tokens(address, symbol, carbon_token_id, page_size, cursor, check_address_reserved_byte)` | Reads a cursor page of fungible balances for an account. Optional symbol or Carbon token id filters narrow the result when non-empty/non-zero. | Returns `CursorPaginatedResult<Vec<BalanceResult>>`. Errors if the response is not cursor-paginated. | Wallet inventory needs fungible balances without loading unrelated account data. |
| `get_account_fungible_tokens_with_address_type(address, symbol, carbon_token_id, page_size, cursor, check_address_reserved_byte, address_type)` | Variant that also forwards address type. | Returns `CursorPaginatedResult<Vec<BalanceResult>>`. Same failures as `get_account_fungible_tokens(...)`. | Infrastructure must pass all address validation controls explicitly. |
| `get_account_nfts(address, symbol, carbon_token_id, carbon_series_id, page_size, cursor, extended, check_address_reserved_byte)` | Reads a cursor page of NFT instances held by an account, optionally filtered by symbol, Carbon token id, or Carbon series id. | Returns `CursorPaginatedResult<Vec<TokenDataResult>>`. Errors if the response is not cursor-paginated. | Wallet inventory or owner dashboard needs account-owned NFT rows. |
| `get_account_nfts_with_address_type(address, symbol, carbon_token_id, carbon_series_id, page_size, cursor, extended, check_address_reserved_byte, address_type)` | Variant that also forwards address type. | Returns `CursorPaginatedResult<Vec<TokenDataResult>>`. Same failures as `get_account_nfts(...)`. | Address-type controls are required for account-owned NFT reads. |
| `get_account_owned_tokens(address, symbol, carbon_token_id, page_size, cursor, check_address_reserved_byte)` | Reads a cursor page of token definitions owned by an account. | Returns `CursorPaginatedResult<Vec<TokenResult>>`. Errors if the response is not cursor-paginated. | Creator or owner dashboards list tokens controlled by an account. |
| `get_account_owned_tokens_with_address_type(address, symbol, carbon_token_id, page_size, cursor, check_address_reserved_byte, address_type)` | Variant that also forwards address type. | Returns `CursorPaginatedResult<Vec<TokenResult>>`. Same failures as `get_account_owned_tokens(...)`. | Owner-token reads require explicit address-type handling. |
| `get_account_owned_token_series(address, symbol, carbon_token_id, page_size, cursor, check_address_reserved_byte)` | Reads a cursor page of token series owned by an account. | Returns `CursorPaginatedResult<Vec<TokenSeriesResult>>`. Errors if the response is not cursor-paginated. | Creator dashboards need series-level ownership, not individual NFT instances. |
| `get_account_owned_token_series_with_address_type(address, symbol, carbon_token_id, page_size, cursor, check_address_reserved_byte, address_type)` | Variant that also forwards address type. | Returns `CursorPaginatedResult<Vec<TokenSeriesResult>>`. Same failures as `get_account_owned_token_series(...)`. | Series ownership reads require explicit address-type handling. |

## Auctions, Archives, Scripts, And Broadcasting

| API | Purpose and parameters | Returns and failures | Use it when |
| --- | ---------------------- | -------------------- | ----------- |
| `get_auctions_count(chain, symbol)` | Reads the number of auctions for a token symbol on a chain. | Returns `u64`; the SDK accepts JSON numbers or integer-compatible strings. | Marketplace pagination needs a total count before reading pages. |
| `get_auctions(chain, symbol, page, page_size)` | Reads one numeric page of auctions for a token symbol. | Returns `PaginatedResult<Vec<AuctionResult>>`. Errors if the response is not a paginated object. | Marketplace UI lists auctions with page/page-size pagination. |
| `get_auction(chain, symbol, token_id)` | Reads one auction by chain, token symbol, and token id. | Returns `AuctionResult`. Errors on node or decode failures. | A detail page needs one auction listing. |
| `get_archive(hash)` | Reads archive metadata by archive hash. | Returns `ArchiveResult`. Errors on node or decode failures. | Storage tooling needs archive size, owners, block count, or missing block data. |
| `write_archive(hash, block_index, content)` | Base64-encodes raw bytes and writes one archive block. | Returns `bool`; the SDK accepts JSON booleans, 0/1 numbers, or string equivalents. | Storage tooling has raw block bytes to submit. |
| `write_archive_base64(hash, block_index, content)` | Writes one archive block when `content` is already base64 text. | Returns `bool`. Same failures as `write_archive(...)`. | The caller already stores archive block content as base64 text. |
| `read_archive(hash, block_index)` | Reads one archive block by archive hash and block index. | Returns `String` exactly as reported by the node. Errors on node failures. | Storage tooling needs archive block content. |
| `invoke_raw_script(chain, script_hex)` | Executes a VM script as a read-only invocation on a chain. It does not create or broadcast a transaction. | Returns `ScriptResult`; decode `result` or indexed `results` with model helpers. Errors on node or decode failures. | The caller needs read-only contract output before deciding whether to build a transaction. |
| `send_raw_transaction(tx_hex)` | Broadcasts a signed VM transaction hex string. | Returns the transaction hash from a string response or response object `hash` field. Errors if the response has an embedded error or no hash. | The caller already has signed VM transaction hex. |
| `send_transaction(tx)` | Serializes a signed `Transaction` with signatures and delegates to `send_raw_transaction(...)`. | Returns the transaction hash. Same failures as `send_raw_transaction(...)`. | Rust code has a signed `Transaction` object instead of prebuilt hex. |
| `send_carbon_transaction(tx)` | Hex-encodes serialized signed Carbon transaction bytes and broadcasts them. | Returns the transaction hash. Errors if no hash is returned. | The caller already has signed Carbon transaction bytes. |
| `send_signed_tx_msg(tx)` | Serializes a `SignedTxMsg` with Carbon serialization and delegates to `send_carbon_transaction(...)`. | Returns the transaction hash. Errors on Carbon serialization failure or send failure. | Code has a signed Carbon message object instead of serialized bytes. |

Broadcast example:

```rust
let tx_hash = rpc.send_transaction(&tx).await?;
let final_tx = rpc.get_transaction(&tx_hash).await?;
if final_tx.state_is_success() {
    println!("{}", final_tx.result);
}
```

## Local Signing Helpers And Carbon Result Parsers

These helpers hold or use private keys in the current process. Use them for
trusted backend tooling, CLIs, tests, or local scripts. Browser and wallet flows
should request wallet signatures instead of passing private keys into the SDK.

| API | Purpose and parameters | Returns and failures | Use it when |
| --- | ---------------------- | -------------------- | ----------- |
| `sign_and_send_transaction(keys, nexus, script, chain, payload, expiration)` | Builds a VM `Transaction`, uses `default_expiration_seconds()` when `expiration` is `None`, signs it with `keys`, and sends it with `send_transaction(...)`. | Returns the transaction hash. Errors on signing, serialization, or send failure. | Trusted code has a VM script and wants one call for transaction construction, signing, and broadcast. |
| `sign_and_send_built_transaction(tx, keys)` | Signs an existing mutable `Transaction` and broadcasts it with `send_transaction(...)`. | Returns the transaction hash. Errors on signing, serialization, or send failure. | Code has already set transaction fields such as nexus, chain, payload, and expiration. |
| `sign_carbon_transaction(msg, keys)` | Signs an unsigned Carbon `TxMsg` with `keys`. | Returns `SignedTxMsg`. Errors on Carbon signing or serialization-related failure. | A caller needs the signed Carbon message object before deciding how to serialize or send it. |
| `sign_and_send_carbon_transaction(msg, keys)` | Signs a Carbon `TxMsg`, serializes the signed message, and broadcasts it with `send_signed_tx_msg(...)`. | Returns the transaction hash. Errors on signing, serialization, or send failure. | Trusted code owns the private key and wants to broadcast an unsigned Carbon message. |
| `build_sign_send_tx_msg(msg, keys)` | Signs a Carbon `TxMsg` and sends the resulting `SignedTxMsg`. | Returns the transaction hash. Same failures as `sign_and_send_carbon_transaction(...)`. | Existing code uses this helper name for Carbon sign-and-send. |
| `send_create_token_tx(msg, keys)` | Signs and sends a Carbon create-token message through `build_sign_send_tx_msg(...)`. The current implementation returns `None` for the decoded token id; it does not poll the transaction. | Returns `(String, Option<u64>)`, where the first value is the transaction hash and the second is currently `None`. Errors on signing or send failure. | Code wants the legacy helper shape but still must poll `get_transaction(...)` and parse the result to obtain the token id. |
| `parse_create_token_result(result_hex)` | Delegates to the Carbon create-token result parser. `result_hex` should be `TransactionResult.result` from a finalized successful transaction. | Returns the created Carbon token id as `u64`. Errors if the result hex is malformed or not the expected shape. | After `get_transaction(...)` reports success for a create-token transaction, the caller needs the new token id. |
| `parse_create_token_series_result(result_hex)` | Delegates to the Carbon create-series result parser. `result_hex` should be `TransactionResult.result` from a finalized successful transaction. | Returns the created Carbon series id as `u32`. Errors if the result hex is malformed or not the expected shape. | After `get_transaction(...)` reports success for a create-series transaction, the caller needs the new series id. |
