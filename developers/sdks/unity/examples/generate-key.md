# Generate Key

This example demonstrates how to generate a new private/public key pair

```csharp
public void GenerateKey()
{
    // Generate a new random private key and derive corresponding address and public key
    var key = PhantasmaKeys.Generate();

    // Log key data including address, private key in HEX, and WIF format for debugging or export
    Debug.Log($"[GenerateKey] Address: {key.Address.Text}, HEX: {Base16.Encode(key.PrivateKey)}, WIF: {key.ToWIF()}");
}
```
