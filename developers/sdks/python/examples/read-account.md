# Read Account

This read-only example queries an account and prints its SOUL balance.

```python
import os

from phantasma_py.rpc import PhantasmaRPC


def main() -> None:
    endpoint = os.environ.get("PHANTASMA_RPC", "https://pharpc1.phantasma.info/rpc")
    address = os.environ["PHANTASMA_ADDRESS"]

    rpc = PhantasmaRPC(endpoint)
    account = rpc.get_account(address)
    soul = account.get_token_balance("SOUL", decimals=8)

    print(f"{account.address}: {soul.decimal_amount()} SOUL")


if __name__ == "__main__":
    main()
```

Run it with an address and endpoint:

```bash
export PHANTASMA_ADDRESS="P..."
export PHANTASMA_RPC="https://pharpc1.phantasma.info/rpc"
python read_account.py
```
