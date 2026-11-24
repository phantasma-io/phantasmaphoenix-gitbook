---
title: "Triggers"
weight: 70
---

Triggers are special methods invoked by the runtime on lifecycle events.

In TOMB source they are written as `trigger onSomething(...)`.

The compiler accepts the trigger names and signatures below; an unknown name fails compilation.

## Token triggers

The validator invokes these triggers on token-backed contracts:

- `onMint`
- `onBurn`
- `onSend`
- `onReceive`
- `onInfuse`
- `onAttach`
- `onUpgrade`
- `onSeries`
- `onWrite`

The chain runs these triggers only when the operation runs in the VM: in contract code or in a script transaction. A structured transaction never runs them, and the chain handles it in one of two ways:

- A structured transfer or mint goes through without `onSend`, `onReceive` or `onMint`. This covers `TransferFungible`, `TransferNonFungible_Single`, `TransferNonFungible_Multi`, their `_GasPayer` forms, `MintFungible` and `MintNonFungible`. A holder can send a transfer this way, so `onSend` and `onReceive` cannot ban a transfer, and `onMint` cannot stop a structured mint.
- A structured burn (`BurnFungible`, `BurnNonFungible` and their `_GasPayer` forms) of a token whose contract declares `onBurn` is refused with `<symbol> has an onBurn trigger: burn it through the VM`. A transfer into an NFT whose token declares `onInfuse` is refused as well; infuse through `Runtime.InfuseToken` instead. Governance operations are exempt from both checks.

The compiler also accepts `onWitness`, `onMigrate` and `onKill`. The validator never invokes them: account migration and contract kill are not part of the current chain, so a trigger with one of these names compiles and never runs.

## Shared trigger signatures

### `onMint`, `onBurn`, `onSend`, `onReceive`, `onInfuse`

```csharp
trigger onMint(from: address, to: address, symbol: string, value: number)
trigger onBurn(from: address, to: address, symbol: string, value: number)
trigger onSend(from: address, to: address, symbol: string, value: number)
trigger onReceive(from: address, to: address, symbol: string, value: number)
trigger onInfuse(from: address, to: address, symbol: string, value: number)
```

The fourth argument is a `number`. Depending on the runtime flow, it may represent an amount or a token identifier.

### `onSeries`, `onAttach`, `onUpgrade`

```csharp
trigger onSeries(from: address)
trigger onAttach(from: address)
trigger onUpgrade(from: address)
```

### `onWrite`

```csharp
trigger onWrite(from: address, data: bytes)
```

The compiler declares the second parameter as `any`; a parameter of type
`any` cannot be placed in the ABI, so declare it as `bytes`.

### Accepted but never invoked

```csharp
trigger onWitness(from: address)
trigger onKill(from: address)
trigger onMigrate(from: address, to: address)
```

## Notes

- `onAttach` runs when VM code is attached to an existing token; `onUpgrade` runs on a later code update.
- A token-backed contract must define `onMint`; the validator refuses to create or attach one without it.
- `onInfuse` and `onWrite` run on `Runtime.InfuseToken` and `Runtime.WriteToken`; a trigger that fails rolls the operation back.
- Without an `onWrite` trigger, `Runtime.WriteToken` needs the signature of the token owner (the owner of the token, not of the NFT), or a call from the token's own contract. Otherwise it fails with `Writing the RAM of <symbol> needs the token owner's witness`.
