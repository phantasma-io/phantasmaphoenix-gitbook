# Triggers

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

The chain runs these triggers only when the operation runs in the VM: in contract code or in a script transaction. A structured transaction that transfers, mints or burns a token does not run `onSend`, `onReceive`, `onMint` or `onBurn`. This covers `TransferFungible`, `TransferNonFungible_Single`, `TransferNonFungible_Multi`, `MintFungible`, `MintNonFungible`, `BurnFungible`, `BurnNonFungible` and the `_GasPayer` forms of the transfers and burns. A trigger therefore cannot ban the transfer or the burn of a token: the holder can send the same operation as a structured transaction.

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
