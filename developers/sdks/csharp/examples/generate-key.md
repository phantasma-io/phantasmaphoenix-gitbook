# Generate Key

This example demonstrates how to generate a new private/public key pair

```csharp
using PhantasmaPhoenix.Cryptography;

public void GenerateKey()
{
	// Generate a new random private key and derive address and public key
	var keys = PhantasmaKeys.Generate();

	Console.WriteLine($"Address: {keys.Address.Text}");
	Console.WriteLine($"Private (WIF): {keys.ToWIF()}");
	Console.WriteLine($"Private (HEX): {Base16.Encode(keys.PrivateKey)}");
	Console.WriteLine($"Public  (HEX): {Base16.Encode(keys.PublicKey)}");
}
```
