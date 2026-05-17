# Go SDK Example: Offline Carbon Transaction

This example builds a Carbon create-token message and signs it locally. It does
not broadcast.

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

    signedHex, err := carbon.BuildCreateTokenTxAndSignHex(
        tokenInfo,
        keys,
        carbon.DefaultCreateTokenFeeOptions(),
        100_000_000,
        time.Now().UTC().Add(20*time.Minute).UnixMilli(),
    )
    if err != nil {
        log.Fatal(err)
    }

    fmt.Println(signedHex)
}
```

Broadcast the hex with `rpc.PhantasmaRPC.SendCarbonTransaction` only after the
application has selected the target network and funding key.
