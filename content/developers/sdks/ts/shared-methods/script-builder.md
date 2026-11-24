---
title: "ScriptBuilder"
linkTitle: "Script Builder"
weight: 90
---

To execute operations on-chain you must build a script using `ScriptBuilder`.

```ts
import { Address, ScriptBuilder } from "phantasma-sdk-ts/public";

const sb = new ScriptBuilder();
```

## allowGas

Sets the gas payer and the most KCAL the transaction may spend: `gasPrice * gasLimit` is the transaction's `maxGas`, in KCAL atoms. A script sent as a VM transaction with `sendRawTransaction` must call `allowGas`.

```ts
import { Address, DomainSettings, ScriptBuilder } from "phantasma-sdk-ts/public";

const from = Address.fromText("P2K...");
const gasPrice = DomainSettings.DefaultMinimumGasFee;
const gasLimit = 21000;

const script = new ScriptBuilder()
  .beginScript()
  .allowGas(from, Address.nullAddress, gasPrice, gasLimit)
  .callInterop("Runtime.TransferTokens", [from, "P2K...", "KCAL", "1000000000"])
  .spendGas(from)
  .endScript();
```

## spendGas

Adds a `SpendGas` call. The chain accepts the call and ignores it: the chain settles the gas bill and refunds unused KCAL to the gas payer after the script finishes, with or without `SpendGas`.

```ts
const script = new ScriptBuilder()
  .beginScript()
  .allowGas(from, Address.nullAddress, gasPrice, gasLimit)
  .callContract("stake", "Claim", [from, from])
  .spendGas(from)
  .endScript();
```

## callInterop

Use internal operations such as `Runtime.TransferTokens` or `Runtime.TransferToken`.

```ts
const script = new ScriptBuilder()
  .beginScript()
  .allowGas(from, Address.nullAddress, gasPrice, gasLimit)
  .callInterop("Runtime.TransferTokens", [from, "P2K...", "SOUL", "100000000"])
  .spendGas(from)
  .endScript();
```

## callContract

Call a smart contract method by name.

```ts
const script = new ScriptBuilder()
  .beginScript()
  .allowGas(from, Address.nullAddress, gasPrice, gasLimit)
  .callContract("stake", "Stake", [from, "100000000"])
  .spendGas(from)
  .endScript();
```

> [!NOTE]
> Built-in contract names use lowercase identifiers such as `stake`. Token
> symbols use uppercase identifiers such as `SOUL`.
