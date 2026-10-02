# Creating a new Address

Generates a new key pair and prints its address.

```ts
import { bytesToHex, PhantasmaKeys } from "phantasma-sdk-ts/public";

const wallet = PhantasmaKeys.generate(); // This will generate a new wallet / WIF.

console.log(`Address: ${wallet.address.text}`);
console.log(`Private (WIF): ${wallet.toWIF()}`);
console.log(`Private (HEX): ${bytesToHex(wallet.privateKey)}`);
console.log(`Public  (HEX): ${bytesToHex(wallet.publicKey)}`);
```
