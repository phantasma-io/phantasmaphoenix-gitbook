# Sending a transaction

{% hint style="info" %}
After sending the transaction, you might receive a popup on the wallet that you're using to allow the transaction to go through.
{% endhint %}

{% hint style="info" %}
**Need** **help** understanding how to create a Script ( a call to a blockchain to execute a chain of commands ) ? Check the following page.
{% endhint %}

{% content-ref url="../../shared-methods/scriptbuilder/create-a-script.md" %}
[create-a-script.md](../../shared-methods/scriptbuilder/create-a-script.md)
{% endcontent-ref %}

## Using Phantasma Link

The `signTx` is the method that will call the Wallet for the user to **accept** or **reject** the transaction.

<pre class="language-typescript" data-overflow="wrap" data-line-numbers><code class="lang-typescript">import { PhantasmaLink, ScriptBuilder, Address, Base16 } from 'phantasma-ts';

let gasPrice = 100000;
<strong>let gasLimit = 210000;
</strong>
// Link variable is from the Connect to the Wallet example.

if (!Link.account) {
    // Account not logged in.
    return;
}

const from = Address.FromText(String(Link.account.address));

const payload = Base16.encode('Example.' + contractName);
const sb = new ScriptBuilder();
const myScript = sb.AllowGas(from, Address.Null, gasPrice, gasLimit)
    .CallContract(contractName, contractMethod, args)
    .SpendGas(from)
    .EndScript();

Link.signTx(myScript, payload, async function (txHash) {
    console.log(txHash);
function () {
    // Error On Sending the transaction.
});
</code></pre>
