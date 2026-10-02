# Features

## Supported Languages

`pha-tomb` compiles one source language:

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

- `nativecheck` checks native-contract and interop calls against the chain snapshot pinned in the compiler. `nativecheck:error` fails the build on a call the chain rejects.
- The [Libraries](libraries.md) page lists the methods that run on the current chain; a compiler library method that is not listed there is rejected by the validator at run time.

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
