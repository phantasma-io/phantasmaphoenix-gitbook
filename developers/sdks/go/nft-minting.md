# Go SDK NFT Minting

The Go SDK exposes two Carbon NFT minting paths:

| Path | Helper | Use it when |
| ---- | ------ | ----------- |
| Direct Carbon NFT mint | `BuildMintNonFungibleTx*` | The token uses a Carbon series id and caller-provided ROM/RAM bytes. |
| Deterministic Phantasma NFT mint | `BuildMintPhantasmaNonFungibleTx*` or `BuildMintPhantasmaNonFungibleSingleTx*` | The caller provides public ROM fields and the chain assigns deterministic Phantasma NFT ids. |

## Direct Carbon NFT Mint

```go
schemas := carbon.PrepareStandardTokenSchemas(false)
rom, err := carbon.BuildNFTRom(schemas.ROM, big.NewInt(1), []carbon.MetadataField{
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

txHex, err := carbon.BuildMintNonFungibleTxAndSignHex(
    carbonTokenID,
    carbonSeriesID,
    keys,
    receiver,
    rom,
    nil,
    carbon.DefaultMintNFTFeeOptions(),
    100_000_000,
    time.Now().UTC().Add(20*time.Minute).UnixMilli(),
)
```

`BuildMintNonFungibleTx*` mints one NFT and uses one-item mint gas.

## Deterministic Phantasma NFT Mint

```go
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

txHex, err := carbon.BuildMintPhantasmaNonFungibleSingleTxAndSignHex(
    carbonTokenID,
    big.NewInt(777),
    keys,
    receiver,
    publicRom,
    nil,
    carbon.DefaultMintNFTFeeOptions(),
    100_000_000,
    time.Now().UTC().Add(20*time.Minute).UnixMilli(),
)
```

For batch mints, pass a slice of `carbon.PhantasmaNFTMintInfo` to
`BuildMintPhantasmaNonFungibleTx*`. The helper scales the maximum gas by the
number of token records.

## Result Parsing

```go
tx, err := client.GetTransaction(ctx, hash)
if !tx.StateIsSuccess() {
    return fmt.Errorf("mint failed: %s", tx.State)
}

addresses, err := carbon.ParseMintNonFungibleResult(carbonTokenID, tx.Result)
```

Use `ParseMintPhantasmaNonFungibleResult` for the deterministic Phantasma NFT
helper. It returns the derived Phantasma NFT id and Carbon instance id for each
minted item.
