# Carbon Workflows

Carbon tokens are native, VM-less assets. For NFTs, Carbon provides fast token creation, series creation, and minting using specialized chain calls.

## Prerequisites

- Symbol must be uppercase A-Z (for example `MYNFT`).
- Token metadata is required and must include `name`, `icon`, `url`, `description`.
- `icon` must be a base64 data URI (PNG/JPEG/SVG).
- NFT tokens require schemas (series, ROM, RAM) via `TokenSchemasBuilder`.

{% hint style="info" %}
If you fetch schemas from RPC (`getToken`), convert them using `vmStructSchemaFromRpcResult` before passing to builders.
{% endhint %}

## 1) Create a Carbon Token (NFT)

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

async function main() {
  const keys = PhantasmaKeys.fromWIF("YOUR_WIF");
  const creatorPk = new Bytes32(keys.PublicKey);

  const tokenSchemas = TokenSchemasBuilder.prepareStandard(true);

  const metadata = TokenMetadataBuilder.buildAndSerialize({
    name: "My NFT",
    description: "Example NFT",
    icon: "data:image/png;base64,...",
    url: "https://example.com",
  });

  const tokenInfo = TokenInfoBuilder.build(
    "MYNFT",
    IntX.fromBigInt(0n),
    true,
    0,
    creatorPk,
    metadata,
    tokenSchemas,
  );

  const feeOptions = new CreateTokenFeeOptions();
  const maxData = 1_000_000_000n;

  const txHex = CreateTokenTxHelper.buildTxAndSignHex(
    tokenInfo,
    keys,
    feeOptions,
    maxData,
  );

  const rpc = new PhantasmaAPI("https://testnet.phantasma.info/rpc", undefined as any, "testnet");
  const txHash = await rpc.sendCarbonTransaction(txHex);

  const txInfo = await rpc.getTransaction(txHash);
  const carbonTokenId = BigInt(CreateTokenTxHelper.parseResult(txInfo.result));
  console.log("Carbon token id:", carbonTokenId.toString());
}

main().catch(console.error);
```

## 2) Create a Token Series

```ts
import {
  Bytes32,
  CreateSeriesFeeOptions,
  CreateTokenSeriesTxHelper,
  MetadataField,
  PhantasmaAPI,
  PhantasmaKeys,
  SeriesInfoBuilder,
  TokenSchemasBuilder,
  getRandomPhantasmaId,
} from "phantasma-sdk-ts";

async function main() {
  const keys = PhantasmaKeys.fromWIF("YOUR_WIF");
  const creatorPk = new Bytes32(keys.PublicKey);

  const carbonTokenId = 123n; // BigInt(CreateTokenTxHelper.parseResult(...))

  const tokenSchemas = TokenSchemasBuilder.prepareStandard(true);
  const seriesSchema = tokenSchemas.seriesMetadata;

  const metadata: MetadataField[] = [
    { name: "name", value: "My Series" },
    { name: "description", value: "Series description" },
    { name: "imageURL", value: "https://example.com/cover.png" },
    { name: "infoURL", value: "https://example.com/info" },
    { name: "royalties", value: 10000000 },
  ];

  const phantasmaSeriesId = await getRandomPhantasmaId();
  const seriesInfo = SeriesInfoBuilder.build(
    seriesSchema,
    phantasmaSeriesId,
    0,
    0,
    creatorPk,
    metadata,
  );

  const feeOptions = new CreateSeriesFeeOptions();
  const maxData = 100_000_000n;

  const txHex = CreateTokenSeriesTxHelper.buildTxAndSignHex(
    carbonTokenId,
    seriesInfo,
    keys,
    feeOptions,
    maxData,
  );

  const rpc = new PhantasmaAPI("https://testnet.phantasma.info/rpc", undefined as any, "testnet");
  const txHash = await rpc.sendCarbonTransaction(txHex);

  const txInfo = await rpc.getTransaction(txHash);
  const carbonSeriesId = CreateTokenSeriesTxHelper.parseResult(txInfo.result);
  console.log("Carbon series id:", carbonSeriesId);
}

main().catch(console.error);
```

## 3) Mint a Carbon NFT

```ts
import {
  Bytes32,
  MintNftFeeOptions,
  MintNonFungibleTxHelper,
  MetadataField,
  NftRomBuilder,
  PhantasmaAPI,
  PhantasmaKeys,
  TokenSchemasBuilder,
  getRandomPhantasmaId,
} from "phantasma-sdk-ts";

async function main() {
  const keys = PhantasmaKeys.fromWIF("YOUR_WIF");
  const creatorPk = new Bytes32(keys.PublicKey);

  const carbonTokenId = 123n; // BigInt(CreateTokenTxHelper.parseResult(...))
  const carbonSeriesId = 1; // CreateTokenSeriesTxHelper.parseResult(...)

  const tokenSchemas = TokenSchemasBuilder.prepareStandard(true);
  const romSchema = tokenSchemas.rom; // use the schema from your token

  // Include only fields defined in romSchema (plus optional "rom" bytes).
  const metadata: MetadataField[] = [
    { name: "name", value: "NFT #1" },
    { name: "description", value: "Example mint" },
    { name: "imageURL", value: "https://example.com/nft.png" },
    { name: "infoURL", value: "https://example.com/nft" },
    { name: "royalties", value: 10000000 },
  ];

  const phantasmaNftId = await getRandomPhantasmaId();
  const rom = NftRomBuilder.buildAndSerialize(romSchema, phantasmaNftId, metadata);

  const feeOptions = new MintNftFeeOptions();
  const maxData = 100_000_000n;

  const txHex = MintNonFungibleTxHelper.buildTxAndSignHex(
    carbonTokenId,
    carbonSeriesId,
    keys,
    creatorPk,
    rom,
    new Uint8Array(),
    feeOptions,
    maxData,
  );

  const rpc = new PhantasmaAPI("https://testnet.phantasma.info/rpc", undefined as any, "testnet");
  const txHash = await rpc.sendCarbonTransaction(txHex);

  const txInfo = await rpc.getTransaction(txHash);
  const carbonNftAddresses = MintNonFungibleTxHelper.parseResult(carbonTokenId, txInfo.result);
  console.log(carbonNftAddresses[0].ToHex());
}

main().catch(console.error);
```

## Wallet Signing (Frontend)

For frontend flows, build a `TxMsg` using the same helpers and sign with:

- `PhantasmaLink.signCarbonTxAndBroadcast(txMsg, ...)`
- `EasyConnect.signCarbonTransaction(txMsg, ...)`

These require a wallet that supports Phantasma Link v4.
