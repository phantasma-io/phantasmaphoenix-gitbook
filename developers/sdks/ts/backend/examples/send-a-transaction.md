---
description: Sending a transaction from a Node.js backend.
---

# Send a Transaction

{% hint style="info" %}
The signer's WIF is needed; export it from Poltergeist Lite or Ecto.
{% endhint %}

The program imports the keys, builds the script, signs the transaction and polls for its result.

```ts
import { PhantasmaAPI, Transaction } from "phantasma-sdk-ts/public";

const RPC = new PhantasmaAPI("https://testnet.phantasma.info/rpc", null, "testnet");

const delay = (ms: number) => new Promise((resolve) => setTimeout(resolve, ms));

/**
 * Send a transaction
 * @param transaction Transaction to send already signed
 */
async function SendATransaction(transaction: Transaction) {
  let transactionSignedBytes = transaction.toStringEncoded(true); // Get the transaction in bytes convert it to string
  let txHash = await RPC.sendRawTransaction(transactionSignedBytes); // Send the transaction to the network
  await delay(5000); // Wait 5 seconds or more
  let result = await RPC.getTransaction(txHash); // Get the result of the transaction
  return result;
}
```

***

{% hint style="info" %}
Check a full example how to transfer tokens
{% endhint %}

{% content-ref url="transfer-tokens.md" %}
[transfer-tokens.md](transfer-tokens.md)
{% endcontent-ref %}
