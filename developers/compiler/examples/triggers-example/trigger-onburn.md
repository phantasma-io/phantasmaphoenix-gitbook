# Trigger OnBurn

## Example 1&#x20;

In this example, this contract only burn if it's the owner and reject anything else.

{% code lineNumbers="true" %}
```csharp
contract test {
    import Runtime;
    global owner : address;
    trigger onBurn(from:address, symbol:string, amount:number)
    {
        Runtime.expect(Runtime.isWitness(owner), "Only owner can burn!");
        return;
    }
}
```
{% endcode %}

