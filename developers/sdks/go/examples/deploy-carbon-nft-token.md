# Go SDK Example: Deploy Carbon NFT Token

This example signs a create-token transaction and shows the confirmation parser.
Broadcast requires a funded key and a network endpoint.

```go
package main

import (
    "context"
    "fmt"
    "log"
    "math/big"
    "time"

    "github.com/phantasma-io/phantasma-sdk-go/pkg/carbon"
    "github.com/phantasma-io/phantasma-sdk-go/pkg/cryptography"
    "github.com/phantasma-io/phantasma-sdk-go/pkg/rpc"
)

func main() {
    ctx, cancel := context.WithTimeout(context.Background(), 30*time.Second)
    defer cancel()

    keys, err := cryptography.FromWIF("YOUR_WIF")
    if err != nil {
        log.Fatal(err)
    }

    owner, err := carbon.Bytes32FromPublicKey(keys.PublicKey())
    if err != nil {
        log.Fatal(err)
    }

    schemas := carbon.PrepareStandardTokenSchemas(true)
    metadata, err := carbon.BuildTokenMetadata(map[string]string{
        "name":        "My NFT",
        "icon":        "data:image/png;base64,iVBORw0KGgo=",
        "url":         "https://example.com",
        "description": "My Carbon NFT token",
    })
    if err != nil {
        log.Fatal(err)
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
        log.Fatal(err)
    }

    // The builder carries no prices. The message leaves it with a zero gas offer.
    msg := carbon.BuildCreateTokenTx(tokenInfo, owner, carbon.TxLimits{})

    client := rpc.NewRPCTestnet()

    // Plans the fee, checks that the symbol is free, signs and broadcasts.
    hash, err := client.SendTransaction(ctx, msg, carbon.KeyPairSigners(keys), rpc.SendTransactionOptions{})
    if err != nil {
        log.Fatal(err)
    }

    tx, err := client.GetTransaction(ctx, hash)
    if err != nil {
        log.Fatal(err)
    }
    if !tx.StateIsSuccess() {
        log.Fatalf("transaction failed: %s", tx.State)
    }

    carbonTokenID, err := carbon.ParseCreateTokenResult(tx.Result)
    if err != nil {
        log.Fatal(err)
    }

    fmt.Println("carbon token id:", carbonTokenID)
}
```

For production flows, poll until the transaction is confirmed instead of
reading it immediately after broadcast.
