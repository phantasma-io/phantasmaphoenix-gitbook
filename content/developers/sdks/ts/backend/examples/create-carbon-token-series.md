---
title: "Creation of New Carbon Token Series"
linkTitle: "Create New Carbon Token Series"
weight: 150
---

To create a new Carbon token series, you first need to obtain the Carbon token ID.
This ID is returned from the token creation transaction, and it can also be retrieved using the getToken RPC API call.

## Creating a New Carbon Token Series

The following code snippet demonstrates how to create a new Carbon token series.

### Imports

These are the imports typically required for creating a Carbon token series:

```ts
import {
  Bytes32,
  CreateTokenSeriesTxHelper,
  MetadataField,
  PhantasmaAPI,
  PhantasmaKeys,
  SeriesInfoBuilder,
  TokenSchemasBuilder,
} from "phantasma-sdk-ts/public";
import { getRandomPhantasmaId } from "phantasma-sdk-ts/types";
```

### Initialize Deployer Keys

In the following examples, we will use the deployer’s `PhantasmaKeys` keypair and its `Bytes32` public key.

```ts
  // Initialize PhantasmaKeys using WIF-encoded private key
  const txSender = PhantasmaKeys.fromWIF("YOUR_WIF");
  // Get the public key from the keypair
  const senderPubKey = new Bytes32(txSender.publicKey);
```

### Build Series Info

`SeriesInfoBuilder` helps construct the class describing the series being created.

`maxMint` and `maxSupply`, which are passed to `SeriesInfoBuilder.build()`, limit the number of NFTs that can be minted in the following way:
Each time you mint an NFT, both the mint and supply counters increase by one.
If you burn an NFT, the supply counter decreases by one.

For example:

* `maxMint = 20` → only 20 NFTs will ever be created.

* `maxMint = 0`, `maxSupply = 20` → minting can continue as long as there are fewer than 20 existing (non-burned) NFTs at the moment.

```ts
  const tokenSchemas = TokenSchemasBuilder.prepareStandard(true);
  const seriesSchema = tokenSchemas.seriesMetadata;

  // Metadata fields must match the series schema.
  const metadata: MetadataField[] = [
    { name: "name", value: "My Series" },
    { name: "description", value: "Series description" },
    { name: "imageURL", value: "https://example.com/cover.png" },
    { name: "infoURL", value: "https://example.com/info" },
    { name: "royalties", value: 10000000 },
  ];

  // First we need to generate a new random Phantasma ID for the new series.
  // Keep it: a deterministic mint names the series by this id.
  const newPhantasmaSeriesId = await getRandomPhantasmaId();

  const info = SeriesInfoBuilder.build(
    seriesSchema,
    newPhantasmaSeriesId,
    0, // maxMint
    0, // maxSupply
    senderPubKey, // Public key of the series creator
    metadata, // Series metadata (required; must match schema)
  );
```

### Build the Message

`CreateTokenSeriesTxHelper.buildTx` assembles the `Token.CreateTokenSeries`
call. The builder carries no prices, so the message leaves it with a zero gas
offer.

```ts
  const carbonTokenId = 123n; // CreateTokenTxHelper.parseResult(...)

  const msg = CreateTokenSeriesTxHelper.buildTx(
    carbonTokenId, // Carbon token ID to which the new series will be attached
    info, // SeriesInfo instance built with SeriesInfoBuilder
    senderPubKey, // Public key of the series creator, which pays the gas
  );
```

### Plan, Sign and Send

```ts
  const rpc = new PhantasmaAPI("https://testnet.phantasma.info/rpc", null, "testnet");

  const txHash = await rpc.sendTransaction(msg, txSender);
```

`sendTransaction` plans the fee from the message, signs it and broadcasts it. A
series creation carries one assumed fact, which is whether the series metadata
holds an `_i` id, so `plan.exact` reports whether the bill is a prediction or a
ceiling. See [Fees And Broadcasting](../../fees-and-broadcasting.md).

### Parse the Result

After the transaction is mined and its result is available, parse it to obtain the new Carbon series ID.
This ID can later be used to mint new NFTs.

```ts
  // Wait for transaction confirmation...
  const txInfo = await rpc.getTransaction(txHash);

  if (txInfo.state === "Halt") {
    const seriesId = CreateTokenSeriesTxHelper.parseResult(txInfo.result);
  } else {
    // Handle transaction failure
  }
```

> [!NOTE]
> If you already have schemas from RPC (`getToken`), convert them with `vmStructSchemaFromRpcResult`.
