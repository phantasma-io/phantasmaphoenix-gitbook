# ✨ Features

## Supported Languages

TOMB generates code that runs in the PhantasmaVM, and supports multiple programming languages.

| Language  | File Extension | Status                                | Description                                                                        |
| --------- | -------------- | ------------------------------------- | ---------------------------------------------------------------------------------- |
| TOMB lang | .tomb          | Fully working                         | The original language supported by TOMB (the rest of this document samples use it) |

## Supported Features

* Smart contracts and Non-contract Scripts (eg: transactions, raw invokes)
* Numbers, strings ([Example](https://docs.phantasma.io/#tomb-example_strings)), bools, timestamps, addresses, hashes and decimals ([Example](https://docs.phantasma.io/#tomb-example_decimals))
* Constants
* Enums ([Example](https://docs.phantasma.io/#tomb-example_enums))
* Global and local variables ([Example](https://docs.phantasma.io/#tomb-example_simple_counter))
* Array indexing ([Example](https://docs.phantasma.io/#tomb-example_string_manipulation))
* Bitshifting and logical operators
* Contract constructors, methods and triggers
* Contract public methods ([Example](https://docs.phantasma.io/#tomb-example_simple_sum))
* Return values
* Collections (Maps ([Example](https://docs.phantasma.io/#tomb-example_map)) and lists)
* Generic types
* If ... Else ([Example](https://docs.phantasma.io/#tomb-example_conditions))
* While ... and Do ... While loops
* Switch .. case ([Example](https://docs.phantasma.io/#tomb-example_switch_case))
* Break and Continue
* Throw Exceptions
* Uninitialized globals validation
* Custom events
* Interop and Contract calls
* Inline asm
* Structs
* Import libraries (Runtime, Leaderboard, Token, etc)
* Comments (single and multi line)
* Contract tasks
* ABI generation

## Planned Features

Some of the planned features:

* Try .. Catch
* More...
* Warnings
* Debugger support

## Feature requests

Feature's requested from the Community

* Call a function from anywhere in the code
* Create Classes that can be manipulated
* Change Struct values of an instanciated struct without needing to recreated
* Add && and || (currently its or, and)
* Better support for Arrays, methods like, Array.shuffle() | Array.push() | Array.add() | Array.pop() | Array.shift()
* Better Math Library, implement methods like, Math.Ceil() | Math.floor()
* Multiple file support (Before compiling it, to make the code easier to write.)
* Implement a null types
