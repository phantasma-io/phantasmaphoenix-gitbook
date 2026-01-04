# EasyConnect

## Overview

`EasyConnect` is a small wrapper around `PhantasmaLink` from `phantasma-sdk-ts`. It manages login and exposes helpers for signing transactions.

{% hint style="info" %}
For the layer map and quick choice, see [Wallet Connection](/developers/sdks/ts/frontend/wallet-connection.md).
{% endhint %}

## When to use

- Frontend apps that want a smaller API than `PhantasmaLink`.
- Carbon signing via `signCarbonTransaction`.
- Non-React projects (for React, see [@phantasma/connect-react](/developers/sdks/ts/frontend/connect-react.md)).

## Install

```
npm install phantasma-sdk-ts
```

## Configuration

`EasyConnect` supports three configuration styles:

- `new EasyConnect()` uses:
  - `requiredVersion = 4`
  - `platform = "phantasma"`
  - `providerHint = "poltergeist"`
  - and then calls `setConfig("auto")`
- `new EasyConnect([version, platform, providerHint])` overrides the defaults.
- `setConfig("auto" | "poltergeist" | "ecto")` sets the provider hint.

`setConfig("auto")` checks `window.PhantasmaLinkSocket`. If it exists, it switches to `ecto`; otherwise it leaves `providerHint` empty.

{% hint style="info" %}
`EasyConnect` is intended for browser use. The default config reads from `window`.
{% endhint %}

## Connect (async wrapper)

`EasyConnect.connect` uses callbacks. If you prefer `async/await`, wrap it:

```ts
import { EasyConnect } from "phantasma-sdk-ts";

function connectAsync(conn: EasyConnect): Promise<void> {
  return new Promise((resolve, reject) => {
    conn.connect(
      (success) => {
        if (success) {
          resolve();
          return;
        }
        reject(new Error("Wallet rejected connection"));
      },
      (err) => {
        const message = typeof err === "string" ? err : JSON.stringify(err);
        reject(new Error(message));
      },
    );
  });
}

async function connectWallet() {
  const conn = new EasyConnect();
  conn.setConfig("poltergeist");

  await connectAsync(conn);
  console.log("Connected address:", conn.link.account?.address);

  return conn;
}
```

## Account info

After a successful connection, `conn.link.account` contains:

- `alias`
- `name`
- `address`
- `avatar`
- `platform`
- `external`
- `balances`
- `files`

## Signing helpers

`EasyConnect` exposes the following helpers:

- `signTransaction(script, payload, onSuccess, onFail)` (VM transactions)
- `signCarbonTransaction(txMsg, onSuccess, onFail)` (Carbon transactions)
- `signData(data, onSuccess, onFail)`
- `invokeScript(script, callback)`
- `disconnect()`

`signCarbonTransaction` calls `PhantasmaLink.signCarbonTxAndBroadcast`, which requires Phantasma Link protocol v4 or higher.

## Underlying PhantasmaLink

`EasyConnect` exposes the underlying `PhantasmaLink` instance as `conn.link`.  
If you want a custom dApp ID, set it before connecting:

```ts
const conn = new EasyConnect();
conn.link.dappID = "My Dapp";
conn.connect(/* ... */);
```
