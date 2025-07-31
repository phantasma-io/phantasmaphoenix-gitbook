# Decimals

There is compiler support for decimal numbers.\
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
