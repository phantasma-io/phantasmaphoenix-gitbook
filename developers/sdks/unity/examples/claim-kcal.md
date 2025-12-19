# Claim KCAL

This example demonstrates how to claim all KCAL tokens earned from SOUL staking

```csharp
public void ClaimKcal()
{
    // Initialize PhantasmaAPI instance
    var api = new PhantasmaAPI("https://testnet.phantasma.info/rpc");

    // Load private key
    var keys = PhantasmaKeys.FromWIF("PK_in_WIF_format");

    // Address derived from the loaded private key - used as transaction sender
    var senderAddress = keys.Address;

    // Target chain Nexus name (e.g. "testnet" or "mainnet")
    var nexus = "testnet";

    // Not used right now, use as is
    var feePrice = 100000; // TODO: Adapt to new fee model.
    var feeLimit = 21000; // TODO: Adapt to new fee model.

    byte[] script;

    try
    {
        // ScriptBuilder is used to create a serialized transaction script
        var sb = new ScriptBuilder();

        // Instruction to allow gas fees for the transaction - required by all transaction scripts
        sb.AllowGas(senderAddress, Address.Null, feePrice, feeLimit);

        // Call the 'Claim' method in the 'stake' contract with sender address
        sb.CallContract("stake", "Claim", senderAddress, senderAddress);

        // Spend gas necessary for transaction execution
        sb.SpendGas(senderAddress);

        // Finalize and get raw bytecode for the transaction script
        script = sb.EndScript();
    }
    catch (Exception e)
    {
        Debug.LogError($"[Error] Could not built transaction script {e}");
        return;
    }

    // Sign and send the transaction using the generated script and optional payload comment
    StartCoroutine(api.SignAndSendTransaction(keys, nexus, script, "main", "example9-tx-payload",
        // Callback on success
        (txHash, encodedTx) =>
        {
            if (!string.IsNullOrEmpty(txHash))
            {
                Debug.Log($"Transaction was sent, hash: {txHash}. Check transaction status using GetTransaction() call");

                // Start polling to track transaction execution status on-chain
                // CheckTxStateLoop() implementation is available in "Check Transaction State" example
                StartCoroutine(CheckTxStateLoop(api, txHash, null));
                return;
            }
            else
            {
                Debug.LogError("[Error] Empty transaction hash returned, but no explicit error");
            }
        },
        // Callback for RPC errors (invalid token, network error, etc.)
        (errorCode, errorMessage) =>
        {
            Debug.LogError($"[Error][{errorCode}] Failed to send transaction: {errorMessage}");
        }));
}
```
