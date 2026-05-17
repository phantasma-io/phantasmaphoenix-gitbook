# C++ SDK Example: Offline Carbon Transaction

This example shows the Carbon builder shape. It signs locally and does not
broadcast.

```cpp
#include "PhantasmaAPI.h"
#include "Adapters/PhantasmaAPI_openssl.h"
#include "Cryptography/KeyPair.h"
#include "Carbon/Types.h"
#include "Carbon/Contracts/Token.h"
#include "Carbon/Tx.h"

int main() {
    auto keys = phantasma::PhantasmaKeys::Generate();

    phantasma::carbon::TokenInfo tokenInfo{};
    tokenInfo.symbol = phantasma::carbon::SmallString("MYNFT");
    tokenInfo.flags = phantasma::carbon::TokenFlags_NonFungible;
    tokenInfo.owner = phantasma::carbon::Bytes32(keys.PublicKeyBytes(), keys.PublicKeyLength());
    tokenInfo.maxSupply = phantasma::carbon::IntX(0);

    auto env = phantasma::carbon::CreateTokenTxHelper::BuildTx(tokenInfo, tokenInfo.owner);
    auto signedBytes = phantasma::carbon::SignAndSerialize(env, keys);

    return signedBytes.empty() ? 1 : 0;
}
```

Real token deployment must also provide token metadata and NFT schemas before
broadcasting.
