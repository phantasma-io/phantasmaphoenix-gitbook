---
title: "Carbon: Native Assets on Phantasma Phoenix"
linkTitle: "Carbon"
weight: 20
description: "Carbon is the native asset runtime for tokens and NFTs on Phantasma Phoenix."
---

Carbon is the native asset layer for Phantasma Phoenix. It defines how tokens and NFTs are created, stored, and transferred directly by the chain.

Every token on Phantasma Phoenix is a native asset of the chain. Standard asset operations such as token creation, series creation, minting, transfer, burn, and infusion are handled directly by the chain instead of requiring a custom contract for every asset.

For advanced behavior, a token can also be backed by VM code. In practice this means:
- a new token-backed contract can be installed during token creation
- VM code can be attached later to an already existing token
- the attached or created token-backed contract can then be upgraded later

This is different from a standalone custom contract. Token symbols and standalone custom contract names are separate flows.

Below is a quick look at what makes Carbon different and how the 4th-generation asset model works.

## What makes Carbon different

- **Native asset operations**: Creating, minting, transferring, burning, and creating NFT series are built-in chain operations, so you do not deploy a custom smart contract just to define an asset.
- **Schema-validated metadata**: NFT metadata is structured and validated by the chain using schemas.
- **NFT addresses and infusion**: Each NFT has its own address, derived from its token id and instance id. Assets sent to that address become attached to the NFT (nested ownership). Sending assets to an NFT address, and moving them out of it, needs the signature of the NFT's owner.
- **Optional token-backed VM layer**: Advanced tokens can have VM logic attached without changing the fact that the token itself is still a native asset.

## 4th-generation asset model

In Carbon, asset rules live in the protocol itself. Tokens and NFTs are native chain entities, and their operations are handled by built-in runtime methods.

Here is a high-level comparison between a contract-based asset model and Carbon's native model:

| Aspect | Contract-based asset model | Carbon native asset model |
| --- | --- | --- |
| Execution model | Asset logic runs inside a smart contract | Asset logic is a built-in chain runtime operation |
| Asset definition | Tokens/NFTs are defined by contract code | Tokens/NFTs are protocol primitives |
| Deployment step | Requires contract deployment before assets exist | Tokens are created by native transactions; optional VM logic can be added through token-backed flows |
| Execution path | User-defined bytecode runs in a VM | Native asset operations stay native; optional token-backed hooks run in VM when present |
| Metadata structure | Metadata rules are defined by the contract | Metadata is schema-based (series, ROM, RAM) and validated by the chain |
| Ownership model | Ownership is stored as contract state (tokenId -> owner) | The chain records the owner of each NFT; each NFT also has its own address, and assets sent to it are attached to the NFT |
| Performance under load | VM overhead; latency depends on execution logic | Native runtime operations with minimal latency and high throughput |
| Tooling flow | Deploy a contract, then call its methods | Build a transaction and sign it with a wallet |

## Core concepts

- **Token vs NFT**: Fungible tokens represent balances; NFTs represent individual items.
- **Series metadata (shared)**: Information shared across a collection.
- **ROM (immutable)**: Per-item fields that never change after minting.
- **RAM (mutable)**: Optional per-item fields that can be updated later.
- **Infusion**: Sending assets to an NFT's address to attach them to the NFT. The NFT's owner signs the transfer.
- **Token-backed contract**: Optional VM code bound to a token symbol for advanced lifecycle behavior.

## How to use Carbon

- Use the Token Deployment UI to deploy tokens, attach token-backed VM contracts, create NFT series, mint NFTs, and infuse NFTs without writing code.
- Start with the short guide: [Token Deployment UI](token-deployment-ui.md).
- Connect a Phantasma Link wallet, such as Poltergeist Lite.
- For advanced workflows, the SDKs let you build and sign transactions directly, and VM tooling lets you compile and deploy contract bundles where needed.

## Want the developer details?

- [Token Deployment UI guide](developers/token-deployment-frontend.md)
- [Carbon workflows (TypeScript SDK)](developers/sdks/ts/carbon-workflows.md)
- [Create Carbon token / series / mint examples](developers/sdks/ts/backend/_index.md)
- [SDKs](developers/sdks/_index.md)
