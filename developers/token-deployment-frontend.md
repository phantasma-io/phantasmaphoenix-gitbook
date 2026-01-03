# Token Deployment UI

The Token Deployment frontend lets you deploy Carbon fungible/NFT tokens, create NFT series, and mint NFTs without writing code.

## Choose the right network

Use the site that matches your target network and switch your wallet to the same Phantasma nexus (Settings -> Nexus in PGL):

- Mainnet: [https://deploy.phantasma.info](https://deploy.phantasma.info) (wallet nexus: Main Net)
- Testnet: [https://deploy-testnet.phantasma.info](https://deploy-testnet.phantasma.info) (wallet nexus: Test Net)
- Devnet: [https://deploy-devnet.phantasma.info](https://deploy-devnet.phantasma.info) (wallet nexus: Dev Net)

If the wallet nexus does not match the site, you will see data from one network but sign on another. That causes inconsistent results or failed transactions. Always align them.

## Before you start

- Use a Phantasma Link [wallet](https://phantasma.info/blockchain/#wallets) (Poltergeist Lite or compatible) with Carbon support.
- Make sure you have enough KCAL for gas and enough SOUL for data escrow (maxData). The UI shows both in the Fees & limits panels (see the Fees section below).
- Prepare a small token icon as a base64 data URI (PNG, JPEG, or WebP). Size limits are listed below.

<a id="fees-kcal"></a>
## Fees: KCAL + SOUL (default estimates)

These are user-facing estimates based on current UI defaults; on-chain governance can change them. Always confirm the final fee shown by the wallet before signing.

Each tab has a **Fees & limits** panel. It shows **Estimated totals (max)**:
- **KCAL**: max gas (`maxGas`) calculated from the fee values you enter.
- **SOUL**: max data (`maxData`) cap for storage escrow.

These are maximums. The final amounts are computed on-chain and shown by the wallet. Unused gas or data escrow is refunded.

### KCAL gas (computation + bandwidth)

Estimated base fee (KCAL only, without SOUL data escrow):
- Create token: about 10,000 to 20,000 KCAL, depending on symbol length.
  - length 1 -> 20,000.01 KCAL
  - length 4 -> 11,250.01 KCAL
  - length 10 -> 10,019.54125 KCAL
  - Each extra symbol character halves the symbol fee, so longer symbols are slightly cheaper (within the range above).
- Create series: about 2,500.01 KCAL
- Mint NFT: about 0.001 KCAL (per NFT, plus SOUL data escrow)

KCAL covers execution cost and bandwidth (payload/result/events sizes). The wallet shows the final KCAL fee before signing.

### SOUL data escrow (maxData)

SOUL data escrow pays for permanent storage growth. It is not based on payload size.

How it works (chain behavior):
- Storage growth is measured in rows of 1024 bytes (1 KiB) of key/value data.
- For each state change, the key size and value size are added and rounded up to the next 1024-byte block (1 KiB).
- Only increases in row count are charged; deletions can refund SOUL.
- `dataFee = rowsAdded * dataEscrowPerRow` where `dataEscrowPerRow` is a governance parameter.
- The transaction sets `TxMsg.maxData` as the maximum SOUL escrow. If `dataFee > maxData`, the transaction is aborted.

UI specifics:
- **Max data (SOUL)** expects an integer in SOUL base units (1 SOUL = 100,000,000 base units).
- **Estimated totals (max)** shows both the human SOUL value and the base units for clarity.

## Deploy a token

1. Open the site and connect your wallet.
2. Pick token type: **Fungible** or **NFT**.
3. Fill symbol, metadata, decimals, and max supply (see details below).
4. For NFTs, confirm the token schemas (default is OK for most collections).
5. Click **Deploy Token** and confirm the transaction in the wallet.

<a id="symbol-rules"></a>
### Symbol rules

- Only uppercase Latin letters A-Z.
- Length: 1 to 255 characters (current chain limit).
- No digits, spaces, underscores, punctuation, or non-ASCII letters.
- Symbols must be unique on the target network.

Examples: `MYTOKEN` (valid), `TOKEN1`, `TOKEN_ABC`, `MY TOKEN` (invalid). The UI uppercases input automatically.

<a id="token-metadata"></a>
### Token metadata (token-level)

Token metadata is stored on-chain and is **required** for all tokens. All values must be strings.

Required fields:
- `name` - display name
- `icon` - base64 data URI, `data:image/png|jpeg|webp;base64,...`
- `url` - project URL
- `description` - short description

Icon rules:
- Only PNG, JPEG, or WebP data URIs are supported.
- The base64 payload must be valid and non-empty.
- Phantasma Link enforces a ~64 KB transaction size limit. The UI caps icon payloads at 30,000 base64 chars (about 22.5 KB), but you should still keep the icon small (roughly <= 22 KB) to avoid rejection.

You can add extra key/value metadata, but do **not** reuse reserved keys `name`, `icon`, `url`, `description`.

<a id="decimals-supply"></a>
### Decimals and supply

Decimals define how many digits are allowed after the decimal point, and therefore the smallest unit of the token.

- Example: decimals = 2 means 1.23 tokens are stored as 123 base units.
- The UI expects max supply in human units and converts it to base units by multiplying by 10^decimals.
- If decimals = 0, fractional values are not allowed.

Limits:
- Fungible tokens: decimals must be 0 to 64 (chain validation). The UI allows higher values but they will be rejected on-chain.
- Fungible max supply: up to 2^255 - 1 base units (about 5.79e76). This is a chain limit, not a recommendation.
- NFTs: decimals are fixed to 0.
- NFT max supply must fit into Int64 (<= 9,223,372,036,854,775,807).
- Max supply of `0` means **unlimited** supply.

Default UI values:
- Fungible decimals default to 8. NFT decimals default to 0.
- Max supply defaults to 0 (unlimited).

Example: decimals = 1 and max supply = 0.2 -> base units = 2.

<a id="nft-schemas"></a>
## NFT schemas and metadata

NFT tokens require schemas that describe what metadata fields exist and how to serialize them.

Schemas:
- **Series metadata (shared)** - stored once per series and shared by all NFTs in that series.
- **ROM (per NFT, immutable)** - stored per NFT instance and cannot be changed.
- **RAM (per NFT, mutable)** - optional; can be updated after minting.

Standard fields that must exist either in Series metadata or in NFT ROM:
`name`, `description`, `imageURL`, `infoURL`, `royalties`.

System fields are reserved and managed by the SDK: `id`, `mode`, `rom` (and internal `_i`). Do not create custom fields with these names.

Field names are case-sensitive. Duplicate names across Series and ROM are rejected.

### Field value rules (UI)

- `String` - non-empty text.
- `Int8/Int16/Int32/Int64/Int256` - signed integer (no decimals).
- `Bytes/Bytes16/Bytes32/Bytes64` - hex string, even length; optional `0x` prefix.
- Other complex VM types exist, but the UI only accepts raw strings. If you need arrays/structs, use the CLI or SDK.

Royalties input:
- Enter percentage (0 to 100) with up to 7 decimal places.
- On-chain value is `percent * 10^7` (example: `1%` -> `10000000`, `2.5%` -> `25000000`).

<a id="create-series"></a>
## Create an NFT series

1. Deploy an **NFT** token.
2. In the token list, select that token.
3. Open the **Series** tab.
4. Fill the required fields from the schema. Keep ROM hex as `0x` if you do not use shared ROM.
5. Sign the transaction. The UI will show the new **series ID**.

<a id="mint-nfts"></a>
## Mint NFTs

1. Select your NFT token in the list.
2. Open the **Mint** tab.
3. Choose the series ID.
4. Fill ROM metadata fields (all required).
5. If RAM schema exists, fill RAM fields too.
6. Sign the transaction. The UI will display minted NFT addresses and the Phantasma ID.

<a id="troubleshooting"></a>
## Troubleshooting

- **Token list looks wrong or transactions fail**: wallet nexus does not match the deployment site (Settings -> Nexus).
- **Symbol validation error**: use only A-Z with no digits or symbols.
- **Icon rejected**: not a valid data URI or the file is too large.
- **No series available**: create a series first.
