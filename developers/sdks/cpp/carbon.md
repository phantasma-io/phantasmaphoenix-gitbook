# C++ SDK Carbon

The C++ Carbon headers implement Carbon serialization, token and schema
structures, transaction message builders, signing, and result parsers.

## Header Groups

| Header | Contents |
| ------ | -------- |
| `Carbon/Carbon.h` | Core read/write helpers and Carbon serialization primitives. |
| `Carbon/DataCommon.h`, `Carbon/DataBlockchain.h`, `Carbon/DataVm.h` | Wire structs used by Carbon messages and VM metadata. |
| `Carbon/Contracts/Token.h` | Token info, series info, NFT state/import structures, metadata builders, and token schema helpers. |
| `Carbon/Contracts/TokenSchemas.h` | Schema field helpers and standard NFT schema construction. |
| `Carbon/Tx.h` | Transaction limits, native builders, create-token, create-series, NFT mint builders, result parsers, and signing. |
| `Carbon/FeePlan.h`, `Carbon/FeePlanSummary.h` | Fee planning from the message, and the decimal rendering of a plan. |
| `Carbon/ChainFeePlan.h` | The planner that holds the chain's gas config and prices messages against it. |
| `Carbon/FeeInfusions.h` | Reads what a burned NFT holds, which a burn plan requires. |
| `Carbon/Preflight.h` | The symbol check a token creation runs before it is signed. |
| `Carbon/Send.h` | Build, plan, check, sign and send in one call. |

## Lifecycle Builders

| Builder | Purpose |
| ------- | ------- |
| `NativeTxHelper::TransferFungible` | Build a native fungible transfer, in the plain or the gas-payer form. |
| `NativeTxHelper::TransferNonFungible` | Build a native NFT transfer of one or more instances. |
| `CreateTokenTxHelper::BuildTx` | Build unsigned create-token `TxEnvelope`. |
| `CreateTokenSeriesTxHelper::BuildTx` | Build unsigned create-series `TxEnvelope`. |
| `MintNonFungibleTxHelper::BuildTx` | Build a direct one-NFT Carbon mint envelope. |
| `MintPhantasmaNonFungibleTxHelper::BuildTx` | Build one or more deterministic Phantasma NFT mint records. |
| `SignAndSerialize(env, keys)` | Sign and serialize a `TxEnvelope`. |

`TxEnvelope::View()` returns the underlying Carbon `TxMsg`; `buffers` owns
serialized payload storage referenced by message views.

The builders carry no prices. A message leaves a builder with `maxGas` at `0`,
and it is planned before it is signed.

{% content-ref url="/developers/sdks/cpp/fees-and-broadcasting.md" %}
[Fees And Broadcasting](/developers/sdks/cpp/fees-and-broadcasting.md)
{% endcontent-ref %}

## Result Parsers

| Parser | Returns |
| ------ | ------- |
| `CreateTokenTxHelper::ParseResult(resultHex)` | Created Carbon token id. |
| `CreateTokenSeriesTxHelper::ParseResult(resultHex)` | Created Carbon series id. |
| `MintNonFungibleTxHelper::ParseResult(carbonTokenId, resultHex)` | Carbon NFT addresses derived from instance ids. |
| `MintPhantasmaNonFungibleTxHelper::ParseResult(resultHex)` | Phantasma NFT id and Carbon instance id rows. |

Parse only after the submitted transaction is confirmed successful.

## Reading A Message Back

`Blockchain::ParseTx` and `Blockchain::ParseSignedTx` read a Carbon message the
way the chain reads it. A truncated message is refused rather than read as a
shorter one. See
[Fees And Broadcasting](/developers/sdks/cpp/fees-and-broadcasting.md).
