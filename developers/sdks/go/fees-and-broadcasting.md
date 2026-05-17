# Go SDK Fees And Broadcasting

The Go SDK can build and sign VM transactions and Carbon transactions. The SDK
does not choose networks, retry policies, or confirmation policies for the
caller.

## Transaction Families

| Family | Build with | Broadcast with | Result handling |
| ------ | ---------- | -------------- | --------------- |
| VM script transaction | `script_builder` + `blockchain.Transaction` | `PhantasmaRPC.SendRawTransaction` or signing helpers | `GetTransaction`, `TransactionResult.StateIsSuccess()` |
| Carbon transaction | `carbon.TxMsg` / lifecycle helpers | `PhantasmaRPC.SendCarbonTransaction` or `SignAndSendCarbonTransaction` | `GetTransaction`, Carbon result parser helpers |

## Carbon Fee Options

| Type | Used by | Default behavior |
| ---- | ------- | ---------------- |
| `FeeOptions` | generic Carbon messages and NFT mint helpers | `CalculateMaxGas()` for one item or `CalculateMaxGasForCount(count)` where exposed by the concrete type |
| `CreateTokenFeeOptions` | `BuildCreateTokenTx*` | includes create-token base and symbol-length fee estimate |
| `CreateSeriesFeeOptions` | `BuildCreateTokenSeriesTx*` | includes create-series base estimate |
| `MintNFTFeeOptions` | NFT mint helpers | `CalculateMaxGasForCount(count)` scales mint gas by a positive count |

```go
fees := carbon.DefaultCreateTokenFeeOptions()
symbol, err := carbon.NewSmallString("MYNFT")
if err != nil {
    return err
}
maxGas := fees.CalculateMaxGas(symbol)
fmt.Println(maxGas)
```

Direct NFT mint helpers use one-item mint gas. Phantasma NFT batch helpers pass
the token count to the mint fee calculation.

## `maxData` And Expiry

High-level Carbon builders accept `maxData` and `expiry` arguments. Use
`100_000_000` as the normal data cap unless the application has measured its
storage needs. Pass an explicit expiry in Unix milliseconds for queued signing
or batching flows.

The source helper `NowUnixMillis()` is available for caller-side expiry
calculation.

## Broadcast And Confirmation

```go
hash, err := client.SendCarbonTransaction(ctx, signedTxHex)
if err != nil {
    return err
}

tx, err := client.GetTransaction(ctx, hash)
if err != nil {
    return err
}
if !tx.StateIsSuccess() {
    return fmt.Errorf("transaction failed: %s", tx.State)
}
```

Broadcast methods return the transaction hash reported by the endpoint. They do
not wait for final execution or parse Carbon results.
