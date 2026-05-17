# C++ SDK Example: Read-Only RPC

```cpp
#include "Adapters/PhantasmaAPI_rapidjson.h"
#include "Adapters/PhantasmaAPI_curl.h"
#include "PhantasmaAPI.h"

int main() {
    phantasma::HttpClient http("http://localhost:5172/rpc");
    phantasma::rpc::PhantasmaAPI api(http);

    phantasma::rpc::PhantasmaError err{};
    auto height = api.GetBlockHeight("main", &err);
    if (err.code != 0) {
        return 1;
    }

    return height >= 0 ? 0 : 1;
}
```

Select the adapter stack that matches the application's HTTP and JSON
dependencies.
