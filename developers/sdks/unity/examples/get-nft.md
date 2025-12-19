# Get NFT

{% hint style="warning" %}
This functionality is partially implemented. Some features may be missing; see the [roadmap](https://phantasma.info/blockchain#roadmap).
{% endhint %}

This example shows how to fetch an NFT's details using the `GetNFT()` method from the `PhantasmaAPI` class. The NFT details are then logged to the console.

```csharp
public void GetNFT()
{
     PhantasmaAPI api = new PhantasmaAPI("https://testnet.phantasma.info/rpc");
     var symbol = "CROWN";
     var tokenId = "1";
     var loadProperties = true;
     StartCoroutine(api.GetNFT(symbol, tokenId, loadProperties, (nft) =>
     {
         Debug.Log(nft);
     }));
}
```
