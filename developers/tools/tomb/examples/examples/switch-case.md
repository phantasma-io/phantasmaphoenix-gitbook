# Switch case

Simple contract that received a number and returns a string, while using a switch case.

{% code lineNumbers="true" %}
```csharp
contract test {
    public check(x:number): string {
        switch (x) {
            case 0: return "zero";
            case 1: return "one";
            case 2: return "two";
            default: return "other";
        }                  
    }
}
```
{% endcode %}
