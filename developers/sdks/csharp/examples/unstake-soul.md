# Unstake SOUL

This example demonstrates how to unstake SOUL tokens

```csharp
using PhantasmaPhoenix.Core;
using PhantasmaPhoenix.Cryptography;
using PhantasmaPhoenix.Protocol;
using PhantasmaPhoenix.RPC;
using PhantasmaPhoenix.VM;

public void UnstakeSoul()
{
	// Initialize PhantasmaAPI instance
	var api = new PhantasmaAPI("https://testnet.phantasma.info/rpc", null);

	// Load private key
	var keys = PhantasmaKeys.FromWIF("PK_in_WIF_format");

	// Address derived from the loaded private key - used as transaction sender
	var senderAddress = keys.Address;

	// Target chain Nexus name (e.g. "testnet" or "mainnet")
	var nexus = "testnet";

	// Amount to unstake
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

		// Add instruction to unstake tokens, converting human-readable amount to chain format
		sb.CallContract("stake", "Unstake", senderAddress,
			UnitConversion.ToBigInteger(amount, DomainSettings.StakingTokenDecimals));

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
	var hashText = await api.SignAndSendTransactionAsync(keys, nexus, script, "main", "example8-tx-payload");
	if (!string.IsNullOrEmpty(hashText))
	{
		Console.WriteLine($"Transaction was sent, hash: {hashText}");

		// Start polling to track transaction execution status on-chain
		await Example06_CheckTransactionState.Run(api, hashText,
			state => Console.WriteLine($"Tx completed with state: {state?.ToString() ?? "Unknown"}"));
	}
	else
	{
		throw new Exception("Empty transaction hash returned");
	}
}
```
