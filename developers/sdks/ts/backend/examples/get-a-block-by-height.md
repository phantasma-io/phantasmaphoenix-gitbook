# Get a Block by Height

This is a simple example how to the **Block** by **Height**

```typescript
import { PhantasmaAPI, Transaction, Block } from "phantasma-ts";

const CHAIN_NAME = "main"; // This is the name of the chain, please don't change it.
const NETWORK_API_URL = "https://testnet.phantasma.io/rpc"; // for mainnet this should be https://pharpc1.phantasma.io/rpc
const NETWORK_PEER_URL = undefined; // this the peers URL to get the list of peers, if not provided it will use the default one "https://peers.phantasma.io/"
const NEXUS_NAME = "testnet"; // For mainnet use this "mainnet"
const API = new PhantasmaAPI(
  NETWORK_API_URL, 
  NETWORK_PEER_URL, 
  NEXUS_NAME 
);

let height = 999; // Here should be the block height that you're trying to get.
let result = await API.GetBlockByHeight(CHAIN_NAME, height);
console.log({ result });
```
