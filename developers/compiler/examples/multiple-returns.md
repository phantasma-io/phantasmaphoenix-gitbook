# Multiple returns



### Returning multiple values

It is possible in TOMB to return multiple results from a single method.\
The method return type must be marked with an asterisk, then multiple returns can be issued.\
A return without expression will terminate the method execution.\


{% code lineNumbers="true" %}
```csharp
contract test {
	// this method returns an array of strings (could also be numbers, structs, etc)
    public getStrings(): string* {
         return "hello";
         return "world";
         return;
    }
}
```
{% endcode %}

