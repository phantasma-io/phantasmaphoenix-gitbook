---
title: "Decode Transfer Events"
weight: 40
---

> [!NOTE]
> The event data of a fungible transfer is carried by the `TokenSend` and `TokenReceive` events.

```ts
import {getTokenEventData} from 'phantasma-sdk-ts/public';
let data = "044B43414C07005039278C0400046D61696E"; // this data should be inside the transaction event data
let event_data = getTokenEventData(data);
console.log(event_data);
```
