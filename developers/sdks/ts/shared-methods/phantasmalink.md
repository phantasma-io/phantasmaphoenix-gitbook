# Phantasma Link

## Overview

`PhantasmaLink` is the low-level browser wallet bridge in `phantasma-sdk-ts`. It connects a dApp to a wallet such as Poltergeist or Ecto and exposes the raw Link signing and query methods.

Use it when you want direct control over:

- transport selection
- wallet authorize flow
- VM script signing
- Carbon signing and broadcast
- prebuilt transaction signing

If you want a smaller wrapper, use [EasyConnect](/developers/sdks/ts/shared-methods/easyconnect.md).
If you want React state and widgets, use [@phantasma/connect-react](/developers/sdks/ts/frontend/connect-react.md).

## Current Defaults

Constructor defaults in current `phantasma-sdk-ts`:

- host: `localhost:7090`
- websocket path: `ws://localhost:7090/phantasma`
- version: `4`
- chain: `main`
- nexus: empty until the wallet returns one
- platform: `poltergeist`

Important change: `nexus` no longer defaults to a fake network value. It is empty until wallet authorize or `getNexus()` returns a real value.

## Transport Selection

`PhantasmaLink` can use two transport styles:

- raw local WebSocket
- injected `window.PhantasmaLinkSocket`

Current behavior:

- if `window.PhantasmaLinkSocket` exists and `providerHint !== "poltergeist"`, the SDK uses injected transport
- otherwise it uses raw WebSocket

That means `providerHint = "poltergeist"` is the simple way to force local-socket behavior.

## Basic Login

```ts
import { PhantasmaLink } from "phantasma-sdk-ts";

const link = new PhantasmaLink("My Dapp", true);

link.login(
  (success) => {
    if (success) {
      console.log("Connected address:", link.account?.address);
      console.log("Wallet:", link.wallet);
      console.log("Nexus:", link.nexus);
    }
  },
  (error) => {
    console.error("Login failed:", error);
  },
  4,
  "phantasma",
  "poltergeist"
);
```

## Account And Session Data

After successful login, these fields are the most useful:

- `link.account`
  - wallet account details such as `address`, `name`, `balances`, `files`
- `link.wallet`
  - wallet name returned by the authorize flow
- `link.nexus`
  - wallet network returned by authorize or refreshed with `getNexus()`
- `link.chain`
  - VM chain used in Link requests, default `main`

## Main Methods

| Method | Use |
| --- | --- |
| `login(...)` | Open a wallet session and authorize the dApp. |
| `invokeScript(script, callback)` | Read-only VM script execution through the wallet. |
| `signTx(script, payload, callback, onError, pow, signature)` | Ask the wallet to sign and send a VM script transaction. |
| `signTxSignature(tx, callback, onError, signature)` | Ask the wallet to sign an already serialized unsigned transaction. |
| `signPrebuiltTransaction(tx, callback, onError, signature)` | Build on top of `signTxSignature` and return a ready-to-broadcast signed transaction hex. |
| `signData(data, callback, onError, signature)` | Ask the wallet to sign arbitrary Base16 data. |
| `signCarbonTxAndBroadcast(txMsg, callback, onError)` | Sign and broadcast a Carbon transaction message. |
| `getNexus(callback, onError)` | Query the wallet network and sync `link.nexus`. |
| `getPeer(callback, onError)` | Query the connected wallet peer. |
| `disconnect(message)` | Close the session. |

## Size Limits And Payload Rules

- `invokeScript` requires `script.length < 8192`
- `signTx` requires `script.length < 65536`
- `signData` requires `data.length < 1024`
- `signTxSignature` requires `tx.length < 65536`
- `signCarbonTxAndBroadcast` requires serialized tx hex length `< 65536`

For `signTx` payloads:

- if `payload` is `null`, the SDK uses the default hex for `Phantasma-ts`
- if `payload` is a plain string, the SDK encodes it internally
- do not pre-encode the payload hex yourself when calling `signTx`

## `signTx` Versus `signPrebuiltTransaction`

These methods solve different problems.

### `signTx(...)`

Use `signTx(...)` when you want the wallet to handle a normal VM transaction from:

- `script`
- `payload`
- optional `pow`

This is the usual path for ordinary wallet-driven VM transactions.

### `signPrebuiltTransaction(...)`

Use `signPrebuiltTransaction(...)` when you already have a `Transaction` object and want the wallet to provide only the signature.

This is the right tool when you need to control transaction fields locally before asking the wallet to sign, for example:

- custom expiration
- custom payload handling
- pre-mined proof-of-work on a fully assembled transaction
- raw broadcast through `PhantasmaAPI.sendRawTransaction(...)`

Example:

```ts
import { PhantasmaLink, Transaction } from "phantasma-sdk-ts";

const link = new PhantasmaLink("My Dapp");
const tx = new Transaction("<nexus>", "<chain>", "<scriptHex>", new Date(), "<payloadHex>");

link.signPrebuiltTransaction(
  tx,
  (result) => {
    console.log("wallet signature:", result.signature);
    console.log("signed tx hex:", result.signedTx);
  },
  (error) => {
    console.error("signPrebuiltTransaction failed:", error);
  }
);
```

The returned `signedTx` can then be sent through `PhantasmaAPI.sendRawTransaction(...)`.

## `signTxSignature(...)`

`signTxSignature(...)` is lower level than `signPrebuiltTransaction(...)`.

It accepts:

- an unsigned serialized transaction hex
- a signature type, currently `Ed25519`

The wallet returns a signature payload. `signPrebuiltTransaction(...)` is usually more convenient because it also assembles and verifies the signed transaction for you.

## Carbon Signing

For Carbon-native flows, use `signCarbonTxAndBroadcast(...)`.

```ts
import { CreateTokenTxHelper } from "phantasma-sdk-ts";

const txMsg = CreateTokenTxHelper.buildTx(tokenInfo, creatorPublicKey);

link.signCarbonTxAndBroadcast(
  txMsg,
  (result) => console.log("Carbon tx result:", result),
  (error) => console.error("Carbon signing failed:", error)
);
```

## Proof Of Work Enum

```ts
enum ProofOfWork {
  None = 0,
  Minimal = 5,
  Moderate = 15,
  Hard = 19,
  Heavy = 24,
  Extreme = 30,
}
```

## Practical Guidance

- Prefer `signTx(...)` for normal wallet-driven VM transactions.
- Prefer `signPrebuiltTransaction(...)` when your app must control the final transaction bytes before signing.
- Use `getNexus()` if you need to refresh wallet network state explicitly after connection.
- Force `providerHint = "poltergeist"` when you need raw local-socket behavior rather than injected transport.
