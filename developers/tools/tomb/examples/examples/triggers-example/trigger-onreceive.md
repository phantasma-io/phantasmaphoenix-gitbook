# Trigger OnReceive

## Example 1&#x20;

In this example, this account will only accept transfers of KCAL and reject anything else.

{% code lineNumbers="true" %}
```csharp
contract test {

    trigger onReceive(from:address, symbol:string, amount:number)
    {
        if (symbol != "KCAL") {
            throw "can't receive asset: " + symbol;
        }
        
        return;
    }
}
```
{% endcode %}

## Example 2

In this example, any asset sent to this account will be auto-converted into SOUL.

{% code lineNumbers="true" %}
```csharp
contract test {
    import Call;
    trigger onReceive(from:address, symbol:string, amount:number)
    {
        if (symbol != "SOUL") {
            Call.contract("Swap", "SwapTokens", from, symbol, "SOUL", amount);
        }
        
        return;
    }
}
```
{% endcode %}
