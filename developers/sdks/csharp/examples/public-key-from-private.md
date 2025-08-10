# Public Key From Private

This example demonstrates how to extract a public key from a private key

```csharp
public void PublicKeyFromPrivate()
{
	// Load private key
	var keys = PhantasmaKeys.FromWIF("PK_in_WIF_format");

	// Or
	// var keys = new PhantasmaKeys(Base16.Decode("PK_in_HEX_format"));

	Console.WriteLine($"Address: {keys.Address.Text}");
	Console.WriteLine($"Public (HEX): {Base16.Encode(keys.PublicKey)}");
}
```
