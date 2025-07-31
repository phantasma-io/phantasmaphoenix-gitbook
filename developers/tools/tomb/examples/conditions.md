# Conditions

Like most programming languages, it is possible to do conditional branching use if statement.\
Logic operators supported include and, or and xor.\


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
