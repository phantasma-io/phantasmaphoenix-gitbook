---
title: "Create Script Call"
weight: 20
---

> [!NOTE]
> **Check the Scriptbuilder:** It explains how to create every type of script.

- [ScriptBuilder](../../shared-methods/script-builder.md)

## Example

```ts
import { ScriptBuilder } from "phantasma-sdk-ts/public";

const address = "P2K..."; // the account to read

const sb = new ScriptBuilder();
const script = sb
  .beginScript()
  .callContract("stake", "GetUnclaimed", [address])
  .endScript();

console.log(script);
```

The script returns the KCAL the account can claim from its SOUL stake.
[Invoke a Script](invoke-a-script.md) runs such a script without a transaction.
