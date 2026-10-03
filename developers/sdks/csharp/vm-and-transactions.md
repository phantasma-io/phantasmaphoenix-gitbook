---
description: Build, sign and send script transactions, and run read-only scripts, in C#.
---

# Script Transactions

A script transaction carries a VM script. The script names who pays the gas and how much at most, then runs its calls. Token transfers, staking and contract calls all work this way. A transfer, mint or burn can also go as a structured transaction, which carries no script; see [Structured Transactions](/developers/sdks/csharp/carbon.md).

The types live in `PhantasmaPhoenix.VM` (`ScriptBuilder` and its extensions), `PhantasmaPhoenix.Protocol` (`Transaction`) and `PhantasmaPhoenix.RPC` (`PhantasmaAPI`).

## Build And Send

```csharp
using PhantasmaPhoenix.Cryptography;
using PhantasmaPhoenix.Protocol;
using PhantasmaPhoenix.RPC;
using PhantasmaPhoenix.VM;

using var api = new PhantasmaAPI("https://testnet.phantasma.info/rpc");
var keys = PhantasmaKeys.FromWIF(Environment.GetEnvironmentVariable("WIF")!);
var to = Address.Parse(Environment.GetEnvironmentVariable("TO")!);

// AllowGas names the gas payer and the most KCAL the transaction may spend.
var script = new ScriptBuilder()
	.AllowGas(keys.Address, Address.Null, DomainSettings.DefaultMinimumGasFee, Transaction.DefaultGasLimit)
	.TransferTokens("KCAL", keys.Address, to, 10_000_000_000) // 1 KCAL, which has ten decimals
	.EndScript();

var hash = await api.SignAndSendTransactionAsync(keys, "testnet", script, "main", "example payload");
Console.WriteLine(hash);
```

Every script transaction calls `AllowGas(from, to, gasPrice, gasLimit)`, and scripts built with `ScriptBuilder` call it first. The chain takes the gas payer from `from`, who must sign the transaction, and the transaction's `maxGas` from `gasPrice * gasLimit`, in KCAL atoms. A script without the call is rejected with `No call to AllowGas`. It reserves that amount from the payer before the script runs, charges the bill after it, and returns the rest. The example offers `DomainSettings.DefaultMinimumGasFee` (100000) times `Transaction.DefaultGasLimit` (9999), 0.09999 KCAL, so the payer needs at least that much available. `to` is the dApp fee target; `Address.Null` names none. The parameters and the other script helpers are listed on [Script Builder](/developers/script-builder/README.md).

A script transaction has no storage ceiling. When it adds contract storage, the chain charges the SOUL deposit after the script, and the gas payer must hold that SOUL. `SpendGas`, which many scripts call at the end, has no effect: the chain settles the bill after the script either way.

`SignAndSendTransactionAsync(keys, nexus, script, chain, payload, customSignFunction, expiration)` builds the transaction, signs it, sends it with `sendRawTransaction`, and returns the hash. It throws when the node does not answer with the hash computed locally. `payload` is a string or bytes the transaction carries for the reader, for example an order id.

## Expiration

A transaction stays admissible until its expiration. `SignAndSendTransactionAsync` sets it to `TxLimits.DefaultExpiryMs` (45 seconds) from now when `expiration` is not given. A flow that waits for a person, for example a confirmation dialog, takes the chain's own window instead:

```csharp
using PhantasmaPhoenix.Core;
using PhantasmaPhoenix.Protocol.Carbon.Blockchain.TxHelpers;
using PhantasmaPhoenix.RPC;

using var api = new PhantasmaAPI("https://testnet.phantasma.info/rpc");
var chainParams = await api.Fees.ChainParamsAsync();

// The latest moment the chain accepts, minus five seconds of margin, in milliseconds.
var expiryMs = TxLimits.ExpiryWithin(chainParams.ExpiryWindow);
var expiration = new Timestamp((uint)(expiryMs / 1000));
```

Pass `expiration` as the last argument of `SignAndSendTransactionAsync`. The chain refuses an expiration at or beyond its window.

## Sign Without Sending

```csharp
using PhantasmaPhoenix.Core;
using PhantasmaPhoenix.Cryptography;
using PhantasmaPhoenix.Protocol;
using PhantasmaPhoenix.Protocol.Carbon.Blockchain.TxHelpers;

var keys = PhantasmaKeys.FromWIF(Environment.GetEnvironmentVariable("WIF")!);
var script = Environment.GetEnvironmentVariable("SCRIPT_HEX")!.Decode()!; // a script built as above

var tx = new Transaction("testnet", "main", script, new Timestamp((uint)(TxLimits.DefaultExpiry() / 1000)), "example payload");
var hash = tx.Sign(keys);
var signedHex = Base16.Encode(tx.ToByteArray(true));
```

`tx.Sign(keys)` signs the unsigned bytes, appends the signature and returns the transaction hash. `tx.ToByteArray(false)` gives the unsigned bytes, which a wallet signs over Phantasma Link; `AddSignature` appends a signature made elsewhere. `api.SendRawTransactionAsync(signedHex)` broadcasts the result.

## Read-Only Scripts

`InvokeRawScriptAsync(chain, scriptHex)` runs a script on the node without a transaction. It needs no key and no gas. Each result is a serialized VM object in hex:

```csharp
using PhantasmaPhoenix.Cryptography;
using PhantasmaPhoenix.RPC;
using PhantasmaPhoenix.VM;

using var api = new PhantasmaAPI("https://pharpc1.phantasma.info/rpc");
var account = Address.Parse(Environment.GetEnvironmentVariable("ACCOUNT")!);

// The KCAL this account can claim from its SOUL stake, in KCAL atoms.
var script = new ScriptBuilder()
	.CallContract("stake", "GetUnclaimed", account)
	.EndScript();

var result = await api.InvokeRawScriptAsync("main", Base16.Encode(script));
var unclaimed = VMObject.FromBytes(Base16.Decode(result!.Results[0])!).AsNumber();
Console.WriteLine(unclaimed);
```

`VMObject` converts a result with `AsNumber`, `AsString`, `AsBool`, `AsTimestamp`, `AsByteArray` and the other members listed on [Keys, VM, and Transactions](/developers/sdks/csharp/reference/keys-vm-and-transactions.md#vm-objects). A conversion that does not fit the stored type throws. Which interops and native contracts a script can call is described on [Interop](/developers/blockchain/chain/information/virtual-machine/interop.md).

## The Result Of A Transaction

`GetTransactionAsync(hash)` returns the transaction once it is in a block. `State` tells the outcome:

| `ExecutionState` | Meaning |
| --- | --- |
| `Halt` | The script completed. |
| `Break` | The script aborted. It changed nothing, and the gas payer paid the gas bill. |
| `Fault` | The chain rejected the transaction. |
| `Running` | The transaction is not final yet. |

`Result` holds the script's return value in hex, and `Events` the events it emitted. The [Check Transaction State](/developers/sdks/csharp/examples/check-transaction-state.md) example polls a hash until it reaches a final state.

## Related Pages

{% content-ref url="/developers/script-builder/README.md" %}
Script Builder
{% endcontent-ref %}

{% content-ref url="/developers/sdks/csharp/fees-and-broadcasting.md" %}
Fees And Broadcasting
{% endcontent-ref %}

{% content-ref url="/developers/sdks/csharp/reference/keys-vm-and-transactions.md" %}
Keys, VM, and Transactions
{% endcontent-ref %}
