# Oracle

{% hint style="info" %}
The Oracle library exposes access to the [oracle](https://docs.phantasma.io/#chain-oracles) features of Phantasma
{% endhint %}

| Method                                                             | Return type | Description                                                                                       |
| ------------------------------------------------------------------ | ----------- | ------------------------------------------------------------------------------------------------- |
| Oracle.read(url:String)                                            | None        | Executes an URL read via oracles. The URL must be a valid Phantasma Oracle URL.                   |
| Oracle.price(symbol:String)                                        | None        | Reads the current price of the given symbol via oracles.                                          |
| Oracle.quote(baseSymbol:String, quoteSymbol:String, amount:Number) | None        | Returns the current price converted to the given quote symbol with the given amount, via oracles. |
