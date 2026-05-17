# TypeScript SDK VM And Transaction APIs

This page covers the public TypeScript APIs for keys, addresses, VM scripts,
transactions, binary helpers, VM object decoding, and event helpers.

## Keys, Addresses, And Signatures

| API | Purpose |
| --- | ------- |
| `PhantasmaKeys.generate()` | Creates a random Ed25519 key pair. |
| `PhantasmaKeys.fromWIF(wif)` | Imports a WIF private key. |
| `keys.privateKey`, `keys.publicKey`, `keys.address` | Canonical key accessors. |
| `keys.toWIF()` | Exports WIF. |
| `keys.sign(message)` | Signs a byte array. |
| `Address.fromText(text)` / `Address.parse(text)` | Parses address text. |
| `Address.fromPublicKey(publicKey)` | Builds a user address from a public key. |
| `Address.nullAddress` | Null address singleton. |
| `Address.isValidAddress(text)` | Boolean validation helper. |
| `Ed25519Signature.verify(message, address)` | Verifies one signature. |

PascalCase address/key aliases remain for compatibility and are marked
deprecated in the type declarations.

## ScriptBuilder

`ScriptBuilder` is a chainable VM script builder. Use `ScriptBuilder.create()`
or `new ScriptBuilder()`.

| API | Purpose |
| --- | ------- |
| `beginScript()` | Starts a script chain. |
| `getScript()` | Returns current script hex. |
| `endScript()` | Appends `RET` and returns final script hex. |
| `emit(...)`, `emitPush`, `emitPop`, `emitExtCall`, `emitLoad...` | Low-level opcode and value emitters. |
| `emitLabel`, `emitJump`, `emitCall`, `emitConditionalJump` | Label and branch helpers. |
| `callInterop(method, args)` | Emits a VM interop call. |
| `callContract(contractName, method, args)` | Emits a contract call. |
| `allowGas`, `spendGas` | Gas helpers. |
| `mintTokens`, `transferTokens`, `transferBalance`, `transferNft` | Token helpers. |
| `crossTransferToken`, `crossTransferNft` | Cross-chain helpers. |
| `stake`, `unstake`, `callNft` | Stake and NFT helpers. |
| `appendHexEncoded(bytes)` | Appends already-encoded bytecode. |

Deprecated PascalCase aliases remain for older consumers and are planned for
removal at v1.0.

## Transaction

`Transaction` represents a classic VM script transaction.

| API | Purpose |
| --- | ------- |
| `new Transaction(nexusName, chainName, script, expiration, payload)` | Creates an unsigned transaction. |
| `Transaction.fromHex(serializedData)` | Parses serialized hex. |
| `Transaction.fromBytes(serializedData)` | Parses serialized bytes. |
| `sign(wif)`, `signWithPrivateKey(privateKey)`, `signWithKeys(keys)` | Signing helpers. |
| `verifySignature(address)` / `verifySignatures(addresses)` | Signature checks. |
| `getUnsignedBytes()` | Returns unsigned transaction bytes. |
| `toByteArray(withSignature)` | Serializes to bytes. |
| `toString(withSignature)` | Serializes to hex. |
| `toStringEncoded(withSignature)` | Serializes bytes with Base16 encoding. |
| `getHash()` | Computes and stores transaction hash. |
| `mineTransaction(difficulty)` | Mutates transaction payload for proof of work. |
| `deserialize(serialized)` | Static deserializer for bytes. |

Use `toStringEncoded(true)` or `toString(true)` for `sendRawTransaction` only
after the transaction has the required signatures.

## VM Objects And Event Helpers

| API | Purpose |
| --- | ------- |
| `VMObject`, `VMType`, `decodeVMObject` | VM result decoding and typed conversion. |
| `Decoder` | Script/result decoder helper. |
| `Opcode` | VM opcode enum. |
| `getTokenEventData`, `getGasEventData`, `getMarketEventData`, `getInfusionEventData`, `getChainValueEventData`, `getTransactionSettleEventData` | Event data decoders. |

## Binary And Utility Helpers

| API | Purpose |
| --- | ------- |
| `PBinaryReader`, `PBinaryWriter` | VM binary format reader/writer. |
| `CarbonBinaryReader`, `CarbonBinaryWriter` | Carbon wire-format reader/writer. |
| `Base16`, `bytesToHex`, `hexToBytes`, `decodeBase16`, `encodeBase16` | Hex helpers. |
| `bigIntToTwosComplementLE`, `twosComplementLEToBigInt` | Integer encoding helpers. |
| `getDifficulty` | Proof-of-work difficulty helper. |
| `isValidIdentifier`, `isReservedIdentifier`, `isValidTicker` | Naming validators. |
