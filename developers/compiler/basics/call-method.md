# Call method

Showcases how a contract method can call other methods.\
If a method is declared private, it can't be called by anyone except the actual contract that implements it.

{% code lineNumbers="true" %}
```csharp
contract test {
	private sum(a:number, b:number) {
		return a + b;
	}

	public calculatePrice(x:number): number
	{		
		local price: number = 10;
		price = this.sum(price, x); // here we use 'this' for calling another method

		return price;
	}
}
```
{% endcode %}
