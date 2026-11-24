---
title: "Phantasma Link v5 For Wallets"
weight: 110
description: "Answer Phantasma Link v5 requests from dApps in a C# or Unity wallet."
---

A wallet written in C# or Unity answers Phantasma Link v5 requests from dApps with the classes of `PhantasmaPhoenix.Protocol` and `PhantasmaPhoenix.Link`. They cover the consent prompts, signing, broadcasting, sessions and three transports. The dApp side is described on [Phantasma Link v5](../ts/frontend/phantasma-link-v5.md), and the protocol on [Link Client](../../link-client/link-client.md).

Current package versions: `PhantasmaPhoenix.Protocol` 0.6.1 and `PhantasmaPhoenix.Link` 0.3.4. Install them as shown on [Setup](setup.md).

## Classes

| Class | Package | Role |
| --- | --- | --- |
| `IWalletLinkV5Ops` | `PhantasmaPhoenix.Protocol` | The operations your wallet implements: consent prompts, account data, signing and broadcasting. |
| `WalletLinkV5` | `PhantasmaPhoenix.Protocol` | The dispatcher. It parses a request, checks the session, calls your operations and builds the response. |
| `ILinkSessionStore`, `InMemoryLinkSessionStore` | `PhantasmaPhoenix.Protocol` | Storage for the sessions the user approved. |
| `LinkServer` | `PhantasmaPhoenix.Link` | The WebSocket server of a desktop wallet. |
| `LinkDeeplinkEndpoint` | `PhantasmaPhoenix.Protocol` | Handles the deeplinks a mobile wallet receives: pairing, requests and wake-up. |
| `LinkRelayClient` | `PhantasmaPhoenix.Protocol` | Connects the wallet to the relay, receives requests and publishes responses. |
| `RelayWebSocketClient` | `PhantasmaPhoenix.Link` | The WebSocket connection the relay client runs on. |
| `ILinkPairingStore`, `InMemoryLinkPairingStore` | `PhantasmaPhoenix.Protocol` | Storage for the pairings of deeplink and relay channels. |
| `LinkPairing`, `LinkPairingParams` | `PhantasmaPhoenix.Protocol` | Parses a pairing URI. |
| `LinkChannel` | `PhantasmaPhoenix.Protocol` | Encrypts and decrypts the frames of a deeplink or relay channel. |
| `LinkSignMessage` | `PhantasmaPhoenix.Protocol` | Builds the exact bytes a wallet signs for `pha_signMessage`. |

The classes of `PhantasmaPhoenix.Protocol` live in the namespace `PhantasmaPhoenix.Protocol`, and the classes of `PhantasmaPhoenix.Link` in the namespace `PhantasmaPhoenix.Link`.

## How A Request Flows

Every transport ends in the same call. The transport receives the request text and passes it to `WalletLinkV5.HandleMessage`. The dispatcher checks the request and calls one of your operations. Your operation reports its result through a callback, and the dispatcher turns it into the response text. The transport sends that text back to the dApp.

| Transport | Wallet type | C# class |
| --- | --- | --- |
| Loopback | Desktop wallet, dApp on the same machine | `LinkServer` |
| Deeplink | Mobile wallet, dApp on the same device | `LinkDeeplinkEndpoint` |
| Relay | Large requests, and a dApp on another device | `LinkRelayClient` |

The injected transport belongs to browser-extension wallets, and the C# SDK has no class for it.

Deeplink and relay frames are encrypted with the key of the pairing. The endpoint and the relay client decrypt a frame before they dispatch it. A frame that does not decrypt is dropped without an answer. Loopback frames are plain text.

## Implementing The Wallet Operations

`IWalletLinkV5Ops` has one member per wallet operation. Each operation reports through a callback, because a consent prompt finishes later on the wallet's UI thread.

| Member | Called for | Prompt | Result on success |
| --- | --- | --- | --- |
| `Status` | Every request except `pha_connect` | No | `WalletStatus.Ready`. Return `WalletStatus.Closed` while the wallet is locked; the dispatcher then answers `4900`. |
| `Connect(dappName, done)` | `pha_connect` without a session to resume | Yes | `LinkConnectResult.Ok(account, walletName, walletVersion, nexus)` |
| `GetAccount(done)` | `pha_getAccounts`, a session resume, a pairing approval | No | `LinkAccountResult.Ok(account)` |
| `GetChains(done)` | `pha_getChains`, a session resume, a pairing approval | No | `new LinkChains { Nexus = nexus }`. The dispatcher names the chain `phantasma:<nexus>`. |
| `GetWalletInfo(done)` | `pha_getWalletInfo`, a session resume, a pairing approval | No | `LinkWalletInfo` with the wallet name, version and RPC URL |
| `SignTransaction(tx, format, kind, pow, done)` | `pha_signTransaction` | Yes | `LinkSignTransactionResult.Ok(signedTx)`. The wallet does not broadcast. |
| `SendTransaction(tx, format, kind, pow, done)` | `pha_sendTransaction` | Yes | `LinkSendResult.Ok(hash)` after the broadcast |
| `SignMessage(message, display, done)` | `pha_signMessage` | Yes | `LinkSignMessageResult.Ok(signature, random)` |
| `ConfirmPairing(pairing, done)` | A pairing deeplink | Yes | `true` when the user approves |
| `InvokeScript(chain, script, done)` | `pha_invokeScript` | No | `LinkInvokeResult.Ok(results)` |

An operation that fails reports a `LinkFailure`, and the dispatcher maps it to the error code the dApp receives:

| `LinkFailure` | Code | Use it when |
| --- | --- | --- |
| `UserRejected` | `4001` | The user declined. |
| `InvalidTransaction` | `-32602` | The transaction bytes are malformed or cannot be described. |
| `NotLoggedIn` | `4900` | No account is unlocked. |
| `UnsupportedSignatureKind` | `5003` | The requested signature kind is not supported. |
| `NexusMismatch` | `5002` | The transaction names another nexus than the wallet. |
| `Internal` | `-32603` | Any other wallet-side failure, for example a node error. |

### Transaction Bytes

The `format` argument says what the bytes are and where the wallet sends them:

| `LinkTxFormat` | The bytes are | Read them with | Sign with | Broadcast with |
| --- | --- | --- | --- | --- |
| `Script` | An unsigned script `Transaction` | `Transaction.Unserialize` | `transaction.Sign(keys)`, then `transaction.ToByteArray(true)` | `PhantasmaAPI.SendRawTransactionAsync` |
| `Carbon` | A serialized `TxMsg` | `CarbonBlob.New<TxMsg>` | `TxMsgSigner.Sign(msg, keys)` | `PhantasmaAPI.SendCarbonTransactionAsync` |

The two RPC methods take the signed bytes as hex.

Unsigned script bytes end before the signature section. In `PhantasmaPhoenix.Protocol` 0.6.1, `Transaction.Unserialize` then writes a line that starts with `Error:` to the console and still returns the transaction, without signatures.

A `TxMsg` arrives with its gas offer already planned by the dApp. `TxMsgSigner` refuses a message whose `maxGas` is `0`, because the chain never admits such a message.

The chain accepts only Ed25519 signatures on transactions of both formats. The dispatcher passes `SignatureKind.Ed25519` when the request names no kind or a kind it does not know. Answer any other kind with `LinkFailure.UnsupportedSignatureKind`.

The `pow` argument carries the proof-of-work level the dApp asked for. The protocol does not let a wallet mine proof of work on a transaction the dApp built, because mining would change bytes the dApp already assembled. A transaction that needs proof of work carries it before it reaches the wallet.

### Example

The class below serves one unlocked account through one node. `askUser` is the wallet's own prompt: it shows a question and reports the user's answer. A real wallet also returns `WalletStatus.Closed` while it is locked and fills the account balances.

```csharp
using System;
using System.Threading.Tasks;
using PhantasmaPhoenix.Cryptography;
using PhantasmaPhoenix.Protocol;
using PhantasmaPhoenix.Protocol.Carbon;
using PhantasmaPhoenix.Protocol.Carbon.Blockchain;
using PhantasmaPhoenix.RPC;

/// <summary>Answers Phantasma Link v5 requests for one account through one RPC node.</summary>
public sealed class ExampleWalletOps : IWalletLinkV5Ops
{
	private const string WalletName = "Example Wallet";
	private const string WalletVersion = "1.0.0";

	private readonly PhantasmaKeys _keys;
	private readonly PhantasmaAPI _api;
	private readonly string _nexus;
	private readonly Action<string, Action<bool>> _askUser;

	public ExampleWalletOps(PhantasmaKeys keys, PhantasmaAPI api, string nexus, Action<string, Action<bool>> askUser)
	{
		_keys = keys;
		_api = api;
		_nexus = nexus;
		_askUser = askUser;
	}

	public WalletStatus Status => WalletStatus.Ready;

	public void Connect(string dappName, Action<LinkConnectResult> done)
	{
		_askUser($"Connect {dappName} to {_keys.Address.Text}?", approved =>
			done(approved
				? LinkConnectResult.Ok(Account(), WalletName, WalletVersion, _nexus)
				: LinkConnectResult.Fail(LinkFailure.UserRejected, "The user declined the connection")));
	}

	public void GetAccount(Action<LinkAccountResult> done) => done(LinkAccountResult.Ok(Account()));

	public void GetChains(Action<LinkChains> done) => done(new LinkChains { Nexus = _nexus });

	public void GetWalletInfo(Action<LinkWalletInfo> done) =>
		done(new LinkWalletInfo { Name = WalletName, Version = WalletVersion, Rpc = _api.Host });

	public void SignTransaction(byte[] serializedTx, LinkTxFormat format, SignatureKind kind, ProofOfWork pow, Action<LinkSignTransactionResult> done)
	{
		var failure = Describe(serializedTx, format, kind, out var text);
		if (failure != LinkFailure.None)
		{
			done(LinkSignTransactionResult.Fail(failure, text));
			return;
		}

		_askUser($"Sign {text}?", approved =>
			done(approved
				? LinkSignTransactionResult.Ok(Sign(serializedTx, format))
				: LinkSignTransactionResult.Fail(LinkFailure.UserRejected, "The user declined the transaction")));
	}

	public void SendTransaction(byte[] serializedTx, LinkTxFormat format, SignatureKind kind, ProofOfWork pow, Action<LinkSendResult> done)
	{
		SignTransaction(serializedTx, format, kind, pow, signed => _ = BroadcastAsync(signed, format, done));
	}

	public void SignMessage(byte[] message, string? display, Action<LinkSignMessageResult> done)
	{
		_askUser(display ?? $"Sign a message of {message.Length} bytes?", approved =>
		{
			if (!approved)
			{
				done(LinkSignMessageResult.Fail(LinkFailure.UserRejected, "The user declined the message"));
				return;
			}

			// The signed bytes are the domain tag, 32 fresh random bytes and the message.
			var random = LinkSignMessage.GenerateRandom();
			var payload = LinkSignMessage.BuildPayload(message, random);
			var signature = Ed25519Signature.Generate(_keys, payload);
			done(LinkSignMessageResult.Ok(signature.Bytes, random));
		});
	}

	public void ConfirmPairing(LinkPairingParams pairing, Action<bool> done) =>
		_askUser($"Pair with {pairing.DappName ?? "a dApp without a name"}?", done);

	public void InvokeScript(string chain, byte[] script, Action<LinkInvokeResult> done) =>
		_ = InvokeAsync(chain, script, done);

	private LinkAccount Account() => new LinkAccount { Address = _keys.Address.Text };

	/// <summary>Returns LinkFailure.None and a description for the prompt when the wallet can sign
	/// the transaction, or the failure and its reason.</summary>
	private LinkFailure Describe(byte[] serializedTx, LinkTxFormat format, SignatureKind kind, out string text)
	{
		// The chain accepts only Ed25519 signatures on transactions.
		if (kind != SignatureKind.Ed25519)
		{
			text = $"Signature kind {kind} is not supported";
			return LinkFailure.UnsupportedSignatureKind;
		}

		try
		{
			if (format == LinkTxFormat.Script)
			{
				var tx = Transaction.Unserialize(serializedTx);
				if (tx == null)
				{
					text = "The bytes are not a script transaction";
					return LinkFailure.InvalidTransaction;
				}
				if (tx.NexusName != _nexus)
				{
					text = $"The transaction is for nexus {tx.NexusName}";
					return LinkFailure.NexusMismatch;
				}
				text = $"a script transaction on chain {tx.ChainName}";
				return LinkFailure.None;
			}

			var msg = CarbonBlob.New<TxMsg>(serializedTx);
			if (msg.maxGas == 0)
			{
				text = "The transaction has no gas offer";
				return LinkFailure.InvalidTransaction;
			}
			text = $"a {msg.type} transaction with a gas offer of {msg.maxGas}";
			return LinkFailure.None;
		}
		catch (Exception e)
		{
			text = e.Message;
			return LinkFailure.InvalidTransaction;
		}
	}

	private byte[] Sign(byte[] serializedTx, LinkTxFormat format)
	{
		if (format == LinkTxFormat.Script)
		{
			var tx = Transaction.Unserialize(serializedTx)!;
			tx.Sign(_keys);
			return tx.ToByteArray(true);
		}
		return TxMsgSigner.Sign(CarbonBlob.New<TxMsg>(serializedTx), _keys);
	}

	private async Task BroadcastAsync(LinkSignTransactionResult signed, LinkTxFormat format, Action<LinkSendResult> done)
	{
		if (signed.Failure != LinkFailure.None || signed.SignedTx == null)
		{
			done(LinkSendResult.Fail(signed.Failure, signed.Message));
			return;
		}

		try
		{
			var hex = Base16.Encode(signed.SignedTx);
			var hash = format == LinkTxFormat.Script
				? await _api.SendRawTransactionAsync(hex)
				: await _api.SendCarbonTransactionAsync(hex);
			done(hash != null && Hash.TryParse(hash, out var parsed)
				? LinkSendResult.Ok(parsed)
				: LinkSendResult.Fail(LinkFailure.Internal, "The node returned no transaction hash"));
		}
		catch (Exception e)
		{
			done(LinkSendResult.Fail(LinkFailure.Internal, e.Message));
		}
	}

	private async Task InvokeAsync(string chain, byte[] script, Action<LinkInvokeResult> done)
	{
		try
		{
			var result = await _api.InvokeRawScriptAsync(chain, Base16.Encode(script));
			done(result == null
				? LinkInvokeResult.Fail(LinkFailure.Internal, "The node returned no result")
				: LinkInvokeResult.Ok(result.Results));
		}
		catch (Exception e)
		{
			done(LinkInvokeResult.Fail(LinkFailure.Internal, e.Message));
		}
	}
}
```

## The Dispatcher

Create one dispatcher for the wallet and pass it to every transport:

```csharp
var ops = new ExampleWalletOps(keys, new PhantasmaAPI("https://pharpc1.phantasma.info/rpc"), "mainnet", askUser);
var dispatcher = new WalletLinkV5(ops, new InMemoryLinkSessionStore());
```

`keys` is the account's `PhantasmaKeys`, and `askUser` is the wallet's prompt from the example above.

`HandleMessage(message, respond)` takes one request text and calls `respond` exactly once with the response text. The transports call it for you. The dispatcher checks a request in this order:

| Check | Error code |
| --- | --- |
| The text is JSON. | `-32700` |
| `plv` is `5`. | `-32600` |
| `method` is present. | `-32600` |
| For every method except `pha_connect`: `Status` is `Ready`. | `4900` |
| For every method except `pha_connect`: `session` names a stored session. | `4100` |
| No other request waits for an answer. | `-32603` |
| The method is one of the nine below. | `-32601` |

The dispatcher serves `pha_connect`, `pha_disconnect`, `pha_getAccounts`, `pha_getChains`, `pha_getWalletInfo`, `pha_signMessage`, `pha_signTransaction`, `pha_sendTransaction` and `pha_invokeScript`.

It handles one request at a time. A request that arrives while another request still waits for its answer gets `-32603`. After `PendingTakeoverSeconds` (150 by default) a new request takes over the waiting one, so a prompt the dApp abandoned does not block the wallet. When the old prompt finishes later, its answer still goes to its own request.

### Parameters And Limits

- `pha_connect` requires `params.dapp.name` (`-32602` without it).
- `pha_signTransaction` and `pha_sendTransaction` require `params.format`, `script` or `carbon` (`-32602` otherwise), and `params.tx` as non-empty base64 (`-32602` otherwise). `params.signatureKind` and `params.pow` are optional; an unknown value reads as `Ed25519` and `None`.
- `pha_signMessage` requires `params.message` as base64. `params.display` is an optional text for the prompt.
- `pha_invokeScript` takes `params.script` as base64 and `params.chain`, which defaults to `main`.
- A `tx` or a `message` longer than 44,739,244 base64 characters, the encoding of 32 MiB, gets `5001` with `data.maxPayloadBytes` set to 33554432. The dispatcher refuses it before it decodes the base64.

### Sessions

The dispatcher owns the sessions. On an approved `pha_connect` it creates a session id, stores a `LinkSessionRecord` with the dApp name and the account address, and returns the id to the dApp. The dApp sends that id with every later request.

A `pha_connect` whose `params.session` names a stored session resumes it without a prompt, when three things hold: the dApp name is the same, the wallet is `Ready`, and `GetAccount` returns the same address. Otherwise the dispatcher runs the full consent flow and creates a new session. `pha_disconnect` removes the session and succeeds for an unknown session as well.

`InMemoryLinkSessionStore` forgets the sessions when the process ends. Implement `ILinkSessionStore` with a durable medium, a file or `PlayerPrefs` in Unity, to let a returning dApp resume after a wallet restart. The dispatcher calls the store only from the thread that runs `HandleMessage`, so the store needs no locking.

### The Connect Result

| Field | Value |
| --- | --- |
| `wallet` | `{ name, version }` from `Connect`, or from `GetWalletInfo` on a resume |
| `capabilities.plvVersions` | `[5]` |
| `capabilities.methods` | The nine methods above |
| `capabilities.chains` | `["phantasma:<nexus>"]` |
| `capabilities.txFormats` | `["script", "carbon"]` |
| `capabilities.signatureKinds` | `["Ed25519", "ECDSA"]` |
| `capabilities.maxPayloadBytes` | `{ "loopback": 33554432 }` |
| `account` | `{ address, name, avatar, balances }`; a balance is `{ symbol, value, decimals }`, plus `ids` when the list is not empty |
| `session` | `{ id }` |

### Events

The dispatcher builds two events, which the deeplink endpoint and the relay client send:

- `pha_sessionEstablished`: the connect result, sent right after the user approves a pairing. `EstablishConsentedSession(dappName, deliver)` creates the session without a prompt, because the pairing prompt already covered account access. It delivers nothing when the wallet is not `Ready` or has no account; the dApp then sends `pha_connect`, which prompts.
- `pha_sessionDeleted`: sent when the wallet evicts, expires or revokes the session of a relay pairing. `BuildSessionDeletedEnvelope(sessionId)` builds it.

## Desktop Wallets: Loopback

`LinkServer` is a WebSocket server on port 7090 (`WalletLink.WebSocketPort`). It listens on every network interface of the machine (`IPAddress.Any`). It serves the v1-v4 protocol on the path `/phantasma` and Phantasma Link v5 on `/phantasma/v5`. The constructor takes the v1-v4 dispatcher, `WalletLink`, and optionally the v5 one; without a `WalletLinkV5` the server serves only `/phantasma`.

```csharp
var server = new LinkServer(legacyLink, dispatcher);
server.OnUI = runOnUiThread;
server.OnUserMessage = text => showNotice(text);
server.Start();
```

`legacyLink` is the wallet's own subclass of `WalletLink`, which answers v1-v4 requests. `runOnUiThread` is an `Action<Action>` that runs an action on the wallet's UI thread, and `showNotice` is the wallet's own notice.

| Member | Meaning |
| --- | --- |
| `Start()` | Opens the port and starts accepting connections. |
| `OnUI` | Receives every request as an action that calls the dispatcher. Run it on the UI thread, because the operations prompt the user. Without `OnUI` the server answers no request. |
| `OnUserMessage` | Receives a message for the user, for example when port 7090 is taken. |
| `OnMessageBack` | Receives every response text after it is sent. |
| `Tick()` | Sends a ping on every open connection whose last ping or pong is 5 seconds old. The server sends no ping by itself, so call `Tick` regularly, for example from the wallet's update loop. |
| `Stop()` | Stops the server. In version 0.3.4 the accept callback that is still waiting then throws `InvalidOperationException` (`listener is null`) on a thread-pool thread, and that ends a .NET process. |

## Mobile Wallets: Deeplinks

`LinkDeeplinkEndpoint` handles the URLs the operating system passes to the wallet app. It recognizes a URL by the end of its path:

| Path | Meaning |
| --- | --- |
| `/v5/pair` | A pairing request. The fragment carries the pairing material. |
| `/v5/req` | A request: `#t=<topic>&f=<encrypted frame>`. |
| `/v5/wake` | Carries nothing. The wallet connects to the relay and reads the requests waiting there. |

```csharp
var pairings = new InMemoryLinkPairingStore();
var relay = new LinkRelayClient(dispatcher, pairings, new RelayWebSocketClient(), runOnUiThread);
var deeplinks = new LinkDeeplinkEndpoint(dispatcher, ops, pairings, relay);
relay.EnsureConnected();

// Every URL the app receives goes to the endpoint first.
if (!deeplinks.TryHandle(url, openUrl))
{
	// Not a Phantasma Link v5 URL.
}
```

`openUrl` is the wallet's own way to open a URL. The endpoint uses it to answer the dApp. `TryHandle` returns `true` for every v5 URL, also for one it dropped as invalid.

The endpoint matches the path suffix, so it serves both forms of a link: the universal links under `https://link.phantasma.info/v5/` and the custom scheme `phantasma://v5/`. The association files on `link.phantasma.info` name the Poltergeist Lite app, so the operating system opens those universal links in Poltergeist Lite. Another wallet registers the `phantasma://` scheme, and pairs across devices by scanning the dApp's QR code.

### Pairing

A pairing URI carries a topic, which identifies the channel, and the key material in one of two modes:

| Mode | The URI carries | The wallet needs |
| --- | --- | --- |
| Symmetric | `sk`: the 32-byte channel key. The dApp uses this mode on channels that no other app can read: a QR code or a universal link. | A callback URL or a relay to answer through. |
| ECDH | `pk`: the dApp's X25519 public key. The dApp uses this mode on the custom scheme, which another app could read. | A relay, a `LinkRelayClient` and a dApp name. The wallet creates its own key pair and derives the channel key. |

The endpoint drops a pairing that does not meet the needs of its mode. Otherwise it calls `ConfirmPairing`. When the user approves, it stores a `LinkPairingRecord` and subscribes to the topic on the relay when the pairing names one.

Then, if the pairing names the dApp, the wallet sends the connect result at once as `pha_sessionEstablished`, so the first connection takes one approval. An ECDH pairing sends it through the relay together with the wallet's public key, from which the dApp derives the channel key. A symmetric pairing uses the relay when it has one, and the callback URL otherwise. A pairing without a dApp name gets no such event; the dApp then sends `pha_connect`, which prompts.

### Requests And Responses

For a `/v5/req` link the endpoint finds the pairing by topic, decrypts the frame with the pairing key and passes the request to the dispatcher. It answers by opening the callback URL of the pairing with the encrypted response: `<callback>#plv=5&t=<topic>&f=<encrypted frame>`. A request for an unknown topic, or a frame that does not decrypt, gets no answer.

The constructor accepts a `log` delegate for diagnostics. The endpoint writes the kind of event, the topic, the pairing mode, whether the pairing has a relay and a callback, and the host of the callback URL. It never writes a key or a frame.

## The Relay

`LinkRelayClient` keeps one WebSocket connection per relay URL. It subscribes to the topics of the stored pairings that name a relay, decrypts each delivered frame with the pairing key, passes it to the dispatcher and publishes the encrypted response. The relay never sees plain text.

```csharp
var relay = new LinkRelayClient(
	dispatcher,
	pairings,
	new RelayWebSocketClient(),
	marshal: runOnUiThread,
	log: line => writeLog(line));
```

`writeLog` is the wallet's own logger. The relay client reconnects by itself, so the log is the only way to see a broken connection.

| Parameter | Default | Meaning |
| --- | --- | --- |
| `marshal` | Runs inline | Runs the dispatcher work. Socket events arrive on any thread, and the operations prompt the user, so a Unity wallet passes its main-thread hook. |
| `reconnectDelaysMs` | 1000, 2000, 5000, 15000, 30000 | The waits between reconnect attempts; the last value repeats. |
| `log` | None | Receives connection events and relay errors. |
| `relaySessionCap` | 6 | How many relay pairings stay subscribed. The relay accepts 8 topics per connection by default. |
| `idleTtl` | 7 days | A pairing without a request for this long is removed. |

| Member | Meaning |
| --- | --- |
| `EnsureConnected()` | Connects to the relays of the stored pairings and subscribes to their topics. Call it when the wallet starts. The endpoint calls it for `/v5/wake`. |
| `TrackPairing(record)` | Subscribes to the topic of a new pairing. The endpoint calls it after an approval. |
| `RevokeSession(sessionId)` | Ends a session the user revoked: sends `pha_sessionDeleted`, unsubscribes the topic and removes the pairing. |
| `PublishSealed(record, envelope)` | Encrypts a response and publishes it on the pairing topic. |
| `NormalizeRelayUrl(relay)` | Turns the `relay` value of a pairing URI into a URL: a host `h` becomes `wss://h/relay`, and a value with `://` stays as it is. |
| `Dispose()` | Closes every connection. |

`EnsureConnected` and `TrackPairing` also clean up the pairings. They remove a pairing idle for longer than `idleTtl`, keep the most recently used pairings subscribed up to `relaySessionCap`, and remove the rest. Before the client removes a pairing that established a session, it sends `pha_sessionDeleted`, so the dApp pairs again and does not wait for an answer.

A response longer than 900,000 characters is published in chunks of that size. A response that needs more than 64 chunks is not sent. The client reassembles incoming chunks up to 64 MiB of frame text per message and 8 messages at a time, and drops a message that stays incomplete for 120 seconds.

## Signing A Message

For `pha_signMessage` the wallet signs `PHANTASMA_LINK_V5_MSG\n || random || message`, where `random` is 32 bytes from a cryptographic random generator. The prefix keeps a message signature from being valid as a transaction signature. `LinkSignMessage` provides the parts:

| Member | Meaning |
| --- | --- |
| `DomainTag` | The ASCII bytes of `PHANTASMA_LINK_V5_MSG\n`. |
| `RandomLength` | 32. |
| `GenerateRandom()` | Returns 32 random bytes. |
| `BuildPayload(message, random)` | Returns the bytes to sign. It throws when `random` is not 32 bytes. |

The result carries the raw 64-byte Ed25519 signature and `random`. A verifier rebuilds the payload from the original message and `random`, and checks the signature against the account address:

```csharp
var payload = LinkSignMessage.BuildPayload(message, random);
var valid = new Ed25519Signature(signature).Verify(payload, new[] { Address.Parse(accountAddress) });
```

## Storing Pairings

`InMemoryLinkPairingStore` forgets the pairings when the process ends. Implement `ILinkPairingStore` with a durable medium to keep paired dApps working after a wallet restart. A `LinkPairingRecord` holds:

| Field | Meaning |
| --- | --- |
| `Topic` | The channel id. |
| `Key` | The 32-byte channel key. |
| `CallbackUrl` | Where the wallet opens response deeplinks. |
| `RelayUrl` | The relay URL, or empty for a deeplink-only pairing. |
| `DappName` | The dApp name from the pairing URI. |
| `CreatedUtc`, `LastSeenUtc` | When the pairing was created and last used. |
| `SessionId` | The session the pairing established, used to send `pha_sessionDeleted`. |

`Key` decrypts every message of the channel. A durable store keeps it as a secret, the same way the wallet keeps its account keys.

## Related Pages

- [Link Client](../../link-client/link-client.md)
- [Phantasma Link v5](../ts/frontend/phantasma-link-v5.md)
- [Fees And Broadcasting](fees-and-broadcasting.md)
