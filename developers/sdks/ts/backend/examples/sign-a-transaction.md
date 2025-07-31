# Sign a Transaction



{% hint style="info" %}
Here's a simple example how to sign a transaction
{% endhint %}

<pre class="language-typescript"><code class="lang-typescript"><strong>import {PhantasmaKeys, Transaction} from 'phantasma-ts';
</strong><strong>/**
</strong> * Sign a transaction
 * @param transaction Transaction to sign
 */
function SignATransaction(transaction: Transaction){
  let wif = "";
  let keys = PhantasmaKeys.fromWIF(wif);
  transaction.signWithKeys(keys);
  return transaction;
}
</code></pre>
