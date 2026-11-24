---
title: "Storage And Data Escrow"
weight: 20
---

This page describes smart contract storage on the current chain. The important migration point is Phoenix (Gen3) versus Gen2: storage growth is now charged to the transaction through SOUL data escrow, while Gen2 checked address-level storage allowance derived from staked SOUL.

Smart contracts can persist data through VM storage interops such as `Data.Set`, `Map.Set`, and `List.Add`. Storage growth is not funded by staking SOUL to the contract address. It is accounted by the transaction that performs the write.

KCAL is the gas token and SOUL is the data token. KCAL pays for execution and block data. SOUL is escrowed for permanent state growth from the transaction's fee payer.

<a id="contract-storage-is-not-increased-by-self-staking-soul"></a>
## Contract Storage Is Not Increased By Self-Staking SOUL

Staking SOUL to `$THIS_ADDRESS` does not increase a smart contract's storage allowance. Contract storage growth is charged to the transaction that writes it: the chain counts the 1024-byte quanta the transaction adds and escrows `dataEscrowPerRow` SOUL for each one from the transaction's fee payer. `Stake.stake($THIS_ADDRESS, amount)` is a Gen2 storage-provisioning pattern and should not be used to fund smart contract storage.

This is a deliberate architectural difference from Gen2. In Gen2, contract writes were checked against address-level available storage derived from staked SOUL. The storage cost now belongs to the transaction that creates or enlarges state, not to a stake balance attached to the contract.

## What Counts As Contract Storage

Contract storage is the persistent state written by deployed VM contracts. The common write interops are:

| Interop | Writes |
| --- | --- |
| `Data.Set` | A scalar field in the current deployed contract context. |
| `Data.Delete` | Removes a scalar field from the current deployed contract context. |
| `Map.Set` | A table entry under a field in the current deployed contract context. |
| `Map.Remove` | Removes a table entry. |
| `Map.Clear` | Removes all entries for a table field. |
| `List.Add` | Appends a list entry under a field in the current deployed contract context. |
| `List.Replace` | Replaces an existing list entry. |
| `List.RemoveAt` | Removes a list entry. |
| `List.Clear` | Removes all entries for a list field. |

Write interops operate on the current deployed contract context. Read interops can target another contract by name, but writes cannot use a contract-name argument to write arbitrary contract storage.

## Who Pays For Storage Growth

The transaction payer pays. More precisely, the chain charges the address used as the transaction's fee payer, commonly exposed by SDKs and tooling as `gasFrom` or the transaction sender.

The contract address does not need to have staked SOUL for storage writes to succeed. It also does not receive extra storage capacity if SOUL is transferred to it or staked on it. The relevant requirements are:

- the transaction must be authorized correctly
- the fee payer must hold the transaction's `maxGas` in KCAL
- the fee payer must hold enough SOUL for the data escrow
- for a Carbon message, the `maxData` ceiling must cover the storage growth

The chain reserves `maxGas` and `maxData` from the fee payer before execution and rejects the transaction when the fee payer cannot cover them: with `GasFees` for KCAL, with `DataFees` for SOUL. A transaction whose escrow would exceed its `maxData` aborts: it keeps none of its changes, ends in the state `Break`, and still pays its gas bill. A script transaction sent with `sendRawTransaction` carries no ceiling: the chain charges the escrow for the actual growth after execution, and rejects the transaction with `DataFees` when the gas payer does not hold that SOUL.

## How Data Usage Is Measured

The validator measures storage growth from the transaction's actual before/after state changes. For each charged state row:

1. The validator takes the size of the row before and after the transaction.
2. Key bytes and value bytes are counted together.
3. Each size is rounded up to whole 1024-byte quanta.
4. Only a change in the number of quanta is charged or refunded.

Creating a new row or expanding an existing row can increase data usage. Deleting a row or shrinking a row can create a data escrow refund. Rows whose size does not change do not add storage escrow, although the transaction can still pay KCAL gas for execution and block data.

Some internal chain rows are excluded from data escrow accounting. Contract authors should not rely on those exclusions for application storage; contract state written by VM storage interops is always charged.

## `maxData` And SOUL Data Escrow

`maxData` is the maximum SOUL data escrow of a Carbon message, including a script wrapped in one. It is not a byte count and it is not a contract storage quota. It is a spending limit for the message's persistent state growth. A script transaction sent with `sendRawTransaction` has no such limit; the escrow is settled from the gas payer's SOUL balance.

The effective charge is:

```text
SOUL data escrow = quantaAdded * dataEscrowPerRow
```

`dataEscrowPerRow` is the price of one 1024-byte quantum. A row of up to 1024 bytes is one quantum; a larger row, for example an NFT that carries an image, is charged for every quantum it fills.

`dataEscrowPerRow` is a governance-controlled chain parameter. Tooling and wallets should treat any fixed value as an estimate and confirm the final transaction result from the chain.

Unused prepaid data escrow is refunded. A transaction that deletes or shrinks storage receives the escrow that the released quanta paid; the refund goes to its fee payer.

## Why `Stake.stake($THIS_ADDRESS, amount)` Fails

`$THIS_ADDRESS` is a contract address. The `Stake.stake` interop uses the staking path, not the contract-storage path. That path expects address forms supported by staking and can reject a contract address with an error like:

```text
Exception: todo - non-user addresses have limited support [ctx=stake ...]
```

That error does not mean the contract is out of storage. It means the contract called an old Gen2-style self-staking pattern that is not the storage-funding mechanism.

If the purpose of the call is to provision contract storage, remove the self-staking call and make sure the fee payer of the transaction that performs the storage writes holds enough SOUL, and that a `maxData` ceiling, when the transaction carries one, covers the growth. If the purpose is not storage provisioning, review the staking flow separately; staking semantics are not a substitute for contract storage funding.

## Creating Many Pools, Maps, Or Lists

Contracts that create many pools or large collections should be designed around transaction data escrow:

- estimate how many scalar fields, map entries, list entries, and count rows the operation writes, and how many 1024-byte quanta they take
- when the transaction carries a `maxData` ceiling, set it high enough for the expected growth
- make the user or backend account that pays the fees hold enough SOUL for the data escrow
- split large initialization work across multiple transactions when one transaction would need a very large escrow
- avoid writing duplicate or unused state because every persistent row can increase data escrow
- delete obsolete rows when the contract no longer needs them; the transaction that deletes them receives the escrow they paid

For pool factories, the storage cost is part of the pool-creation transaction. It is not solved by staking SOUL on the factory contract or on each pool contract.

## Migration Notes For Gen2 Contracts

Gen2 contracts and examples may contain patterns like:

```text
Token.transfer(from, $THIS_ADDRESS, "SOUL", amount);
Stake.stake($THIS_ADDRESS, amount);
```

In Gen2, this could be used to increase the address-level storage space available to a contract. That is not the current storage funding model. Ported contracts should replace storage-provisioning self-stake flows with transaction-level fee planning:

- contract method keeps only the application logic it actually needs
- caller or backend builds the transaction with sufficient `maxGas`, and `maxData` when the transaction carries one
- wallet or tooling shows KCAL gas and SOUL data escrow before signing
- contract storage writes are allowed or rejected by the transaction result, not by contract stake balance

Do not keep `Stake.stake($THIS_ADDRESS, amount)` for storage compatibility. The call fails before the storage writes run, and staking the contract is not the storage funding path.

## Troubleshooting

| Symptom | Meaning | Fix |
| --- | --- | --- |
| `non-user addresses have limited support` from `ctx=stake` | The contract called `Stake.stake` with a contract address such as `$THIS_ADDRESS`. | Do not use self-staking to fund contract storage. The fee payer's SOUL pays for storage growth. |
| `DataFees` rejection | The fee payer does not hold the SOUL that `maxData` reserves, or, for a script transaction, the escrow charged after execution. | Make sure the fee payer holds enough SOUL. |
| The transaction ends in the state `Break` and its `debugComment` mentions `data fees` | The storage growth needs more escrow than `maxData` allows. The transaction changed nothing and paid its gas bill. | Increase `maxData`. |
| Storage write succeeds in a small test but fails when creating many entries | The larger transaction adds more storage quanta than the test transaction. | Estimate the growth of all fields and collection entries, or split the work into smaller transactions. |
| Contract has SOUL balance or stake but storage write still fails | Contract SOUL balance or stake is not the storage funding mechanism. | Fund the transaction's fee payer with SOUL, and raise `maxData` when the transaction carries it. |

## Related Pages

- [How to Deploy](how-to-deploy.md)
- [Virtual Machine Interop](../chain/information/virtual-machine/interop.md)
- [Token Deployment UI](../../token-deployment-frontend.md)
