---
title: "Importing a Wallet"
weight: 90
---

> [!NOTE]
> Export the WIF from your wallet (Poltergeist Lite or Ecto).

### Import Wallet

Derive the address from the WIF.

> [!NOTE]
> A backend service that signs transactions loads its keys this way.

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

> [!NOTE]
> The private key can be read back from the WIF

```ts
import { getPrivateKeyFromWif } from "phantasma-sdk-ts/public";

const wif = "YOUR_WIF";
const privKey = getPrivateKeyFromWif(wif);
```
