# Creation of New Carbon Token Series

To create a new Carbon token series, you first need to obtain the Carbon token ID.
This ID is returned from the token creation transaction, and it can also be retrieved using the getToken RPC API call.

## Creating a New Carbon Token Series

The following code snippet demonstrates how to create a new Carbon token series.

### Imports

These are the imports typically required for creating a Carbon token series:

```ts
import {
  Bytes32,
  CreateSeriesFeeOptions,
  CreateTokenSeriesTxHelper,
  getRandomPhantasmaId,
  SeriesInfoBuilder,
  PhantasmaAPI,
  PhantasmaKeys,
} from "phantasma-sdk-ts";
````

### Initialize Deployer Keys

In the following examples, we will use the deployer’s `PhantasmaKeys` keypair and its `Bytes32` public key.

```ts
  // Initialize PhantasmaKeys using WIF-encoded private key
  const txSender = PhantasmaKeys.fromWIF("KwPpBSByydVKqStGHAnZzQofCqhDmD2bfRgc9BmZqM3ZmsdWJw4d");
  // Get the public key from the keypair
  const senderPubKey = new Bytes32(txSender.PublicKey);
````

### Build Series Info

`SeriesInfoBuilder` helps construct the class describing the series being created.

`maxMint` and `maxSupply`, which are passed to `SeriesInfoBuilder.build()`, limit the number of NFTs that can be minted in the following way:
Each time you mint an NFT, both the mint and supply counters increase by one.
If you burn an NFT, the supply counter decreases by one.

For example:

* `maxMint = 20` → only 20 NFTs will ever be created.

* `maxMint = 0`, `maxSupply = 20` → minting can continue as long as there are fewer than 20 existing (non-burned) NFTs at the moment.

```ts
  // First we need to generate a new random Phantasma ID for the new series
  const newPhantasmaSeriesId = await getRandomPhantasmaId();

  const info = SeriesInfoBuilder.build(
    newPhantasmaSeriesId,
    0, // maxMint
    0, // maxSupply
    senderPubKey, // Public key of the series creator
    new Uint8Array(), // Optional metadata shared by all NFTs in the series
  );
````

### Set Series Creation Fees

`CreateSeriesFeeOptions` is used to specify the fees for series creation.
You can call the constructor without arguments to use default values.

```ts
  const feeOptions = new CreateSeriesFeeOptions(
    10000, // Base fee
    2500000000, // Create series fee
    10000 // Fee multiplier
  );
````

### Build and Sign the Transaction

`CreateTokenSeriesTxHelper` simplifies the process of building and signing the series creation transaction.

```ts
  const tx = CreateTokenSeriesTxHelper.buildTxAndSignHex(
    carbonTokenId, // Carbon token ID to which the new series will be attached
    info, // SeriesInfo instance built with SeriesInfoBuilder
    txSender, // Keypair used to sign the transaction
    feeOptions, // Fee options defined above
    100000000, // Create series max data (use this default value if unsure)
  );
````

### Broadcast the Transaction

Broadcast the transaction to the network.

```ts
  const rpc = new PhantasmaAPI("https://testnet.phantasma.info/rpc", null, "testnet");

  // Use sendCarbonTransaction() to call Carbon methods
  const txHash = await rpc.sendCarbonTransaction(tx);
````

### Parse the Result

After the transaction is mined and its result is available, parse it to obtain the new Carbon series ID.
This ID can later be used to mint new NFTs.

```ts
  // Wait for transaction confirmation...

  if (success) {
    const seriesId = CreateTokenSeriesTxHelper.parseResult(result);
  } else {
    // Handle transaction failure
  }
```
