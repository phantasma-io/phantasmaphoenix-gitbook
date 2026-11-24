---
title: "Setup"
weight: 10
---

## Installation

> [!NOTE]
> **Important:** Before the Phoenix chain update, the package **phantasma-ts** was used. It is now deprecated. Use **phantasma-sdk-ts** instead.

### In a TypeScript project

```
npm install phantasma-sdk-ts
```

New TypeScript code should import from the public entrypoint:

```ts
import { PhantasmaAPI, PhantasmaKeys, ScriptBuilder } from "phantasma-sdk-ts/public";
```

Lowercase deep imports are available for stable source areas such as
`phantasma-sdk-ts/rpc`, `phantasma-sdk-ts/tx`, `phantasma-sdk-ts/vm`,
and `phantasma-sdk-ts/types`. `/public` carries the RPC client, the Carbon
builders and the fee planner. Use `/types` for the few Carbon helpers that are
not runtime exports of `/public`, such as `getRandomPhantasmaId`. The root
export and `core/**` paths remain for compatibility with older consumers, but
new code should use `/public` or the documented lowercase entrypoints.

The Ledger flow lives in the SDK, and the application passes in the transport of
its own runtime. The SDK opens no device and depends on no USB package, so a
consumer that never touches a Ledger installs no native USB stack.

### React bindings (optional)

```
npm install phantasma-link-react
```

`phantasma-link-react` wraps the Link v5 client in a provider, a store and a connect widget. See [React Wallet Connection](frontend/connect-react.md).

## Backend or Frontend?

For backend usage, see:

- [Backend Guide](backend/_index.md)

For frontend usage with Poltergeist/Ecto:

- [Frontend Guide](frontend/_index.md)
