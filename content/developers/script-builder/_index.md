---
title: "📝 ScriptBuilder (C# SDK)"
linkTitle: "Script Builder"
weight: 80
---

`ScriptBuilder` is the C# SDK helper for assembling Phantasma transaction scripts: it allocates gas, transfers fungible tokens and NFTs, mints tokens and calls contracts. The methods below are C# extension methods from `PhantasmaPhoenix.VM` (`ScriptBuilderExtensions.cs` and `ScriptUtils.cs`); each one emits the VM `EXTCALL` interops the node runs. Every method that takes a `to: Address` also has an overload that takes the destination as an address string. The `CrossTransferToken` and `CrossTransferNFT` extensions emit `Runtime.SendTokens`, which the node does not implement, so they are not documented here.

> [!NOTE]
> For the underlying VM interop surface (and the script builders in the other SDKs), see [External Calls](external-calls.md).

### Methods

#### AllowGas

`public static ScriptBuilder AllowGas(this ScriptBuilder sb, Address from, Address to, BigInteger gasPrice, BigInteger gasLimit)`

Declares who pays for the transaction and the most KCAL it may spend. A VM transaction sent with `sendRawTransaction` must call `AllowGas`: the chain reads the gas payer and `maxGas` from this call, and it rejects the transaction without it with `No call to AllowGas`.

The chain uses only the product `gasPrice * gasLimit`. That product is the transaction's `maxGas`, in KCAL atoms (1 KCAL is 10^10 atoms). The validator computes the actual gas bill after execution and refunds the unused part to the gas payer. A `maxGas` below the chain's `minimumGasOffer` or `minimumGasBill` is rejected; read both values with `getGasConfig`.

A VM transaction sent with `sendRawTransaction` carries no SOUL data escrow limit. The chain bills the data escrow for the actual state growth after execution, and the gas payer must hold that SOUL.

**Parameters**

* `sb`: An instance of the ScriptBuilder class.
* `from`: The gas payer. It must sign the transaction. In a Carbon-wrapped VM transaction, `from` must equal the transaction's gas payer and `gasPrice * gasLimit` must equal its `maxGas`; otherwise the call fails with `gas mismatch`.
* `to`: The dApp fee target. When it is a user address, it receives the dApp share of the gas bill, which the chain gas config sets with `gasDappRatioMul` and `gasDappRatioShift` after the burn and producer shares. Pass `Address.Null` when there is no dApp target; no dApp share is paid then.
* `gasPrice`: Multiplied by `gasLimit` to give `maxGas`.
* `gasLimit`: Multiplied by `gasPrice` to give `maxGas`.

#### SpendGas

`public static ScriptBuilder SpendGas(this ScriptBuilder sb, Address address)`

Adds a `SpendGas` call. The current chain accepts the call and ignores it. It settles the gas bill and refunds unused KCAL to the gas payer after the script finishes, with or without `SpendGas`.

**Parameters**

* `sb`: An instance of the ScriptBuilder class.
* `address`: Not used by the current chain.

#### TransferTokens

`public static ScriptBuilder TransferTokens(this ScriptBuilder sb, string tokenSymbol, Address from, Address to, BigInteger amount)`

Transfers an amount of a fungible token between two addresses (`Runtime.TransferTokens`).

**Parameters**

* `sb`: An instance of the ScriptBuilder class.
* `tokenSymbol`: The symbol of the fungible token to transfer.
* `from`: The source address from which the tokens will be transferred.
* `to`: The destination address to which the tokens will be transferred.
* `amount`: The amount of tokens to transfer.

#### TransferBalance

`public static ScriptBuilder TransferBalance(this ScriptBuilder sb, string tokenSymbol, Address from, Address to)`

Transfers the whole balance of a fungible token between two addresses (`Runtime.TransferBalance`).

**Parameters**

* `sb`: An instance of the ScriptBuilder class.
* `tokenSymbol`: The symbol of the fungible token to transfer.
* `from`: The source address from which the tokens will be transferred.
* `to`: The destination address to which the tokens will be transferred.

#### TransferNFT

`public static ScriptBuilder TransferNFT(this ScriptBuilder sb, string tokenSymbol, Address from, Address to, BigInteger tokenId)`

Transfers one NFT, identified by its Phantasma NFT id, between two addresses (`Runtime.TransferToken`).

**Parameters**

* `sb`: The ScriptBuilder instance.
* `tokenSymbol`: The symbol of the NFT token.
* `from`: The source address.
* `to`: The destination address.
* `tokenId`: The Phantasma NFT id.

**Example**

```csharp
ScriptBuilder sb = new ScriptBuilder();
sb.TransferNFT("NFT", fromAddress, toAddress, tokenId);
byte[] script = sb.EndScript();
```

#### MintTokens

`public static ScriptBuilder MintTokens(this ScriptBuilder sb, string tokenSymbol, Address from, Address target, BigInteger amount)`

Mints an amount of a fungible token to `target` (`Runtime.MintTokens`). `from` must be allowed to mint the token.

#### CallContract

`public static ScriptBuilder CallContract(this ScriptBuilder sb, string contractName, string method, params object[] args)`

`public static ScriptBuilder CallContract(this ScriptBuilder sb, NativeContractKind contractKind, string method, params object[] args)`

Calls a method of a deployed contract, or of a native contract named by `NativeContractKind`, with the given arguments. The arguments are pushed in reverse order, then the method name, then the contract context is entered with `CTX` and `SWITCH`.

**Parameters**

* `sb`: The ScriptBuilder instance.
* `contractName`: A string representing the name of the smart contract to be called.
* `method`: A string representing the name of the method to be called.
* `args`: An array of objects representing the custom arguments to be passed to the method.

**Example**

```csharp
ScriptBuilder sb = new ScriptBuilder();
sb.CallContract("MyContract", "MyMethod", arg1, arg2, arg3);
byte[] script = sb.EndScript();
```

#### CallNFT

`public static ScriptBuilder CallNFT(this ScriptBuilder sb, string symbol, BigInteger seriesID, string method, params object[] args)`

Calls a method of an NFT series contract. The context name is `SYMBOL#seriesID`, which the node resolves to the series created from the token's `nft` submodule.

**Parameters**

* `sb`: The ScriptBuilder instance.
* `symbol`: A string representing the symbol of the NFT contract to be called.
* `seriesID`: A BigInteger representing the series identifier of the NFT contract to be called.
* `method`: A string representing the name of the method to be called.
* `args`: An array of objects representing the custom arguments to be passed to the method.

**Example**

```csharp
ScriptBuilder sb = new ScriptBuilder();
sb.CallNFT("NFT", seriesID, "MyMethod", arg1, arg2, arg3);
byte[] script = sb.EndScript();
```
