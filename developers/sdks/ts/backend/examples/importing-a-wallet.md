# Importing a Wallet

{% hint style="info" %}
You can get the WIF, on your wallet, Poltergeist or Ecto.
{% endhint %}

### Import Wallet

Small example of how to get the **address** from the **WIF**.

{% hint style="info" %}
This is used to sign transaction, that's why you need this if you're running your backend service.
{% endhint %}

```ts
import { PhantasmaKeys } from "phantasma-sdk-ts";

const wif = "YOUR_WIF"; // replace with your WIF
const wallet = PhantasmaKeys.fromWIF(wif);

const address = wallet.Address.Text; // Get the Address.
```

### Importing a Wallet from a private key

Small example of how to import a wallet from a **private key**.

```ts
import { PhantasmaKeys, getWifFromPrivateKey } from "phantasma-sdk-ts";

const privateKey = "YOUR_PRIVATE_KEY_HEX";
const wif = getWifFromPrivateKey(privateKey);
const wallet = PhantasmaKeys.fromWIF(wif);

const address = wallet.Address.Text; // Get the Address.
console.log(`${address}`);
```

{% hint style="info" %}
You can also get the **private key** from the **WIF**
{% endhint %}

```ts
import { getPrivateKeyFromWif } from "phantasma-sdk-ts";

const wif = "YOUR_WIF";
const privKey = getPrivateKeyFromWif(wif);
```
