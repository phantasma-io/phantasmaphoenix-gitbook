---
title: "Library Importing"
weight: 50
---

Choose a compiler library from the library reference, then import it at the top of the contract body.

- [Libraries](../libraries.md)

## Example

In this example, the contract imports the **NFT** library. The same import pattern applies to the other compiler libraries.

```csharp
contract test {
	import NFT;

	public mintSample(from:address, to:address, symbol:string, rom:bytes, ram:bytes)
	{
		NFT.mint(from, to, symbol, rom, ram, 1);
	}
}
```

> [!NOTE]
> Only import libraries that the current compiler and validator support. For NFT RAM updates, `NFT.write(...)` maps to `Runtime.WriteToken(...)` on current Carbon validators.
