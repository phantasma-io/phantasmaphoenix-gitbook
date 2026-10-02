# Interop

Interop calls are the bridge between VM bytecode and native chain functionality. A script uses `EXTCALL` with a method name such as `Runtime.TransferTokens` or `Data.Get`, and the validator handles the real token, NFT, storage, or contract lifecycle operation in native code.

This page lists the interops the node implements and the names it rejects.

## Runtime Context And Utility

| Method | Args | Status | Notes |
| --- | --- | --- | --- |
| `Runtime.GasTarget` | none | implemented | Returns the gas target address for the current execution. |
| `Runtime.Context` | none | implemented | Requires a real current context; rejects if context is not available yet. |
| `Runtime.PreviousContext` | none | implemented | Returns the parent context name. |
| `Runtime.IsTrigger` | none | implemented | Returns whether the current execution is inside a trigger path. |
| `Runtime.GenerateUID` | none | implemented | Returns an id that is unique within the execution. |
| `Runtime.Time` | none | implemented | Returns current block time as VM timestamp. |
| `Runtime.Version` | none | implemented | Returns current VM behavior version. |
| `Runtime.IsWitness` | `address` | implemented | Checks whether the address is currently witnessed. |
| `Runtime.Log` | `message` | implemented | Emits a VM-side log line. |
| `Runtime.Notify` | `eventKind, address, payload` | implemented | Requires a real deployed contract context. The kind must be `Custom_V2`; any other kind fails with `contract events must use Runtime.NotifyV2 (Custom_V2)`. |
| `Runtime.NotifyV2` | `name, address, payload` | implemented | Requires a real deployed contract context. Emits an event with kind `Custom_V2` that carries the event name. `pha-tomb` 2.2.0 and later compile `emit` to this call. |

The node rejects these names:

- `Runtime.TransactionHash`
- `Runtime.Validator`
- `Runtime.Random`
- `Runtime.SetSeed`
- `Runtime.IsMinter`
- `Runtime.AESEncrypt`
- `Runtime.AESDecrypt`

## Contract Lifecycle

| Method | Args | Status | Notes |
| --- | --- | --- | --- |
| `Runtime.DeployContract` | `from, contractName, script, abi` | implemented | Deploys a standalone custom contract. Requires minimal proof of work. Custom names are lowercase. |
| `Runtime.UpgradeContract` | `from, contractName, script, abi` | implemented | Upgrades an existing deployed contract. Also used later for token-backed contracts after they already exist. Requires minimal proof of work. |
| `Runtime.KillContract` | `from, contractName` | not implemented | Rejected. |
| `Nexus.CreateToken` | `from, script, abi` | implemented | Creates a new token-backed contract from contract metadata. Requires minimal proof of work. |
| `Nexus.AttachTokenContract` | `from, symbol, script, abi` | implemented | Attaches VM code to an existing token. Requires minimal proof of work. |

Important lifecycle rules:

- `Runtime.DeployContract` is for standalone custom contracts, not uppercase token symbols.
- `Nexus.CreateToken` is the install path for a new token-backed contract.
- `Nexus.AttachTokenContract` is the install path for an existing token that does not yet have VM code attached.
- `Runtime.UpgradeContract` is the later update path for both standalone contracts and already-installed token-backed contracts.
- Token-backed create and attach flows require a valid token contract shape. In practice, `onMint` is mandatory.

## Fungible Token Operations

| Method | Args | Status | Notes |
| --- | --- | --- | --- |
| `Runtime.GetBalance` | `address, symbol` | implemented | Returns the current fungible balance. |
| `Runtime.TransferTokens` | `source, destination, symbol, amount` | implemented | Main fungible transfer interop. |
| `Runtime.TransferBalance` | `source, destination, symbol` | implemented | Transfers the full current balance for that symbol. |
| `Runtime.MintTokens` | `source, destination, symbol, amount` | implemented | Runs `onMint` on a token-backed contract; the mint is applied only when the trigger succeeds. |
| `Runtime.BurnTokens` | `address, symbol, amount` | implemented | Burns a fungible amount. |
| `Runtime.SwapTokens` | - | not implemented | Rejected. |

## NFT And Token-Backed Operations

| Method | Args | Status | Notes |
| --- | --- | --- | --- |
| `Runtime.GetOwnerships` | `address, symbol` | implemented | NFT-only. Returns a deterministic `BigInteger[]`-style VM object of owned Phantasma NFT IDs. |
| `Runtime.GetOwnershipsBySeries` | `address, symbol, seriesID` | implemented | NFT-only. Like `GetOwnerships`, but limited to a single series. |
| `Runtime.TransferToken` | `source, destination, symbol, tokenID` | implemented | Uses runtime-visible Phantasma NFT IDs, not raw Carbon instance IDs. |
| `Runtime.MintToken` | `source, destination, symbol, rom, ram, seriesID` | implemented | Uses Phantasma series metadata IDs and preserves VM-facing ROM behavior. Triggers `onMint` when token-backed contract code exists. |
| `Runtime.BurnToken` | `source, symbol, tokenID` | implemented | NFT burn path. |
| `Runtime.InfuseToken` | `source, targetSymbol, tokenID, infuseSymbol, value` | implemented | Supported infuse path for token-backed NFT operations. |
| `Runtime.ReadTokenROM` | `symbol, tokenID` | implemented | Reads runtime-visible ROM. |
| `Runtime.ReadTokenRAM` | `symbol, tokenID` | implemented | Reads runtime-visible RAM. |
| `Runtime.ReadToken` | `symbol, tokenID[, fields]` | implemented | Returns a map-like VM object for requested fields. Defaults to `chain,owner,creator,ROM,RAM,tokenID,seriesID,mintID,infusion`. |
| `Runtime.ReadInfusions` | `symbol, tokenID` | implemented | Rebuilds Phantasma-style infusion view from current Carbon balances. |
| `Runtime.WriteToken` | `from, symbol, tokenID, ram` | implemented | Updates NFT RAM by runtime-visible Phantasma NFT ID. Invokes `onWrite` before the native RAM update when a token-backed trigger exists. |

`Runtime.ReadToken` and the other NFT interops identify an NFT by its public Phantasma NFT id. The internal instance id is a storage detail.

`Runtime.WriteToken` follows the same runtime-visible NFT ID rule. It replaces RAM bytes, accepts empty RAM to clear the RAM flag, does not change owner, ROM, or token supply, and rolls back the RAM update plus trigger storage writes if `onWrite` fails. Native token symbols and dangerous symbols are rejected.

## Token Metadata And Discovery

| Method | Args | Status | Notes |
| --- | --- | --- | --- |
| `Runtime.TokenExists` | `symbol` | implemented | Returns `false` for unknown symbols instead of hard failing. |
| `Runtime.GetTokenDecimals` | `symbol` | implemented | Reads token decimals from current token metadata. |
| `Runtime.GetTokenFlags` | `symbol` | implemented | Reads current token flags. |
| `Runtime.GetTokenOwner` | `symbol` | implemented | Returns the current token owner address object. |

`Runtime.GetTokenSupply` and `Runtime.GetAvailableTokenSymbols` appear in older documentation but are not part of the current Carbon VM interop surface; calls to them are rejected.

## NFT Series

| Method | Args | Status | Notes |
| --- | --- | --- | --- |
| `Nexus.CreateTokenSeries` | `from, symbol, seriesID, maxSupply, mode, script, abi` | implemented | Uses Phantasma metadata `_i` for series identity and validates the caller before running `onSeries`. |

Important notes:

- series creation is separate from token creation or token attach
- same-token token-backed series flows preserve both token identity and outer user witness where required
- series metadata persists canonical Phantasma fields for later runtime use

## Contract Storage

These are the storage primitives contract authors rely on most.

| Method | Args | Status | Notes |
| --- | --- | --- | --- |
| `Data.Get` | `contractName, field, vmType` | implemented | Reads a contract scalar field and returns a typed default when missing. |
| `Data.Set` | `field, value` | implemented | Writes into the current deployed contract context only. |
| `Data.Delete` | `field` | implemented | Deletes a scalar field from the current deployed contract context. |
| `Map.Has` | `contractName, field, key, keyType` | implemented | Checks whether a map-style entry exists. The current implementation consumes the extra type argument for compatibility even though the existence check itself is key-based. |
| `Map.Get` | `contractName, field, key, vmType` | implemented | Reads a map entry and returns a typed default when missing. |
| `Map.Set` | `field, key, value` | implemented | Updates table storage and keeps canonical entry counts. |
| `Map.Remove` | `field, key` | implemented | Removes an entry and updates count. |
| `Map.Count` | `contractName, field` | implemented | Returns current entry count. |
| `Map.Clear` | `field` | implemented | Deletes all entries and resets count. |
| `Map.Keys` | `contractName, field` | implemented | Returns a byte-array vector of current keys. |
| `List.Get` | `contractName, field, index, vmType` | implemented | Reads by zero-based index. |
| `List.Add` | `field, value` | implemented | Appends at the current tail index. |
| `List.Replace` | `field, index, value` | implemented | Replaces an existing list entry. |
| `List.RemoveAt` | `field, index` | implemented | Uses compact swap-with-last semantics. |
| `List.Count` | `contractName, field` | implemented | Returns current list length. |
| `List.Clear` | `field` | implemented | Deletes list entries and resets count. |

Storage behavior notes:

- write methods operate on the current deployed contract context, not an arbitrary named contract
- read methods can target another contract by name
- the node keeps an entry count per map and list field, and rejects storage whose count and entries disagree

## Account And Constructor Helpers

| Method | Args | Status | Notes |
| --- | --- | --- | --- |
| `Account.Name` | `address` | implemented | Resolves a name through governance lookup. |
| `Address()` | `addressLike` | implemented | Builds or normalizes an address object. |
| `Hash()` | `hashLike` | implemented | Builds a hash object. |
| `Timestamp()` | `timestampLike` | implemented | Builds a timestamp value. |

The node rejects these names:

- `Account.LastActivity`
- `Account.Transactions`
- `ABI()`

## Organization, Oracle, And Task Namespaces

The node rejects these names:

- `Organization.AddMember`
- `Organization.RemoveMember`
- `Organization.Kill`
- `Oracle.Read`
- `Oracle.Price`
- `Oracle.Quote`
- `Task.Start`
- `Task.Stop`
- `Task.Get`
- `Task.Current`
- `Nexus.GetGovernanceValue`
- `Nexus.BeginInit`
- `Nexus.EndInit`
- `Nexus.MigrateToken`
- `Nexus.CreateChain`
- `Nexus.CreatePlatform`
- `Nexus.CreateOrganization`
- `Nexus.SetPlatformTokenHash`

## Developer Guidance

If you are writing new contracts today:

- use `Runtime.DeployContract` and `Runtime.UpgradeContract` for standalone contracts
- use `Nexus.CreateToken`, `Nexus.AttachTokenContract`, and later `Runtime.UpgradeContract` for token-backed contracts
- rely on `Data.*`, `Map.*`, and `List.*` for persistent state
- rely on `Runtime.MintTokens`, `Runtime.TransferTokens`, `Runtime.MintToken`, `Runtime.TransferToken`, `Runtime.ReadToken`, `Runtime.WriteToken`, and `Nexus.CreateTokenSeries` for current token and NFT flows
- do not build contracts or examples around names the node rejects
