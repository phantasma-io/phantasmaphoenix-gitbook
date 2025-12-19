# Creation of New Carbon Tokens

All Phantasma Phoenix tokens are built upon Carbon tokens at their core. Carbon tokens operate without the need for smart contracts - their metadata is stored within specialized hierarchical structures defined by schemas. These tokens are managed using low-level Carbon-level chain methods, which are purpose-built for speed and efficiency. Manipulating Carbon tokens requires no VM execution or scripting.

For more advanced scenarios, Phantasma Phoenix also provides Smart NFTs, which include attached smart contracts.

Both Carbon NFTs and Smart NFTs support infusion and all standard NFT operations - they are mintable, transferable, burnable, and tradable.

Carbon NFTs can be upgraded to Smart NFTs by embedding a TOMB (PhantasmaVM) contract within their Carbon metadata.

## Creating a New Carbon Token

The following code snippet demonstrates how to create a new Carbon token.

### Imports

These are the imports typically required for creating a Carbon token:

```ts
import {
  Bytes32,
  CreateTokenFeeOptions,
  CreateTokenTxHelper,
  IntX,
  PhantasmaAPI,
  PhantasmaKeys,
  TokenInfoBuilder,
  TokenMetadataBuilder,
  TokenSchemasBuilder,
} from "phantasma-sdk-ts";
````

### Initialize Deployer Keys

In the following examples, we will use the deployer’s `PhantasmaKeys` keypair and its `Bytes32` public key.

```ts
  // Initialize PhantasmaKeys using WIF-encoded private key
  const txSender = PhantasmaKeys.fromWIF("YOUR_WIF");
  // Get the public key from the keypair
  const senderPubKey = new Bytes32(txSender.PublicKey);
````

### Build Token Info

`TokenInfoBuilder` helps construct the class describing the token being deployed.

```ts
  const tokenSchemas = TokenSchemasBuilder.prepareStandard(true);

  const metadata = TokenMetadataBuilder.buildAndSerialize({
    name: "My NFT",
    description: "Example NFT",
    icon: "data:image/png;base64,...",
    url: "https://example.com",
  });

  const info = TokenInfoBuilder.build(
    "MYNFT", // New token symbol
    IntX.fromI64(0n), // Maximum token supply, or 0 for unlimited supply
    true, // Whether the token is non-fungible (NFT) or not (fungible). Currently, only NFTs are supported
    0, // Token decimals (always 0 for NFTs)
    senderPubKey, // Public key of the token creator
    metadata, // Optional metadata fields (key and value are strings only for now)
    tokenSchemas,
  );
````

### Set Token Creation Fees

`CreateTokenFeeOptions` is used to specify the fees for token creation.
You can call the constructor without arguments to use default values.

```ts
  const feeOptions = new CreateTokenFeeOptions(
    10000, // Base fee
    10000000000, // Create token base fee
    10000000000, // Create token symbol fee
    10000 // Fee multiplier
  );
````

### Build and Sign the Transaction

`CreateTokenTxHelper` simplifies the process of building and signing the token creation transaction.

```ts
  const maxData = 1_000_000_000n;
  const tx = CreateTokenTxHelper.buildTxAndSignHex(
    info, // TokenInfo instance built with TokenInfoBuilder
    txSender, // Keypair used to sign the transaction
    feeOptions, // Fee options defined above
    maxData // Create token max data (use this default value if unsure)
  );
````

### Broadcast the Transaction

Broadcast the transaction to the network.

```ts
  const rpc = new PhantasmaAPI("https://testnet.phantasma.info/rpc", undefined as any, "testnet");

  // Use sendCarbonTransaction() to call Carbon methods
  const txHash = await rpc.sendCarbonTransaction(tx);
````

### Parse the Result

After the transaction is mined and its result is available, parse it to obtain the new Carbon token ID.
This ID can later be used to create token series and mint new NFTs.

```ts
  // Wait for transaction confirmation...
  const txInfo = await rpc.getTransaction(txHash);

  if (txInfo.state === "Halt") {
    const tokenId = CreateTokenTxHelper.parseResult(txInfo.result);
  } else {
    // Handle transaction failure
  }
```

{% hint style="info" %}
For frontend signing, build a `TxMsg` via `CreateTokenTxHelper.buildTx(...)` and use `PhantasmaLink.signCarbonTxAndBroadcast` or `EasyConnect.signCarbonTransaction`.
{% endhint %}
