---
description: Create Carbon tokens and NFTs without writing code.
---

# Token Deployment UI

The Token Deployment UI is a web interface for creating Carbon tokens and NFTs, and for managing VM contract lifecycle without writing custom frontend code.

## What you can do

- Deploy fungible tokens and NFTs
- Deploy standalone VM contracts
- Attach VM contracts to existing tokens
- Upgrade existing custom or token-backed contracts
- Create NFT series
- Mint NFTs
- Infuse NFTs (attach assets to an NFT address)

## How it works

1. Open the Token Deployment UI: https://deploy.phantasma.info
2. Connect a wallet that supports Carbon transactions.
3. Choose an action:
   - **Token** for native Carbon token flows
   - **Contract** for VM contract lifecycle
   - **Series**, **Mint**, or **Infuse** for NFT flows
4. Fill in the required fields.
5. Review and sign the transaction in your wallet.

For contract lifecycle actions, upload compiled `.pvm` and `.abi` artifacts from `pha-tomb`.

## Need the full details?

For the full step-by-step guide (networks, fees, schemas, and field rules), see:

- [Token Deployment UI guide](/developers/token-deployment-frontend.md)
- [Carbon overview](/about/carbon.md)
