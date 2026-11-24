---
title: "Go SDK Carbon"
linkTitle: "Carbon"
weight: 50
---

A structured transaction carries a typed message, a `carbon.TxMsg`, that the
chain executes without a VM script. Transfers, mints and burns of tokens and
NFTs, and calls into the token module such as a token creation, use it. The
types and builders live in `github.com/phantasma-io/phantasma-sdk-go/pkg/carbon`.

A message goes through four steps: build, plan the fee, sign, send.
`PhantasmaRPC.SendTransaction` runs the last three.

## Workflow Guides

| Task | Page |
| ---- | ---- |
| Create a token and its series | [Token Deployment](token-deployment.md) |
| Mint NFTs | [NFT Minting](nft-minting.md) |
| Choose schemas, build metadata | [Schemas And Metadata](schemas-and-metadata.md) |
| Plan the fee, sign, send | [Fees And Broadcasting](fees-and-broadcasting.md) |
| Call a module method, decode a message | [Carbon Operations](carbon-operations.md) |
| Read the binary format | [Carbon API and Wire Format](reference/carbon-wire.md) |

## The Message

| `TxMsg` field | Meaning |
| ------------- | ------- |
| `Type` | The message type, a `TxType`. |
| `Expiry` | The last moment the chain accepts the message, in milliseconds since 1970. |
| `MaxGas` | The gas offer in KCAL atoms. A builder leaves it at `0`, which marks the message as not planned; planning sets it. |
| `MaxData` | The storage deposit ceiling in SOUL atoms. Planning sets it. |
| `GasFrom` | The 32-byte public key of the account that pays the gas. |
| `Payload` | A text the transaction carries, a `SmallString` of at most 255 bytes of UTF-8. |
| `Msg` | The body of the type, for example `*carbon.TxMsgTransferFungible`. |

Accounts are 32-byte public keys, `carbon.Bytes32`. See
[Keys And Addresses](keys-and-addresses.md) for the
conversions from key pairs and addresses.

## Native Builders

| Builder | Parameters | Message types |
| ------- | ---------- | ------------- |
| `BuildTransferFungibleTx(TransferFungibleParams)` | `From`, `To`, `TokenID`, `Amount` (`uint64` atoms), optional `GasPayer` | `TransferFungible`, `TransferFungibleGasPayer` |
| `BuildTransferNonFungibleTx(TransferNonFungibleParams)` | `From`, `To`, `TokenID`, `InstanceIDs`, optional `GasPayer` | `TransferNonFungibleSingle` for one instance, `TransferNonFungibleMulti` for several, and their gas-payer forms |
| `BuildMintFungibleTx(MintFungibleParams)` | `Owner`, `To`, `TokenID`, `Amount` (`IntX`) | `MintFungible` |
| `BuildBurnFungibleTx(BurnFungibleParams)` | `From`, `TokenID`, `Amount` (`IntX`), optional `GasPayer` | `BurnFungible`, `BurnFungibleGasPayer` |
| `BuildBurnNonFungibleTx(BurnNonFungibleParams)` | `From`, `TokenID`, `InstanceID`, optional `GasPayer` | `BurnNonFungible`, `BurnNonFungibleGasPayer` |

`BuildTransferNonFungibleTx` returns an error for an empty `InstanceIDs`; the
others return the message alone.

The account named in `From` or `Owner` signs. With `GasPayer` set, a second
account pays the gas and signs as well. Any holder can burn its own tokens.
Only the token owner can mint.

A transfer amount is a `uint64`, also for a big-fungible token, whose balances
can exceed that range. A larger amount moves with a script transfer, whose
amount is a big integer. Mints and burns carry an `IntX`:
`carbon.IntXFromInt64(n)` wraps an ordinary amount and `carbon.NewIntX(b)` a
`*big.Int`.

Every parameter struct embeds `TxLimits`: `MaxGas`, `MaxData` and `Expiry`.
Without `Expiry` the builder stamps `carbon.DefaultTxExpiry` (45 seconds) from
now; see [Expiry](fees-and-broadcasting.md#expiry) for a
longer lifetime.

## Example: Send NFTs, Burn Tokens

```go
package main

import (
    "context"
    "fmt"
    "log"
    "os"
    "time"

    "github.com/phantasma-io/phantasma-sdk-go/pkg/carbon"
    "github.com/phantasma-io/phantasma-sdk-go/pkg/cryptography"
    "github.com/phantasma-io/phantasma-sdk-go/pkg/rpc"
)

func main() {
    ctx, cancel := context.WithTimeout(context.Background(), 30*time.Second)
    defer cancel()

    owner, err := cryptography.FromWIF(os.Getenv("OWNER_WIF"))
    if err != nil {
        log.Fatal(err)
    }
    payer, err := cryptography.FromWIF(os.Getenv("PAYER_WIF"))
    if err != nil {
        log.Fatal(err)
    }
    to, err := carbon.Bytes32FromPhantasmaAddressText(os.Getenv("TO"))
    if err != nil {
        log.Fatal(err)
    }
    ownerKey, err := carbon.Bytes32FromPublicKey(owner.PublicKey())
    if err != nil {
        log.Fatal(err)
    }
    payerKey, err := carbon.Bytes32FromPublicKey(payer.PublicKey())
    if err != nil {
        log.Fatal(err)
    }

    client := rpc.NewRPCTestnet()

    // Two NFT instances of token 77 move to the receiver. The payer pays the gas.
    send, err := carbon.BuildTransferNonFungibleTx(carbon.TransferNonFungibleParams{
        From:        ownerKey,
        GasPayer:    payerKey,
        To:          to,
        TokenID:     77,
        InstanceIDs: []uint64{1001, 1002},
    })
    if err != nil {
        log.Fatal(err)
    }
    sendHash, err := client.SendTransaction(ctx, send, carbon.KeyPairSigners(owner, payer), rpc.SendTransactionOptions{})
    if err != nil {
        log.Fatal(err)
    }

    // The owner burns 5 whole SOUL, which has 8 decimals, and pays the gas itself.
    burn := carbon.BuildBurnFungibleTx(carbon.BurnFungibleParams{
        From:    ownerKey,
        TokenID: 2,
        Amount:  carbon.IntXFromInt64(5 * 100_000_000),
    })
    burnHash, err := client.SendTransaction(ctx, burn, carbon.KeyPairSigners(owner), rpc.SendTransactionOptions{})
    if err != nil {
        log.Fatal(err)
    }

    fmt.Println(sendHash, burnHash)
}
```

`SendTransaction` plans each message from the chain's current prices, signs it
with the given keys and sends it. It returns the transaction hash. Token `2` is
SOUL and token `1` is KCAL; other token ids come from `GetToken`, instance ids
from `GetAccountNFTs`.

## Token Module Builders

| Builder | Call | Result parser | Page |
| ------- | ---- | ------------- | ---- |
| `BuildCreateTokenTx(tokenInfo, creator, limits)` | `Token.CreateToken` | `ParseCreateTokenResult`: the token id | [Token Deployment](token-deployment.md) |
| `BuildCreateTokenSeriesTx(tokenID, seriesInfo, creator, limits)` | `Token.CreateTokenSeries` | `ParseCreateTokenSeriesResult`: the Carbon series id | [Token Deployment](token-deployment.md) |
| `BuildMintPhantasmaNonFungibleTx(tokenID, sender, receiver, tokens, limits)` | `Token.MintPhantasmaNonFungible` | `ParseMintPhantasmaNonFungibleResult`: the NFT ids and instance ids | [NFT Minting](nft-minting.md) |
| `BuildMintPhantasmaNonFungibleSingleTx(tokenID, seriesID, sender, receiver, rom, ram, limits)` | The same, for one NFT | The same | [NFT Minting](nft-minting.md) |

Each has two more forms for a process that signs without a client.
`...AndSign(..., signer, config, options)` plans the message against a gas
config, signs it with the one key pair and returns the signed bytes.
`...AndSignHex` returns them as hex. The signer is the creator or the sender.

## NFT Addresses And Instance Ids

| Function | Meaning |
| -------- | ------- |
| `GetNFTAddress(tokenID, instanceID)` | The address of one NFT instance. Assets sent to it belong to the NFT. |
| `UnpackNFTAddress(address)` | The token id and the instance id of an NFT address. |
| `IsNFTAddress(address)` | `true` for the form of an NFT address: fifteen zero bytes, a `0x01` byte, a non-zero token id and a non-zero instance id. |
| `UnpackNFTInstanceID(instanceID)` | The Carbon series id (low 32 bits) and the mint number (high 32 bits). |

A transfer into an NFT address needs the signature of the NFT's owner.

## Sign And Serialize

| Function | Does |
| -------- | ---- |
| `SignTxMsg(msg, keys...)` | Signs with in-memory key pairs and returns a `SignedTxMsg`. |
| `SignAndSerializeTxMsg(msg, keys...)`, `SignAndSerializeTxMsgHex(msg, keys...)` | The same, returned as bytes or hex. The hex goes to `SendCarbonTransaction`. |
| `SignTxMsgWith(ctx, msg, signers...)` | Signs with any `TxSigner`, for example a hardware wallet or a signing service. |
| `Serialize(blob)`, `Deserialize(data, blob)` | Writes and reads any Carbon structure, `TxMsg` and `SignedTxMsg` included. |

Signing refuses a message whose `MaxGas` is `0`: plan it first, or set the offer
deliberately. A native message fixes its own witnesses, and the keys must match
them exactly: a missing key or an extra key is an error. One account that pays
the gas and owns the tokens signs once. A `Call`, `CallMulti` or `Trade` takes
the witnesses in the order given, and the gas payer must be one of them.

## Related Pages

- [Fees And Broadcasting](fees-and-broadcasting.md)
- [Carbon Operations](carbon-operations.md)
- [Carbon API and Wire Format](reference/carbon-wire.md)
