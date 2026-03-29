# Wallet Connection

Use the Phantasma Link protocol to connect a browser dApp to a wallet. The TS SDK exposes three layers of that same connection stack.

## Choose A Layer

| Layer | Package | Best For | Docs |
| --- | --- | --- | --- |
| `PhantasmaLink` | `phantasma-sdk-ts` | direct control over transport, wallet requests, and signing | [Phantasma Link](/developers/sdks/ts/shared-methods/phantasmalink.md) |
| `EasyConnect` | `phantasma-sdk-ts` | smaller browser wrapper with Carbon and prebuilt signing helpers | [EasyConnect](/developers/sdks/ts/shared-methods/easyconnect.md) |
| `@phantasma/connect-react` | `@phantasma/connect-react` | React apps, transport selection, restore support, widget UI | [React Wallet Connection](/developers/sdks/ts/frontend/connect-react.md) |

## Quick Choice

- React app -> `@phantasma/connect-react`
- Non-React app, ordinary browser flow -> `EasyConnect`
- Need direct wallet control or exact low-level signing flow -> `PhantasmaLink`

## Choose The Right Signing Path

### Normal wallet-driven VM transaction

Use:

- `PhantasmaLink.signTx(...)`
- or `EasyConnect.signTransaction(...)`

### Prebuilt VM transaction

Use:

- `Transaction`
- `PhantasmaLink.signPrebuiltTransaction(...)`
- or `EasyConnect.signPrebuiltTransaction(...)`
- then `PhantasmaAPI.sendRawTransaction(...)`

This is the correct path when your application needs exact control over:

- final payload bytes
- expiration
- pre-mined proof of work

### Carbon-native transaction

Use:

- `PhantasmaLink.signCarbonTxAndBroadcast(...)`
- or `EasyConnect.signCarbonTransaction(...)`

## Transport Choice

Depending on the layer, you may be using:

- injected wallet transport
- local socket transport

If your app depends on a specific wallet path, do not leave that choice ambiguous. Current React tooling exposes explicit transport modes:

- `auto`
- `injected`
- `local-socket`

## Typical Flow

1. connect to a wallet
2. build a VM script or Carbon `TxMsg`
3. choose the correct signing path
4. submit and confirm with RPC
