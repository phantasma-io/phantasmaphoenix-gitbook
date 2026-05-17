# Go SDK VM And Transactions

The Go SDK separates VM script construction from transaction construction.
Build the script with `pkg/vm/script_builder`, wrap it in a
`pkg/blockchain.Transaction`, sign it with `pkg/cryptography`, then broadcast
the serialized bytes through `pkg/rpc`.

## Script Builder

```go
sender := cryptography.MustAddressFromString("P...")
receiver := cryptography.MustAddressFromString("P...")

script := scriptbuilder.BeginScript().
    AllowGas(sender, cryptography.NullAddress(), big.NewInt(100000), big.NewInt(21000)).
    TransferTokens("SOUL", sender, receiver, big.NewInt(100000000)).
    SpendGas(sender).
    EndScript()
```

Use `EndScriptWithError` or `ToScript` in validation-heavy tools. `EndScript`
panics when the builder has accumulated an error.

## Address Arguments

High-level helpers such as `AllowGas`, `SpendGas`, `TransferTokens`, `Stake`,
and `Unstake` take `cryptography.Address` values. `AllowGasText`,
`TransferTokensText`, and similar `*Text` helpers parse address text before
emitting VM address bytes.

Raw `string` arguments passed to `CallContract` or `CallInterop` are emitted as
VM strings. Do not pass address text directly to those generic methods when the
ABI expects an address value.

## Build And Sign A VM Transaction

```go
tx := blockchain.NewTransaction(
    "testnet",
    "main",
    script,
    uint32(time.Now().UTC().Add(20*time.Minute).Unix()),
    []byte("GO-SDK"),
)

if err := tx.Sign(keys); err != nil {
    return err
}

txHash, err := client.SendRawTransaction(ctx, hex.EncodeToString(tx.Bytes()))
```

For trusted local signing flows, the RPC client also exposes:

| Helper | Use it for |
| ------ | ---------- |
| `SignAndSendTransaction` | Build, sign, and broadcast a classic VM transaction with default expiration. |
| `SignAndSendTransactionWithExpiration` | Same flow with explicit expiration. |
| `SignAndSendTransactionTextPayload` | Same flow with UTF-8 payload text. |
| `SignAndSendBuiltTransaction` | Sign and broadcast an already-built `blockchain.Transaction`. |

## Transaction State

After broadcast, fetch the transaction and use the SDK state helpers:

```go
final, err := client.GetTransaction(ctx, txHash)
if err != nil {
    return err
}
if final.StateIsFault() {
    return fmt.Errorf("transaction failed: %s", final.State)
}
```
