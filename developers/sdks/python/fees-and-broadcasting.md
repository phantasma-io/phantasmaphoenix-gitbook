# Python SDK Fees And Broadcasting

A Carbon transaction is built, planned, signed and sent as four separate steps.
The same message works whether the key sits in memory, in a hardware wallet, or
in a wallet reached over Phantasma Link.

Builders carry no prices. A message built without a `max_gas` has a zero gas
offer, and that marks it as not yet planned. Signing such a message is refused,
because the chain never admits an offer of zero.

## Two Transaction Families

| Family | Build with | Broadcast with | Result handling |
| ------ | ---------- | -------------- | --------------- |
| VM script transaction | `ScriptBuilder` + `Transaction` | `PhantasmaRPC.send_raw_transaction(...)` | `get_transaction(...)`, `TransactionResult.state_is_success` |
| Carbon transaction | the Carbon builders | `PhantasmaRPC.send_transaction(...)` or `send_carbon_transaction(...)` | `get_transaction(...)`, the Carbon result parsers |

VM transactions use nexus and chain names and a VM script. Carbon transactions
use the `TxMsg` fields `expiry`, `max_gas`, `max_data`, `gas_from` and a typed
payload.

## The Four Steps

```python
from phantasma_py import PhantasmaRPC, build_transfer_fungible_tx, summarize_fee_plan
from phantasma_py.carbon import bytes32_from_public_key
from phantasma_py.crypto import PhantasmaKeys

rpc = PhantasmaRPC("https://testnet.phantasma.info/rpc")
keys = PhantasmaKeys.from_wif("...")

# 1. Build the message.
msg = build_transfer_fungible_tx(
    from_address=bytes32_from_public_key(keys.public_key),
    to=receiver,
    token_id=1,  # KCAL
    amount=100_000_000,
)

# 2. Plan it against the chain.
plan = rpc.fees.plan(msg)
summary = summarize_fee_plan(plan)
print(f"gas {summary.gas_bill} KCAL, storage deposit up to {summary.storage_ceiling} SOUL")

# 3 and 4. Sign and send.
tx_hash = rpc.send_transaction(msg, [keys])
```

`send_transaction` runs steps 2 to 4 in one call, plus the pre-flight. A message
whose `max_gas` is still zero is planned. A message the caller already planned
is sent as it is.

## What The Chain Bills

The chain charges for every byte the transaction puts in the block. It also
escrows SOUL for the storage the transaction adds. A message therefore carries
two ceilings, and both have to be set before it is signed:

| Field | Meaning |
| ----- | ------- |
| `TxMsg.max_gas` | The gas offer, in KCAL atoms. Unused gas is refunded. A short offer is rejected. |
| `TxMsg.max_data` | The storage escrow ceiling, in SOUL atoms. It prices every new 1024-byte storage quantum at the current `dataEscrowPerRow`. |

## The Fee Planner

`rpc.fees` is the `FeePlanner` of the chain the client talks to. It reads
`getGasConfig` through the client and keeps the answer for a minute.

| Member | What it does |
| ------ | ------------ |
| `plan(msg, options=None)` | Prices one message and returns a `FeePlan`. |
| `config(refresh=False)` | Returns the cached `GasConfig`. |
| `chain_params(refresh=False)` | Returns `expiry_window_ms`, the block rate target and the gas model version. |
| `plan_with(config, msg, options=None)` | Prices a message against a config the caller already holds. It touches no network. |
| `invalidate()` | Drops the cached config, so the next call reads it again. |

`plan_fees(msg, config, options=None)`, exported from `phantasma_py`, is the
same calculation as a plain function. Use it when the config is already in hand
and no client is available.

### The Plan

| Field | Meaning |
| ----- | ------- |
| `max_gas` | The gas offer that covers the bill. |
| `max_data` | The storage escrow ceiling. |
| `expected_gas_bill` | The bill the chain formula yields for these inputs. |
| `new_storage_quanta` | Storage quanta the operation creates. |
| `deleted_storage_quanta` | Storage quanta the operation deletes. The field is informational. |
| `kinds` | The operations the message was recognised as, in call order. |
| `exact` | Whether the bill is a prediction or a ceiling. |
| `envelope_bytes` | The signed size the plan was computed for. |
| `apply(msg)` | Returns a copy of the message with `max_gas` and `max_data` set. |

`summarize_fee_plan(plan)` renders the amounts in KCAL and SOUL through
`gas_bill`, `gas_offer` and `storage_ceiling`.
`summarize_fee_plan_with_decimals` takes the decimals explicitly.

### A Prediction Or A Ceiling

Part of the price depends on chain state that the message does not carry. One
example is whether the recipient already holds the token. Every such fact is
taken at the reading that costs more.

`plan.exact` reports the result. It is `True` when nothing the plan had to
assume could have changed the number. It is `False` when a costlier reading
decided part of the price, or when part of the message had to be budgeted. A
wallet shows the amount when the flag is `True`, and "up to" in front of the
amount when it is `False`.

The flag says nothing about facts the caller stated. A stated fact that is wrong
produces a wrong bill.

### Stating A Fact

`FeePlanOptions` is where a caller tells the planner a fact it would otherwise
assume. `PlanRequestOptions` carries it as `facts`, together with
`refresh_config`.

| Field | What it states |
| ----- | -------------- |
| `recipient_holds_token` | The recipient already has a balance row for this token. |
| `big_fungible` | Price the widest answer a variable length balance can have. |
| `token_burned_before` | The token's burnt counter already exists. |
| `supply_row_exists` | The supply row still exists and does not have to be recreated. |
| `duplicated_series` | The series mints duplicates. |
| `rom_has_meta_id` | The ROM carries an `_i` id. |
| `series_has_meta_id` | The series metadata carries an `_i` id. |
| `infusions` | What the burned NFTs hold. `None` is unstated. An empty list states that they hold nothing. |
| `script_units_allowance`, `script_event_bytes`, `script_storage_quanta` | The allowance for a VM script. |
| `witness_count` | How many witnesses will sign a `CALL`, `CALL_MULTI`, `TRADE` or `PHANTASMA` message. |

### Which Operation Reads Which Fact

| `NativeFeeKind` | Facts it reads |
| --------------- | -------------- |
| `TRANSFER_FUNGIBLE` | `recipient_holds_token` |
| `TRANSFER_NON_FUNGIBLE` | `recipient_holds_token` |
| `MINT_FUNGIBLE` | `recipient_holds_token`, `supply_row_exists`, `big_fungible` |
| `MINT_NON_FUNGIBLE` | `recipient_holds_token`, `supply_row_exists`, `rom_has_meta_id` |
| `MINT_PHANTASMA_NON_FUNGIBLE` | `recipient_holds_token`, `supply_row_exists`, `duplicated_series` |
| `BURN_FUNGIBLE` | `token_burned_before`, `supply_row_exists`, `big_fungible` |
| `BURN_NON_FUNGIBLE` | `token_burned_before`, `supply_row_exists`, and `infusions`, which is required |
| `CREATE_TOKEN` | none |
| `CREATE_TOKEN_SERIES` | `series_has_meta_id` |
| `REGISTER_NAME` | none |
| `SCRIPT` | none |

Balance rows of the gas and data tokens are free, so `recipient_holds_token`
cannot move the price of a KCAL or SOUL transfer.

`NativeFeeKind.SCRIPT` covers VM scripts and calls the SDK does not model. Their
work depends on execution, so they are budgeted and never predicted.
`plan.exact` is `False` whenever one is present.

A `CALL_MULTI` performs several operations. Each one is priced and then summed,
because the chain bills a batch as the sum of its calls with the envelope
counted once.

## Burning An NFT

A burn returns whatever the NFT holds at its own address, and the chain charges
for each returned asset. That set is chain state with no costlier bound, so
`plan_fees` demands the list. `rpc.fees.plan` reads it from the chain for you,
through `rpc.infused_assets(token_id, instance_id)`, and so does
`send_transaction`.

`burned_instances(msg)` names the NFT instances a message burns, in any shape.
It covers the native burn types, a `Token.BurnNonFungible` call, and every such
call inside a `CALL_MULTI`. An empty answer means no list is needed.

## The Pre-Flight Before A Token Creation

A token creation pays its base policy fee before the chain looks at the symbol, and
that fee is the largest single price in the protocol. `send_transaction`
therefore asks whether the symbol is taken, and refuses to send unless the chain
answered that it is free. It raises `PreflightError` otherwise.

`rpc.preflight_transaction(msg)` reports that verdict to a caller that wants to
decide for itself. The verdicts are `FREE`, `TAKEN`, `UNKNOWN` and
`NOT_APPLICABLE`. `UNKNOWN` means the lookup established nothing.

```python
from phantasma_py.rpc import SendTransactionOptions

tx_hash = rpc.send_transaction(msg, [keys], SendTransactionOptions(skip_preflight=True))
```

## Signing

| Call | What it does |
| ---- | ------------ |
| `sign_tx_msg(msg, *keys)` | Signs with in-memory key pairs. |
| `sign_and_serialize_tx_msg(msg, *keys)` | The same, and returns the envelope bytes. |
| `sign_and_serialize_tx_msg_hex(msg, *keys)` | The same as hex. |
| `sign_tx_msg_with(msg, *signers)` | Signs with any set of `TxSigner` witnesses, such as a hardware wallet. |
| `sign_and_serialize_tx_msg_with(msg, *signers)` | The same, and returns the envelope bytes. |

A gas-payer transfer takes the payer's and the owner's keys. The SDK puts them
in the order the chain reads.

A contract call chooses its own witness set, and each witness is 96 bytes the
chain bills, so those messages need `witness_count` in the plan options.
`send_transaction` and the `build_*_tx_and_sign` helpers fill it in from the
signers they are given.

## Expiry

A message keeps a default lifetime of `DEFAULT_TX_EXPIRY_MS`, which is 45,000
milliseconds. When a person sits between building and signing, set
`TxLimits.expiry` from the chain's own window:

```python
from phantasma_py.carbon import TxLimits, expiry_within

params = rpc.fees.chain_params()
limits = TxLimits(expiry=expiry_within(params.expiry_window_ms))
```

`expiry_within(expiry_window_ms, margin_ms=0)` returns the latest expiry the
chain will still admit, less a margin for clock skew. A margin of `0` means five
seconds.

## Signing Without A Chain

The `build_*_tx_and_sign` helpers plan the message against a `GasConfig` the
caller supplies:

```python
config = rpc.fees.config()
tx_hex = build_create_token_tx_and_sign_hex(token_info, keys, config)
```

Without a chain to plan against, state the offer yourself:

```python
from phantasma_py.carbon import TxLimits, build_transfer_fungible_tx, sign_and_serialize_tx_msg_hex

msg = build_transfer_fungible_tx(
    from_address=sender,
    to=receiver,
    token_id=1,
    amount=1_000_000,
    limits=TxLimits(max_gas=50_000_000),  # 0.005 KCAL
)
raw_hex = sign_and_serialize_tx_msg_hex(msg, keys)
```

A 170-byte KCAL transfer bills 0.00426 KCAL on mainnet, and the unused part of
the offer is refunded.

## Reading The Prices Directly

| Call | What it returns |
| ---- | --------------- |
| `rpc.get_gas_config()` | The on-chain gas configuration and the chain parameters. |
| `rpc.estimate_transaction(tx_data)` | A dry run of a serialized envelope against current chain state. |

`getGasConfig` changes only through a governance resolution, so its result is
safe to cache. `estimate_transaction` gives the exact bill of a script, which
the local planner can only budget. A node with the estimate service switched off answers a standard RPC error.

## Explicit Carbon Broadcast

```python
tx_hash = rpc.send_carbon_transaction(signed_tx_hex)
```

`send_carbon_transaction(...)` accepts signed Carbon bytes or hex. It returns
the transaction hash reported by the RPC endpoint.

## Confirmation And Result Parsing

Broadcasting only submits the transaction. Fetch the confirmed transaction and
then parse the result for the specific Carbon operation.

```python
from phantasma_py.carbon import parse_create_token_result

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
| Phantasma NFT mint | `parse_mint_phantasma_non_fungible_result(result_hex)` |

Do not parse one operation's result with another operation's parser.

## VM Broadcast

```python
tx_hash = rpc.send_raw_transaction(tx)
```

`send_raw_transaction(...)` accepts a `Transaction`, bytes, or hex. If you pass
a `Transaction`, it serializes the signed bytes.

## Errors

A node that refuses a request with an HTTP error and a JSON-RPC body surfaces
the body as an `RPCError` with the node's code and message, so the node's
refusal is told from a transport failure.

A transaction message that arrives truncated is refused rather than read as a
shorter message.

## Read Back After Broadcast

For token workflows, verify chain state after parsing the result:

```python
token = rpc.get_token("MYNFT", carbon_token_id=carbon_token_id)
series = rpc.get_token_series("MYNFT", carbon_token_id=carbon_token_id)
```

This catches a common integration mistake: a transaction can be submitted to one
endpoint while the application reads from a different network or a stale node.

## Safety Checklist

- Plan a message before signing it. A zero offer is never admitted.
- Read `plan.exact` before showing an amount to a person.
- Keep wallet WIF values out of the documentation, the logs and the repository.
- Check `tx.state_is_success` before parsing `tx.result`.
- Keep the token symbol and the Carbon token id together in application state.
- Keep the exact `TokenSchemas` used for deployment. Do not reconstruct a
  different schema before creating series or minting.
