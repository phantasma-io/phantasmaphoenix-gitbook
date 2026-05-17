# API Overview

This page summarizes the main building blocks of the TypeScript SDK and how
they fit together in current Carbon, VM, RPC, and wallet workflows.

For method-level details, use the complete reference:

{% content-ref url="reference/README.md" %}
TypeScript SDK Complete API Reference
{% endcontent-ref %}

## Package

| Item | Value |
| ---- | ----- |
| Package | `phantasma-sdk-ts` |
| Current source version | `0.8.2` |
| Runtime | Node `>=22`; browser bundles depend on the wallet/link feature being used |
| Recommended import | `phantasma-sdk-ts/public` |

## Core Building Blocks

### `PhantasmaAPI`

RPC client for chain reads and transaction broadcast.

Use it for:

- `getAccount`, `getBlockByHeight`, `getTransaction`
- `sendRawTransaction` for signed VM transactions
- `sendCarbonTransaction` for Carbon transactions
- `invokeRawScript` for read-only VM execution

### `ScriptBuilder`

Builds VM scripts for invokes and state-changing calls.

Common uses:

- `allowGas(...)`
- `spendGas(...)`
- `callContract(...)`
- `callInterop(...)`

### `Transaction`

Represents a VM transaction object.

Use it when you need to control transaction fields locally before signing, for example:

- `nexus`
- `chain`
- `script`
- `expiration`
- `payload`
- pre-mined proof of work

This is the object used with `signPrebuiltTransaction(...)`.

### `PhantasmaKeys`

Local key management and signing helpers.

Common entry points:

- `PhantasmaKeys.fromWIF(wif)`
- `PhantasmaKeys.generate()`
- `.address`

## Wallet Layers

The TS SDK exposes three wallet integration layers.

### `PhantasmaLink`

Use this when you want direct wallet control.

Key capabilities:

- `login(...)`
- `signTx(...)`
- `signTxSignature(...)`
- `signPrebuiltTransaction(...)`
- `signCarbonTxAndBroadcast(...)`
- `getNexus(...)`

### `EasyConnect`

Use this when you want a smaller browser wrapper but still want access to the underlying link.

Key capabilities:

- `connect(...)`
- `signTransaction(...)`
- `signCarbonTransaction(...)`
- `signPrebuiltTransaction(...)`
- `deployContract(...)`
- `conn.link` for lower-level escape hatches

### `@phantasma/connect-react`

Use this when you want React state, transport selection, restore support, and a ready-made account widget.

Key capabilities:

- `PhaConnectState`
- `PhaConnectCtx`
- `PhaAccountWidgetV1`
- transport modes: `auto`, `injected`, `local-socket`
- connection diagnostics and restore support

See:

- [Wallet Connection](/developers/sdks/ts/frontend/wallet-connection.md)
- [Phantasma Link](/developers/sdks/ts/shared-methods/phantasmalink.md)
- [EasyConnect](/developers/sdks/ts/shared-methods/easyconnect.md)
- [React Wallet Connection](/developers/sdks/ts/frontend/connect-react.md)

## Which Signing Path To Use

### Wallet-built VM transaction

Use:

- `PhantasmaLink.signTx(...)`
- or `EasyConnect.signTransaction(...)`

### Prebuilt VM transaction

Use:

- `Transaction`
- `PhantasmaLink.signPrebuiltTransaction(...)`
- or `EasyConnect.signPrebuiltTransaction(...)`
- then `PhantasmaAPI.sendRawTransaction(...)`

This is the correct pattern when your application needs exact control over the final transaction bytes.

### Carbon-native transaction

Use:

- Carbon helper builders to create a `TxMsg`
- `PhantasmaLink.signCarbonTxAndBroadcast(...)`
- or `EasyConnect.signCarbonTransaction(...)`

## Carbon Helpers

For Carbon tokens and NFTs, use `phantasma-sdk-ts/public` for the RPC client
and application-level SDK types. Import the complete Carbon helper surface from
`phantasma-sdk-ts/types`; this includes fee option classes and helper functions
that are not runtime exports of `/public`.

- `TokenInfoBuilder`
- `TokenMetadataBuilder`
- `TokenSchemasBuilder`
- `SeriesInfoBuilder`
- `NftRomBuilder`
- `CreateTokenTxHelper`
- `CreateTokenSeriesTxHelper`
- `MintNonFungibleTxHelper`
- `MintPhantasmaNonFungibleTxHelper`

These helpers build `TxMsg` objects or other schema-aware payloads for Carbon flows.

`FeeOptions.calculateMaxGas(count?)` and
`MintNftFeeOptions.calculateMaxGas(countOrTokens?)` are count-sensitive in the
current SDK. Direct one-NFT mint helpers pass `1`; Phantasma NFT batch helpers
pass the token list.

## Decoder And Event Helpers

Use these for result and event parsing:

- `Decoder`
- `getTokenEventData`

## Schema Conversion Helpers

RPC schema payloads come back as plain objects. Convert them into SDK schema types with:

- `vmStructSchemaFromRpcResult`

This is useful when you fetch token schema information through RPC and want to build series or NFT ROM data locally.
