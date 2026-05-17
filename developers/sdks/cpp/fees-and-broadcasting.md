# C++ SDK Fees And Broadcasting

The C++ SDK can build and sign classic VM transactions and Carbon transactions.
The caller chooses the network, endpoint, key source, retry behavior, and
confirmation policy.

## Carbon Fee Options

| Type | Used by | Default behavior |
| ---- | ------- | ---------------- |
| `FeeOptions` | generic Carbon messages and base mint policy | `CalculateMaxGas()` for one item or `CalculateMaxGas(count)` for count-sensitive flows |
| `CreateTokenFeeOptions` | `CreateTokenTxHelper` | includes create-token base and symbol-length estimate |
| `CreateSeriesFeeOptions` | `CreateTokenSeriesTxHelper` | includes create-series base estimate |
| `MintNftFeeOptions` | NFT mint helpers | scales by count for deterministic Phantasma NFT batches |

`CalculateMaxGas(count)` rejects zero counts and reports overflow through the
SDK exception mechanism configured by `PHANTASMA_EXCEPTION`.

## Defaults

| Helper | Default gas behavior |
| ------ | -------------------- |
| `CreateTokenTxHelper::BuildTx` | Uses `CreateTokenFeeOptions::CalculateMaxGas(tokenInfo.symbol)`. |
| `CreateTokenSeriesTxHelper::BuildTx` | Uses `CreateSeriesFeeOptions::CalculateMaxGas()`. |
| `MintNonFungibleTxHelper::BuildTx` | Uses `MintNftFeeOptions::CalculateMaxGas(1)`. |
| `MintPhantasmaNonFungibleTxHelper::BuildTx` | Uses `MintNftFeeOptions::CalculateMaxGas(numTokens)`. |

When `expiry` is `0`, Carbon helpers use `GetDefaultExpiry()`, which is current
Unix milliseconds plus 60 seconds.

## Broadcast And Confirmation

Serialize a signed Carbon envelope, hex-encode the bytes for the RPC endpoint,
then call `SendCarbonTransaction`. After broadcast, fetch the transaction and
parse the result with the matching helper only if the transaction state is
successful.

For classic VM transactions, sign `Transaction`, serialize with signatures, and
broadcast with `SendRawTransaction`.
