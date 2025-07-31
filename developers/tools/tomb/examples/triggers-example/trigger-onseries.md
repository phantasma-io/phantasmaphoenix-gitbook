# Trigger OnSeries

## Example 1&#x20;

In this example, this contract when a series is created will check if it was the owner that did it and reject anything else.

{% code lineNumbers="true" %}
```csharp
contract test {
    import Runtime;
    global owner : address;
    
    trigger onSeries(from:address)
    {
        Runtime.expect(Runtime.isWitness(owner), "not the owner");
        return;
    }
}
```
{% endcode %}
