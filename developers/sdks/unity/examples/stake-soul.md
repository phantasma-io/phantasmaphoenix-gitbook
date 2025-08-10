# Stake SOUL

This example demonstrates how to stake SOUL tokens

```csharp
public void StakeSoul()
{
    // Initialize PhantasmaAPI instance
    var api = new PhantasmaAPI("https://testnet.phantasma.info/rpc");

    // Load private key
    var keys = PhantasmaKeys.FromWIF("PK_in_WIF_format");

    // Address derived from the loaded private key - used as transaction sender
    var senderAddress = keys.Address;

    // Target chain Nexus name (e.g. "testnet" or "mainnet")
    var nexus = "testnet";

    // Amount to stake
    var amount = 0.01m;

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

        // Call the 'Stake' method in the 'stake' contract with sender address and converted to big integer token amount
        sb.CallContract("stake", "Stake", senderAddress, UnitConversion.ToBigInteger(amount, DomainSettings.StakingTokenDecimals));

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
    StartCoroutine(api.SignAndSendTransaction(keys, nexus, script, "main", "example7-tx-payload",
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
