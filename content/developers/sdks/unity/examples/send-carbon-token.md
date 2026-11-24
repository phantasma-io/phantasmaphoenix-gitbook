---
title: "Send a Carbon Token"
weight: 60
---

This example transfers a fungible token through the Carbon path. The message is
a native transfer, and one call plans the fee, signs and broadcasts it.

A Carbon message names the token by its Carbon id, so the symbol is resolved
first. The same call gives the decimals the amount is converted with.

```csharp
using UnityEngine;
using System;
using System.Globalization;
using PhantasmaPhoenix.Core;
using PhantasmaPhoenix.Cryptography;
using PhantasmaPhoenix.Protocol.Carbon;
using PhantasmaPhoenix.Protocol.Carbon.Blockchain;
using PhantasmaPhoenix.Protocol.Carbon.Blockchain.TxHelpers;

public class SendCarbonToken : MonoBehaviour
{
	public void Run()
	{
		var api = new PhantasmaAPI("https://testnet.phantasma.info/rpc");
		var keys = PhantasmaKeys.FromWIF("YOUR_WIF");

		var symbol = "SOUL";
		var recipient = "P2K...";
		var amount = 1.5m;

		StartCoroutine(api.GetToken(symbol, (tokenResult) =>
			{
				TxMsg message;
				try
				{
					message = NativeTxHelper.TransferFungible(new TransferFungibleParams
					{
						From = new Bytes32(keys.PublicKey),
						To = new Bytes32(Address.Parse(recipient).GetPublicKey()),
						TokenId = ulong.Parse(tokenResult.CarbonId, CultureInfo.InvariantCulture),
						Amount = (ulong)UnitConversion.ToBigInteger(amount, tokenResult.Decimals)
					});
				}
				catch (Exception e)
				{
					Debug.LogError($"[Error] Could not build the transaction message {e}");
					return;
				}

				// No gas offer is set on the message, so the SDK reads the chain's gas
				// configuration and prices the transfer before signing it.
				StartCoroutine(api.SignAndSendCarbonTransaction(keys, message,
					(txHash, encodedTx) =>
					{
						if (!string.IsNullOrEmpty(txHash))
						{
							Debug.Log($"Transaction was sent, hash: {txHash}");
							return;
						}

						Debug.LogError("[Error] Failed to send transaction");
					},
					(errorCode, errorMessage) =>
					{
						Debug.LogError($"[Error][{errorCode}] Failed to send transaction: {errorMessage}");
					}));
			},
			(errorCode, errorMessage) =>
			{
				Debug.LogError($"[Error][{errorCode}] {errorMessage}");
			}
		));
	}
}
```

Poll the transaction state before acting on the result. See
[Check Transaction State](check-transaction-state.md).

To show the fee before the player confirms, plan it first. See
[Carbon Transactions And Fees](../carbon-transactions.md).
