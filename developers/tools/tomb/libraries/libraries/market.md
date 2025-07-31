# Market

{% hint style="info" %}
The Market library exposes access to methods that allow to buy and sell NFts (including auctions) in shared liquidity NFT markets of Phantasma.
{% endhint %}

| Method                                                                                                                                                                                                                                                 | Return type | Description                                           |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- | ----------------------------------------------------- |
| Market.sell(from:Address, baseSymbol:String, quoteSymbol:String, tokenID:Number, price:Number, endDate:Timestamp)                                                                                                                                      | None        | To sell an NFT, by the tokenID.                       |
| Market.buy(from:Address, symbol:String, tokenID:Number)                                                                                                                                                                                                | None        | To buy an NFT, by the tokenID.                        |
| Market.cancel(symbol:String, tokenID:Number)                                                                                                                                                                                                           | None        | To cancel a Sell.                                     |
| Market.hasAuction(symbol:String, tokenID:Number)                                                                                                                                                                                                       | Bool        | Returns true if has an auction for the given tokenID. |
| Market.bid(from:Address, symbol:String, tokenID:Number, price:Number, buyingFee:Number, buyingFeeAddress:Address)                                                                                                                                      | None        | To bid for the given tokenID.                         |
| Market.listToken(from:Address, baseSymbol:String, quoteSymbol:String, tokenID:Number, price:Number, endPrice:Number, startDate:Timestamp, endDate:Timestamp, extensionPeriod:Number, typeAuction:Number, listingFee:Number, listingFeeAddress:Address) | None        | To list the token by the TokenID.                     |
| Market.editAuction(from:Address, baseSymbol:String, quoteSymbol:String, tokenID:Number, price:Number, endPrice:Number, startDate:Timestamp, endDate:Timestamp, extensionPeriod:Number)                                                                 | None        | To edit the auction for the given tokenID.            |

\
