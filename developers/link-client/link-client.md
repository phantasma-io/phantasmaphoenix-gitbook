---
description: Connecting wallets to dApps
---

# 🔗 Phantasma Link Client

Phantasma Link is a protocol that lets dApps sign transactions and run on-chain operations on behalf of users, in a transparent way, without ever accessing the user's private key.

{% hint style="info" %}
This page is a protocol overview, not a TypeScript guide.
If you're building in TS, start here:

- [Frontend Guide](/developers/sdks/ts/frontend/frontend.md)

Then use these pages as needed:

- [Phantasma Link (TS)](/developers/sdks/ts/shared-methods/phantasmalink.md)
- [EasyConnect (TS)](/developers/sdks/ts/shared-methods/easyconnect.md)
- [React Wallet Connection](/developers/sdks/ts/frontend/connect-react.md)
{% endhint %}

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

- TypeScript: [Phantasma Link](/developers/sdks/ts/shared-methods/phantasmalink.md), [EasyConnect](/developers/sdks/ts/shared-methods/easyconnect.md)
- Unity: [Unity Link Client](/developers/sdks/unity/reference/link-client.md)
