# TypeScript SDK Complete API Reference

This section documents the current `phantasma-sdk-ts` public surface for
application and tooling work. Start with setup and task pages for common flows;
use this section for method groups, result shapes, wire structures,
compatibility notes, and lower-level helpers.

Source baseline:

| Item | Value |
| ---- | ----- |
| Package | `phantasma-sdk-ts` |
| Version | `0.8.2` |
| Runtime | Node `>=22` |
| Recommended imports | `phantasma-sdk-ts/public`, plus `phantasma-sdk-ts/types` for the complete Carbon helper surface |
| Source commit | `fbd458026479e02a5caecc6cd8244d7f1e54e504` |

## Pages

| Page | Use it when |
| ---- | ----------- |
| [RPC Client](rpc-methods.md) | You need `PhantasmaAPI` methods, raw JSON-RPC result handling, broadcast helpers, or pagination behavior. |
| [RPC Result Models](rpc-models.md) | You need result interface fields returned by account, token, block, transaction, NFT, auction, archive, or network calls. |
| [VM and Transaction APIs](vm-transaction-binary.md) | You need key/address handling, VM scripts, transactions, signatures, event decoding, binary helpers, or compatibility aliases. |
| [Carbon API and Wire Format](carbon-wire.md) | You need Carbon serializers, schemas, token/series/NFT builders, fee options, signed messages, or result parsers. |
| [Public API Inventory](public-api.md) | You need the complete declaration list across package exports and deep-import declaration files. |

## Import Policy

Use `/public` for new code:

```ts
import { PhantasmaAPI, PhantasmaKeys, ScriptBuilder } from "phantasma-sdk-ts/public";
```

Lowercase deep imports are also available for stable areas:

```ts
import { PhantasmaAPI } from "phantasma-sdk-ts/rpc";
import { Transaction } from "phantasma-sdk-ts/tx";
import { ScriptBuilder } from "phantasma-sdk-ts/vm";
```

Use `/types` for Carbon helpers that are not runtime exports of `/public`:

```ts
import { CreateTokenFeeOptions, getRandomPhantasmaId } from "phantasma-sdk-ts/types";
```

The package root and `core/**` deep imports remain compatibility paths. New
code should not add new dependencies on those paths.

## Compatibility Aliases

The SDK keeps legacy PascalCase methods and old typoed aliases where existing
consumers may still use them. Canonical APIs are camelCase. Deprecated aliases
are declared with `@deprecated` and are planned for removal at v1.0.
