# Creation of new carbon tokens

All Phantasma Phoenix tokens are built upon Carbon tokens at their core. Carbon tokens operate without the need for smart contracts - their metadata is stored within specialized hierarchical structures defined by schemas. These tokens are managed using low-level Carbon-level chain methods, which are purpose-built for speed and efficiency. Manipulating Carbon tokens requires no VM execution or scripting.

For more advanced scenarios, Phantasma Phoenix also provides Smart NFTs, which include attached smart contracts.

Both Carbon NFTs and Smart NFTs support infusion and all standard NFT operations - they are mintable, transferable, burnable, and tradable.

Following code snippet shows how to create a new carbon token.

These are imports which are usually required for creating a carbon token.

```ts
import {
  Bytes32,
  CarbonBlob,
  CreateTokenFeeOptions,
  CreateTokenTxHelper,
  IntX,
  SignedTxMsg,
  PhantasmaAPI,
  PhantasmaKeys,
  TokenInfoBuilder,
  TokenMetadataBuilder,
} from "phantasma-sdk-ts";
````

Also in the following code snippets we will use deployer's PhantasmaKeys keypair and Bytes32 public key.

```ts
  // Initialize PhantasmaKeys using WIF-encoded private key
  const txSender = PhantasmaKeys.fromWIF("KwPpBSByydVKqStGHAnZzQofCqhDmD2bfRgc9BmZqM3ZmsdWJw4d");
  // Get public key from keypair
  const senderPubKey = new Bytes32(txSender.PublicKey);
````

TokenInfoBuilder helps us build special class describing token being deployed.

```ts
  const info = TokenInfoBuilder.build(
    "MYNFT", // New token symbol
    IntX.fromI64(0n), // Maximum token supply or 0 for unlimited supply
    true, // If token is non-fungible (NFT) or not (fungible). Right now only NFTs are supported
    0, // Token decimals (for NFTs always 0)
    senderPubKey, // Public key of the token creator
    TokenMetadataBuilder.buildAndSerialize(cfg.tokenMetadataFields), // Map with optional metadata fields (key and value are strings only right now - SDK will be improved in the future to support more types)
  );
````

CreateTokenFeeOptions class is used to specify the fees for creating a token. You can call constructor without passing any arguments to use default values.

```ts
  const feeOptions = new CreateTokenFeeOptions(
    10000, // base fee
    10000000000, // Create token base fee
    10000000000, // Create token symbol fee
    10000 // Fee multiplier
  );
````

CreateTokenTxHelper helper simplifies the process of creating a transaction for creating a token.

```ts
  const tx = CreateTokenTxHelper.buildTxAndSignHex(
    info, // TokenInfo class generated with TokenInfoBuilder.build()
    txSender, // Keypair of the token creator used to sign the transaction
    feeOptions, // Fee options shown in code snippet above
    1000000000 // Create token max data (use this default value if in doubt)
  );
````

Broadcast transaction to the network.

```ts
  const rpc = new PhantasmaAPI("https://testnet.phantasma.info/rpc", null, cfg.nexus);

  const txHash = await rpc.sendCarbonTransaction(tx);
````

After waiting for transaction to be mined and receiving it's result, in case of success, parse the result to get the new carbon token ID. This ID can be used to create new token series and to mint new NFTs.

```ts
  ... wait for tx

  if (success) {
    const tokenId = CreateTokenTxHelper.parseResult(result);
  } else {
  }
}
```
