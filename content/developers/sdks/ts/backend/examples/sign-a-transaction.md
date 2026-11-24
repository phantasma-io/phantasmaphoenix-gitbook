---
title: "Sign a Transaction"
weight: 120
---

> [!NOTE]
> Signing a transaction locally with a key pair.

```ts
import { PhantasmaKeys, Transaction } from "phantasma-sdk-ts/public";

function SignATransaction(transaction: Transaction) {
  let wif = "";
  let keys = PhantasmaKeys.fromWIF(wif);
  transaction.signWithKeys(keys);
  return transaction;
}
```
