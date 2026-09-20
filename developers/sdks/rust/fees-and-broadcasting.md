# Rust SDK Fees And Broadcasting

A Carbon transaction is built, planned, signed and sent as four separate steps.
The same message works whether the key sits in memory, in a hardware wallet, or
in a wallet reached over Phantasma Link.

Builders carry no prices. A message built without a `max_gas` has a zero gas
offer, and that marks it as not yet planned. Signing such a message is refused,
because the chain never admits an offer of zero.

## Two Transaction Families

| Family | Build with | Broadcast with | Result handling |
| ------ | ---------- | -------------- | --------------- |
| VM script transaction | `ScriptBuilder` + `Transaction` | `PhantasmaRpc::send_raw_transaction(...)` or `send_transaction(...)` | `get_transaction(...)`, `TransactionResult::state_is_success()` |
| Carbon transaction | the Carbon builders | `PhantasmaRpc::send_tx_msg(...)`, `send_carbon_transaction(...)` or `send_signed_tx_msg(...)` | `get_transaction(...)`, the Carbon result parsers |

VM transactions use nexus and chain names and a VM script. Carbon transactions
use the `TxMsg` fields `expiry`, `max_gas`, `max_data`, `gas_from` and a typed
payload.

## The Four Steps

```rust
use phantasma_sdk::{
    build_transfer_fungible_tx, bytes32_from_public_key, summarize_fee_plan, PhantasmaKeys,
    PhantasmaRpc, PlanRequestOptions, Result, SendTransactionOptions, TransferFungibleParams,
    TxSigner,
};

async fn send_kcal(client: &PhantasmaRpc, keys: &PhantasmaKeys, receiver: [u8; 32]) -> Result<String> {
    // 1. Build the message.
    let msg = build_transfer_fungible_tx(TransferFungibleParams {
        from: bytes32_from_public_key(&keys.public_key())?,
        to: receiver.into(),
        token_id: 1, // KCAL
        amount: 100_000_000,
        ..TransferFungibleParams::default()
    });

    // 2. Plan it against the chain.
    let plan = client.fees().plan(&msg, &PlanRequestOptions::default()).await?;
    let summary = summarize_fee_plan(&plan);
    println!("gas {} KCAL, storage deposit up to {} SOUL", summary.gas_bill, summary.storage_ceiling);

    // 3 and 4. Sign and send.
    let signers: [&dyn TxSigner; 1] = [keys];
    client.send_tx_msg(&msg, &signers, &SendTransactionOptions::default()).await
}
```

`send_tx_msg` runs steps 2 to 4 in one call, plus the pre-flight. A message
whose `max_gas` is still zero is planned. A message the caller already planned
is sent as it is.

## What The Chain Bills

The chain charges for every byte the transaction puts in the block. It also
escrows every storage row the transaction creates. A message therefore carries
two ceilings, and both have to be set before it is signed:

| Field | Meaning |
| ----- | ------- |
| `TxMsg::max_gas` | The gas offer, in KCAL atoms. Unused gas is refunded. A short offer is rejected. |
| `TxMsg::max_data` | The storage escrow ceiling, in SOUL atoms. It prices every new row at the current row price. |

## The Fee Planner

`client.fees()` returns the `FeePlanner` of the chain this client talks to. It
reads `getGasConfig` through the client and keeps the answer for a minute.

| Member | What it does |
| ------ | ------------ |
| `plan(&msg, &options)` | Prices one message and returns a `FeePlan`. |
| `config(refresh)` | Returns the cached `GasConfig`. |
| `chain_params(refresh)` | Returns `expiry_window`, `block_rate_target` and `gas_model_version`. |
| `plan_with(&config, &msg, &options)` | Prices a message against a config the caller already holds. It touches no network. |
| `invalidate()` | Drops the cached config, so the next call reads it again. |

`plan_fees(&msg, &config, &options)` is the same calculation as a plain
function. Use it when the config is already in hand and no client is available.

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
| `apply(&msg)` | Returns a copy of the message with `max_gas` and `max_data` set. |

`summarize_fee_plan(&plan)` renders the amounts in KCAL and SOUL through
`gas_bill`, `gas_offer` and `storage_ceiling`.
`summarize_fee_plan_with_decimals` takes the decimals explicitly.

### A Prediction Or A Ceiling

Part of the price depends on chain state that the message does not carry. One
example is whether the recipient already holds the token. Every such fact is
taken at the reading that costs more.

`plan.exact` reports the result. It is `true` when nothing the plan had to
assume could have changed the number. It is `false` when a costlier reading
decided part of the price, or when part of the message had to be budgeted. A
wallet shows the amount when the flag is `true`, and "up to" in front of the
amount when it is `false`.

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
| `infusions` | What the burned NFTs hold. `None` is unstated. An empty vector states that they hold nothing. |
| `script_units_allowance`, `script_event_bytes`, `script_storage_quanta` | The allowance for a VM script. |
| `witness_count` | How many witnesses will sign a `Call`, `CallMulti`, `Trade` or `Phantasma` message. |

### Which Operation Reads Which Fact

| `NativeFeeKind` | Facts it reads |
| --------------- | -------------- |
| `TransferFungible` | `recipient_holds_token` |
| `TransferNonFungible` | `recipient_holds_token` |
| `MintFungible` | `recipient_holds_token`, `supply_row_exists`, `big_fungible` |
| `MintNonFungible` | `recipient_holds_token`, `supply_row_exists`, `rom_has_meta_id` |
| `MintPhantasmaNonFungible` | `recipient_holds_token`, `supply_row_exists`, `duplicated_series` |
| `BurnFungible` | `token_burned_before`, `supply_row_exists`, `big_fungible` |
| `BurnNonFungible` | `token_burned_before`, `supply_row_exists`, and `infusions`, which is required |
| `CreateToken` | none |
| `CreateTokenSeries` | `series_has_meta_id` |
| `RegisterName` | none |
| `Script` | none |

Balance rows of the gas and data tokens are free, so `recipient_holds_token`
cannot move the price of a KCAL or SOUL transfer.

`NativeFeeKind::Script` covers VM scripts and calls the SDK does not model.
Their work depends on execution, so they are budgeted and never predicted.
`plan.exact` is `false` whenever one is present.

A `CallMulti` performs several operations. Each one is priced and then summed,
because the chain bills a batch as the sum of its calls with the envelope
counted once.

## Burning An NFT

A burn returns whatever the NFT holds at its own address, and the chain charges
for each returned asset. That set is chain state with no costlier bound, so
`plan_fees` demands the list. `client.fees().plan` reads it from the chain for
you, through `client.infused_assets(token_id, instance_id)`, and so does
`send_tx_msg`.

`burned_instances(&msg)` names the NFT instances a message burns, in any shape.
It covers the native burn types, a `Token.BurnNonFungible` call, and every such
call inside a `CallMulti`. An empty answer means no list is needed.

## The Pre-Flight Before A Token Creation

A token creation pays its policy fee before the chain looks at the symbol, and
that fee is the largest single price in the protocol. `send_tx_msg` therefore
asks whether the symbol is taken, and refuses to send unless the chain answered
that it is free.

`client.preflight_transaction(&msg)` reports that verdict to a caller that wants
to decide for itself. Set `SendTransactionOptions::skip_preflight` to send
without the lookup.

## Signing

| Call | What it does |
| ---- | ------------ |
| `sign_tx_msg_with_keys(&msg, &[&keys])` | Signs with in-memory key pairs. |
| `sign_tx_msg_with(&msg, &signers)` | Signs with any set of `TxSigner` witnesses, such as a hardware wallet. |
| `sign_and_serialize_tx_msg_hex(&msg, &keys)` | Signs with one key pair and returns the envelope hex. |

A gas-payer transfer takes the payer's and the owner's keys. The SDK puts them
in the order the chain reads.

A contract call chooses its own witness set, and each witness is 96 bytes the
chain bills, so those messages need `witness_count` in the plan options.
`send_tx_msg` and the `build_*_tx_and_sign` helpers fill it in from the signers
they are given.

## Expiry

A message keeps a default lifetime of `DEFAULT_TX_EXPIRY`, which is 45 seconds.
When a person sits between building and signing, set `TxLimits::expiry` from the
chain's own window:

```rust
use std::time::Duration;
use phantasma_sdk::expiry_within;

let params = client.fees().chain_params(false).await?;
let expiry = expiry_within(params.expiry_window, Duration::ZERO)?;
```

A margin of `Duration::ZERO` means five seconds of headroom for clock skew.

## Reading The Prices Directly

| Call | What it returns |
| ---- | --------------- |
| `client.get_gas_config()` | The on-chain gas configuration and the chain parameters. |
| `client.estimate_transaction(tx_data)` | A dry run of a serialized envelope against current chain state. |

`getGasConfig` changes only through a governance resolution, so its result is
safe to cache. `estimate_transaction` gives the exact bill of a script, which
the local planner can only budget. It returns a standard RPC error until the
estimate service is launched.

## Explicit Carbon Broadcast

```rust
use phantasma_sdk::{PhantasmaRpc, Result};

#[tokio::main]
async fn main() -> Result<()> {
    let rpc = PhantasmaRpc::new("https://testnet.phantasma.info/rpc");
    let tx_hash = rpc.send_carbon_transaction(&signed_tx_bytes).await?;

    println!("{tx_hash}");
    Ok(())
}
```

`send_carbon_transaction(...)` accepts signed Carbon bytes. Use
`send_signed_tx_msg(...)` when you already have a decoded `SignedTxMsg`.

## Confirmation And Result Parsing

Broadcasting only submits the transaction. Fetch the confirmed transaction and
then parse the result for the specific Carbon operation.

```rust
use phantasma_sdk::{parse_create_token_result, PhantasmaRpc, Result};

#[tokio::main]
async fn main() -> Result<()> {
    let rpc = PhantasmaRpc::new("https://testnet.phantasma.info/rpc");

    let tx_hash = rpc.send_carbon_transaction(&signed_create_token_bytes).await?;
    let tx = rpc.get_transaction(&tx_hash).await?;

    if !tx.state_is_success() {
        eprintln!("transaction failed: {}", tx.state);
        return Ok(());
    }

    let carbon_token_id = parse_create_token_result(&tx.result)?;
    println!("{carbon_token_id}");

    Ok(())
}
```

Use the parser that matches the operation:

| Operation | Parser |
| --------- | ------ |
| Create token | `parse_create_token_result(result_hex)` |
| Create token series | `parse_create_token_series_result(result_hex)` |
| Phantasma NFT mint | `parse_mint_phantasma_non_fungible_result(result_hex)` |

Do not parse one operation's result with another operation's parser.

## VM Broadcast

```rust
let tx_hash = rpc.send_transaction(&tx).await?;
```

`send_transaction(...)` serializes a signed `Transaction`. Use
`send_raw_transaction(...)` when you already have signed VM transaction hex.

## Combined Sign And Send Helpers

`PhantasmaRpc` also exposes helpers that combine local signing and broadcast:

| Helper | Family |
| ------ | ------ |
| `send_tx_msg(...)` | Carbon message, with plan, pre-flight, signatures and broadcast in one step |
| `sign_and_send_transaction(...)` | VM script transaction |
| `sign_and_send_built_transaction(...)` | An existing signed VM `Transaction` |

These are convenience methods for applications that already own the key and
endpoint selection. They are not wallet prompts and they do not add user
confirmation.

## Errors

A node that refuses a request with an HTTP error and a JSON-RPC body surfaces
the body as `PhantasmaError::Rpc` with the node's code and message, so a match
on the error tells the node's refusal from a transport failure.

A transaction message that arrives truncated is refused rather than read as a
shorter message.

## Read Back After Broadcast

For token workflows, always verify chain state after parsing the result:

```rust
let token = rpc.get_token_with_id("MYNFT", true, carbon_token_id).await?;
let series = rpc.get_token_series("MYNFT", carbon_token_id, 20, "").await?;
```

For NFT mints, read by token id, series cursor, account cursor, or NFT id:

```rust
let nfts = rpc
    .get_token_nfts(carbon_token_id, 0, 20, "", true, "")
    .await?;
let owned = rpc
    .get_account_nfts(address_text, "MYNFT", carbon_token_id, 0, 20, "", true, false)
    .await?;
```

This catches a common integration mistake: a transaction can be submitted to an
endpoint, but the app may be reading from a different network or a stale RPC
node.

## Safety Checklist

- Plan a message before signing it. A zero offer is never admitted.
- Read `plan.exact` before showing an amount to a person.
- Use mainnet, testnet, and devnet endpoints intentionally.
- Keep wallet WIF values outside docs, logs, and Git.
- Check `tx.state_is_success()` before parsing `tx.result`.
- Keep the token symbol and Carbon token id together in application state.
- Keep the exact `TokenSchemas` used for deployment; do not reconstruct a
different schema before creating series or minting.
- Treat examples as local builder examples unless they explicitly say they were
  run against a funded live endpoint.
