# Go SDK Example: Read-Only RPC

```go
package main

import (
    "context"
    "fmt"
    "log"
    "time"

    "github.com/phantasma-io/phantasma-sdk-go/pkg/rpc"
)

func main() {
    ctx, cancel := context.WithTimeout(context.Background(), 10*time.Second)
    defer cancel()

    client := rpc.NewRPCTestnet()

    height, err := client.GetBlockHeight(ctx, "main")
    if err != nil {
        log.Fatal(err)
    }

    version, err := client.GetVersion(ctx)
    if err != nil {
        log.Fatal(err)
    }

    fmt.Println("height:", height.String())
    fmt.Println("node:", version.Version, version.Commit)
}
```

Use short contexts for UI and CLI reads. For background services, pass the
service-level context so shutdown cancels in-flight RPC calls.
