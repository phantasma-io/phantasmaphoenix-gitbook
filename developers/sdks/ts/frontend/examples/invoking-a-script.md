---
description: Get some data from the blockchain
---

{% hint style="warning" %}
This functionality is currently disabled and will be re‑enabled according to the [roadmap](https://phantasma.info/blockchain#roadmap)
{% endhint %}

# Invoking a Script

{% hint style="info" %}
This is used to query data from the blockchain, it's act's like a **get**

The arguments or **args** here should be always inside of an array.
{% endhint %}

To do it using the **PhantasmaAPI** check this example

{% content-ref url="../../backend/examples/invoke-a-script.md" %}
[invoke-a-script.md](../../backend/examples/invoke-a-script.md)
{% endcontent-ref %}

## Using Phantasma Link

This example is using the PhantasmaLink

Invoking a Script doesn't need the user to accept anything.

{% code overflow="wrap" lineNumbers="true" %}
```typescript
import { PhantasmaLink, Transaction, ScriptBuilder } from "phantasma-sdk-ts";

const CHAIN_NAME = "main"; // This is the name of the chain, please don't change it.

let contractName = "mycontract";
let contractMethod = "getMyInfo";
let args = ["arg1", "arg2"]; // this is just a example of arguments.


const sb = new ScriptBuilder();
const myScript = sb.BeginScript()
    .CallContract(contractName, contractMethod, args)
    .EndScript();

Link.invokeScript(myScript, (result) => {
    // Handle the Data returned here.
});

```
{% endcode %}
