# React Wallet Connection (@phantasma/connect-react)

## Overview

`@phantasma/connect-react` is a React wrapper around [EasyConnect](/developers/sdks/ts/shared-methods/easyconnect.md) (from `phantasma-sdk-ts`).  
It provides a MobX state class and a ready-to-use connect widget.

{% hint style="info" %}
For the layer map and quick choice, see [Wallet Connection](/developers/sdks/ts/frontend/wallet-connection.md).
{% endhint %}

## Install

```
npm install @phantasma/connect-react
```

## Provider setup

Create a shared `PhaConnectState` and expose it via context:

```tsx
import { ReactNode } from "react";
import { PhaConnectCtx, PhaConnectState } from "@phantasma/connect-react";

export function PhantasmaProvider({ children }: { children: ReactNode }) {
  const phaConnectState = new PhaConnectState();

  return (
    <PhaConnectCtx.Provider value={phaConnectState}>
      {children}
    </PhaConnectCtx.Provider>
  );
}
```

## Built-in widget

Use the built-in account widget:

```tsx
import { PhaAccountWidgetV1, PhaConnectState } from "@phantasma/connect-react";

export function WalletButton({ state }: { state: PhaConnectState }) {
  return <PhaAccountWidgetV1 state={state} />;
}
```

## Custom UI (MobX-aware)

`PhaConnectState` is MobX observable. Wrap your component with `observer` so it re-renders on state changes.

```tsx
import { useContext, useEffect } from "react";
import { observer } from "mobx-react-lite";
import { PhaConnectCtx } from "@phantasma/connect-react";

export const WalletStatus = observer(() => {
  const pha = useContext(PhaConnectCtx);

  useEffect(() => {
    pha.restore();
  }, [pha]);

  if (!pha.is_connected) {
    return (
      <button onClick={() => pha.connect()} disabled={pha.is_connecting}>
        {pha.is_connecting ? "Connecting..." : "Connect wallet"}
      </button>
    );
  }

  const address = pha.conn?.link?.account?.address ?? "";
  return <div>Connected: {address}</div>;
});
```

## Signing

When connected, `pha.conn` is an `EasyConnect` instance.  
You can use either the wrapper or the underlying `PhantasmaLink`:

- VM tx: `pha.conn.link.signTx(...)`
- Carbon tx: `pha.conn.signCarbonTransaction(...)`

If you prefer `async/await`, wrap the callback-style methods with a Promise (same approach as in the EasyConnect page).

## Restore behavior

`pha.restore()` checks `localStorage` for the `pha-connect-react` key and calls `connect()` if it exists.
