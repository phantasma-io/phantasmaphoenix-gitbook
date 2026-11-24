---
title: "🔗 Phantasma Link Client"
linkTitle: "Link Client"
weight: 50
description: "Connecting wallets to dApps"
---

Phantasma Link is a protocol that lets dApps sign transactions and run on-chain operations on behalf of users, in a transparent way, without ever accessing the user's private key.

> [!NOTE]
> This page describes the protocol. The TypeScript implementation is documented on [Frontend Guide](../sdks/ts/frontend/_index.md), [Phantasma Link v5](../sdks/ts/frontend/phantasma-link-v5.md), [Phantasma Link](../sdks/ts/frontend/phantasmalink.md), [EasyConnect](../sdks/ts/frontend/easyconnect.md) and [React Wallet Connection](../sdks/ts/frontend/connect-react.md).

## Phantasma Link v5

Phantasma Link v5 is the current protocol generation. The wallet still signs on the user's behalf and never exposes the private key. v5 replaces the v1-v4 string protocol with a structured JSON envelope: typed parameters, numeric error codes, capability negotiation, end-to-end encryption, and revocable sessions. The same envelope travels over four transports:

- **Injected**: a browser-extension wallet. The extension defines `window.phantasmaLink` on the page, and the dApp calls it directly.
- **Loopback**: a WebSocket to a desktop wallet on the same machine.
- **Deeplink** ping-pong (app to app): the primary path on mobile. It works on iOS and keeps signing working even when the relay is down.
- **Relay**: for large payloads and cross-device flows.

v5 also raises the request size limit from about 32 KB to the chain ceiling (1 MiB metadata, 32 MiB transaction). The TypeScript SDK is the reference implementation, exposed under the `phantasma-sdk-ts/link/v5` entry point, and the full protocol is specified in `spec/phantasma-link-v5.md` in that SDK.

The v1-v4 string protocol described below remains supported during a deprecation window.

## Protocol operations

A wallet that implements Phantasma Link answers a small set of requests from a connected dApp. Each request is sent to the wallet over the link transport and answered asynchronously. The concrete method names and callback shapes depend on the SDK you use (see [Implementations](#implementations)); the operations below are what those methods map to.

### Authorization

The dApp requests a wallet session, identifying itself with a dApp id and the link protocol version. The wallet prompts the user and, on approval, returns a session token and the connected nexus. SDKs send this as `authorize/{dappID}/{version}`.

### Account access

Once authorized, the dApp can read the connected account: its address, registered name, and token balances. SDKs send this as `getAccount/{platform}`.

### Data signing

The dApp can ask the wallet to sign arbitrary bytes with the user's key, without exposing the private key. The wallet returns the signature over the supplied data.

### Transaction signing

The dApp builds a transaction script and asks the wallet to sign and broadcast it. The wallet signs with the user's key, submits the transaction, and returns the resulting transaction hash.

### Logout

The dApp ends the session. The wallet clears the session token and cached account state.

## Implementations

Use the SDK pages for the concrete method signatures and examples:

- TypeScript: [Phantasma Link v5](../sdks/ts/frontend/phantasma-link-v5.md), [Phantasma Link](../sdks/ts/frontend/phantasmalink.md), [EasyConnect](../sdks/ts/frontend/easyconnect.md)
- Unity: [Unity Link Client](../sdks/unity/reference/link-client.md)
- C# wallets: [Phantasma Link v5 For Wallets](../sdks/csharp/wallet-link-v5.md), the wallet side of v5
