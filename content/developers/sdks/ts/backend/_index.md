---
title: "Backend"
linkTitle: "Backend Guide"
weight: 100
---

Use the TS SDK in Node.js or server-side tooling to build scripts, sign transactions with private keys, and call RPC directly.

## Recommended Flow

1. Create a `PhantasmaAPI` instance.
2. Build a script with `ScriptBuilder`.
3. Create and sign a `Transaction`.
4. Broadcast with `sendRawTransaction` and poll `getTransaction` for execution state.

For Carbon flows, build the message with a Carbon helper and pass it to
`sendTransaction`, which plans the fee, signs and broadcasts. Use
`sendCarbonTransaction` when the envelope is already signed and serialized.

> [!NOTE]
> Start with the step-by-step guide: [Quickstart](../quickstart.md).

> [!NOTE]
> For Carbon token flows, see [Carbon Workflows](../carbon-workflows.md) and
> [Fees And Broadcasting](../fees-and-broadcasting.md).

## Examples

[Create a Transaction](examples/create-a-transaction.md)

[Create Script Call](examples/create-script-call.md)

[Creating a New Address](examples/creating-a-new-address.md)

[Decode Transfer Events](examples/decode-transfer-events.md)

[Get a Block by Height](examples/get-a-block-by-height.md)

[Get a Transaction](examples/get-a-transaction.md)

[Get Data from New Blocks](examples/get-data-from-new-blocks.md)

[Get User Balances](examples/get-user-balances.md)

[Importing a Wallet](examples/importing-a-wallet.md)

[Invoke a Script](examples/invoke-a-script.md)

[Send a Transaction](examples/send-a-transaction.md)

[Sign a Transaction](examples/sign-a-transaction.md)

[Transfer Tokens](examples/transfer-tokens.md)

[Create New Carbon Token](examples/create-carbon-token.md)

[Create New Carbon Token Series](examples/create-carbon-token-series.md)

[Mint New Carbon NFT](examples/mint-carbon-nft.md)

[Infuse an NFT](examples/infuse-nft.md)

> [!NOTE]
> If you want to see full projects, check:
>
> * [https://github.com/phantasma-io/phantasma-node-examples](https://github.com/phantasma-io/phantasma-node-examples)
> * [https://github.com/phantasma-io/Phantasma-Blocks](https://github.com/phantasma-io/Phantasma-Blocks)
> * [https://github.com/phantasma-io/Phantasma-Airdrop](https://github.com/phantasma-io/Phantasma-Airdrop)
