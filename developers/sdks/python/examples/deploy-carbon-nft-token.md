# Deploy Carbon NFT Token

This example builds and signs the `CreateToken` and `CreateTokenSeries`
transaction payloads for a standard Carbon NFT collection. It prints the signed
transaction hex, and it does not broadcast.

Signing needs the chain's prices, because the builders carry none. The example
reads the gas configuration from a node and plans against it.

```python
from phantasma_py.carbon import (
    IntX,
    build_create_token_series_tx_and_sign_hex,
    build_create_token_tx_and_sign_hex,
    build_series_info,
    build_token_info,
    build_token_metadata,
    bytes32_from_public_key,
    prepare_standard_token_schemas,
    serialize,
)
from phantasma_py.crypto import PhantasmaKeys
from phantasma_py.rpc import PhantasmaRPC


def main() -> None:
    rpc = PhantasmaRPC("https://testnet.phantasma.info/rpc")
    keys = PhantasmaKeys.generate()
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

    config = rpc.fees.config()

    create_token_hex = build_create_token_tx_and_sign_hex(token_info, keys, config)
    print(f"signer: {keys.address.text}")
    print(f"create token tx: {create_token_hex}")

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
        config,
    )
    print(f"create series tx: {create_series_hex}")


if __name__ == "__main__":
    main()
```

For live deployment, send `create_token_hex` first, wait for confirmation, parse
the Carbon token id from the transaction result, and then build the series
transaction with that id.
