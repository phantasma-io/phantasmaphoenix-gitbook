# Phantasma Link

## Overview

PhantasmaLink connects your dApp to a Phantasma wallet (Poltergeist/Ecto) and lets the user sign transactions.

## Defaults and connection details

- Default host: `localhost:7090` (WebSocket URL: `ws://localhost:7090/phantasma`).
- Default chain: `main`.
- `login` defaults: `version = 4`, `platform = "phantasma"`, `providerHint = "poltergeist"`.

If `window.PhantasmaLinkSocket` exists and `providerHint` is not `poltergeist`, the SDK uses that socket instead of a raw WebSocket.

## Initialization

```ts
import { PhantasmaLink, ProofOfWork } from "phantasma-sdk-ts";

const link = new PhantasmaLink("My Dapp", true);

link.login(
  (success) => {
    if (success) {
      console.log("Connected address:", link.account?.address);
    }
  },
  (error) => {
    console.error("Login failed:", error);
  },
  4, // protocol version
  "phantasma", // platform
  "poltergeist" // providerHint: "poltergeist" or "ecto"
);
```

## Account data

After a successful login, `link.account` contains:

- `alias`
- `name`
- `address`
- `avatar`
- `platform`
- `external`
- `balances`
- `files`

## Key Methods

- `login(onLogin, onError, version = 4, platform = "phantasma", providerHint = "poltergeist")`
- `invokeScript(script, callback)` for read-only calls.
- `signTx(script, payload, callback, onError, pow = ProofOfWork.None, signature = "Ed25519")`
- `signData(data, callback, onError, signature = "Ed25519")`
- `signTxSignature(tx, callback, onError, signature = "Ed25519")`
- `getPeer(callback, onError)`
- `toggleMessageLogging()`
- `signCarbonTxAndBroadcast(txMsg, callback, onError)` for Carbon transactions.
- `disconnect(triggered)`

{% hint style="info" %}
For the layer map and quick choice, see [Wallet Connection](/developers/sdks/ts/frontend/wallet-connection.md).  
If you prefer a wrapper, use [EasyConnect](/developers/sdks/ts/shared-methods/easyconnect.md).  
For React, use [React Wallet Connection](/developers/sdks/ts/frontend/connect-react.md).
{% endhint %}

## Formats and limits

- `script` must be a hex string produced by `ScriptBuilder.EndScript()`.
- `invokeScript` requires `script.length < 8192`.
- `signTx` requires `script.length < 65536`.
- `signTx` `payload` handling:
  - If `payload` is `null`, the SDK uses the default hex for `"Phantasma-ts"`.
  - If `payload` is a string, the SDK encodes it internally; do not pass pre-encoded hex.
- `signData` expects Base16-encoded data and requires `data.length < 1024`.
- `signTxSignature` expects a Base16-encoded serialized transaction and requires `tx.length < 1024`.
- `signCarbonTxAndBroadcast` requires Phantasma Link v4+, a valid `txMsg`, and a serialized hex length `< 65536`.

## Sending a Transaction

Assumes `link` is already connected via `login`.

```ts
import { Address, DomainSettings, ScriptBuilder } from "phantasma-sdk-ts";

const from = Address.FromText(link.account.address);
const gasPrice = DomainSettings.DefaultMinimumGasFee;
const gasLimit = 21000;

const script = new ScriptBuilder()
  .BeginScript()
  .AllowGas(from, Address.Null, gasPrice, gasLimit)
  .CallContract("stake", "Claim", [from, from])
  .SpendGas(from)
  .EndScript();

link.signTx(
  script,
  "Example.stake",
  (result) => console.log("tx hash:", result?.hash),
  (error) => console.error(error)
);
```

## Signing Data

Assumes `link` is already connected via `login`.

```ts
const messageHex = "48656c6c6f"; // "Hello" in Base16

link.signData(
  messageHex,
  (result) => console.log("signData result:", result),
  (error) => console.error("signData failed:", error)
);
```

## Signing a Transaction Signature

Assumes `link` is already connected via `login`.

```ts
const txHex = "<BASE16_SERIALIZED_TRANSACTION>";

link.signTxSignature(
  txHex,
  (result) => console.log("signTxSignature result:", result),
  (error) => console.error("signTxSignature failed:", error)
);
```

## Signing and Broadcasting a Carbon Transaction

Assumes `link` is already connected via `login`.

Build a `TxMsg` using the Carbon helpers (see [Carbon Workflows](/developers/sdks/ts/carbon-workflows.md)), then sign:

```ts
import { CreateTokenTxHelper } from "phantasma-sdk-ts";

const txMsg = CreateTokenTxHelper.buildTx(tokenInfo, creatorPublicKey);

link.signCarbonTxAndBroadcast(
  txMsg,
  (result) => console.log("Carbon tx result:", result),
  (error) => console.error("Carbon signing failed:", error)
);
```

## Proof of Work

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
