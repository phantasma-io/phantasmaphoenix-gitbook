---
title: "Our Features"
weight: 10
---

## Carbon native assets

Carbon is the native asset runtime for tokens and NFTs on Phantasma Phoenix. Asset operations (create, mint, transfer, burn) are built into the chain, so standard token and NFT flows do not require custom smart contracts or VM execution. Metadata is schema-validated by the chain. See the full overview: [Carbon: Native Assets on Phantasma Phoenix](carbon.md).

## SmartNFTs (dynamic NFTs)

SmartNFTs extend Carbon with VM-driven logic for NFTs that can evolve and update their content based on defined rules. A SmartNFT token is backed by a VM contract: the contract is installed when the token is created or attached to an existing token later, and it can be upgraded.

## NFT addresses and infusion

Each NFT has its own address, derived from its token id and instance id. Assets sent to that address become attached to the NFT, enabling nested ownership. Sending assets to an NFT address, and moving them out of it, needs the signature of the NFT's owner. Infusion works for every NFT, SmartNFTs included.

## Dual Token Economy

_Govern with SOUL - Fuel your experience with KCAL_

SOUL and KCAL work together in the Phantasma economy.

**SOUL**

- Core token used for staking and governance.
- Staked SOUL earns KCAL, which the staker claims.

**KCAL**

- Fuel token used for transaction fees and on-chain operations.

## Carbon-negative footprint

Phantasma is the first certified carbon-negative blockchain.

## Wallet connectivity

Phantasma Link connects dApps to wallets for signing transactions and interacting with the chain.

## Tools and SDKs

Use the Token Deployment UI for token and NFT workflows and contract lifecycle actions: [Token Deployment UI](token-deployment-ui.md). Developers can also build directly with the C#, Unity, TypeScript/JavaScript, Go, Python, Rust, and C++ SDKs, or use `pha-deploy` for repeatable CLI workflows.

## On-chain storage

Contracts keep their own data on chain. The fee payer of the transaction that writes the data escrows SOUL for it, and a transaction that removes the data receives the escrow back. See [Storage And Data Escrow](developers/blockchain/smart-contracts/storage-and-data-escrow.md).
