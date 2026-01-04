# Wallet Connection

Use the Phantasma Link protocol to connect a browser dApp to a wallet. The TS SDK exposes three layers of the same connection.

## Choose a layer

| Layer | Package | Best for | Docs |
| --- | --- | --- | --- |
| PhantasmaLink | `phantasma-sdk-ts` | Direct, low-level API | [Phantasma Link](/developers/sdks/ts/shared-methods/phantasmalink.md) |
| EasyConnect | `phantasma-sdk-ts` | Smaller wrapper + Carbon signing helper | [EasyConnect](/developers/sdks/ts/shared-methods/easyconnect.md) |
| @phantasma/connect-react | `@phantasma/connect-react` | React-first wrapper + UI widget | [React Wallet Connection](/developers/sdks/ts/frontend/connect-react.md) |

## Quick choice

- React app -> `@phantasma/connect-react`.
- Non-React app -> `EasyConnect`.
- Full control -> `PhantasmaLink`.

## Typical flow

1. Connect to a wallet (Poltergeist or Ecto).
2. Build a script with `ScriptBuilder`.
3. Call `signTx` (VM) or `signCarbonTxAndBroadcast` / `signCarbonTransaction` (Carbon).
4. Confirm with `getTransaction`.
