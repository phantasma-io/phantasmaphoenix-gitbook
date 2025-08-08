# Get User Balances

{% hint style="info" %}
Don't forget that this can also be used to the all of the account information.

**On line 15** it's possible to just return the account.
{% endhint %}

In this example show's how to get the User Balance.

```ts
import {PhantasmaAPI, Balance} from 'phantasma-sdk-ts';
const CHAIN_NAME = "main"; // This is the name of the chain, please don't change it.
const NETWORK_API_URL = "https://testnet.phantasma.info/rpc";
const NETWORK_PEER_URL = undefined; // this the peers URL to get the list of peers, if not provided it will use the default one "https://peers.phantasma.info/"
const NEXUS_NAME = "testnet"; // For mainnet use this "mainnet"
const API = new PhantasmaAPI(NETWORK_API_URL, NETWORK_PEER_URL as any, NEXUS_NAME );

/**
 * Get the user balance
 * @param address Address of the account you want to get the balance
 * @returns 
 */
async function GetUserBalance(address: string) : Promise<Balance[]> {
  let account = await API.getAccount(address);
  return account.balances;
}

```
