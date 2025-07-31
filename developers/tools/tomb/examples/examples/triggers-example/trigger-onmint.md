# Trigger OnMint

## Example 1&#x20;

In this example, this token will check the symbol, the address that called, and check it was called from within the contract and reject anything else.

{% code lineNumbers="true" fullWidth="true" %}
```csharp
token TEST {
    import Runtime;
    trigger onMint(from:address, to:address, symbol:string, tokenID:number) 
    {
        local contractSymbol: string = $THIS_SYMBOL;
        local thisAddr : address = $THIS_ADDRESS;
        Runtime.expect(symbol == contractSymbol, "invalid symbol");
        Runtime.expect(from == thisAddr, "minting failed -> Not Contract");
        Runtime.expect(Runtime.isWitness(thisAddr), "minting failed -> not Contract");
        return;
    }
}
```
{% endcode %}

