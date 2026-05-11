# Python SDK NFT Minting

This page covers Carbon NFT minting with `phantasma_py`. It starts after an NFT
token and series already exist.

## Required Inputs

You need:

- a funded signing key;
- the Carbon token id returned by `CreateToken`;
- the Carbon series id returned by `CreateTokenSeries`;
- the token schemas used by the token;
- a receiver as `Bytes32`;
- ROM metadata that matches the token ROM schema.

The standard NFT ROM fields are:

- `name`
- `description`
- `imageURL`
- `infoURL`
- `royalties`

`royalties` is the integer on-chain royalty value. `10_000_000` represents 1%.

## Build Standard NFT ROM

```python
from phantasma_py.carbon import build_nft_rom, prepare_standard_token_schemas

schemas = prepare_standard_token_schemas(shared_metadata=False)

rom = build_nft_rom(
    schemas.rom,
    phantasma_nft_id=1,
    metadata=[
        ("name", "Example NFT #1"),
        ("description", "Example NFT metadata"),
        ("imageURL", "https://example.invalid/nft-1.png"),
        ("infoURL", "https://example.invalid/nft-1"),
        ("royalties", 10_000_000),
    ],
)
```

`build_nft_rom(...)` adds the chain-owned `_i` field from
`phantasma_nft_id` and serializes every schema field with type checks.

## Build And Sign MintNonFungible

```python
from phantasma_py.carbon import (
    build_mint_non_fungible_tx_and_sign_hex,
    bytes32_from_public_key,
)
from phantasma_py.crypto import PhantasmaKeys

keys = PhantasmaKeys.from_wif("YOUR_WIF")
receiver = bytes32_from_public_key(keys.public_key)

carbon_token_id = 123
carbon_series_id = 1

mint_hex = build_mint_non_fungible_tx_and_sign_hex(
    carbon_token_id,
    carbon_series_id,
    keys,
    receiver,
    rom,
    ram=b"",
)
```

`ram` is optional. Pass serialized RAM bytes only when the token has a RAM
schema or when the token uses dynamic RAM extras.

## Broadcast And Parse Mint Result

```python
from phantasma_py.carbon import parse_mint_non_fungible_result
from phantasma_py.rpc import PhantasmaRPC

rpc = PhantasmaRPC("https://testnet.phantasma.info/rpc")
tx_hash = rpc.send_carbon_transaction(mint_hex)

tx_result = rpc.get_transaction(tx_hash)
nft_addresses = parse_mint_non_fungible_result(carbon_token_id, tx_result.result)

print(nft_addresses[0].hex())
```

`parse_mint_non_fungible_result(...)` returns Carbon NFT addresses derived from
the Carbon token id and the instance ids emitted by the chain.

## Phantasma NFT Mint Helper

The SDK also exposes Phantasma NFT mint helpers. These use a token-module call
instead of the direct `MintNonFungible` transaction payload and return
`PhantasmaNFTMintResult` values.

Use `build_phantasma_nft_rom(...)` for the caller-provided public ROM. It
rejects reserved fields such as `_i` and `rom`, because those fields are
chain-owned for this flow.

```python
from phantasma_py.carbon import (
    build_mint_phantasma_non_fungible_single_tx_and_sign_hex,
    build_phantasma_nft_rom,
    bytes32_from_public_key,
    prepare_standard_token_schemas,
)
from phantasma_py.crypto import PhantasmaKeys

keys = PhantasmaKeys.from_wif("YOUR_WIF")
receiver = bytes32_from_public_key(keys.public_key)
schemas = prepare_standard_token_schemas(shared_metadata=False)

public_rom = build_phantasma_nft_rom(
    schemas.rom,
    [
        ("name", "Example NFT #1"),
        ("description", "Example NFT metadata"),
        ("imageURL", "https://example.invalid/nft-1.png"),
        ("infoURL", "https://example.invalid/nft-1"),
        ("royalties", 10_000_000),
    ],
)

mint_hex = build_mint_phantasma_non_fungible_single_tx_and_sign_hex(
    token_id=123,
    phantasma_series_id=1,
    signer=keys,
    receiver=receiver,
    public_rom=public_rom,
    ram=b"",
)
```

Parse the result with:

```python
from phantasma_py.carbon import parse_mint_phantasma_non_fungible_result

tx_result = rpc.get_transaction(tx_hash)
minted = parse_mint_phantasma_non_fungible_result(tx_result.result)

print(minted[0].phantasma_nft_id.hex(), minted[0].carbon_instance_id)
```

## Read Back Minted NFTs

Use the current Carbon id-aware RPC calls:

```python
nfts_page = rpc.get_token_nfts(
    carbon_token_id,
    carbon_series_id,
    page_size=20,
    cursor="",
    extended=True,
)

account_nfts = rpc.get_account_nfts(
    account=keys.address.text,
    token_symbol="ART",
    carbon_token_id=carbon_token_id,
    carbon_series_id=carbon_series_id,
)
```

Use the cursor returned by these calls to continue pagination.

## When To Use Each Mint Helper

| Helper | Use it when |
| ------ | ----------- |
| `build_mint_non_fungible_tx_and_sign_hex` | You already have explicit ROM/RAM bytes for the NFT. |
| `build_mint_phantasma_non_fungible_single_tx_and_sign_hex` | You want the SDK to build the token-module Phantasma NFT mint call for one NFT. |
| `build_mint_phantasma_non_fungible_tx_and_sign_hex` | You want to mint multiple Phantasma NFT entries in one token-module call. |
