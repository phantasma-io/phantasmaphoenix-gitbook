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

// The builder carries no prices. Plan the message, then sign it.
const Blockchain::GasConfig config = ToGasConfig(api.GetGasConfig().gasConfig);
FeePlanOptions options;
options.witnessCount = 1;
options.infusionsRead = true;
FeePlan plan;
if( !PlanFees(env.msg, config, options, plan) )
    return;

env.msg = plan.Apply(env.msg);
auto signedBytes = SignAndSerialize(env, keys);
```

`SendTransaction` in `Carbon/Send.h` does the whole flow instead: it checks the
symbol, plans the fee, signs and broadcasts.

{% hint style="warning" %}
`Token.CreateToken` pays its policy fee before the contract looks at the symbol,
and that fee is the largest single price in the protocol. A symbol that is
already taken costs the fee and returns nothing. `PreflightTransaction` asks the
chain first. See
[Fees And Broadcasting](/developers/sdks/cpp/fees-and-broadcasting.md).
{% endhint %}

## After Broadcast

Broadcast with `SendCarbonTransaction` and then read the final transaction. If
the transaction state is successful, parse the result:

```cpp
auto carbonTokenId = CreateTokenTxHelper::ParseResult(tx.result);
```

Keep the token symbol and Carbon token id together in application state. Later
RPC reads can use both values.
