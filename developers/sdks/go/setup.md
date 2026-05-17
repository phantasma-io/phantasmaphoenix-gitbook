# Go SDK Setup

The Go SDK is published as the module
`github.com/phantasma-io/phantasma-sdk-go`.

## Requirements

| Item | Requirement |
| ---- | ----------- |
| Go | `1.25` or newer |
| Toolchain used by the source repo | `go1.26.2` |
| Current public tag observed locally | `v0.9.0` |

Install the module:

```bash
go get github.com/phantasma-io/phantasma-sdk-go
```

## Imports

Use the packages that own the API area:

```go
import (
    "github.com/phantasma-io/phantasma-sdk-go/pkg/carbon"
    "github.com/phantasma-io/phantasma-sdk-go/pkg/cryptography"
    "github.com/phantasma-io/phantasma-sdk-go/pkg/rpc"
    scriptbuilder "github.com/phantasma-io/phantasma-sdk-go/pkg/vm/script_builder"
)
```

Lower-level packages such as `pkg/io`, `pkg/jsonrpc`, `pkg/domain`, and
`pkg/vm` are public for protocol tooling and migration work. Application code
should prefer the higher-level packages unless it needs direct wire-format
control.

## RPC Client

```go
ctx, cancel := context.WithTimeout(context.Background(), 10*time.Second)
defer cancel()

client := rpc.NewRPC("http://localhost:5172/rpc")
// client := rpc.NewRPCMainnet()
// client := rpc.NewRPCTestnet()
```

All typed RPC methods take `context.Context` as their first argument. Use
contexts to enforce request deadlines and cancellation.

## Source Layout

| Path | Contents |
| ---- | -------- |
| `pkg/rpc` | JSON-RPC client and typed method wrappers. |
| `pkg/rpc/response` | Result models returned by RPC wrappers. |
| `pkg/carbon` | Carbon serialization, transaction messages, token builders, fee options, and result parsers. |
| `pkg/cryptography` | Address, WIF, Ed25519 key, signature, and hash types. |
| `pkg/vm/script_builder` | VM script builder and high-level script helpers. |
| `pkg/blockchain` | Classic VM transaction type and transaction state helpers. |
