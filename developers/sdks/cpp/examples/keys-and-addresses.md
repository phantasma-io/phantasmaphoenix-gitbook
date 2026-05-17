# C++ SDK Example: Keys And Addresses

```cpp
#include "PhantasmaAPI.h"
#include "Adapters/PhantasmaAPI_openssl.h"
#include "Cryptography/KeyPair.h"

int main() {
    auto keys = phantasma::PhantasmaKeys::Generate();
    auto address = keys.GetAddress();
    auto wif = keys.ToWIF();

    auto imported = phantasma::PhantasmaKeys::FromWIF(wif);

    bool parseError = false;
    auto parsed = phantasma::Address::FromText(address.Text(), &parseError);
    if (parseError || parsed != imported.GetAddress()) {
        return 1;
    }

    return 0;
}
```

Store WIF values as secrets. The example round-trips WIF only to show the API
shape.
