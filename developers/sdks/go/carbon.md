# Go SDK Carbon

`pkg/carbon` implements Phantasma Phoenix Carbon serialization, transaction
messages, signing helpers, token-module argument/result blobs, and schema-aware
metadata helpers.

## API Layers

| Layer | Main APIs | Use it for |
| ----- | --------- | ---------- |
| Lifecycle builders | `BuildCreateTokenTx`, `BuildCreateTokenSeriesTx`, `BuildMintPhantasmaNonFungibleTx`, signed and hex variants | Token deployment, series creation, and deterministic Phantasma NFT mints. |
| Native builders | `BuildTransferFungibleTx`, `BuildTransferNonFungibleTx`, `BuildMintFungibleTx`, `BuildBurnFungibleTx`, `BuildBurnNonFungibleTx` | Transfers, fungible mints and burns, which need no VM script. |
| Fee planning | `PlanFees`, `FeePlan`, `FeePlanOptions`, `SummarizeFeePlan`, `TxLimits`, `ExpiryWithin` | Pricing a message before it is signed. |
| Typed messages | `TxMsg`, `SignedTxMsg`, `Witness`, `TxMsg*`, module argument structs | Inspecting, assembling, signing, or serializing Carbon transactions directly. |
| Wire primitives | `Writer`, `Reader`, `Serialize`, `Deserialize`, fixed bytes, `IntX`, `SmallString` | Protocol tooling, tests, diagnostics, and custom Carbon messages. |

## Serialization

```go
w := carbon.NewWriter()
w.Write8U(42)

symbol, err := carbon.NewSmallString("SOUL")
if err != nil {
    return err
}
symbol.WriteCarbon(w)

bytes := w.Bytes()
r := carbon.NewReader(bytes)
value := r.Read8U()
fmt.Println(value)
```

Use `Serialize(blob)` and `Deserialize(data, blob)` when the object implements
the `carbon.Blob` interface. Use `Must...` variants only where invalid input is
a programmer error.

## Signing

```go
signed, err := carbon.SignTxMsg(tx, keys)
if err != nil {
    return err
}

hexTx, err := carbon.SignAndSerializeTxMsgHex(tx, keys)
```

`SignAndSerializeTxMsgHex` returns the form accepted by
`rpc.PhantasmaRPC.SendCarbonTransaction`.

## Lifecycle Builders

| Builder family | Purpose |
| -------------- | ------- |
| `BuildCreateTokenTx*` | Create a Carbon token definition. |
| `BuildCreateTokenSeriesTx*` | Create a series under an NFT token. |
| `BuildMintPhantasmaNonFungibleTx*` | Mint one or more deterministic Phantasma NFT instances. |
| `BuildMintPhantasmaNonFungibleSingleTx*` | Convenience wrapper for one deterministic Phantasma NFT. |

The builder forms return `TxMsg`. `AndSign` returns signed bytes. `AndSignHex`
returns signed hex.

## Result Parsers

Parse transaction results only after `GetTransaction` reports a successful
state:

| Operation | Parser |
| --------- | ------ |
| Create token | `ParseCreateTokenResult(resultHex)` |
| Create token series | `ParseCreateTokenSeriesResult(resultHex)` |
| Direct Carbon NFT mint | `ParseMintNonFungibleResult(carbonTokenID, resultHex)` |
| Phantasma NFT helper mint | `ParseMintPhantasmaNonFungibleResult(resultHex)` |
