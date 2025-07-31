# Get data from new Blocks

This shows how to get a program to go **block** by block until it finds a event that we want.

It's possible to add more **validation**, such as check for the **address**, the **symbol** that was **received** etc.

```typescript
import { PhantasmaAPI, Transaction, Block, getTokenEventData } from "phantasma-ts";

const CHAIN_NAME = "main"; // This is the name of the chain, please don't change it.
const NETWORK_API_URL = "https://testnet.phantasma.io/rpc"; // for mainnet this should be https://pharpc1.phantasma.io/rpc
const NETWORK_PEER_URL = undefined; // this the peers URL to get the list of peers, if not provided it will use the default one "https://peers.phantasma.io/"
const NEXUS_NAME = "testnet"; // For mainnet use this "mainnet"
const API = new PhantasmaAPI(
  NETWORK_API_URL, 
  NETWORK_PEER_URL, 
  NEXUS_NAME 
);

/**
 * On Transaction Received
 * @param address User that received
 * @param symbol Symbol received
 * @param amount Amount of the symbol received
 */
function onTransactionReceived(address, symbol, amount) {}

// Function that periodically checks the height of the chain and fetches the latest block if the height has increased
async function CheckForNewBlocks() {
  // Get the current height of the chain
  let newHeight = await API.getBlockHeight(CHAIN_NAME);
  let currentHeight = newHeight;

  // Check if the height has increased
  if (newHeight > currentHeight) {
    // Fetch the latest block
    let latestBlock = await API.getBlockByHeight(CHAIN_NAME, newHeight);

    // Check all transactions in this block
    for (let i = 0; i < latestBlock.txs.length; i++) {
      let tx = latestBlock.txs[i];

      // Check all events in this transaction
      for (let j = 0; j < tx.events.length; j++) {
        let evt = tx.events[j];
        if (evt.kind == "TokenReceive") {
          var data = getTokenEventData(evt.data);
          onTransactionReceived(evt.address, data.symbol, data.value);
        }
      }
    }

    // Update the current height of the chain
    currentHeight = newHeight;
  }

  // Repeat this process after a delay
  setTimeout(CheckForNewBlocks, 1000);
}
```
