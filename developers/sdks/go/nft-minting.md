# Go SDK NFT Minting

An NFT is minted into a series of an NFT token. The token and the series come
first; see [Token Deployment](/developers/sdks/go/token-deployment.md). One
`Token.MintPhantasmaNonFungible` call mints one or more instances for one
recipient, and the chain derives the id of each NFT. The builders live in
`github.com/phantasma-io/phantasma-sdk-go/pkg/carbon`.

## Required Inputs

| Input | Where it comes from |
| ----- | ------------------- |
| The token id | `ParseCreateTokenResult` after the token creation, or `CarbonID` of `GetToken`. |
| The series id | The id the series was created with, a `*big.Int`. Not the Carbon series id. |
| The ROM schema | The one the token was created with. |
| The series owner's key | It signs the mint and pays the gas. |
| The recipient | A `carbon.Bytes32`, for example from `Bytes32FromPhantasmaAddressText`. |

## Build The ROM

The ROM is the read-only data of an NFT. `BuildPhantasmaNFTRom(romSchema, fields)`
writes one value for every field of the token's ROM schema and checks each
value against the field's type; see
[NFT ROM](/developers/sdks/go/schemas-and-metadata.md#nft-rom). With the standard
schemas, the ROM carries the five standard fields:

| Field | Type | Meaning |
| ----- | ---- | ------- |
| `name` | `string` | The name of the NFT. |
| `description` | `string` | Its description. |
| `imageURL` | `string` | The URL of the image. |
| `infoURL` | `string` | A page about the NFT. |
| `royalties` | `int32` | The royalty a sale on the chain market pays to the account the NFT was minted to, in units of 10,000,000 per 1%. |

In a series with `mode` `0`, the chain derives the NFT id from the ROM, so two
NFTs of one token with the same ROM cannot both exist: the second mint fails
with `token ID already in use`. Give every NFT something of its own, such as its
name or number. In a series whose NFTs share one ROM (`mode` `1`), the id also
covers the mint number.

## Mint

```go
package main

import (
    "context"
    "fmt"
    "log"
    "math/big"
    "os"
    "strconv"
    "time"

    "github.com/phantasma-io/phantasma-sdk-go/pkg/carbon"
    "github.com/phantasma-io/phantasma-sdk-go/pkg/cryptography"
    "github.com/phantasma-io/phantasma-sdk-go/pkg/rpc"
)

func main() {
    ctx, cancel := context.WithTimeout(context.Background(), 30*time.Second)
    defer cancel()

    keys, err := cryptography.FromWIF(os.Getenv("WIF"))
    if err != nil {
        log.Fatal(err)
    }
    sender, err := carbon.Bytes32FromPublicKey(keys.PublicKey())
    if err != nil {
        log.Fatal(err)
    }
    receiver, err := carbon.Bytes32FromPhantasmaAddressText(os.Getenv("TO"))
    if err != nil {
        log.Fatal(err)
    }
    tokenID, err := strconv.ParseUint(os.Getenv("TOKEN_ID"), 10, 64) // from ParseCreateTokenResult
    if err != nil {
        log.Fatal(err)
    }
    seriesID, ok := new(big.Int).SetString(os.Getenv("SERIES_ID"), 10) // the id the series was created with
    if !ok {
        log.Fatal("SERIES_ID is not a number")
    }

    // The ROM schema the token was created with.
    schemas := carbon.PrepareStandardTokenSchemas(false)
    rom, err := carbon.BuildPhantasmaNFTRom(schemas.ROM, []carbon.MetadataField{
        {Name: "name", Value: "Example NFT #1"},
        {Name: "description", Value: "The first example NFT"},
        {Name: "imageURL", Value: "https://example.invalid/nft/1.png"},
        {Name: "infoURL", Value: "https://example.invalid/nft/1"},
        {Name: "royalties", Value: int32(50_000_000)}, // 5%
    })
    if err != nil {
        log.Fatal(err)
    }

    msg, err := carbon.BuildMintPhantasmaNonFungibleSingleTx(tokenID, seriesID, sender, receiver, rom, nil, carbon.TxLimits{})
    if err != nil {
        log.Fatal(err)
    }

    client := rpc.NewRPCTestnet()
    hash, err := client.SendTransaction(ctx, msg, carbon.KeyPairSigners(keys), rpc.SendTransactionOptions{})
    if err != nil {
        log.Fatal(err)
    }
    fmt.Println(hash)
}
```

`sender` pays the gas and signs; it must be the series owner. The last two
arguments before the limits are the ROM and the RAM; `nil` gives an empty RAM,
which the standard schemas expect.

The mint fee depends on three facts the message does not carry: whether the
recipient already holds the token, whether the supply row still exists, and
whether the series mints duplicates. `SendTransaction` plans each at the
reading that costs more, so the offer can exceed the bill; the rest returns.
See [Stating A Fact](/developers/sdks/go/fees-and-broadcasting.md#stating-a-fact).

## Several NFTs In One Call

`BuildMintPhantasmaNonFungibleTx(tokenID, sender, receiver, tokens, limits)`
takes one `PhantasmaNFTMintInfo` per instance. The entries may name different
series of the same token; every instance goes to the one recipient.

```go
tokens := []carbon.PhantasmaNFTMintInfo{
    {PhantasmaSeriesID: carbon.NewIntX(big.NewInt(1)), ROM: romOne},
    {PhantasmaSeriesID: carbon.NewIntX(big.NewInt(1)), ROM: romTwo},
    {PhantasmaSeriesID: carbon.NewIntX(big.NewInt(2)), ROM: romThree},
}

msg, err := carbon.BuildMintPhantasmaNonFungibleTx(tokenID, sender, receiver, tokens, carbon.TxLimits{})
```

An empty `tokens` slice returns an error. A `nil` `RAM` is written as empty.

## Mint Without A Client

The `...AndSign` forms plan the message against a gas config the caller
supplies, sign it with the one key, and return the signed transaction:

```go
gasConfig, err := client.GetGasConfig(ctx)
if err != nil {
    return err
}
config, err := gasConfig.ToGasConfig()
if err != nil {
    return err
}

signedTxHex, err := carbon.BuildMintPhantasmaNonFungibleSingleTxAndSignHex(
    tokenID,
    seriesID,
    keys, // the series owner
    receiver,
    rom,
    nil, // RAM
    &config,
    carbon.PlanAndSignOptions{},
)
```

`BuildMintPhantasmaNonFungibleTxAndSignHex` does the same for several entries.
`client.SendCarbonTransaction(ctx, signedTxHex)` sends the result.

## Parse The Result

After the transaction is in a block, its result names every minted instance:

```go
tx, err := waitForTransaction(ctx, client, hash)
if err != nil {
    return err
}
if !tx.StateIsSuccess() {
    return fmt.Errorf("mint failed: %s", tx.State)
}

minted, err := carbon.ParseMintPhantasmaNonFungibleResult(tx.Result)
if err != nil {
    return err
}
for _, m := range minted {
    // The NFT id is stored little-endian; RPC methods take it as a decimal number.
    idBytes := m.PhantasmaNFTID.Bytes()
    slices.Reverse(idBytes)
    nftID := new(big.Int).SetBytes(idBytes)

    carbonSeriesID, mintNumber := carbon.UnpackNFTInstanceID(m.CarbonInstanceID)
    fmt.Println(nftID, m.CarbonInstanceID, carbonSeriesID, mintNumber)
}
```

`waitForTransaction` is the polling function from
[VM And Transactions](/developers/sdks/go/vm-and-transactions.md#the-result-of-a-transaction).
`PhantasmaNFTID` is the 256-bit id the chain derived for the NFT; `GetNFT` and
the script interops such as `Runtime.TransferToken` name the NFT by it.
`CarbonInstanceID` is the id that structured transfers and burns take, for
example `TransferNonFungibleParams.InstanceIDs`.

## Read NFTs Back

| Call | Returns |
| ---- | ------- |
| `GetTokenNFTs(ctx, tokenID, carbonSeriesID, pageSize, cursor, extended)` | The NFTs of a token, or of one series when `carbonSeriesID` is not `0`, page by page. |
| `GetAccountNFTs(ctx, account, symbol, tokenID, carbonSeriesID, pageSize, cursor, extended, checkAddressReservedByte)` | The NFTs an account holds. |
| `GetNFT(ctx, symbol, nftID, extended)` | One NFT by its id in decimal text. |
| `GetNFTs(ctx, symbol, nftIDs, extended)` | Several NFTs by id. |

The paged calls return a `response.CursorPaginatedResult`: pass `*page.Cursor`
back to read the next page, until it is `nil` or empty. With `extended` set, a
page holds at most 50 entries, otherwise 100.

## Related Pages

{% content-ref url="/developers/sdks/go/token-deployment.md" %}
[Token Deployment](/developers/sdks/go/token-deployment.md)
{% endcontent-ref %}

{% content-ref url="/developers/sdks/go/schemas-and-metadata.md" %}
[Schemas And Metadata](/developers/sdks/go/schemas-and-metadata.md)
{% endcontent-ref %}

{% content-ref url="/developers/sdks/go/carbon.md" %}
[Carbon](/developers/sdks/go/carbon.md)
{% endcontent-ref %}
