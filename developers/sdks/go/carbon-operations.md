# Go SDK Carbon Operations

The Go SDK includes lower-level Carbon structures for token, market, chain, gas,
and configuration calls. Use them when a workflow is not covered by the
create-token, create-series, or NFT mint builders.

## Typed Payloads

Carbon payload structures implement the SDK's `Blob` interface and can be
serialized with `carbon.Serialize`.

| Group | Examples |
| ----- | -------- |
| Token module | `MintFungibleArgs`, `TransferFungibleArgs`, `TransferNonFungibleArgs`, `BurnFungibleArgs`, `BurnNonFungibleArgs`, `UpdateTokenMetadataArgs`, `UpdateSeriesMetadataArgs` |
| Market module | `MarketSellTokenArgs`, `MarketCancelSaleArgs`, `MarketBuyTokenArgs`, listing query args, `MarketConfig` |
| Config data | `ChainConfig`, `GasConfig`, `TokensConfig` |
| Messages | `TxMsgCall`, `TxMsgCallMulti`, `TxMsgTransferFungible`, `TxMsgTransferNonFungibleSingle`, `TxMsgTrade`, `TxMsgPhantasma`, `TxMsgPhantasmaRaw` |

## Custom Call Message

```go
args := carbon.Serialize(carbon.TransferFungibleArgs{
    To:      receiver,
    TokenID: carbonTokenID,
    Amount:  carbon.NewIntX(big.NewInt(100)),
})

msg := carbon.TxMsg{
    Type:    carbon.TxTypeCall,
    Expiry:  carbon.NowUnixMillis() + 60_000,
    MaxGas:  carbon.DefaultFeeOptions().CalculateMaxGas(),
    MaxData: 100_000_000,
    GasFrom: sender,
    Call: &carbon.TxMsgCall{
        ModuleID: uint32(carbon.ModuleIDToken),
        MethodID: uint32(carbon.TokenMethodTransferFungible),
        Args:     args,
    },
}
```

Prefer lifecycle builders when they cover the operation. Use direct message
construction only when the module call is outside the higher-level helper set.

## Archive And Auction Reads

`pkg/rpc` exposes archive and auction wrappers. `WriteArchive` accepts raw bytes
and base64-encodes them for the RPC call. Use `WriteArchiveBase64` only when the
block content is already base64 text.
