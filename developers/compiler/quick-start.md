# Quick Start

This page shows the shortest path from source file to compiled contract artifacts.

## 1. Install the compiler

The current `pha-tomb` NuGet tool package requires the .NET 10 SDK. Confirm that your shell selects a `10.x` SDK:

```bash
dotnet --version
```

Install `pha-tomb` as a .NET global tool:

```bash
dotnet tool install --global pha-tomb
# or update an existing install
dotnet tool update --global pha-tomb
```

Then confirm the binary is available:

```bash
pha-tomb --version
pha-tomb --help
```

If you prefer to build from source, see [Setup](setup.md).

## 2. Create a source file

Create a `.tomb` file, for example `my_contract.tomb`.

```csharp
contract my_contract {
    import Runtime;

    global owner: address;

    constructor(from: address) {
        owner = from;
    }

    public getOwner(): address {
        return owner;
    }
}
```

## 3. Compile it

`pha-tomb` expects the source file as the last argument. The command needs `pha-tomb` 2.2.1 or later.

```bash
pha-tomb output:./build debug nativecheck:error my_contract.tomb
```

This writes artifacts under:

```text
./build/Output/
```

Typical outputs:
- `my_contract.pvm`
- `my_contract.abi`
- optional `my_contract.debug`
- optional `my_contract.asm`

### The `protocol:` option

The compiler starts every constructor with a check: `Runtime.version()` must be at least the `protocol:` value. `Runtime.version()` returns the VM version, which is 1 on mainnet, testnet and devnet. The same value is `featureLevel` in the result of [`getPhantasmaVmConfig`](../rpc/methods.md#getphantasmavmconfig).

Since 2.2.1 the default value is 1, so leave the option out. A value above 1 makes every constructor fail at deploy.

Versions up to 2.2.0 use 19 by default. A contract with a constructor compiled by such a version fails at deploy with `Current nexus protocol version should be 19 or more`. With an older version, add `protocol:1` or update the tool with `dotnet tool update --global pha-tomb`.

The `protocol` field of an [RPC block](../rpc/models.md#blockresult) is a different number. It is 19 on current blocks.

## 4. Deploy it

After compilation, choose the correct deployment flow:

- standalone lowercase custom contract -> [pha-deploy contract deploy](../tools/pha-deploy.md)
- uppercase token-backed contract -> [pha-deploy --create-token](../tools/pha-deploy.md)
- attach VM code to an existing token -> [pha-deploy contract attach](../tools/pha-deploy.md)

## Next steps

- [Setup](setup.md)
- [Features](features.md)
- [Basics](basics/README.md)
- [Trigger examples](examples/trigger-examples.md)
