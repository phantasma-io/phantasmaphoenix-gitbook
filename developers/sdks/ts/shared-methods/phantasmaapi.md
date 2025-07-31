# ☁️ PhantasmaAPI

{% hint style="info" %}
Here's how to setup a simple connection to the Phantasma Blockchain API
{% endhint %}

The first thing to do is to create an instance of the **PhantasmaAPI.**

* It will receive as parameters, the **RPC URL,** the **Peers URL** or **undefined,** and the **Nexus Name**

### Testnet Configurations

* RPC URL -> https://testnet.phantasma.io/rpc
* Peers URL -> undefined
* Nexus Name -> testnet

It should look like this

```javascript
import { PhantasmaAPI } from 'phantasma-sdk-ts';
let phantasmaAPI = new PhantasmaAPI('https://testnet.phantasma.info/rpc', undefined as any, 'testnet');
```

### Mainnet Configurations

* RPC URL -> It can used anyone of this
  * [https://pharpc1.phantasma.info/rpc](https://pharpc1.phantasma.info/rpc)
  * [https://pharpc2.phantasma.info/rpc](https://pharpc2.phantasma.info/rpc)
* Peers URL -> [https://peers.phantasma.info/getpeers.json](https://peers.phantasma.info/getpeers.json)
* Nexus Name -> mainnet

It should look like this

```javascript
import { PhantasmaAPI } from 'phantasma-sdk-ts';
let phantasmaAPI = new PhantasmaAPI('https://pharpc1.phantasma.info/rpc', undefined as any, 'mainnet');
```
