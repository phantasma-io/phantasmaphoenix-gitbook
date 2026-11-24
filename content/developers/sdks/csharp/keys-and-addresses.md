---
title: "Keys And Addresses"
weight: 40
description: "Create, import and use Phantasma keys and addresses in C#."
---

Keys, addresses, signatures and hashes live in the package `PhantasmaPhoenix.Cryptography`, namespace `PhantasmaPhoenix.Cryptography`. The full member list is on [Keys, VM, and Transactions](reference/keys-vm-and-transactions.md).

## Create And Import Keys

`PhantasmaKeys` holds one Ed25519 key pair. It derives the public key and the address from the 32-byte private key.

```csharp
using PhantasmaPhoenix.Cryptography;

// A new random key.
var keys = PhantasmaKeys.Generate();

// The same key, exported and imported as WIF.
var wif = keys.ToWIF();
var imported = PhantasmaKeys.FromWIF(wif);

// The same key from its raw bytes, for example read from hex.
var fromHex = new PhantasmaKeys(Base16.Decode(Base16.Encode(keys.PrivateKey))!);

Console.WriteLine(keys.Address.Text);
Console.WriteLine(imported.Address.Text == keys.Address.Text);
Console.WriteLine(Base16.Encode(fromHex.PublicKey));
```

| Member | Meaning |
| --- | --- |
| `PhantasmaKeys.Generate()` | Returns a key pair with 32 random bytes as the private key. |
| `PhantasmaKeys.FromWIF(wif)` | Decodes a WIF string. It throws when the decoded data is not 34 bytes that start with `0x80` and end with `0x01`. |
| `new PhantasmaKeys(privateKey)` | Takes 32 bytes. Of a 64-byte array it keeps the first 32. Any other length throws. |
| `ToWIF()` | Returns the private key as WIF. |
| `PrivateKey`, `PublicKey` | The 32-byte private key and the 32-byte public key. |
| `Address` | The user address of the public key. |

A WIF string or a private key gives full control of the account. Keep it out of source code and logs.

## Seed Phrases

`Mnemonics` creates English BIP-39 seed phrases and derives keys from a phrase:

```csharp
using PhantasmaPhoenix.Cryptography;

var phrase = Mnemonics.GenerateMnemonic(MnemonicPhraseLength.Twelve_Words);

var (privateKey, wrongWord) = Mnemonics.MnemonicToPK(phrase);
if (privateKey == null)
{
	throw new ArgumentException(wrongWord == null
		? "The phrase is not a valid seed phrase"
		: $"The word '{wrongWord}' is not in the word list");
}

var keys = new PhantasmaKeys(privateKey);
Console.WriteLine(keys.Address.Text);
```

| Member | Meaning |
| --- | --- |
| `GenerateMnemonic(length)` | Returns a new phrase of 12 words (`MnemonicPhraseLength.Twelve_Words`) or 24 words (`Twenty_Four_Words`). |
| `MnemonicToPK(phrase, index = 0)` | Derives the private key at the path `m/44'/60'/0'/0/<index>` and returns it. On failure it returns `null` and the word that is not in the word list, or `null` for that word when the phrase is invalid for another reason. |
| `MnemonicToWif(phrase, index = 0)` | The same derivation, returned as WIF. |

The `index` selects one of the accounts of the same phrase.

## Addresses

An address is 34 bytes: a kind byte, a reserved byte and 32 bytes of key or hash data. Its text form starts with a letter for its kind:

| Prefix | Kind | Example source |
| --- | --- | --- |
| `P` | User: an account with a public key | `keys.Address` |
| `S` | System: a token, a contract, an organization or another chain-owned address | `Address.FromHash(...)` |
| `X` | Interop: an address derived from a 33-byte public key | `Address.FromKey(...)` |

The null address has the text `NULL` and the value `Address.Null`.

```csharp
using PhantasmaPhoenix.Cryptography;

var text = "P2KJPTC82NAFEzXg3X4eA83JvyWQ8PJVaBop2fUUsKPBcou";

if (Address.IsValidAddress(text))
{
	var address = Address.Parse(text);
	Console.WriteLine(address.IsUser);
	Console.WriteLine(Base16.Encode(address.GetPublicKey()));
}
```

| Member | Meaning |
| --- | --- |
| `Address.Parse(text, checkReservedByte = true)` | Reads a text address. It throws on a wrong length, a wrong prefix for the address kind, or a reserved byte that is not zero. |
| `Address.IsValidAddress(text)` | Returns `true` when `Parse` succeeds. |
| `Text` | The text form, or `NULL` for the null address. |
| `GetPublicKey()` | The 32 bytes after the kind byte and the reserved byte. |
| `IsUser`, `IsSystem`, `IsInterop`, `IsNull`, `Kind` | The kind of the address. |

Structured transactions name accounts by their 32-byte public key. `new Bytes32(keys.PublicKey)` or `new Bytes32(address.GetPublicKey())` gives that form; `Bytes32` is in the namespace `PhantasmaPhoenix.Protocol.Carbon`.

## Signing And Verifying

`keys.Sign(message)` returns an `Ed25519Signature` over the bytes. `Verify(message, addresses)` returns `true` when the signature belongs to one of the user addresses:

```csharp
using System.Text;
using PhantasmaPhoenix.Cryptography;

var keys = PhantasmaKeys.Generate();
var message = Encoding.UTF8.GetBytes("Example message");

var signature = (Ed25519Signature)keys.Sign(message);
var valid = signature.Verify(message, new[] { keys.Address });

// The raw 64 bytes, and a check against a bare public key.
var raw = signature.Bytes;
var validRaw = Ed25519.Verify(raw, message, keys.PublicKey);
```

A signature over arbitrary bytes can also be a valid transaction signature when the bytes are a transaction. A wallet that signs messages for other parties adds a prefix that no transaction can start with; Phantasma Link v5 does that, see [Phantasma Link v5 For Wallets](wallet-link-v5.md#signing-a-message).

## Hashes And Encodings

| Member | Meaning |
| --- | --- |
| `Hash.Parse(text)` | Reads a 64-character hex hash, with or without `0x`. Transaction and block hashes are shown in this form. |
| `Hash.TryParse(text, out hash)` | The same without an exception. |
| `Hash.FromBytes(bytes)` | Uses 32 bytes as they are and hashes any other length with SHA-256. |
| `Base16.Encode(bytes)`, `Base16.Decode(text, allowExceptions = true)` | Hex. `Decode` accepts an optional `0x`. On bad input it throws, or returns `null` when `allowExceptions` is `false`. |
| `Base58.Encode(bytes)`, `Base58.Decode(text)` | The Base58 encoding of addresses and WIF. |

## Related Pages

- [Keys, VM, and Transactions](reference/keys-vm-and-transactions.md)
- [Seed Phrase](examples/seed-phrase.md)
- [Private Key Guideline](../../private-key-guideline.md)
