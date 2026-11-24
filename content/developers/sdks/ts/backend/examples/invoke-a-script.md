---
title: "Invoke a Script"
weight: 100
---

> [!NOTE]
> Current RPC and TypeScript SDK source expose `invokeRawScript` as a read-only VM execution call. The example does not require transaction signing or a wallet prompt.

> [!NOTE]
> Before Invoking a Script, learn how to create one, [**here**](../../shared-methods/script-builder.md)**.**
>
> Also you need to know how to setup the **PhantasmaAPI,** to be able to call it Check it [**Here**](../../shared-methods/phantasmaapi.md)**.**

```ts
import { Decoder, PhantasmaAPI, ScriptBuilder } from "phantasma-sdk-ts/public";

const CHAIN_NAME = "main";
const NETWORK_API_URL = "https://testnet.phantasma.info/rpc";
const NETWORK_PEER_URL = undefined;
const NEXUS_NAME = "testnet"; // For mainnet use this "mainnet"

const rpc = new PhantasmaAPI(NETWORK_API_URL, NETWORK_PEER_URL as any, NEXUS_NAME);

// Returns the KCAL atoms an account can claim from its SOUL stake, as decimal text.
async function getUnclaimed(address: string) {
  const sb = new ScriptBuilder();
  const script = sb
    .beginScript()
    .callContract("stake", "GetUnclaimed", [address])
    .endScript();

  const result = await rpc.invokeRawScript(CHAIN_NAME, script);

  // The result is a serialized VM object in hex.
  const decoder = new Decoder(result.result);
  return decoder.readVmObject();
}
```
