# Mint Carbon NFT

This example builds and signs a Carbon NFT mint transaction without
broadcasting it.

```python
from phantasma_py.carbon import (
    build_mint_non_fungible_tx_and_sign_hex,
    build_nft_rom,
    bytes32_from_public_key,
    prepare_standard_token_schemas,
)
from phantasma_py.crypto import PhantasmaKeys


def main() -> None:
    keys = PhantasmaKeys.generate()
    receiver = bytes32_from_public_key(keys.public_key)
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

    mint_hex = build_mint_non_fungible_tx_and_sign_hex(
        token_id=123,
        series_id=1,
        signer=keys,
        receiver=receiver,
        rom=rom,
        ram=b"",
    )

    print(f"signer: {keys.address.text}")
    print(f"mint tx: {mint_hex}")


if __name__ == "__main__":
    main()
```

Replace `token_id` and `series_id` with the Carbon ids returned by the
confirmed token and series deployment transactions.
