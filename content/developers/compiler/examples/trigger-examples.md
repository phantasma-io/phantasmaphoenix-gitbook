---
title: "Trigger Examples"
weight: 140
---

## Trigger OnAttach

> [!NOTE]
> This trigger runs when VM code is attached to an already existing token through the token attach flow.

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

> [!NOTE]
> This method runs when a contract or token-backed contract is upgraded.
>
> Keep in mind that if you don't implement this method it's not possible to upgrade it.
>
> Also add validations to keep it safe and secure.

In this example, this contract will only be updated if it's the owner that called it and reject anything else.

> [!WARNING]
> Make sure to **add** a **validation** like this, else your **contract** can be **hacked** and **updated** without your **consent**!

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

## Trigger OnMint

> [!NOTE]
> This method runs when the token is minted in the VM, for example by `Token.mint` or `NFT.mint`. A structured `MintFungible` or `MintNonFungible` transaction does not run it.

In this example, the trigger checks the symbol and requires the mint to name the contract itself as the source (`from`).

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

> [!WARNING]
> A contract is never a witness of its own address. `Runtime.isWitness($THIS_ADDRESS)` returns `false` in triggers and in methods, so a check on it rejects every mint.

## Trigger OnBurn

> [!NOTE]
> This method runs when the token is burned in the VM, for example by `Token.burn` or `NFT.burn`. The chain refuses a structured `BurnFungible` or `BurnNonFungible` transaction for a token whose contract declares `onBurn`, so a holder can burn the token only through the VM, where the trigger runs.

In this example, a burn succeeds only when the address in `owner` signed the transaction.

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

## Trigger OnSeries

> [!NOTE]
> This method will be **triggered** when a series is **created.**

In this example, the contract checks that the owner initiated the series creation path.

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

## Trigger OnInfuse

> [!NOTE]
> This method runs when a token is infused into an NFT of this token through `Runtime.InfuseToken`, for example by `NFT.infuse`. The chain refuses a plain transfer into such an NFT, so a transfer cannot skip the trigger.

In this example, the token only accepts infusion with the same symbol.

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

## Trigger OnWrite

> [!NOTE]
> This method runs when NFT RAM is updated.

In this example, this token will only be able to be updated if it's the owner that called the change  and reject anything else.

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

## Trigger OnSend

> [!NOTE]
> This method runs on the token's own contract when the token is transferred in the VM, for example by `Token.transfer` or `NFT.transfer`. A structured transfer (`TransferFungible`, `TransferNonFungible_Single`, `TransferNonFungible_Multi`) does not run it, so the check applies only to transfers made in the VM. See [Triggers](../basics/triggers.md).

In this example, the token refuses a transfer from an address that its admin has frozen.

```csharp
token TEST {
    import Runtime;
    import Map;

    property name: string = "Test";

    global _admin: address;
    global frozen: storage_map<address, bool>;

    constructor(owner:address) {
        _admin = owner;
    }

    public freeze(target:address) {
        Runtime.expect(Runtime.isWitness(_admin), "only the admin can freeze");
        frozen.set(target, true);
    }

    trigger onSend(from:address, to:address, symbol:string, amount:number)
    {
        Runtime.expect(!frozen.has(from), "the sender is frozen");
        return;
    }
}
```

## Trigger OnReceive

> [!NOTE]
> This method runs on the token's own contract after `onSend`, for the same transfers. A structured transfer does not run it either. A standalone `contract` gets no trigger call when tokens arrive at its address.

In this example, the token refuses a transfer to an address that its admin has blocked.

```csharp
token TEST {
    import Runtime;
    import Map;

    property name: string = "Test";

    global _admin: address;
    global blocked: storage_map<address, bool>;

    constructor(owner:address) {
        _admin = owner;
    }

    public block(target:address) {
        Runtime.expect(Runtime.isWitness(_admin), "only the admin can block");
        blocked.set(target, true);
    }

    trigger onReceive(from:address, to:address, symbol:string, amount:number)
    {
        Runtime.expect(!blocked.has(to), "the receiver is blocked");
        return;
    }
}
```
