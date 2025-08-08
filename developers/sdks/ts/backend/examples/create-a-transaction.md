# Create a Transaction

### Creating a Transaction

This how to create a transaction.

```ts
import {Base16, PhantasmaKeys, Transaction} from 'phantasma-sdk-ts';
const NexusName = "testnet"; // Could also be simnet or mainnet
const ChainName = "main"; // Since we only have the main chain, it's always main.
let payload = Base16.encode("Phantasma-NodeJS"); // This is what going to appear on the explorer and on the wallet.
let script = "YOUR_SCRIPT_HERE";
let expiration: Date = new Date(Date.UTC(
 new Date().getUTCFullYear(),
 new Date().getUTCMonth(),
 new Date().getUTCDate(),
 new Date().getUTCHours() + 1,
 new Date().getUTCMinutes() + 10,
 new Date().getUTCSeconds() + 10
));

let transaction = new Transaction(
 NexusName,  //Nexus Name
 ChainName,     //Chain
 script,     //In string format
 expiration, //Date Object
 payload     //Extra Info to attach to Transaction in Serialized Hex
);
```

### Sign a Transaction

Now we need to sign the transaction if we want it to be accepted by the blockchain.

```ts
let wif = "L2i7rHp9WBhGMq4CRepsntA5WuMfUjPeHi4krf9njTxVsYhRgHyD"; // REPLACE with WIF of your wallet 
let keys = PhantasmaKeys.fromWIF(wif);

transaction.signWithKeys(keys);
let transactionSignedBytes = transaction.toString(true); 
```
