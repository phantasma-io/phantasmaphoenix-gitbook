---
title: "React Wallet Connection (phantasma-link-react)"
linkTitle: "React Wallet Connection"
weight: 50
---

`phantasma-link-react` is the React layer for the Phantasma Link v5 protocol. It wraps the
`PhantasmaLink5` client of `phantasma-sdk-ts` in a provider, a MobX store and a connect widget.
The protocol logic stays in the SDK; the package binds the session, the account and the wallet
events to React and renders the pairing link or QR code and the account menu.

Current package version: `0.3.0`. It depends on `phantasma-sdk-ts` 0.19.0 or later and needs
`react` and `react-dom` 18 or later as peer dependencies.

## Install

```bash
npm install phantasma-link-react
```

The components ship their stylesheet as `phantasma-link-react/styles.css`. Import it once where
the application imports its global styles.

## Quick Start

```tsx
import { PhantasmaLinkProvider, ConnectWidget } from "phantasma-link-react";

const dapp = { name: "My dApp", url: "https://mydapp.example" };

export function App() {
  return (
    <PhantasmaLinkProvider config={{ dapp, transport: "deeplink" }}>
      <header>
        <ConnectWidget />
      </header>
    </PhantasmaLinkProvider>
  );
}
```

The provider creates one store, builds the client when it mounts, restores a persisted session
if there is one, and disposes the client when it unmounts. It rebuilds the store only when the
dApp name or URL, the relay URL or the deeplink host changes.

## Configuration

`PhantasmaLinkConfig`:

| Field | Meaning |
| --- | --- |
| `dapp` | `DappMetadata`: the name and URL the wallet shows in its approval screen and embeds in the pairing URI. |
| `transport` | The initial transport: `injected`, `deeplink`, `relay` or `loopback`. Without it the store picks `injected` when a wallet extension is on the page, otherwise `deeplink`. |
| `relayUrl` | The relay WebSocket URL for the `relay` transport. Default: the public relay. |
| `host` | The universal-link host of the `deeplink` pairing URI. Default: `link.phantasma.info`. |

## Transports

| Transport | Use it when |
| --- | --- |
| `injected` | A browser-extension wallet defines `window.phantasmaLink` on the page. No pairing; the wallet prompts in its own UI. |
| `deeplink` | The dApp runs on the device that holds the wallet. The pairing URI is a universal link that opens the wallet. |
| `relay` | The wallet is on another device. The pairing URI is shown as a QR code, and the session arrives over the relay. |
| `loopback` | The wallet runs on the same machine and listens on a local WebSocket. |

`store.setTransport("relay")` switches at runtime. The store remembers the chosen transport in
`localStorage`, because the deeplink flow reloads the page on the way back from the wallet.

For `relay`, and for a `deeplink` connection that has no session yet, `connect()` enters the
`pairing` status and sets `pairingUri`; the session arrives as a wallet event once the user has
approved the pairing. `loopback`, `injected` and a resumable `deeplink` session call the wallet
directly.

## The Store

`usePhantasmaLink()` returns the `PhantasmaLinkStore` of the nearest provider. Read its fields
inside a `mobx-react` `observer` component, otherwise the component does not re-render when
the session changes.

```tsx
import { observer } from "mobx-react";
import { usePhantasmaLink } from "phantasma-link-react";

export const Demo = observer(function Demo() {
  const link = usePhantasmaLink();
  if (!link.connected) return <p>Not connected</p>;
  return (
    <div>
      <p>{link.address}</p>
      <button onClick={() => link.signMessage("hello")}>Sign message</button>
      <button onClick={() => link.getChains()}>Get chains</button>
    </div>
  );
});
```

Fields:

| Field | Meaning |
| --- | --- |
| `status` | `idle`, `pairing`, `connecting`, `connected` or `error`. |
| `connected` | `true` while a session is live. |
| `account`, `address` | The connected `LinkAccountV5` and its address. |
| `capabilities`, `walletInfo` | What the wallet reported on connect. |
| `transport` | The current transport. |
| `pairingUri` | The pairing link while the status is `pairing`. |
| `busyOp` | The label of the request in flight, if any. |
| `logs` | A rolling log of requests, results, events and errors (`LinkLogEntry`, 200 entries). |
| `client` | The underlying `PhantasmaLink5` client, for calls the store does not wrap. |

Operations: `connect()`, `cancel()`, `disconnect()`, `setTransport(kind)`, `getChains()`,
`getWalletInfo()`, `getAccounts()`, `signMessage(text)`, `sendTransaction(params)`,
`invokeScript(params)`, `clearLogs()`. Each request appends to `logs`, and a failure is logged
as an `error` entry. `sendTransaction` takes the `SendTransactionParams` of the v5 protocol: the
wallet signs and broadcasts. A dApp that wants the signature without the broadcast calls
`store.client.signTransaction(params)`.

## Components

- `ConnectWidget`: a button that reads "Connect wallet" until a session is live, opens the
  pairing link or QR code when the transport needs pairing, and then shows the address with
  "Copy address" and "Disconnect".
- `PairingModal`: the pairing dialog on its own, with `uri`, `transport` and `onClose` props.

## Helpers And Re-exports

- `verifyV5Signature(message, result, address)` checks a `signMessage` result against the
  signer's address. It returns `true` or `false`, or `null` when the inputs cannot be checked.
- `errMsg(e)` and `clip_copy(text)` are the small utilities the components use.
- The package re-exports `observer`, `makeAutoObservable` and `runInAction` from MobX, so that an
  application that builds its own observable stores shares one MobX instance with the package.
- It also re-exports the v5 types an application needs next to the store: `LinkEvent`,
  `TxFormat`, `SignatureKind`, `bytesToBase64`, `base64ToBytes`, `utf8ToBytes`, `DappMetadata`,
  `LinkAccountV5`, `LinkBalance`, `WalletCapabilities`, `WalletInfo`, `ConnectResult`,
  `SendTransactionParams`, `SignMessageParams`, `InvokeScriptParams`.

## Relationship To The SDK

The store owns one `PhantasmaLink5` client and exposes it as `store.client`. Everything the
protocol offers is documented on the client page:

- [Phantasma Link v5](phantasma-link-v5.md)

The v1-v4 wrappers `EasyConnect` and `PhantasmaLink` are separate classes of `phantasma-sdk-ts`
and are not used by this package.
