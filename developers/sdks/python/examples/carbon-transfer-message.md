# Python Example: Carbon Transfer Message

This example builds and signs a direct Carbon fungible-transfer message offline.
It prints signed transaction hex and does not broadcast.

```python
from phantasma_py.carbon import (
    SmallString,
    TxMsg,
    TxMsgTransferFungible,
    TxType,
    bytes32_from_public_key,
    sign_and_serialize_tx_msg_hex,
)
from phantasma_py.crypto import PhantasmaKeys

keys = PhantasmaKeys(bytes([7]) * 32)
receiver_keys = PhantasmaKeys(bytes([9]) * 32)

sender = bytes32_from_public_key(keys.public_key)
receiver = bytes32_from_public_key(receiver_keys.public_key)

msg = TxMsg(
    TxType.TRANSFER_FUNGIBLE,
    expiry=1_759_711_416_000,
    max_gas=10_000_000,
    max_data=1_000,
    gas_from=sender,
    payload=SmallString("docs"),
    msg=TxMsgTransferFungible(
        to=receiver,
        token_id=1,
        amount=1_000_000,
    ),
)

print(sign_and_serialize_tx_msg_hex(msg, keys))
```

`token_id` is the Carbon token id. If your application starts from a symbol, read
the token first and persist the matching Carbon id.
