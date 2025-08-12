# Creating a new Address

This is just a simple way to create a new wallet.

```ts
import {  PhantasmaKeys } from 'phantasma-sdk-ts';

const wallet = PhantasmaKeys.generate(); // This will generate a new wallet / WIF.
console.log(`Address: ${wallet.Address}`);
console.log(`Private (WIF): ${wallet.toWIF()}`);
console.log(`Private (HEX): ${Base16.encode(wallet.PrivateKey.toString())}`);
console.log(`Public  (HEX): ${Base16.encode(wallet.PublicKey.toString())}`);
```

