# Trigger Examples

## Trigger OnAttach

{% hint style="info" %}
This trigger runs when VM code is attached to an already existing token through the token attach flow.
{% endhint %}

```csharp
token TEST {
    import Runtime;

    property name: string = "Test";

    global attached: bool;

    trigger onAttach(from:address)
    {
        Runtime.expect(Runtime.isWitness(from), "witness failed");
        attached = true;
    }
}
```

## Trigger OnUpgrade

{% hint style="info" %}
This method runs when a contract or token-backed contract is upgraded.

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
This method runs when the token is minted in the VM, for example by `Token.mint` or `NFT.mint`. A structured `MintFungible` or `MintNonFungible` transaction does not run it.
{% endhint %}

In this example, the trigger checks the symbol and requires the mint to name the contract itself as the source (`from`).

{% code lineNumbers="true" fullWidth="true" %}
```csharp
token TEST {
    import Runtime;

    property name: string = "Test";

    trigger onMint(from:address, to:address, symbol:string, value:number)
    {
        local contractSymbol: string = $THIS_SYMBOL;
        local thisAddr : address = $THIS_ADDRESS;
        Runtime.expect(symbol == contractSymbol, "invalid symbol");
        Runtime.expect(from == thisAddr, "minting failed -> Not Contract");
        return;
    }
}
```
{% endcode %}

{% hint style="warning" %}
A contract is never a witness of its own address. `Runtime.isWitness($THIS_ADDRESS)` returns `false` in triggers and in methods, so a check on it rejects every mint.
{% endhint %}

## Trigger OnBurn

{% hint style="info" %}
This method runs when the token is burned in the VM, for example by `Token.burn` or `NFT.burn`. A structured `BurnFungible` or `BurnNonFungible` transaction does not run it, so `onBurn` cannot stop a holder from burning.
{% endhint %}

In this example, a burn made in the VM succeeds only when the address in `owner` signed the transaction.

{% code lineNumbers="true" %}
```csharp
token TEST {
    import Runtime;

    property name: string = "Test";

    global owner : address;

    trigger onBurn(from:address, to:address, symbol:string, amount:number)
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

In this example, the contract checks that the owner initiated the series creation path.

{% code lineNumbers="true" %}
```csharp
token TEST {
    import Runtime;

    property name: string = "Test";

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

In this example, the token only accepts infusion with the same symbol.

{% code lineNumbers="true" %}
```csharp
token TEST {
    import Runtime;

    property name: string = "Test";

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
This method runs when NFT RAM is updated.
{% endhint %}

In this example, this token will only be able to be updated if it's the owner that called the change  and reject anything else.

{% code lineNumbers="true" %}
```csharp
token TEST {
    import Runtime;

    property name: string = "Test";

    global owner: address;

    trigger onWrite(from:address, ram:bytes)
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

    trigger onSend(from:address, to:address, symbol:string, amount:number)
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

In this example, this account will only accept transfers of KCAL and reject anything else.

{% code lineNumbers="true" %}
```csharp
contract test {

    trigger onReceive(from:address, to:address, symbol:string, amount:number)
    {
        if (symbol != "KCAL") {
            throw "can't receive asset: " + symbol;
        }

        return;
    }
}
```
{% endcode %}
