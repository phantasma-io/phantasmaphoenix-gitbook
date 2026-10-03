# Phantasma SDKs

Phantasma SDKs provide language-specific APIs for RPC calls, key handling,
transaction signing, VM script construction, and Carbon workflows.

## Script Builder

Every SDK has a `ScriptBuilder` for VM scripts: contract calls, interop calls,
gas, transfers, staking and NFT operations. The C# methods are documented
under Script Builder; the other SDKs document theirs on their VM pages.

{% content-ref url="/developers/script-builder" %}
Script builder
{% endcontent-ref %}

## External Calls

External calls, also called interop calls, are VM calls into chain runtime
functionality. Use the External Calls reference when a script needs runtime data
or chain operations exposed outside a contract API.

{% content-ref url="/developers/script-builder/external-calls.md" %}
External Calls
{% endcontent-ref %}

## Fees Under Gas Model v2

The chain bills every byte a transaction puts in the block, and it escrows SOUL
for every storage quantum the transaction adds. A Carbon message therefore
carries a gas offer and a storage ceiling, and both have to be set before it is
signed. A message signed with a zero offer is never admitted. [Fees And
Gas](/developers/blockchain/chain/fees-and-gas.md) describes the rules the
chain applies.

Every SDK computes both from the message itself and from the chain's own gas
configuration. Builders carry no prices. The flow is the same in each language:
build the message, plan it, sign it, send it. Each SDK also has one call that
does all four.

Each SDK documents this on its own fees page:

| SDK | Page |
| --- | ---- |
| TypeScript | [Fees And Broadcasting](/developers/sdks/ts/fees-and-broadcasting.md) |
| C# | [Fees And Broadcasting](/developers/sdks/csharp/fees-and-broadcasting.md) |
| Unity | [Carbon Transactions And Fees](/developers/sdks/unity/carbon-transactions.md) |
| Go | [Fees And Broadcasting](/developers/sdks/go/fees-and-broadcasting.md) |
| Python | [Fees And Broadcasting](/developers/sdks/python/fees-and-broadcasting.md) |
| Rust | [Fees And Broadcasting](/developers/sdks/rust/fees-and-broadcasting.md) |
| C++ | [Fees And Broadcasting](/developers/sdks/cpp/fees-and-broadcasting.md) |

## Supported Languages

* C#
* C++
* Go
* Python
* Rust
* TypeScript (usable from JavaScript)

## C# SDK / Godot Engine

The C# SDK is a set of .NET libraries with no engine dependency; a Godot project in C# uses it like any other package.

{% content-ref url="/developers/sdks/csharp/" %}
C# SDK
{% endcontent-ref %}

## TypeScript / JavaScript SDK

{% content-ref url="/developers/sdks/ts/" %}
TypeScript
{% endcontent-ref %}

## Go SDK

{% content-ref url="/developers/sdks/go/" %}
Go
{% endcontent-ref %}

## Python SDK

{% content-ref url="/developers/sdks/python/" %}
Python
{% endcontent-ref %}

## Rust SDK

{% content-ref url="/developers/sdks/rust/" %}
Rust
{% endcontent-ref %}

## Unity SDK / Unity Engine

{% content-ref url="/developers/sdks/unity/" %}
Unity SDK
{% endcontent-ref %}

## C++ / Unreal Engine

The C++ SDK is a header-only library with no engine dependency; an Unreal Engine project includes it with its own JSON, HTTP and crypto adapters.

{% content-ref url="/developers/sdks/cpp/" %}
C++
{% endcontent-ref %}
