---
description: >-
  Here's an small example how to send a transaction using NodeJS for the
  backend.
---

# Send a Transaction

{% hint style="info" %}
Don't forget to import the WIF, you can the wif by exporting it from Poltergeist or Ecto Wallet.
{% endhint %}

Here's how to import the wallet keys.

Here we'll create the script that will be sending the transaction.

```ts
/**
 * Send a transaction
 * @param transaction Transaction to send already signed
 */
async function SendATransaction(transaction: Transaction){
  let transactionSignedBytes = transaction.toString(true); // Get the transaction in bytes convert it to string
  let txHash = await RPC.sendRawTransaction(transactionSignedBytes); // Send the transaction to the network
  await delay(5000); // Wait 5 seconds or more 
  let result = await GetATransaction(txHash); // Get the result of the transaction
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
