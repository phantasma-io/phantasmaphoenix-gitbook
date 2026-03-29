# Triggers

Triggers are special methods invoked by the runtime on lifecycle events.

In TOMB source they are written as `trigger onSomething(...)`.

The compiler accepts only the trigger names and signatures it currently implements. If you use an unknown trigger name, compilation fails.

## Token triggers

Currently accepted token trigger names:

- `onMint`
- `onBurn`
- `onSend`
- `onReceive`
- `onInfuse`
- `onAttach`
- `onUpgrade`
- `onSeries`
- `onWrite`
- `onMigrate`
- `onKill`

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

### `onWitness`, `onSeries`, `onKill`, `onAttach`, `onUpgrade`

```csharp
trigger onWitness(from: address)
trigger onSeries(from: address)
trigger onKill(from: address)
trigger onAttach(from: address)
trigger onUpgrade(from: address)
```

### `onMigrate`

```csharp
trigger onMigrate(from: address, to: address)
```

### `onWrite`

```csharp
trigger onWrite(from: address, data: any)
```

## Practical notes

- `onAttach` is for token-backed contract attachment flows.
- `onUpgrade` is the lifecycle hook for later code updates.
- Token-backed contracts should not assume every compiler-accepted trigger is available in every old network snapshot. Validate against the target chain.
- For current attach/create flows, token-backed contracts must satisfy validator-side token admission rules such as the required `onMint` surface.
