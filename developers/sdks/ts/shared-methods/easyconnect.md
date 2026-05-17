# EasyConnect

## Overview

`EasyConnect` is a lightweight wrapper around `PhantasmaLink`. It keeps the callback-style wallet model, but gives frontend apps a smaller surface for common connection and signing tasks.

Use it when you want:

- simpler browser wallet connection than raw `PhantasmaLink`
- a direct helper for Carbon signing
- a wrapper that still exposes the underlying `link` when you need lower-level control

If you are in React, the preferred higher-level wrapper is [@phantasma/connect-react](/developers/sdks/ts/frontend/connect-react.md).

## Install

```bash
npm install phantasma-sdk-ts
```

## Current Defaults

Without options, `EasyConnect` starts with:

- `requiredVersion = 4`
- `platform = "phantasma"`
- `providerHint = "poltergeist"`
- `nexus = null` until a real connection succeeds

Important change: `EasyConnect.nexus` is no longer pre-filled with a fake default network. It stays `null` until the underlying link reports a recognized nexus.

## Configuration

You can construct it in three common ways:

```ts
const conn = new EasyConnect();
```

```ts
const conn = new EasyConnect(["4", "phantasma", "poltergeist"]);
```

```ts
const conn = new EasyConnect();
conn.setConfig("auto");
conn.setConfig("ecto");
conn.setConfig("poltergeist");
```

### `setConfig(...)`

Supported values:

- `"auto"`
- `"ecto"`
- `"poltergeist"`

Current behavior:

- `"auto"` uses injected transport when `window.PhantasmaLinkSocket` exists, otherwise it leaves `providerHint` empty and falls back to raw socket transport rules
- `"ecto"` sets `providerHint = "ecto"`
- `"poltergeist"` sets `providerHint = "poltergeist"`

## Connect

```ts
import { EasyConnect } from "phantasma-sdk-ts/public";

const conn = new EasyConnect();
conn.setConfig("poltergeist");

conn.connect(
  (success) => {
    if (success) {
      console.log("Connected address:", conn.link.account?.address);
      console.log("Wallet nexus:", conn.nexus);
    }
  },
  (error) => {
    console.error("Connect failed:", error);
  }
);
```

After a successful connection:

- `conn.connected === true`
- `conn.link` is the underlying `PhantasmaLink`
- `conn.nexus` is set when the wallet reported a recognized nexus value

## Underlying Link

`EasyConnect` deliberately exposes `conn.link`.

That means you can start simple and still drop down to raw Link features when needed, for example:

- `conn.link.signTx(...)`
- `conn.link.signPrebuiltTransaction(...)`
- `conn.link.getNexus(...)`

## Main Helpers

| Method | Use |
| --- | --- |
| `connect(onSuccess, onFail)` | Connect and authorize the dApp. |
| `disconnect(message)` | Close the wallet session. |
| `signTransaction(script, payload, onSuccess, onFail)` | Normal wallet-driven VM transaction signing. |
| `signCarbonTransaction(txMsg, onSuccess, onFail)` | Carbon signing and broadcast helper. |
| `signPrebuiltTransaction(tx, onSuccess, onFail)` | Sign a locally assembled `Transaction`. |
| `signData(data, onSuccess, onFail)` | Arbitrary data signing. |
| `invokeScript(script, callback)` | Read-only VM invoke. |
| `deployContract(script, payload, pow, onSuccess, onFail)` | Convenience wrapper over `link.signTx(...)` with proof-of-work parameter. |

## `signTransaction(...)` Versus `signPrebuiltTransaction(...)`

### `signTransaction(...)`

Use this for ordinary wallet-driven VM script transactions where the wallet builds the final transaction from:

- script
- payload

This is the simplest wallet-built VM signing path.

### `signPrebuiltTransaction(...)`

Use this when your application already created a `Transaction` object and needs the wallet signature on that exact transaction.

This is the better tool when you need to control:

- expiration
- payload bytes
- pre-mined proof-of-work on the fully assembled transaction

Example:

```ts
import { EasyConnect, Transaction } from "phantasma-sdk-ts/public";

const conn = new EasyConnect();

const tx = new Transaction("<nexus>", "<chain>", "<scriptHex>", new Date(), "<payloadHex>");

conn.signPrebuiltTransaction(
  tx,
  (result) => {
    console.log("signed tx:", result.signedTx);
  },
  (error) => {
    console.error(error);
  }
);
```

## Carbon Signing

`signCarbonTransaction(...)` is the easy entry point for Carbon-native transaction messages:

```ts
conn.signCarbonTransaction(
  txMsg,
  (result) => console.log("Carbon tx result:", result),
  (error) => console.error("Carbon signing failed:", error)
);
```

## Contract Lifecycle Note

`deployContract(...)` is only a thin helper over `link.signTx(...)` with a proof-of-work argument. It is fine for straightforward wallet-managed deploy flows.

If your application must assemble a VM transaction locally before signing, prefer:

- `Transaction`
- `signPrebuiltTransaction(...)`
- raw broadcast through `PhantasmaAPI.sendRawTransaction(...)`

## Async Wrapper Example

If you prefer `async/await`, wrap the callbacks:

```ts
import { EasyConnect } from "phantasma-sdk-ts/public";

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
      }
    );
  });
}
```
