# Virtual Machine

The node runs the Phantasma VM. It executes:

- standalone custom contracts deployed with `Runtime.DeployContract(...)`
- token-backed contracts created with `Nexus.CreateToken(...)` or attached later with `Nexus.AttachTokenContract(...)`
- trigger code: `onMint`, `onBurn`, `onSend`, `onReceive`, `onInfuse`, `onSeries`, `onAttach`, `onUpgrade` and `onWrite`
- transaction scripts and read-only scripts executed through the VM entry context

This section describes what the VM executes, how contracts are admitted, and which interops the node implements.

## What To Read First

- [architecture.md](architecture.md)
  - how execution contexts, registers, stack, interop, gas, and triggers fit together
- [types.md](types.md)
  - the VM value model used by scripts, ABIs, and interop calls
- [opcodes.md](opcodes.md)
  - the core instruction set and base opcode gas costs
- [interop.md](interop.md)
  - the native bridge from VM code into token, NFT, storage, and contract lifecycle operations

## Practical Scope

For most contract authors, the most important parts are:

- custom contract lifecycle through `Runtime.DeployContract(...)` and `Runtime.UpgradeContract(...)`
- token-backed lifecycle through `Nexus.CreateToken(...)`, `Nexus.AttachTokenContract(...)`, and `Runtime.UpgradeContract(...)`
- token and NFT interops such as `Runtime.MintTokens`, `Runtime.MintToken`, `Runtime.TransferTokens`, `Runtime.TransferToken`, `Runtime.ReadToken`, and `Nexus.CreateTokenSeries`
- storage helpers `Data.*`, `Map.*`, and `List.*`

If you are deploying contracts rather than writing raw scripts, start with the tools:

- [`pha-deploy`](../../../../tools/pha-deploy.md)
- [Token Deployment Frontend](../../../../token-deployment-frontend.md)
