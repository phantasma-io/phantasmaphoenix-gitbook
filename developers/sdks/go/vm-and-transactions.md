# Go SDK VM And Transactions

A script transaction carries a VM script. The script names who pays the gas
and how much at most, then runs its calls: token transfers, staking, contract
calls. A transfer, mint or burn can also go as a structured transaction, which
carries no script; see [Carbon](/developers/sdks/go/carbon.md).

| Package | Import path | Holds |
| ------- | ----------- | ----- |
| `scriptbuilder` | `github.com/phantasma-io/phantasma-sdk-go/pkg/vm/script_builder` | `ScriptBuilder` and its call helpers. |
| `blockchain` | `github.com/phantasma-io/phantasma-sdk-go/pkg/blockchain` | `Transaction`, the script transaction. |
| `vm` | `github.com/phantasma-io/phantasma-sdk-go/pkg/vm` | Opcodes, `VMType`, `VMObject`. |
| `rpc` | `github.com/phantasma-io/phantasma-sdk-go/pkg/rpc` | Sending, reading the result, read-only scripts. |

## Build And Send

```go
package main

import (
    "context"
    "fmt"
    "log"
    "math/big"
    "os"
    "time"

    "github.com/phantasma-io/phantasma-sdk-go/pkg/cryptography"
    "github.com/phantasma-io/phantasma-sdk-go/pkg/rpc"
    scriptbuilder "github.com/phantasma-io/phantasma-sdk-go/pkg/vm/script_builder"
)

func main() {
    ctx, cancel := context.WithTimeout(context.Background(), 30*time.Second)
    defer cancel()

    keys, err := cryptography.FromWIF(os.Getenv("WIF"))
    if err != nil {
        log.Fatal(err)
    }
    to, err := cryptography.FromString(os.Getenv("TO"))
    if err != nil {
        log.Fatal(err)
    }

    // AllowGas names the gas payer and the most KCAL the transaction may spend.
    script, err := scriptbuilder.BeginScript().
        AllowGas(keys.Address(), cryptography.NullAddress(), big.NewInt(100_000), big.NewInt(9_999)).
        TransferTokens("KCAL", keys.Address(), to, big.NewInt(10_000_000_000)). // 1 KCAL, which has ten decimals
        EndScriptWithError()
    if err != nil {
        log.Fatal(err)
    }

    client := rpc.NewRPCTestnet()
    hash, err := client.SignAndSendTransaction(ctx, keys, "testnet", script, "main", []byte("example payload"))
    if err != nil {
        log.Fatal(err)
    }
    fmt.Println(hash)
}
```

Every script transaction calls `AllowGas(from, to, gasPrice, gasLimit)`, and
scripts built with `ScriptBuilder` call it first. The chain takes the gas payer
from `from`, who must sign the transaction, and the transaction's `maxGas` from
`gasPrice * gasLimit`, in KCAL atoms. A script without the call is rejected
with `No call to AllowGas`. The chain reserves that amount from the payer before
the script runs, charges the bill after it, and returns the rest. The example
offers 100,000 times 9,999 atoms, 0.09999 KCAL, so the payer needs at least that
much available. `to` is the dApp fee target; the null address names none.

A script transaction has no storage ceiling. When it adds contract storage, the
chain charges the SOUL deposit after the script, and the gas payer must hold
that SOUL. `SpendGas`, which many scripts call at the end, has no effect: the
chain settles the bill after the script either way.

`SignAndSendTransaction(ctx, keys, nexus, script, chainName, payload)` builds
the transaction, signs it, sends it with `sendRawTransaction` and returns the
hash the node reports. The nexus is `mainnet` or `testnet`, the chain `main`.
`payload` is bytes the transaction carries for the reader, for example an order
id. The transaction expires `carbon.DefaultTxExpiry` (45 seconds) after
signing; see [Expiration](#expiration).

## Script Helpers

| Helper | Emits |
| ------ | ----- |
| `AllowGas(from, to, gasPrice, gasLimit)` | `gas.AllowGas`. |
| `SpendGas(address)` | `gas.SpendGas`, which has no effect. |
| `TransferTokens(symbol, from, to, amount)` | `Runtime.TransferTokens`: `amount` atoms of a fungible token. |
| `TransferBalance(symbol, from, to)` | `Runtime.TransferBalance`: the whole balance of the token. |
| `TransferNFT(symbol, from, to, tokenID)` | `Runtime.TransferToken`: one NFT, named by its Phantasma NFT id. |
| `MintTokens(symbol, from, to, amount)` | `Runtime.MintTokens`, which runs the `onMint` trigger of the token's contract. |
| `Stake(address, amount)`, `Unstake(address, amount)` | `stake.Stake`, `stake.Unstake`, with SOUL atoms. |
| `CallNFT(symbol, seriesID, method, args...)` | A call into the contract of an NFT series, named `SYMBOL#seriesID` with the Phantasma series id. The series must carry a contract script. |
| `CrossTransferToken`, `CrossTransferNFT` | `Runtime.SendTokens`, `Runtime.SendToken`. The chain has neither interop, and the script faults. |
| `CallContract(contract, method, args...)` | Any contract method. |
| `CallInterop(method, args...)` | Any interop; the list is on [Interop](/developers/blockchain/chain/information/virtual-machine/interop.md). |

Every helper that takes `cryptography.Address` values has a form ending in
`Text` that takes address text: `AllowGasText`, `SpendGasText`,
`TransferTokensText`, `TransferTokensToText`, `TransferBalanceText`,
`TransferNFTText`, `TransferNFTToText`, `MintTokensText`, `StakeText`,
`UnstakeText`, and the cross-chain ones. These parse the text with
`cryptography.FromString` and also accept `NULL` for the null address. A text
that does not parse becomes a builder error.

The `stake` contract has four methods: `Stake(from, amount)`,
`Unstake(from, amount)`, `Claim(from, from)`, which claims the KCAL the stake
has generated, and `GetUnclaimed(from)`, which returns that amount. A call to
any other name faults. Of the native contracts, the VM loads only `gas` and
`stake`.

Amounts are atoms, the smallest unit of a token. `util.ConvertDecimalsBack`
from `github.com/phantasma-io/phantasma-sdk-go/pkg/util` converts text such as
`"1.5"` with the token's decimals into atoms and returns an error when the text
has more decimals than the token. `util.ConvertDecimals` converts back.

## Arguments

`CallContract`, `CallInterop` and `CallNFT` take their arguments as Go values:

| Go value | VM value |
| -------- | -------- |
| `string` | String |
| `bool` | Bool |
| `[]byte` | Bytes |
| any integer type, `*big.Int`, `big.Int` | Number |
| `time.Time` | Timestamp, in seconds |
| `cryptography.Address`, `*cryptography.Address` | Bytes: the address with its length byte |
| a slice or array of the above | An array |

Any other type, or `nil`, is a builder error. The chain reads an address
argument from address text as well as from address bytes, so a `string` with
the address also works. A `cryptography.Address` is checked before the
transaction is signed.

The builder collects the first error. `EndScriptWithError()` appends `RET` and
returns the script or that error; `EndScript()` panics on it. `ToScript()`
returns the script without appending `RET`. Copies of a `ScriptBuilder` share
one buffer, so start a new builder for each script.

## Low-Level Script Emission

The `Emit...` methods write single instructions:

```go
package main

import (
    "encoding/hex"
    "fmt"
    "log"

    "github.com/phantasma-io/phantasma-sdk-go/pkg/vm"
    scriptbuilder "github.com/phantasma-io/phantasma-sdk-go/pkg/vm/script_builder"
)

func main() {
    script, err := scriptbuilder.BeginScript().
        EmitLoadBool(0, true).
        EmitConditionalJump(vm.JMPIF, 0, "done").
        EmitLoadString(1, "skipped").
        EmitLabel("done").
        EmitLoadString(2, "Runtime.Time").
        EmitM(vm.EXTCALL, []byte{2}).
        EndScriptWithError()
    if err != nil {
        log.Fatal(err)
    }
    fmt.Println(hex.EncodeToString(script))
}
```

| Method | Writes |
| ------ | ------ |
| `EmitS(opcode)`, `EmitM(opcode, bytes)` | An opcode, with immediate bytes for `EmitM`. |
| `EmitLoad(reg, bytes, vmType)` | A `LOAD` of raw bytes with a VM type. More than 65,535 bytes is a builder error. |
| `EmitLoadString`, `EmitLoadBool`, `EmitLoadInt`, `EmitLoadNumberAsBinary`, `EmitLoadTime` | A `LOAD` of one Go value. |
| `EmitPush(reg)`, `EmitPop(reg)`, `EmitMove(src, dst)`, `EmitCopy(src, dst)` | Stack and register moves. |
| `EmitExtCall(method, reg)` | Loads the interop name into `reg` and calls it. |
| `EmitLabel(label)`, `EmitJump(opcode, label, reg)`, `EmitConditionalJump(opcode, reg, label)`, `EmitCall(label, regCount)` | Labels and jumps. Labels ignore case. A jump to an unknown label fails when the script is finished. |
| `EmitThrow(reg)` | `THROW`. |
| `EmitRaw(bytes)`, `EmitVarBytes(value)` | Raw bytes, a variable-length integer. |
| `CurrentSize()` | The script length so far. |

## Sign And Send Step By Step

```go
tx := blockchain.NewTransaction("testnet", "main", script, expirationUnix, []byte("example payload"))
if err := tx.Sign(keys); err != nil {
    return err
}

hash, err := client.SendRawTransaction(ctx, hex.EncodeToString(tx.Bytes()))
```

| Member | Meaning |
| ------ | ------- |
| `NewTransaction(nexus, chain, script, expiration, payload)` | A transaction that expires at `expiration`, in Unix seconds. It computes `Hash`. |
| `Sign(keyPair)` | Signs the unsigned bytes and appends the signature. |
| `Bytes()` | The signed transaction, the form `SendRawTransaction` takes as hex. |
| `BytesEx(false)` | The unsigned bytes, which a wallet signs. |
| `Hash` | The hash of the unsigned bytes. Set when the transaction is built or decoded; changing a field later does not update it. |
| `IsSignedBy(addresses)` | `true` when one of the signatures belongs to one of the addresses. |
| `Mine(difficulty)` | See [Proof Of Work](#proof-of-work). |
| `Serialize(writer)`, `Deserialize(reader)` | The binary form, through `pkg/io`. Only Ed25519 signatures are read back. |

The RPC client has shortcuts for the whole flow:

| Method | Does |
| ------ | ---- |
| `SignAndSendTransaction(ctx, keys, nexus, script, chain, payload)` | Builds a transaction that expires in 45 seconds, signs and sends it. |
| `SignAndSendTransactionWithExpiration(..., expiration)` | The same with an expiration in Unix seconds. |
| `SignAndSendTransactionTextPayload(..., payload)` | The same with a text payload. |
| `SignAndSendBuiltTransaction(ctx, tx, keys)` | Signs a built transaction and sends it. |

## Expiration

The chain accepts a transaction until its expiration and refuses an expiration
at or beyond its own window. A flow that waits for a person, for example a
confirmation dialog, takes the whole window:

```go
params, err := client.Fees().ChainParams(ctx, false)
if err != nil {
    return err
}
// The latest moment the chain accepts, minus five seconds of margin, in milliseconds.
expiryMs, err := carbon.ExpiryWithin(params.ExpiryWindow, 0)
if err != nil {
    return err
}
expiration := uint32(expiryMs / 1000)
```

Pass `expiration` to `SignAndSendTransactionWithExpiration` or
`NewTransaction`. A script transaction counts its expiration in seconds; a
structured transaction counts it in milliseconds.

## Proof Of Work

`Runtime.DeployContract`, `Runtime.UpgradeContract`, `Nexus.CreateToken` and
`Nexus.AttachTokenContract` run only in a script transaction whose hash has a
difficulty of at least 5. Other scripts need none.

```go
tx := blockchain.NewTransaction("mainnet", "main", script, expirationUnix, nil)
tx.Mine(5)
if err := tx.Sign(keys); err != nil {
    return err
}
```

`Mine(difficulty)` replaces the payload with a 4-byte counter and raises it until
`tx.Hash.GetDifficulty()` reaches the difficulty. Mine before signing: mining
changes the hash, and a signature made before it no longer matches.

## Read-Only Scripts

`InvokeRawScript(ctx, chain, scriptHex)` runs a script on the node without a
transaction. It needs no key and no gas:

```go
package main

import (
    "context"
    "encoding/hex"
    "fmt"
    "log"
    "os"
    "time"

    "github.com/phantasma-io/phantasma-sdk-go/pkg/cryptography"
    "github.com/phantasma-io/phantasma-sdk-go/pkg/rpc"
    scriptbuilder "github.com/phantasma-io/phantasma-sdk-go/pkg/vm/script_builder"
)

func main() {
    ctx, cancel := context.WithTimeout(context.Background(), 30*time.Second)
    defer cancel()

    account, err := cryptography.FromString(os.Getenv("ACCOUNT"))
    if err != nil {
        log.Fatal(err)
    }

    // The KCAL this account can claim from its SOUL stake, in KCAL atoms.
    script, err := scriptbuilder.BeginScript().
        CallContract("stake", "GetUnclaimed", account).
        EndScriptWithError()
    if err != nil {
        log.Fatal(err)
    }

    client := rpc.NewRPCMainnet()
    result, err := client.InvokeRawScript(ctx, "main", hex.EncodeToString(script))
    if err != nil {
        log.Fatal(err)
    }
    value, err := result.DecodeResultWithError()
    if err != nil {
        log.Fatal(err)
    }
    fmt.Println(value.AsNumber())
}
```

`Result` holds the last value the script left, and `Results` every value, each
a serialized VM object in hex. `DecodeResultWithError()` and
`DecodeResultsWithError(index)` decode them into a `vm.VMObject`, whose
`AsNumber`, `AsString`, `AsBool` and `AsBytes` convert the value. A conversion
that does not fit the stored type panics.

## The Result Of A Transaction

`GetTransaction(ctx, hash)` returns an error until the transaction is in a
block. Its `State` then tells the outcome:

| `State` | Meaning |
| ------- | ------- |
| `Halt` | The script completed. `StateIsSuccess()` is `true`. |
| `Break` | The script aborted. It changed nothing, and the gas payer paid the gas bill. `StateIsFault()` is `true`. |
| `Fault` | The chain rejected the transaction. `StateIsFault()` is `true`. |

`Result` holds the return value in hex and `Events` the events the transaction
emitted. This function waits for a final state:

```go
// waitForTransaction polls a transaction hash until the transaction reaches a final state or
// ctx ends.
func waitForTransaction(ctx context.Context, client rpc.PhantasmaRPC, hash string) (response.TransactionResult, error) {
    for {
        tx, err := client.GetTransaction(ctx, hash)
        if err == nil && (tx.StateIsSuccess() || tx.StateIsFault()) {
            return tx, nil
        }
        select {
        case <-ctx.Done():
            return response.TransactionResult{}, ctx.Err()
        case <-time.After(time.Second):
        }
    }
}
```

`response` is the package `github.com/phantasma-io/phantasma-sdk-go/pkg/rpc/response`.
The other Go pages use `waitForTransaction` after sending.

## Related Pages

{% content-ref url="/developers/sdks/go/fees-and-broadcasting.md" %}
[Fees And Broadcasting](/developers/sdks/go/fees-and-broadcasting.md)
{% endcontent-ref %}

{% content-ref url="/developers/sdks/go/reference/vm-transaction-binary.md" %}
[VM and Transaction APIs](/developers/sdks/go/reference/vm-transaction-binary.md)
{% endcontent-ref %}

{% content-ref url="/developers/script-builder/README.md" %}
[Script Builder](/developers/script-builder/README.md)
{% endcontent-ref %}
