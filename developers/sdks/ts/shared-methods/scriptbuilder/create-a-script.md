# Create a Script

To execute code in the blockchain, you need to create a **Script**, using **ScriptBuilder**.

First, let's instantiate the **ScriptBuilder**

```javascript
import { Address, ScriptBuilder } from "phantasma-sdk-ts"
let scriptBuilder = new ScriptBuilder();
```

### Allow Gas

This method is used to allow a dApp or a wallet to make use some **GAS (** KCAL to execute a function that will change something in the blockchain. **)**

**Parameters**

* **From**: Address or String
* **Target**: Address or String, Normally used a Address.Null or a SmartContract Address.
* **GasPrice**: Number, Normally used the **default** Gas Price: 100000
* **GasLimit**: Number, This is the max Gas that can be used to execute this transaction.

{% hint style="info" %}
When you have a **AllowGas**, you will always need to have a **SpendGas**
{% endhint %}

```javascript
let fromAddress = Address.FromText(Address.NullText); // your address here
let toAddress = Address.FromText(Address.NullText); // your address here
let gasPrice = 100000;
let gasLimit = 210000;
let tokenSymbol = "SOUL";
let amount = 100000000;
```

It can be used like this.

```javascript
let script = scriptBuilder
    .AllowGas(fromAddress.Text, Address.Null, gasPrice, gasLimit)
    .CallInterop("Runtime.TransferTokens", [fromAddress.Text, toAddress, tokenSymbol, amount]) 
    .SpendGas(fromAddress.Text)
    .EndScript();
```

### Spend Gas

This method is used to Spend the Gas a dApp or a wallet to used for the transaction.

**Parameters**

* **From**: Address or String, the Address that will pay for the transaction.

{% hint style="info" %}
When you have a **AllowGas**, you will always need to have a **SpendGas**
{% endhint %}

<pre class="language-javascript"><code class="lang-javascript"><strong>let fromAddress = "";
</strong><strong>let targetAddress = Address.Null;
</strong><strong>let gasPrice = 100000;
</strong><strong>let gasLimit = 210000;
</strong><strong>let tokenSymbol = "SOUL";
</strong><strong>
</strong><strong>// This method belong to the ScriptBuilder.
</strong><strong>SpendGas(fromAddress);
</strong></code></pre>

An example on how it could be used.

```javascript
let script = scriptBuilder
    .AllowGas(fromAddress.Text, Address.Null, gasPrice, gasLimit)
    .CallInterop("Runtime.TransferTokens", [fromAddress.Text, toAddress, tokenSymbol, amount]) 
    .SpendGas(fromAddress.Text)
    .EndScript();
```

### Call Interop

This method is used to Call an Internal Operation in the blockchain, you can check the list of possible Internal Operations that you can call [here](https://app.gitbook.com/s/PmRIerRvyRSGopMwjYP3/phantasma-scriptbuilder/external-calls).

**Parameters**

* Method Name: String, Check the list for more details.
* An array with the arguments needed.

In this example we'll be checking the **Runtime.TransferTokens**

```javascript
let script = scriptBuilder
    .AllowGas(fromAddress.Text, Address.Null, gasPrice, gasLimit)
    .CallInterop("Runtime.TransferTokens", [fromAddress.Text, toAddress, tokenSymbol, amount]) 
    .SpendGas(fromAddress.Text)
    .EndScript();
```

### Call Contract

This method is used to Call a Contract Method that is deployed in the blockchain.

**Parameters**

* Contract Name: String
* Method Name: String, the name of the method inside of the contract.
* An array with the arguments needed to call that method.

In this example we will be calling the **Stake contract** the stake Method.

{% hint style="info" %}
A normal **contract** will be always **lowercased** and a Token contract will be always **Uppercased**.

Example:

* "stake" -> Stake Contract
* "SOUL" -> SOUL Token Contract.
{% endhint %}

```javascript
let script = scriptBuilder
    .AllowGas(fromAddress.Text, Address.Null, gasPrice, gasLimit)
    .CallContract("stake", "Stake", [fromAddress.Text, amount]) 
    .SpendGas(fromAddress.Text)
    .EndScript();
```
