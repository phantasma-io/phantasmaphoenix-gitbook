---
title: "C++ SDK VM And Transactions"
linkTitle: "VM and Transactions"
weight: 40
---

A script transaction carries a VM script. The script names who pays the gas
and how much at most, then runs its calls: token transfers, staking, contract
calls. A transfer, mint or burn can also go as a structured transaction, which
carries no script; see [Carbon](carbon.md).

| Header | Holds |
| ------ | ----- |
| `VM/ScriptBuilder.h` | `ScriptBuilder` and its call helpers. |
| `Blockchain/Transaction.h` | `Transaction`, the script transaction. |
| `VM/VMObject.h`, `VM/Opcodes.h` | VM values and opcodes. |
| `Utils/RpcUtils.h` | `SignAndSendTransaction` and the confirmation helpers. |

## Build And Send

```cpp
#define PHANTASMA_IMPLEMENTATION
#include "Adapters/PhantasmaAPI_rapidjson.h"
#include "Adapters/PhantasmaAPI_curl.h"
#include "PhantasmaAPI.h"
#include "Adapters/PhantasmaAPI_openssl.h"
#include "Carbon/Carbon.h"
#include "VM/ScriptBuilder.h"
#include "Utils/RpcUtils.h"
#include <cstdlib>
#include <iostream>

using namespace phantasma;

int main()
{
    const char* wif = std::getenv("WIF");
    const char* to = std::getenv("TO");
    if( !wif || !to )
        return 1;

    PhantasmaKeys keys = PhantasmaKeys::FromWIF(wif);
    bool badAddress = false;
    Address receiver = Address::FromText(to, 0, &badAddress);
    if( keys.IsNull() || badAddress )
        return 1;

    // AllowGas names the gas payer and the most KCAL the transaction may spend.
    ByteArray script = ScriptBuilder::BeginScript()
                           .AllowGas(keys.GetAddress(), Address(), BigInteger(100000), BigInteger(9999))
                           .TransferTokens("KCAL", keys.GetAddress(), receiver, BigInteger(10000000000)) // 1 KCAL, which has ten decimals
                           .EndScript();

    HttpClient http("https://testnet.phantasma.info"); // the API adds /rpc
    rpc::PhantasmaAPI api(http);
    rpc::PhantasmaError err{};
    String hash = SignAndSendTransaction(api, keys, "testnet", "main", script, String("example payload"), &err);
    if( err.code != 0 )
        return 1;

    std::cout << hash << std::endl;
    return 0;
}
```

Every script transaction calls `AllowGas(from, to, gasPrice, gasLimit)`, and
scripts built with `ScriptBuilder` call it first. The chain takes the gas payer
from `from`, who must sign the transaction, and the transaction's `maxGas` from
`gasPrice * gasLimit`, in KCAL atoms. A script without the call is rejected
with `No call to AllowGas`. The chain reserves that amount from the payer before
the script runs, charges the bill after it, and returns the rest. The example
offers 100,000 times 9,999 atoms, 0.09999 KCAL, so the payer needs at least that
much available. `to` is the dApp fee target; `Address()`, the null address,
names none.

A script transaction has no storage ceiling. When it adds contract storage, the
chain charges the SOUL deposit after the script, and the gas payer must hold
that SOUL. `SpendGas`, which many scripts call at the end, has no effect: the
chain settles the bill after the script either way.

`SignAndSendTransaction(api, keys, nexus, chain, script, payload, &err,
expiration)` builds the transaction, signs it, sends it with
`sendRawTransaction` and returns the hash the node reports. The nexus is
`mainnet` or `testnet`, the chain `main`. Without `expiration` the transaction
expires 45 seconds after signing (`DefaultScriptExpiration()`); see
[Expiration](#expiration). When the node reports a hash other than the one
computed locally, it throws or, without exceptions, returns the node's answer.

## Script Helpers

| Helper | Emits |
| ------ | ----- |
| `AllowGas(from, to, gasPrice, gasLimit)` | `gas.AllowGas`. |
| `SpendGas(address)` | `gas.SpendGas`, which has no effect. |
| `TransferTokens(symbol, from, to, amount)` | `Runtime.TransferTokens`: `amount` atoms of a fungible token. `to` is an `Address` or address text. |
| `TransferBalance(symbol, from, to)` | `Runtime.TransferBalance`: the whole balance of the token. |
| `TransferToken(symbol, from, to, nftId)` | `Runtime.TransferToken`: one NFT, named by its Phantasma NFT id. |
| `MintTokens(symbol, from, to, amount)` | `Runtime.MintTokens`, which runs the `onMint` trigger of the token's contract. |
| `BurnTokens(from, symbol, amount)`, `BurnToken(from, symbol, nftId)` | `Runtime.BurnTokens`, `Runtime.BurnToken`. |
| `WriteToken(from, symbol, nftId, ram)` | `Runtime.WriteToken`: replaces the RAM of an NFT. |
| `ReadTokenRAMToRegister(symbol, nftId, reg)`, `WriteTokenFromRegister(from, symbol, nftId, reg)` | The RAM of an NFT through a register. |
| `Stake(address, amount)` | `stake.Stake`, with SOUL atoms. |
| `CallContract(contract, method, args...)` | Any contract method. |
| `CallInterop(method, args...)` | Any interop; the list is on [Interop](../../blockchain/chain/information/virtual-machine/interop.md). |

The `stake` contract has four methods: `Stake(from, amount)`,
`Unstake(from, amount)`, `Claim(from, from)`, which claims the KCAL the stake
has generated, and `GetUnclaimed(from)`, which returns that amount. The builder
has a helper for `Stake` only; the others go through `CallContract`:

```cpp
ScriptBuilder sb;
sb.AllowGas(from, Address(), BigInteger(100000), BigInteger(9999))
    .CallContract("stake", "Claim", from, from);
ByteArray claimScript = sb.EndScript();
```

A call to any other `stake` method faults. Of the native contracts, the VM
loads only `gas` and `stake`.

## Arguments

`CallContract` and `CallInterop` take their arguments as C++ values:

| Value | VM value |
| ----- | -------- |
| `String`, `const Char*` | String |
| `Int32`, `Int64`, `BigInteger` | Number |
| `bool` | Bool |
| `ByteArray` | Bytes |
| `Timestamp` | Timestamp |
| An enum | Enum |
| `Address` and other serializable types | Bytes: the serialized value |
| `PHANTASMA_VECTOR<T>` | An array; it uses the two registers after the target register |

The chain reads an address argument from address text as well as from address
bytes, so a string with the address also works.

## Low-Level Script Emission

`ScriptBuilder` also writes single instructions: `Emit(opcode, bytes,
count)`, `EmitLoad(reg, value)`, `EmitPush`, `EmitPop`, `EmitMove`, `EmitCopy`,
`EmitExtCall(method, reg)`, the logic and comparison emitters such as
`EmitAnd`, `EmitEqual` and `EmitLessThan`, and the jumps `EmitLabel`,
`EmitJump`, `EmitConditionalJump` and `EmitCall`. `EndScript()` appends `RET`
and resolves the jumps. `EmitRaw(bytes, count)` and `EmitVarBytes(value)`
append raw bytes.

```cpp
ScriptBuilder sb;
sb.EmitLoad(0, true)
    .EmitConditionalJump(Opcode::JMPIF, 0, "done")
    .EmitLoad(1, String("skipped"))
    .EmitLabel("done")
    .EmitExtCall("Runtime.Time", 2);
ByteArray timeScript = sb.EndScript();
```

## The Transaction

```cpp
#include "Blockchain/Transaction.h"

Transaction tx("testnet", "main", script, DefaultScriptExpiration(), String("example payload"));
tx.Sign(keys);

String signedHex = Base16::Encode(tx.ToByteArray(true));
String hash = api.SendRawTransaction(signedHex.c_str(), &err);
```

| Member | Meaning |
| ------ | ------- |
| `Transaction(nexus, chain, script, expiration, payload)` | A transaction that expires at `expiration`, a `Timestamp` in seconds. The payload is a `String` or bytes. |
| `Sign(keys)` | Signs the unsigned bytes and appends the signature. |
| `ToByteArray(true)`, `ToByteArray(false)` | The signed transaction, or the unsigned bytes a wallet signs. |
| `GetHash()` | The hash of the unsigned bytes. |
| `IsSignedBy(address)` | Whether one of the signatures belongs to the address. |
| `Mine(difficulty)` | See [Proof Of Work](#proof-of-work). |
| `Transaction::Unserialize<BinaryReader>(bytes, count)` | Reads a serialized transaction. |
| `NexusName()`, `ChainName()`, `Script()`, `Expiration()`, `Payload()`, `Signatures()` | The fields. |

## Expiration

The chain accepts a transaction until its expiration and refuses an expiration
at or beyond its own window. `DefaultScriptExpiration()` gives 45 seconds from
now. A flow that waits for a person takes the whole window: read
`expiryWindow` from `GetGasConfig`, and pass
`Timestamp((Timestamp::ValueType)(carbon::ExpiryWithin(expiryWindowMs) / 1000))`.
A script transaction counts its expiration in seconds; a structured
transaction counts it in milliseconds.

## Proof Of Work

`Runtime.DeployContract`, `Runtime.UpgradeContract`, `Nexus.CreateToken` and
`Nexus.AttachTokenContract` run only in a script transaction whose hash has a
difficulty of at least 5. Other scripts need none.

```cpp
Transaction mined("mainnet", "main", script, DefaultScriptExpiration(), ByteArray());
mined.Mine(5); // ProofOfWork::Minimal of Cryptography/PoW.h
mined.Sign(keys);
```

`Mine` adds a 4-byte counter to the payload, after the payload's own bytes, and
raises it until `GetHash().GetDifficulty()` reaches the difficulty. It refuses a
transaction that is already signed, because mining changes the hash.

## Read-Only Scripts

`InvokeRawScript(chain, scriptHex, &err)` runs a script on the node without a
transaction. It needs no key and no gas:

```cpp
ScriptBuilder reader;
reader.CallContract("stake", "GetUnclaimed", address);
ByteArray readScript = reader.EndScript();

rpc::Script result = api.InvokeRawScript("main", Base16::Encode(readScript).c_str(), &err);
if( err.code == 0 && !result.results.empty() )
{
    VMObject value = VMObject::FromBytes(Base16::Decode(result.results[0]));
    BigInteger unclaimed = value.AsNumber(); // KCAL atoms
}
```

`results` holds every value the script left, each a serialized VM object in
hex, and `result` the last of them. `AsNumber`, `AsString`, `AsBool` and
`AsByteArray` convert a `VMObject`. A script that aborted comes back as error
`-4` with the reason in `message`; see [Errors](rpc.md#errors).

## The Result Of A Transaction

`GetTransaction(hash, &err)` answers an error until the transaction is in a
block. Its `state` then tells the outcome:

| `state` | Meaning |
| ------- | ------- |
| `Halt` | The script completed. |
| `Break` | The script aborted. It changed nothing, and the gas payer paid the gas bill. |
| `Fault` | The chain rejected the transaction. |

`result` holds the return value in hex and `events` the events the
transaction emitted. `WaitForConfirmation(apis, count, hash, expiry, output,
sleep)` in `Utils/RpcUtils.h` polls until the node returns the transaction or
reports it rejected; check `output.state` afterwards.

## Related Pages

- [Fees And Broadcasting](fees-and-broadcasting.md)
- [VM and Transaction APIs](reference/vm-transaction-binary.md)
- [Script Builder](../../script-builder/_index.md)
