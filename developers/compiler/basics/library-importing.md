# Library Importing

Choose a compiler library from the library reference, then import it at the top of the contract body.

{% content-ref url="../libraries.md" %}
[libraries.md](../libraries.md)
{% endcontent-ref %}

## Example

In this example, the contract imports the **NFT** library. The same import pattern applies to the other compiler libraries.

{% code lineNumbers="true" %}
```csharp
contract test {
	import NFT;
	
	public mintSample(from:address, to:address, symbol:string, rom:any, ram:any)
	{
		NFT.mint(from, to, symbol, rom, ram, 1);
	}
}
```
{% endcode %}

{% hint style="info" %}
Only import libraries that the current compiler and validator support. For NFT RAM updates, `NFT.write(...)` maps to `Runtime.WriteToken(...)` on current Carbon validators.
{% endhint %}
