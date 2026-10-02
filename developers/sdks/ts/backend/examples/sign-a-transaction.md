# Sign a Transaction

{% hint style="info" %}
Signing a transaction locally with a key pair.
{% endhint %}

```ts
import { PhantasmaKeys, Transaction } from "phantasma-sdk-ts/public";

function SignATransaction(transaction: Transaction) {
  let wif = "";
  let keys = PhantasmaKeys.fromWIF(wif);
  transaction.signWithKeys(keys);
  return transaction;
}
```
