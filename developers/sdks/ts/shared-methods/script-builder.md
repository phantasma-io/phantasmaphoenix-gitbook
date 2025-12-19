# ScriptBuilder

To execute operations on-chain you must build a script using `ScriptBuilder`.

```ts
import { Address, ScriptBuilder } from "phantasma-sdk-ts";

const sb = new ScriptBuilder();
```

## AllowGas

Allocates KCAL for a transaction. Every state-changing script must call `AllowGas` and `SpendGas`.

```ts
import { Address, DomainSettings, ScriptBuilder } from "phantasma-sdk-ts";

const from = Address.FromText("P2K...");
const gasPrice = DomainSettings.DefaultMinimumGasFee;
const gasLimit = 21000;

const script = new ScriptBuilder()
  .BeginScript()
  .AllowGas(from, Address.Null, gasPrice, gasLimit)
  .CallInterop("Runtime.TransferTokens", [from, "P2K...", "KCAL", "1000000000"])
  .SpendGas(from)
  .EndScript();
```

## SpendGas

Finalizes gas usage for the transaction.

```ts
const script = new ScriptBuilder()
  .BeginScript()
  .AllowGas(from, Address.Null, gasPrice, gasLimit)
  .CallContract("stake", "Claim", [from, from])
  .SpendGas(from)
  .EndScript();
```

## CallInterop

Use internal operations such as `Runtime.TransferTokens` or `Runtime.TransferToken`.

```ts
const script = new ScriptBuilder()
  .BeginScript()
  .AllowGas(from, Address.Null, gasPrice, gasLimit)
  .CallInterop("Runtime.TransferTokens", [from, "P2K...", "SOUL", "100000000"])
  .SpendGas(from)
  .EndScript();
```

## CallContract

Call a smart contract method by name.

```ts
const script = new ScriptBuilder()
  .BeginScript()
  .AllowGas(from, Address.Null, gasPrice, gasLimit)
  .CallContract("stake", "Stake", [from, "100000000"])
  .SpendGas(from)
  .EndScript();
```

{% hint style="info" %}
Contract names are usually lowercase (for example `stake`). Token symbols are uppercase (for example `SOUL`).
{% endhint %}
