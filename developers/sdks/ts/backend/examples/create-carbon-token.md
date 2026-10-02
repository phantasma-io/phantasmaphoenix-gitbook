# Creation of New Carbon Tokens

{% hint style="info" %}
For a non-technical overview of Carbon and SmartNFTs, see [Carbon: Native Assets on Phantasma Phoenix](/about/carbon.md).
{% endhint %}

This page focuses on the technical steps to create a Carbon token.

## Creating a New Carbon Token

The following code snippet demonstrates how to create a new Carbon token.

### Imports

These are the imports typically required for creating a Carbon token:

```ts
import {
  Bytes32,
  CreateTokenTxHelper,
  IntX,
  PhantasmaAPI,
  PhantasmaKeys,
  summarizeFeePlan,
  TokenInfoBuilder,
  TokenMetadataBuilder,
  TokenSchemasBuilder,
} from "phantasma-sdk-ts/public";
```

### Initialize Deployer Keys

In the following examples, we will use the deployer’s `PhantasmaKeys` keypair and its `Bytes32` public key.

```ts
  // Initialize PhantasmaKeys using WIF-encoded private key
  const txSender = PhantasmaKeys.fromWIF("YOUR_WIF");
  // Get the public key from the keypair
  const senderPubKey = new Bytes32(txSender.publicKey);
```

### Build Token Info

`TokenInfoBuilder` helps construct the class describing the token being deployed.

```ts
  const tokenSchemas = TokenSchemasBuilder.prepareStandard(true);

  const metadata = TokenMetadataBuilder.buildAndSerialize({
    name: "My NFT",
    description: "Example NFT",
    icon: "data:image/png;base64,iVBORw0KGgo=",
    url: "https://example.com",
  });

  const info = TokenInfoBuilder.build(
    "MYNFT", // New token symbol
    IntX.fromI64(0n), // Maximum token supply, or 0 for unlimited supply
    true, // true for an NFT token, false for a fungible token
    0, // Token decimals (always 0 for NFTs)
    senderPubKey, // Public key of the token creator
    metadata, // Token metadata (required for all tokens; values are strings)
    tokenSchemas,
  );
```

### Build the Message

`CreateTokenTxHelper.buildTx` assembles the `Token.CreateToken` call. The
builder carries no prices, so the message leaves it with a zero gas offer.

```ts
  const msg = CreateTokenTxHelper.buildTx(
    info, // TokenInfo instance built with TokenInfoBuilder
    senderPubKey, // Public key of the token creator, which pays the gas
  );
```

### Plan, Sign and Send

`sendTransaction` runs the four steps in one call: the symbol pre-flight, the
fee plan, the signatures and the broadcast.

```ts
  const rpc = new PhantasmaAPI("https://testnet.phantasma.info/rpc", null, "testnet");

  const txHash = await rpc.sendTransaction(msg, txSender);
```

To see the fee before sending, plan it first:

```ts
  const plan = await rpc.fees.plan(msg);
  console.log(summarizeFeePlan(plan)); // gasBill, gasOffer, storageCeiling

  const txHash = await rpc.sendTransaction(plan.apply(msg), txSender);
```

{% hint style="warning" %}
`Token.CreateToken` pays its base policy fee before the contract looks at the symbol,
and that fee is the largest single price in the protocol. A symbol that is
already taken costs the fee and returns nothing. `sendTransaction` asks the
chain first and refuses to send when the symbol is taken, or when the lookup
established nothing. Pass `{ preflight: false }` to decide for yourself.
{% endhint %}

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
For frontend signing, build the `TxMsg` the same way, plan it with
`rpc.fees.plan(msg)`, apply the plan, and pass the result to
`PhantasmaLink.signCarbonTxAndBroadcast` or `EasyConnect.signCarbonTransaction`.
{% endhint %}
