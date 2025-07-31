# Invoke a Script

{% hint style="info" %}
Before Invoking a Script, learn how to create one, [**here**](../../shared-methods/scriptbuilder/create-a-script.md)**.**

Also you need to know how to setup the **PhantasmaAPI,** to be able to call it Check it [**Here**](../../shared-methods/phantasmaapi.md)**.**
{% endhint %}

```javascript
import { PhantasmaAPI, ScriptBuilder } from "phantasma-ts";
const CHAIN_NAME = "main"; // This is the name of the chain, please don't change it.
const NETWORK_API_URL = "https://testnet.phantasma.io/rpc"; // for mainnet this should be https://pharpc1.phantasma.io/rpc
const NETWORK_PEER_URL = undefined; // this the peers URL to get the list of peers, if not provided it will use the default one "https://peers.phantasma.io/"
const NEXUS_NAME = "testnet"; // For mainnet use this "mainnet"
const API = new PhantasmaAPI(
  NETWORK_API_URL, 
  NETWORK_PEER_URL, 
  NEXUS_NAME 
);

let RPC = new PhantasmaAPI('https://testnet.phantasma.io/rpc', undefined, 'testnet');

async function GetMasterCount(){
    let sb = new ScriptBuilder();
    let script = sb
        .CallContract("stake", "GetMasterCount", []) 
        .EndScript();

    let myScript = sb.str;

    let txResult = await RPC.invokeRawScript(myScript);
    // this will return the data in a VMObject in Base16, you need to decode it.
    return txResult;
}
```
