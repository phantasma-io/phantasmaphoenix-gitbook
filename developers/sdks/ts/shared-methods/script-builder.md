# ScriptBuilder

To execute operations on-chain you must build a script using `ScriptBuilder`.

```ts
import { Address, ScriptBuilder } from "phantasma-sdk-ts/public";

const sb = new ScriptBuilder();
```

## allowGas

Allocates KCAL for a transaction. Every state-changing script must call `allowGas` and `spendGas`.

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

Finalizes gas usage for the transaction.

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

{% hint style="info" %}
Built-in contract names use lowercase identifiers such as `stake`. Token
symbols use uppercase identifiers such as `SOUL`.
{% endhint %}
