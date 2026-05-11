# Build Carbon Token Payload

This example builds Carbon token metadata payload bytes without broadcasting a
transaction.

```python
from phantasma_py.carbon import (
    Bytes32,
    IntX,
    build_token_info,
    build_token_metadata,
    prepare_standard_token_schemas,
    serialize,
)


def main() -> None:
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
                "name": "Example Art Token",
                "icon": "data:image/png;base64,AA==",
                "url": "https://example.invalid/art",
                "description": "Example token metadata",
            }
        ),
        token_schemas=serialize(schemas),
    )

    print(serialize(token).hex())


if __name__ == "__main__":
    main()
```

Use the signed transaction builders in [Carbon](../carbon.md) when you need to
turn this payload into a signed Carbon transaction.
