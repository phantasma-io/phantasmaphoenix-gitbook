---
title: "Python SDK NFT Minting"
linkTitle: "NFT Minting"
weight: 70
---

This page covers Carbon NFT minting with `phantasma_py`. It starts after an NFT
token and series already exist.

The chain derives the NFT id and stores a canonical ROM. One call mints one or
more instances.

## Required Inputs

You need:

- a funded signing key;
- the Carbon token id returned by `CreateToken`;
- the Phantasma series id used when the series was created;
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

## Build The Public ROM

`build_phantasma_nft_rom(...)` serializes the public part of the ROM. It rejects
the reserved fields `_i` and `rom`, because the chain owns them for this flow.

Use the ROM schema the token was created with. The example continues from a
token created with `prepare_standard_token_schemas(shared_metadata=False)`,
which puts the standard fields in the per-NFT ROM.

```python
from phantasma_py.carbon import (
    build_phantasma_nft_rom,
    bytes32_from_public_key,
    prepare_standard_token_schemas,
)
from phantasma_py.crypto import PhantasmaKeys

keys = PhantasmaKeys.from_wif("YOUR_WIF")
sender = bytes32_from_public_key(keys.public_key)
receiver = sender

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
```

`build_nft_rom(schema, phantasma_nft_id, metadata)` is the other ROM builder. It
writes the chain-owned `_i` field itself, and it serves the flows where the
caller supplies the id.

## Build, Plan, Sign And Send

```python
from phantasma_py.carbon import build_mint_phantasma_non_fungible_single_tx
from phantasma_py.rpc import PhantasmaRPC

rpc = PhantasmaRPC("https://testnet.phantasma.info/rpc")

carbon_token_id = 123
phantasma_series_id = 777

msg = build_mint_phantasma_non_fungible_single_tx(
    carbon_token_id,
    phantasma_series_id,
    sender,
    receiver,
    public_rom,
    ram=b"",
)

tx_hash = rpc.send_transaction(msg, [keys])
```

The builder carries no prices. `send_transaction` plans the fee from the
message, signs it and broadcasts it.

`ram` is optional. Pass serialized RAM bytes only when the token has a RAM
schema or when the token uses dynamic RAM extras.

A mint prices three facts the message does not carry: whether the recipient
already holds the token, whether the supply row still exists, and whether the
series mints duplicates. Each is taken at the reading that costs more. See
[Fees And Broadcasting](fees-and-broadcasting.md).

The SDK carries no builder for a direct `MINT_NON_FUNGIBLE`. The chain refuses
that operation where governance has not allowed caller-supplied ROM ids, and
that is the state of the public chains today.

## Mint Without A Client

The `_and_sign` helpers plan the message against a `GasConfig` the caller
supplies:

```python
from phantasma_py.carbon import build_mint_phantasma_non_fungible_single_tx_and_sign_hex

config = rpc.fees.config()

mint_hex = build_mint_phantasma_non_fungible_single_tx_and_sign_hex(
    token_id=carbon_token_id,
    phantasma_series_id=phantasma_series_id,
    signer=keys,
    receiver=receiver,
    public_rom=public_rom,
    ram=b"",
    config=config,
)

tx_hash = rpc.send_carbon_transaction(mint_hex)
```

For batch mints, pass a sequence of `PhantasmaNFTMintInfo` to
`build_mint_phantasma_non_fungible_tx` or its signing variants.

## Parse The Mint Result

```python
from phantasma_py.carbon import parse_mint_phantasma_non_fungible_result

tx_result = rpc.get_transaction(tx_hash)
if not tx_result.state_is_success:
    raise RuntimeError(f"mint failed: {tx_result.state}")

minted = parse_mint_phantasma_non_fungible_result(tx_result.result)
print(minted[0].phantasma_nft_id.hex(), minted[0].carbon_instance_id)
```

Each entry carries the Phantasma NFT id the chain derived and the Carbon
instance id it minted.

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

Use the cursor returned by these calls to continue pagination. `page_size`
accepts 1 to 100, and 1 to 50 when `extended` is true.

## When To Use Each Mint Helper

| Helper | Use it when |
| ------ | ----------- |
| `build_mint_phantasma_non_fungible_single_tx` | You send through the client and mint one instance. |
| `build_mint_phantasma_non_fungible_tx` | You send through the client and mint several instances in one call. |
| `build_mint_phantasma_non_fungible_single_tx_and_sign_hex` | You hold a `GasConfig` and want signed hex for one instance. |
| `build_mint_phantasma_non_fungible_tx_and_sign_hex` | You hold a `GasConfig` and want signed hex for a batch. |
