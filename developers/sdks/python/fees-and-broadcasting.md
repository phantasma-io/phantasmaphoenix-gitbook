# Python SDK Fees And Broadcasting

The Python SDK can build and sign VM transactions and Carbon transactions. It
does not hide broadcasting behind examples: applications choose the endpoint,
key source, fee options, confirmation policy, and retry behavior.

## Two Transaction Families

| Family | Build with | Broadcast with | Result handling |
| ------ | ---------- | -------------- | --------------- |
| VM script transaction | `ScriptBuilder` + `Transaction` | `PhantasmaRPC.send_raw_transaction(...)` | `PhantasmaRPC.get_transaction(...)`, `TransactionResult.state_is_success` |
| Carbon transaction | `TxMsg` / Carbon lifecycle helpers | `PhantasmaRPC.send_carbon_transaction(...)` | `PhantasmaRPC.get_transaction(...)`, Carbon result parser helpers |

VM transactions use nexus/chain names and a VM script. Carbon transactions use
Carbon `TxMsg` fields such as `expiry`, `max_gas`, `max_data`, `gas_from`, and
typed Carbon payloads.

## Carbon Fee Options

High-level Carbon lifecycle builders accept fee option objects:

| Class | Used by | Default behavior |
| ----- | ------- | ---------------- |
| `FeeOptions` | generic Carbon messages and NFT mint helpers | `calculate_max_gas(count=1)`, defaulting to `gas_fee_base * fee_multiplier` for one item |
| `CreateTokenFeeOptions` | `build_create_token_tx*` | includes create-token base and symbol-length fee estimate |
| `CreateSeriesFeeOptions` | `build_create_token_series_tx*` | includes create-series base estimate |
| `MintNFTFeeOptions` | NFT mint helpers | `calculate_max_gas(count_or_tokens=1)`, where a count or token list scales the mint gas maximum |

```python
from phantasma_py.carbon import CreateTokenFeeOptions

fees = CreateTokenFeeOptions()
max_gas = fees.calculate_max_gas_for_symbol("MYNFT")
```

These values are maximums placed into the transaction. The chain determines the
actual consumed fee.

Direct `build_mint_non_fungible_tx*` calls mint one NFT and use
`fees.calculate_max_gas(1)`. `build_mint_phantasma_non_fungible_tx*` accepts a
sequence of public mint records and uses the sequence length, so a batch of five
NFTs carries five times the one-mint maximum gas.

## `max_data`

Carbon builders default `max_data` to `100_000_000`. This is the maximum data
escrow cap carried by the transaction. The chain aborts the transaction if the
required data escrow is greater than the cap.

```python
tx_hex = build_create_token_tx_and_sign_hex(
    token_info,
    keys,
    max_data=100_000_000,
)
```

Use a larger cap only after the application understands the storage growth of
the operation it is building. Unused escrow is handled by the chain, not by the
SDK.

## Expiry

High-level Carbon builders use `expiry=0` as "now plus 60 seconds" based on
`now_unix_millis()`.

```python
from phantasma_py.carbon import now_unix_millis

expiry = now_unix_millis() + 5 * 60 * 1000
```

Pass an explicit expiry when the transaction may wait in a signing queue or
when your service batches transactions.

## Explicit Carbon Broadcast

```python
from phantasma_py.rpc import PhantasmaRPC

rpc = PhantasmaRPC("https://testnet.phantasma.info/rpc")
tx_hash = rpc.send_carbon_transaction(signed_tx_hex)
```

`send_carbon_transaction(...)` accepts signed Carbon bytes or hex. It returns the
transaction hash reported by the RPC endpoint.

## Confirmation And Result Parsing

Broadcasting only submits the transaction. Fetch the confirmed transaction and
then parse the result for the specific Carbon operation.

```python
from phantasma_py.carbon import parse_create_token_result
from phantasma_py.rpc import PhantasmaRPC

rpc = PhantasmaRPC("https://testnet.phantasma.info/rpc")

tx_hash = rpc.send_carbon_transaction(signed_create_token_hex)
tx = rpc.get_transaction(tx_hash)

if not tx.state_is_success:
    raise RuntimeError(f"transaction failed: {tx.state}")

carbon_token_id = parse_create_token_result(tx.result)
```

Use the parser that matches the operation:

| Operation | Parser |
| --------- | ------ |
| Create token | `parse_create_token_result(result_hex)` |
| Create token series | `parse_create_token_series_result(result_hex)` |
| Direct Carbon NFT mint | `parse_mint_non_fungible_result(carbon_token_id, result_hex)` |
| Phantasma NFT helper mint | `parse_mint_phantasma_non_fungible_result(result_hex)` |

Do not parse one operation's result with another operation's parser.

## VM Broadcast

```python
from phantasma_py.rpc import PhantasmaRPC

rpc = PhantasmaRPC("https://testnet.phantasma.info/rpc")
tx_hash = rpc.send_raw_transaction(tx)
```

`send_raw_transaction(...)` accepts a `Transaction`, bytes, or hex. If you pass a
`Transaction`, it serializes the signed bytes.

## Combined Sign And Send Helpers

`PhantasmaRPC` also exposes helpers that combine local signing and broadcast:

| Helper | Family |
| ------ | ------ |
| `sign_and_send_transaction(...)` | VM script transaction |
| `sign_carbon_transaction(...)` | sign a Carbon `TxMsg` locally |
| `sign_and_send_carbon_transaction(...)` | Carbon `TxMsg` signing plus broadcast |

These are convenience methods for applications that already own the key and
endpoint selection. They are not wallet prompts and they do not add user
confirmation.

## Read Back After Broadcast

For token workflows, always verify chain state after parsing the result:

```python
token = rpc.get_token("MYNFT", carbon_token_id=carbon_token_id)
series = rpc.get_token_series("MYNFT", carbon_token_id=carbon_token_id)
```

For NFT mints, read by token id, series cursor, account cursor, or NFT id:

```python
nfts = rpc.get_token_nfts(carbon_token_id, page_size=20, extended=True)
owned = rpc.get_account_nfts(keys.address.text, page_size=20, extended=True)
```

This catches a common integration mistake: a transaction can be submitted to an
endpoint, but the app may be reading from a different network or a stale RPC
node.

## Safety Checklist

- Use mainnet, testnet, and devnet endpoints intentionally.
- Keep wallet WIF values outside docs, logs, and Git.
- Check `tx.state_is_success` before parsing `tx.result`.
- Keep the token symbol and Carbon token id together in application state.
- Keep the exact `TokenSchemas` used for deployment; do not reconstruct a
different schema before creating series or minting.
- Treat examples as local builder examples unless they explicitly say they were
  run against a funded live endpoint.
