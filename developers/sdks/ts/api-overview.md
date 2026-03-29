# API Overview

This page summarizes the main building blocks of the TS SDK and how they fit together in current Carbon and VM workflows.

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

- `AllowGas(...)`
- `SpendGas(...)`
- `CallContract(...)`
- `CallInterop(...)`

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
- `.Address`

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

For Carbon tokens and NFTs, use helpers under `core/types/Carbon`:

- `TokenInfoBuilder`
- `TokenMetadataBuilder`
- `TokenSchemasBuilder`
- `SeriesInfoBuilder`
- `NftRomBuilder`
- `CreateTokenTxHelper`
- `CreateTokenSeriesTxHelper`
- `MintNonFungibleTxHelper`

These helpers build `TxMsg` objects or other schema-aware payloads for Carbon flows.

## Decoder And Event Helpers

Use these for result and event parsing:

- `Decoder`
- `getTokenEventData`

## Schema Conversion Helpers

RPC schema payloads come back as plain objects. Convert them into SDK schema types with:

- `vmStructSchemaFromRpcResult`

This is useful when you fetch token schema information through RPC and want to build series or NFT ROM data locally.
