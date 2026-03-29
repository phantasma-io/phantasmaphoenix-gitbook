# Opcodes

This page documents the current Phantasma VM opcode set used by the Carbon validator.

## Gas Cost Model

The VM assigns a small base gas cost per opcode before any interop-side native work is considered.

The current base costs are:

- `0`
  - `NOP`, `RET`
- `1`
  - most ordinary opcodes
- `5`
  - `CALL`, `LOAD`, `PUT`, `GET`
- `10`
  - `EXTCALL`, `CTX`
- `100`
  - `SWITCH`

## Full Opcode Table

| Opcode | Args | Purpose | Base Gas |
| --- | --- | --- | ---: |
| `NOP` | - | Do nothing. | `0` |
| `MOVE` | `src, dst` | Move a register value by reference semantics. | `1` |
| `COPY` | `src, dst` | Copy a register value by value semantics. | `1` |
| `PUSH` | `src` | Push a register value onto the shared stack. | `1` |
| `POP` | `dst` | Pop the top stack value into a register. | `1` |
| `SWAP` | `a, b` | Swap two register values. | `1` |
| `CALL` | `count, offset` | Enter a new execution frame and jump to an offset. | `5` |
| `EXTCALL` | `reg` | Execute a native interop method named by the register value. | `10` |
| `JMP` | `offset` | Unconditional jump. | `1` |
| `JMPIF` | `offset, reg` | Jump if the register evaluates to true. | `1` |
| `JMPNOT` | `offset, reg` | Jump if the register evaluates to false. | `1` |
| `RET` | - | Return from the current frame or context. | `0` |
| `THROW` | `reg` | Abort execution with a VM exception. | `1` |
| `LOAD` | `dst, type, data` | Load an immediate typed value into a register. | `5` |
| `CAST` | `src, dst, type` | Convert a value into another VM type. | `1` |
| `CAT` | `a, b, dst` | Concatenate values into a result. | `1` |
| `RANGE` | `src, dst, index, length` | Extract a slice from a value. | `1` |
| `LEFT` | `src, dst, length` | Extract the left-most portion of a value. | `1` |
| `RIGHT` | `src, dst, length` | Extract the right-most portion of a value. | `1` |
| `SIZE` | `src, dst` | Return the serialized RAM size of a value. | `1` |
| `COUNT` | `src, dst` | Return the number of elements in a struct-like value. | `1` |
| `NOT` | `src, dst` | Boolean negation. | `1` |
| `AND` | `a, b, dst` | Boolean or bitwise AND depending on value shape. | `1` |
| `OR` | `a, b, dst` | Boolean or bitwise OR depending on value shape. | `1` |
| `XOR` | `a, b, dst` | Boolean or bitwise XOR depending on value shape. | `1` |
| `EQUAL` | `a, b, dst` | Equality comparison. | `1` |
| `LT` | `a, b, dst` | Less-than comparison. | `1` |
| `GT` | `a, b, dst` | Greater-than comparison. | `1` |
| `LTE` | `a, b, dst` | Less-than-or-equal comparison. | `1` |
| `GTE` | `a, b, dst` | Greater-than-or-equal comparison. | `1` |
| `INC` | `reg` | Increment a numeric value. | `1` |
| `DEC` | `reg` | Decrement a numeric value. | `1` |
| `SIGN` | `src, dst` | Return the sign of a numeric value. | `1` |
| `NEGATE` | `src, dst` | Negate a numeric value. | `1` |
| `ABS` | `src, dst` | Return absolute value. | `1` |
| `ADD` | `a, b, dst` | Addition. | `1` |
| `SUB` | `a, b, dst` | Subtraction. | `1` |
| `MUL` | `a, b, dst` | Multiplication. | `1` |
| `DIV` | `a, b, dst` | Division. | `1` |
| `MOD` | `a, b, dst` | Modulo. | `1` |
| `SHL` | `a, b, dst` | Shift left. | `1` |
| `SHR` | `a, b, dst` | Shift right. | `1` |
| `MIN` | `a, b, dst` | Return the smaller value. | `1` |
| `MAX` | `a, b, dst` | Return the larger value. | `1` |
| `POW` | `a, b, dst` | Exponentiation. | `1` |
| `CTX` | `src, dst` | Resolve a named execution context. | `10` |
| `SWITCH` | `reg` | Switch execution into a resolved context. | `100` |
| `PUT` | `value, target, field` | Write a field into a struct-like target. | `5` |
| `GET` | `dst, target, field` | Read a field from a struct-like target. | `5` |
| `CLEAR` | `reg` | Reset a register to `None`. | `1` |
| `UNPACK` | `src, dst` | Decode a serialized struct-like value. | `1` |
| `PACK` | - | Reserved; currently unused. | `1` |
| `DEBUG` | - | Debug breakpoint opcode. In code this is stored as `DEBUG_`. | `1` |

## Notes For Contract Authors

- `EXTCALL` is how VM code reaches native chain functionality such as token transfers, storage helpers, and contract lifecycle operations.
- `CTX` and `SWITCH` are what make cross-context contract calls and trigger execution possible.
- `PACK` is still effectively unused in the current implementation.
- The base opcode gas above is only part of the final transaction cost. Heavy interops can add much larger native gas charges.
