# Sending a Transaction

{% hint style="info" %}
After sending the transaction, you might receive a popup on the wallet that you're using to allow the transaction to go through.
{% endhint %}

{% hint style="info" %}
**Need** **help** understanding how to create a Script ( a call to a blockchain to execute a chain of commands ) ? Check the following page.
{% endhint %}

{% content-ref url="../../shared-methods/script-builder.md" %}
[script-builder.md](../../shared-methods/script-builder.md)
{% endcontent-ref %}

## Using PhantasmaLink

The `signTx` method asks the wallet to sign and broadcast the transaction.

```ts
import { Address, DomainSettings, PhantasmaLink, ScriptBuilder } from "phantasma-sdk-ts";

const Link = new PhantasmaLink("My Dapp", true);

Link.login(
  (success) => {
    if (!success) return;

    // Link variable is from the Connect to the Wallet example.
    if (!Link.account) {
      // Account not logged in.
      return;
    }

    const gasPrice = DomainSettings.DefaultMinimumGasFee;
    const gasLimit = 21000;

    const contractName = "stake";
    const contractMethod = "Claim";
    const args = [Link.account.address, Link.account.address];

    const from = Address.FromText(Link.account.address);

    const script = new ScriptBuilder()
      .BeginScript()
      .AllowGas(from, Address.Null, gasPrice, gasLimit)
      .CallContract(contractName, contractMethod, args)
      .SpendGas(from)
      .EndScript();

    const payload = `Example.${contractName}`; // raw string, NOT base16

    Link.signTx(
      script,
      payload,
      (result) => {
        if (result?.hash) {
          console.log("Transaction hash:", result.hash);
        } else {
          console.log("signTx result:", result);
        }
      },
      (error) => {
        // Error On Sending the transaction.
        console.error("Transaction failed:", error);
      }
    );
  },
  (error) => {
    console.error("Login failed:", error);
  },
  4,
  "phantasma",
  "poltergeist"
);
```
