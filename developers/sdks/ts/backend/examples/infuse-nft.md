# Infuse an NFT

Infusion in Carbon is a transfer to the target NFT's Carbon address. RPC builds the `infusion` list by reading balances at that address.

## Requirements

- Target NFT Carbon address (32-byte hex).
- Carbon token ID and instance IDs for infused NFTs, or carbon token ID and amount for fungible infusion.
- Signatures: the owner of the infused assets must sign; with FeatureLevel max (`NftInfuseWitness` active), the target NFT owner must also sign.

## Step 1: Resolve the target NFT Carbon address

### Option A: via RPC (recommended)

`getNFT` returns `carbonNftAddress` for a target NFT identified by its symbol and Phantasma ID.

```ts
import { Bytes32, PhantasmaAPI, hexToBytes } from "phantasma-sdk-ts";

const rpc = new PhantasmaAPI("https://testnet.phantasma.info/rpc", null, "testnet");
const target = await rpc.getNFT("TGT", "1234", true);
const targetNftAddress = new Bytes32(hexToBytes(target.carbonNftAddress));
```

`getTokenData` returns the same data but is a deprecated alias of `getNFT` on the RPC side.

### Option B: from mint result or carbon instance ID

If you already have the Carbon instance ID (from minting), build the address locally:

```ts
import { TokenHelper } from "phantasma-sdk-ts";

const targetNftAddress = TokenHelper.getNftAddress(carbonTokenId, carbonInstanceId);
```

If you just minted the NFT, you can parse the result and use the returned `Bytes32` address directly:

```ts
import { MintNonFungibleTxHelper } from "phantasma-sdk-ts";

const carbonNftAddresses = MintNonFungibleTxHelper.parseResult(carbonTokenId, txInfo.result);
const targetNftAddress = carbonNftAddresses[0];
```

## Step 2: Infuse NFTs (Carbon transfer)

For NFT infusion you must transfer the infused NFT instance(s) to the target NFT address.
Carbon transfer uses **carbon token IDs** and **carbon instance IDs** (not the Phantasma NFT ID).

```ts
import {
  Bytes32,
  FeeOptions,
  PhantasmaAPI,
  PhantasmaKeys,
  SmallString,
  TxMsg,
  TxMsgSigner,
  TxMsgTransferNonFungibleSingle,
  TxTypes,
  bytesToHex,
  hexToBytes,
} from "phantasma-sdk-ts";

export async function infuseSingleNft() {
  const rpc = new PhantasmaAPI("https://testnet.phantasma.info/rpc", null, "testnet");

  const signer = PhantasmaKeys.fromWIF("YOUR_WIF");
  const senderPk = new Bytes32(signer.PublicKey);

  const target = await rpc.getNFT("TGT", "1234", true);
  const targetNftAddress = new Bytes32(hexToBytes(target.carbonNftAddress));

  const infusedTokenId = 555n; // carbon token id of the NFT you are infusing
  const infusedInstanceId = 42n; // carbon instance id of the NFT you are infusing

  const fee = new FeeOptions();
  const expiry = BigInt(Date.now() + 60_000);

  const msg = new TxMsgTransferNonFungibleSingle({
    to: targetNftAddress,
    tokenId: infusedTokenId,
    instanceId: infusedInstanceId,
  });

  const tx = new TxMsg(
    TxTypes.TransferNonFungible_Single,
    expiry,
    fee.calculateMaxGas(1),
    0n,
    senderPk,
    SmallString.empty,
    msg,
  );

  const signed = TxMsgSigner.signAndSerialize(tx, signer);
  const txHash = await rpc.sendCarbonTransaction(bytesToHex(signed));
  return txHash;
}
```

If you want to infuse multiple instances of the same token ID, use `TxMsgTransferNonFungibleMulti`.
If you need multiple token IDs in a single transaction, use `TxMsgCallMulti` with `TokenContract_Methods.TransferNonFungible` (see `token-deployment-frontend/src/lib/phantasma/infuse.ts`).

## Step 3: Infuse fungible tokens (Carbon transfer)

Fungible infusion is also a transfer to the target NFT address, but it uses `TxMsgTransferFungible`.
`amount` is an integer in token base units.

```ts
import {
  Bytes32,
  FeeOptions,
  PhantasmaAPI,
  PhantasmaKeys,
  SmallString,
  TxMsg,
  TxMsgSigner,
  TxMsgTransferFungible,
  TxTypes,
  bytesToHex,
  hexToBytes,
} from "phantasma-sdk-ts";

export async function infuseFungible() {
  const rpc = new PhantasmaAPI("https://testnet.phantasma.info/rpc", null, "testnet");

  const signer = PhantasmaKeys.fromWIF("YOUR_WIF");
  const senderPk = new Bytes32(signer.PublicKey);

  const target = await rpc.getNFT("TGT", "1234", true);
  const targetNftAddress = new Bytes32(hexToBytes(target.carbonNftAddress));

  const fungibleTokenId = 777n; // carbon token id for the fungible token
  const amount = 1_000_000n;

  const fee = new FeeOptions();
  const expiry = BigInt(Date.now() + 60_000);

  const msg = new TxMsgTransferFungible(targetNftAddress, fungibleTokenId, amount);

  const tx = new TxMsg(
    TxTypes.TransferFungible,
    expiry,
    fee.calculateMaxGas(),
    0n,
    senderPk,
    SmallString.empty,
    msg,
  );

  const signed = TxMsgSigner.signAndSerialize(tx, signer);
  const txHash = await rpc.sendCarbonTransaction(bytesToHex(signed));
  return txHash;
}
```

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
import { ScriptBuilder } from "phantasma-sdk-ts";

const sb = new ScriptBuilder();
const script = sb
  .BeginScript()
  .AllowGas(senderAddress, sb.NullAddress, gasPrice, gasLimit)
  .CallInterop("Runtime.InfuseToken", [
    senderAddress,
    targetSymbol,
    targetNftId,
    infuseSymbol,
    infuseNftId,
  ])
  .SpendGas(senderAddress)
  .EndScript();
```

Limitations (current behavior):

- Currently, when the target token is an NFT, `Runtime.InfuseToken` only supports NFT infusion.
- It does **not** currently support fungible infusion into an NFT. Use the Carbon transfer flow above for fungible infusion.
- `Runtime.TransferToken` refuses to send NFTs to NFT addresses; NFT infusion must use `Runtime.InfuseToken`.
