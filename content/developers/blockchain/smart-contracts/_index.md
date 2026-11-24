---
title: "Smart Contracts"
weight: 10
---

Phantasma supports VM smart contracts. In the current toolchain, contracts are authored in TOMB source files and compiled with `pha-tomb`.

Smart-contract workflows fall into two broad groups:
- standalone custom contracts
- token-backed contracts bound to an uppercase token symbol

- [TOMB Compiler](../../compiler/_index.md)

## Deployment flows

- standalone lowercase custom contract -> deploy with `contract deploy`
- new uppercase token-backed contract -> create with `--create-token`
- existing token + new VM code -> `contract attach`
- later contract code update -> `contract upgrade`

For the current deployment tooling:

- [pha-deploy](../../tools/pha-deploy.md)

For the deployment flow overview:

- [How to Deploy](how-to-deploy.md)

For contract storage costs and SOUL data escrow:

- [Storage And Data Escrow](storage-and-data-escrow.md)
