# Simple Counter

Simple contract that implements a global counter (that can be incremented by anyone who calls the contract).\
Note that any global variable that is not generic must be initialized in the contract constructor.\


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
