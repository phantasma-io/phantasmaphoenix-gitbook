# 📝 Phantasma ScriptBuilder Class Documentation

The Phantasma ScriptBuilder class is a utility for creating transaction scripts in the Phantasma blockchain. This class provides methods for various operations such as transferring tokens, interacting with smart contracts, and managing gas for transactions.

### Methods

#### AllowGas

`public static ScriptBuilder AllowGas(this ScriptBuilder sb, Address from, Address to, BigInteger gasPrice, BigInteger gasLimit)`

This method is used to allocate gas for a transaction script in the Phantasma blockchain. It is required to be called at the beginning of every transaction script. The gas allocated will be used to pay for the gas fees associated with executing the script.

**Parameters**

* `sb`: An instance of the ScriptBuilder class.
* `from`: The source address for allocating gas. The gas fees will be deducted from this address.
* `to`: The destination address to which the gas fees will be sent. This can be the address of a dapp contract to donate a portion of the fees, or it can be null.
* `gasPrice`: The base cost in KCAL (Phantasma's native token) of every script operation. The gas price must be equal to or larger than what the nodes currently accept.
* `gasLimit`: The maximum amount of gas that can be spent. This helps to prevent malicious contracts from spending all of the account's KCAL.

#### SpendGas

`public static ScriptBuilder SpendGas(this ScriptBuilder sb, Address address)`

This method is used to pay for the actual gas consumed during the execution of a transaction script. It should be called as the last operation in a script, after allocating gas using the AllowGas method. Any leftover KCAL after spending gas will be returned to the specified address, which must match the address previously passed in the AllowGas method.

**Parameters**

* `sb`: An instance of the ScriptBuilder class.
* `address`: The address to which any leftover KCAL should be returned. This must match the address previously passed in the AllowGas method.

#### TransferTokens

`public static ScriptBuilder TransferTokens(this ScriptBuilder sb, string tokenSymbol, Address from, Address to, BigInteger amount)`

This method is used to transfer a specific amount of fungible tokens from one address to another in the Phantasma blockchain.

**Parameters**

* `sb`: An instance of the ScriptBuilder class.
* `tokenSymbol`: The symbol of the fungible token to transfer.
* `from`: The source address from which the tokens will be transferred.
* `to`: The destination address to which the tokens will be transferred.
* `amount`: The amount of tokens to transfer.

#### TransferBalance

`public static ScriptBuilder TransferBalance(this ScriptBuilder sb, string tokenSymbol, Address from, Address to)`

This method is used to transfer the full available balance of a specific fungible token from one address to another in the Phantasma blockchain.

**Parameters**

* `sb`: An instance of the ScriptBuilder class.
* `tokenSymbol`: The symbol of the fungible token to transfer.
* `from`: The source address from which the tokens will be transferred.
* `to`: The destination address to which the tokens will be transferred.

#### TransferNFT

`public static ScriptBuilder TransferNFT(this ScriptBuilder sb, string tokenSymbol, Address from, Address to, BigInteger tokenId)`

The TransferNFT method of the ScriptBuilder class is used to transfer a single Non-Fungible Token (NFT) from one address to another. The NFT is specified by its tokenID argument, which uniquely identifies the NFT within the given tokenSymbol and from address.

**Parameters**

* `sb`: The ScriptBuilder instance.
*   `tokenSymbol`: A string representing the&#x20;

    symbol of the NFT to be transferred.
* `from`: An Address object representing the source address from which the NFT will be transferred.
* `to`: An Address object representing the destination address to which the NFT will be transferred.
* `tokenId`: A BigInteger representing the unique identifier of the NFT to be transferred.

**Example**

```csharp
ScriptBuilder sb = new ScriptBuilder();
sb.TransferNFT("NFT", fromAddress, toAddress, tokenId);
byte[] script = sb.EndScript();
```

#### CallContract

`public static ScriptBuilder CallContract(this ScriptBuilder sb, string contractName, string method, params object[] args)`

The CallContract method of the ScriptBuilder class is used to call a specific method from a smart contract with custom arguments. The contract is specified by its contractName, and the method to be called is specified by its method argument. Custom arguments can be passed as an array of objects using the args parameter.

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

The CallNFT method of the ScriptBuilder class is used to call a specific method from a smart Non-Fungible Token (NFT) contract, identified by its symbol and seriesID, with custom arguments. The method to be called is specified by its method argument, and custom arguments can be passed as an array of objects using the args parameter.

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
