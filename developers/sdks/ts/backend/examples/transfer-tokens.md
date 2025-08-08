# Transfer Tokens

Here's an example how to make a Token transfer in a backend using typescript.

```ts
import {PhantasmaKeys, ScriptBuilder, Transaction, PhantasmaAPI, Base16, Address } from 'phantasma-sdk-ts';
async function TransferTokens() {
  let wif = "";
  let keys = PhantasmaKeys.fromWIF(wif);

  let fromAddress = keys.Address;

  let toAddress = "exampleAddress";

  const amount = String(1 * 10 ** 8); // 1 Soul
  const tokenSymbol = "SOUL";
  const payload = Base16.encode("Phantasma-NodeJS");
  let gasPrice = 100000;
  let gasLimit = 210000;

  let sb = new ScriptBuilder();
  let script = sb
    .AllowGas(fromAddress.Text, Address.Null, gasPrice, gasLimit)
    .CallInterop("Runtime.TransferTokens", [
      fromAddress.Text,
      toAddress,
      tokenSymbol,
      amount,
    ])
    .SpendGas(fromAddress.Text)
    .EndScript();

  let myScript = sb.str;

  let expiration: Date = new Date(Date.UTC(
        new Date().getUTCFullYear(),
        new Date().getUTCMonth(),
        new Date().getUTCDate(),
        new Date().getUTCHours() + 1,
        new Date().getUTCMinutes() + 10,
        new Date().getUTCSeconds() + 10
    ));

  let transaction = new Transaction(
    "testnet", //Nexus Name
    "main", //Chain
    myScript, //In string format
    expiration, //Date Object
    payload //Extra Info to attach to Transaction in Serialized Hex
  );
  
  transaction.signWithKeys(keys);
  const transactionSigned = transaction.toString(true);

  let txHash = await RPC.sendRawTransaction(transactionSigned);
  console.log({ txHash });
  await delay(5000);
  let result = await RPC.getTransaction(txHash);
  return txHash;
}
```
