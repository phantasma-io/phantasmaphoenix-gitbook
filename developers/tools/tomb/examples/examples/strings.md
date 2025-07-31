# Strings

## Default usage

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

## String Manipulation

The compiler supports casting strings into number arrays (unicode values) and number arrays back to strings.\


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

###

\
