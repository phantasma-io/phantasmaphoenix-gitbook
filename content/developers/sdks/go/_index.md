---
title: "Go SDK"
weight: 40
---

The Go SDK is a typed Go module for Phantasma applications, services, and
tooling. It covers JSON-RPC access, context-aware calls, Ed25519 keys and
addresses, VM script building, VM transaction signing, and Carbon wire-format
transactions.

Module path:

```bash
go get github.com/phantasma-io/phantasma-sdk-go
```

Main packages:

```go
import (
    "github.com/phantasma-io/phantasma-sdk-go/pkg/carbon"
    "github.com/phantasma-io/phantasma-sdk-go/pkg/cryptography"
    "github.com/phantasma-io/phantasma-sdk-go/pkg/rpc"
    scriptbuilder "github.com/phantasma-io/phantasma-sdk-go/pkg/vm/script_builder"
)
```

> [!NOTE]
> Repository: [https://github.com/phantasma-io/phantasma-sdk-go](https://github.com/phantasma-io/phantasma-sdk-go)

## What It Covers

| Area | Package | Use it for |
| ---- | ------- | ---------- |
| RPC | `pkg/rpc`, `pkg/rpc/response` | Context-aware JSON-RPC calls and typed response models. |
| Keys and addresses | `pkg/cryptography` | WIF import/export, Ed25519 signatures, address parsing, hashes. |
| VM scripts | `pkg/vm/script_builder` | Contract calls, interop calls, gas handling, transfers, staking, and NFT calls. |
| VM transactions | `pkg/blockchain` | Script transaction construction, signing, serialization, and state helpers. |
| Carbon | `pkg/carbon` | Carbon serialization, schemas, token creation payloads, NFT mint payloads, signed Carbon messages. |

## Carbon Workflows

- [Token Deployment](token-deployment.md)
- [NFT Minting](nft-minting.md)
- [Schemas And Metadata](schemas-and-metadata.md)
- [Fees And Broadcasting](fees-and-broadcasting.md)
- [Carbon Operations](carbon-operations.md)

## Read-Only RPC Example

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
    version, err := client.GetVersion(ctx)
    if err != nil {
        log.Fatal(err)
    }

    fmt.Println(version.Version, version.Commit)
}
```

Read-only calls do not require a signing key. Broadcasting helpers require a
funded key and an endpoint selected by the application.

## Guides

- [Setup](setup.md)
- [RPC](rpc.md)
- [Keys And Addresses](keys-and-addresses.md)
- [VM and Transactions](vm-and-transactions.md)
- [Carbon](carbon.md)
- [API Overview](api-reference.md)
- [Complete API Reference](reference/_index.md)
- [Examples](examples/_index.md)
