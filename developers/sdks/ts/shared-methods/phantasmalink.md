# Phantasma Link

## Overview

PhantasmaLink connects your dApp to a Phantasma wallet (Poltergeist/Ecto) over a local WebSocket and lets the user sign transactions.

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

## Key Methods

- `login(onLogin, onError, version = 4, platform = "phantasma", providerHint = "poltergeist")`
- `invokeScript(script, callback)` for read-only calls.
- `signTx(script, payload, callback, onError, pow = ProofOfWork.None, signature = "Ed25519")`
- `signData(data, callback, onError)`
- `getPeer(callback, onError)`
- `toggleMessageLogging()`
- `signCarbonTxAndBroadcast(txMsg, callback, onError)` for Carbon transactions.

{% hint style="info" %}
If you prefer a wrapper, use `EasyConnect` (it exposes `signCarbonTransaction` and handles login setup).
{% endhint %}

{% hint style="info" %}
Carbon signing requires Phantasma Link protocol version 4 or higher.
{% endhint %}

{% hint style="info" %}
`payload` in `signTx` is a raw string. The SDK encodes it internally, so do not pass a pre-encoded hex string.
{% endhint %}

{% hint style="info" %}
`script` must be a hex string produced by `ScriptBuilder.EndScript()`.
{% endhint %}

## Sending a Transaction

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
