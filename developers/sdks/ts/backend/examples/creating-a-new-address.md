# Creating a new Address

This is just a simple way to create a new wallet.

```ts
import { bytesToHex, PhantasmaKeys } from "phantasma-sdk-ts";

const wallet = PhantasmaKeys.generate(); // This will generate a new wallet / WIF.

console.log(`Address: ${wallet.Address.Text}`);
console.log(`Private (WIF): ${wallet.toWIF()}`);
console.log(`Private (HEX): ${bytesToHex(wallet.PrivateKey)}`);
console.log(`Public  (HEX): ${bytesToHex(wallet.PublicKey)}`);
```
