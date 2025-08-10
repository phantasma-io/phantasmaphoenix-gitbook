# Mint an NFT

{% hint style="warning" %}
This functionality is not yet available and will be released according to the [roadmap](https://phantasma.info/blockchain#roadmap)
{% endhint %}

This example demonstrates how to mint an NFT on the Phantasma blockchain. A transaction script is created and sent using the `SendTransaction()` method from the `PhantasmaLinkClient` class.

```csharp
public void MintNFT()
{
    if (!PhantasmaLinkClient.Instance.IsLogged) return;

    ScriptBuilder sb = new ScriptBuilder();
    var userAddress = Address.FromText(PhantasmaLinkClient.Instance.Address);
    var toAddress = Address.FromText("P2KKEjZK7AbcKZjuZMsWKKgEjNzeGtr2zBiV7qYJHxNXvUa");
    var symbol = "NSYM";
    var rom = new byte[0];
    var ram = new byte[0];
    var series = new BigInteger("0");
    var payload = Base16.Decode("OurDappExample");
    var script = sb.AllowGas(userAddress, Address.Null, PhantasmaLinkClient.Instance.GasPrice, PhantasmaLinkClient.Instance.GasLimit ).
        CallInterop("Runtime.MintToken", userAddress, toAddress, symbol, rom, ram, series).
        SpendGas(userAddress).
        EndScript();
    
    PhantasmaLinkClient.Instance.SendTransaction("main", script, payload, (hash, s) =>
    {
        if ( hash.IsNull )
        {
            Debug.Log("Transaction failed: " + s);
            return;
        }
        
        Debug.Log("Transaction sent: " + hash);
    });
}
```
