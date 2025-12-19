# Get data from new Blocks

This shows how to get a program to go **block** by block until it finds a event that we want.

It's possible to add more **validation**, such as check for the **address**, the **symbol** that was **received** etc.

```ts
import { PhantasmaAPI, getTokenEventData } from "phantasma-sdk-ts";

const CHAIN_NAME = "main"; // This is the name of the chain, please don't change it.
const NETWORK_API_URL = "https://testnet.phantasma.info/rpc"; // for mainnet this should be https://pharpc1.phantasma.info/rpc
const NETWORK_PEER_URL = undefined; // this the peers URL to get the list of peers, if not provided it will use the default one "https://peers.phantasma.info/"
const NEXUS_NAME = "testnet"; // For mainnet use this "mainnet"

const api = new PhantasmaAPI(
  NETWORK_API_URL,
  NETWORK_PEER_URL as any,
  NEXUS_NAME,
);

/**
 * On Transaction Received
 * @param address User that received
 * @param symbol Symbol received
 * @param amount Amount of the symbol received
 */
function onTransactionReceived(address: string, symbol: string, amount: string) {
  console.log("Token received:", { address, symbol, amount });
}

// Function that periodically checks the height of the chain and fetches the latest block if the height has increased
async function checkForNewBlocks(currentHeight: number): Promise<number> {
  // Get the current height of the chain
  const latestHeight = await api.getBlockHeight(CHAIN_NAME);

  // Check if the height has increased
  if (latestHeight > currentHeight) {
    // Fetch the latest block
    const latestBlock = await api.getBlockByHeight(CHAIN_NAME, latestHeight);

    // Check all transactions in this block
    for (const tx of latestBlock.txs) {
      // Check all events in this transaction
      for (const evt of tx.events) {
        if (evt.kind === "TokenReceive") {
          const data = getTokenEventData(evt.data);
          onTransactionReceived(evt.address, data.symbol, data.value.toString());
        }
      }
    }

    // Update the current height of the chain
    return latestHeight;
  }

  return currentHeight;
}

async function startPolling() {
  let currentHeight = await api.getBlockHeight(CHAIN_NAME);

  const tick = async () => {
    try {
      currentHeight = await checkForNewBlocks(currentHeight);
    } catch (error) {
      console.error("Polling error:", error);
    }
    // Repeat this process after a delay
    setTimeout(tick, 1000);
  };

  tick();
}

startPolling().catch(console.error);
```
