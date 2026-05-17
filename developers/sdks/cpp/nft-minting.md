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

`MintNonFungibleTxHelper` mints one NFT and uses one-item mint gas.

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

This helper scales `maxGas` by `tokens.size()`. The public ROM must not contain
chain-owned `_i` or nested `rom` fields.

## Result Parsing

Use `MintNonFungibleTxHelper::ParseResult` for direct mints and
`MintPhantasmaNonFungibleTxHelper::ParseResult` for deterministic Phantasma NFT
mints.
