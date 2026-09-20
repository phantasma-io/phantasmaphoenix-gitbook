# Go SDK NFT Minting

The chain derives the NFT id and stores a canonical ROM. One call mints one or
more instances.

| Path | Helper | Use it when |
| ---- | ------ | ----------- |
| Deterministic Phantasma NFT mint | `BuildMintPhantasmaNonFungibleSingleTx*` | One instance of one series. |
| Batch mint | `BuildMintPhantasmaNonFungibleTx*` | Several instances, which may come from several series. |

The SDK carries no builder for a direct `MintNonFungible`. The chain refuses
that operation where governance has not allowed caller-supplied ROM ids, and
that is the state of the public chains today.

## Build The Public ROM

`BuildPhantasmaNFTRom` serializes the public part of the ROM. The chain owns the
`_i` id for a deterministic mint, so the builder leaves it out.

Use the ROM schema the token was created with. The example continues from a
token created with `PrepareStandardTokenSchemas(false)`, which puts the standard
fields in the per-NFT ROM.

```go
schemas := carbon.PrepareStandardTokenSchemas(false)
publicRom, err := carbon.BuildPhantasmaNFTRom(schemas.ROM, []carbon.MetadataField{
    {Name: "name", Value: "NFT #1"},
    {Name: "description", Value: "Example mint"},
    {Name: "imageURL", Value: "https://example.com/nft.png"},
    {Name: "infoURL", Value: "https://example.com/nft"},
    {Name: "royalties", Value: int32(0)},
})
if err != nil {
    return err
}

receiver, err := carbon.Bytes32FromPhantasmaAddressText("P...")
if err != nil {
    return err
}
```

## Mint Through The Client

```go
msg, err := carbon.BuildMintPhantasmaNonFungibleSingleTx(
    carbonTokenID,
    big.NewInt(777), // the Phantasma series id used when the series was created
    sender,
    receiver,
    publicRom,
    nil, // RAM
    carbon.TxLimits{},
)
if err != nil {
    return err
}

hash, err := client.SendTransaction(ctx, msg, carbon.KeyPairSigners(keys), rpc.SendTransactionOptions{})
```

`SendTransaction` plans the fee from the message, signs it and broadcasts it.

## Mint Without A Client

The `...AndSign` helpers plan the message against a gas config the caller
supplies:

```go
gasConfig, err := client.GetGasConfig(ctx)
if err != nil {
    return err
}
config, err := gasConfig.ToGasConfig()
if err != nil {
    return err
}

txHex, err := carbon.BuildMintPhantasmaNonFungibleSingleTxAndSignHex(
    carbonTokenID,
    big.NewInt(777),
    keys,
    receiver,
    publicRom,
    nil, // RAM
    &config,
    carbon.PlanAndSignOptions{},
)
```

For batch mints, pass a slice of `carbon.PhantasmaNFTMintInfo` to
`BuildMintPhantasmaNonFungibleTx` or its signing variants.

A mint prices three facts the message does not carry: whether the recipient
already holds the token, whether the supply row still exists, and whether the
series mints duplicates. Each is taken at the reading that costs more. See
[Fees And Broadcasting](/developers/sdks/go/fees-and-broadcasting.md).

## Result Parsing

```go
tx, err := client.GetTransaction(ctx, hash)
if !tx.StateIsSuccess() {
    return fmt.Errorf("mint failed: %s", tx.State)
}

minted, err := carbon.ParseMintPhantasmaNonFungibleResult(tx.Result)
```

`ParseMintPhantasmaNonFungibleResult` returns the derived Phantasma NFT id and
the Carbon instance id for each minted item.
`ParseMintNonFungibleResult(carbonTokenID, resultHex)` parses a direct mint
result into Carbon NFT addresses, for chains where that operation is allowed.
