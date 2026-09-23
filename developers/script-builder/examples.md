# Examples

The following examples use the C# SDK `ScriptBuilder` to create transaction scripts.

#### Example 1: Transfer Tokens

```csharp
ScriptBuilder sb = new ScriptBuilder();
sb.AllowGas(fromAddress, Address.Null, gasPrice, gasLimit);
sb.TransferTokens("KCAL", fromAddress, toAddress, transferAmount);
sb.SpendGas(fromAddress);
byte[] script = sb.EndScript();
```

#### Example 2: Transfer NFT

```csharp
ScriptBuilder sb = new ScriptBuilder();
sb.AllowGas(fromAddress, Address.Null, gasPrice, gasLimit);
sb.TransferNFT("NFT", fromAddress, toAddress, tokenId);
sb.SpendGas(fromAddress);
byte[] script = sb.EndScript();
```

#### Example 3: Call Smart Contract

```csharp
ScriptBuilder sb = new ScriptBuilder();
sb.AllowGas(fromAddress, Address.Null, gasPrice, gasLimit);
sb.CallContract("MyContract", "MyMethod", arg1, arg2, arg3);
sb.SpendGas(fromAddress);
byte[] script = sb.EndScript();
```

#### Example 4: Call NFT Contract

```csharp
ScriptBuilder sb = new ScriptBuilder();
sb.AllowGas(fromAddress, Address.Null, gasPrice, gasLimit);
sb.CallNFT("NFT", seriesID, "MyMethod", arg1, arg2, arg3);
sb.SpendGas(fromAddress);
byte[] script = sb.EndScript();
```

Each script begins with `AllowGas`, which sets the gas payer and the transaction's `maxGas` (`gasPrice * gasLimit`, in KCAL atoms). The operation follows. The closing `SpendGas` call is optional on the current chain. `EndScript()` returns the script bytes.
