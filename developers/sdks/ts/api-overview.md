# API Overview

This page summarizes the main building blocks of the TS SDK and when to use them.

## Core Classes

### PhantasmaAPI
RPC client for chain data and broadcasting transactions.

- `getAccount`, `getBlockByHeight`, `getTransaction`
- `sendRawTransaction` for signed VM transactions
- `sendCarbonTransaction` for Carbon transactions
- `invokeRawScript` for read-only calls

### ScriptBuilder
Builds VM scripts for state-changing calls and read-only invokes.

- `AllowGas` / `SpendGas` for transactional scripts
- `CallContract` for contract methods
- `CallInterop` for core runtime operations

### Transaction
Represents a signed VM transaction.

- Construct with `nexus`, `chain`, `script` (hex), `expiration`, `payload` (hex).
- Sign using `signWithKeys` or `sign(wif)`.
- Broadcast using `PhantasmaAPI.sendRawTransaction`.

### PhantasmaKeys
Manages keypairs and signing.

- `PhantasmaKeys.fromWIF(wif)`
- `PhantasmaKeys.generate()`
- `.Address` gives an `Address` object

### PhantasmaLink / EasyConnect / React
Wallet integration for frontend apps.

- `PhantasmaLink.login(...)`
- `PhantasmaLink.signTx(...)` for VM transactions
- `PhantasmaLink.signCarbonTxAndBroadcast(...)` for Carbon transactions
- `EasyConnect.signCarbonTransaction(...)` wraps Carbon signing + broadcast
- `@phantasma/connect-react` wraps `EasyConnect` for React and provides `PhaConnectState` and `PhaAccountWidgetV1`

See:
- [Wallet Connection](/developers/sdks/ts/frontend/wallet-connection.md)
- [Phantasma Link](/developers/sdks/ts/shared-methods/phantasmalink.md)
- [EasyConnect](/developers/sdks/ts/shared-methods/easyconnect.md)
- [React Wallet Connection](/developers/sdks/ts/frontend/connect-react.md)

### Decoder and Event Helpers
Decode VM results and event payloads.

- `Decoder` to read VM objects from `invokeRawScript` results
- `getTokenEventData` to decode TokenReceive/TokenSend event data

## Carbon Helpers

For Carbon tokens, use helpers under `core/types/Carbon`:

- `TokenInfoBuilder`, `TokenMetadataBuilder`, `TokenSchemasBuilder`
- `SeriesInfoBuilder`, `NftRomBuilder`
- `CreateTokenTxHelper`, `CreateTokenSeriesTxHelper`, `MintNonFungibleTxHelper`

These helpers build `TxMsg` objects or signed hex suitable for `sendCarbonTransaction`.

## Schema Conversion Helpers

RPC returns schema results as plain objects. Convert them to SDK schema types using:

- `vmStructSchemaFromRpcResult`

This is useful when you fetch token schemas via `getToken` and want to build series or NFT ROM data locally.
