# Get NFT

This example shows how to fetch an NFT's details using the `GetNFT()` method from the `PhantasmaAPI` class. The NFT details are then logged to the console.

```csharp
public void GetNFT()
{
     PhantasmaAPI api = new PhantasmaAPI("https://testnet.phantasma.io/rpc");
     var symbol = "CROWN";
     var ID = "";
     StartCoroutine(api.GetNFT(symbol, ID, (nft) =>
     {
         Debug.Log(nft);
     }));
}
```
