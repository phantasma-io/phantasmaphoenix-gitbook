---
description: Carbon is the native asset runtime for tokens and NFTs on Phantasma Phoenix.
---

# Carbon: Native Assets on Phantasma Phoenix

Carbon is the native asset layer for Phantasma Phoenix. It defines how tokens and NFTs are created, stored, and transferred directly by the chain.

All Phantasma Phoenix tokens are built on Carbon at their core. Carbon tokens do not require smart contracts: their metadata lives in schema-defined hierarchical structures, and the chain manages these assets through low-level Carbon methods built for speed and efficiency. Manipulating Carbon tokens requires no VM execution or scripting.

For more advanced scenarios, Phantasma Phoenix also provides SmartNFTs with attached smart contracts. Both Carbon NFTs and SmartNFTs support infusion and the full set of NFT operations (mint, transfer, burn, trade). A Carbon NFT can be upgraded to a SmartNFT by embedding a TOMB (PhantasmaVM) contract in its Carbon metadata, enabling NFTs that evolve and update their content based on defined rules.

Below is a quick look at what makes Carbon different and how the 4th-generation asset model works.

## What makes Carbon different

- **Native asset operations**: Creating, minting, transferring, and burning assets are built-in chain operations, so you do not deploy a custom smart contract just to define a token.
- **Schema-validated metadata**: NFT metadata is structured and validated by the chain using schemas.
- **NFT addresses and infusion**: Each NFT has its own Carbon address derived from its token id and instance id. Assets sent to that address become attached to the NFT (nested ownership).

## 4th-generation asset model

In Carbon, asset rules live in the protocol itself. Tokens and NFTs are native chain entities, and their operations are handled by built-in runtime methods.

Here is a high-level comparison between a contract-based asset model and Carbon's native model:

| Aspect | Contract-based asset model | Carbon native asset model |
| --- | --- | --- |
| Execution model | Asset logic runs inside a smart contract | Asset logic is a built-in chain runtime operation |
| Asset definition | Tokens/NFTs are defined by contract code | Tokens/NFTs are protocol primitives |
| Deployment step | Requires contract deployment before assets exist | No asset contract deployment; tokens are created by Carbon transactions |
| Execution path | User-defined bytecode runs in a VM | No user bytecode for asset operations (native runtime calls) |
| Metadata structure | Metadata rules are defined by the contract | Metadata is schema-based (series, ROM, RAM) and validated by the chain |
| Ownership model | Ownership is stored as contract state (tokenId -> owner) | Each NFT has its own Carbon address; assets can be attached by sending to that address |
| Performance under load | VM overhead; latency depends on execution logic | Native runtime operations with minimal latency and high throughput |
| Tooling flow | Deploy a contract, then call its methods | Build a Carbon transaction and sign it with a wallet |

## Core concepts

- **Token vs NFT**: Fungible tokens represent balances; NFTs represent individual items.
- **Series metadata (shared)**: Information shared across a collection.
- **ROM (immutable)**: Per-item fields that never change after minting.
- **RAM (mutable)**: Optional per-item fields that can be updated later.
- **Infusion**: Sending assets to an NFT's address to attach them to the NFT.

## How to use Carbon

- Use the Token Deployment UI to deploy tokens, create NFT series, mint NFTs, and infuse NFTs without writing code.
- Start with the short, user-friendly guide: [Token Deployment UI](/about/token-deployment-ui.md).
- Connect a wallet that supports signing Carbon transactions.
- For advanced workflows, the SDKs let you build and sign Carbon transactions directly.

## Want the developer details?

- [Token Deployment UI guide](/developers/token-deployment-frontend.md)
- [Carbon workflows (TypeScript SDK)](/developers/sdks/ts/carbon-workflows.md)
- [Create Carbon token / series / mint examples](/developers/sdks/ts/backend/backend.md)
