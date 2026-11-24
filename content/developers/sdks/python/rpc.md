---
title: "Python SDK RPC"
linkTitle: "RPC"
weight: 20
---

`phantasma_py.rpc` contains the JSON-RPC transport and typed response models for
current Phantasma RPC calls exposed by the SDK.

## Client

```python
from phantasma_py.rpc import PhantasmaRPC

rpc = PhantasmaRPC("http://localhost:5172/rpc")
version = rpc.get_version()

print(version.version, version.commit)
```

`JsonRpcClient` sends positional JSON-RPC parameters, validates response ids, and
raises `RPCError` for transport and RPC failures.

Pass `api_key=...` to send an API key in the `X-Api-Key` header on every request:

```python
rpc = PhantasmaRPC("http://localhost:5172/rpc", api_key="your-api-key")
```

```python
from phantasma_py.errors import RPCError
from phantasma_py.rpc import PhantasmaRPC

rpc = PhantasmaRPC.mainnet()

try:
    owner = rpc.lookup_name("example-name")
except RPCError as exc:
    print(exc.code, exc.data)
```

## Account And Balance Reads

```python
from phantasma_py.rpc import PhantasmaRPC

rpc = PhantasmaRPC.mainnet()
info = rpc.get_account_info("P...")
balance = rpc.get_token_balance("P...", "SOUL")

print(info.name, balance.decimal_amount())
```

`get_token_balance(address, symbol)` answers one token; `get_account_fungible_tokens(address)`
pages through every fungible balance of the address. Both return `BalanceResult`
values, and `decimal_amount()` renders the amount with the token's decimals.

## Blocks And Transactions

```python
from phantasma_py.rpc import PhantasmaRPC

rpc = PhantasmaRPC("http://localhost:5172/rpc")

height = rpc.get_block_height("main")
block = rpc.get_block_by_height("main", height)
tx = rpc.get_transaction(block.txs[0])

print(block.hash)
print(tx.state, tx.state_is_success)
```

Chain-aware helpers pass the chain name where the current RPC expects it:

```python
count = rpc.get_block_transaction_count_by_hash(block.hash, chain="main")
tx = rpc.get_transaction_by_block_hash_and_index(block.hash, 0, chain="main")
```

## Tokens And NFTs

```python
from phantasma_py.rpc import PhantasmaRPC

rpc = PhantasmaRPC.mainnet()

token = rpc.get_token("SOUL")
print(token.symbol, token.decimals, token.is_fungible())

series_page = rpc.get_token_series("ART", carbon_token_id=1)
nfts_page = rpc.get_token_nfts(1, page_size=20, extended=True)
```

The SDK exposes both symbol-oriented RPC calls and current Carbon id-aware calls
such as `get_token_series`, `get_token_series_by_id`, `get_token_nfts`,
`get_account_fungible_tokens`, `get_account_nfts`, and account-owned token or
series cursors.

Cursor result wrappers expose the decoded items and the next cursor returned by
the node. Keep passing the returned cursor until the endpoint returns an empty
cursor or your application has enough results.

```python
cursor = ""

while True:
    page = rpc.get_token_nfts(
        carbon_token_id=1,
        carbon_series_id=0,
        page_size=20,
        cursor=cursor,
        extended=True,
    )

    for nft in page.result or []:
        print(nft.id, nft.series)

    if not page.cursor:
        break

    cursor = page.cursor
```

Use account cursor helpers when the question starts from a wallet address:

```python
owned = rpc.get_account_nfts(
    "P...",
    token_symbol="ART",
    carbon_token_id=1,
    carbon_series_id=0,
    page_size=20,
    extended=True,
)
```

Use token cursor helpers when the question starts from a collection or series.

## Invoke Script

`invoke_raw_script(chain, script_hex)` returns a `ScriptResult`. The result can
decode VM object bytes when the RPC response contains encoded VM results.

```python
from phantasma_py.rpc import PhantasmaRPC
from phantasma_py.vm import ScriptBuilder

rpc = PhantasmaRPC("http://localhost:5172/rpc")
script = ScriptBuilder.begin().call_interop("Runtime.Time").end_script_hex()
result = rpc.invoke_raw_script("main", script)

value = result.decode_result()
print(value)
```

## Broadcasting

Broadcasting is intentionally explicit:

```python
tx_hash = rpc.send_raw_transaction(raw_transaction_hex)
carbon_hash = rpc.send_carbon_transaction(raw_carbon_transaction_hex)
```

Use `sign_and_send_transaction(...)` for VM transactions and `send_transaction(...)` for Carbon messages
only with keys, funds, and endpoints that are intentionally selected by the
caller.

For the full broadcast, confirmation, and result parser flow, see
[Fees And Broadcasting](fees-and-broadcasting.md).

## Custom RPC Calls

If the node exposes a method that does not have a typed wrapper yet, use
`PhantasmaRPC.call(...)` directly. The SDK still sends JSON-RPC positional
parameters and validates the response envelope.

```python
raw = rpc.call("getBlockHeight", "main")
```

Prefer typed wrappers when they exist; typed wrappers decode dataclasses and
use the parameter order expected by current RPC methods.

## RPC Method Families

The current `PhantasmaRPC` class wraps these groups:

| Group | Representative methods |
| ----- | ---------------------- |
| Build info | `get_version`, `get_phantasma_vm_config` |
| Account | `get_account_info`, `get_account_infos`, `lookup_name`, `get_address_transactions`; `get_account` and `get_accounts` are deprecated |
| Blocks | `get_block_height`, `get_block_by_height`, `get_block_by_hash`, `get_latest_block` |
| Transactions | `get_transaction`, `get_transaction_by_block_hash_and_index`, `send_raw_transaction` |
| Chain and contracts | `get_chains`, `get_chain`, `get_nexus`, `get_contract`, `get_contracts` |
| Organizations | `get_organization`, `get_organizations`, `get_organization_members`, `get_organization_member` |
| Tokens and NFTs | `get_token`, `get_tokens`, `get_token_balance`, `get_token_series`, `get_token_nfts`, `get_nft`, `get_nfts` |
| Account token cursors | `get_account_fungible_tokens`, `get_account_nfts`, `get_account_owned_tokens`, `get_account_owned_token_series` |
| Auctions and archives | `get_auctions`, `get_auction`, `get_archive`, `read_archive`, `write_archive` |
| Scripts and Carbon | `invoke_raw_script`, `send_carbon_transaction`, `send_transaction` |

`get_chains`, `get_chain`, `get_nexus`, `get_leaderboard` and the archive
methods are stubs on the node: they answer an empty or default value. See
[Stubbed Node Methods](reference/rpc-methods.md#stubbed-node-methods).
