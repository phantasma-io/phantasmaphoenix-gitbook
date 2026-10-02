# C++ SDK Example: Offline Carbon Transaction

This example shows the Carbon builder shape. It signs locally and does not
broadcast.

The builder carries no prices, so the message leaves it with a zero gas offer.
Signing needs the chain's prices, which means the offer has to be planned or set
by hand. The example sets it by hand through `TxLimits`, which is what an
offline signer does when it cannot read the chain.

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

    phantasma::carbon::TxLimits limits{};
    limits.maxGas = 50000000;   // 0.005 KCAL, stated because no chain is read here
    limits.maxData = 100000000; // storage escrow ceiling

    auto env = phantasma::carbon::CreateTokenTxHelper::BuildTx(tokenInfo, tokenInfo.owner, limits);
    auto signedBytes = phantasma::carbon::SignAndSerialize(env, keys);

    return signedBytes.empty() ? 1 : 0;
}
```

Real token deployment must also provide token metadata and NFT schemas before
broadcasting.

A stated offer that is short is rejected by the chain, and a token creation pays
its base policy fee before the symbol is checked. Plan the message against the
chain's gas config whenever a node can be reached. See
[Fees And Broadcasting](/developers/sdks/cpp/fees-and-broadcasting.md).
