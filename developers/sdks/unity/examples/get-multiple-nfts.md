# Get Multiple NFTs

{% hint style="warning" %}
This functionality is not yet available and will be released according to the [roadmap](https://phantasma.info/blockchain#roadmap)
{% endhint %}

This example demonstrates how to fetch multiple NFTs at once using the `GetNFTs()` method from the `PhantasmaAPI` class. The number of fetched NFTs is then logged to the console.

```csharp
public void GetNFTs()
{
    PhantasmaAPI api = new PhantasmaAPI("https://testnet.phantasma.info/rpc");
    var symbol = "CROWN";
    var IDs = new String[] { "" };
    StartCoroutine(api.GetNFTs(symbol, IDs, (nfts) =>
    {
        Debug.Log(nfts.Length);
    }));
}
```
