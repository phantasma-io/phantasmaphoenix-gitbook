# Trigger OnWrite

## Example 1&#x20;

In this example, this token will only be able to be updated if it's the owner that called the change  and reject anything else.

{% code lineNumbers="true" %}
```csharp
token TEST {
    import Runtime;
    global owner: Address;
    trigger onWrite(from:address, ram:bytes, tokenID:number)
    {
        Runtime.expect(Runtime.isWitness(owner), "Only owner can update");
        return;
    }
}
```
{% endcode %}

