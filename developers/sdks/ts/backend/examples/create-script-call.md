# Create Script Call

{% hint style="info" %}
**Check the Scriptbuilder:** It explains how to create every type of script.
{% endhint %}

{% content-ref url="../../shared-methods/script-builder.md" %}
[script-builder.md](../../shared-methods/script-builder.md)
{% endcontent-ref %}

## Example

```ts
import { ScriptBuilder } from "phantasma-sdk-ts";

const sb = new ScriptBuilder();
const script = sb
  .BeginScript()
  .CallContract("stake", "GetMasterCount", [])
  .EndScript();

console.log(script);
```
