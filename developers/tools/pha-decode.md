# pha-decode

CLI tool for decoding Phantasma transactions (Carbon + VM) and legacy event hex.

## What it can decode

- Carbon transactions (Call, Call_Multi, mint, burn, transfer).
- VM transactions (script disassembly and method calls).
- Legacy event hex payloads (classic events).
- JSON or pretty text output.
- Optional ABI resolution from local files or RPC.

## Requirements

- Node.js with ESM support (Node 18+ recommended).

## Installation

```bash
# install globally
npm i -g pha-decode

# or run once via npx
npx pha-decode --help

# local dev install
npm install
npm run build
```

## Quick start

Decode a local transaction hex (shorthand):

```bash
pha-decode 0xDEADBEEF...
```

Decode a transaction hash from RPC:

```bash
pha-decode tx --hash 155422A6882C3342933521DDC1A335292BF6448DBD489ED0BE21CFC74AFBA52A \
  --rpc https://pharpc1.phantasma.info/rpc \
  --format json \
  --vm-detail calls \
  --carbon-detail call
```

Decode legacy event hex:

```bash
pha-decode event --hex 0xAABBCC... --kind TokenMint
```

## Commands and inputs

`pha-decode` supports two commands:

- `tx` (default): decode a transaction from hex (`--hex`) or from hash (`--hash` + `--rpc`).
- `event`: decode legacy event data from hex (`--hex`) with an optional event kind (`--kind`).

Input rules:

- Hex strings may include `0x` prefix and must have even length.
- `--hash` requires `--rpc`.
- `event` mode requires `--hex`.

## Output formats

`--format` controls output:

- `pretty` (default): human readable sections.
- `json`: machine friendly output.

JSON output structure (example):

```json
{
  "source": "tx-hash",
  "input": "155422A6...",
  "rpc": { "url": "https://...", "method": "getTransaction" },
  "carbon": { "...": "..." },
  "vm": { "...": "..." },
  "event": { "...": "..." },
  "warnings": [],
  "errors": []
}
```

## Option reference

General:

- `--format <json|pretty>` Output format (default: `pretty`).
- `--rpc <url>` RPC endpoint for `--hash`.
- `--resolve` Fetch contract ABIs from RPC and merge into the method table.
- `--abi <path>` ABI JSON file or directory (merged with built-ins).
- `--protocol <number>` Protocol version used for ABI selection (default: latest known).
- `--protocol-version <number>` Alias for `--protocol`.
- `--verbose` Enable SDK logging.
- `--help` Show help.

VM output detail:

- `--vm-detail <all|calls|ops|none>` Control VM output (default: `all`).
  - Accepted aliases: `both` -> `all`, `methods` -> `calls`, `opcodes` -> `ops`, `off` -> `none`.

Carbon output detail:

- `--carbon-detail <all|call|msg|none>` Control Carbon output (default: `call`).

Event decoding:

- `--kind <eventKind>` Event kind hint for legacy event hex. Accepts numeric id or name.

### Event mode rules

When `event` is selected:

- `--abi`, `--resolve`, `--vm-detail`, and `--carbon-detail` are ignored.
- If `--kind` is omitted or unknown, the tool returns raw hex with a warning.

## ABI resolution

The decoder starts with built-in ABI definitions. You can add more:

- `--abi <path>` loads a JSON file or a directory of JSON files and merges into the method table.
- `--resolve` uses the RPC `getContracts` output and merges contract methods.

If the RPC returns no contracts or a method is unknown, the decoder keeps raw hex values
and adds warnings instead of guessing.

## Event kinds (legacy)

`--kind` accepts either the numeric id or the name (case-insensitive, whitespace ignored).

| Id | Name |
| --- | --- |
| 0 | Unknown |
| 1 | ChainCreate |
| 2 | TokenCreate |
| 3 | TokenSend |
| 4 | TokenReceive |
| 5 | TokenMint |
| 6 | TokenBurn |
| 7 | TokenStake |
| 8 | TokenClaim |
| 9 | AddressRegister |
| 10 | AddressLink |
| 11 | AddressUnlink |
| 12 | OrganizationCreate |
| 13 | OrganizationAdd |
| 14 | OrganizationRemove |
| 15 | GasEscrow |
| 16 | GasPayment |
| 17 | AddressUnregister |
| 18 | OrderCreated |
| 19 | OrderCancelled |
| 20 | OrderFilled |
| 21 | OrderClosed |
| 22 | FeedCreate |
| 23 | FeedUpdate |
| 24 | FileCreate |
| 25 | FileDelete |
| 26 | ValidatorPropose |
| 27 | ValidatorElect |
| 28 | ValidatorRemove |
| 29 | ValidatorSwitch |
| 30 | PackedNFT |
| 31 | ValueCreate |
| 32 | ValueUpdate |
| 33 | PollCreated |
| 34 | PollClosed |
| 35 | PollVote |
| 36 | ChannelCreate |
| 37 | ChannelRefill |
| 38 | ChannelSettle |
| 39 | LeaderboardCreate |
| 40 | LeaderboardInsert |
| 41 | LeaderboardReset |
| 42 | PlatformCreate |
| 43 | ChainSwap |
| 44 | ContractRegister |
| 45 | ContractDeploy |
| 46 | AddressMigration |
| 47 | ContractUpgrade |
| 48 | Log |
| 49 | Inflation |
| 50 | OwnerAdded |
| 51 | OwnerRemoved |
| 52 | DomainCreate |
| 53 | DomainDelete |
| 54 | TaskStart |
| 55 | TaskStop |
| 56 | CrownRewards |
| 57 | Infusion |
| 58 | Crowdsale |
| 59 | OrderBid |
| 60 | ContractKill |
| 61 | OrganizationKill |
| 62 | MasterClaim |
| 63 | ExecutionFailure |
| 64 | Custom |
| 65 | Custom_V2 |
