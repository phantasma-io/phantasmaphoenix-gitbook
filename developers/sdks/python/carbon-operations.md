# Python SDK Carbon Operations

The high-level Carbon lifecycle helpers cover token creation, series creation,
and NFT minting. The Carbon module also exposes typed transaction payloads and
module-call argument structures for lower-level operations.

Use this page when you need to build Carbon messages directly instead of using
one of the lifecycle helper functions.

## High-Level Helpers Vs Direct Messages

| Need | Preferred API |
| ---- | ------------- |
| Create a token | `build_create_token_tx*` |
| Create a token series | `build_create_token_series_tx*` |
| Mint direct Carbon NFTs | `build_mint_non_fungible_tx*` |
| Mint Phantasma NFT helper metadata | `build_mint_phantasma_non_fungible_*` |
| Transfer, burn, market, config, metadata update, custom calls | `TxMsg`, `TxMsgCall`, typed args, and `sign_tx_msg(...)` |

Direct messages are lower level. They give you the wire shape, but the
application is still responsible for choosing the method, fields, permissions,
fees, and confirmation flow.

## Direct Carbon Transfer Message

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

keys = PhantasmaKeys.from_wif("YOUR_WIF")
sender = bytes32_from_public_key(keys.public_key)
receiver = bytes32_from_public_key(PhantasmaKeys.generate().public_key)

msg = TxMsg(
    TxType.TRANSFER_FUNGIBLE,
    expiry=1_759_711_416_000,
    max_gas=10_000_000,
    max_data=1_000,
    gas_from=sender,
    payload=SmallString("example"),
    msg=TxMsgTransferFungible(
        to=receiver,
        token_id=1,
        amount=1_000_000,
    ),
)

signed_hex = sign_and_serialize_tx_msg_hex(msg, keys)
```

The direct transfer message uses a Carbon token id, not a token symbol. Keep the
symbol and Carbon token id together in your application state.

## Token Module Call Args

The SDK includes serializable argument types for current token-module calls:

| Args type | Use it for |
| --------- | ---------- |
| `MintFungibleArgs` | Token module `MintFungible`. |
| `TransferFungibleArgs` | Token module `TransferFungible`. |
| `TransferNonFungibleArgs` | Token module `TransferNonFungible`. |
| `BurnFungibleArgs` | Token module `BurnFungible`. |
| `BurnNonFungibleArgs` | Token module `BurnNonFungible`. |
| `CreateTokenSeriesArgs` | Token module `CreateTokenSeries`. |
| `CreateMintedTokenSeriesArgs` | Token module `CreateMintedTokenSeries`. |
| `UpdateTokenMetadataArgs` | Token module `UpdateTokenMetadata`. |
| `UpdateSeriesMetadataArgs` | Token module `UpdateSeriesMetadata`. |
| `MintPhantasmaNonFungibleArgs` | Token module `MintPhantasmaNonFungible`. |

Example: serialize token-module mint args.

```python
from phantasma_py.carbon import IntX, MintFungibleArgs, serialize

args = MintFungibleArgs(token_id=1, to=receiver, amount=IntX(100_000_000))
args_bytes = serialize(args)
```

To make a module call, place the serialized args in `TxMsgCall`.

```python
from phantasma_py.carbon import ModuleID, TokenContractMethod, TxMsgCall

call = TxMsgCall(
    module_id=ModuleID.TOKEN,
    method_id=TokenContractMethod.MINT_FUNGIBLE,
    args=args_bytes,
)
```

Only call methods that the signing account is allowed to execute on the target
network. The SDK can serialize the call, but authorization is chain behavior.

## Market Module Args

Market argument types are also exposed:

| Args type | Use it for |
| --------- | ---------- |
| `MarketSellTokenArgs` / `MarketSellTokenByIDArgs` | Create a fixed-price listing. |
| `MarketCancelSaleArgs` / `MarketCancelSaleByIDArgs` | Cancel a listing. |
| `MarketBuyTokenArgs` / `MarketBuyTokenByIDArgs` | Buy a listing. |
| `MarketGetTokenListingCountArgs` | Query listing count through a module call. |
| `MarketGetTokenListingInfoArgs` / `MarketGetTokenListingInfoByIDArgs` | Query listing details through a module call. |
| `TokenListing`, `MarketConfig`, `default_market_config()` | Listing/config wire structures. |

For read-only marketplace information, prefer RPC methods when available. Use
market module call args when you are deliberately constructing a Carbon module
message.

## Config Structures

`ChainConfig`, `GasConfig`, `TokensConfig`, and `MarketConfig` implement the
same Carbon serialization contract as transaction messages.

```python
from phantasma_py.carbon import TokensConfig, TokensConfigFlags, serialize

config = TokensConfig(
    TokensConfigFlags.REQUIRE_METADATA
    | TokensConfigFlags.REQUIRE_NFT_STANDARD
)

config_bytes = serialize(config)
```

These structures describe wire data. Whether a config update is accepted depends
on governance and module permissions.

## Multi-Call And Trade Payloads

`TxMsgCallMulti` groups multiple module calls in one Carbon message. `TxMsgTrade`
groups transfer, mint, and burn payloads in the trade payload shape used by the
Carbon wire format.

Use these only when your application has a concrete chain-supported flow that
requires the lower-level payload. For ordinary token deployment and minting,
prefer the lifecycle helpers.

## Round-Trip Decoding

```python
from phantasma_py.carbon import SignedTxMsg, deserialize, serialize

decoded = deserialize(raw_signed_bytes, SignedTxMsg)

assert serialize(decoded) == raw_signed_bytes
```

Round trips are useful in services that inspect a signed Carbon transaction
before submitting it to RPC.

## Result Parsers Are Operation-Specific

Only a few token lifecycle calls have dedicated parser helpers:

- `parse_create_token_result`
- `parse_create_token_series_result`
- `parse_mint_non_fungible_result`
- `parse_mint_phantasma_non_fungible_result`

For other direct operations, inspect the chain/RPC result shape for that module
method before adding a parser. Do not assume every Carbon call returns the same
result format.
