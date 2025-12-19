# Invoke a Script

{% hint style="warning" %}
This functionality is currently disabled and will be re‑enabled according to the [roadmap](https://phantasma.info/blockchain#roadmap)
{% endhint %}

{% hint style="info" %}
Before Invoking a Script, learn how to create one, [**here**](../../shared-methods/script-builder.md)**.**

Also you need to know how to setup the **PhantasmaAPI,** to be able to call it Check it [**Here**](../../shared-methods/phantasmaapi.md)**.**
{% endhint %}

```ts
import { Decoder, PhantasmaAPI, ScriptBuilder } from "phantasma-sdk-ts";

const CHAIN_NAME = "main";
const NETWORK_API_URL = "https://testnet.phantasma.info/rpc";
const NETWORK_PEER_URL = undefined;
const NEXUS_NAME = "testnet"; // For mainnet use this "mainnet"

const rpc = new PhantasmaAPI(NETWORK_API_URL, NETWORK_PEER_URL as any, NEXUS_NAME);

async function getMasterCount() {
  const sb = new ScriptBuilder();
  const script = sb
    .BeginScript()
    .CallContract("stake", "GetMasterCount", [])
    .EndScript();

  const result = await rpc.invokeRawScript(CHAIN_NAME, script);

  // this will return the data in a VMObject in Base16, you need to decode it.
  const decoder = new Decoder(result.result);
  const value = decoder.readVmObject();
  return value;
}
```
