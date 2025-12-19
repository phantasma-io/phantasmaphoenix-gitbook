# Burn an NFT

{% hint style="warning" %}
This functionality is currently disabled and will be re‑enabled according to the [roadmap](https://phantasma.info/blockchain#roadmap)
{% endhint %}

This example demonstrates how to burn an NFT, permanently removing it from the Phantasma blockchain. A transaction script is created and sent using the `SendTransaction()` method from the `PhantasmaLinkClient` class.

```csharp
public void BurnNFT()
{
    if (!PhantasmaLinkClient.Instance.IsLogged) return;

    ScriptBuilder sb = new ScriptBuilder();
    var userAddress = Address.Parse(PhantasmaLinkClient.Instance.Address);
    var symbol = "CROWN";
    var id = new BigInteger("1000000000000");
    var payload = System.Text.Encoding.UTF8.GetBytes("OurDappExample");
    var script = sb.AllowGas(userAddress, Address.Null, PhantasmaLinkClient.Instance.GasPrice, PhantasmaLinkClient.Instance.GasLimit ).
        CallInterop("Runtime.BurnToken", userAddress, symbol, id).
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
