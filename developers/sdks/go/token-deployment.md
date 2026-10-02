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

msg := carbon.BuildCreateTokenTx(tokenInfo, owner, carbon.TxLimits{})
```

The builder carries no prices, so the message leaves it with a zero gas offer.
`SendTransaction` plans the fee, checks the symbol, signs and broadcasts:

```go
hash, err := client.SendTransaction(ctx, msg, carbon.KeyPairSigners(keys), rpc.SendTransactionOptions{})
if err != nil {
    return err
}

tx, err := client.GetTransaction(ctx, hash)
if !tx.StateIsSuccess() {
    return fmt.Errorf("token deployment failed: %s", tx.State)
}

carbonTokenID, err := carbon.ParseCreateTokenResult(tx.Result)
```

{% hint style="warning" %}
A token creation pays its base policy fee before the chain looks at the symbol, and
that fee is the largest single price in the protocol. A symbol that is already
taken costs the fee and returns nothing. `SendTransaction` asks the chain first
and refuses to send when the symbol is taken, or when the lookup established
nothing. See [Fees And Broadcasting](/developers/sdks/go/fees-and-broadcasting.md).
{% endhint %}

To sign without a client, read the gas config first and use the
`Build...TxAndSignHex` helper:

```go
gasConfig, err := client.GetGasConfig(ctx)
if err != nil {
    return err
}
config, err := gasConfig.ToGasConfig()
if err != nil {
    return err
}

txHex, err := carbon.BuildCreateTokenTxAndSignHex(tokenInfo, keys, &config, carbon.PlanAndSignOptions{})
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
