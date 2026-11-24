---
title: "Python SDK"
weight: 50
---

![](/images/banner-pha-phoenix-python-sdk.png)

The Python SDK is a typed Python 3.11+ package for Phantasma applications and
automation. It covers JSON-RPC access, checked address and key handling, VM
script building, VM script transaction signing, and Carbon wire-format
transactions.

Package name:

```bash
pip install phantasma-sdk-py
```

Import namespace:

```python
import phantasma_py
```

The current package exposes Python-style dataclasses, exceptions, type hints,
and module names under `phantasma_py`. Older examples that import legacy modules
do not apply to this SDK.

## What It Covers

| Area | Module | Use it for |
| ---- | ------ | ---------- |
| RPC | `phantasma_py.rpc` | Calling Phantasma JSON-RPC endpoints and decoding typed result dataclasses. |
| Keys and addresses | `phantasma_py.crypto` | WIF import/export, Ed25519 signatures, address parsing, hashes. |
| VM scripts | `phantasma_py.vm` | Building scripts for contract calls, interop calls, gas, transfers, staking, and NFT calls. |
| VM transactions | `phantasma_py.transaction` | Serializing, signing, mining, and checking VM script transactions. |
| Carbon | `phantasma_py.carbon` | Carbon serialization, schemas, token creation payloads, series payloads, NFT mint payloads, signed Carbon messages. |

## Carbon Workflows

Use the Carbon workflow pages when creating native assets:

- [Token Deployment](token-deployment.md)
- [NFT Minting](nft-minting.md)
- [Schemas And Metadata](schemas-and-metadata.md)
- [Fees And Broadcasting](fees-and-broadcasting.md)
- [Carbon Operations](carbon-operations.md)

## Basic RPC Example

```python
from phantasma_py.rpc import PhantasmaRPC

rpc = PhantasmaRPC.mainnet()
info = rpc.get_account_info("P...")
soul = rpc.get_token_balance("P...", "SOUL")

print(info.address, info.name)
print(soul.decimal_amount())
```

Read-only calls do not require a signing key. Broadcasting helpers require
funded keys and an endpoint you explicitly intend to use.

## Guides

- [Setup](setup.md)
- [RPC](rpc.md)
- [Keys And Addresses](keys-and-addresses.md)
- [VM and Transactions](vm-and-transactions.md)
- [Carbon](carbon.md)
- [API Overview](api-reference.md)
- [Complete API Reference](reference/_index.md)
- [Examples](examples/_index.md)
