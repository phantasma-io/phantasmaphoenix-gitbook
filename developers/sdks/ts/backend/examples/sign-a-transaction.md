# Sign a Transaction

{% hint style="info" %}
Here's a simple example how to sign a transaction
{% endhint %}

```ts
import { PhantasmaKeys, Transaction } from "phantasma-sdk-ts";

function SignATransaction(transaction: Transaction) {
  let wif = "";
  let keys = PhantasmaKeys.fromWIF(wif);
  transaction.signWithKeys(keys);
  return transaction;
}
```
