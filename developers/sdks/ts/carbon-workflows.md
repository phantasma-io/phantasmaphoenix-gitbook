# Carbon Workflows

Carbon tokens are native, VM-less assets. For NFTs, Carbon provides fast token creation, series creation, and minting using specialized chain calls.

## Prerequisites

- Symbol must be uppercase A-Z (for example `MYNFT`).
- Token metadata is required for all tokens and must include `name`, `icon`, `url`, `description`.
- `icon` must be a base64 data URI (PNG/JPEG/WebP).
- NFT tokens require schemas (series, ROM, RAM) via `TokenSchemasBuilder`.

## Token schemas: standard vs custom

Use `TokenSchemasBuilder.prepareStandard(sharedMetadata)` when you only need the standard NFT fields and no custom ROM/RAM.

- `sharedMetadata = true` puts standard fields in **series metadata** (shared by all NFTs).
- `sharedMetadata = false` puts standard fields in **ROM** (per NFT).
- RAM schema is empty by default. With an empty RAM schema, the SDK sets `DynamicExtras`,
  so extra RAM fields can be serialized. When you define RAM fields, only those fields
  are serialized, and any extra RAM fields are dropped (not readable or updatable later).

Use `TokenSchemasBuilder.fromJson(json)` when you need custom fields or want full control of the schema.

Schema JSON format:

{% content-ref url="schema-json-reference.md" %}
[Schema JSON Reference](schema-json-reference.md)
{% endcontent-ref %}

```json
{
  "seriesMetadata": [
    { "name": "name", "type": "String" },
    { "name": "description", "type": "String" },
    { "name": "imageURL", "type": "String" },
    { "name": "infoURL", "type": "String" },
    { "name": "royalties", "type": "Int32" }
  ],
  "rom": [
    { "name": "artist", "type": "String" },
    { "name": "album", "type": "String" }
  ],
  "ram": [
    { "name": "level", "type": "Int32" }
  ]
}
```

Rules:
- `seriesMetadata`, `rom`, and `ram` must be JSON arrays of `{name, type}` objects.
  (These arrays are not related to `Array_*` field types.)
- `type` must be a `VmType` name string (for example `String`, `Int32`, `Bytes32`, `Array_String`).
  See the [Schema JSON Reference](schema-json-reference.md).
- Do not include system fields `_i`, `mode`, `rom` — the builder adds them automatically.
- Standard NFT fields (`name`, `description`, `imageURL`, `infoURL`, `royalties`) must be declared
  in either **series metadata** or the NFT **ROM schema** (at least one of the two).
- Field names are case-sensitive.

### Token metadata vs NFT metadata

- **Token metadata** (`name`, `icon`, `url`, `description`) is required for all tokens and is built with `TokenMetadataBuilder`.
- **NFT metadata** (series/ROM) is defined by the schema and uses standard fields plus any custom fields.

{% hint style="info" %}
If you fetch schemas from RPC (`getToken`), convert them using `vmStructSchemaFromRpcResult` before passing to builders. Do not rebuild schemas with `prepareStandard`.
{% endhint %}

## 1) Create a Carbon Token (NFT)

```ts
import {
  Bytes32,
  CreateTokenTxHelper,
  IntX,
  PhantasmaAPI,
  PhantasmaKeys,
  TokenInfoBuilder,
  TokenMetadataBuilder,
  TokenSchemasBuilder,
} from "phantasma-sdk-ts/public";

async function main() {
  const api = new PhantasmaAPI("https://testnet.phantasma.info/rpc", null, "testnet");
  const keys = PhantasmaKeys.fromWIF("YOUR_WIF");
  const creatorPk = new Bytes32(keys.publicKey);

  const tokenSchemas = TokenSchemasBuilder.prepareStandard(true);

  const metadata = TokenMetadataBuilder.buildAndSerialize({
    name: "My NFT",
    description: "Example NFT",
    icon: "data:image/png;base64,iVBORw0KGgo=",
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

  // The builder produces the message only. The fee is planned from it afterwards.
  const msg = CreateTokenTxHelper.buildTx(tokenInfo, creatorPk);

  // Plans the fee, checks the symbol, signs and broadcasts.
  const txHash = await api.sendTransaction(msg, keys);

  const txInfo = await api.getTransaction(txHash);
  const carbonTokenId = CreateTokenTxHelper.parseResult(txInfo.result);
  console.log("Carbon token id:", carbonTokenId.toString());
}

main().catch(console.error);
```

{% hint style="warning" %}
`Token.CreateToken` pays its base policy fee before the contract looks at the symbol.
A symbol that is already taken costs that fee and returns nothing.
`sendTransaction` runs one lookup first and refuses when the chain says the
symbol is taken, or when it could establish nothing. See
[Fees And Broadcasting](fees-and-broadcasting.md).
{% endhint %}

## 2) Create a Token Series

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

async function main() {
  const api = new PhantasmaAPI("https://testnet.phantasma.info/rpc", null, "testnet");
  const keys = PhantasmaKeys.fromWIF("YOUR_WIF");
  const creatorPk = new Bytes32(keys.publicKey);

  const carbonTokenId = 123n; // CreateTokenTxHelper.parseResult(...)

  const tokenSchemas = TokenSchemasBuilder.prepareStandard(true);
  const seriesSchema = tokenSchemas.seriesMetadata;

  const metadata: MetadataField[] = [
    { name: "name", value: "My Series" },
    { name: "description", value: "Series description" },
    { name: "imageURL", value: "https://example.com/cover.png" },
    { name: "infoURL", value: "https://example.com/info" },
    { name: "royalties", value: 10000000 },
  ];

  // Keep this id. A deterministic mint names the series by it.
  const phantasmaSeriesId = await getRandomPhantasmaId();
  const seriesInfo = SeriesInfoBuilder.build(
    seriesSchema,
    phantasmaSeriesId,
    0,
    0,
    creatorPk,
    metadata,
  );

  const msg = CreateTokenSeriesTxHelper.buildTx(carbonTokenId, seriesInfo, creatorPk);
  const txHash = await api.sendTransaction(msg, keys);

  const txInfo = await api.getTransaction(txHash);
  const carbonSeriesId = CreateTokenSeriesTxHelper.parseResult(txInfo.result);
  console.log("Carbon series id:", carbonSeriesId);
}

main().catch(console.error);
```

## 3) Mint a Carbon NFT

The chain derives the NFT id and stores a canonical ROM. One call mints one or
more instances, and every instance is one entry in `tokens`. Instances of
several series may share one call.

The ROM schema has to be the one the token was created with. The example below
continues from a token created with `prepareStandard(false)`, which puts the
standard fields in the per-NFT ROM. With `prepareStandard(true)` those fields
live in the series metadata, and the ROM carries only the custom fields the
schema declares.

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

async function main() {
  const api = new PhantasmaAPI("https://testnet.phantasma.info/rpc", null, "testnet");
  const keys = PhantasmaKeys.fromWIF("YOUR_WIF");
  const senderPk = new Bytes32(keys.publicKey);

  const carbonTokenId = 123n; // CreateTokenTxHelper.parseResult(...)
  const phantasmaSeriesId = 456n; // the id used when the series was created

  const tokenSchemas = TokenSchemasBuilder.prepareStandard(false);
  const romSchema = tokenSchemas.rom; // use the schema from your token

  // Include only fields defined in romSchema. `_i` and `rom` are chain-owned
  // here and are refused.
  const metadata: MetadataField[] = [
    { name: "name", value: "NFT #1" },
    { name: "description", value: "Example mint" },
    { name: "imageURL", value: "https://example.com/nft.png" },
    { name: "infoURL", value: "https://example.com/nft" },
    { name: "royalties", value: 10000000 },
  ];

  const rom = PhantasmaNftRomBuilder.buildAndSerialize(romSchema, metadata);

  const msg = MintPhantasmaNonFungibleTxHelper.buildTx({
    tokenId: carbonTokenId,
    sender: senderPk,
    to: senderPk,
    tokens: [
      new PhantasmaNftMintInfo({
        phantasmaSeriesId: IntX.fromBigInt(phantasmaSeriesId),
        rom,
        ram: new Uint8Array(),
      }),
    ],
  });

  const txHash = await api.sendTransaction(msg, keys);

  const txInfo = await api.getTransaction(txHash);
  const minted = MintPhantasmaNonFungibleTxHelper.parseResult(txInfo.result);
  console.log(minted[0].phantasmaNftId.toHex(), minted[0].carbonInstanceId.toString());
}

main().catch(console.error);
```

Each result entry carries the Phantasma NFT id the chain derived and the Carbon
instance id it minted.

## Wallet Signing (Frontend)

A wallet signs the message, so the application plans the fee before it hands the
message over:

```ts
const plan = await api.fees.plan(msg);
const planned = plan.apply(msg);
```

Then sign with:

- `PhantasmaLink.signCarbonTxAndBroadcast(plannedMsg, ...)`
- `EasyConnect.signCarbonTransaction(plannedMsg, ...)`

These require a wallet that supports Phantasma Link v4 or later.

A person confirming in a wallet takes longer than a local signature, so take the
chain's whole expiry window when building the message. See
[Fees And Broadcasting](fees-and-broadcasting.md).
