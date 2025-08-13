# Guideline: Private Key Storage in Applications

When integrating with Phantasma blockchain you must decide **where the private key is stored and who controls it**.
This choice affects **security, trust, and user experience**.

{% hint style="warning" %}
Hardware wallets such as Ledger are not yet supported.
Support is planned according to the [roadmap](https://phantasma.info/blockchain#roadmap).
{% endhint %}

## Two Main Approaches

### **A. Application-controlled private key**
- The app generates and stores the user's private key locally (e.g., in player settings, local storage, or secure enclave).
- The SDK signs all transactions **inside the app**.

**Pros:**
- Fully autonomous - no need for an external wallet.
- Can automate transactions without user confirmation.

**Cons:**
- **Security risk:** if your storage is compromised, the key is exposed.
- You are responsible for implementing secure storage and backup.
- Not compatible with hardware wallets (e.g., Ledger) when they require secure signing.

### **B. Wallet-controlled private key (via Phantasma Link)**
- The private key is **never stored in your app**.
- Transactions are signed by the wallet (e.g., Phantasma Link, Ledger), not by the game/app.
- The app sends signing requests to the wallet.

**Pros:**
- Lower trust requirement - your app never has access to the key.
- Users keep control of their keys.
- Works with hardware wallets.

**Cons:**
- Requires wallet installation/configuration.
- Transactions may require explicit user approval.

## Choosing the Right Approach

| Situation | Recommended Approach |
|-----------|----------------------|
| High-security assets, sensitive transactions, hardware wallet users | **Wallet-controlled key** |
| Casual/low-value use, autonomous game mechanics, no external wallet expected | **App-controlled key** |
| You want maximum user trust with minimal onboarding friction | Consider **auto-generated wallet** with clear export/import options |

{% hint style="info" %}
If you choose the **wallet-controlled** approach via Phantasma Link, make sure to install and use the dedicated **Link Client** package for your SDK.

If you choose the **application-controlled** approach (working directly with the private key), use the lower-level **Core** or equivalent packages for your SDK.
{% endhint %}

## Security Notes
- **Never** hardcode private keys in source code or binaries.
- If storing locally, protect the private key using all available security measures, such as strong encryption, a good password, and secure platform storage when possible.
- Users should be able to back up their private keys (or seed phrases) and restore them when needed. Export must be secure and intentional, using encryption, passwords, or offline methods.
- Treat a private key like a password - leaking it compromises all assets.

## Quick summary
- **App stores the key → More convenience, more risk**
- **Wallet stores the key → More security, more steps for the user**
