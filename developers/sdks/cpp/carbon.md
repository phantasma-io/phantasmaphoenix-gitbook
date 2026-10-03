# C++ SDK Carbon

A structured transaction carries a typed message, a `Blockchain::TxMsg`, that
the chain executes without a VM script. Transfers, mints and burns of tokens
and NFTs, and calls into the token module such as a token creation, use it. The
types and builders live in the namespace `phantasma::carbon`, under
`include/Carbon/`.

A message goes through four steps: build, plan the fee, sign, send.
`SendTransaction` in `Carbon/Send.h` runs the last three.

## Workflow Guides

| Task | Page |
| ---- | ---- |
| Create a token and its series | [Token Deployment](/developers/sdks/cpp/token-deployment.md) |
| Mint NFTs | [NFT Minting](/developers/sdks/cpp/nft-minting.md) |
| Choose schemas, build metadata | [Schemas And Metadata](/developers/sdks/cpp/schemas-and-metadata.md) |
| Plan the fee, sign, send | [Fees And Broadcasting](/developers/sdks/cpp/fees-and-broadcasting.md) |
| Call a module method, read a message back | [Carbon Operations](/developers/sdks/cpp/carbon-operations.md) |

## Headers

| Header | Contents |
| ------ | -------- |
| `Carbon/Carbon.h`, `Carbon/Types.h` | Serialization primitives, `Bytes32`, `SmallString`, `intx`. |
| `Carbon/DataBlockchain.h` | `TxMsg`, the message bodies, `SignedTxMsg`, `TxMsgSigner`, `ParseTx`, `ParseSignedTx`. |
| `Carbon/Tx.h` | `TxLimits`, `NativeTxHelper`, the token module builders, `TxEnvelope`, `TokenHelper`, the result parsers. |
| `Carbon/Contracts/Token.h`, `Carbon/Contracts/TokenSchemas.h` | Token, series and NFT structures, and their builders. |
| `Carbon/PhantasmaAddress.h` | `FromPhantasmaAddress`, from a Phantasma address to a `Bytes32`. |
| `Carbon/FeePlan.h`, `Carbon/FeePlanSummary.h`, `Carbon/ChainFeePlan.h`, `Carbon/FeeInfusions.h` | Fee planning. |
| `Carbon/Preflight.h`, `Carbon/Send.h` | The symbol check of a token creation, and the one-call send. |

## The Message

| `TxMsg` field | Meaning |
| ------------- | ------- |
| `type` | The message type, a `TxTypes` value. |
| `expiry` | The last moment the chain accepts the message, in milliseconds since 1970. |
| `maxGas` | The gas offer in KCAL atoms. A builder leaves it at `0`, which marks the message as not planned; planning sets it. |
| `maxData` | The storage deposit ceiling in SOUL atoms. Planning sets it. |
| `gasFrom` | The 32-byte public key of the account that pays the gas. |
| `payload` | A text the transaction carries, a `SmallString` of at most 255 bytes. |
| The body | One member per type, for example `transferFt`, `burnFungible` or `call`. |

Accounts are 32-byte public keys: `carbon::Bytes32(keys.GetPublicKey())` for a
key pair, `carbon::FromPhantasmaAddress(address)` for a parsed address.

## Native Builders

`NativeTxHelper` builds the native types. Each builder takes the parties, the
token and the amount or instances, and optional `TxLimits`:

| Builder | Parameters | Message types |
| ------- | ---------- | ------------- |
| `TransferFungible(parties, to, tokenId, amount)` | `amount` in atoms, a `uint64_t` | `TransferFungible`, `TransferFungible_GasPayer` |
| `TransferNonFungible(parties, to, tokenId, instanceIds, count, out, outError)` | Answers `false` for an empty list | `TransferNonFungible_Single` for one instance, `TransferNonFungible_Multi` for several, and their `_GasPayer` forms |
| `MintFungible(owner, to, tokenId, amount)` | `amount` an `intx` | `MintFungible` |
| `BurnFungible(parties, tokenId, amount)` | `amount` an `intx` | `BurnFungible`, `BurnFungible_GasPayer` |
| `BurnNonFungible(parties, tokenId, instanceId)` | | `BurnNonFungible`, `BurnNonFungible_GasPayer` |

`parties` is `{ from }`, or `{ from, &gasPayer }` for a second account that
pays the gas and signs as well. The account in `from` or `owner` signs. Any
holder can burn its own tokens; only the token owner can mint. The
`instanceIds` array of `TransferNonFungible` must outlive the message, which
points at it.

A transfer amount is a `uint64_t`, also for a big-fungible token. Only an amount
above that range needs a module call or a script transfer, whose amounts are
big integers. Mints and burns carry an `intx` because they also serve
big-fungible tokens.

`TxLimits` holds `maxGas`, `maxData` and `expiry`. Without `expiry` a builder
stamps `DefaultExpiryMs` (45 seconds) from now; `ExpiryWithin(windowMs)` gives
the latest expiry the chain accepts.

## Example: Send NFTs With A Gas Payer

```cpp
using namespace phantasma::carbon;

const Bytes32 from(ownerKeys.GetPublicKey());
const Bytes32 payer(gasPayerKeys.GetPublicKey());
const uint64_t instanceIds[] = { 1001, 1002 };

// Two NFT instances of token 77 move to the recipient. The payer pays the gas.
Blockchain::TxMsg send;
std::string error;
if( !NativeTxHelper::TransferNonFungible({ from, &payer }, recipient, 77, instanceIds, 2, send, error) )
    return; // error says why

String hash;
if( !SendTransaction(api, send, { &gasPayerKeys, &ownerKeys }, config, SendOptions{}, hash, error) )
    return;
```

`SendTransaction` plans the message against `config`, the chain's gas config,
signs it with the given keys and sends it. A `_GasPayer` message is signed by
the gas payer first, then by the owner. `config` comes from
`ToGasConfig(api.GetGasConfig().gasConfig)`; it changes only through a
governance resolution, so read it once and keep it.

## Token Module Builders

| Builder | Call | Result parser | Page |
| ------- | ---- | ------------- | ---- |
| `CreateTokenTxHelper::BuildTx(tokenInfo, creator, limits)` | `Token.CreateToken` | `CreateTokenTxHelper::ParseResult`: the token id | [Token Deployment](/developers/sdks/cpp/token-deployment.md) |
| `CreateTokenSeriesTxHelper::BuildTx(tokenId, seriesInfo, creator, limits)` | `Token.CreateTokenSeries` | `CreateTokenSeriesTxHelper::ParseResult`: the Carbon series id | [Token Deployment](/developers/sdks/cpp/token-deployment.md) |
| `MintPhantasmaNonFungibleTxHelper::BuildTx(tokenId, sender, receiver, tokens, out, outError, limits)` | `Token.MintPhantasmaNonFungible` | `MintPhantasmaNonFungibleTxHelper::ParseResult`: the NFT ids and instance ids | [NFT Minting](/developers/sdks/cpp/nft-minting.md) |
| `MintNonFungibleTxHelper::BuildTx(...)` | A direct `MintNonFungible` | `MintNonFungibleTxHelper::ParseResult`: NFT addresses | Refused by the chain while caller-chosen NFT ids are disabled, as on mainnet |

These builders return a `TxEnvelope`: the message in `msg` and, in `buffers`,
the bytes the message points into. Move an envelope; do not copy it, because a
copy's message still points into the original's buffers.

## Signing

| Function | Does |
| -------- | ---- |
| `SignAndSerialize(env, keys)` | Signs an envelope with one key and returns the signed bytes. |
| `Blockchain::TxMsgSigner::SignAndSerialize(msg, keys)` | The same for a message. |
| `Blockchain::TxMsgSigner::SignAndSerialize(msg, signers, out, outError)` | Signs with several keys. It answers `false` when the count is not the one the type fixes, or when a key is not the account the message names. |

The signing functions do not check the gas offer: plan the message before
signing it, or the chain rejects the zero offer. A `Call`, `CallMulti` or
`Trade` takes its witnesses in the order given, and the gas payer must be one of
them.

`Base16::Encode(signedBytes)` gives the hex that `api.SendCarbonTransaction`
takes.

## NFT Addresses And Instance Ids

| Function | Meaning |
| -------- | ------- |
| `TokenHelper::GetNftAddress(tokenId, instanceId)` | The address of one NFT instance. Assets sent to it belong to the NFT. |
| `TokenHelper::IsNftAddress(address)` | `true` for the form of an NFT address: fifteen zero bytes, a `0x01` byte, a non-zero token id and a non-zero instance id. |

An instance id holds the Carbon series id in its low 32 bits and the mint number
in its high 32 bits. A transfer into an NFT address needs the signature of the
NFT's owner.

## Related Pages

{% content-ref url="/developers/sdks/cpp/fees-and-broadcasting.md" %}
[Fees And Broadcasting](/developers/sdks/cpp/fees-and-broadcasting.md)
{% endcontent-ref %}

{% content-ref url="/developers/sdks/cpp/carbon-operations.md" %}
[Carbon Operations](/developers/sdks/cpp/carbon-operations.md)
{% endcontent-ref %}

{% content-ref url="/developers/sdks/cpp/reference/carbon-wire.md" %}
[Carbon API and Wire Format](/developers/sdks/cpp/reference/carbon-wire.md)
{% endcontent-ref %}
