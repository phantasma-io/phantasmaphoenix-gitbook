# Map support

The compiler supports generic types, including maps.\
Maps are one of the few types that don't have to initialized in the constructor.\


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
