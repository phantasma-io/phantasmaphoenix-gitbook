# Python SDK Carbon

`phantasma_py.carbon` implements Carbon wire formats, VM schemas, token and NFT
builder helpers, module call argument types, and signed Carbon transaction
messages.

## Workflow Guides

Use these pages for end-to-end token and NFT flows:

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

## Deployment Lifecycle

The SDK exposes the native Carbon lifecycle directly:

1. Build token metadata and token schemas.
2. Build and sign `CreateToken`.
3. Broadcast with `PhantasmaRPC.send_carbon_transaction(...)`.
4. Parse the Carbon token id from the confirmed transaction result.
5. Build and sign `CreateTokenSeries`.
6. Parse the Carbon series id from the confirmed transaction result.
7. Build and sign one of the NFT mint transactions.

The builder helpers produce transaction bytes or hex. Broadcasting stays an
explicit RPC step so applications can choose the network, key source, fees, and
confirmation policy.

For lower-level token, market, config, transfer, burn, multi-call, and trade
payloads, use [Carbon Operations](carbon-operations.md). For the validation
rules behind token metadata, NFT schemas, ROM, and RAM, use
[Schemas And Metadata](schemas-and-metadata.md).

## Wire Format

The Carbon module provides `CarbonWriter`, `CarbonReader`, fixed byte types, and
generic `serialize()` / `deserialize()` helpers.

```python
from phantasma_py.carbon import CarbonReader, CarbonWriter, IntX

writer = CarbonWriter()
IntX(100).write_carbon(writer)

decoded = IntX.read_carbon(CarbonReader(writer.bytes()))
assert decoded.value == 100
```

Carbon serialization uses fixed-width little-endian integers, zero-terminated
UTF-8 strings, fixed byte values (`Bytes16`, `Bytes32`, `Bytes64`),
length-prefixed arrays, and compact signed `IntX` values.

## Token Metadata And Schemas

Token metadata requires `name`, `icon`, `url`, and `description`. The icon value
must be a PNG, JPEG, or WebP data URI with a non-empty base64 payload. Token
symbols must contain only uppercase ASCII letters `A-Z`.

```python
from phantasma_py.carbon import (
    Bytes32,
    IntX,
    build_token_info,
    build_token_metadata,
    prepare_standard_token_schemas,
    serialize,
)

owner = Bytes32()
schemas = prepare_standard_token_schemas(shared_metadata=False)

token = build_token_info(
    symbol="ART",
    max_supply=IntX(0),
    is_nft=True,
    decimals=0,
    owner=owner,
    metadata=build_token_metadata(
        {
            "name": "Art Token",
            "icon": "data:image/png;base64,AA==",
            "url": "https://example.invalid/art",
            "description": "Example token metadata",
        }
    ),
    token_schemas=serialize(schemas),
)

payload_hex = serialize(token).hex()
```

`prepare_standard_token_schemas(False)` creates the standard series, ROM, and
RAM schema structure expected by current Carbon token helpers.

Fungible token info uses the same `build_token_info(...)` helper with
`is_nft=False`. In that case `token_schemas` is empty and `decimals` controls
the smallest unit. NFT token info requires `is_nft=True`, `decimals=0`, and
serialized token schemas.

## Create Token Transactions

Use token info to build a signed Carbon transaction message.

```python
from phantasma_py.carbon import build_create_token_tx_and_sign_hex
from phantasma_py.crypto import PhantasmaKeys


def sign_create_token(token_info, wif: str) -> str:
    keys = PhantasmaKeys.from_wif(wif)
    return build_create_token_tx_and_sign_hex(token_info, keys)
```

`build_create_token_tx(...)` returns an unsigned `TxMsg` if you need to inspect
or sign separately. The `_and_sign` helpers return serialized signed bytes, and
the `_and_sign_hex` helpers return hex.

## Series And NFT Minting

The SDK exposes builders for the current Carbon token lifecycle:

| Builder | Purpose |
| ------- | ------- |
| `build_create_token_tx` | Create a Carbon token payload. |
| `build_create_token_series_tx` | Create a token series payload. |
| `build_mint_non_fungible_tx` | Mint Carbon NFTs with explicit ROM/RAM bytes. |
| `build_mint_phantasma_non_fungible_tx` | Mint Phantasma NFT metadata through the Carbon token module. |
| `build_mint_phantasma_non_fungible_single_tx` | Convenience builder for one Phantasma NFT mint. |

NFT ROM helpers validate schema fields before producing bytes:

```python
from phantasma_py.carbon import build_nft_rom, prepare_standard_token_schemas

schemas = prepare_standard_token_schemas(shared_metadata=False)
rom = build_nft_rom(
    schemas.rom,
    1,
    [
        ("name", "Example NFT"),
        ("description", "Example NFT metadata"),
        ("imageURL", "https://example.invalid/image.png"),
        ("infoURL", "https://example.invalid/nft"),
        ("royalties", 10_000_000),
    ],
)
```

## Direct Transaction Messages

For lower-level flows, construct `TxMsg` and sign it directly.

```python
from phantasma_py.carbon import SignedTxMsg, deserialize, serialize

decoded = deserialize(raw_bytes, SignedTxMsg)
assert serialize(decoded) == raw_bytes
```

Signing helpers:

```python
from phantasma_py.carbon import sign_and_serialize_tx_msg_hex
from phantasma_py.crypto import PhantasmaKeys

keys = PhantasmaKeys.from_wif("...")
raw_hex = sign_and_serialize_tx_msg_hex(tx_msg, keys)
```

## Result Parsers

Carbon call results are returned as hex strings by script or transaction flows.
The SDK includes parsers for current token-module result shapes:

```python
from phantasma_py.carbon import (
    parse_create_token_result,
    parse_create_token_series_result,
    parse_mint_non_fungible_result,
    parse_mint_phantasma_non_fungible_result,
)
```

Use these helpers instead of hand-decoding Carbon result bytes.
