# Architecture

The Phantasma VM is a register-based virtual machine with a shared stack and explicit execution contexts. It is the execution engine behind VM contracts, VM token triggers, and raw script execution.

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
- `Runtime.Notify(...)` and `Runtime.NotifyV2(...)` also require a real contract context because emitted events need a concrete contract name

## Interop Boundary

The VM does not implement token, NFT, governance, or storage logic directly in bytecode. Scripts cross that boundary through `EXTCALL` and a method name such as:

- `Runtime.TransferTokens`
- `Runtime.MintToken`
- `Nexus.CreateToken`
- `Data.Get`
- `Map.Set`

Each interop is dispatched inside the validator's native runtime. That is where witness checks, policy rules, token metadata validation, proof-of-work requirements, and storage writes actually happen.

## Gas Model

A script pays gas units for:

1. Every instruction it executes: a flat cost per opcode, listed in the opcode table.
2. The size of its work: data that instructions copy or concatenate, struct reads and writes, call frames, and arithmetic on large numbers.
3. Every interop call: a cost from the Phantasma VM configuration, `gasStandard` for most interops and `gasNexus`, `gasOrganization`, `gasAccount`, `gasOracle`, or `gasConstructor` for some, plus the native work the interop performs, such as token fees.

The chain converts gas units to KCAL and adds the block data of the transaction. [Fees And Gas](/developers/blockchain/chain/fees-and-gas.md) gives the formulas and the full work table. The `getPhantasmaVmConfig` RPC method returns the interop costs.

For contract lifecycle flows, native work dominates the total cost. `Runtime.DeployContract`, `Runtime.UpgradeContract`, `Nexus.CreateToken`, and `Nexus.AttachTokenContract` are not cheap operations.

## Proof Of Work Gates

Some interops require at least minimal proof of work on the transaction before the validator will execute them:

- `Runtime.DeployContract`
- `Runtime.UpgradeContract`
- `Nexus.CreateToken`
- `Nexus.AttachTokenContract`

If the transaction does not meet the minimum difficulty, execution fails before the lifecycle operation is allowed.

## Trigger Execution

Token-backed contracts can expose these trigger methods:

- `onMint`
- `onBurn`
- `onSend`
- `onReceive`
- `onInfuse`
- `onSeries`
- `onAttach`
- `onUpgrade`
- `onWrite`

The runtime invokes them through dedicated trigger paths rather than as ordinary public methods:

- trigger guards prevent unsafe recursive trigger re-entry
- important token operations run speculatively and merge state only on success
- authorization is checked before sensitive lifecycle writes
- token-backed admission checks happen before a bad contract is accepted into token namespace

One especially important example is `onMint`: token-backed create and attach flows require it up front, because mint paths depend on it later.

## Token-Backed Contracts Versus Standalone Contracts

The VM has two contract models:

- standalone custom contracts
  - lowercase contract names
  - deployed with `Runtime.DeployContract(...)`
- token-backed contracts
  - uppercase token symbols
  - created through `Nexus.CreateToken(...)` or attached later through `Nexus.AttachTokenContract(...)`

They run on the same VM and are admitted through different rules and lifecycle paths.
