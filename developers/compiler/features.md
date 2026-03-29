# Features

## Supported Languages

`pha-tomb` currently documents one source language for contract authoring:

| Language  | File Extension | Status                                | Description                                                                                               |
| --------- | -------------- | ------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| TOMB      | .tomb          | Current compiler surface              | The current Phantasma smart-contract source language used by `pha-tomb`. |

## Supported Features

- smart contracts and non-contract scripts
- numbers, strings, bools, timestamps, addresses, hashes, byte arrays
- constants, enums, structs
- global and local variables
- contract methods, constructors, triggers, events, properties
- nested NFT submodules inside token modules
- arrays, maps, lists, generic types
- `if`, `while`, `do/while`, `for`, `switch`, `break`, `continue`
- exceptions via `throw`
- inline assembly
- interop calls and contract calls
- ABI generation
- debug artifact generation

## Important caveats

- `Task` syntax is parsed by the compiler, but the current chain runtime does not expose the full `Task.*` interop surface needed to rely on it in production.
- `nativecheck` validates against the compiler's pinned Carbon snapshots. Treat warnings and errors there as signal, not noise.
- Not every compiler-accepted native call is necessarily available on every chain baseline. Always test against the target network.
- Some helper libraries still have unsupported methods that compile to explicit runtime failure.

## Generated artifacts

Depending on module type and flags, `pha-tomb` can emit:

- `.pvm`
- `.abi`
- `.debug`
- `.asm`
- `.pvm.hex`
- `.abi.hex`
- `.tx` / `.tx.hex` for script modules

For the current CLI shape and output rules, see [Setup](setup.md) and [pha-deploy](../tools/pha-deploy.md).
