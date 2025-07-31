# Creating a new Address

This is just a simple way to create a new wallet.

```javascript
import {  PhantasmaKeys } from 'phantasma-sdk-ts';

const wallet = PhantasmaKeys.generate(); // This will generate a new wallet / WIF.
const walletAddres = wallet.Address;
console.log(`${walletAddres}`);
```

