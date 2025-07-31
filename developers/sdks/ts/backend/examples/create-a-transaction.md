# Create a Transaction

### Creating a Transaction

This how to create a transaction.

<pre class="language-typescript"><code class="lang-typescript">import {PhantasmaKeys, Transaction} from 'phantasma-ts';
<strong>const NexusName = "testnet"; // Could also be simnet or mainnet
</strong><strong>const ChainName = "main"; // Since we only have the main chain, it's always main.
</strong><strong>let payload = Base16.encode("Phantasma-NodeJS"); // This is what going to appear on the explorer and on the wallet.
</strong>let expiration: Date = new Date(Date.UTC(
 new Date().getUTCFullYear(),
 new Date().getUTCMonth(),
 new Date().getUTCDate(),
 new Date().getUTCHours() + 1,
 new Date().getUTCMinutes() + 10,
 new Date().getUTCSeconds() + 10
));

let transaction = new Transaction(
 NexusName,  //Nexus Name
 ChainName,     //Chain
 myScript,     //In string format
 expiration, //Date Object
 payload     //Extra Info to attach to Transaction in Serialized Hex
);
</code></pre>

### Sign a Transaction

Now we need to sign the transaction if we want it to be accepted by the blockchain.

<pre class="language-javascript"><code class="lang-javascript"><strong>import {PhantasmaKeys} from 'phantasma-ts';
</strong>let wif = ""; // WIF of your wallet 
let keys = PhantasmaKeys.fromWIF(wif);

transaction.signWithKeys(keys);
let transactionSignedBytes = transaction.toString(true); 
</code></pre>
