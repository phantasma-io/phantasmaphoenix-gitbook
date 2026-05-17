# Go SDK Example: Keys And Addresses

```go
package main

import (
    "fmt"
    "log"

    "github.com/phantasma-io/phantasma-sdk-go/pkg/carbon"
    "github.com/phantasma-io/phantasma-sdk-go/pkg/cryptography"
)

func main() {
    keys, err := cryptography.GeneratePhantasmaKeys()
    if err != nil {
        log.Fatal(err)
    }

    imported, err := cryptography.FromWIF(keys.WIF())
    if err != nil {
        log.Fatal(err)
    }

    address := imported.Address()
    parsed, err := cryptography.FromString(address.String())
    if err != nil {
        log.Fatal(err)
    }

    carbonAddress, err := carbon.Bytes32FromPhantasmaAddress(parsed)
    if err != nil {
        log.Fatal(err)
    }

    fmt.Println(address.String())
    fmt.Println(carbonAddress.String())
}
```

Do not log WIF values in production. The example round-trips the WIF only to
show the API shape.
