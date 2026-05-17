# Setup

## Installation

{% hint style="info" %}
**Important:** Before the Phoenix chain update, the package **phantasma-ts** was used. It is now deprecated. Use **phantasma-sdk-ts** instead.
{% endhint %}

### In a TypeScript project

```
npm install phantasma-sdk-ts
```

New TypeScript code should import from the public entrypoint:

```ts
import { PhantasmaAPI, PhantasmaKeys, ScriptBuilder } from "phantasma-sdk-ts/public";
```

Lowercase deep imports are available for stable source areas such as
`phantasma-sdk-ts/rpc`, `phantasma-sdk-ts/tx`, `phantasma-sdk-ts/vm`,
and `phantasma-sdk-ts/types`. Use `/types` when you need the complete Carbon
helper surface, including fee option classes and Carbon id helpers. The root
export and `core/**` paths remain for compatibility with older consumers, but
new code should use `/public` or the documented lowercase entrypoints.

### React wrapper (optional)

```
npm install @phantasma/connect-react
```

## Backend or Frontend?

For backend usage, see:

{% content-ref url="/developers/sdks/ts/backend/backend.md" %}
Backend Guide
{% endcontent-ref %}

For frontend usage with Poltergeist/Ecto:

{% content-ref url="/developers/sdks/ts/frontend/frontend.md" %}
Frontend Guide
{% endcontent-ref %}
