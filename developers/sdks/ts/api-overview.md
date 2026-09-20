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
| Current source version | `0.18.1` |
| Runtime | Node `>=22`; browser bundles depend on the wallet/link feature being used |
| Recommended import | `phantasma-sdk-ts/public` |

## Core Building Blocks

### `PhantasmaAPI`

RPC client for chain reads, fee planning, and transaction broadcast.

Use it for:

- `getAccountInfo`, `getBlockByHeight`, `getTransaction`
- `fees` for the chain's fee planner
- `sendTransaction` to plan, sign and broadcast a Carbon message in one call
- `sendRawTransaction` for signed VM transactions
- `sendCarbonTransaction` for a Carbon envelope that is already signed
- `invokeRawScript` for read-only VM execution

`getAccount` and `getAccounts` are deprecated. Their response embeds every NFT
id the address owns, so it grows with the size of the account. Use
`getAccountInfo` with `getAccountFungibleTokens` and `getAccountNFTs`.

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

### Carbon-native transaction, local key

Use:

- Carbon helper builders to create a `TxMsg`
- `PhantasmaAPI.sendTransaction(msg, signers)`

This plans the fee, runs the token-creation pre-flight, signs with every witness
and broadcasts.

### Carbon-native transaction, wallet key

Use:

- Carbon helper builders to create a `TxMsg`
- `PhantasmaAPI.fees.plan(msg)` and `plan.apply(msg)` to set the fee ceilings
- `PhantasmaLink.signCarbonTxAndBroadcast(...)`
- or `EasyConnect.signCarbonTransaction(...)`

## Carbon Helpers

`phantasma-sdk-ts/public` exports the RPC client, the Carbon builders and the
fee planner. Use `phantasma-sdk-ts/types` only for the few helpers that are not
in `/public`, such as `getRandomPhantasmaId`.

Schema and payload builders:

- `TokenInfoBuilder`
- `TokenMetadataBuilder`
- `TokenSchemasBuilder`
- `SeriesInfoBuilder`
- `NftRomBuilder`
- `PhantasmaNftRomBuilder`

Message builders:

- `NativeTxHelper` for transfers, fungible mints and burns
- `CreateTokenTxHelper`
- `CreateTokenSeriesTxHelper`
- `MintPhantasmaNonFungibleTxHelper`

These helpers build `TxMsg` objects or other schema-aware payloads for Carbon
flows. They carry no prices. A message is planned after it is built, and the
plan sets `maxGas` and `maxData`.

{% content-ref url="fees-and-broadcasting.md" %}
[Fees And Broadcasting](fees-and-broadcasting.md)
{% endcontent-ref %}

## Decoder And Event Helpers

Use these for result and event parsing:

- `Decoder`
- `getTokenEventData`

## Schema Conversion Helpers

RPC schema payloads come back as plain objects. Convert them into SDK schema types with:

- `vmStructSchemaFromRpcResult`

This is useful when you fetch token schema information through RPC and want to build series or NFT ROM data locally.
