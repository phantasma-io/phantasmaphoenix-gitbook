# Examples

The following examples demonstrate how to use the ScriptBuilder class to create various transaction scripts for the Phantasma blockchain.

#### Example 1: Transfer Tokens

```csharp
ScriptBuilder sb = new ScriptBuilder();
sb.AllowGas(fromAddress, toAddress, gasPrice, gasLimit);
sb.TransferTokens("KCAL", fromAddress, toAddress, transferAmount);
sb.SpendGas(fromAddress);
byte[] script = sb.EndScript();
```

#### Example 2: Transfer NFT

```csharp
ScriptBuilder sb = new ScriptBuilder();
sb.AllowGas(fromAddress, toAddress, gasPrice, gasLimit);
sb.TransferNFT("NFT", fromAddress, toAddress, tokenId);
sb.SpendGas(fromAddress);
byte[] script = sb.EndScript();
```

#### Example 3: Call Smart Contract

```csharp
ScriptBuilder sb = new ScriptBuilder();
sb.AllowGas(fromAddress, toAddress, gasPrice, gasLimit);
sb.CallContract("MyContract", "MyMethod", arg1, arg2, arg3);
sb.SpendGas(fromAddress);
byte[] script = sb.EndScript();
```

#### Example 4: Call NFT Contract

```csharp
ScriptBuilder sb = new ScriptBuilder();
sb.AllowGas(fromAddress, toAddress, gasPrice, gasLimit);
sb.CallNFT("NFT", seriesID, "MyMethod", arg1, arg2, arg3);
sb.SpendGas(fromAddress);
byte[] script = sb.EndScript();
```

These examples show how to create transaction scripts using the ScriptBuilder class and its methods. Each script begins with the AllowGas method to allocate gas for the transaction, followed by the specific operation to be executed, and ends with the SpendGas method to pay for the gas used during the execution. Finally, the EndScript`()` method is called to generate the byte array representation of the transaction script.
