# Trigger Examples

## Trigger OnUpgrade

{% hint style="info" %}
This method will be **triggered** when a **contract** / **token** is **upgraded**.

Keep in mind that if you don't implement this method it's not possible to upgrade it.

Also add validations to keep it safe and secure.
{% endhint %}

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

## Trigger OnMint

{% hint style="info" %}
This method will be **triggered** when a token is **minted**.
{% endhint %}

In this example, this token will check the symbol, the address that called, and check it was called from within the contract and reject anything else.

{% code lineNumbers="true" fullWidth="true" %}
```csharp
token TEST {
    import Runtime;
    trigger onMint(from:address, to:address, symbol:string, tokenID:number)
    {
        local contractSymbol: string = $THIS_SYMBOL;
        local thisAddr : address = $THIS_ADDRESS;
        Runtime.expect(symbol == contractSymbol, "invalid symbol");
        Runtime.expect(from == thisAddr, "minting failed -> Not Contract");
        Runtime.expect(Runtime.isWitness(thisAddr), "minting failed -> not Contract");
        return;
    }
}
```
{% endcode %}

## Trigger OnBurn

{% hint style="info" %}
This method will be **triggered** when a token is **burned**.
{% endhint %}

In this example, this contract only burn if it's the owner and reject anything else.

{% code lineNumbers="true" %}
```csharp
contract test {
    import Runtime;
    global owner : address;
    trigger onBurn(from:address, symbol:string, amount:number)
    {
        Runtime.expect(Runtime.isWitness(owner), "Only owner can burn!");
        return;
    }
}
```
{% endcode %}

## Trigger OnSeries

{% hint style="info" %}
This method will be **triggered** when a series is **created.**
{% endhint %}

In this example, this contract when a series is created will check if it was the owner that did it and reject anything else.

{% code lineNumbers="true" %}
```csharp
contract test {
    import Runtime;
    global owner : address;

    trigger onSeries(from:address)
    {
        Runtime.expect(Runtime.isWitness(owner), "not the owner");
        return;
    }
}
```
{% endcode %}

## Trigger OnInfuse

{% hint style="info" %}
This method will be **triggered** when a token is **infused**.
{% endhint %}

In this example, this token will only accept being infused with the same token and reject anything else.

{% code lineNumbers="true" %}
```csharp
token TEST {
    import Runtime;
    trigger onInfuse(from:address, target:address, symbol:string, nftID:number)
    {
        local thisSymbol = $THIS_SYMBOL;
        Runtime.expect( thisSymbol == symbol, "Only with this token can be infused");
        return;
    }
}
```
{% endcode %}

## Trigger OnWrite

{% hint style="info" %}
This method will be **triggered** when **NFT.Write** is called. (When **NFT** ram is being updated)
{% endhint %}

In this example, this token will only be able to be updated if it's the owner that called the change  and reject anything else.

{% code lineNumbers="true" %}
```csharp
token TEST {
    import Runtime;
    global owner: Address;
    trigger onWrite(from:address, ram:bytes, tokenID:number)
    {
        Runtime.expect(Runtime.isWitness(owner), "Only owner can update");
        return;
    }
}
```
{% endcode %}

## Trigger OnSend

{% hint style="info" %}
This method will be **triggered** when a token is **sent**.

It's possible to prevent from sending external tokens!
{% endhint %}

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

## Trigger OnReceive

{% hint style="info" %}
This method will be **triggered** when a token is **received**.

It's possible to prevent receiving external tokens!
{% endhint %}

### Example 1

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

### Example 2

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

## Trigger OnMigrate

{% hint style="info" %}
this method will be **triggered** when a user **migrates** **the** **account**.
{% endhint %}

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

## Trigger OnKill

{% hint style="danger" %}
This method will be **triggered** when you want to **destroy/delete** the token.

Be very careful when implementing this trigger.
{% endhint %}

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
