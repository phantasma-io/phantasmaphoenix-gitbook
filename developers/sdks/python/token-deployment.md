# Python SDK Token Deployment

This page shows the Carbon token deployment flow in `phantasma_py`. It builds
native Carbon transaction messages, signs them locally, and shows where to
broadcast and parse results.

## Flow

Carbon NFT deployment has three steps:

1. Build token metadata and schemas.
2. Sign and broadcast `CreateToken`.
3. Parse the returned Carbon token id and use it when creating series or
   minting NFTs.

Series creation is a separate transaction after the token exists:

1. Build `SeriesInfo`.
2. Sign and broadcast `CreateTokenSeries`.
3. Parse the returned Carbon series id and use it when minting.

The SDK does not hide broadcasting. `send_carbon_transaction(...)` sends the
signed bytes to the selected RPC endpoint, so use it only with an intentional
endpoint, funded signing key, and final wallet/operator approval.

## Build Token Metadata

Token metadata is required for all Carbon tokens. The SDK validates the four
required string fields and the icon data URI.

```python
from phantasma_py.carbon import build_token_metadata

metadata = build_token_metadata(
    {
        "name": "Example Art Token",
        "icon": "data:image/png;base64,AA==",
        "url": "https://example.invalid/art",
        "description": "Example NFT collection",
    }
)
```

Rules enforced by the SDK:

- `name`, `icon`, `url`, and `description` must be present and non-empty.
- `icon` must be a PNG, JPEG, or WebP data URI with non-empty base64 data.
- Token symbols must contain uppercase ASCII letters `A-Z`.

## Build NFT Schemas

For a standard NFT collection, use `prepare_standard_token_schemas(False)`.
With `shared_metadata=False`, the standard NFT fields are stored per NFT in
ROM.

```python
from phantasma_py.carbon import prepare_standard_token_schemas, serialize

schemas = prepare_standard_token_schemas(shared_metadata=False)
token_schemas = serialize(schemas)
```

The standard NFT fields are:

- `name`
- `description`
- `imageURL`
- `infoURL`
- `royalties`

Use `shared_metadata=True` only when those standard fields should live in
series metadata instead of each NFT ROM.

## Build And Sign CreateToken

```python
from phantasma_py.carbon import (
    IntX,
    build_create_token_tx_and_sign_hex,
    build_token_info,
    build_token_metadata,
    bytes32_from_public_key,
    prepare_standard_token_schemas,
    serialize,
)
from phantasma_py.crypto import PhantasmaKeys

keys = PhantasmaKeys.from_wif("YOUR_WIF")
owner = bytes32_from_public_key(keys.public_key)
schemas = prepare_standard_token_schemas(shared_metadata=False)

token_info = build_token_info(
    symbol="ART",
    max_supply=IntX(0),
    is_nft=True,
    decimals=0,
    owner=owner,
    metadata=build_token_metadata(
        {
            "name": "Example Art Token",
            "icon": "data:image/png;base64,AA==",
            "url": "https://example.invalid/art",
            "description": "Example NFT collection",
        }
    ),
    token_schemas=serialize(schemas),
)

create_token_hex = build_create_token_tx_and_sign_hex(token_info, keys)
print(create_token_hex)
```

For NFT tokens:

- `is_nft=True` sets the non-fungible token flag.
- `decimals` should be `0`.
- `max_supply=IntX(0)` means unlimited supply.
- `token_schemas` is required.

## Broadcast And Parse Token Id

```python
from phantasma_py.carbon import parse_create_token_result
from phantasma_py.rpc import PhantasmaRPC

rpc = PhantasmaRPC("https://testnet.phantasma.info/rpc")
tx_hash = rpc.send_carbon_transaction(create_token_hex)

tx_result = rpc.get_transaction(tx_hash)
carbon_token_id = parse_create_token_result(tx_result.result)

print(carbon_token_id)
```

This broadcast block is live network code. The SDK tests verify serialization,
signing, and result parsing; funded live broadcasting must be done by the
caller on the intended network.

## Build And Sign CreateTokenSeries

Use the Carbon token id returned by `CreateToken`.

```python
from phantasma_py.carbon import (
    build_create_token_series_tx_and_sign_hex,
    build_series_info,
    bytes32_from_public_key,
)
from phantasma_py.crypto import PhantasmaKeys

keys = PhantasmaKeys.from_wif("YOUR_WIF")
owner = bytes32_from_public_key(keys.public_key)

carbon_token_id = 123
series_info = build_series_info(
    phantasma_series_id=1,
    max_mint=0,
    max_supply=0,
    owner=owner,
)

create_series_hex = build_create_token_series_tx_and_sign_hex(
    carbon_token_id,
    series_info,
    keys,
)
```

`max_mint=0` and `max_supply=0` leave those series limits unlimited. Use
positive values when the collection needs explicit caps.

## Broadcast And Parse Series Id

```python
from phantasma_py.carbon import parse_create_token_series_result
from phantasma_py.rpc import PhantasmaRPC

rpc = PhantasmaRPC("https://testnet.phantasma.info/rpc")
tx_hash = rpc.send_carbon_transaction(create_series_hex)

tx_result = rpc.get_transaction(tx_hash)
carbon_series_id = parse_create_token_series_result(tx_result.result)

print(carbon_series_id)
```

Use the parsed `carbon_series_id` when minting Carbon NFTs.

## Read Back Deployment State

After the deployment transactions are confirmed, read the token and series
through RPC:

```python
token = rpc.get_token("ART")
series_page = rpc.get_token_series("ART", carbon_token_id=carbon_token_id)

print(token.symbol, token.carbon_id)
print(series_page.cursor, series_page.result)
```

`get_token_series_by_id(...)` can fetch one known series when you already have
the Phantasma series id or Carbon series id.
