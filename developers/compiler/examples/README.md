# 🖥️ Examples

## Array example

Here is a simple example of how to declare and initialize an array.

```csharp
contract test {
	import Array;

	public getStrings(): array<string> {
        	local result : array<string> = {"A", "B", "C"};
        	return result;
    	}
}
```

## Call contract from another contract

Example showcasing calling contract storage directly from another contract.
Basic version where another storage map is called, and this value is incremented and stored in another contract storage.

{% code lineNumbers="true" %}
```csharp
contract test {

	import Map;
	import Storage;
	import Call;

	global counters: storage_map<number, number>;

	private getContractCount(tokenId:number):number {

		local count:number := Call.interop<number>("Map.Get",  "OTHERCONTRACT", "_storageMap", tokenId, $TYPE_OF(number));
		return count;

	}

	public updateCount(tokenID:number) {

		local contractCounter:number := this.getContractCount(tokenID);
		contractCounter += 1;
		counters.set(tokenID, contractCounter);

	}

	public getCount(tokenID:number):number {

		local temp:number := counters.get(tokenID);
		return temp;

	}
}
```
{% endcode %}

## Conditions

Like most programming languages, it is possible to do conditional branching use if statement.
Logic operators supported include and, or and xor.


{% code lineNumbers="true" %}
```csharp
contract test {
	public isEvenAndPositive(n:number):bool
	{
		if (n>0 and n%2==0)
		{
			return true;
		}
		else
		{
			return false;
		}
	}
}
```
{% endcode %}

## Counter per Address

Another contract that implements a counter, this time unique per user address.
Showcases how to validate that a transaction was done by user possessing private keys to 'from' address

{% code lineNumbers="true" %}
```csharp
contract test {
	import Runtime;
	import Map;

	global counters: storage_map<address, number>;

	public increment(from:address)
	{
		Runtime.expect(Runtime.isWitness(from), "witness failed");
		local temp: number;
		temp := counters.get(from);
		temp += 1;
		counters.set(from, temp);
	}
}
```
{% endcode %}

## Custom Events

### Example 1

Showcases how a contract can declare and emit custom events.

{% code lineNumbers="true" %}
```csharp
contract test {
	event MyPayment:number = "{address} paid {data}"; // here we use a short-form description

	public paySomething(from:address, x:number)
	{
		Runtime.expect(Runtime.isWitness(from), "witness failed");

		local price: number := 10;
		local thisAddr:address := $THIS_ADDRESS;
		Token.transfer(from, thisAddr, "SOUL", price);

		emit MyPayment(from, price);
	}
}
```
{% endcode %}

### Example 2

A more complex version of the previous example, showcasing custom description scripts.

{% code lineNumbers="true" %}
```csharp
description payment_event {

	code(from:address, amount:number): string {
		local result:string := "";
		result += from;
		result += " paid ";
		result += amount;
		return result;
	}
}

contract test {
	event MyPayment:number = payment_event; // here we use a short-form declaration

	// everything else would be same as previous example
}
```
{% endcode %}

### Example 3

A yet more complex version of the previous examples, showcasing custom description scripts and also struct declarations.

{% code lineNumbers="true" %}
```csharp
struct my_event_data {
	amount:number;
	symbol:string;
}

description payment_event {

	code(from:address, data:my_event_data): string {
		local result:string := "";
		result += from;
		result += " paid ";
		result += data.amount;
		result += " ";
		result += data.symbol;
		return result;
	}
}

contract test {
	event MyPayment:my_event_data = payment_event; // here we use a short-form declaration

	// everything else would be same as previous examples
}
```
{% endcode %}

## Decimals

There is compiler support for decimal numbers.
Note that internally those are converted to Number types in fixed point format.

{% code lineNumbers="true" %}
```csharp
contract test {
	global val: decimal<4>; // the number between <> is the number of decimal places

	constructor(owner:address)
	{
		val := 2.1425;
	}

	public getValue():number
	{
		return val; // this will return 21425, which is the previous value in fixed point format
	}

	public getDecimals():number
	{
		return val.decimals(); // this returns 4 as result
	}

	public sum(other:decimal<4>):number
	{
		return val + other;
	}

}

```
{% endcode %}

## Enums

There is compiler support for enumerated value types, that map directly to the Phantasma VM enum type.


{% code lineNumbers="true" %}
```csharp
// NOTE - like other custom types, it is declared outside the scope of a contract
enum MyEnum { A = 0, B = 1, C = 2}
// if the numbers are sequential, it is ok to ommit them, eg:
//enum MyEnum { A, B, C}

contract test {
	global state: MyEnum;

	constructor(owner:address)
	{
		state := MyEnum.B;
	}

	public getValue():MyEnum
	{
		return state;
	}
}

```
{% endcode %}

## Inline asm

Inline asm allows to write assembly code that is then inserted and merged into the rest of the code.
This feature is useful as an workaround for missing features in the compiler.

{% code lineNumbers="true" %}
```csharp
script startup {

	import Call;

	code() {
		local temp:string;
		asm {
			LOAD $temp "hello"
		}
	}
}
```
{% endcode %}

## Map support

The compiler supports generic types, including maps.
Maps are one of the few types that don't have to initialized in the constructor.


```csharp
contract test {
	global my_state: storage_map<address, number>;

	constructor(owner:address)
	{
		my_state.set(owner, 42);
	}

	public getState(target:address):number
	{
		return my_state.get(target);
	}
}
```

## Methods variables

It is possible to use methods as variables.


{% code lineNumbers="true" %}
```csharp
contract test {

	import Runtime;
	import Map;

	global _counter:number;

	global _callMap: storage_map<address, method<address>>;

	constructor(owner:address)
	{
		_counter := 0;
	}

	public registerUser(from:address, amount:number)
	{
		local target: method<address>;

		if (amount > 10) {
			target := incCounter;
		}
		else {
			target := decCounter;
		}

		_callMap.set(from, target);
	}

	public callUser(from:address) {
		local target: method<address> := _callMap.get(from);

		Call.method(target, from);
	}

	private incCounter(target:address) {
		_counter += 1;
	}

	private subCounter(target:address) {
		_counter -= 1;
	}
}

```
{% endcode %}

## Returning multiple values

It is possible in TOMB to return multiple results from a single method.
The method return type must be marked with an asterisk, then multiple returns can be issued.
A return without expression will terminate the method execution.


{% code lineNumbers="true" %}
```csharp
contract test {
	// this method returns an array of strings (could also be numbers, structs, etc)
    public getStrings(): string* {
         return "hello";
         return "world";
         return;
    }
}
```
{% endcode %}

## NFTs

Showcases how to implement an NFT, showcasing all details including ROM, RAM and token series.

When creating an NFT, they must have 4 default properties implemented and they're:

* `name`, returns the name of the NFT
* `description`, returns the descriptions of the NFT
* `imageURL`, returns the image URL of the NFT
* `infoURL`, returns the info URL of the NFT

{% code lineNumbers="true" %}
```csharp
struct luchador_rom
{
	genes:bytes;
	name:string;
}

struct luchador_ram
{
	experience:number;
	level:number;
}

struct item_rom
{
	kind:number;
	quality:number;
}

struct item_ram
{
	power:number;
	level:number;
}

token NACHO {
	global _owner: address;

	const LUCHADOR_SERIES: number = 1;
	const LUCHADOR_SUPPLY: number = 100000;

	const ITEM_SERIES: number = 2;
	const ITEM_SUPPLY: number = 500000;

	property name: string = "Nachomen";

	property isBurnable: bool = true;
	property isFinite: bool = true;
	property isFungible: bool = false;
	property maxSupply: number = LUCHADOR_SUPPLY + ITEM_SUPPLY;

	nft luchador<luchador_rom, luchador_ram> {

		property name: string {
			return _ROM.name;
		}

		property description: string {
			return "Luchador with level " + _RAM.level;
		}

		property imageURL: string {
			return "https://nacho.men/img/luchador/"+ _tokenID;
		}

		property infoURL: string {
			return "https://nacho.men/api/luchador/"+ _tokenID;
		}
	}

	nft item<item_rom, item_ram> {

		property name: string {
			switch (_ROM.kind)
			{
				case 1: return "Potion";
				case 2: return "Gloves";
				default: return "Item #" + _ROM.kind;
			}
		}

		property description: string {
			return "Item level " + _RAM.level;
		}

		property imageURL: string {
			return "https://nacho.men/img/item/"+ _tokenID;
		}

		property infoURL: string {
			return "https://nacho.men/api/item/"+ _tokenID;
		}
	}

	constructor (addr:address) {
		_owner := addr;
		// at least one token series must exist, here we create 2 series
		// they don't have to be created in the constructor though, can be created later
		NFT.createSeries(_owner, $THIS_SYMBOL, LUCHADOR_SERIES, LUCHADOR_SUPPLY, TokenSeries.Unique, luchador);
		NFT.createSeries(_owner, $THIS_SYMBOL, ITEM_SERIES, ITEM_SUPPLY, TokenSeries.Unique, item);
	}
}
```
{% endcode %}

## Random numbers

It is possible to generate pseudo random numbers, and also to control the generation seed.
If a seed is not specified, then the current transaction hash will be used as seed, if available.


{% code lineNumbers="true" %}
```csharp
contract test {
	import Random;

	global my_state: number;

	constructor(owner:address)
	{
		Random.seed(16676869); // optionally we can specify a seed, this will make the next sequence of random numbers to be deterministic
		my_state = mutateState();
	}

	public mutateState():number
	{
		my_state = Random.generate() % 1024; // Use modulus operator to constrain the random number to a specific range
		return my_state;
	}
}
```
{% endcode %}

## Scripts

### Default

A script is something that can be used either for a transaction or for an API invokeScript call.
This example showcases a simple script with one argument, that calls a contract.
Note that for scripts with arguments, for them to run properly you will have to push them into the stack before.

{% code lineNumbers="true" %}
```csharp
script startup {

	import Call;

	code(target:address) {
		local temp:number := 50000;
		Call.contract("Stake", "Unstake", target, temp);
	}
}
```
{% endcode %}



### Deploy contract

This example showcases a script that deploys a token contract.

{% code lineNumbers="true" %}
```csharp
token GHOST {
...
}

script deploy {

    import Token;
    import Module;

    code() {
        local maxSupply:number := 50000;
        local decimals:number := 1;
		local flags:TokenFlags := TokenFlags.None;
        Token.create(@P2KAkQRrL62zYvb5198CHBLiKHKr4bJvAG7aXwV69rtbeSz, "GHOST",  "Ghost Token", maxSupply, decimals, flags, Module.getScript(GHOST),  Module.getABI(GHOST));
    }
}
```
{% endcode %}

### Minting script

This example showcases a script that mints a custom NFT.


{% code lineNumbers="true" %}
```csharp
struct my_rom_data {
	name:string;
	counter:number;
}

script token_minter {

	import Token;

	code(source:address, target:address) {
		local rom_data:my_rom_data := Struct.my_rom_data("hello", 123);
		NFT.mint(source, target, "LOL", rom_data, "ram_can_be_anything");
	}
}
```
{% endcode %}

## Simple Counter

Simple contract that implements a global counter (that can be incremented by anyone who calls the contract).
Note that any global variable that is not generic must be initialized in the contract constructor.


{% code lineNumbers="true" %}
```csharp
contract test {
	global counter: number;

	constructor(owner:address)
	{
		counter:= 0;
	}

	public increment()
	{
		if (counter < 0){
			throw "invalid state";
		}
		counter += 1;
	}
}
```
{% endcode %}

## Simple Sum

Simple contract that sums two numbers and returns the result.

{% code lineNumbers="true" %}
```csharp
contract test {
	public sum(a:number, b:number):number
	{
		return a + b;
	}
}
```
{% endcode %}

## Strings

### Default usage

Simple contract that shows how to use strings and built-in type methods, string.length() in this specific case.

{% code lineNumbers="true" %}
```csharp
contract test {
	global val: string;

	constructor(owner:address)
	{
		val = "hello";
		val += " world";
	}

	public getLength():number
	{
		return val.length();
	}
}
```
{% endcode %}

### String Manipulation

The compiler supports casting strings into number arrays (unicode values) and number arrays back to strings.


{% code lineNumbers="true" %}
```csharp
contract test {
	import Array;

	public toUpper(s:string):string
	{
		local my_array: array<number>;

		// extract chars from string into an array
		my_array := s.toArray();

		local length :number := Array.length(my_array);

		for (local i = 0; i<length; i+=1)
		{
			local ch : number := my_array[i];

			if (ch >= 97) {
				if (ch <= 122) {
					my_array[i] := ch - 32;
				}
			}
		}

		// convert the array back into a unicode string
		local result:string := String.fromArray(my_array);
		return result;
	}
}
```
{% endcode %}

## Switch case

Simple contract that received a number and returns a string, while using a switch case.

{% code lineNumbers="true" %}
```csharp
contract test {
    public check(x:number): string {
        switch (x) {
            case 0: return "zero";
            case 1: return "one";
            case 2: return "two";
            default: return "other";
        }
    }
}
```
{% endcode %}

## Tasks

A task allows a contract method to run periodically without user intervention.
Tasks can't have parameters, however you can use Task.current() along with a global Map to associate custom user data to each task.


{% code lineNumbers="true" %}
```csharp
contract test {
	import Time;
	import Task;

	global victory:bool;
	global deadline:timestamp;

	constructor(owner:address) {
		victory := false;
		time := Time.now() + time.hours(2);
		Task.start(checkResult, owner, 0, TaskFrequency.Always, 999);
	}

	task checkResult()  {
		if (victory) {
			break;
		}

		local now: timestamp := Time.now();

		if (time >= deadline) {
			break;
		}

		continue;
	}

	public win(from:address)
	{
		victory := true;
	}
}

```
{% endcode %}

## Type interface in variable declarations

It is possible to let TOMB compiler auto-detect type of a local variable if you omit the type and provide an initialization expression.


{% code lineNumbers="true" %}
```csharp
contract test {
    public calculate():string {
         local a := "hello ";
         local b := "world";
        return a + b;
    }
}
```
{% endcode %}
