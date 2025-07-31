# Get a Transaction



## How to get a transaction

Here is a small example on how to get a transaction by the transaction hash.

```typescript
import { PhantasmaAPI, Transaction } from "phantasma-ts";

const CHAIN_NAME = "main"; // This is the name of the chain, please don't change it.
const NETWORK_API_URL = "https://testnet.phantasma.io/rpc"; // for mainnet this should be https://pharpc1.phantasma.io/rpc
const NETWORK_PEER_URL = undefined; // this the peers URL to get the list of peers, if not provided it will use the default one "https://peers.phantasma.io/"
const NEXUS_NAME = "testnet"; // For mainnet use this "mainnet"
const API = new PhantasmaAPI(
  NETWORK_API_URL, 
  NETWORK_PEER_URL, 
  NEXUS_NAME 
);

let txHash = ""; // Here should be the transaction hash
let result = await API.getTransaction(txHash);
console.log({ result });
```
