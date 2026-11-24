---
title: "Variable declaration"
linkTitle: "Variable Declaration"
weight: 80
---

### Value assignment

Earlier TOMB syntax allowed `:=` for assignment. In the current compiler surface, assignment uses only `=`.

## Global variables

A global variable is declared outside any method with the keyword `global`. Global variables are the persistent state of the contract.

```csharp
contract test {
    global myValue : number;
}
```

## Local variables

A local variable is declared inside a method with the keyword `local`. A local must be initialized before it is read and must be used; the compiler rejects an unused local.

```csharp
contract test {
    public myMethod(){
        local myVariable : string = "something";
    }
}
```
