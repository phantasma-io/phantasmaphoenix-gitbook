---
title: "Phantasma SDKs"
linkTitle: "SDKs"
weight: 100
---

Phantasma SDKs provide language-specific APIs for RPC calls, key handling,
transaction signing, VM script construction, and Carbon workflows.

## Script Builder

Every SDK has a `ScriptBuilder` for VM scripts: contract calls, interop calls,
gas, transfers, staking and NFT operations. The C# methods are documented
under Script Builder; the other SDKs document theirs on their VM pages.

- [Script builder](../script-builder/_index.md)

## External Calls

External calls, also called interop calls, are VM calls into chain runtime
functionality. Use the External Calls reference when a script needs runtime data
or chain operations exposed outside a contract API.

- [External Calls](../script-builder/external-calls.md)

## Fees Under Gas Model v2

The chain bills every byte a transaction puts in the block, and it escrows SOUL
for every storage quantum the transaction adds. A Carbon message therefore
carries a gas offer and a storage ceiling, and both have to be set before it is
signed. A message signed with a zero offer is never admitted. [Fees And
Gas](../blockchain/chain/fees-and-gas.md) describes the rules the
chain applies.

Every SDK computes both from the message itself and from the chain's own gas
configuration. Builders carry no prices. The flow is the same in each language:
build the message, plan it, sign it, send it. Each SDK also has one call that
does all four.

Each SDK documents this on its own fees page:

| SDK | Page |
| --- | ---- |
| TypeScript | [Fees And Broadcasting](ts/fees-and-broadcasting.md) |
| C# | [Fees And Broadcasting](csharp/fees-and-broadcasting.md) |
| Unity | [Carbon Transactions And Fees](unity/carbon-transactions.md) |
| Go | [Fees And Broadcasting](go/fees-and-broadcasting.md) |
| Python | [Fees And Broadcasting](python/fees-and-broadcasting.md) |
| Rust | [Fees And Broadcasting](rust/fees-and-broadcasting.md) |
| C++ | [Fees And Broadcasting](cpp/fees-and-broadcasting.md) |

## Supported Languages

* C#
* C++
* Go
* Python
* Rust
* TypeScript (usable from JavaScript)

## C# SDK / Godot Engine

The C# SDK is a set of .NET libraries with no engine dependency; a Godot project in C# uses it like any other package.

- [C# SDK](csharp/_index.md)

## TypeScript / JavaScript SDK

- [TypeScript](ts/_index.md)

## Go SDK

- [Go](go/_index.md)

## Python SDK

- [Python](python/_index.md)

## Rust SDK

- [Rust](rust/_index.md)

## Unity SDK / Unity Engine

- [Unity SDK](unity/_index.md)

## C++ / Unreal Engine

The C++ SDK is a header-only library with no engine dependency; an Unreal Engine project includes it with its own JSON, HTTP and crypto adapters.

- [C++](cpp/_index.md)
