# Invoke a Script

{% hint style="warning" %}
This functionality is not yet available and will be released according to the [roadmap](https://phantasma.info/blockchain#roadmap)
{% endhint %}

{% hint style="info" %}
Before Invoking a Script, learn how to create one, [**here**](../../shared-methods/scriptbuilder/create-a-script.md)**.**

Also you need to know how to setup the **PhantasmaAPI,** to be able to call it Check it [**Here**](../../shared-methods/phantasmaapi.md)**.**
{% endhint %}

```javascript
import { PhantasmaAPI, ScriptBuilder } from "phantasma-sdk-ts";
const CHAIN_NAME = "main";
const NETWORK_API_URL = "https://testnet.phantasma.info/rpc";
const NETWORK_PEER_URL = undefined;
const NEXUS_NAME = "testnet"; // For mainnet use this "mainnet"

let RPC = new PhantasmaAPI('https://testnet.phantasma.info/rpc', undefined as any, 'testnet');

async function GetMasterCount(){
    let sb = new ScriptBuilder();
    let script = sb
        .CallContract("stake", "GetMasterCount", []) 
        .EndScript();

    let myScript = sb.str;

    let txResult = await RPC.invokeRawScript(CHAIN_NAME, myScript);
    // this will return the data in a VMObject in Base16, you need to decode it.
    return txResult;
}
```
