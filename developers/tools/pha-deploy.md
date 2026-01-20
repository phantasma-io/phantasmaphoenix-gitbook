# pha-deploy

CLI utility for deploying fungible tokens and NFTs on Phantasma, creating NFT
series, and minting NFTs using a TOML configuration file (or CLI-only flags). It uses the same
`phantasma-sdk-ts` builders as the Token Deployment UI, but is optimized for
repeatable CLI workflows.

Related: [Token Deployment UI](../token-deployment-frontend.md)

## Installation

```bash
# install globally
npm i -g pha-deploy

# or run once via npx
npx pha-deploy --help

# local dev install
npm install
npm run build
```

If you have [`just`](https://github.com/casey/just) installed, the repo includes helpers
such as `just ct` (create token), `just cs` (create series), and `just mn` (mint).

## Quick start

```bash
# copy the example config
cp config/config.example.toml config.toml

# edit config.toml (rpc, nexus, wif, metadata, schemas)
pha-deploy --create-token
```

## Configuration file (config.toml)

By default the CLI loads `config.toml` from the current working directory.
Use `--config <path>` to load an alternate file.

The config uses TOML with embedded JSON strings (triple quotes) for complex data.

### Connection and signer

```toml
rpc = "https://testnet.phantasma.info/rpc"
nexus = "testnet"
wif = ""
```

- `rpc` defaults to `https://testnet.phantasma.info/rpc` if omitted.
- `nexus` should match the target network (example: `mainnet`, `testnet`).
- `wif` is required for all actions (including dry-run) because the CLI signs transactions.
  Keep it out of version control. See [Private Key Guideline](../private-key-guideline.md).

### Token definition

```toml
symbol = "NFTMY"
token_type = "nft" # nft | fungible
token_max_supply = 1000000000000
fungible_decimals = 8
```

Rules enforced by the SDK:

- Symbol must be 1 to 255 characters, uppercase A-Z only.
- `token_type = "fungible"` requires `token_max_supply` and `fungible_decimals`.
- `fungible_decimals` must be an integer in the range 0..255.
- `token_max_supply` must be non-negative.
- For NFTs, `token_max_supply` is optional, but if provided it must fit into Int64.

### Token metadata (required)

`token_metadata` must be a JSON object. All values must be strings.
Required fields: `name`, `icon`, `url`, `description`.

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

Icon rules (enforced by the SDK):

- Must be a base64 data URI: `data:image/png|jpeg|webp;base64,...`
- Payload must be valid base64 and non-empty.

### Token schemas (NFTs only)

NFT tokens require `token_schemas`, provided as JSON with three arrays:
`seriesMetadata`, `rom`, and `ram`.

```toml
token_schemas = """
{
  "seriesMetadata": [
    { "name": "extraSharedSampleField", "type": "String" }
  ],
  "rom": [
    { "name": "name", "type": "String" },
    { "name": "description", "type": "String" },
    { "name": "imageURL", "type": "String" },
    { "name": "infoURL", "type": "String" },
    { "name": "royalties", "type": "Int32" }
  ],
  "ram": []
}
"""
```

Schema rules enforced by `TokenSchemasBuilder`:

- Mandatory metadata fields must appear in either `seriesMetadata` or `rom`:
  `name`, `description`, `imageURL`, `infoURL`, `royalties`.
- System fields are reserved and auto-managed by the SDK: `id`, `mode`, `rom`.
  Do not add custom fields with these names.
- Field names are case-sensitive.
- If `ram` is an empty array, the SDK uses a dynamic RAM schema.

Supported field types (VmType names):

```
Dynamic
Array
Bytes
Struct
Int8
Int16
Int32
Int64
Int256
Bytes16
Bytes32
Bytes64
String
Array_Dynamic
Array_Bytes
Array_Struct
Array_Int8
Array_Int16
Array_Int32
Array_Int64
Array_Int256
Array_Bytes16
Array_Bytes32
Array_Bytes64
Array_String
```

### Series metadata and NFT metadata

`series_metadata` and `nft_metadata` accept either:

- a JSON object of key/value pairs, or
- a JSON array of `{ "name": "...", "value": ... }` entries.

Values can be strings or numbers. The SDK validates the values against the schema.

```toml
series_metadata = """
{
  "name": "Series Name",
  "description": "Series description",
  "imageURL": "https://example.com/series.png",
  "infoURL": "https://example.com",
  "royalties": 10000000
}
"""

nft_metadata = """
{
  "name": "NFT Name",
  "description": "NFT description",
  "imageURL": "https://example.com/nft.png",
  "infoURL": "https://example.com",
  "royalties": 10000000
}
"""
```

### Token and series identifiers

```toml
carbon_token_id = 0
carbon_token_series_id = 0
```

Use these when creating a series or minting against an existing token or series.

### Limits and fees

```toml
create_token_max_data = 1000000000
create_token_series_max_data = 100000000
mint_token_max_data = 100000000

gas_fee_base = 10000
gas_fee_create_token_base = 10000000000
gas_fee_create_token_symbol = 10000000000
gas_fee_create_token_series = 2500000000
gas_fee_multiplier = 10000
```

These values are passed directly to the SDK transaction helpers. Use the defaults
from `config.example.toml` as a starting point and adjust only if needed.

### Runtime flags

```toml
dry_run = false
```

`dry_run` enables dry-run mode in config. The CLI `--dry-run` flag always overrides it.

## CLI-only usage (no config file)

You can run without a TOML file by passing all required values as flags:

Create a token:

```bash
pha-deploy --create-token \
  --rpc <rpcUrl> \
  --nexus <nexus> \
  --wif <wif> \
  --symbol <symbol> \
  --token-type nft \
  --token-metadata '<tokenMetadataJson>' \
  --token-schemas '<tokenSchemasJson>' \
  --create-token-max-data <maxData> \
  --gas-fee-base <gasFeeBase> \
  --gas-fee-create-token-base <gasFeeCreateTokenBase> \
  --gas-fee-create-token-symbol <gasFeeCreateTokenSymbol> \
  --gas-fee-multiplier <gasFeeMultiplier>
```

Create a series:

```bash
pha-deploy --create-series \
  --rpc <rpcUrl> \
  --nexus <nexus> \
  --wif <wif> \
  --carbon-token-id <tokenId> \
  --token-schemas '<tokenSchemasJson>' \
  --series-metadata '<seriesMetadataJson>' \
  --create-token-series-max-data <maxData> \
  --gas-fee-base <gasFeeBase> \
  --gas-fee-create-token-series <gasFeeCreateTokenSeries> \
  --gas-fee-multiplier <gasFeeMultiplier>
```

Mint an NFT:

```bash
pha-deploy --mint-nft \
  --rpc <rpcUrl> \
  --nexus <nexus> \
  --wif <wif> \
  --carbon-token-id <tokenId> \
  --carbon-token-series-id <seriesId> \
  --token-schemas '<tokenSchemasJson>' \
  --nft-metadata '<nftMetadataJson>' \
  --mint-token-max-data <maxData> \
  --gas-fee-base <gasFeeBase> \
  --gas-fee-multiplier <gasFeeMultiplier>
```

Notes:

- For fungible tokens, also pass `--token-max-supply` and `--fungible-decimals`.
- For series and mint actions, supply the metadata JSON strings and token schemas.

## Running actions

### Create a token

```bash
pha-deploy --create-token --config path/to/config.toml
```

Requirements:

- `wif`, `rpc`, `nexus`, `symbol`.
- `token_metadata` is required for all tokens.
- For fungible tokens: `token_max_supply`, `fungible_decimals`.
- For NFT tokens: `token_schemas`.

### Create an NFT series

```bash
pha-deploy --create-series --config path/to/config.toml
```

Requirements:

- `carbon_token_id`.
- `token_schemas.seriesMetadata`.
- `series_metadata` (can be empty JSON object if your schema only includes required defaults).

### Mint an NFT

```bash
pha-deploy --mint-nft --config path/to/config.toml
```

Requirements:

- `carbon_token_id` and `carbon_token_series_id`.
- `token_schemas.rom`.
- `nft_metadata`.

### Dry-run and settings log

Append `--dry-run` to any action to build and print the transaction without broadcasting.
Use `--settings-log` to print the resolved configuration; the CLI omits the WIF and
prints the derived owner address instead.

### Transaction status

After broadcasting, the CLI polls `getTransaction` every 2 seconds for up to 30 seconds.
If the state does not reach `Halt` in that window, it reports the timeout so you can
check the transaction manually.

## CLI flags and overrides

Actions:

- `--create-token`
- `--create-series`
- `--mint-nft`

Common flags:

- `--config <path>` Path to TOML config file (default: `config.toml`).
- `--dry-run` Do not broadcast transactions; just show payloads.
- `--rpc-log` Enable SDK JSON-RPC logging (full response payloads).
- `--settings-log` Print resolved configuration before executing an action.
- `--help` Show help.

Overrides (replace `config.toml` values when provided):

- `--rpc <url>` RPC endpoint.
- `--nexus <name>` Nexus name (example: `mainnet`, `testnet`).
- `--wif <wif>` WIF for signing.
- `--symbol <symbol>` Token symbol.
- `--token-type <nft|fungible>` Token type to create (default: `nft`).
- `--token-max-supply <int>` Max supply (required for `fungible`).
- `--fungible-max-supply <int>` Alias for `--token-max-supply`.
- `--fungible-decimals <0..255>` Decimals for fungible tokens.
- `--carbon-token-id <int>` Existing token id (for series or mint).
- `--carbon-token-series-id <int>` Existing series id (for mint).
- `--rom <hex>` Token ROM hex (not required by built-in actions).
- `--token-schemas '<json>'` Inline JSON for token schemas.
- `--token-metadata '<json>'` Inline JSON for token metadata.
- `--series-metadata '<json>'` Inline JSON for series metadata.
- `--nft-metadata '<json>'` Inline JSON for NFT metadata.
- `--create-token-max-data <int>` Payload limit for token creation.
- `--create-token-series-max-data <int>` Payload limit for series creation.
- `--mint-token-max-data <int>` Payload limit for minting.
- `--gas-fee-base <int>` Base gas fee.
- `--gas-fee-create-token-base <int>` Gas fee for create-token.
- `--gas-fee-create-token-symbol <int>` Symbol registration fee.
- `--gas-fee-create-token-series <int>` Gas fee for create-series.
- `--gas-fee-multiplier <int>` Multiplier applied to gas fee.

Notes:

- JSON arguments must be single-line quoted strings. For large edits, update `config.toml`.
- Unknown flags are ignored by the config loader, but prefer editing the TOML for long-lived changes.
