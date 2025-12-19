# Frontend

Use the TS SDK to connect to wallets and ask users to sign transactions from the browser.

## Wallet Integration

You can work directly with **PhantasmaLink** or use the wrapper **EasyConnect**.

{% content-ref url="/developers/sdks/ts/shared-methods/phantasmalink.md" %}
Phantasma Link
{% endcontent-ref %}

{% hint style="info" %}
EasyConnect wraps PhantasmaLink and adds helpers like `signCarbonTransaction`.
{% endhint %}

## Recommended Flow

1. Connect to a wallet (Poltergeist or Ecto).
2. Build a script with `ScriptBuilder`.
3. Call `signTx` (or `signCarbonTxAndBroadcast` for Carbon transactions).
4. Use `getTransaction` to confirm results.

For Carbon token flows, see [Carbon Workflows](../carbon-workflows.md).

## Examples

[Connect to the Wallet](/developers/sdks/ts/frontend/examples/connect-to-the-wallet.md)

[Invoking a Script](/developers/sdks/ts/frontend/examples/invoking-a-script.md)

[Sending a Transaction](/developers/sdks/ts/frontend/examples/sending-a-transaction.md)
