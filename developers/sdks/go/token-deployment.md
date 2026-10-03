# Go SDK Token Deployment

A token is created by one structured transaction that calls
`Token.CreateToken`. An NFT token then needs at least one series before
anything can be minted, and each series is one more transaction. The builders
live in `github.com/phantasma-io/phantasma-sdk-go/pkg/carbon`.

## What The Chain Checks And Charges

| Rule | Detail |
| ---- | ------ |
| Symbol | Uppercase letters `A` to `Z` only, at most 255 characters, not used by another token. `BuildTokenInfo` applies the same rule through `CheckTokenSymbol`. |
| Metadata | `name`, `icon`, `url` and `description` are required, and `icon` is a base64 data URI of a PNG, JPEG or WebP image. `BuildTokenMetadata` checks both. |
| Owner | The owner signs the creation and becomes the token owner. A new series needs the token owner's signature. A mint needs the signature of the series owner, `SeriesInfo.Owner`. |
| Fungible token | `decimals` up to 64, no schemas. |
| NFT token | `decimals` is `0`, and the schemas are required; `BuildTokenInfo` returns an error without them. |
| Supply | `maxSupply` `0` means no limit. `BuildTokenInfo` then marks a fungible token as big-fungible, because the chain refuses an unlimited token with 64-bit balances; it does the same for a supply beyond the `int64` range. An NFT supply must fit an `int64`. |

A token creation pays two policy fees from the gas config:
`policyFeeCreateTokenBase`, and `policyFeeCreateTokenSymbol` halved once for
every letter after the first, so short symbols cost more. A series pays
`policyFeeCreateTokenSeries`. Read the current values with `GetGasConfig`. The
chain takes the base fee before it checks the symbol, so a taken symbol costs
the base fee and creates nothing. `SendTransaction` asks the chain first and
refuses a taken symbol; see
[The Pre-Flight Before A Token Creation](/developers/sdks/go/fees-and-broadcasting.md#the-pre-flight-before-a-token-creation).

## Create A Fungible Token

```go
owner, err := carbon.Bytes32FromPublicKey(keys.PublicKey())
if err != nil {
    return err
}

metadata, err := carbon.BuildTokenMetadata(map[string]string{
    "name":        "Example Coin",
    "icon":        "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mNkYAAAAAYAAjCB0C8AAAAASUVORK5CYII=",
    "url":         "https://example.invalid",
    "description": "A fungible example token",
})
if err != nil {
    return err
}

// 1,000,000 whole units with 8 decimals, so 10^14 atoms at most.
info, err := carbon.BuildTokenInfo("EXCOIN", carbon.IntXFromInt64(100_000_000_000_000), false, 8, owner, metadata, nil)
if err != nil {
    return err
}

hash, err := client.SendTransaction(ctx, carbon.BuildCreateTokenTx(info, owner, carbon.TxLimits{}), carbon.KeyPairSigners(keys), rpc.SendTransactionOptions{})
if err != nil {
    return err
}

tx, err := waitForTransaction(ctx, client, hash)
if err != nil {
    return err
}
if !tx.StateIsSuccess() {
    return fmt.Errorf("token creation failed: %s", tx.State)
}
tokenID, err := carbon.ParseCreateTokenResult(tx.Result)
```

`SendTransaction` plans the fee from the message, runs the symbol check, signs
and sends. `waitForTransaction` is the polling function from
[VM And Transactions](/developers/sdks/go/vm-and-transactions.md#the-result-of-a-transaction).
The owner mints the supply afterwards with `BuildMintFungibleTx`; see
[Carbon](/developers/sdks/go/carbon.md#native-builders).

## Create An NFT Token And A Series

An NFT token carries three schemas: one for the series metadata, one for the
read-only part of each NFT (ROM) and one for its mutable part (RAM).
`PrepareStandardTokenSchemas(false)` returns the standard set with the NFT
fields in each NFT; [Schemas And Metadata](/developers/sdks/go/schemas-and-metadata.md)
explains the choices.

```go
package main

import (
    "context"
    "fmt"
    "log"
    "math/big"
    "os"
    "time"

    "github.com/phantasma-io/phantasma-sdk-go/pkg/carbon"
    "github.com/phantasma-io/phantasma-sdk-go/pkg/cryptography"
    "github.com/phantasma-io/phantasma-sdk-go/pkg/rpc"
    "github.com/phantasma-io/phantasma-sdk-go/pkg/rpc/response"
)

func main() {
    ctx, cancel := context.WithTimeout(context.Background(), 2*time.Minute)
    defer cancel()

    keys, err := cryptography.FromWIF(os.Getenv("WIF"))
    if err != nil {
        log.Fatal(err)
    }
    owner, err := carbon.Bytes32FromPublicKey(keys.PublicKey())
    if err != nil {
        log.Fatal(err)
    }
    client := rpc.NewRPCTestnet()

    schemas := carbon.PrepareStandardTokenSchemas(false)
    metadata, err := carbon.BuildTokenMetadata(map[string]string{
        "name":        "Example Art",
        "icon":        "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mNkYAAAAAYAAjCB0C8AAAAASUVORK5CYII=",
        "url":         "https://example.invalid/art",
        "description": "An example NFT collection",
    })
    if err != nil {
        log.Fatal(err)
    }
    info, err := carbon.BuildTokenInfo("EXART", carbon.IntXFromInt64(0), true, 0, owner, metadata, carbon.SerializeTokenSchemas(schemas))
    if err != nil {
        log.Fatal(err)
    }

    tokenTx, err := send(ctx, client, keys, carbon.BuildCreateTokenTx(info, owner, carbon.TxLimits{}))
    if err != nil {
        log.Fatal(err)
    }
    tokenID, err := carbon.ParseCreateTokenResult(tokenTx.Result)
    if err != nil {
        log.Fatal(err)
    }

    // A series with its own id, no mint limit and no supply limit. The key's account owns it.
    seriesID := big.NewInt(1)
    series, err := carbon.BuildSeriesInfo(seriesID, 0, 0, owner)
    if err != nil {
        log.Fatal(err)
    }
    seriesTx, err := send(ctx, client, keys, carbon.BuildCreateTokenSeriesTx(tokenID, series, owner, carbon.TxLimits{}))
    if err != nil {
        log.Fatal(err)
    }
    carbonSeriesID, err := carbon.ParseCreateTokenSeriesResult(seriesTx.Result)
    if err != nil {
        log.Fatal(err)
    }

    fmt.Println("token id", tokenID, "series id", seriesID, "Carbon series id", carbonSeriesID)
}

// send plans, signs and sends a message, then waits until it is in a block and succeeded.
func send(ctx context.Context, client rpc.PhantasmaRPC, keys cryptography.KeyPair, msg carbon.TxMsg) (response.TransactionResult, error) {
    hash, err := client.SendTransaction(ctx, msg, carbon.KeyPairSigners(keys), rpc.SendTransactionOptions{})
    if err != nil {
        return response.TransactionResult{}, err
    }
    for {
        tx, err := client.GetTransaction(ctx, hash)
        if err == nil && tx.StateIsSuccess() {
            return tx, nil
        }
        if err == nil && tx.StateIsFault() {
            return tx, fmt.Errorf("transaction %s failed: %s", hash, tx.State)
        }
        select {
        case <-ctx.Done():
            return response.TransactionResult{}, ctx.Err()
        case <-time.After(time.Second):
        }
    }
}
```

A series has two ids. `seriesID` is the id the application chooses, any number
that fits 256 bits and is unique within the token; mints name the series by it.
`carbonSeriesID` is the 32-bit id the chain assigns; RPC methods such as
`GetTokenNFTs` take it.

`maxMint` caps how many instances the series can ever mint; burns do not lower
that count. `maxSupply` caps how many exist at once; burns lower it. `0` means
no limit for either.

`BuildSeriesInfo` writes series metadata for the per-NFT standard schemas. A
token created with `PrepareStandardTokenSchemas(true)` keeps the NFT fields in
the series, so its series metadata is built from its own schema with
`BuildTokenSeriesMetadata`; see
[Series Metadata](/developers/sdks/go/schemas-and-metadata.md#series-metadata).

## Sign Without Sending

Each token module builder has a form that builds, plans and signs in one call
against a gas config the caller provides, for a process that signs offline:

```go
gasConfig, err := client.GetGasConfig(ctx)
if err != nil {
    return err
}
config, err := gasConfig.ToGasConfig()
if err != nil {
    return err
}

signedTxHex, err := carbon.BuildCreateTokenTxAndSignHex(tokenInfo, keys, &config, carbon.PlanAndSignOptions{})
```

`BuildCreateTokenSeriesTxAndSignHex` and
`BuildMintPhantasmaNonFungibleTxAndSignHex` work the same way.
`client.SendCarbonTransaction(ctx, signedTxHex)` sends the result later. This
path does not run the symbol check, and the expiry runs from the moment of
signing: 45 seconds unless `PlanAndSignOptions.TxLimits.Expiry` says otherwise.

## Read The Token Back

```go
token, err := client.GetToken(ctx, "EXART", false)
if err != nil {
    return err
}
fmt.Println(token.Symbol, "token id", token.CarbonID)

page, err := client.GetTokenSeries(ctx, "EXART", 0, 10, "")
if err != nil {
    return err
}
for _, s := range page.Result {
    fmt.Println("series", s.SeriesID, "Carbon series id", s.CarbonSeriesID, "minted", s.MintCount)
}
```

`GetTokenSeries` returns the series page by page. Pass `*page.Cursor` back to
read the next page, until the cursor is `nil` or empty. `GetTokenSeriesByID`
returns one series by its id or its Carbon series id.

## Related Pages

{% content-ref url="/developers/sdks/go/nft-minting.md" %}
[NFT Minting](/developers/sdks/go/nft-minting.md)
{% endcontent-ref %}

{% content-ref url="/developers/sdks/go/schemas-and-metadata.md" %}
[Schemas And Metadata](/developers/sdks/go/schemas-and-metadata.md)
{% endcontent-ref %}

{% content-ref url="/developers/sdks/go/fees-and-broadcasting.md" %}
[Fees And Broadcasting](/developers/sdks/go/fees-and-broadcasting.md)
{% endcontent-ref %}
