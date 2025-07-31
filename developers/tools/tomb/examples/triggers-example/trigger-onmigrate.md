# Trigger OnMigrate

## Example 1&#x20;

In this example, this address migrated to another one and we check if it was the actual user that called the method and reject anything else.

{% code lineNumbers="true" %}
```csharp
contract test {
    import Runtime;
    trigger onMigrate(from:address, to:address)
    {
        Runtime.expect(Runtime.isWitness(from), "invalid witness");
    }
}
```
{% endcode %}
