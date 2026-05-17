# Go SDK Complete API Reference

This section documents the public Go SDK API at the level needed for ordinary
application and tooling work without reading source for every call.

Source baseline:

| Item | Value |
| ---- | ----- |
| Module | `github.com/phantasma-io/phantasma-sdk-go` |
| Go version | `1.25+` |
| Current local branch | `development` |
| Current source commit | `7630d54796b8dd23655b39fa01109e4bfc08461b` |
| Current public tag observed | `v0.9.0` |

## Pages

| Page | Use it when |
| ---- | ----------- |
| [RPC Client](rpc-methods.md) | You need typed RPC wrappers, raw calls, pagination, broadcast helpers, or address-type variants. |
| [RPC Result Models](rpc-models.md) | You need fields and helpers returned by account, token, block, transaction, NFT, auction, archive, or network calls. |
| [VM and Transaction APIs](vm-transaction-binary.md) | You need keys, addresses, VM script building, transaction signing, binary helpers, or VM object decoding. |
| [Carbon API and Wire Format](carbon-wire.md) | You need Carbon transaction builders, schemas, metadata, fee options, wire structures, signing, or result parsers. |
| [Public API Inventory](public-api.md) | You need the complete list of exported identifiers under `pkg/**`. |

## Import Policy

Prefer package-level imports that match the feature being used:

```go
import (
    "github.com/phantasma-io/phantasma-sdk-go/pkg/carbon"
    "github.com/phantasma-io/phantasma-sdk-go/pkg/cryptography"
    "github.com/phantasma-io/phantasma-sdk-go/pkg/rpc"
    "github.com/phantasma-io/phantasma-sdk-go/pkg/rpc/response"
    scriptbuilder "github.com/phantasma-io/phantasma-sdk-go/pkg/vm/script_builder"
)
```

The SDK keeps lower-level packages public for wire tooling. Application code
should not depend on lower-level internals when a higher-level package provides
the same operation.
