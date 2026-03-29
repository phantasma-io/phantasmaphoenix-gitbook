# Tools

CLI tools for working with Phantasma data, token workflows, and VM contract lifecycle.

## Available tools

- [pha-decode](pha-decode.md) - decode Carbon and VM transactions plus legacy event hex.
- [pha-deploy](pha-deploy.md) - create tokens, create NFT series, mint assets, compile contracts, deploy custom contracts, upgrade contracts, and attach VM code to existing tokens.

## When to use these tools

- Use **pha-decode** when you need to inspect raw transactions or legacy event hex.
- Use **pha-deploy** when you want a repeatable CLI alternative to the Token Deployment UI, or when you need explicit contract lifecycle workflows such as `contract compile`, `contract deploy`, `contract upgrade`, or `contract attach`.

Related docs:
- [Token Deployment UI](../token-deployment-frontend.md)
- [Private Key Guideline](../private-key-guideline.md)
