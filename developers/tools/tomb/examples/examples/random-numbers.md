# Random numbers

It is possible to generate pseudo random numbers, and also to control the generation seed.\
If a seed is not specified, then the current transaction hash will be used as seed, if available.\


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
