---
title: "C++ SDK API Overview"
linkTitle: "API Overview"
weight: 110
---

The header groups of the C++ SDK and their main types. The reference pages list
every method, result field, wire structure and helper.

- [C++ SDK Complete API Reference](reference/_index.md)

## RPC

| API | Purpose |
| --- | ------- |
| `rpc::PhantasmaAPI` (`PhantasmaAPI.h`) | Typed RPC calls through an adapter's `HttpClient`, which takes the node's base URL. Each method fills an optional `PhantasmaError`. |
| `rpc::PhantasmaJsonAPI` | `Make...Request` and `Parse...Response` pairs for an application that owns its transport. |
| `Adapters/*` | RapidJSON and libcurl, or CppRestSDK, for JSON and HTTP; OpenSSL for the cryptography. |

Details: [RPC Client](reference/rpc-methods.md), [RPC Result Models](reference/rpc-models.md).

## Keys, Addresses And Hashes

| API | Purpose |
| --- | ------- |
| `PhantasmaKeys` | Ed25519 key pair: generation, WIF, address, signing. |
| `Address` | Text and byte forms, kinds, system addresses from names. |
| `Ed25519Signature`, `Hash`, `PrivateKey` | Signatures, hashes, the guarded private key. |

Details: [Keys And Addresses](keys-and-addresses.md).

## VM And Script Transactions

| API | Purpose |
| --- | ------- |
| `ScriptBuilder` (`VM/ScriptBuilder.h`) | VM bytecode: contract and interop calls, gas, transfers, staking, low-level emitters. |
| `Transaction` (`Blockchain/Transaction.h`) | The script transaction: signing, serialization, proof of work. |
| `VMObject` (`VM/VMObject.h`) | VM values, such as the results of a read-only script. |
| `Utils/RpcUtils.h` | `SignAndSendTransaction`, `DefaultScriptExpiration`, the confirmation helpers. |

Details: [VM And Transactions](vm-and-transactions.md), [VM and Transaction APIs](reference/vm-transaction-binary.md).

## Carbon

| API | Purpose |
| --- | ------- |
| `NativeTxHelper` | Transfers, mints and burns without a script. |
| `CreateTokenTxHelper`, `CreateTokenSeriesTxHelper`, `MintPhantasmaNonFungibleTxHelper` | Token, series and NFT mint messages, and the parsers of their results. |
| `TokenInfoBuilder`, `TokenMetadataBuilder`, `TokenSchemasBuilder`, `SeriesInfoBuilder`, `TokenSeriesMetadataBuilder`, `PhantasmaNftRomBuilder` | Token, schema, series and ROM data. |
| `PlanFees`, `ChainFeePlanner`, `SummarizeFeePlan`, `TxLimits`, `ExpiryWithin` | Fee planning and lifetimes. |
| `TxMsgSigner`, `SignAndSerialize`, `ParseTx`, `ParseSignedTx` | Signing and reading messages. |
| `PreflightTransaction`, `SendTransaction` | The symbol check, and build, plan, check, sign and send in one call. |

Details: [Carbon](carbon.md), [Carbon Operations](carbon-operations.md), [Carbon API and Wire Format](reference/carbon-wire.md).

## Fees

Under gas model v2 the chain bills every byte a transaction puts in the block
and escrows SOUL for new storage. Builders carry no prices, so a message is
planned before it is signed.

- [Fees And Broadcasting](fees-and-broadcasting.md)
