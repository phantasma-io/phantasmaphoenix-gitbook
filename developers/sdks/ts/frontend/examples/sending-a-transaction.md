# Sending a Transaction

{% hint style="info" %}
The wallet can prompt the user to approve the transaction before it broadcasts
the signed payload.
{% endhint %}

{% hint style="info" %}
Use the script builder page when you need to create the VM script for the
transaction.
{% endhint %}

{% content-ref url="../../shared-methods/script-builder.md" %}
[script-builder.md](../../shared-methods/script-builder.md)
{% endcontent-ref %}

## Using PhantasmaLink

The `signTx` method asks the wallet to sign and broadcast the transaction.

```ts
import { Address, DomainSettings, PhantasmaLink, ScriptBuilder } from "phantasma-sdk-ts/public";

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

    const from = Address.fromText(Link.account.address);

    const script = new ScriptBuilder()
      .beginScript()
      .allowGas(from, Address.nullAddress, gasPrice, gasLimit)
      .callContract(contractName, contractMethod, args)
      .spendGas(from)
      .endScript();

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
