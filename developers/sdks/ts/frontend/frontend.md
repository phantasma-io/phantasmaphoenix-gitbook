# Frontend

Use the TS SDK to connect to wallets and ask users to sign transactions from the browser.

## Wallet Integration

Phantasma Link is the base connection layer.  
On top of it you can use `EasyConnect` (wrapper) or `@phantasma/connect-react` (React wrapper).

## Wallet Connection Layers

| Layer | Package | Use when | Docs |
| --- | --- | --- | --- |
| PhantasmaLink | `phantasma-sdk-ts` | You want the direct, low-level API | [Phantasma Link](/developers/sdks/ts/shared-methods/phantasmalink.md) |
| EasyConnect | `phantasma-sdk-ts` | You want a smaller wrapper + Carbon signing helper | [EasyConnect](/developers/sdks/ts/shared-methods/easyconnect.md) |
| @phantasma/connect-react | `@phantasma/connect-react` | You want a React-first wrapper and UI widget | [React Wallet Connection](/developers/sdks/ts/frontend/connect-react.md) |

{% content-ref url="/developers/sdks/ts/shared-methods/phantasmalink.md" %}
Phantasma Link
{% endcontent-ref %}

{% content-ref url="/developers/sdks/ts/shared-methods/easyconnect.md" %}
EasyConnect
{% endcontent-ref %}

{% content-ref url="/developers/sdks/ts/frontend/connect-react.md" %}
React Wallet Connection
{% endcontent-ref %}

## Recommended Flow

1. Connect to a wallet (Poltergeist or Ecto).
2. Build a script with `ScriptBuilder`.
3. Call `signTx` (or `signCarbonTxAndBroadcast` / `signCarbonTransaction` for Carbon transactions).
4. Use `getTransaction` to confirm results.

For Carbon token flows, see [Carbon Workflows](../carbon-workflows.md).

## Examples

[Connect to the Wallet](/developers/sdks/ts/frontend/examples/connect-to-the-wallet.md)

[Invoking a Script](/developers/sdks/ts/frontend/examples/invoking-a-script.md)

[Sending a Transaction](/developers/sdks/ts/frontend/examples/sending-a-transaction.md)
