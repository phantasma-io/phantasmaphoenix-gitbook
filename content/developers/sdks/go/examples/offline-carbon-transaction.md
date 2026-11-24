---
title: "Go SDK Example: Offline Carbon Transaction"
linkTitle: "Offline Carbon Transaction"
weight: 40
---

This example builds a Carbon create-token message and signs it locally. It does
not broadcast.

```go
package main

import (
    "context"
    "fmt"
    "log"
    "math/big"

    "github.com/phantasma-io/phantasma-sdk-go/pkg/carbon"
    "github.com/phantasma-io/phantasma-sdk-go/pkg/cryptography"
    "github.com/phantasma-io/phantasma-sdk-go/pkg/rpc"
)

func main() {
    keys, err := cryptography.GeneratePhantasmaKeys()
    if err != nil {
        log.Fatal(err)
    }

    owner, err := carbon.Bytes32FromPublicKey(keys.PublicKey())
    if err != nil {
        log.Fatal(err)
    }

    schemas := carbon.PrepareStandardTokenSchemas(false)
    metadata, err := carbon.BuildTokenMetadata(map[string]string{
        "name":        "Example NFT",
        "icon":        "data:image/png;base64,iVBORw0KGgo=",
        "url":         "https://example.com",
        "description": "Example NFT token",
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

    // Signing needs the chain's prices. Read the gas config once on a machine
    // that reaches a node, and carry it to the signer; signing itself needs no node.
    client := rpc.NewRPCTestnet()
    gasResult, err := client.GetGasConfig(context.Background())
    if err != nil {
        log.Fatal(err)
    }
    gasConfig, err := gasResult.ToGasConfig()
    if err != nil {
        log.Fatal(err)
    }

    signedHex, err := carbon.BuildCreateTokenTxAndSignHex(
        tokenInfo,
        keys,
        &gasConfig,
        carbon.PlanAndSignOptions{},
    )
    if err != nil {
        log.Fatal(err)
    }

    fmt.Println(signedHex)
}
```

The gas config comes from `client.GetGasConfig(ctx)` and `ToGasConfig()`. It
changes only through a governance resolution, so an offline signer can hold a
copy. A message signed against a stale config may offer too little gas, and a
short offer is rejected.

A message also expires. The default lifetime is 45 seconds, so an offline flow
should set `TxLimits.Expiry` from the chain's own window with
`carbon.ExpiryWithin`.

Broadcast the hex with `rpc.PhantasmaRPC.SendCarbonTransaction` only after the
application has selected the target network and funding key.
