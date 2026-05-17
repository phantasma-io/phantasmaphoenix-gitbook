# C++ SDK Carbon Operations

Use direct Carbon message structures when a workflow is outside the lifecycle
builder set.

## Transaction Payloads

The Carbon blockchain data headers include typed payloads for:

| Group | Structures |
| ----- | ---------- |
| Calls | `TxMsgCall`, `TxMsgCallMulti`, call argument sections |
| Fungible transfers | transfer, gas-payer transfer, mint, and burn payloads |
| NFT transfers | single, multi, gas-payer, mint, and burn payloads |
| Trades | `TxMsgTrade` and token listing structures |
| VM bridge | `TxMsgPhantasma`, `TxMsgPhantasmaRaw` |

Construct direct messages only when the higher-level helpers do not cover the
operation. The lifecycle helpers also handle fee defaults, expiry defaults, and
payload storage ownership.

## Module Calls

`ModuleId` and `TokenContract_Methods` in `Carbon/Tx.h` provide the module and
method ids used by token builders. For custom calls, serialize the argument
blob, assign the module and method ids, then sign the `TxMsg`.

## Archive And Auction Caveat

The generated C++ RPC header marks archive and leaderboard/organization-style
methods as stubbed in the current node/API surface. Treat those wrappers as
interface-only wrappers until live node behavior is verified.
