---
cover: .gitbook/assets/gitbook-banner-pha-phoenix-python-sdk.png
coverY: 0
---

# Python SDK

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
and module names under `phantasma_py`. Do not use older generated examples with
this SDK.

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

{% content-ref url="token-deployment.md" %}
Token Deployment
{% endcontent-ref %}

{% content-ref url="nft-minting.md" %}
NFT Minting
{% endcontent-ref %}

{% content-ref url="schemas-and-metadata.md" %}
Schemas And Metadata
{% endcontent-ref %}

{% content-ref url="fees-and-broadcasting.md" %}
Fees And Broadcasting
{% endcontent-ref %}

{% content-ref url="carbon-operations.md" %}
Carbon Operations
{% endcontent-ref %}

## Basic RPC Example

```python
from phantasma_py.rpc import PhantasmaRPC

rpc = PhantasmaRPC.mainnet()
account = rpc.get_account("P...")
soul = account.get_token_balance("SOUL", decimals=8)

print(account.address)
print(soul.decimal_amount())
```

Read-only calls do not require a signing key. Broadcasting helpers require
funded keys and an endpoint you explicitly intend to use.

## Guides

{% content-ref url="setup.md" %}
Setup
{% endcontent-ref %}

{% content-ref url="rpc.md" %}
RPC
{% endcontent-ref %}

{% content-ref url="keys-and-addresses.md" %}
Keys And Addresses
{% endcontent-ref %}

{% content-ref url="vm-and-transactions.md" %}
VM and Transactions
{% endcontent-ref %}

{% content-ref url="carbon.md" %}
Carbon
{% endcontent-ref %}

{% content-ref url="api-reference.md" %}
API Reference
{% endcontent-ref %}

{% content-ref url="examples/README.md" %}
Examples
{% endcontent-ref %}
