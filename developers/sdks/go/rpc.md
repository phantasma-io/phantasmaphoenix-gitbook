# Go SDK RPC

`pkg/rpc` wraps Phantasma JSON-RPC endpoints with typed methods and result
models from `pkg/rpc/response`. Each method is context-first and returns an
ordinary Go `(value, error)` pair.

## Client Construction

```go
client := rpc.NewRPC("http://localhost:5172/rpc")
mainnet := rpc.NewRPCMainnet()
testnet := rpc.NewRPCTestnet()
mainnetSet := rpc.NewRPCSetMainnet()
```

Use `client.Call(ctx, method, params...)` only when a node method is needed
before the SDK has a typed wrapper. Typed wrappers perform response decoding and
should be preferred for application code.

## Common Parameters

| Parameter | Meaning |
| --------- | ------- |
| `ctx` | Request context. Pass a timeout or cancellation context from the caller. |
| `extended` | Requests expanded response data when the node supports compact and expanded shapes. |
| `page`, `pageSize` | Numeric pagination for older endpoints. |
| `cursor` | Opaque cursor for Carbon token/NFT inventory endpoints. Keep passing it until the returned cursor is empty. |
| `carbonTokenID`, `carbonSeriesID` | Numeric Carbon filters. Pass `0` when no Carbon id filter is needed. |
| `AddressTypePhantasma`, `AddressTypeCarbon` | Explicit address interpretation for wrappers that expose node address-type parameters. |

## Core Reads

```go
height, err := client.GetBlockHeight(ctx, "main")
account, err := client.GetAccount(ctx, "P...")
tx, err := client.GetTransaction(ctx, "HASH")
tokens, err := client.GetTokens(ctx, true)
```

Use account-level helpers when you already loaded a full account:

```go
token, err := client.GetToken(ctx, "SOUL", true)
if err != nil {
    return err
}

balance := account.GetTokenBalance(token)
fmt.Println(balance.ConvertDecimals())
```

## Carbon And Current RPC Wrappers

The current Go SDK includes the Carbon-era methods used by the other Phoenix
SDKs:

| Area | Methods |
| ---- | ------- |
| Build and chain config | `GetVersion`, `GetPhantasmaVMConfig`, `GetChains`, `GetChain`, `GetNexus` |
| Blocks and transactions | `GetBlockByHash`, `GetLatestBlock`, `GetBlockTransactionCountByHashOnChain`, `GetTransactionByBlockHashAndIndexOnChain` |
| Contracts and organizations | `GetContracts`, `GetContractByName`, `GetContractByAddress`, `GetOrganization`, `GetOrganizationByName`, `GetOrganizations`, `GetLeaderboard` |
| Token definitions | `GetTokens`, `GetTokensByOwner`, `GetToken`, `GetTokenWithID`, `GetTokenData`, `GetTokenBalance` |
| Series and NFTs | `GetTokenSeries`, `GetTokenSeriesByID`, `GetTokenNFTs`, `GetTokenNFTsWithSeriesID`, `GetNFT`, `GetNFTs` |
| Account inventory | `GetAccountFungibleTokens`, `GetAccountNFTs`, `GetAccountOwnedTokens`, `GetAccountOwnedTokenSeries` and address-type variants |
| Archives and auctions | `GetArchive`, `ReadArchive`, `WriteArchive`, `WriteArchiveBase64`, `GetAuctionsCount`, `GetAuctions`, `GetAuction` |
| Broadcast | `SendRawTransaction`, `SendCarbonTransaction`, `SignAndSendTransaction`, `SignAndSendCarbonTransaction` |

## Cursor Pagination

```go
cursor := ""
for {
    page, err := client.GetTokenSeries(ctx, "MYNFT", 0, 100, cursor)
    if err != nil {
        return err
    }
    for _, series := range page.Result {
        fmt.Println(series.SeriesID, series.CarbonSeriesID)
    }
    if page.Cursor == "" {
        break
    }
    cursor = page.Cursor
}
```

Use cursor pagination for large Carbon token, series, NFT, and account
inventory reads. Numeric page/page-size pagination remains for endpoints such as
auctions and address transaction history.

## Broadcast

`SendRawTransaction` broadcasts signed classic VM transaction hex.
`SendCarbonTransaction` broadcasts signed Carbon transaction hex. Neither method
waits for final execution state; poll `GetTransaction(ctx, hash)` and check
`TransactionResult.StateIsSuccess()`.
