# Get a Block by Height

```ts
import { PhantasmaAPI } from "phantasma-sdk-ts";

const CHAIN_NAME = "main"; // This is the name of the chain, please don't change it.
const NETWORK_API_URL = "https://testnet.phantasma.info/rpc"; // for mainnet this should be https://pharpc1.phantasma.info/rpc
const NETWORK_PEER_URL = undefined; // this the peers URL to get the list of peers, if not provided it will use the default one "https://peers.phantasma.info/"
const NEXUS_NAME = "testnet"; // For mainnet use this "mainnet"

const api = new PhantasmaAPI(
  NETWORK_API_URL,
  NETWORK_PEER_URL as any,
  NEXUS_NAME,
);

async function main() {
  const height = 999; // Here should be the block height that you're trying to get.
  const result = await api.getBlockByHeight(CHAIN_NAME, height);
  console.log({ result });
}

main().catch(console.error);
```
