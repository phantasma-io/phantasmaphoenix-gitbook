# Libraries

A library is imported at the top of a contract, token, script or description
body with `import Name;`. The tables list the libraries and methods that
compile with `pha-tomb` and run on the current chain. A compiler library whose
calls the validator rejects is not listed; `nativecheck:error` reports such
calls at compile time.

## Account

| Method | Return type | Description |
| --- | --- | --- |
| Account.getName(from:Address) | String | Returns the name registered for the address, or an empty string. |

The other methods of the compiler's Account library (name registration,
account scripts, migration) call the `account` native contract, which the
current chain does not serve.

## Address

| Method | Return type | Description |
| --- | --- | --- |
| Address.isNull(target:Address) | Bool | Returns true if the address is the null address. |
| Address.isUser(target:Address) | Bool | Returns true if the address is a user address. |
| Address.isSystem(target:Address) | Bool | Returns true if the address is a system address. |
| Address.isInterop(target:Address) | Bool | Returns true if the address is an interop address. |

## Array

Arrays can also be used directly through TOMB array variables.

| Method | Return type | Description |
| --- | --- | --- |
| Array.get(array:Any, index:Number) | Generic<0> | Returns the element at the index. |
| Array.set(array:Any, index:Number, value:Generic<0>) | None | Sets the element at the index. |
| Array.remove(array:Any, index:Number) | None | Removes the element at the index. |
| Array.clear(array:Any) | None | Removes every element. |
| Array.length(array:Any) | Number | Returns the number of elements. |
| Array.push(array:Any, value:Generic<0>) | None | Appends an element. |
| Array.pop(array:Any) | Generic<0> | Removes and returns the last element. |

## Call

| Method | Return type | Description |
| --- | --- | --- |
| Call.interop<T>(name:String, ...:Generic) | T | Calls a VM interop by name, for example `Call.interop<number>("Map.Get", "OTHER", "_field", key, $TYPE_OF(number))`. The interop reference lists the names the validator implements. |
| Call.contract<T>(contract:String, method:String, ...:Generic) | T | Calls a method of a deployed contract, or of the `gas` and `stake` native contracts. |
| Call.method<T>(method:Method, ...:Generic) | T | Calls a method of the current contract by name. |

The type parameter names the return type; use `none` for a method that
returns nothing.

{% content-ref url="../blockchain/chain/information/virtual-machine/interop.md" %}
Interop
{% endcontent-ref %}

## Decimal

| Method | Return type | Description |
| --- | --- | --- |
| Decimal.decimals(target:Any) | Number | Returns the number of decimal places of a `decimal<N>` value. |
| Decimal.convert(decimalPlaces:Number, value:Number) | Number | Converts a value to the given number of decimal places. |

## Enum

| Method | Return type | Description |
| --- | --- | --- |
| Enum.isSet(target:Enum<>, flag:Enum<>) | Bool | Returns true if the flag is set in the value. |

## Format

Available inside `description` modules only, which render event text for
wallets and explorers.

| Method | Return type | Description |
| --- | --- | --- |
| Format.decimals(value:Number, symbol:String) | String | Renders an amount with the decimals of the token. |
| Format.symbol(symbol:String) | String | Renders a token symbol. |
| Format.account(address:Address) | String | Renders an address, with its name when one is registered. |

## List

Lists are declared as `storage_list<T>` globals; the methods are called on the
variable.

| Method | Return type | Description |
| --- | --- | --- |
| List.get(index:Number) | Generic | Returns the element at the index. |
| List.add(value:Generic) | None | Appends an element. |
| List.replace(index:Number, value:Generic) | None | Replaces the element at the index. |
| List.removeAt(index:Number) | None | Removes the element at the index. The last element takes its place. |
| List.count() | Number | Returns the number of elements. |
| List.clear() | None | Removes every element. |

## Map

Maps are declared as `storage_map<K, V>` globals; the methods are called on the
variable.

| Method | Return type | Description |
| --- | --- | --- |
| Map.get(key:Generic) | Generic | Returns the value stored under the key, or the default of the value type. |
| Map.set(key:Generic, value:Generic) | None | Stores a value under the key. |
| Map.remove(key:Generic) | None | Removes the key. |
| Map.clear() | None | Removes every entry. |
| Map.count() | Number | Returns the number of entries. |
| Map.has(key:Generic) | Bool | Returns true if the key exists. |

## Math

| Method | Return type | Description |
| --- | --- | --- |
| Math.min(a:Number, b:Number) | Number | Returns the smaller number. |
| Math.max(a:Number, b:Number) | Number | Returns the larger number. |
| Math.abs(a:Number) | Number | Returns the absolute value. |
| Math.pow(a:Number, b:Number) | Number | Returns `a` raised to the power `b`. |
| Math.sqrt(x:Number) | Number | Returns the integer square root. |

## Module

| Method | Return type | Description |
| --- | --- | --- |
| Module.getScript(target:Module) | Bytes | Returns the compiled script of a module declared in the same file. |
| Module.getABI(target:Module) | Bytes | Returns the serialized ABI of a module declared in the same file. |

## NFT

| Method | Return type | Description |
| --- | --- | --- |
| NFT.transfer(from:Address, to:Address, symbol:String, id:Number) | None | Transfers one NFT by its Phantasma NFT id. |
| NFT.mint(from:Address, to:Address, symbol:String, rom:Any, ram:Any, seriesID:Number) | None | Mints an NFT with the given ROM and RAM into a series. |
| NFT.write(from:Address, symbol:String, tokenID:Number, ram:Any) | None | Replaces the RAM of an NFT (`Runtime.WriteToken`). Runs `onWrite` when the token contract defines it; without `onWrite`, the token owner must sign or the token's own contract must call. |
| NFT.burn(from:Address, symbol:String, id:Number) | None | Burns an NFT. |
| NFT.infuse(from:Address, symbol:String, id:Number, infuseSymbol:String, infuseValue:Number) | None | Moves a fungible amount or one NFT into the NFT. |
| NFT.getInfusions(symbol:String, id:Number) | Any | Returns what the NFT holds. |
| NFT.getOwnerships(address:Address, symbol:String) | Any | Returns the NFT ids of the token the address owns. |
| NFT.getOwnershipsBySeries(address:Address, symbol:String, seriesID:Number) | Any | The same, limited to one series. |
| NFT.read(symbol:String, id:Number) | Any | Returns the NFT fields (`Runtime.ReadToken`). |
| NFT.readROM(symbol:String, id:Number) | T | Returns the ROM of an NFT as the struct type `T`. |
| NFT.readRAM(symbol:String, id:Number) | T | Returns the RAM of an NFT as the struct type `T`. |
| NFT.createSeries(from:Address, symbol:String, seriesID:Number, maxSupply:Number, mode:Enum, nft:Module) | None | Creates a series of the token from an `nft` submodule. |

## Runtime

| Method | Return type | Description |
| --- | --- | --- |
| Runtime.expect(condition:Bool, error:String) | None | Aborts execution with the error text when the condition is false. |
| Runtime.log(message:String) | None | Writes a log line. |
| Runtime.isWitness(address:Address) | Bool | Returns true if the address signed the transaction. |
| Runtime.isTrigger() | Bool | Returns true inside a trigger. |
| Runtime.context() | String | Returns the name of the executing context. |
| Runtime.previousContext() | String | Returns the name of the calling context. |
| Runtime.gasTarget() | Address | Returns the gas target address of the transaction. |
| Runtime.version() | Number | Returns the VM behavior version. |
| Runtime.deployContract(from:Address, contract:Module) | None | Deploys a standalone contract from a module declared in the same file. |
| Runtime.upgradeContract(from:Address, contract:Module) | None | Upgrades a deployed contract. |

## Stake

| Method | Return type | Description |
| --- | --- | --- |
| Stake.stake(from:Address, stakeAmount:Number) | None | Stakes SOUL for the address. |
| Stake.unstake(from:Address, unstakeAmount:Number) | None | Unstakes SOUL. |
| Stake.claim(from:Address, stakeAddress:Address) | None | Claims the KCAL generated by a stake. |
| Stake.getUnclaimed(from:Address) | Number | Returns the KCAL the address can claim. |

{% hint style="warning" %}
`Stake.stake($THIS_ADDRESS, amount)` does not increase contract storage. Storage growth is paid by the transaction through SOUL data escrow and `maxData`. See [Storage And Data Escrow](../blockchain/smart-contracts/storage-and-data-escrow.md#contract-storage-is-not-increased-by-self-staking-soul).
{% endhint %}

The master, voting-power and conversion methods of the compiler's Stake
library are not served by the current `stake` contract.

## Storage

| Method | Return type | Description |
| --- | --- | --- |
| Storage.read(contract:String, field:String) | Generic | Reads a field of a contract (`Data.Get`). |
| Storage.write(field:String, value:Any) | None | Writes a field of the current contract (`Data.Set`). |
| Storage.delete(field:String) | None | Deletes a field of the current contract (`Data.Delete`). |

Writes go to the current contract only. Storage growth is charged through the
transaction's SOUL data escrow; see
[Storage And Data Escrow](../blockchain/smart-contracts/storage-and-data-escrow.md).
The file storage methods of the compiler's Storage library call the `storage`
native contract, which the current chain does not serve.

## String

| Method | Return type | Description |
| --- | --- | --- |
| String.length(target:String) | Number | Returns the number of characters. |
| String.substr(target:String, index:Number, length:Number) | String | Returns a substring. |
| String.toArray(target:String) | Array | Returns the characters as an array of numbers. |
| String.fromArray(target:Array) | String | Builds a string from an array of character codes. |
| String.toUpper(target:String) | String | Returns the upper-case form. |
| String.toLower(target:String) | String | Returns the lower-case form. |

## Time

| Method | Return type | Description |
| --- | --- | --- |
| Time.now() | Timestamp | Returns the block time. |
| Time.unix(value:Number) | Timestamp | Builds a timestamp from a Unix time in seconds. |

## Token

| Method | Return type | Description |
| --- | --- | --- |
| Token.create(from:Address, script:Bytes, abi:Bytes) | None | Creates a token-backed contract; the symbol, name, flags, supply and decimals come from the token module's properties. |
| Token.exists(symbol:String) | Bool | Returns true if the token exists. |
| Token.getDecimals(symbol:String) | Number | Returns the decimals of the token; zero for an NFT. |
| Token.getFlags(symbol:String) | Enum | Returns the `TokenFlags` of the token. |
| Token.getOwner(symbol:String) | Address | Returns the owner address of the token. |
| Token.transfer(from:Address, to:Address, symbol:String, amount:Number) | None | Transfers an amount of a fungible token. |
| Token.transferAll(from:Address, to:Address, symbol:String) | None | Transfers the whole balance of a fungible token. |
| Token.mint(from:Address, to:Address, symbol:String, amount:Number) | None | Mints an amount of a fungible token. |
| Token.write(from:Address, symbol:String, tokenID:Number, ram:Any) | None | Replaces the RAM of an NFT (`Runtime.WriteToken`). |
| Token.burn(from:Address, symbol:String, amount:Number) | None | Burns an amount of a fungible token. |
| Token.getBalance(from:Address, symbol:String) | Number | Returns the balance of the address. |

## UID

| Method | Return type | Description |
| --- | --- | --- |
| UID.generate() | Number | Returns an identifier that is unique within the transaction. |
