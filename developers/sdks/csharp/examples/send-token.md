# Send Token

This example demonstrates how to transfer fungible tokens

```csharp
public void SendToken()
{
	// Initialize PhantasmaAPI instance
	var api = new PhantasmaAPI("https://testnet.phantasma.info/rpc");

	// Load private key
	var keys = PhantasmaKeys.FromWIF("PK_in_WIF_format");

	// Address derived from the loaded private key - used as transaction sender
	var senderAddress = keys.Address;

	// Target chain Nexus name (e.g. "testnet" or "mainnet")
	var nexus = "testnet";

	// Recipient address for the token transfer
	var destinationAddress = "P2K...";

	// Token symbol to transfer (e.g. SOUL, KCAL)
	var symbol = "KCAL";

	// Amount to send
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

		// Add instruction to transfer tokens from sender to destination, converting human-readable amount to chain format
		sb.TransferTokens(symbol, senderAddress, Address.Parse(destination),
			UnitConversion.ToBigInteger(amount, token.Decimals));

		// Spend gas necessary for transaction execution
		sb.SpendGas(senderAddress);

		// Finalize and get raw bytecode for the transaction script
		script = sb.EndScript();
	}
	catch (Exception e)
	{
		throw new Exception($"Could not build transaction script: {e.Message}");
	}

	// Signing transaction with private key and sending it to the chain
	var txHash = await api.SignAndSendTransactionAsync(keys, nexus, script, chain, "example5-tx-payload");
	if (!string.IsNullOrEmpty(txHash))
	{
		Console.WriteLine($"Transaction was sent, hash: {txHash}");

		// Start polling to track transaction execution status on-chain
		await Example06_CheckTransactionState.Run(api, txHash,
			state => Console.WriteLine($"Tx completed with state: {state?.ToString() ?? "Unknown"}"));
	}
	else
	{
		throw new Exception("Failed to send transaction");
	}
}
```
