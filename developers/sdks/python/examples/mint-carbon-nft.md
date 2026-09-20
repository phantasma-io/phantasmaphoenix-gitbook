# Mint Carbon NFT

This example builds a Carbon NFT mint message, plans its fee against a node,
signs it and broadcasts it.

```python
from phantasma_py import summarize_fee_plan
from phantasma_py.carbon import (
    build_mint_phantasma_non_fungible_single_tx,
    build_phantasma_nft_rom,
    bytes32_from_public_key,
    prepare_standard_token_schemas,
)
from phantasma_py.crypto import PhantasmaKeys
from phantasma_py.rpc import PhantasmaRPC


def main() -> None:
    rpc = PhantasmaRPC("https://testnet.phantasma.info/rpc")
    keys = PhantasmaKeys.from_wif("YOUR_WIF")
    sender = bytes32_from_public_key(keys.public_key)
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

    msg = build_mint_phantasma_non_fungible_single_tx(
        123,  # Carbon token id
        777,  # Phantasma series id
        sender,
        sender,  # receiver
        public_rom,
        ram=b"",
    )

    plan = rpc.fees.plan(msg)
    summary = summarize_fee_plan(plan)
    print(f"gas {summary.gas_bill} KCAL, storage deposit up to {summary.storage_ceiling} SOUL")

    tx_hash = rpc.send_transaction(plan.apply(msg), [keys])
    print(f"signer: {keys.address.text}")
    print(f"mint tx: {tx_hash}")


if __name__ == "__main__":
    main()
```

Replace the Carbon token id with the id returned by the confirmed token
deployment, and the Phantasma series id with the id used when the series was
created.

The builder carries no prices. `plan.apply(msg)` writes the ceilings into the
message, so `send_transaction` sends it as it is. To build without a node, plan
against a `GasConfig` and use the `_and_sign_hex` variant. See
[Fees And Broadcasting](/developers/sdks/python/fees-and-broadcasting.md).
