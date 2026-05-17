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

    txHex, err := carbon.BuildMintNonFungibleTxAndSignHex(
        42,
        1,
        keys,
        receiver,
        rom,
        nil,
        carbon.DefaultMintNFTFeeOptions(),
        100_000_000,
        time.Now().UTC().Add(20*time.Minute).UnixMilli(),
    )
    if err != nil {
        log.Fatal(err)
    }

    fmt.Println(txHex)
}
```

For deterministic Phantasma NFT mints, build public ROM with
`BuildPhantasmaNFTRom` and call
`BuildMintPhantasmaNonFungibleSingleTxAndSignHex` or the batch helper. Batch
helpers scale mint gas by the number of token records.
