# Importing a Wallet

{% hint style="info" %}
You can get the WIF, on your wallet, Poltergeist or Ecto.
{% endhint %}

### Import Wallet

Small example of how to get the **address** from the **WIF**.

{% hint style="info" %}
This is used to sign transaction, that's why you need this if you're running your backend service.
{% endhint %}

```javascript
import { Address, PhantasmaKeys } from "phantasma-sdk-ts";
const wif = "L2osWF9ouySfmkSUNuPVSReHvtWuf1xkMLdeJBPVf57Zvz8vGSuE"; // replace with your WIF
const wallet = PhantasmaKeys.fromWIF(wif);

const addr = wallet.Address; // Get the Address.
```



### Importing a Wallet from a private key

Small example of how to import a wallet from a **private key**.

```typescript
import { Address, PhantasmaKeys, getWifFromPrivateKey} from "phantasma-sdk-ts"
const privateKey = "a6c2b2b883562e558803a23c4137daf6bbf747f23a66034e882e0cfe31ca66f8";
let wif = getWifFromPrivateKey(privateKey);
const wallet = PhantasmaKeys.fromWIF(wif);

const addr = wallet.Address; // Get the Address.
console.log(`${addr}`)
```



{% hint style="info" %}
You can also get the **private key** from the **WIF**
{% endhint %}

```typescript
import { Address, PhantasmaKeys, getPrivateKeyFromWif } from "phantasma-sdk-ts";
const wif = "L2osWF9ouySfmkSUNuPVSReHvtWuf1xkMLdeJBPVf57Zvz8vGSuE";
const privKey = getPrivateKeyFromWif(wif);
```
