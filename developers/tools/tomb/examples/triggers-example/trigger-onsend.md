# Trigger OnSend

## Example 1&#x20;

In this example, this account will only accept transfers of KCAL and reject anything else.

{% code lineNumbers="true" %}
```csharp
contract test {

    trigger onSend(from:address, symbol:string, amount:number)
    {
        if (symbol != "KCAL") {
            throw "can't send asset: " + symbol;
        }
        
        return;
    }
}
```
{% endcode %}
