# C++ SDK Token Deployment

Use the Carbon token helpers when deploying native Carbon tokens. A typical NFT
token flow prepares token metadata, NFT schemas, `TokenInfo`, then a signed
create-token envelope.

## Create Token

```cpp
using namespace phantasma;
using namespace phantasma::carbon;

TokenInfo tokenInfo{};
tokenInfo.symbol = SmallString("MYNFT");
tokenInfo.flags = TokenFlags_NonFungible;
tokenInfo.decimals = 0;
tokenInfo.owner = Bytes32(keys.PublicKeyBytes(), keys.PublicKeyLength());
tokenInfo.maxSupply = IntX(0);
tokenInfo.metadata = ByteView{metadataBytes.data(), metadataBytes.size()};
tokenInfo.tokenSchemas = ByteView{schemaBytes.data(), schemaBytes.size()};

auto env = CreateTokenTxHelper::BuildTx(tokenInfo, tokenInfo.owner);
auto signedBytes = SignAndSerialize(env, keys);
```

The helper computes `maxGas` with `CreateTokenFeeOptions` and uses default
expiry when the caller passes `expiry = 0`.

## After Broadcast

Broadcast with `SendCarbonTransaction` and then read the final transaction. If
the transaction state is successful, parse the result:

```cpp
auto carbonTokenId = CreateTokenTxHelper::ParseResult(tx.result);
```

Keep the token symbol and Carbon token id together in application state. Later
RPC reads can use both values.
