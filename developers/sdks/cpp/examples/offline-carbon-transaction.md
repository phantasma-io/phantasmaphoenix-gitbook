# C++ SDK Example: Offline Carbon Transaction

This example builds an NFT token creation, plans its fee against the chain's
gas config, and signs it without sending it. The gas config is the only thing
read from a node; a signer without network access receives a copy of it.

```cpp
#define PHANTASMA_IMPLEMENTATION
#include "Adapters/PhantasmaAPI_rapidjson.h"
#include "Adapters/PhantasmaAPI_curl.h"
#include "PhantasmaAPI.h"
#include "Adapters/PhantasmaAPI_openssl.h"
#include "Numerics/Base16.h"
#include "Cryptography/KeyPair.h"
#include "Carbon/Carbon.h"
#include "Carbon/Tx.h"
#include "Carbon/Contracts/Token.h"
#include "Carbon/Contracts/TokenSchemas.h"
#include "Carbon/FeePlan.h"
#include <iostream>

using namespace phantasma;
using namespace phantasma::carbon;

int main()
{
    // The chain's prices. They change only through a governance resolution.
    HttpClient http("https://testnet.phantasma.info");
    rpc::PhantasmaAPI api(http);
    rpc::PhantasmaError err{};
    const Blockchain::GasConfig config = ToGasConfig(api.GetGasConfig(&err).gasConfig);
    if( err.code != 0 )
        return 1;

    PhantasmaKeys keys = PhantasmaKeys::Generate();
    const Bytes32 owner(keys.GetPublicKey());
    std::string error;

    ByteArray metadata;
    if( !TokenMetadataBuilder::BuildAndSerialize({
            { "name", "Example Art" },
            { "icon", "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mNkYAAAAAYAAjCB0C8AAAAASUVORK5CYII=" },
            { "url", "https://example.invalid/art" },
            { "description", "An example NFT collection" },
        }, metadata, error) )
        return 1;

    const TokenSchemasOwned schemas = TokenSchemasBuilder::PrepareStandardTokenSchemas();
    TokenInfoOwned info;
    if( !TokenInfoBuilder::Build("EXART", intx((int64_t)0), true, 0, owner, metadata, TokenSchemasBuilder::Serialize(schemas.View()), info, error) )
        return 1;

    TxEnvelope env = CreateTokenTxHelper::BuildTx(info.View(), owner);

    FeePlanOptions options;
    options.witnessCount = 1;
    options.infusionsRead = true; // nothing is burned
    FeePlan plan;
    if( !PlanFees(env.msg, config, options, plan) )
        return 1;
    env.msg = plan.Apply(env.msg);

    const ByteArray signedTx = SignAndSerialize(env, keys);
    std::cout << Base16::Encode(signedTx) << std::endl;
    return 0;
}
```

The plan covers the two policy fees of a token creation, which the chain takes
before it looks at the symbol. A signer that sends the result later skips the
symbol check of `SendTransaction`; run `PreflightTransaction` first. The
message expires 45 seconds after it was built unless `TxLimits::expiry` says
otherwise. See [Fees And Broadcasting](/developers/sdks/cpp/fees-and-broadcasting.md).
