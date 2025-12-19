# Update an NFT's RAM

{% hint style="warning" %}
This functionality is currently disabled and will be re‑enabled according to the [roadmap](https://phantasma.info/blockchain#roadmap)
{% endhint %}

This example shows how to update the RAM of an NFT. A transaction script is created and sent using the `SendTransaction()` method from the `PhantasmaLinkClient` class.

```csharp
public void UpdateNFTsRAM()
{
    if (!PhantasmaLinkClient.Instance.IsLogged) return;

    ScriptBuilder sb = new ScriptBuilder();
    var userAddress = Address.Parse(PhantasmaLinkClient.Instance.Address);
    var symbol = "NSYM";
    var ram = new byte[0];
    var tokenID = new BigInteger("0");
    var payload = System.Text.Encoding.UTF8.GetBytes("OurDappExample");
    var script = sb.AllowGas(userAddress, Address.Null, PhantasmaLinkClient.Instance.GasPrice, PhantasmaLinkClient.Instance.GasLimit ).
        CallInterop("Runtime.WriteToken", userAddress, symbol, tokenID, ram).
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
