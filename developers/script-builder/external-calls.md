# External Calls

Script Builder reaches native chain functionality through VM interop calls. In bytecode terms this is the same `EXTCALL` mechanism documented in the VM section, but from a developer point of view it is easier to think of these as named external methods such as:

- `Runtime.TransferTokens`
- `Runtime.MintToken`
- `Nexus.CreateToken`
- `Data.Get`
- `Map.Set`

The authoritative behavior is documented in the VM interop reference:

- [../blockchain/chain/information/virtual-machine/interop.md](../blockchain/chain/information/virtual-machine/interop.md)

This page focuses on how to use that surface from script-building code.

## How External Calls Work

At a high level, a script:

1. pushes arguments to the VM stack
2. pushes the interop method name
3. executes `EXTCALL`

If you are using a helper library or Script Builder abstraction, it usually hides the raw stack manipulation and gives you a direct helper such as `CallInterop("Runtime.TransferTokens", ...)`.

## Interop Namespaces You Can Rely On Today

The current Carbon validator supports useful working surfaces in these namespaces:

- `Runtime.*`
  - context helpers, logging, token operations, NFT operations, contract deploy and upgrade
- `Nexus.*`
  - token-backed create, token-backed attach, token series creation
- `Data.*`
  - scalar contract storage
- `Map.*`
  - map-like contract storage
- `List.*`
  - list-like contract storage
- `Account.Name`
  - governance name lookup
- constructors
  - `Address()`, `Hash()`, `Timestamp()`

## Important Working Flows

### Standalone custom contract lifecycle

- `Runtime.DeployContract(from, contractName, script, abi)`
- `Runtime.UpgradeContract(from, contractName, script, abi)`

Use lowercase custom contract names for these flows.

### Token-backed contract lifecycle

- `Nexus.CreateToken(from, script, abi)`
- `Nexus.AttachTokenContract(from, symbol, script, abi)`
- `Runtime.UpgradeContract(from, contractName, script, abi)`

Use these for uppercase token symbols. Do not try to deploy an uppercase token-backed contract through `Runtime.DeployContract`.

### Fungible token operations

- `Runtime.GetBalance`
- `Runtime.TransferTokens`
- `Runtime.TransferBalance`
- `Runtime.MintTokens`
- `Runtime.BurnTokens`

### NFT operations

- `Runtime.GetOwnerships`
- `Runtime.TransferToken`
- `Runtime.MintToken`
- `Runtime.BurnToken`
- `Runtime.InfuseToken`
- `Runtime.ReadToken`
- `Runtime.ReadTokenROM`
- `Runtime.ReadTokenRAM`
- `Runtime.ReadInfusions`
- `Nexus.CreateTokenSeries`

### Contract storage

- `Data.Get`, `Data.Set`, `Data.Delete`
- `Map.Has`, `Map.Get`, `Map.Set`, `Map.Remove`, `Map.Count`, `Map.Clear`, `Map.Keys`
- `List.Get`, `List.Add`, `List.Replace`, `List.RemoveAt`, `List.Count`, `List.Clear`

## Methods That Still Exist In Old Tables But Are Not Ready

Do not write new examples around these yet:

- `Runtime.KillContract`
- `Runtime.SwapTokens`
- `Runtime.WriteToken`
- `Runtime.AESDecrypt`
- `Runtime.AESEncrypt`
- `Organization.*`
- `Oracle.*`
- `Task.*`
- several older `Nexus.*` names such as `CreateChain` and `CreateOrganization`

## Practical Advice

- Use the VM interop reference for exact current behavior.
- If you are building deployment tooling, prefer `pha-deploy` or the Token Deployment UI instead of hand-authoring raw lifecycle scripts unless you actually need low-level control.
- When you do write raw scripts, separate standalone contract flows from token-backed flows in your own code and documentation. They are different validator paths on purpose.
