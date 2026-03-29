---
description: Here, we will provide information on how to deploy your Smart Contract
---

# How to Deploy

{% hint style="info" %}
Before deployment, compile your source with `pha-tomb` and make sure you have the generated `.pvm` and `.abi` artifacts.
{% endhint %}

## Step 1: decide which flow you actually need

This is the most common source of deployment errors.

### Standalone custom contract

Use this for lowercase custom contract names such as `my_contract`.

Tool:
- `pha-deploy contract deploy`

### New token-backed contract

Use this for uppercase token symbols such as `MYTOKEN`.

Tool:
- `pha-deploy --create-token`

### Attach VM code to an existing token

Use this when the token already exists on-chain and you now want to bind VM code to it.

Tool:
- `pha-deploy contract attach`

### Upgrade an existing contract

Use this after the contract already exists on-chain.

Tool:
- `pha-deploy contract upgrade`

## Step 2: compile the contract

Example:

```bash
pha-tomb output:./build protocol:19 debug nativecheck:error my_contract.tomb
```

This generates artifacts under `./build/Output/`.

Typical outputs:
- `my_contract.pvm`
- `my_contract.abi`
- optional `my_contract.debug`
- optional `my_contract.asm`

## Step 3: deploy with the correct tool

### Standalone custom contract

```bash
pha-deploy contract deploy \
  --rpc https://testnet.phantasma.info/rpc \
  --nexus testnet \
  --chain main \
  --wif <wif> \
  --contract-name my_contract \
  --script ./build/Output/my_contract.pvm \
  --abi ./build/Output/my_contract.abi
```

### Upgrade a standalone custom contract

```bash
pha-deploy contract upgrade \
  --rpc https://testnet.phantasma.info/rpc \
  --nexus testnet \
  --chain main \
  --wif <wif> \
  --contract-name my_contract \
  --script ./build/Output/my_contract.pvm \
  --abi ./build/Output/my_contract.abi
```

### Attach VM code to an existing token

```bash
pha-deploy contract attach \
  --rpc https://testnet.phantasma.info/rpc \
  --nexus testnet \
  --chain main \
  --wif <wif> \
  --symbol MYTOKEN \
  --script ./build/Output/MYTOKEN.pvm \
  --abi ./build/Output/MYTOKEN.abi
```

### Create a new token-backed contract

For a new token-backed contract, do not use `contract deploy`.

Use:
- `pha-deploy --create-token`

See:
- [pha-deploy](../../tools/pha-deploy.md)

## Important validator rules

- `contract deploy` is for lowercase custom contracts.
- Uppercase token symbols belong to token-backed flows.
- `contract attach` expects an already existing token.
- Token-backed contracts must satisfy token validation rules, including the required trigger surface such as `onMint`.
- For NFT tokens, series creation is still a separate step after token creation or attach.
