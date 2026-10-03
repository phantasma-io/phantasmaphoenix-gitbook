# Go SDK Carbon Operations

The builders on [Carbon](/developers/sdks/go/carbon.md) cover transfers, mints,
burns, token and series creation, and NFT mints. Every other module method is
called with a `Call` message: a module id, a method id and the serialized
arguments.

## Builders Or A Call

| Need | Use |
| ---- | --- |
| A transfer, mint or burn | The native builders on [Carbon](/developers/sdks/go/carbon.md#native-builders). |
| A token, a series, an NFT mint | The token module builders on [Carbon](/developers/sdks/go/carbon.md#token-module-builders). |
| Any other module method | A `TxMsgCall` with typed arguments. |
| Several calls in one transaction | A `TxMsgCallMulti`. |
| Tokens moving between several accounts at once | A `TxMsgTrade`. |

## A Module Call

A structured transfer carries a `uint64` amount. A big-fungible token can hold
more than that, and such an amount moves with the token module's own
`TransferFungible` method, whose amount is an `IntX`:

```go
// 10^23 atoms, above the uint64 range.
amount, _ := new(big.Int).SetString("100000000000000000000000", 10)

args := carbon.Serialize(&carbon.TransferFungibleArgs{
    To:      receiver,
    From:    sender,
    TokenID: carbonTokenID,
    Amount:  carbon.NewIntX(amount),
})

msg := carbon.TxMsg{
    Type:    carbon.TxTypeCall,
    Expiry:  carbon.DefaultExpiry(),
    GasFrom: sender,
    Msg: &carbon.TxMsgCall{
        ModuleID: uint32(carbon.ModuleIDToken),
        MethodID: uint32(carbon.TokenMethodTransferFungible),
        Args:     args,
    },
}

// The message carries no prices. SendTransaction plans it, signs it and sends it.
hash, err := client.SendTransaction(ctx, msg, carbon.KeyPairSigners(keys), rpc.SendTransactionOptions{})
```

`sender` is the public key of `keys` as a `carbon.Bytes32`. A `Call` takes its
witnesses from the keys it is signed with, in that order, and the gas payer
must be one of them. Each witness adds 96 bytes the chain bills, so planning a
`Call` by hand needs `FeePlanOptions.WitnessCount`; `SendTransaction` fills it
in from the signers.

## Token Module Methods

`ModuleIDToken` (1). The method ids are the `TokenMethod...` constants.

| Method | Arguments | Signed by |
| ------ | --------- | --------- |
| `TransferFungible` | `TransferFungibleArgs` | `From`. |
| `TransferNonFungible` | `TransferNonFungibleArgs` | `From`. |
| `CreateToken` | `TokenInfo` | The owner; see [Token Deployment](/developers/sdks/go/token-deployment.md). |
| `MintFungible` | `MintFungibleArgs` | The token owner. |
| `BurnFungible` | `BurnFungibleArgs` | `From`. |
| `CreateTokenSeries` | `CreateTokenSeriesArgs` | The token owner. |
| `MintPhantasmaNonFungible` | `MintPhantasmaNonFungibleArgs` | The series owner; see [NFT Minting](/developers/sdks/go/nft-minting.md). |
| `BurnNonFungible` | `BurnNonFungibleArgs` | `From`, who owns the instances. |
| `UpdateTokenMetadata` | `UpdateTokenMetadataArgs` | The token owner. The fields given replace the fields of the same name or are added; the chain checks the result. |
| `UpdateSeriesMetadata` | `UpdateSeriesMetadataArgs` | The series owner. The bytes replace the series metadata; build them with `BuildTokenSeriesMetadata` for the same series id. |
| `DeleteTokenSeries` | The token id (`uint64`) and the Carbon series id (`uint32`), written with `carbon.NewWriter` | The token owner or the series owner, once no NFT of the series exists. |
| `ApplyInflation` | The token id (`uint64`) | Anyone. It mints the token's scheduled inflation when a period is due. |
| `MintNonFungible`, `CreateMintedTokenSeries` | `MintNonFungibleArgs`, `CreateMintedTokenSeriesArgs` | Refused: both take an NFT id chosen by the caller, which the token configuration disables. |
| `SetTokensConfig` | `TokensConfig` | Governance only. |

The remaining method ids, `GetBalance`, `GetBalances`, `GetInstances`,
`GetTokenInfo`, `GetTokenInfoBySymbol`, `GetTokenIDBySymbol`,
`GetTokenSupply`, `GetSeriesInfo`, `GetSeriesInfoByMetaID`,
`GetSeriesSupply`, `GetNonFungibleInfo`, `GetNonFungibleInfoByRomID` and
`GetNextTokenInflation`, read state. The RPC methods on
[RPC](/developers/sdks/go/rpc.md) return the same data without a transaction.

## Market Module Methods

`ModuleIDMarket` (4). The method ids are the `MarketMethod...` constants. A
listing sells one NFT for a fungible token at a fixed price.

| Method | Arguments | Rules |
| ------ | --------- | ----- |
| `SellToken`, `SellTokenByID` | `MarketSellTokenArgs`, `MarketSellTokenByIDArgs` | Signed by the NFT owner, `From`. The NFT moves to the market module until it is bought or the listing is cancelled. The quote token must be fungible, `EndDate`, in milliseconds, in the future, and the price not negative; with the `PriceRequired` rule, above zero. |
| `BuyToken`, `BuyTokenByID` | `MarketBuyTokenArgs`, `MarketBuyTokenByIDArgs` | Signed by the buyer, `From`, who pays the price in the quote token. Without the `CanPurchaseLate` rule, only before the end date. |
| `CancelSale`, `CancelSaleByID` | `MarketCancelSaleArgs`, `MarketCancelSaleByIDArgs` | Without the `CanCancelEarly` rule, only after the end date. Signed by the seller, or by anyone once the delisting grace after the end date has passed. The NFT returns to the seller. |
| `GetTokenListingCount`, `GetTokenListingInfo`, `GetTokenListingInfoByID` | The `MarketGet...Args` structs | Read state. |

The plain forms name the NFT by token id and instance id. The `ByID` forms name
it by token symbol and Phantasma NFT id, and the quote token by symbol.

With the `EnforceRoyalties` rule, a sale pays up to three royalties out of the
price, at 10,000,000 per 1%:

1. The `royalties` value of the token metadata, to the token owner.
2. The `royalties` value of the series metadata, to the series owner.
3. The `royalties` value of the NFT's ROM, to the account the NFT was minted to.

Each is a share of what remains of the price after the ones before it. The
seller receives the rest.

`MarketConfig` holds the rules. The chain's defaults, which
`DefaultMarketConfig()` copies, turn on `PriceRequired` and `EnforceRoyalties`
and set a delisting grace of one day. Only governance changes them. The listing
time fields of the configuration are not checked when a listing is made.

## Governance Module Methods

`ModuleIDGovernance` (0). The SDK names two methods:

| Method | Arguments | Rules |
| ------ | --------- | ----- |
| `GovernanceMethodRegisterName` | `RegisterNameArgs`: `Address`, `Name` | Signed by `Address`. One name per address, at most `maxNameLength` characters, lowercase ASCII letters, digits and `_`. The fee is `policyFeeRegisterName` halved for every character after the first, so short names cost more. A registered name cannot be removed. |
| `GovernanceMethodSetGasConfig` | `GasConfig` | Governance only. |

## Several Calls In One Transaction

A `TxMsgCallMulti` runs its `Calls` in order, in one transaction: they all
complete or none does. An argument of a later call can be the result of an
earlier one. `TxMsgCall.Sections` then replaces `Args`: each
`CallArgSection` holds either bytes or a negative `RegisterOffset`, and `-1`
means the result of the call before. The sections are joined into the
arguments.

## Trades

A `TxMsgTrade` moves tokens of several accounts in one transaction: fungible
mints, NFT mints, fungible transfers, NFT transfers, fungible burns and NFT
burns, run in that order. Each entry names its own `From`, and every such
account signs. Two accounts can swap tokens this way without trusting each
other. NFT mints in a trade take an NFT id chosen by the caller and are refused.

## Read A Signed Transaction Back

```go
data, err := carbon.DecodeHex(signedTxHex)
if err != nil {
    return err
}

signed, err := carbon.Deserialize(data, &carbon.SignedTxMsg{})
if err != nil {
    return err
}

fmt.Println(signed.Msg.Type, signed.Msg.MaxGas, len(signed.Witnesses))
```

`Deserialize` refuses bytes that are cut short or carry extra bytes at the end.
`carbon.Serialize(signed)` writes the same bytes again. A service that receives
a signed transaction from a wallet can check the type, the gas offer and the
witnesses this way before it sends the transaction.

## Configuration Structures

`ChainConfig`, `GasConfig`, `TokensConfig` and `MarketConfig` are the wire forms
of the chain's settings. They serialize like any other Carbon structure, and
only governance can change them. Read the gas configuration with
`client.GetGasConfig(ctx)` and convert it with `ToGasConfig()`; see
[Fees And Broadcasting](/developers/sdks/go/fees-and-broadcasting.md).

## Result Parsers

`ParseCreateTokenResult`, `ParseCreateTokenSeriesResult` and
`ParseMintPhantasmaNonFungibleResult` read the results of the token module
builders. `ParseMintNonFungibleResult` reads the result of a `MintNonFungible`
call. For any other method, read `TransactionResult.Result` with
`carbon.NewReader(data)` in the layout the method writes; a call that writes
nothing returns an empty result.

## Related Pages

{% content-ref url="/developers/sdks/go/carbon.md" %}
[Carbon](/developers/sdks/go/carbon.md)
{% endcontent-ref %}

{% content-ref url="/developers/sdks/go/fees-and-broadcasting.md" %}
[Fees And Broadcasting](/developers/sdks/go/fees-and-broadcasting.md)
{% endcontent-ref %}

{% content-ref url="/developers/sdks/go/reference/carbon-wire.md" %}
[Carbon API and Wire Format](/developers/sdks/go/reference/carbon-wire.md)
{% endcontent-ref %}
