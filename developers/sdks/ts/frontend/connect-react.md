# React Wallet Connection (`@phantasma/connect-react`)

## Overview

`@phantasma/connect-react` is the React-first wallet layer on top of `EasyConnect`.

Current package version:

- `0.1.0`

It gives you:

- a React context
- a state container for connect / disconnect / restore
- transport selection
- connection diagnostics
- a ready-made account widget

## Install

```bash
npm install @phantasma/connect-react
```

## Core Pieces

The package exports:

- `PhaConnectState`
- `PhaConnectCtx`
- `PhaAccountWidgetV1`

`PhaConnectState` is the main object you create and place into context.

## Provider Setup

```tsx
import { ReactNode } from "react";
import { PhaConnectCtx, PhaConnectState } from "@phantasma/connect-react";

const phaConnectState = new PhaConnectState({
  transportMode: "auto",
});

export function PhantasmaProvider({ children }: { children: ReactNode }) {
  return (
    <PhaConnectCtx.Provider value={phaConnectState}>
      {children}
    </PhaConnectCtx.Provider>
  );
}
```

## Connect Options

`PhaConnectState` accepts an optional config object:

```ts
type ConnectOptions = {
  requiredVersion?: number;
  platform?: string;
  transportMode?: "auto" | "injected" | "local-socket";
  transportDetectionTimeoutMs?: number;
  connectAttemptTimeoutMs?: number;
};
```

### Transport Modes

- `auto`
  - detect and choose between injected and local socket
- `injected`
  - prefer injected wallet transport
- `local-socket`
  - prefer raw local wallet socket

For tooling or UIs that depend on a predictable local wallet path, `local-socket` is often the safer choice.

## Built-In Widget

```tsx
import { PhaAccountWidgetV1, PhaConnectState } from "@phantasma/connect-react";

export function WalletButton({ state }: { state: PhaConnectState }) {
  return <PhaAccountWidgetV1 state={state} />;
}
```

## Custom UI

`PhaConnectState` exposes connection state you can render yourself:

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

## Useful State And Helpers

Common fields and methods on `PhaConnectState`:

- `conn`
  - current `EasyConnect` instance or `null`
- `err_msg`
  - latest error text
- `is_connecting`
- `is_connected`
- `selected_transport_mode`
- `available_transports`
- `last_connect_diagnostics`
- `connect(...)`
- `connect_with_transport_mode(...)`
- `set_transport_mode(...)`
- `disconnect()`
- `restore()`
- `refresh_available_transports(...)`

## Diagnostics

`last_connect_diagnostics` is especially useful when you are debugging connection behavior. It records things like:

- configured transport mode
- selected transport
- available transports
- whether fallback was used
- whether injected transport was detected
- whether local socket was reachable
- failure class and failure message

That makes it much easier to explain why a particular wallet path was chosen.

## Restore Behavior

`restore()` uses persisted session config and attempts to reconnect. This is the normal way to restore a previous wallet session after a page reload.

## Signing

When connected, `pha.conn` is an `EasyConnect` instance. That means you can use:

- `pha.conn.signTransaction(...)`
- `pha.conn.signCarbonTransaction(...)`
- `pha.conn.signPrebuiltTransaction(...)`
- `pha.conn.link.signTx(...)`
- `pha.conn.link.signPrebuiltTransaction(...)`

Practical rule:

- normal wallet-driven VM transaction -> `signTransaction(...)`
- prebuilt VM transaction -> `signPrebuiltTransaction(...)`
- Carbon `TxMsg` -> `signCarbonTransaction(...)`

## Relationship To Lower Layers

The stack looks like this:

- `@phantasma/connect-react`
  - React state and transport orchestration
- `EasyConnect`
  - smaller browser wallet wrapper
- `PhantasmaLink`
  - low-level Link transport and signing

If the higher layer is not enough for a particular use case, you can always drop down through `pha.conn` and then through `pha.conn.link`.
