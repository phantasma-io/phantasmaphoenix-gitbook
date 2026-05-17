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
| `Carbon/Tx.h` | Fee options, create-token, create-series, NFT mint builders, result parsers, and signing. |

## Lifecycle Builders

| Builder | Purpose |
| ------- | ------- |
| `CreateTokenTxHelper::BuildTx` | Build unsigned create-token `TxEnvelope`. |
| `CreateTokenSeriesTxHelper::BuildTx` | Build unsigned create-series `TxEnvelope`. |
| `MintNonFungibleTxHelper::BuildTx` | Build a direct one-NFT Carbon mint envelope. |
| `MintPhantasmaNonFungibleTxHelper::BuildTx` | Build one or more deterministic Phantasma NFT mint records. |
| `SignAndSerialize(env, keys)` | Sign and serialize a `TxEnvelope`. |

`TxEnvelope::View()` returns the underlying Carbon `TxMsg`; `buffers` owns
serialized payload storage referenced by message views.

## Result Parsers

| Parser | Returns |
| ------ | ------- |
| `CreateTokenTxHelper::ParseResult(resultHex)` | Created Carbon token id. |
| `CreateTokenSeriesTxHelper::ParseResult(resultHex)` | Created Carbon series id. |
| `MintNonFungibleTxHelper::ParseResult(carbonTokenId, resultHex)` | Carbon NFT addresses derived from instance ids. |
| `MintPhantasmaNonFungibleTxHelper::ParseResult(resultHex)` | Phantasma NFT id and Carbon instance id rows. |

Parse only after the submitted transaction is confirmed successful.
