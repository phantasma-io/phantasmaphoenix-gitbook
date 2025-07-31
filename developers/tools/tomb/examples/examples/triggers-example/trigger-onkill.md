# Trigger OnKill

## Example 1&#x20;

In this example, this token will only be killed by the owner and reject anything else.

{% hint style="danger" %}
This is to **destroy** the contract.
{% endhint %}

{% code lineNumbers="true" %}
```csharp
contract test {
    import Runtime;
    trigger onKill(from:address)
    {
        Runtime.expect(Runtime.isWitness(owner),"only the owner can kill.");
        return;
    }
}
```
{% endcode %}

