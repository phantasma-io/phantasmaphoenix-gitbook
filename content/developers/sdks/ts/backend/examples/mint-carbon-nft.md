---
title: "Minting a New Carbon NFT"
linkTitle: "Mint New Carbon NFT"
weight: 160
---

To mint a new Carbon NFT you need the Carbon token ID and the Phantasma series
ID. The token ID is returned by the token creation transaction. The series ID is
the one you generated when the series was created.

The chain derives the NFT id and stores a canonical ROM. One call mints one or
more instances.

## Minting a New Carbon NFT

The following code snippet demonstrates how to mint a new Carbon NFT.

### Imports

These are the imports typically required for minting a Carbon NFT:

```ts
import {
  Bytes32,
  IntX,
  MetadataField,
  MintPhantasmaNonFungibleTxHelper,
  PhantasmaAPI,
  PhantasmaKeys,
  PhantasmaNftMintInfo,
  PhantasmaNftRomBuilder,
  TokenSchemasBuilder,
} from "phantasma-sdk-ts/public";
```

### Initialize Deployer Keys

In the following examples, we will use the deployer's `PhantasmaKeys` keypair and its `Bytes32` public key.

```ts
  // Initialize PhantasmaKeys using WIF-encoded private key
  const txSender = PhantasmaKeys.fromWIF("YOUR_WIF");
  // Get the public key from the keypair
  const senderPubKey = new Bytes32(txSender.publicKey);
```

### Build NFT ROM

`PhantasmaNftRomBuilder` serializes the public part of the ROM. The chain owns
the `_i` id and the `rom` bytes for a deterministic mint, so those two field
names are refused here.

Use the ROM schema the token was created with. The example continues from a
token created with `prepareStandard(false)`, which puts the standard fields in
the per-NFT ROM.

```ts
  const tokenSchemas = TokenSchemasBuilder.prepareStandard(false);
  const romSchema = tokenSchemas.rom; // use the schema from your token

  // Include only fields defined in romSchema.
  const metadata: MetadataField[] = [
    { name: "name", value: "NFT #1" }, // NFT name
    { name: "description", value: "Example mint" }, // NFT description
    { name: "imageURL", value: "https://example.com/nft.png" }, // NFT image URL (or IPFS URL)
    { name: "infoURL", value: "https://example.com/nft" }, // NFT information URL
    { name: "royalties", value: 10000000 }, // NFT royalties. 10000000 = 1%
  ];

  const rom = PhantasmaNftRomBuilder.buildAndSerialize(romSchema, metadata);
```

### Build the Message

Every instance is one entry in `tokens`. Instances of several series may share
one call.

```ts
  const carbonTokenId = 123n; // CreateTokenTxHelper.parseResult(...)
  const phantasmaSeriesId = 456n; // the id used when the series was created

  const msg = MintPhantasmaNonFungibleTxHelper.buildTx({
    tokenId: carbonTokenId,
    sender: senderPubKey, // pays the gas and signs
    to: senderPubKey, // receives every instance this call mints
    tokens: [
      new PhantasmaNftMintInfo({
        phantasmaSeriesId: IntX.fromBigInt(phantasmaSeriesId),
        rom, // ROM produced by PhantasmaNftRomBuilder
        ram: new Uint8Array(), // NFT RAM, optional
      }),
    ],
  });
```

### Plan, Sign and Send

```ts
  const rpc = new PhantasmaAPI("https://testnet.phantasma.info/rpc", null, "testnet");

  const txHash = await rpc.sendTransaction(msg, txSender);
```

A mint prices three facts the message does not carry: whether the recipient
already holds the token, whether the supply row still exists, and whether the
series mints duplicates. Each is taken at the reading that costs more, so
`plan.exact` is `false` unless you state them. See
[Fees And Broadcasting](../../fees-and-broadcasting.md).

### Parse the Result

After the transaction is mined and its result becomes available, parse it to
obtain the minted instances. Each entry carries the Phantasma NFT id the chain
derived and the Carbon instance id it minted.

```ts
  // Wait for transaction confirmation...
  const txInfo = await rpc.getTransaction(txHash);

  if (txInfo.state === "Halt") {
    const minted = MintPhantasmaNonFungibleTxHelper.parseResult(txInfo.result);
    console.log(
      `Minted NFT with phantasma ID ${minted[0].phantasmaNftId.toHex()} ` +
        `and carbon instance ID ${minted[0].carbonInstanceId}`
    );
  } else {
    console.log("Could not mint NFT");
  }
```
