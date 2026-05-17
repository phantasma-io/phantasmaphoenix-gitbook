# Go SDK Example: Offline VM Transaction

This example builds and signs a classic VM transaction locally. It does not
broadcast.

```go
package main

import (
    "encoding/hex"
    "fmt"
    "log"
    "math/big"
    "time"

    "github.com/phantasma-io/phantasma-sdk-go/pkg/blockchain"
    "github.com/phantasma-io/phantasma-sdk-go/pkg/cryptography"
    scriptbuilder "github.com/phantasma-io/phantasma-sdk-go/pkg/vm/script_builder"
)

func main() {
    keys, err := cryptography.GeneratePhantasmaKeys()
    if err != nil {
        log.Fatal(err)
    }

    sender := keys.Address()
    receiver := cryptography.MustAddressFromString(sender.String())

    script := scriptbuilder.BeginScript().
        AllowGas(sender, cryptography.NullAddress(), big.NewInt(100000), big.NewInt(21000)).
        TransferTokens("SOUL", sender, receiver, big.NewInt(100000000)).
        SpendGas(sender).
        EndScript()

    tx := blockchain.NewTransaction(
        "testnet",
        "main",
        script,
        uint32(time.Now().UTC().Add(20*time.Minute).Unix()),
        []byte("GO-SDK"),
    )

    if err := tx.Sign(keys); err != nil {
        log.Fatal(err)
    }

    fmt.Println(hex.EncodeToString(tx.Bytes()))
}
```

For external address input, use checked parsing instead of
`MustAddressFromString`.
