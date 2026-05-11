# Build VM Transaction

This example builds and signs a VM script transaction without broadcasting it.

```python
import time

from phantasma_py.crypto import PhantasmaKeys
from phantasma_py.transaction import Transaction
from phantasma_py.vm import ScriptBuilder


def main() -> None:
    keys = PhantasmaKeys.generate()
    script = ScriptBuilder.begin().call_interop("Runtime.Time").end_script()

    tx = Transaction(
        nexus_name="mainnet",
        chain_name="main",
        script=script,
        expiration=int(time.time()) + 300,
    )
    tx.sign(keys)

    print(f"address: {keys.address.text}")
    print(f"transaction hash: {tx.hash}")
    print(f"raw transaction: {tx.to_bytes().hex()}")


if __name__ == "__main__":
    main()
```

The generated key is local to the process. Replace it with
`PhantasmaKeys.from_wif(...)` only when you intentionally want to sign with a
real account.
