# NFT

{% hint style="info" %}
The NFT library exposes methods that allow minting, burning, [infusing](https://docs.phantasma.io/#nft-infusion) and transfering Phantasma NFTs.
{% endhint %}

| Method                                                                                                  | Return type | Description                                                                               |
| ------------------------------------------------------------------------------------------------------- | ----------- | ----------------------------------------------------------------------------------------- |
| NFT.transfer(from:Address, to:Address, symbol:String, id:Number)                                        | None        | Transfer an NFT from one address to another, by the nftID and symbol.                     |
| NFT.mint(from:Address, to:Address, symbol:String, rom:Any, ram:Any, seriesID:Number)                    | None        | Mint an NFT from one address to another, with the specific ROM and RAM, and the seriesID. |
| NFT.write(from:Address, symbol:String, tokenID:Number, ram:Any)                                         | None        | Write NFT is to update the RAM inside the NFT by the nftID.                               |
| NFT.burn(from:Address, symbol:String, id:Number)                                                        | None        | Burn the nft by the NFTID.                                                                |
| NFT.infuse(from:Address, symbol:String, id:Number, infuseSymbol:String, infuseValue:Number)             | None        | Infuse the NFT with other tokens/NFT with a given amount.                                 |
| NFT.createSeries(from:Address, symbol:String, seriesID:Number, maxSupply:Number, mode:Enum, nft:Module) | None        | Creates a series of NFTs.                                                                 |
| NFT.readROM(symbol:String, id:Number)                                                                   | T           | Returns the ROM by the NFTID.                                                             |
| NFT.readRAM(symbol:String, id:Number)                                                                   | T           | Returns the RAM by the NFTID.                                                             |

\
