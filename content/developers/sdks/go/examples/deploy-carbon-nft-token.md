---
title: "Go SDK Example: Deploy Carbon NFT Token"
linkTitle: "Deploy Carbon NFT Token"
weight: 60
---

This example creates an NFT token, waits for the transaction, and reads the new
token id from its result. It needs a funded key on the network it sends to.

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
    ctx, cancel := context.WithTimeout(context.Background(), time.Minute)
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
        "icon":        "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mNkYAAAAAYAAjCB0C8AAAAASUVORK5CYII=",
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

    // The transaction is readable once it is in a block.
    tx, err := client.GetTransaction(ctx, hash)
    for err != nil || !(tx.StateIsSuccess() || tx.StateIsFault()) {
        select {
        case <-ctx.Done():
            log.Fatal(ctx.Err())
        case <-time.After(time.Second):
        }
        tx, err = client.GetTransaction(ctx, hash)
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

The token uses `PrepareStandardTokenSchemas(true)`, so its NFTs share the
standard fields of their series. Its series therefore carry series metadata
built with `BuildTokenSeriesMetadata`; see
[Series Metadata](../schemas-and-metadata.md#series-metadata).
