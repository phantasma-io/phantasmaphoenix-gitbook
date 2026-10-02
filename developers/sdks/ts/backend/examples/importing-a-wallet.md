# Importing a Wallet

{% hint style="info" %}
Export the WIF from your wallet (Poltergeist Lite or Ecto).
{% endhint %}

### Import Wallet

Derive the address from the WIF.

{% hint style="info" %}
A backend service that signs transactions loads its keys this way.
{% endhint %}

```ts
import { PhantasmaKeys } from "phantasma-sdk-ts/public";

const wif = "YOUR_WIF"; // replace with your WIF
const wallet = PhantasmaKeys.fromWIF(wif);

const address = wallet.address.text; // Get the Address.
```

### Importing a Wallet from a private key

Import a wallet from a private key.

```ts
import { PhantasmaKeys, getWifFromPrivateKey } from "phantasma-sdk-ts/public";

const privateKey = "YOUR_PRIVATE_KEY_HEX";
const wif = getWifFromPrivateKey(privateKey);
const wallet = PhantasmaKeys.fromWIF(wif);

const address = wallet.address.text; // Get the Address.
console.log(`${address}`);
```

{% hint style="info" %}
The private key can be read back from the WIF
{% endhint %}

```ts
import { getPrivateKeyFromWif } from "phantasma-sdk-ts/public";

const wif = "YOUR_WIF";
const privKey = getPrivateKeyFromWif(wif);
```
