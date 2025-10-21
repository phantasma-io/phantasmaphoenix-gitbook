# Transfer Tokens

Here's an example how to make a Token transfer.

```ts
import {
  Base16,
  DomainSettings,
  PhantasmaAPI,
  PhantasmaKeys,
  ScriptBuilder,
  Transaction,
  TransactionData,
} from "phantasma-sdk-ts";

const soulTokenDecimals = 8;
const soulTokenSymbol = "SOUL";

const runningTxStateName = "Running";
const breakTxStateName = "Break";
const faultTxStateName = "Fault";
const haltTxStateName = "Halt";

export async function transferSoulTokens() {
  // const rpcUrl = "https://pharpc1.phantasma.info/rpc";
  const rpcUrl = "https://testnet.phantasma.info/rpc";

  // const nexus = "mainnet";
  const nexus = "testnet";

  const amountFloat = 1.01; // 1.01 SOUL, sample value
  let senderWif = "YOUR_WIF"; //Private key in WIF format

  let amount = (amountFloat * 10 ** soulTokenDecimals).toString(); // Convert to blockchain units

  let keys = PhantasmaKeys.fromWIF(senderWif);
  let senderAddress = keys.Address;

  let recepientAddress = "P2KHhbVZWDv1ZLLoJccN3PUAb9x9BqRnUyH3ZEhu5YwBeJQ";

  // Creating RPC connection
  let rpc = new PhantasmaAPI(rpcUrl, null, nexus);

  // Set Gas parameters for Runtime.TransferTokens
  let gasPrice = DomainSettings.DefaultMinimumGasFee;
  let gasLimit = 2100;

  // Creating a new Script Builder Object
  let sb = new ScriptBuilder();

  // Making a Script
  let script = sb
    .BeginScript()
    .AllowGas(senderAddress, sb.NullAddress, gasPrice, gasLimit)
    .CallInterop("Runtime.TransferTokens", [
      senderAddress,
      recepientAddress,
      soulTokenSymbol,
      amount,
    ])
    .SpendGas(senderAddress)
    .EndScript();

  // Set expiration date
  let expiration = Math.floor(Date.now() / 1000) + 30;
  let expiration_date = new Date(expiration * 1000);

  let payload = Base16.encode("sdk-ts");

  // Creating New Transaction Object
  let transaction = new Transaction(
    nexus,
    "main",
    script,
    expiration_date,
    payload,
  );

  transaction.signWithKeys(keys);

  let hexEncodedTx = transaction.toString(true); //converts trasnaction to base16 string -true means transaction is signed-
  console.log("Broadcasting transaction:", hexEncodedTx);

  // Broadcasting transaction
  let txHash = await rpc.sendRawTransaction(hexEncodedTx);
  console.log("Broadcased tx hash:", txHash);

  const start = Date.now();
  const timeoutMs = 60_000; // 60 seconds total
  const intervalMs = 2_000; // poll every 2 seconds
  let verified = false;

  console.log("Waiting up to 60s for transaction execution state...");

  while (Date.now() - start < timeoutMs) {
    try {
      const txInfo: TransactionData = await rpc.getTransaction(txHash);

      // Print only the state field for clarity
      console.log("getTransaction response: state:", txInfo.state);

      // txInfo.state is provided by the SDK as a string name (e.g. "Running","Halt", etc.)
      const stateStr = txInfo.state;

      if (stateStr === runningTxStateName) {
        // still running -> continue polling
      } else if (
        stateStr === breakTxStateName ||
        stateStr === faultTxStateName
      ) {
        // Break or Fault -> failure
        console.log(
          `Transaction failed: ${stateStr} result: '${txInfo.result}'`,
        );
        verified = true;
        break;
      } else if (stateStr === haltTxStateName) {
        // Halt -> success
        console.log("Transaction succeeded");
        return { success: true, result: txInfo.result };
      } else {
        // Unknown state name -> log and continue polling
        console.log("Unknown ExecutionState value:", stateStr);
      }
    } catch (err) {
      // Transient RPC errors are logged and retried until timeout
      const e = err as Error;
      console.log(
        "Error while checking transaction status (will retry):",
        e && e.message ? e.message : String(err),
      );
    }

    // wait before next poll
    await new Promise((r) => setTimeout(r, intervalMs));
  }

  if (!verified) {
    console.log(
      "Unable to verify transaction execution state within 60 seconds. Please check manually. txHash:",
      txHash,
    );
  }

  return { success: false, result: "" };
}
```
