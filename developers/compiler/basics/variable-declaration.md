# Variable declaration

### Value assignment

On the earlier versions of Phoenix Smart Language (formerly TOMB), the assignment of values to the variables used `:=`and that changed to only using the `=`V

## Global variables

A global variable is declared outside any method and uses the keyword `global` so the compiler know's that variable is a global variable.

On the example below, you can see a declaration of a global variable of type number.

{% code lineNumbers="true" %}
```csharp
contract test {
    global myValue : number;
}
```
{% endcode %}

## Local variables

A local variable needs to declared inside a method, and it uses the `local` keyword so the compiler know's that variable is a local variable.

On the example below, you can see a declarion of a local variable of type string;&#x20;

{% code lineNumbers="true" %}
```csharp
contract test {
    public myMethod(){
        local myVariable : string = "something";
    }
}
```
{% endcode %}

