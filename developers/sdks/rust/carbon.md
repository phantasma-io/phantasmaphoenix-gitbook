# Rust SDK Carbon

`phantasma_sdk::carbon` implements Carbon wire formats, VM schemas, token and
NFT builders, module call argument types, and signed Carbon transaction
messages.

## Workflow Guides

Use these pages for end-to-end token and NFT flows:

{% content-ref url="token-deployment.md" %}
Token Deployment
{% endcontent-ref %}

{% content-ref url="nft-minting.md" %}
NFT Minting
{% endcontent-ref %}

{% content-ref url="schemas-and-metadata.md" %}
Schemas And Metadata
{% endcontent-ref %}

{% content-ref url="fees-and-broadcasting.md" %}
Fees And Broadcasting
{% endcontent-ref %}

{% content-ref url="carbon-operations.md" %}
Carbon Operations
{% endcontent-ref %}

## Deployment Lifecycle

The SDK exposes the native Carbon lifecycle directly:

1. Build token metadata and token schemas.
2. Build and sign `CreateToken`.
3. Broadcast with `PhantasmaRpc::send_carbon_transaction(...)`.
4. Parse the Carbon token id from the confirmed transaction result.
5. Build and sign `CreateTokenSeries`.
6. Parse the Carbon series id from the confirmed transaction result.
7. Build and sign one of the NFT mint transactions.

The builder helpers produce transaction bytes or hex. Broadcasting stays an
explicit async RPC step so applications can choose the network, key source,
fees, and confirmation policy.

For lower-level token, market, config, transfer, burn, multi-call, and trade
payloads, use [Carbon Operations](carbon-operations.md). For the validation
rules behind token metadata, NFT schemas, ROM, and RAM, use
[Schemas And Metadata](schemas-and-metadata.md).

## Wire Format

```rust
use phantasma_sdk::{CarbonReader, CarbonSerializable, CarbonWriter, IntX, Result};

fn main() -> Result<()> {
    let mut writer = CarbonWriter::new();
    IntX::from(100i64).write_carbon(&mut writer)?;

    let mut reader = CarbonReader::new(writer.bytes());
    let decoded = IntX::read_carbon(&mut reader)?;

    assert_eq!(decoded.to_string(), "100");
    Ok(())
}
```

Use generic helpers for whole-object round trips:

```rust
use phantasma_sdk::{deserialize, serialize, SignedTxMsg};

let decoded: SignedTxMsg = deserialize(raw_bytes)?;
assert_eq!(serialize(&decoded)?, raw_bytes);
```

## Token Metadata And Schemas

Token metadata requires `name`, `icon`, `url`, and `description`. The icon value
must be a PNG, JPEG, or WebP data URI with a non-empty base64 payload. Token
symbols must contain only uppercase ASCII letters `A-Z`.

```rust
use phantasma_sdk::{
    build_token_info, build_token_metadata, encode_hex, prepare_standard_token_schemas,
    serialize, Bytes32, IntX, Result,
};

fn main() -> Result<()> {
    let owner = Bytes32::default();
    let schemas = prepare_standard_token_schemas(false);

    let token = build_token_info(
        "ART",
        IntX::from(0i64),
        true,
        0,
        owner,
        build_token_metadata(&[
            ("name", "Art Token"),
            ("icon", "data:image/png;base64,AA=="),
            ("url", "https://example.invalid/art"),
            ("description", "Example token metadata"),
        ])?,
        serialize(&schemas)?,
    )?;

    println!("{}", encode_hex(serialize(&token)?));
    Ok(())
}
```

Fungible token info uses the same `build_token_info(...)` helper with
`is_nft=false`. In that case `token_schemas` is empty and `decimals` controls
the smallest unit. NFT token info requires `is_nft=true`, `decimals=0`, and
serialized token schemas.

## Create Token Transactions

```rust
use phantasma_sdk::{build_create_token_tx_and_sign_hex, PhantasmaKeys, Result, TokenInfo};

fn sign_create_token(token: TokenInfo, wif: &str) -> Result<String> {
    let keys = PhantasmaKeys::from_wif(wif)?;
    build_create_token_tx_and_sign_hex(token, &keys)
}
```

Use unsigned builders when you need to inspect or modify `TxMsg` before signing:

```rust
use phantasma_sdk::{
    build_create_token_tx, bytes32_from_public_key, sign_and_serialize_tx_msg_hex,
    PhantasmaKeys, Result, TokenInfo,
};

fn build_then_sign(token: TokenInfo, keys: &PhantasmaKeys) -> Result<String> {
    let creator = bytes32_from_public_key(&keys.public_key())?;
    let msg = build_create_token_tx(token, creator, None, 100_000_000, 0)?;

    sign_and_serialize_tx_msg_hex(&msg, keys)
}
```

## Series And NFT Minting

Current lifecycle builders include:

| Builder | Purpose |
| ------- | ------- |
| `build_create_token_tx` | Create a Carbon token payload. |
| `build_create_token_series_tx` | Create a token series payload. |
| `build_mint_non_fungible_tx` | Mint Carbon NFTs with explicit ROM/RAM bytes. |
| `build_mint_phantasma_non_fungible_tx` | Mint Phantasma NFT metadata through the Carbon token module. |
| `build_mint_phantasma_non_fungible_single_tx` | Convenience builder for one Phantasma NFT mint. |

NFT ROM helpers validate schema fields before producing bytes:

```rust
use phantasma_sdk::{build_nft_rom, prepare_standard_token_schemas, Result, VMValue};

fn main() -> Result<()> {
    let schemas = prepare_standard_token_schemas(false);
    let rom = build_nft_rom(
        &schemas.rom,
        1i64,
        &[
            ("name", VMValue::String("Example NFT".to_string())),
            ("description", VMValue::String("Example NFT metadata".to_string())),
            ("imageURL", VMValue::String("https://example.invalid/image.png".to_string())),
            ("infoURL", VMValue::String("https://example.invalid/nft".to_string())),
            ("royalties", VMValue::Int(10_000_000)),
        ],
    )?;

    println!("{}", rom.len());
    Ok(())
}
```

## Direct Transaction Messages

```rust
use phantasma_sdk::{
    bytes32_from_public_key, sign_and_serialize_tx_msg_hex, PhantasmaKeys, Result,
    SmallString, TxMsg, TxMsgTransferFungible, TxPayload, TxType,
};

fn main() -> Result<()> {
    let keys = PhantasmaKeys::try_from_slice(&[7u8; 32])?;
    let signer = bytes32_from_public_key(&keys.public_key())?;
    let receiver =
        bytes32_from_public_key(&PhantasmaKeys::try_from_slice(&[9u8; 32])?.public_key())?;

    let msg = TxMsg {
        tx_type: TxType::TransferFungible,
        expiry: 1_759_711_416_000,
        max_gas: 10_000_000,
        max_data: 1_000,
        gas_from: signer,
        payload: SmallString::new("example")?,
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

## Result Parsers

Use parser helpers for token-module result bytes:

```rust
use phantasma_sdk::{
    parse_create_token_result, parse_create_token_series_result,
    parse_mint_non_fungible_result, parse_mint_phantasma_non_fungible_result,
};
```
