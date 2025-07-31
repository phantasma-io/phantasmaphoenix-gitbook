# Tokens

## Transfer Tokens

A contract that takes a payment in tokens from a user.\
Showcases how to transfer tokens and how to use macro $THIS\_ADDRESS to obtain address of the contract.

{% code lineNumbers="true" %}
```csharp
contract test {
	import Runtime;
	import Token;

	public paySomething(from:address, quantity:number)
	{
		Runtime.expect(Runtime.isWitness(from), "witness failed");

		local price: number = 10;
		price *= quantity;

		local thisAddr:address = $THIS_ADDRESS;
		Token.transfer(from, thisAddr, "SOUL", price);

		// TODO after payment give something to 'from' address
	}
}
```
{% endcode %}

## Token Flags

There are also some built-in enums, like TokenFlags.\


{% code lineNumbers="true" %}
```csharp
contract test {
	import Runtime;
	import Token;

	public paySomething(from:address, amount:number, symbol:string)
	{
		Runtime.expect(Runtime.isWitness(from), "witness failed");

		local flags:TokenFlags := Token.getFlags(symbol);

		if (flags.isSet(TokenFlags.Fungible)) {
			local thisAddr:address := $THIS_ADDRESS;
			Token.transfer(from, thisAddr, "SOUL", price);
		}
	}
}
```
{% endcode %}
