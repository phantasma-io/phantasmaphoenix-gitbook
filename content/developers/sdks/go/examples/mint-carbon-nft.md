---
title: "Go SDK Example: Mint Carbon NFT"
linkTitle: "Mint Carbon NFT"
weight: 70
---

This example mints one NFT into an existing series. The token was created with
`PrepareStandardTokenSchemas(false)`, so each NFT carries the standard fields in
its ROM. The key belongs to the series owner.

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
    keys, err := cryptography.FromWIF("YOUR_WIF")
    if err != nil {
        log.Fatal(err)
    }

    sender, err := carbon.Bytes32FromPublicKey(keys.PublicKey())
    if err != nil {
        log.Fatal(err)
    }

    receiver, err := carbon.Bytes32FromPhantasmaAddressText("P...")
    if err != nil {
        log.Fatal(err)
    }

    schemas := carbon.PrepareStandardTokenSchemas(false)
    rom, err := carbon.BuildPhantasmaNFTRom(schemas.ROM, []carbon.MetadataField{
        {Name: "name", Value: "NFT #1"},
        {Name: "description", Value: "Example mint"},
        {Name: "imageURL", Value: "https://example.com/nft.png"},
        {Name: "infoURL", Value: "https://example.com/nft"},
        {Name: "royalties", Value: int32(0)},
    })
    if err != nil {
        log.Fatal(err)
    }

    msg, err := carbon.BuildMintPhantasmaNonFungibleSingleTx(
        42,             // Carbon token id
        big.NewInt(777), // Phantasma series id
        sender,
        receiver,
        rom,
        nil, // RAM
        carbon.TxLimits{},
    )
    if err != nil {
        log.Fatal(err)
    }

    client := rpc.NewRPCTestnet()
    ctx := context.Background()
    hash, err := client.SendTransaction(ctx, msg, carbon.KeyPairSigners(keys), rpc.SendTransactionOptions{})
    if err != nil {
        log.Fatal(err)
    }

    fmt.Println(hash)
}
```

For several NFTs in one call, pass a slice of `carbon.PhantasmaNFTMintInfo` to
`BuildMintPhantasmaNonFungibleTx`. [NFT Minting](../nft-minting.md#parse-the-result)
shows how to wait for the transaction and read the ids of the minted NFTs.

The SDK has no builder for a direct `MintNonFungible`, which takes an NFT id
chosen by the caller. The chain refuses that call while its configuration
disables such ids, as it does on mainnet.
