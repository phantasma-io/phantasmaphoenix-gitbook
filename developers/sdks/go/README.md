# Go SDK

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

{% hint style="info" %}
Repository: [https://github.com/phantasma-io/phantasma-sdk-go](https://github.com/phantasma-io/phantasma-sdk-go)
{% endhint %}

## What It Covers

| Area | Package | Use it for |
| ---- | ------- | ---------- |
| RPC | `pkg/rpc`, `pkg/rpc/response` | Context-aware JSON-RPC calls and typed response models. |
| Keys and addresses | `pkg/cryptography` | WIF import/export, Ed25519 signatures, address parsing, hashes. |
| VM scripts | `pkg/vm/script_builder` | Contract calls, interop calls, gas handling, transfers, staking, and NFT calls. |
| VM transactions | `pkg/blockchain` | Classic VM transaction construction, signing, serialization, and state helpers. |
| Carbon | `pkg/carbon` | Carbon serialization, schemas, token creation payloads, NFT mint payloads, signed Carbon messages. |

## Carbon Workflows

{% content-ref url="token-deployment.md" %}
Token Deployment
{% endcontent-ref %}

{% content-ref url="nft-minting.md" %}
NFT Minting
{% endcontent-ref %}

{% content-ref url="schemas-and-metadata.md" %}
Schemas And Metadata
{% endcontent-ref %}

{% content-ref url="fees-and-broadcasting.md" %}
Fees And Broadcasting
{% endcontent-ref %}

{% content-ref url="carbon-operations.md" %}
Carbon Operations
{% endcontent-ref %}

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

{% content-ref url="setup.md" %}
Setup
{% endcontent-ref %}

{% content-ref url="rpc.md" %}
RPC
{% endcontent-ref %}

{% content-ref url="keys-and-addresses.md" %}
Keys And Addresses
{% endcontent-ref %}

{% content-ref url="vm-and-transactions.md" %}
VM and Transactions
{% endcontent-ref %}

{% content-ref url="carbon.md" %}
Carbon
{% endcontent-ref %}

{% content-ref url="api-reference.md" %}
API Overview
{% endcontent-ref %}

{% content-ref url="reference/README.md" %}
Complete API Reference
{% endcontent-ref %}

{% content-ref url="examples/README.md" %}
Examples
{% endcontent-ref %}
