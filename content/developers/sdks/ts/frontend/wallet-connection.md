---
title: "Wallet Connection"
weight: 10
---

Use the Phantasma Link protocol to connect a browser dApp to a wallet. The TS SDK exposes the v5 client and two layers of the v1-v4 connection stack; `phantasma-link-react` adds React bindings for the v5 client.

## Choose A Layer

| Layer | Package | Best For | Docs |
| --- | --- | --- | --- |
| `PhantasmaLink5` | `phantasma-sdk-ts/link/v5` | the v5 protocol: encrypted deeplink and relay transports, sessions, typed requests, numeric error codes | [Phantasma Link v5](phantasma-link-v5.md) |
| `PhantasmaLink` | `phantasma-sdk-ts` | direct control over transport, wallet requests, and signing | [Phantasma Link](phantasmalink.md) |
| `EasyConnect` | `phantasma-sdk-ts` | smaller browser wrapper with Carbon and prebuilt signing helpers | [EasyConnect](easyconnect.md) |
| `PhantasmaLinkStore` | `phantasma-link-react` | React apps on the v5 protocol: provider, store, connect widget, session restore | [React Wallet Connection](connect-react.md) |

## Quick Choice

- Wallet that speaks Phantasma Link v5 -> `PhantasmaLink5`
- React app -> `phantasma-link-react`
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

The v5 client and the React package offer four transports: `injected` (a browser-extension wallet), `deeplink` (a wallet app on the same device), `relay` (a wallet on another device) and `loopback` (a desktop wallet on the same machine). The React store picks `injected` when an extension is on the page and `deeplink` otherwise; `setTransport(...)` changes it.

`PhantasmaLink` and `EasyConnect` speak the v1-v4 protocol over the injected transport or the local wallet socket. If your app depends on a specific wallet path, choose it explicitly instead of relying on detection.

## Typical Flow

1. connect to a wallet
2. build a VM script or Carbon `TxMsg`
3. choose the correct signing path
4. submit and confirm with RPC
