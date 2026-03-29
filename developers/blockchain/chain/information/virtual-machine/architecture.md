# Architecture

The Phantasma VM used by the current Carbon validator is a register-based virtual machine with a shared stack and explicit execution contexts. It is the execution engine behind VM contracts, VM token triggers, and raw script execution.

## Core Execution Model

At runtime, the VM works with three main pieces of state:

- registers
  - each execution frame has its own register set
- stack
  - values are pushed and popped across interop calls, context switches, and method calls
- execution contexts
  - each script or contract method runs inside a named context

The entry script starts in the synthetic `entry` context. Contract methods and triggers run in named contexts that map to deployed contract identities.

## Contexts And Contract Identity

Two VM instructions are central to multi-context execution:

- `CTX`
  - resolves a context by name
- `SWITCH`
  - transfers execution into that context

For deployed contracts, the context name is also the contract identity used by the validator when it resolves storage and ownership. The runtime treats the synthetic `entry` context specially: some interops are only valid inside a real deployed contract context and will reject calls from `entry`.

This matters for storage and events:

- `Data.Set`, `Data.Delete`, `Map.Set`, `Map.Remove`, `Map.Clear`, `List.Add`, `List.Replace`, `List.RemoveAt`, and `List.Clear` operate on the current deployed contract context
- `Runtime.Notify(...)` also requires a real contract context because emitted events need a concrete contract name

## Interop Boundary

The VM does not implement token, NFT, governance, or storage logic directly in bytecode. Scripts cross that boundary through `EXTCALL` and a method name such as:

- `Runtime.TransferTokens`
- `Runtime.MintToken`
- `Nexus.CreateToken`
- `Data.Get`
- `Map.Set`

Each interop is dispatched inside the validator's native runtime. That is where witness checks, policy rules, token metadata validation, proof-of-work requirements, and storage writes actually happen.

## Gas Model

There are two gas layers to keep in mind:

1. Opcode gas
   - every VM instruction has a small base cost
2. Interop and native work gas
   - interops consume additional configured gas buckets and may trigger much larger native charges underneath

The base opcode costs are defined in the VM opcode table. The interop buckets come from the Phantasma VM config and include categories such as:

- constructor
- standard
- account
- organization
- oracle
- nexus

For contract lifecycle flows, native work dominates the total cost. `Runtime.DeployContract`, `Runtime.UpgradeContract`, `Nexus.CreateToken`, and `Nexus.AttachTokenContract` are not cheap operations.

## Proof Of Work Gates

Some interops require at least minimal proof of work on the transaction before the validator will execute them:

- `Runtime.DeployContract`
- `Runtime.UpgradeContract`
- `Nexus.CreateToken`
- `Nexus.AttachTokenContract`

If the transaction does not meet the minimum difficulty, execution fails before the lifecycle operation is allowed.

## Trigger Execution

Token-backed contracts can expose trigger methods such as:

- `onMint`
- `onBurn`
- `onSend`
- `onReceive`
- `onSeries`
- `onAttach`
- `onUpgrade`

The runtime invokes these through dedicated trigger paths rather than treating them as ordinary public helpers. Current Carbon behavior preserves several important properties:

- trigger guards prevent unsafe recursive trigger re-entry
- important token operations run speculatively and merge state only on success
- authorization is checked before sensitive lifecycle writes
- token-backed admission checks happen before a bad contract is accepted into token namespace

One especially important example is `onMint`: token-backed create and attach flows require it up front, because mint paths depend on it later.

## Token-Backed Contracts Versus Standalone Contracts

Carbon currently supports two distinct VM contract models:

- standalone custom contracts
  - lowercase contract names
  - deployed with `Runtime.DeployContract(...)`
- token-backed contracts
  - uppercase token symbols
  - created through `Nexus.CreateToken(...)` or attached later through `Nexus.AttachTokenContract(...)`

They both run on the same VM, but they are admitted through different validator rules and lifecycle paths. That distinction is intentional and important.
