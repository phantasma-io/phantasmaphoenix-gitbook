# Quickstart

This guide shows a minimal backend flow: build a script, sign a transaction, send it, and confirm the result.

## 1) Install

```
npm install phantasma-sdk-ts
```

## 2) Build and Send a Transaction

```ts
import {
  Address,
  Base16,
  DomainSettings,
  PhantasmaAPI,
  PhantasmaKeys,
  ScriptBuilder,
  Transaction,
} from "phantasma-sdk-ts";

const rpcUrl = "https://testnet.phantasma.info/rpc";
const nexus = "testnet";
const chain = "main";

const api = new PhantasmaAPI(rpcUrl, undefined as any, nexus);

async function sendTransfer() {
  const keys = PhantasmaKeys.fromWIF("YOUR_WIF");
  const from = keys.Address;
  const to = "P2K...";

  const gasPrice = DomainSettings.DefaultMinimumGasFee;
  const gasLimit = 21000;

  const script = new ScriptBuilder()
    .BeginScript()
    .AllowGas(from, Address.Null, gasPrice, gasLimit)
    .CallInterop("Runtime.TransferTokens", [from, to, "KCAL", "1000000000"])
    .SpendGas(from)
    .EndScript();

  const expiration = new Date(Date.now() + 60_000);
  const payload = Base16.encode("quickstart");

  const tx = new Transaction(nexus, chain, script, expiration, payload);
  tx.signWithKeys(keys);

  const txHash = await api.sendRawTransaction(tx.toString(true));
  return txHash;
}
```

## 3) Confirm the Result

```ts
async function waitForConfirmation(txHash: string) {
  for (let i = 0; i < 30; i++) {
    const txInfo = await api.getTransaction(txHash);

    if (txInfo.state === "Halt") {
      return { success: true, result: txInfo.result };
    }

    if (txInfo.state === "Break" || txInfo.state === "Fault") {
      return { success: false, result: txInfo.result };
    }

    await new Promise((r) => setTimeout(r, 1000));
  }

  return { success: false, result: "timeout" };
}
```

## Notes

- `Address.Null` is used as the gas target for normal transactions.
- `payload` is a hex string; use `Base16.encode`.
- For frontend signing, use `PhantasmaLink.signTx` instead of signing locally.
