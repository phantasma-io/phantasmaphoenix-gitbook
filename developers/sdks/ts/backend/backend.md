# Backend

Use the TS SDK in Node.js or server-side tooling to build scripts, sign transactions with private keys, and call RPC directly.

## Recommended Flow

1. Create a `PhantasmaAPI` instance.
2. Build a script with `ScriptBuilder`.
3. Create and sign a `Transaction`.
4. Broadcast with `sendRawTransaction` and poll `getTransaction` for execution state.

For Carbon token flows, use the Carbon helpers and `sendCarbonTransaction`.

{% hint style="info" %}
Start with the step-by-step guide: [Quickstart](../quickstart.md).
{% endhint %}

{% hint style="info" %}
For Carbon token flows, see [Carbon Workflows](../carbon-workflows.md).
{% endhint %}

## Examples

[Create a Transaction](/developers/sdks/ts/backend/examples/create-a-transaction.md)

[Create Script Call](/developers/sdks/ts/backend/examples/create-script-call.md)

[Creating a New Address](/developers/sdks/ts/backend/examples/creating-a-new-address.md)

[Decode Transfer Events](/developers/sdks/ts/backend/examples/decode-transfer-events.md)

[Get a Block by Height](/developers/sdks/ts/backend/examples/get-a-block-by-height.md)

[Get a Transaction](/developers/sdks/ts/backend/examples/get-a-transaction.md)

[Get Data from New Blocks](/developers/sdks/ts/backend/examples/get-data-from-new-blocks.md)

[Get User Balances](/developers/sdks/ts/backend/examples/get-user-balances.md)

[Importing a Wallet](/developers/sdks/ts/backend/examples/importing-a-wallet.md)

[Invoke a Script](/developers/sdks/ts/backend/examples/invoke-a-script.md)

[Send a Transaction](/developers/sdks/ts/backend/examples/send-a-transaction.md)

[Sign a Transaction](/developers/sdks/ts/backend/examples/sign-a-transaction.md)

[Transfer Tokens](/developers/sdks/ts/backend/examples/transfer-tokens.md)

[Create New Carbon Token](/developers/sdks/ts/backend/examples/create-carbon-token.md)

[Create New Carbon Token Series](/developers/sdks/ts/backend/examples/create-carbon-token-series.md)

[Mint New Carbon NFT](/developers/sdks/ts/backend/examples/mint-carbon-nft.md)

{% hint style="info" %}
If you want to see full projects, check:

* [https://github.com/phantasma-io/phantasma-node-examples](https://github.com/phantasma-io/phantasma-node-examples)
* [https://github.com/phantasma-io/Phantasma-Blocks](https://github.com/phantasma-io/Phantasma-Blocks)
* [https://github.com/phantasma-io/Phantasma-Airdrop](https://github.com/phantasma-io/Phantasma-Airdrop)
{% endhint %}
