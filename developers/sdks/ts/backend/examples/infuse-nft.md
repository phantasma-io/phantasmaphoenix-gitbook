# Infuse an NFT

Infusion in Carbon is a transfer to the target NFT's Carbon address. RPC builds the `infusion` list by reading balances at that address.

## Requirements

- Target NFT Carbon address (32-byte hex).
- Carbon token ID and instance IDs for infused NFTs, or carbon token ID and amount for fungible infusion.
- Signatures: the owner of the infused assets and the owner of the target NFT both sign (the `NftInfuseWitness` rule).

## Step 1: Resolve the target NFT Carbon address

### Option A: via RPC (recommended)

`getNFT` returns `carbonNftAddress` for a target NFT identified by its symbol and Phantasma ID.

```ts
import { Bytes32, PhantasmaAPI, hexToBytes } from "phantasma-sdk-ts/public";

const rpc = new PhantasmaAPI("https://testnet.phantasma.info/rpc", null, "testnet");
const target = await rpc.getNFT("TGT", "1234", true);
const targetNftAddress = new Bytes32(hexToBytes(target.carbonNftAddress));
```

`getTokenData` returns the same data but is a deprecated alias of `getNFT` on the RPC side.

### Option B: from mint result or carbon instance ID

If you already have the Carbon instance ID (from minting), build the address locally:

```ts
import { TokenHelper } from "phantasma-sdk-ts/public";

const targetNftAddress = TokenHelper.getNftAddress(carbonTokenId, carbonInstanceId);
```

If you just minted the NFT, read the instance id out of the mint result and
build the address from it:

```ts
import {
  MintPhantasmaNonFungibleTxHelper,
  TokenHelper,
} from "phantasma-sdk-ts/public";

const minted = MintPhantasmaNonFungibleTxHelper.parseResult(txInfo.result);
const targetNftAddress = TokenHelper.getNftAddress(carbonTokenId, minted[0].carbonInstanceId);
```

## Step 2: Infuse NFTs (Carbon transfer)

For NFT infusion you must transfer the infused NFT instance(s) to the target NFT address.
Carbon transfer uses **carbon token IDs** and **carbon instance IDs** (not the Phantasma NFT ID).

```ts
import {
  Bytes32,
  NativeTxHelper,
  PhantasmaAPI,
  PhantasmaKeys,
  hexToBytes,
} from "phantasma-sdk-ts/public";

export async function infuseSingleNft() {
  const rpc = new PhantasmaAPI("https://testnet.phantasma.info/rpc", null, "testnet");

  const signer = PhantasmaKeys.fromWIF("YOUR_WIF");
  const senderPk = new Bytes32(signer.publicKey);

  const target = await rpc.getNFT("TGT", "1234", true);
  const targetNftAddress = new Bytes32(hexToBytes(target.carbonNftAddress));

  const infusedTokenId = 555n; // carbon token id of the NFT you are infusing
  const infusedInstanceId = 42n; // carbon instance id of the NFT you are infusing

  const msg = NativeTxHelper.transferNonFungible({
    from: senderPk,
    to: targetNftAddress,
    tokenId: infusedTokenId,
    instanceIds: [infusedInstanceId],
  });

  return await rpc.sendTransaction(msg, signer);
}
```

`transferNonFungible` picks the single-instance type for one instance and the
multi-instance type for several. `sendTransaction` plans the fee from the
message, signs it and broadcasts it.

To infuse several instances of the same token ID, pass them all in
`instanceIds`. To infuse several token IDs in one transaction, build a
`TxMsgCallMulti` with `TokenContractMethods.TransferNonFungible`. The chain
bills a batch as the sum of its calls, with the envelope counted once.

## Step 3: Infuse fungible tokens (Carbon transfer)

Fungible infusion is also a transfer to the target NFT address. It uses the
fungible transfer builder. `amount` is an integer in the token's atoms.

```ts
import {
  Bytes32,
  NativeTxHelper,
  PhantasmaAPI,
  PhantasmaKeys,
  hexToBytes,
} from "phantasma-sdk-ts/public";

export async function infuseFungible() {
  const rpc = new PhantasmaAPI("https://testnet.phantasma.info/rpc", null, "testnet");

  const signer = PhantasmaKeys.fromWIF("YOUR_WIF");
  const senderPk = new Bytes32(signer.publicKey);

  const target = await rpc.getNFT("TGT", "1234", true);
  const targetNftAddress = new Bytes32(hexToBytes(target.carbonNftAddress));

  const fungibleTokenId = 777n; // carbon token id for the fungible token
  const amount = 1_000_000n; // in the token's atoms

  const msg = NativeTxHelper.transferFungible({
    from: senderPk,
    to: targetNftAddress,
    tokenId: fungibleTokenId,
    amount,
  });

  return await rpc.sendTransaction(msg, signer);
}
```

`parseUnits(value, decimals)` converts a decimal amount into atoms.

## Step 4: Verify infusion

`getNFT` returns an `infusion` list computed from balances at the target NFT address.
For fungibles, `key` is the token ID and `value` is the amount.
For NFTs, `key` is the token symbol and `value` is the infused NFT meta ID.

```ts
const updated = await rpc.getNFT("TGT", "1234", true);
console.log(updated.infusion);
```

## VM interop: Runtime.InfuseToken

If you need to infuse via the VM interop, use `Runtime.InfuseToken` with Phantasma IDs.
`nftId` is the target NFT Phantasma ID and `value` is the infused NFT Phantasma ID.

```ts
import { Address, ScriptBuilder } from "phantasma-sdk-ts/public";

const sb = new ScriptBuilder();
const script = sb
  .beginScript()
  .allowGas(senderAddress, Address.nullAddress, gasPrice, gasLimit)
  .callInterop("Runtime.InfuseToken", [
    senderAddress,
    targetSymbol,
    targetNftId,
    infuseSymbol,
    infuseNftId,
  ])
  .spendGas(senderAddress)
  .endScript();
```

Limitations (current behavior):

- Currently, when the target token is an NFT, `Runtime.InfuseToken` only supports NFT infusion.
- It does **not** currently support fungible infusion into an NFT. Use the Carbon transfer flow above for fungible infusion.
- `Runtime.TransferToken` refuses to send NFTs to NFT addresses; NFT infusion must use `Runtime.InfuseToken`.
