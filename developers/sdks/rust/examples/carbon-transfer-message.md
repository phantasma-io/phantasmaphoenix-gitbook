# Rust Example: Carbon Transfer Message

This example builds and signs a direct Carbon fungible-transfer message offline.
It prints signed transaction hex and does not broadcast.

```rust
use phantasma_sdk::{
    bytes32_from_public_key, sign_and_serialize_tx_msg_hex, PhantasmaKeys, Result,
    SmallString, TxMsg, TxMsgTransferFungible, TxPayload, TxType,
};

fn main() -> Result<()> {
    let keys = PhantasmaKeys::try_from_slice(&[7u8; 32])?;
    let receiver_keys = PhantasmaKeys::try_from_slice(&[9u8; 32])?;

    let sender = bytes32_from_public_key(&keys.public_key())?;
    let receiver = bytes32_from_public_key(&receiver_keys.public_key())?;

    let msg = TxMsg {
        tx_type: TxType::TransferFungible,
        expiry: 1_759_711_416_000,
        max_gas: 10_000_000,
        max_data: 1_000,
        gas_from: sender,
        payload: SmallString::new("docs")?,
        msg: TxPayload::TransferFungible(TxMsgTransferFungible {
            to: receiver,
            token_id: 1,
            amount: 1_000_000,
        }),
    };

    println!("{}", sign_and_serialize_tx_msg_hex(&msg, &keys)?);
    Ok(())
}
```

`token_id` is the Carbon token id. If your application starts from a symbol, read
the token first and persist the matching Carbon id.
