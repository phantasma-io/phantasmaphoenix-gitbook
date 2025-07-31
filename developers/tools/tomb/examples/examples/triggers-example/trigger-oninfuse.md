# Trigger OnInfuse

## Example 1&#x20;

In this example, this token will only accept being infused with the same token and reject anything else.

{% code lineNumbers="true" %}
```csharp
token TEST {
    import Runtime;
    trigger onInfuse(from:address, target:address, symbol:string, nftID:number)
    {
        local thisSymbol = $THIS_SYMBOL;
        Runtime.expect( thisSymbol == symbol, "Only with this token can be infused");
        return;
    }
}
```
{% endcode %}

