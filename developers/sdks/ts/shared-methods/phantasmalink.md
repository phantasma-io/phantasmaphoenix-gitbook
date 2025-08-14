# Phantasma Link

### Introduction

PhantasmaLink is a core component designed for interacting with Phantasma-based wallets. It acts as a foundational block for connecting with wallets.&#x20;

### Class Initialization

PhantasmaLink is a class, and to use it, you must first create an instance of the class.

```javascript
let dappID = "Dapp Name"; // Name for the connection
let consoleLogging = true; // Enable console logging for debugging (default: true)

let Link = new PhantasmaLink(dappID, consoleLogging);
```

### Vocabulary

* **Callback:** A function called after a successful operation.
* **onErrorCallback:** A function called after a failed operation.
* **Script:** Instructions for PhantasmaChain within a transaction object. See ScriptBuilder for more details.
* **Nexus:** The Phantasma chain in use, either 'mainnet' or 'testnet'.
* **Payload:** Additional data attached to a transaction object.
* **ProviderHint:** Informs PhantasmaLink about the intended wallet for connection.

### Functions

1. **login(onLoginCallback, onErrorCallback, providerHint):**
   * Purpose: Initiates login.
   * Parameters:
     * `providerHint`: Can be 'ecto' or 'poltergeist'.
2. **invokeScript(script, callback):**
   * Executes a read-only script operation on the Phantasma Blockchain.
3. **signTx(nexus, script, payload, callback, onErrorCallback):**
   * Signs a transaction through the wallet.
4. **signTxPow(nexus, script, payload, proofOfWork, callback, onErrorCallback):**
   * Signs a transaction with Proof of Work attached.
5. **getPeer(callback, onErrorCallback):**
   * Retrieves the peer list for the connected network.
6. **signData(data, callback, onErrorCallback):**
   * Signs data through the wallet.
7. **toggleMessageLogging():**
   * Toggles console message logging.
8. **dappID():**
   * Returns the Dapp ID.
9. **sendLinkRequest(request, callback):**
   * Internal use for sending wallet instructions through a socket.
10. **createSocket(), retry(), disconnect(message):**
    * Internal functions for socket management.

### ProofOfWork Enumeration

Defines levels of proof of work:

```javascript
enum ProofOfWork {
    None = 0,
    Minimal = 5,
    Moderate = 15,
    Hard = 19,
    Heavy = 24,
    Extreme = 30
}
```

### Usage Examples

Provide code snippets and examples demonstrating how to use the various functions of PhantasmaLink.

#### Login to a wallet

{% content-ref url="../frontend/examples/connect-to-the-wallet.md" %}
[connect-to-the-wallet.md](../frontend/examples/connect-to-the-wallet.md)
{% endcontent-ref %}

#### Invoking a Script

{% content-ref url="../frontend/examples/invoking-a-script.md" %}
[invoking-a-script.md](../frontend/examples/invoking-a-script.md)
{% endcontent-ref %}

#### Sending a Transaction

{% content-ref url="../frontend/examples/sending-a-transaction.md" %}
[sending-a-transaction.md](../frontend/examples/sending-a-transaction.md)
{% endcontent-ref %}
