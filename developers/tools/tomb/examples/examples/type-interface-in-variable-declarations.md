# Type interface in variable declarations

It is possible to let TOMB compiler auto-detect type of a local variable if you omit the type and provide an initialization expression.\


{% code lineNumbers="true" %}
```csharp
contract test {
    public calculate():string {
         local a := "hello ";
         local b := "world";
        return a + b;
    }
}
```
{% endcode %}

