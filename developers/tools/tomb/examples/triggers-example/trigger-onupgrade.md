# Trigger OnUpgrade

## Example 1&#x20;

In this example, this contract will only be updated if it's the owner that called it and reject anything else.

{% hint style="warning" %}
Make sure to **add** a **validation** like this, else your **contract** can be **hacked** and **updated** without your **consent**!
{% endhint %}

{% code lineNumbers="true" %}
```csharp
contract test {
    import Runtime;
    global owner: address;
    
    trigger onUpgrade(from:address)
    {
        Runtime.expect(Runtime.isWitness(owner), "Only the owner can update");
    }
}
```
{% endcode %}

