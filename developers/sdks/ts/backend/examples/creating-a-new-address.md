# Creating a new Address

This is just a simple way to create a new wallet.

```ts
import { Base16, PhantasmaKeys } from "phantasma-sdk-ts";

const wallet = PhantasmaKeys.generate(); // This will generate a new wallet / WIF.

console.log(`Address: ${wallet.Address.Text}`);
console.log(`Private (WIF): ${wallet.toWIF()}`);
console.log(`Private (HEX): ${Base16.encodeUint8Array(wallet.PrivateKey)}`);
console.log(`Public  (HEX): ${Base16.encodeUint8Array(wallet.PublicKey)}`);
```
