---
description: The connecting Wallets to Dapps
---

# 🔗 Phantasma Link Client

Phantasma Link is a protocol designed to allow dapps to sign transactions and do other on-chain operations on the behalf of users, in a transparent way, without requiring access to the user private key.

{% hint style="info" %}
This page is a protocol reference, not a TypeScript guide.  
If you're building in TS, start here:
- [Frontend Guide](/developers/sdks/ts/frontend/frontend.md)

Then use these pages as needed:
- [Phantasma Link (TS)](/developers/sdks/ts/shared-methods/phantasmalink.md)
- [EasyConnect (TS)](/developers/sdks/ts/shared-methods/easyconnect.md)
- [React Wallet Connection](/developers/sdks/ts/frontend/connect-react.md)
{% endhint %}

{% hint style="info" %}
In this documentation, we will explore each method of the Phantasma Link Client, explaining their purpose and usage.
{% endhint %}

### Authorize

```csharp
protected abstract void Authorize(string dapp, string token, int version, Action<bool, string> callback);
```

The `Authorize` method is used to authenticate the user and grant the specified dApp access to the user's wallet. It requires the dApp identifier, an authentication token, and the version number. The `callback` returns a boolean indicating whether the authorization was successful and an optional error message.

### GetAccount

```csharp
protected abstract void GetAccount(string platform, int version, Action<Account, string> callback);
```

The `GetAccount` method retrieves the user's account details for the specified platform and version. The `callback` returns the account object and an optional error message.

### GetPeer

```csharp
protected abstract void GetPeer(Action<string> callback);
```

The `GetPeer` method retrieves the current peer node of the Phantasma blockchain. The `callback` returns the peer node URL.

### GetNexus

```csharp
protected abstract void GetNexus(Action<string> callback);
```

The `GetNexus` method retrieves the current nexus name of the Phantasma blockchain. The `callback` returns the nexus name.

### InvokeScript

```csharp
protected abstract void InvokeScript(string chain, byte[] script, int id, Action<string[], string> callback);
```

The `InvokeScript` method allows you to execute a script on the specified chain in the Phantasma blockchain. It requires the chain name, the script as a byte array, and a unique identifier. The `callback` returns an array of results and an optional error message.

### SignData

```csharp
protected abstract void SignData(string platform, SignatureKind kind, byte[] data, int id, Action<string, string, string> callback);
```

The `SignData` method signs a given data using the user's private key. It requires the platform, the signature type, the data as a byte array, and a unique identifier. The `callback` returns the signed data, random appended bytes, and an optional error message.

### SignTransactionSignature

```csharp
protected abstract void SignTransactionSignature(Phantasma.Core.Domain.Transaction transaction, string platform, SignatureKind kind, Action<Phantasma.Core.Cryptography.Signature, string> callback);
```

The `SignTransactionSignature` method signs a given transaction using the user's private key. It requires the transaction object, the platform, and the signature type. The `callback` returns the transaction signature and an optional error message.

### FetchAndMultiSignature

```csharp
protected abstract void FetchAndMultiSignature(string subject, string platform, SignatureKind kind, int id, Action<bool, string> callback);
```

The `FetchAndMultiSignature` method retrieves the user's multi-signature account for the specified subject and platform, signs it with the user's private key, and submits it to the blockchain. It requires the subject, the platform, the signature type, and a unique identifier. The `callback` returns a boolean indicating the success of the operation and an optional error message.

### SignTransaction

```csharp
protected abstract void SignTransaction(string platform, SignatureKind kind, string chain, byte[] script, byte[] payload, int id, ProofOfWork pow, Action<Hash, string> callback);
```

The `SignTransaction` method creates, signs, and broadcasts a transaction to the Phantasma blockchain. It requires the platform, the signature type, the chain name, the script and payload as byte arrays, a unique identifier, and an optional Proof of Work (PoW) object. The `callback` returns the transaction hash and an optional error message.

### WriteArchive

```csharp
protected abstract void WriteArchive(Hash hash, int blockIndex, byte[] data, Action<bool, string> callback);
```

The `WriteArchive` method writes data to the Phantasma blockchain's archive. It requires the archive hash, the block index, and the data as a byte array. The `callback` returns a boolean indicating the success of the operation and an optional error message.

With this documentation, you should now have a better understanding of the methods available in the Phantasma Link Client and how they can be used to interact with the Phantasma blockchain. Developers can implement these methods in their projects to facilitate easy and secure interaction with the Phantasma ecosystem, providing users with seamless access to decentralized applications and digital asset management.
