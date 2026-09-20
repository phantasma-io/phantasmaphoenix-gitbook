# C++ SDK NFT Minting

The C++ SDK exposes direct Carbon NFT minting and deterministic Phantasma NFT
minting.

## Direct Carbon NFT Mint

```cpp
using namespace phantasma::carbon;

ByteArray rom{/* serialized public ROM bytes */};
ByteArray ram;

auto env = MintNonFungibleTxHelper::BuildTx(
    carbonTokenId,
    carbonSeriesId,
    senderPublicKey,
    receiverPublicKey,
    rom,
    ram
);

auto signedBytes = SignAndSerialize(env, keys);
```

`MintNonFungibleTxHelper` mints one NFT. The chain refuses this operation where
governance has not allowed caller-supplied ROM ids, and that is the state of the
public chains today. The deterministic Phantasma mint below is the path those
chains take.

## Deterministic Phantasma NFT Mint

```cpp
std::vector<PhantasmaNftMintInfo> tokens;
tokens.push_back(PhantasmaNftMintInfo{
    phantasmaSeriesId,
    ByteView{publicRom.data(), publicRom.size()},
    ByteView{}
});

auto env = MintPhantasmaNonFungibleTxHelper::BuildTx(
    carbonTokenId,
    senderPublicKey,
    receiverPublicKey,
    tokens
);
```

The public ROM must not contain the chain-owned `_i` or nested `rom` fields.

The builders carry no prices. Plan the message against the chain's gas config
before signing it, or state the offer in `TxLimits`:

```cpp
FeePlanOptions options;
options.witnessCount = 1;
options.infusionsRead = true;
FeePlan plan;
if( !PlanFees(env.msg, config, options, plan) )
    return;

env.msg = plan.Apply(env.msg);
auto signedBytes = SignAndSerialize(env, keys);
```

A mint prices three facts the message does not carry: whether the recipient
already holds the token, whether the supply row still exists, and whether the
series mints duplicates. Each is taken at the reading that costs more. See
[Fees And Broadcasting](/developers/sdks/cpp/fees-and-broadcasting.md).

## Result Parsing

Use `MintNonFungibleTxHelper::ParseResult` for direct mints and
`MintPhantasmaNonFungibleTxHelper::ParseResult` for deterministic Phantasma NFT
mints.
