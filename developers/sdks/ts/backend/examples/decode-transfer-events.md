# Decode Transfer Events



{% hint style="info" %}
The **Data** is inside the **TokenSent** and **TokenReceived** Events
{% endhint %}

```typescript
import {getTokenEventData} from 'phantasma-ts':
let data = "044B43414C07005039278C0400046D61696E"; // this data should be inside the transaction event data
getTokenEventData(data);
```
