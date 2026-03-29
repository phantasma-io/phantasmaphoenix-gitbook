---
description: TOMB smart-contract compiler for the current Phantasma VM.
cover: .gitbook/assets/gitbook-banner-pha-phoenix-phoenix-compiler.png
coverY: 0
---

# TOMB Compiler

## Description <a href="#description" id="description"></a>

The current Phantasma smart-contract compiler is `pha-tomb`.

Use it to compile `.tomb` source files into:
- `.pvm` VM bytecode
- `.abi` interface metadata
- optional debug and assembly artifacts

`pha-tomb` targets the current Phantasma VM and is the compiler used by the current contract lifecycle tooling.

## What you can build

- standalone custom VM contracts
- token-backed contracts
- NFT submodules inside token modules
- transaction scripts
- ABI-bearing modules for deployment and tooling

## Deployment model

Compiling a contract is only the first step. After compilation, deployment depends on what you are trying to create:

- standalone custom contract -> deploy with `contract deploy`
- new token-backed contract -> create with `--create-token`
- existing token + new VM code -> attach with `contract attach`
- later code update -> `contract upgrade`

For the current deployment tooling, see:
- [pha-deploy](../tools/pha-deploy.md)
- [How to Deploy](../blockchain/smart-contracts/how-to-deploy.md)

## Want to jump right in?

Jump in to the quick start docs and get making your first smart contract:

{% content-ref url="quick-start.md" %}
Quick Start
{% endcontent-ref %}

## Want to deep dive?

Dive deeper into the language surface and standard libraries:

{% content-ref url="features.md" %}
Features
{% endcontent-ref %}
