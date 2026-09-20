# pha-deploy

`pha-deploy` is the CLI for Phantasma token flows and VM contract lifecycle workflows.

Use it when you want repeatable, scriptable deployment steps instead of a browser UI.

Related pages:
- [Token Deployment UI guide](../token-deployment-frontend.md)
- [Compiler setup](../compiler/setup.md)
- [Private Key Guideline](../private-key-guideline.md)

## What pha-deploy covers

Token actions:
- `--create-token`
- `--create-series`
- `--mint-fungible`
- `--mint-nft`

Contract actions:
- `contract compile`
- `contract deploy`
- `contract upgrade`
- `contract attach`

## Choose the right flow

This matters because Phantasma treats lowercase custom contracts and uppercase token symbols as different namespaces.

### Custom VM contract

Use:
- `pha-deploy contract deploy`
- `pha-deploy contract upgrade`

Use a lowercase contract name such as `my_contract`.

Chain path:
- deploy -> `Runtime.DeployContract(...)`
- upgrade -> `Runtime.UpgradeContract(...)`

### New token-backed contract

Use:
- `pha-deploy --create-token`

Use an uppercase token symbol such as `MYTOKEN`.

Chain path:
- `Nexus.CreateToken(...)`

### Attach VM code to an existing token

Use:
- `pha-deploy contract attach`

This is for a token that already exists on-chain but does not yet have the desired VM contract attached.

Chain path:
- `Nexus.AttachTokenContract(...)`

### Upgrade an existing token-backed contract

Use:
- `pha-deploy contract upgrade`

This is for later code updates after the token-backed contract already exists through either `create-token` or `contract attach`.

### NFT note

For NFT collections, token lifecycle and series lifecycle are separate:
- first create the token or attach VM code to the existing token
- then create NFT series
- then mint NFTs

## Installation

```bash
# install globally
npm i -g pha-deploy

# inspect installed versions
pha-deploy --version

# local development
npm install
npm run build
node dist/cli.js --help
```

If you use [`just`](https://github.com/casey/just), the repo also ships helper recipes such as `just ct`, `just cs`, `just mn`, and related dry-run variants.

## Requirements

- Node.js `>=22`
- `pha-tomb >= 2.1.0` for `contract compile`

`contract compile` resolves `pha-tomb` in this order:
1. `--compiler <path>`
2. `PHA_TOMB_PATH`
3. `PATH`

`contract deploy`, `contract upgrade`, and `contract attach` do not invoke the compiler directly. They work from a compiled bundle or explicit `.pvm` / `.abi` inputs.

## Usage

```bash
pha-deploy contract <compile|deploy|upgrade|attach> [options]
pha-deploy --create-token [options]
pha-deploy --create-series [options]
pha-deploy --mint-fungible [options]
pha-deploy --mint-nft [options]
```

## Token workflow

Token actions still support the config-first TOML workflow.

Quick start:

```bash
cp config/config.example.toml config.toml
pha-deploy --create-token --config config.toml
```

### config.toml basics

```toml
rpc = "https://testnet.phantasma.info/rpc"
nexus = "testnet"
wif = ""

symbol = "MYNFT"
token_type = "nft" # nft | fungible
token_max_supply = 1000000000000
fungible_decimals = 8
```

Notes:
- `rpc` defaults to `https://testnet.phantasma.info/rpc` if omitted.
- `nexus` must match the target network.
- `wif` is required even for `--dry-run`, because the CLI still builds and signs transactions.
- Fees are not configured here. The chain prices each transaction, and the CLI
  plans the offer from the message itself. See [Fees](#fees).

### Token validation rules

Rules enforced by the SDK and CLI:
- symbol must be 1 to 255 characters, uppercase A-Z only
- fungible tokens require `token_max_supply` and `fungible_decimals`
- `fungible_decimals` must be in `0..255`
- fungible `token_max_supply` must be non-negative
- NFT `token_max_supply` is optional, but if present it must fit in `Int64`

### Token metadata

`token_metadata` is required for all tokens and must contain string values.

Required fields:
- `name`
- `icon`
- `url`
- `description`

Example:

```toml
token_metadata = """
{
  "name": "My token",
  "icon": "data:image/png;base64,<BASE64_DATA>",
  "url": "https://example.com",
  "description": "Token description"
}
"""
```

Icon rules:
- must be a base64 data URI
- supported formats: `png`, `jpeg`, `webp`
- payload must be valid base64 and non-empty

### NFT schemas

NFT tokens require `token_schemas` with three arrays:
- `seriesMetadata`
- `rom`
- `ram`

Example:

```toml
token_schemas = """
{
  "seriesMetadata": [
    { "name": "name", "type": "String" },
    { "name": "description", "type": "String" },
    { "name": "imageURL", "type": "String" },
    { "name": "infoURL", "type": "String" },
    { "name": "royalties", "type": "Int32" }
  ],
  "rom": [],
  "ram": []
}
"""
```

Schema rules:
- standard NFT fields must appear in either `seriesMetadata` or `rom`:
  - `name`
  - `description`
  - `imageURL`
  - `infoURL`
  - `royalties`
- reserved system fields must not be declared manually:
  - `id`
  - `mode`
  - `rom`
- field names are case-sensitive
- empty `ram` means dynamic RAM extras are allowed

### Series and NFT metadata

`series_metadata` and `nft_metadata` accept either:
- a JSON object of `name -> value`
- an array of `{ "name": "...", "value": ... }`

Values are validated against the schema.

### Token actions

Create a token:

```bash
pha-deploy --create-token --config ./config.toml
```

Create a series:

```bash
pha-deploy --create-series --config ./config.toml
```

Mint an NFT:

```bash
pha-deploy --mint-nft --config ./config.toml
```

Mint fungible tokens:

```bash
pha-deploy --mint-fungible --config ./config.toml
```

### CLI-only examples

Create a token:

```bash
pha-deploy --create-token \
  --rpc <rpcUrl> \
  --nexus <nexus> \
  --wif <wif> \
  --symbol <symbol> \
  --token-type nft \
  --token-metadata '<tokenMetadataJson>' \
  --token-schemas '<tokenSchemasJson>'
```

Create a series:

```bash
pha-deploy --create-series \
  --rpc <rpcUrl> \
  --nexus <nexus> \
  --wif <wif> \
  --carbon-token-id <tokenId> \
  --token-schemas '<tokenSchemasJson>' \
  --series-metadata '<seriesMetadataJson>'
```

Mint an NFT:

```bash
pha-deploy --mint-nft \
  --rpc <rpcUrl> \
  --nexus <nexus> \
  --wif <wif> \
  --carbon-token-id <tokenId> \
  --phantasma-series-id <seriesId> \
  --token-schemas '<tokenSchemasJson>' \
  --nft-metadata '<nftMetadataJson>'
```

### Fees

There is nothing to configure. Every transaction is priced by the chain.

A token transaction is a Carbon message. The CLI builds it, asks the node for
its gas config, and plans the gas offer and the storage deposit from that exact
message. Both are printed before the transaction is sent, and the gas the chain
billed is printed after it settles:

```text
Fee plan: CreateToken, envelope <bytes> bytes
  gas bill        <amount> KCAL (<atoms> atoms)
  gas offer       <amount> KCAL (<atoms> atoms)
  storage deposit <amount> SOUL (<atoms> atoms, <quanta> quanta, refunded when the rows are deleted)
...
Gas billed: <amount> KCAL (<atoms> atoms) - exactly as planned
```

The amounts depend on the network and on the message. Every one of them comes
from the gas config of the node the CLI is pointed at.

The plan is exact where the chain prices an operation from the message alone. It
is an upper bound where the price also depends on chain state the message does
not carry, which is whether the recipient already holds the token, whether the
supply row exists, and which mode a series mints in. Those are taken at the
reading that costs more, so a mint usually settles below its plan. The `gas bill`
line then reads `up to <amount>`, and the difference is refunded. The storage
deposit is refunded once the rows it paid for are deleted.

`--create-token` runs one lookup before it signs. `Token.CreateToken` is charged
its policy fee before the contract checks the symbol, so a symbol that is
already taken would cost that fee for nothing. The CLI refuses to send when the
chain says the symbol is taken, and also when the lookup could not establish an
answer.

The contract lifecycle is a VM script instead of a Carbon message, and no
formula prices a script. The CLI asks the chain's estimate service, which
dry-runs a submitted envelope and reports the bill it would settle with a
margin for state drift. The probe is built at the payer's whole gas token
balance, because an envelope that offers more than the payer holds is refused
instead of priced. Pass `--max-gas` to set the ceiling by hand in KCAL.

## Contract workflow

## 1. Compile

Compile a `.tomb` source file into a reusable bundle.

```bash
pha-deploy contract compile \
  --source ./contracts/demo.tomb \
  --compiler /path/to/pha-tomb \
  --out ./dist/contracts/demo \
  --debug \
  --protocol 16 \
  --nativecheck warn
```

Important flags:
- `--source <path>` required `.tomb` source file
- `--compiler <path>` explicit `pha-tomb` executable
- `--out <dir>` output directory for the bundle
- `--contract-name <name>` required only when the compiler emits multiple modules
- `--protocol <number>`
- `--debug`
- `--nativecheck <off|warn|error>`
- `--libpath <path>` repeatable library search path

Compile output:
- prints the resolved compiler command
- prints separated `stdout` / `stderr`
- writes a `manifest.json`
- copies the compiled artifacts:
  - `.pvm`
  - `.abi`
  - optional `.debug`
  - optional `.asm`
  - optional `.pvm.hex`
  - optional `.abi.hex`

For later deploy/upgrade/attach, `manifest.json` is the preferred handoff artifact.

## 2. Deploy a standalone custom contract

Use this for lowercase custom contracts.

With a manifest:

```bash
pha-deploy contract deploy \
  --rpc https://testnet.phantasma.info/rpc \
  --nexus testnet \
  --chain main \
  --wif <wif> \
  --manifest ./dist/contracts/demo/manifest.json \
  --dry-run
```

With explicit artifacts:

```bash
pha-deploy contract deploy \
  --rpc https://testnet.phantasma.info/rpc \
  --nexus testnet \
  --wif <wif> \
  --contract-name demo \
  --script ./dist/contracts/demo/demo.pvm \
  --abi ./dist/contracts/demo/demo.abi
```

Use lowercase contract names here. If you try to deploy an uppercase token symbol through this flow, the validator will reject it and tell you to use the token flow instead.

## 3. Upgrade a contract

This upgrades an already deployed contract. The same command is used for:
- standalone custom contracts
- token-backed contracts that already exist through `create-token` or `attach`

```bash
pha-deploy contract upgrade \
  --rpc https://testnet.phantasma.info/rpc \
  --nexus testnet \
  --chain main \
  --wif <wif> \
  --manifest ./dist/contracts/demo/manifest.json \
  --dry-run
```

For token-backed upgrades, the bundle contract name must match the token symbol already installed on-chain.

## 4. Attach a contract to an existing token

This flow binds VM code to a token that already exists on-chain.

```bash
pha-deploy contract attach \
  --rpc https://testnet.phantasma.info/rpc \
  --nexus testnet \
  --chain main \
  --wif <wif> \
  --manifest ./dist/contracts/demo/manifest.json \
  --symbol DEMO \
  --dry-run
```

Notes:
- `--symbol <symbol>` selects the existing token symbol to attach to
- if `--symbol` is omitted, the CLI falls back to the bundle contract name
- the token must already exist
- the attached contract must be compatible with that token
- for token-backed contracts, `onMint` is required

## Shared deploy / upgrade / attach flags

- `--rpc <url>` required
- `--nexus <name>` required
- `--chain <name>` optional, defaults to `main`
- `--wif <wif>` required
- `--manifest <path>` preferred compiled bundle input
- `--contract-name <name>` required when using direct `--script` / `--abi`
- `--script <path>` compiled `.pvm`
- `--abi <path>` compiled `.abi`
- `--debug <path>` optional `.debug`
- `--max-gas <kcal>` optional, the gas ceiling in KCAL. Left out, it is read from the chain's estimate
- `--pow <int>`
- `--payload-hex <hex>`
- `--dry-run`

Attach-only:
- `--symbol <symbol>`

## Dry-run, logging, and output

Common operational flags:
- `--dry-run`
- `--rpc-log`
- `--settings-log`

When broadcasting is enabled, the CLI prints:
- operation
- contract name
- signer address
- script and ABI sizes
- generated VM script hex
- signed transaction hex
- tx hash

Attach output also prints the resolved token symbol used in the interop call.

## Version output

`pha-deploy --version` prints both the CLI version and the resolved compiler binding.

Example:

```text
pha-deploy 0.6.0
pha-tomb version 2.1.0
pha-tomb path /usr/local/bin/pha-tomb
```

## Troubleshooting

### `contract deploy` rejects an uppercase name

You are using the wrong flow.

Use:
- `--create-token` for a new token-backed contract
- `contract attach` for an existing token

### `contract attach` fails because `onMint` is missing

This is a validator rule for token-backed contracts. The attached bundle must implement `onMint`.

### `contract compile` says `invalid trigger name:onAttach`

You are probably invoking the wrong `pha-tomb` binary. Pin the compiler explicitly with:
- `--compiler /path/to/pha-tomb`
- or `PHA_TOMB_PATH=/path/to/pha-tomb`

### NFT series still fail after token deployment or attach

Series creation is a separate step. First create the token or attach the contract, then run `--create-series`.
