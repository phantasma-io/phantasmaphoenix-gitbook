# Go SDK Token Deployment

Use `pkg/carbon` when creating native Carbon tokens. A token deployment flow
builds metadata, token schemas for NFTs, a `TokenInfo`, then a signed
create-token transaction.

## NFT Token Flow

```go
schemas := carbon.PrepareStandardTokenSchemas(true)

metadata, err := carbon.BuildTokenMetadata(map[string]string{
    "name":        "Example NFT",
    "icon":        "data:image/png;base64,iVBORw0KGgo=",
    "url":         "https://example.com",
    "description": "Example Carbon NFT token",
})
if err != nil {
    return err
}

owner, err := carbon.Bytes32FromPublicKey(keys.PublicKey())
if err != nil {
    return err
}

tokenInfo, err := carbon.BuildTokenInfo(
    "MYNFT",
    carbon.NewIntX(big.NewInt(0)),
    true,
    0,
    owner,
    metadata,
    carbon.SerializeTokenSchemas(schemas),
)
if err != nil {
    return err
}

txHex, err := carbon.BuildCreateTokenTxAndSignHex(
    tokenInfo,
    keys,
    carbon.DefaultCreateTokenFeeOptions(),
    100_000_000,
    time.Now().UTC().Add(20*time.Minute).UnixMilli(),
)
```

Broadcast the signed hex with `SendCarbonTransaction`, then poll the transaction
and parse the created Carbon token id:

```go
hash, err := client.SendCarbonTransaction(ctx, txHex)
tx, err := client.GetTransaction(ctx, hash)
if !tx.StateIsSuccess() {
    return fmt.Errorf("token deployment failed: %s", tx.State)
}

carbonTokenID, err := carbon.ParseCreateTokenResult(tx.Result)
```

Keep the token symbol and Carbon token id together in application state. Later
RPC calls can use both values to disambiguate current Carbon token reads.

## Required Metadata

`BuildTokenMetadata` requires non-empty `name`, `icon`, `url`, and
`description`. `icon` must be a PNG, JPEG, or WebP data URI with valid base64
payload.

## Symbol Rules

`BuildTokenInfo` validates token symbols through `CheckTokenSymbol`: symbols
must be non-empty uppercase ASCII letters.
