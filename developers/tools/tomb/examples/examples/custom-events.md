# Custom Events

## Example 1

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

## Example 2

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

## Example 3

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



