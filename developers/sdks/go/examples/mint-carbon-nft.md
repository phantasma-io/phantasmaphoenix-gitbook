# Go SDK Example: Mint Carbon NFT

This example signs a direct one-item Carbon NFT mint. It assumes the token and
series already exist and that the caller has the schema used by that token.

```go
package main

import (
    "fmt"
    "log"
    "math/big"
    "time"

    "github.com/phantasma-io/phantasma-sdk-go/pkg/carbon"
    "github.com/phantasma-io/phantasma-sdk-go/pkg/cryptography"
)

func main() {
    keys, err := cryptography.FromWIF("YOUR_WIF")
    if err != nil {
        log.Fatal(err)
    }

    receiver, err := carbon.Bytes32FromPhantasmaAddressText("P...")
    if err != nil {
        log.Fatal(err)
    }

    schemas := carbon.PrepareStandardTokenSchemas(false)
    rom, err := carbon.BuildNFTRom(schemas.ROM, big.NewInt(1), []carbon.MetadataField{
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
    hash, err := client.SendTransaction(ctx, msg, carbon.KeyPairSigners(keys), rpc.SendTransactionOptions{})
    if err != nil {
        log.Fatal(err)
    }

    fmt.Println(hash)
}
```

Build the public ROM with `BuildPhantasmaNFTRom`. For batch mints, pass a slice
of `carbon.PhantasmaNFTMintInfo` to `BuildMintPhantasmaNonFungibleTx`.

The SDK carries no builder for a direct `MintNonFungible`. The chain refuses
that operation where governance has not allowed caller-supplied ROM ids, and
that is the state of the public chains today.
