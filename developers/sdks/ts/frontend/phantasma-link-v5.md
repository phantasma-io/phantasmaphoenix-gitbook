# Phantasma Link v5

`PhantasmaLink5` is the TypeScript client for Phantasma Link v5. It connects a dApp to a wallet, asks the wallet to sign or send transactions and messages, and receives wallet events. The protocol itself is described in the [Phantasma Link overview](/developers/link-client/link-client.md).

Import the client from the `phantasma-sdk-ts/link/v5` entry point:

```ts
import { PhantasmaLink5 } from 'phantasma-sdk-ts/link/v5';
```

The same module is exported as the `PhantasmaLinkV5` namespace from the package root and from `phantasma-sdk-ts/public`:

```ts
import { PhantasmaLinkV5 } from 'phantasma-sdk-ts/public';

const client = PhantasmaLinkV5.PhantasmaLink5.loopback();
```

The v1-v4 client, `PhantasmaLink`, is a separate class and is unchanged. See [Phantasma Link](/developers/sdks/ts/shared-methods/phantasmalink.md).

## Choosing A Transport

Each factory builds the client over one transport.

| Factory | Use it when | Encryption |
| --- | --- | --- |
| `PhantasmaLink5.injected(options?)` | A browser-extension wallet is installed. The extension defines `window.phantasmaLink` on the page (spec section 6.1). | None. The page and the extension run in the same browser. |
| `PhantasmaLink5.webDeeplink(options)` | A web page talks to a wallet app on the same device. | Always, with the channel key created for the pairing. |
| `PhantasmaLink5.loopback(options?)` | The wallet runs on the same machine and listens on a local WebSocket. | None. The connection stays on the local host. |
| `PhantasmaLink5.relay(options)` | Both sides already share a pairing topic and a 32-byte session key, and messages go through the relay. | Always. |
| `PhantasmaLink5.relayEcdh(options)` | Pairing has to use a custom-scheme link, which another app on the device could intercept. | Always, with a key derived after the wallet answers. |
| `PhantasmaLink5.deeplink(options)` | A native app runs the deeplink exchange itself, with its own topic, URL opener and session key. | Always. |
| `new PhantasmaLink5(transport, options)` | A custom transport implements `LinkTransport`. | Set by `options.sessionKey`. Without a key, frames are plaintext. |

Injected uses the page's `window.phantasmaLink`. The extension defines it before the page's scripts run, so there is no event to wait for. `findInjectedProvider()` returns the provider when it is present and speaks v5, otherwise `undefined`; check it before choosing a transport. The factory throws `LinkError` with code `4900` when no provider is on the page. The `provider` option passes a provider explicitly, which tests use.

Loopback connects to `ws://localhost:7090/phantasma/v5`. The `host`, `port` and `path` options change the parts of that URL, and `webSocketFactory` supplies a WebSocket implementation where no global `WebSocket` exists.

The relay transports connect to `wss://link.phantasma.info/relay` (`DEFAULT_RELAY_URL`). The `url` option changes it. `relay` and `deeplink` refuse to build without a 32-byte `sessionKey` and throw `LinkError` with code `-32602`.

`injected`, `webDeeplink`, `deeplink`, `relay` and `relayEcdh` wait up to 5 minutes for each answer, because an answer includes the user's consent, and on mobile an app switch. A client built with the constructor, and the loopback client, wait 60 seconds. The `requestTimeoutMs` option changes the timeout, and `0` disables it.

## Web dApp Flow

`webDeeplink` builds a client for a browser page. It also keeps the pairing record, builds the pairing link and reads the wallet answers:

```ts
import { PhantasmaLink5 } from 'phantasma-sdk-ts/link/v5';

const client = await PhantasmaLink5.webDeeplink({
  dapp: { name: 'Example dApp', url: 'https://dapp.example' },
});

// A wallet answer that arrived while the page was reloading.
const recovered = client.takeUnmatchedResponse();

if (!client.account) {
  // Render client.pairingUri as a link or a QR code for the one-time pairing consent.
  console.log(client.pairingUri);
}

async function onConnectClick() {
  const connect = await client.connect();
  console.log(connect.account.address, connect.capabilities.txFormats);
}
```

The factory does the following:

1. It loads the pairing record from `localStorage` under the key `phantasma.link.v5.webdeeplink`. On the first visit it creates the record: a random topic, a 32-byte channel key and the callback URL. It saves the record before any request leaves the page, because opening the wallet can unload the page.
2. It builds `pairingUri`, a universal link on `link.phantasma.info` that carries the topic, the channel key, the callback URL and the dApp metadata. A symmetric key is never placed in a custom-scheme URL.
3. It restores the last connect result from the record, so `client.account` is set right after a reload.
4. It reads a wallet answer from the current page URL, and listens to `hashchange` for later answers. After it consumes an answer, it removes the fragment from the address bar.

The wallet answers by opening the callback URL with the answer in the URL fragment. The callback defaults to the current page URL without its fragment. The wallet stores the callback when the user approves the pairing, so a different callback needs a new pairing.

After the pairing approval, the wallet can send the connect result back at once. The client then adopts the session, and `client.account` is set without a separate `connect()` call.

The factory never opens a URL itself. Mobile browsers open another app only from a user gesture, so call `connect()`, `signTransaction()` and the other requests from click handlers.

A single-page app whose router consumes `hashchange` passes each new page URL to `client.deliverUrl(url)`.

When the page reloads while a request is open, the request's promise is lost. The wallet answer still arrives with the reloaded page, and `takeUnmatchedResponse()` returns it once, right after the client is built. It returns `id`, `ok`, and `result` or `error`.

`disconnect()` sends `pha_disconnect`, and over deeplink that opens the wallet, which can unload the page before the local cleanup runs. `forgetSession()` clears the local session and the stored record's session fields without contacting the wallet. The wallet drops its side when the session expires.

## Methods

| Member | Wallet method | Result |
| --- | --- | --- |
| `connect(dapp?, extra?)` | `pha_connect` | `ConnectResult`: `wallet`, the granted `capabilities`, `account` and `session`. |
| `getAccounts()` | `pha_getAccounts` | `{ accounts }`, the accounts authorized for this session. |
| `getChains()` | `pha_getChains` | `{ chains, current, nexus }`. |
| `getWalletInfo()` | `pha_getWalletInfo` | `{ name, version, icon?, rpc? }`. |
| `signMessage(params)` | `pha_signMessage` | `{ signature, random }`. |
| `signTransaction(params)` | `pha_signTransaction` | `{ signedTx }`. The dApp broadcasts the transaction. |
| `sendTransaction(params)` | `pha_sendTransaction` | `{ hash }`. The wallet signs and broadcasts. |
| `invokeScript(params)` | `pha_invokeScript` | `{ results }`. A read-only VM call that needs no approval. |
| `disconnect()` | `pha_disconnect` | `{ ok: true }`. Clears the local session as well. |
| `forgetSession()` | none | Clears the local session without contacting the wallet. |
| `onEvent(handler)` | none | Subscribes to wallet events and returns an unsubscribe function. |
| `close()` | none | Closes the transport and rejects every request in flight. |

The getters `account` and `capabilities` return the values from the last successful connect. `pairingUri` returns the pairing link of a client built by `webDeeplink` or `relayEcdh`.

### Connect

`connect()` takes the dApp metadata (`name`, `url`, and optional `icon` and `description`). A client built with a `dapp` option connects without arguments. The second argument can request `chains`, `methods` and `features`. The wallet can grant a subset of what the dApp requests, so check `capabilities` before calling a method.

When the client already holds a session id, `connect()` asks the wallet to resume that session. A wallet that knows the session resumes it without a prompt. Otherwise the wallet shows a new consent prompt.

`capabilities` lists:

| Field | Meaning |
| --- | --- |
| `plvVersions` | Protocol versions the wallet speaks. |
| `methods` | The `pha_*` methods the wallet serves. |
| `chains` | Chain ids such as `phantasma:mainnet`. |
| `txFormats` | `script`, `carbon`, or both. |
| `signatureKinds` | `Ed25519`, `ECDSA`, or both. |
| `features` | Optional feature flags. |
| `maxPayloadBytes` | Optional per-transport payload limits: `relay`, `deeplink`, `loopback`, `injected`. |

## Signing And Sending Transactions

`signTransaction` and `sendTransaction` take the same parameters:

| Field | Meaning |
| --- | --- |
| `format` | `script` for a classic `Transaction`, `carbon` for a Carbon `TxMsg`. The wallet sends a `script` transaction with `sendRawTransaction` and a `carbon` transaction with `sendCarbonTransaction`. |
| `tx` | The unsigned transaction bytes, base64. |
| `signatureKind` | Optional. `Ed25519` selects the Phantasma key, `ECDSA` the secp256k1 key. Carbon witnesses are Ed25519 only, so `ECDSA` with `format: 'carbon'` fails with `5003`. |
| `pow` | Optional proof of work, meaningful only with `format: 'script'`. The protocol does not let the wallet mine proof of work on a transaction the dApp built, because mining would change bytes the dApp already assembled. A transaction that needs proof of work carries it before it is sent. |

A Carbon message must be planned before the wallet signs it, because a builder leaves `maxGas` at `0`. Plan it with the chain's prices and pass the planned copy. See [Fees And Broadcasting](/developers/sdks/ts/fees-and-broadcasting.md).

```ts
import {
  Address,
  Bytes32,
  CarbonBlob,
  NativeTxHelper,
  PhantasmaAPI,
  parseUnits,
} from 'phantasma-sdk-ts/public';
import { TxFormat, bytesToBase64 } from 'phantasma-sdk-ts/link/v5';

const api = new PhantasmaAPI('https://pharpc1.phantasma.info/rpc', null, 'mainnet');
const sender = Address.fromText(client.account!.address);

const transfer = NativeTxHelper.transferFungible({
  from: new Bytes32(sender.getPublicKey()),
  to: new Bytes32(Address.fromText('P2K...').getPublicKey()),
  tokenId: 1n, // KCAL
  amount: parseUnits('10', 10),
});

const plan = await api.fees.plan(transfer);
const { hash } = await client.sendTransaction({
  format: TxFormat.Carbon,
  tx: bytesToBase64(CarbonBlob.serialize(plan.apply(transfer))),
});
```

A classic VM transaction goes to the wallet without signatures:

```ts
import { Address, ScriptBuilder, Transaction } from 'phantasma-sdk-ts/public';
import { TxFormat, bytesToBase64 } from 'phantasma-sdk-ts/link/v5';

const from = Address.fromText(client.account!.address);
const script = new ScriptBuilder()
  .beginScript()
  .allowGas(from, Address.nullAddress, 100000, 21000)
  .callInterop('Runtime.TransferTokens', [from, 'P2K...', 'KCAL', '1000000000'])
  .spendGas(from)
  .endScript();

const tx = new Transaction('mainnet', 'main', script, new Date(Date.now() + 5 * 60 * 1000), '');
const { signedTx } = await client.signTransaction({
  format: TxFormat.Script,
  tx: bytesToBase64(tx.toByteArray(false)),
});
```

`signedTx` is the signed transaction in base64. The dApp submits it itself, as hex: a `script` transaction with `api.sendRawTransaction` and a `carbon` transaction with `api.sendCarbonTransaction`.

## Signing A Message

`signMessage` takes the message bytes in base64, an optional `display` text the wallet can show instead of the bytes, and an optional `signatureKind`.

The wallet signs `PHANTASMA_LINK_V5_MSG\n || random || message`, where `random` is 32 bytes the wallet generates. The prefix keeps a message signature from being valid as a transaction signature. The result returns the signature and `random`, both in base64. With `Ed25519`, the signature is a 64-byte Ed25519 signature. `buildSignMessagePayload(message, random)` rebuilds the signed bytes for verification:

```ts
import { Address, Ed25519Signature } from 'phantasma-sdk-ts/public';
import { base64ToBytes, buildSignMessagePayload, bytesToBase64 } from 'phantasma-sdk-ts/link/v5';

const message = new TextEncoder().encode('Sign in to Example dApp');
const { signature, random } = await client.signMessage({ message: bytesToBase64(message) });

const payload = buildSignMessagePayload(message, base64ToBytes(random));
const valid = new Ed25519Signature(base64ToBytes(signature)).verify(
  payload,
  Address.fromText(client.account!.address)
);
```

## Events

`onEvent((event, data, session) => ...)` receives the events the wallet pushes.

| Event | Meaning |
| --- | --- |
| `pha_accountsChanged` | The accounts authorized for the session changed. `data.accounts` holds the new list. |
| `pha_chainChanged` | The wallet switched chains. `data.chain` holds the new chain id. |
| `pha_sessionDeleted` | The wallet revoked the session. |
| `pha_sessionExpired` | The session expired on the wallet side. |
| `pha_sessionEstablished` | The wallet sent a connect result right after a pairing approval. |

The client handles the last three by itself. It adopts the session from `pha_sessionEstablished`, and it clears the local session on `pha_sessionDeleted` and `pha_sessionExpired`.

A wallet pushes events over a transport that stays open, such as loopback or the relay. Over deeplink the wallet can only answer requests, with one exception: `pha_sessionEstablished` arrives over deeplink, because the wallet is in the foreground when the user approves the pairing.

## Errors

Every failed request rejects with `LinkError`. Branch on its numeric `code`:

| Code | Name | Meaning |
| --- | --- | --- |
| `-32700` | `ParseError` | A frame could not be decoded. |
| `-32600` | `InvalidRequest` | The request envelope is invalid, or the peer does not speak this protocol version. |
| `-32601` | `MethodNotFound` | The wallet does not serve the method. |
| `-32602` | `InvalidParams` | The parameters are invalid. |
| `-32603` | `InternalError` | An internal failure. The client also uses this code when a request times out. |
| `4001` | `UserRejected` | The user declined the request. |
| `4100` | `Unauthorized` | There is no valid session for the request. The client also uses this code when it sends before the channel key exists. |
| `4900` | `Disconnected` | The wallet is disconnected or locked. The client also uses this code when the transport is closed or a request could not be sent. |
| `4902` | `UnsupportedChain` | The wallet does not support the requested chain. |
| `5001` | `PayloadTooLarge` | The request is larger than the wallet accepts. `data` carries the wallet's `maxPayloadBytes`. |
| `5002` | `NexusMismatch` | The nexus or chain of the request does not match the wallet. |
| `5003` | `UnsupportedSignatureKind` | The wallet does not support the requested signature kind. |
| `5004` | `CapabilityNotSupported` | The wallet does not support the requested capability, for example a transaction format. |
| `5100` | `SessionExpired` | The session expired. |
| `5101` | `SessionRevoked` | The session was revoked. |

```ts
import { LinkError, LinkErrorCode } from 'phantasma-sdk-ts/link/v5';

try {
  await client.sendTransaction(params);
} catch (error) {
  if (error instanceof LinkError && error.code === LinkErrorCode.UserRejected) {
    // The user declined in the wallet.
  }
}
```

## Payload Size

The wallet reports its limits per transport in `capabilities.maxPayloadBytes`. Check a large transaction, such as one that carries image data, against that value before sending.

The relay transport splits an outgoing frame into chunks of 900,000 bytes, because the relay accepts at most 1 MiB per frame. It reassembles incoming messages of up to 64 chunks and refuses a reassembled message above 64 MiB of frame text.
