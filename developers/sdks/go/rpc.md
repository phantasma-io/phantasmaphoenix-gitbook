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

`client.Call(ctx, method, params...)` calls a node method that has no typed
wrapper; see [Custom Calls](#custom-calls). The typed methods decode the answer
into the models of `pkg/rpc/response`.

For nodes that require an API key, use `rpc.NewRPCWithApiKey(endpoint, apiKey)`.
The key is sent in the `X-Api-Key` header on every request; an empty key behaves
like `NewRPC`.

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
info, err := client.GetAccountInfo(ctx, "P...")
tx, err := client.GetTransaction(ctx, "HASH")
tokens, err := client.GetTokens(ctx, true)
```

`GetAccountInfo` returns the account name and the staking info. Its cost does
not depend on how much the address holds, which makes it the call for a refresh
loop. `GetAccountInfos` answers up to 100 addresses in one call.

Read balances and NFTs through the cursor methods:

```go
balances, err := client.GetAccountFungibleTokens(ctx, "P...", "", 0, 100, "", false)
```

`GetAccount` and `GetAccounts` are deprecated. Their response embeds every NFT
id the address owns, so it grows with the size of the account. The node caps
each `Balances[].Ids` list at 10000 entries while `Balances[].Amount` keeps the
true count, so the list is silently partial for a large holder.

## Carbon And Current RPC Wrappers

The Go SDK exposes the same RPC methods as the other SDKs:

| Area | Methods |
| ---- | ------- |
| Build and chain config | `GetVersion`, `GetPhantasmaVMConfig`, `GetChains`, `GetChain`, `GetNexus`, `GetPlatforms` |
| Blocks and transactions | `GetBlockHeight`, `GetBlockByHeight`, `GetBlockByHash`, `GetLatestBlock`, `GetBlockTransactionCountByHashOnChain`, `GetTransactionByBlockHashAndIndexOnChain`, `GetTransaction`, `GetAddressTransactions`, `GetAddressTransactionCount` |
| Contracts and organizations | `GetContract`, `GetContracts`, `GetContractByName`, `GetContractByAddress`, `GetOrganization`, `GetOrganizations`, `GetOrganizationMembers`, `GetOrganizationMember`, `GetLeaderboard` |
| Scripts | `InvokeRawScript`; see [Read-Only Scripts](/developers/sdks/go/vm-and-transactions.md#read-only-scripts) |
| Token definitions | `GetTokens`, `GetTokensByOwner`, `GetToken`, `GetTokenWithID`, `GetTokenBalance`. `GetTokenData` is deprecated, and `GetNFT` covers it entirely |
| Series and NFTs | `GetTokenSeries`, `GetTokenSeriesByID`, `GetTokenNFTs`, `GetTokenNFTsWithSeriesID`, `GetNFT`, `GetNFTs` |
| Accounts | `GetAccountInfo`, `GetAccountInfos` and their address-type variants, `LookupName`. `GetAccount` and `GetAccounts` are deprecated |
| Account inventory | `GetAccountFungibleTokens`, `GetAccountNFTs`, `GetAccountOwnedTokens`, `GetAccountOwnedTokenSeries` and address-type variants |
| Fees | `GetGasConfig`, `EstimateTransaction`, `Fees()`, `ControlTokenID`, `InfusedAssets` |
| Archives and auctions | `GetArchive`, `ReadArchive`, `WriteArchive`, `WriteArchiveBase64`, `GetAuctionsCount`, `GetAuctions`, `GetAuction` |
| Broadcast | `SendTransaction`, `SendRawTransaction`, `SendCarbonTransaction`, `SignAndSendTransaction` |

`GetChains`, `GetChain`, `GetNexus`, `GetLeaderboard` and the archive methods
are stubs on the node: they answer an empty or default value. See
[Stubbed Node Methods](/developers/sdks/go/reference/rpc-methods.md#stubbed-node-methods).

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
    if page.Cursor == nil || *page.Cursor == "" {
        break
    }
    cursor = *page.Cursor
}
```

Use cursor pagination for large Carbon token, series, NFT, and account
inventory reads. Numeric page/page-size pagination remains for endpoints such as
auctions and address transaction history.

## Broadcast

`SendRawTransaction` broadcasts signed script transaction hex.
`SendCarbonTransaction` broadcasts signed Carbon transaction hex. Neither method
waits for final execution state; poll `GetTransaction(ctx, hash)` and check
`TransactionResult.StateIsSuccess()`.

## Transaction Events

`GetTransaction` returns the events of a transaction in `Events`, and
`GetBlockByHeight` the events of every transaction of a block. A fungible
transfer emits `TokenSend` for the sender and `TokenReceive` for the receiver:
`Address` names the account, and `Data` holds the symbol, the amount in atoms
and the chain name, in hex.

```go
package main

import (
    "encoding/hex"
    "fmt"
    "log"

    "github.com/phantasma-io/phantasma-sdk-go/pkg/domain/event"
    "github.com/phantasma-io/phantasma-sdk-go/pkg/io"
    "github.com/phantasma-io/phantasma-sdk-go/pkg/util"
)

func main() {
    // The Data of a TokenReceive event, as GetTransaction returns it.
    data, err := hex.DecodeString("044B43414C07005039278C0400046D61696E")
    if err != nil {
        log.Fatal(err)
    }
    transfer := io.Deserialize[*event.TokenEventData](data)

    fmt.Println(transfer.Symbol, transfer.ChainName)          // KCAL main
    fmt.Println(util.ConvertDecimals(transfer.Value, 10))     // 500, as KCAL has ten decimals
    fmt.Println(event.TokenReceive.String())                  // the Kind text of such an event
}
```

To watch an account for incoming transfers, read the height with
`GetBlockHeight`, read each new block with `GetBlockByHeight(ctx, "main",
height)`, skip the transactions whose `StateIsSuccess()` is `false`, and decode
the `TokenReceive` events whose `Address` is the account. The other event kinds
and their data types are in `github.com/phantasma-io/phantasma-sdk-go/pkg/domain/event`.

## Custom Calls

```go
response, err := client.Call(ctx, "getBlockHeight", "main")
if err != nil {
    return err
}
if response.Error != nil {
    return response.Error
}

var height string
if err := response.GetObject(&height); err != nil {
    return err
}
```

`Call` returns the raw `*jsonrpc.RPCResponse`. Its `GetObject`, `GetString`,
`GetInt`, `GetFloat` and `GetBool` decode the result.

## Errors

A node that refuses a request answers with a JSON-RPC error. The typed methods
return it as a `*jsonrpc.RPCError` whose text is `code: message`, for example
`-32603: Transaction not found`. `errors.As` tells such a refusal from a
transport failure:

```go
_, err := client.GetTransaction(ctx, txHash)
var rpcErr *jsonrpc.RPCError
if errors.As(err, &rpcErr) {
    fmt.Println("the node refused:", rpcErr.Code, rpcErr.Message)
}
```

`jsonrpc` is the package `github.com/phantasma-io/phantasma-sdk-go/pkg/jsonrpc`.

## Fee Planning And Sending

`SendTransaction` plans the fee, runs the token-creation pre-flight, signs with
every witness and broadcasts, all in one call.

{% content-ref url="/developers/sdks/go/fees-and-broadcasting.md" %}
[Fees And Broadcasting](/developers/sdks/go/fees-and-broadcasting.md)
{% endcontent-ref %}
