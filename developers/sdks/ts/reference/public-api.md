# TypeScript SDK Public API Inventory

This page lists public classes, methods, functions, enum values, fields, and
constants from the cited source baseline. Use it to check exact names when
working with lower-level SDK APIs.

Source baseline:

| Item | Value |
| ---- | ----- |
| Source repo | `phantasma-sdk-ts` |
| Source commit | `fbd458026479e02a5caecc6cd8244d7f1e54e504` |
| Scope | declaration files under `dist/types`, matching package export and deep-import surfaces |

## Package Exports

Declared export targets from `package.json`:

- `phantasma-sdk-ts`: `./dist/types/index.d.ts` (available)
- `phantasma-sdk-ts/core`: `./dist/types/core/index.d.ts` (available)
- `phantasma-sdk-ts/core/*`: `./dist/types/core/*.d.ts` (available)
- `phantasma-sdk-ts/core/interfaces`: `./dist/types/core/interfaces/index.d.ts` (available)
- `phantasma-sdk-ts/core/ledger`: `./dist/types/core/ledger/index.d.ts` (available)
- `phantasma-sdk-ts/core/link`: `./dist/types/core/link/index.d.ts` (available)
- `phantasma-sdk-ts/core/rpc`: `./dist/types/core/rpc/index.d.ts` (available)
- `phantasma-sdk-ts/core/tx`: `./dist/types/core/tx/index.d.ts` (available)
- `phantasma-sdk-ts/core/types`: `./dist/types/core/types/index.d.ts` (available)
- `phantasma-sdk-ts/core/utils`: `./dist/types/core/utils/index.d.ts` (available)
- `phantasma-sdk-ts/core/vm`: `./dist/types/core/vm/index.d.ts` (available)
- `phantasma-sdk-ts/interfaces`: `./dist/types/interfaces/index.d.ts` (available)
- `phantasma-sdk-ts/interfaces/*`: `./dist/types/interfaces/*.d.ts` (available)
- `phantasma-sdk-ts/ledger`: `./dist/types/ledger/index.d.ts` (available)
- `phantasma-sdk-ts/ledger/*`: `./dist/types/ledger/*.d.ts` (available)
- `phantasma-sdk-ts/link`: `./dist/types/link/index.d.ts` (available)
- `phantasma-sdk-ts/link/*`: `./dist/types/link/*.d.ts` (available)
- `phantasma-sdk-ts/public`: `./dist/types/public.d.ts` (available)
- `phantasma-sdk-ts/rpc`: `./dist/types/rpc/index.d.ts` (available)
- `phantasma-sdk-ts/rpc/*`: `./dist/types/rpc/*.d.ts` (available)
- `phantasma-sdk-ts/tx`: `./dist/types/tx/index.d.ts` (available)
- `phantasma-sdk-ts/tx/*`: `./dist/types/tx/*.d.ts` (available)
- `phantasma-sdk-ts/types`: `./dist/types/types/index.d.ts` (available)
- `phantasma-sdk-ts/types/*`: `./dist/types/types/*.d.ts` (available)
- `phantasma-sdk-ts/utils`: `./dist/types/utils/index.d.ts` (available)
- `phantasma-sdk-ts/utils/*`: `./dist/types/utils/*.d.ts` (available)
- `phantasma-sdk-ts/vm`: `./dist/types/vm/index.d.ts` (available)
- `phantasma-sdk-ts/vm/*`: `./dist/types/vm/*.d.ts` (available)

## phantasma-sdk-ts/core

Source: `dist/types/core/index.d.ts`

### Declarations

```ts
export * from '../rpc/phantasma.js';
```

```ts
export * from '../rpc/index.js';
```

```ts
export * from '../vm/index.js';
```

```ts
export * from '../tx/index.js';
```

```ts
export * from '../utils/index.js';
```

```ts
export * from '../types/index.js';
```

```ts
export * from '../interfaces/index.js';
```

```ts
export * from '../ledger/index.js';
```

```ts
export * from '../link/index.js';
```

## phantasma-sdk-ts/core/interfaces/Carbon/ICarbonBlob

Source: `dist/types/core/interfaces/Carbon/ICarbonBlob.d.ts`

### Declarations

```ts
export * from '../../../interfaces/carbon/carbon-blob-like.js';
```

## phantasma-sdk-ts/core/interfaces/Carbon

Source: `dist/types/core/interfaces/Carbon/index.d.ts`

### Declarations

```ts
export * from '../../../interfaces/carbon/index.js';
```

## phantasma-sdk-ts/core/interfaces/IContract

Source: `dist/types/core/interfaces/IContract.d.ts`

### Declarations

```ts
export * from '../../interfaces/contract.js';
```

## phantasma-sdk-ts/core/interfaces/IKeyPair

Source: `dist/types/core/interfaces/IKeyPair.d.ts`

### Declarations

```ts
export * from '../../interfaces/key-pair.js';
```

## phantasma-sdk-ts/core/interfaces/ISerializable

Source: `dist/types/core/interfaces/ISerializable.d.ts`

### Declarations

```ts
export * from '../../interfaces/serializable.js';
```

## phantasma-sdk-ts/core/interfaces/IStack

Source: `dist/types/core/interfaces/IStack.d.ts`

### Declarations

```ts
export * from '../../interfaces/stack.js';
```

## phantasma-sdk-ts/core/interfaces/IToken

Source: `dist/types/core/interfaces/IToken.d.ts`

### Declarations

```ts
export * from '../../interfaces/token.js';
```

## phantasma-sdk-ts/core/interfaces/Signature

Source: `dist/types/core/interfaces/Signature.d.ts`

### Declarations

```ts
export * from '../../interfaces/signature.js';
```

## phantasma-sdk-ts/core/interfaces

Source: `dist/types/core/interfaces/index.d.ts`

### Declarations

```ts
export * from '../../interfaces/index.js';
```

## phantasma-sdk-ts/core/ledger/Address-Transcode

Source: `dist/types/core/ledger/Address-Transcode.d.ts`

### Declarations

```ts
export * from '../../ledger/address-transcode.js';
```

## phantasma-sdk-ts/core/ledger/Ledger-Commands

Source: `dist/types/core/ledger/Ledger-Commands.d.ts`

### Declarations

```ts
export * from '../../ledger/ledger-commands.js';
```

## phantasma-sdk-ts/core/ledger/Ledger-Utils

Source: `dist/types/core/ledger/Ledger-Utils.d.ts`

### Declarations

```ts
export * from '../../ledger/ledger-utils.js';
```

## phantasma-sdk-ts/core/ledger/Mnemonic

Source: `dist/types/core/ledger/Mnemonic.d.ts`

### Declarations

```ts
export * from '../../ledger/mnemonic.js';
```

## phantasma-sdk-ts/core/ledger/Transaction-Sign

Source: `dist/types/core/ledger/Transaction-Sign.d.ts`

### Declarations

```ts
export * from '../../ledger/transaction-sign.js';
```

## phantasma-sdk-ts/core/ledger/Transaction-Transcode

Source: `dist/types/core/ledger/Transaction-Transcode.d.ts`

### Declarations

```ts
export * from '../../ledger/transaction-transcode.js';
```

## phantasma-sdk-ts/core/ledger

Source: `dist/types/core/ledger/index.d.ts`

### Declarations

```ts
export * from '../../ledger/index.js';
```

## phantasma-sdk-ts/core/ledger/interfaces/ApplicationNameResponse

Source: `dist/types/core/ledger/interfaces/ApplicationNameResponse.d.ts`

### Declarations

```ts
export * from '../../../ledger/interfaces/application-name-response.js';
```

## phantasma-sdk-ts/core/ledger/interfaces/Device

Source: `dist/types/core/ledger/interfaces/Device.d.ts`

### Declarations

```ts
export * from '../../../ledger/interfaces/device.js';
```

## phantasma-sdk-ts/core/ledger/interfaces/DeviceResponse

Source: `dist/types/core/ledger/interfaces/DeviceResponse.d.ts`

### Declarations

```ts
export * from '../../../ledger/interfaces/device-response.js';
```

## phantasma-sdk-ts/core/ledger/interfaces/Ledger

Source: `dist/types/core/ledger/interfaces/Ledger.d.ts`

### Declarations

```ts
export * from '../../../ledger/interfaces/ledger.js';
```

## phantasma-sdk-ts/core/ledger/interfaces/LedgerBalanceFromLedgerResponse

Source: `dist/types/core/ledger/interfaces/LedgerBalanceFromLedgerResponse.d.ts`

### Declarations

```ts
export * from '../../../ledger/interfaces/ledger-balance-from-ledger-response.js';
```

## phantasma-sdk-ts/core/ledger/interfaces/LedgerConfig

Source: `dist/types/core/ledger/interfaces/LedgerConfig.d.ts`

### Declarations

```ts
export * from '../../../ledger/interfaces/ledger-config.js';
```

## phantasma-sdk-ts/core/ledger/interfaces/LedgerDeviceInfoResponse

Source: `dist/types/core/ledger/interfaces/LedgerDeviceInfoResponse.d.ts`

### Declarations

```ts
export * from '../../../ledger/interfaces/ledger-device-info-response.js';
```

## phantasma-sdk-ts/core/ledger/interfaces/LedgerSendTransactionResponse

Source: `dist/types/core/ledger/interfaces/LedgerSendTransactionResponse.d.ts`

### Declarations

```ts
export * from '../../../ledger/interfaces/ledger-send-transaction-response.js';
```

## phantasma-sdk-ts/core/ledger/interfaces/LedgerSigner

Source: `dist/types/core/ledger/interfaces/LedgerSigner.d.ts`

### Declarations

```ts
export * from '../../../ledger/interfaces/ledger-signer.js';
```

## phantasma-sdk-ts/core/ledger/interfaces/LedgerSignerData

Source: `dist/types/core/ledger/interfaces/LedgerSignerData.d.ts`

### Declarations

```ts
export * from '../../../ledger/interfaces/ledger-signer-data.js';
```

## phantasma-sdk-ts/core/ledger/interfaces/PublicKeyResponse

Source: `dist/types/core/ledger/interfaces/PublicKeyResponse.d.ts`

### Declarations

```ts
export * from '../../../ledger/interfaces/public-key-response.js';
```

## phantasma-sdk-ts/core/ledger/interfaces/SignResponse

Source: `dist/types/core/ledger/interfaces/SignResponse.d.ts`

### Declarations

```ts
export * from '../../../ledger/interfaces/sign-response.js';
```

## phantasma-sdk-ts/core/ledger/interfaces/VersionResponse

Source: `dist/types/core/ledger/interfaces/VersionResponse.d.ts`

### Declarations

```ts
export * from '../../../ledger/interfaces/version-response.js';
```

## phantasma-sdk-ts/core/ledger/interfaces

Source: `dist/types/core/ledger/interfaces/index.d.ts`

### Declarations

```ts
export * from '../../../ledger/interfaces/index.js';
```

## phantasma-sdk-ts/core/link/easyConnect

Source: `dist/types/core/link/easyConnect.d.ts`

### Declarations

```ts
export * from '../../link/easy-connect.js';
```

## phantasma-sdk-ts/core/link/easyScript

Source: `dist/types/core/link/easyScript.d.ts`

### Declarations

```ts
export * from '../../link/easy-script.js';
```

## phantasma-sdk-ts/core/link

Source: `dist/types/core/link/index.d.ts`

### Declarations

```ts
export * from '../../link/index.js';
```

## phantasma-sdk-ts/core/link/interfaces/IAccount

Source: `dist/types/core/link/interfaces/IAccount.d.ts`

### Declarations

```ts
export * from '../../../link/interfaces/account.js';
```

## phantasma-sdk-ts/core/link/interfaces/IFile

Source: `dist/types/core/link/interfaces/IFile.d.ts`

### Declarations

```ts
export * from '../../../link/interfaces/file.js';
```

## phantasma-sdk-ts/core/link/interfaces/ProofOfWork

Source: `dist/types/core/link/interfaces/ProofOfWork.d.ts`

### Declarations

```ts
export * from '../../../link/interfaces/proof-of-work.js';
```

## phantasma-sdk-ts/core/link/interfaces

Source: `dist/types/core/link/interfaces/index.d.ts`

### Declarations

```ts
export * from '../../../link/interfaces/index.js';
```

## phantasma-sdk-ts/core/link/phantasmaLink

Source: `dist/types/core/link/phantasmaLink.d.ts`

### Declarations

```ts
export * from '../../link/phantasma-link.js';
```

## phantasma-sdk-ts/core/rpc/helpers

Source: `dist/types/core/rpc/helpers/index.d.ts`

### Declarations

```ts
export * from '../../../rpc/helpers/index.js';
```

## phantasma-sdk-ts/core/rpc/helpers/vmSchemaHelpers

Source: `dist/types/core/rpc/helpers/vmSchemaHelpers.d.ts`

### Declarations

```ts
export * from '../../../rpc/helpers/vm-schema-helpers.js';
```

## phantasma-sdk-ts/core/rpc

Source: `dist/types/core/rpc/index.d.ts`

### Declarations

```ts
export * from '../../rpc/index.js';
```

## phantasma-sdk-ts/core/rpc/interfaces/ABIContract

Source: `dist/types/core/rpc/interfaces/ABIContract.d.ts`

### Declarations

```ts
export * from '../../../rpc/interfaces/abi-contract.js';
```

## phantasma-sdk-ts/core/rpc/interfaces/ABIEvent

Source: `dist/types/core/rpc/interfaces/ABIEvent.d.ts`

### Declarations

```ts
export * from '../../../rpc/interfaces/abi-event.js';
```

## phantasma-sdk-ts/core/rpc/interfaces/ABIMethod

Source: `dist/types/core/rpc/interfaces/ABIMethod.d.ts`

### Declarations

```ts
export * from '../../../rpc/interfaces/abi-method.js';
```

## phantasma-sdk-ts/core/rpc/interfaces/ABIParameter

Source: `dist/types/core/rpc/interfaces/ABIParameter.d.ts`

### Declarations

```ts
export * from '../../../rpc/interfaces/abi-parameter.js';
```

## phantasma-sdk-ts/core/rpc/interfaces/Account

Source: `dist/types/core/rpc/interfaces/Account.d.ts`

### Declarations

```ts
export * from '../../../rpc/interfaces/account.js';
```

## phantasma-sdk-ts/core/rpc/interfaces/AccountTransactions

Source: `dist/types/core/rpc/interfaces/AccountTransactions.d.ts`

### Declarations

```ts
export * from '../../../rpc/interfaces/account-transactions.js';
```

## phantasma-sdk-ts/core/rpc/interfaces/Archive

Source: `dist/types/core/rpc/interfaces/Archive.d.ts`

### Declarations

```ts
export * from '../../../rpc/interfaces/archive.js';
```

## phantasma-sdk-ts/core/rpc/interfaces/Auction

Source: `dist/types/core/rpc/interfaces/Auction.d.ts`

### Declarations

```ts
export * from '../../../rpc/interfaces/auction.js';
```

## phantasma-sdk-ts/core/rpc/interfaces/Balance

Source: `dist/types/core/rpc/interfaces/Balance.d.ts`

### Declarations

```ts
export * from '../../../rpc/interfaces/balance.js';
```

## phantasma-sdk-ts/core/rpc/interfaces/Block

Source: `dist/types/core/rpc/interfaces/Block.d.ts`

### Declarations

```ts
export * from '../../../rpc/interfaces/block.js';
```

## phantasma-sdk-ts/core/rpc/interfaces/BuildInfoResult

Source: `dist/types/core/rpc/interfaces/BuildInfoResult.d.ts`

### Declarations

```ts
export * from '../../../rpc/interfaces/build-info-result.js';
```

## phantasma-sdk-ts/core/rpc/interfaces/Chain

Source: `dist/types/core/rpc/interfaces/Chain.d.ts`

### Declarations

```ts
export * from '../../../rpc/interfaces/chain.js';
```

## phantasma-sdk-ts/core/rpc/interfaces/Channel

Source: `dist/types/core/rpc/interfaces/Channel.d.ts`

### Declarations

```ts
export * from '../../../rpc/interfaces/channel.js';
```

## phantasma-sdk-ts/core/rpc/interfaces/Contract

Source: `dist/types/core/rpc/interfaces/Contract.d.ts`

### Declarations

```ts
export * from '../../../rpc/interfaces/contract.js';
```

## phantasma-sdk-ts/core/rpc/interfaces/CursorPaginatedResult

Source: `dist/types/core/rpc/interfaces/CursorPaginatedResult.d.ts`

### Declarations

```ts
export * from '../../../rpc/interfaces/cursor-paginated-result.js';
```

## phantasma-sdk-ts/core/rpc/interfaces/Dapp

Source: `dist/types/core/rpc/interfaces/Dapp.d.ts`

### Declarations

```ts
export * from '../../../rpc/interfaces/dapp.js';
```

## phantasma-sdk-ts/core/rpc/interfaces/Event

Source: `dist/types/core/rpc/interfaces/Event.d.ts`

### Declarations

```ts
export * from '../../../rpc/interfaces/event.js';
```

## phantasma-sdk-ts/core/rpc/interfaces/EventExtended

Source: `dist/types/core/rpc/interfaces/EventExtended.d.ts`

### Declarations

```ts
export * from '../../../rpc/interfaces/event-extended.js';
```

## phantasma-sdk-ts/core/rpc/interfaces/Governance

Source: `dist/types/core/rpc/interfaces/Governance.d.ts`

### Declarations

```ts
export * from '../../../rpc/interfaces/governance.js';
```

## phantasma-sdk-ts/core/rpc/interfaces/Interop

Source: `dist/types/core/rpc/interfaces/Interop.d.ts`

### Declarations

```ts
export * from '../../../rpc/interfaces/interop.js';
```

## phantasma-sdk-ts/core/rpc/interfaces/KeyValue

Source: `dist/types/core/rpc/interfaces/KeyValue.d.ts`

### Declarations

```ts
export * from '../../../rpc/interfaces/key-value.js';
```

## phantasma-sdk-ts/core/rpc/interfaces/Leaderboard

Source: `dist/types/core/rpc/interfaces/Leaderboard.d.ts`

### Declarations

```ts
export * from '../../../rpc/interfaces/leaderboard.js';
```

## phantasma-sdk-ts/core/rpc/interfaces/LeaderboardRow

Source: `dist/types/core/rpc/interfaces/LeaderboardRow.d.ts`

### Declarations

```ts
export * from '../../../rpc/interfaces/leaderboard-row.js';
```

## phantasma-sdk-ts/core/rpc/interfaces/NFT

Source: `dist/types/core/rpc/interfaces/NFT.d.ts`

### Declarations

```ts
export * from '../../../rpc/interfaces/nft.js';
```

## phantasma-sdk-ts/core/rpc/interfaces/Nexus

Source: `dist/types/core/rpc/interfaces/Nexus.d.ts`

### Declarations

```ts
export * from '../../../rpc/interfaces/nexus.js';
```

## phantasma-sdk-ts/core/rpc/interfaces/Oracle

Source: `dist/types/core/rpc/interfaces/Oracle.d.ts`

### Declarations

```ts
export * from '../../../rpc/interfaces/oracle.js';
```

## phantasma-sdk-ts/core/rpc/interfaces/Organization

Source: `dist/types/core/rpc/interfaces/Organization.d.ts`

### Declarations

```ts
export * from '../../../rpc/interfaces/organization.js';
```

## phantasma-sdk-ts/core/rpc/interfaces/Paginated

Source: `dist/types/core/rpc/interfaces/Paginated.d.ts`

### Declarations

```ts
export * from '../../../rpc/interfaces/paginated.js';
```

## phantasma-sdk-ts/core/rpc/interfaces/Peer

Source: `dist/types/core/rpc/interfaces/Peer.d.ts`

### Declarations

```ts
export * from '../../../rpc/interfaces/peer.js';
```

## phantasma-sdk-ts/core/rpc/interfaces/PhantasmaVmConfig

Source: `dist/types/core/rpc/interfaces/PhantasmaVmConfig.d.ts`

### Declarations

```ts
export * from '../../../rpc/interfaces/phantasma-vm-config.js';
```

## phantasma-sdk-ts/core/rpc/interfaces/Platform

Source: `dist/types/core/rpc/interfaces/Platform.d.ts`

### Declarations

```ts
export * from '../../../rpc/interfaces/platform.js';
```

## phantasma-sdk-ts/core/rpc/interfaces/Receipt

Source: `dist/types/core/rpc/interfaces/Receipt.d.ts`

### Declarations

```ts
export * from '../../../rpc/interfaces/receipt.js';
```

## phantasma-sdk-ts/core/rpc/interfaces/Script

Source: `dist/types/core/rpc/interfaces/Script.d.ts`

### Declarations

```ts
export * from '../../../rpc/interfaces/script.js';
```

## phantasma-sdk-ts/core/rpc/interfaces/SendRawTx

Source: `dist/types/core/rpc/interfaces/SendRawTx.d.ts`

### Declarations

```ts
export * from '../../../rpc/interfaces/send-raw-tx.js';
```

## phantasma-sdk-ts/core/rpc/interfaces/SignatureResult

Source: `dist/types/core/rpc/interfaces/SignatureResult.d.ts`

### Declarations

```ts
export * from '../../../rpc/interfaces/signature-result.js';
```

## phantasma-sdk-ts/core/rpc/interfaces/Stake

Source: `dist/types/core/rpc/interfaces/Stake.d.ts`

### Declarations

```ts
export * from '../../../rpc/interfaces/stake.js';
```

## phantasma-sdk-ts/core/rpc/interfaces/Storage

Source: `dist/types/core/rpc/interfaces/Storage.d.ts`

### Declarations

```ts
export * from '../../../rpc/interfaces/storage.js';
```

## phantasma-sdk-ts/core/rpc/interfaces/Swap

Source: `dist/types/core/rpc/interfaces/Swap.d.ts`

### Declarations

```ts
export * from '../../../rpc/interfaces/swap.js';
```

## phantasma-sdk-ts/core/rpc/interfaces/Token

Source: `dist/types/core/rpc/interfaces/Token.d.ts`

### Declarations

```ts
export * from '../../../rpc/interfaces/token.js';
```

## phantasma-sdk-ts/core/rpc/interfaces/TokenData

Source: `dist/types/core/rpc/interfaces/TokenData.d.ts`

### Declarations

```ts
export * from '../../../rpc/interfaces/token-data.js';
```

## phantasma-sdk-ts/core/rpc/interfaces/TokenExternal

Source: `dist/types/core/rpc/interfaces/TokenExternal.d.ts`

### Declarations

```ts
export * from '../../../rpc/interfaces/token-external.js';
```

## phantasma-sdk-ts/core/rpc/interfaces/TokenPrice

Source: `dist/types/core/rpc/interfaces/TokenPrice.d.ts`

### Declarations

```ts
export * from '../../../rpc/interfaces/token-price.js';
```

## phantasma-sdk-ts/core/rpc/interfaces/TokenSchemasResult

Source: `dist/types/core/rpc/interfaces/TokenSchemasResult.d.ts`

### Declarations

```ts
export * from '../../../rpc/interfaces/token-schemas-result.js';
```

## phantasma-sdk-ts/core/rpc/interfaces/TokenSeries

Source: `dist/types/core/rpc/interfaces/TokenSeries.d.ts`

### Declarations

```ts
export * from '../../../rpc/interfaces/token-series.js';
```

## phantasma-sdk-ts/core/rpc/interfaces/TokenSeriesResult

Source: `dist/types/core/rpc/interfaces/TokenSeriesResult.d.ts`

### Declarations

```ts
export * from '../../../rpc/interfaces/token-series-result.js';
```

## phantasma-sdk-ts/core/rpc/interfaces/TransactionData

Source: `dist/types/core/rpc/interfaces/TransactionData.d.ts`

### Declarations

```ts
export * from '../../../rpc/interfaces/transaction-data.js';
```

## phantasma-sdk-ts/core/rpc/interfaces/Validator

Source: `dist/types/core/rpc/interfaces/Validator.d.ts`

### Declarations

```ts
export * from '../../../rpc/interfaces/validator.js';
```

## phantasma-sdk-ts/core/rpc/interfaces/VmNamedVariableSchemaResult

Source: `dist/types/core/rpc/interfaces/VmNamedVariableSchemaResult.d.ts`

### Declarations

```ts
export * from '../../../rpc/interfaces/vm-named-variable-schema-result.js';
```

## phantasma-sdk-ts/core/rpc/interfaces/VmStructSchemaResult

Source: `dist/types/core/rpc/interfaces/VmStructSchemaResult.d.ts`

### Declarations

```ts
export * from '../../../rpc/interfaces/vm-struct-schema-result.js';
```

## phantasma-sdk-ts/core/rpc/interfaces/VmVariableSchemaResult

Source: `dist/types/core/rpc/interfaces/VmVariableSchemaResult.d.ts`

### Declarations

```ts
export * from '../../../rpc/interfaces/vm-variable-schema-result.js';
```

## phantasma-sdk-ts/core/rpc/interfaces

Source: `dist/types/core/rpc/interfaces/index.d.ts`

### Declarations

```ts
export * from '../../../rpc/interfaces/index.js';
```

## phantasma-sdk-ts/core/rpc/phantasma

Source: `dist/types/core/rpc/phantasma.d.ts`

### Declarations

```ts
export * from '../../rpc/phantasma.js';
```

## phantasma-sdk-ts/core/tx/ContractArtifacts

Source: `dist/types/core/tx/ContractArtifacts.d.ts`

### Declarations

```ts
export * from '../../tx/contract-artifacts.js';
```

## phantasma-sdk-ts/core/tx/ContractTxHelper

Source: `dist/types/core/tx/ContractTxHelper.d.ts`

### Declarations

```ts
export * from '../../tx/contract-tx-helper.js';
```

## phantasma-sdk-ts/core/tx/ExecutionState

Source: `dist/types/core/tx/ExecutionState.d.ts`

### Declarations

```ts
export * from '../../tx/execution-state.js';
```

## phantasma-sdk-ts/core/tx/Transaction

Source: `dist/types/core/tx/Transaction.d.ts`

### Declarations

```ts
export * from '../../tx/transaction.js';
```

## phantasma-sdk-ts/core/tx

Source: `dist/types/core/tx/index.d.ts`

### Declarations

```ts
export * from '../../tx/index.js';
```

## phantasma-sdk-ts/core/tx/utils

Source: `dist/types/core/tx/utils.d.ts`

### Declarations

```ts
export * from '../../tx/utils.js';
```

## phantasma-sdk-ts/core/types/Address

Source: `dist/types/core/types/Address.d.ts`

### Declarations

```ts
export * from '../../types/address.js';
```

## phantasma-sdk-ts/core/types/Carbon/Blockchain/CarbonTokenFlags

Source: `dist/types/core/types/Carbon/Blockchain/CarbonTokenFlags.d.ts`

### Declarations

```ts
export * from '../../../../types/carbon/blockchain/carbon-token-flags.js';
```

## phantasma-sdk-ts/core/types/Carbon/Blockchain/Extensions/TxMsgSigner

Source: `dist/types/core/types/Carbon/Blockchain/Extensions/TxMsgSigner.d.ts`

### Declarations

```ts
export * from '../../../../../types/carbon/blockchain/extensions/tx-msg-signer.js';
```

## phantasma-sdk-ts/core/types/Carbon/Blockchain/Extensions

Source: `dist/types/core/types/Carbon/Blockchain/Extensions/index.d.ts`

### Declarations

```ts
export * from '../../../../../types/carbon/blockchain/extensions/index.js';
```

## phantasma-sdk-ts/core/types/Carbon/Blockchain/ModuleId

Source: `dist/types/core/types/Carbon/Blockchain/ModuleId.d.ts`

### Declarations

```ts
export * from '../../../../types/carbon/blockchain/module-id.js';
```

## phantasma-sdk-ts/core/types/Carbon/Blockchain/Modules/Builders/IdHelper

Source: `dist/types/core/types/Carbon/Blockchain/Modules/Builders/IdHelper.d.ts`

### Declarations

```ts
export * from '../../../../../../types/carbon/blockchain/modules/builders/id-helper.js';
```

## phantasma-sdk-ts/core/types/Carbon/Blockchain/Modules/Builders/MetadataHelper

Source: `dist/types/core/types/Carbon/Blockchain/Modules/Builders/MetadataHelper.d.ts`

### Declarations

```ts
export * from '../../../../../../types/carbon/blockchain/modules/builders/metadata-helper.js';
```

## phantasma-sdk-ts/core/types/Carbon/Blockchain/Modules/Builders/NftRomBuilder

Source: `dist/types/core/types/Carbon/Blockchain/Modules/Builders/NftRomBuilder.d.ts`

### Declarations

```ts
export * from '../../../../../../types/carbon/blockchain/modules/builders/nft-rom-builder.js';
```

## phantasma-sdk-ts/core/types/Carbon/Blockchain/Modules/Builders/PhantasmaNftRomBuilder

Source: `dist/types/core/types/Carbon/Blockchain/Modules/Builders/PhantasmaNftRomBuilder.d.ts`

### Declarations

```ts
export * from '../../../../../../types/carbon/blockchain/modules/builders/phantasma-nft-rom-builder.js';
```

## phantasma-sdk-ts/core/types/Carbon/Blockchain/Modules/Builders/SeriesInfoBuilder

Source: `dist/types/core/types/Carbon/Blockchain/Modules/Builders/SeriesInfoBuilder.d.ts`

### Declarations

```ts
export * from '../../../../../../types/carbon/blockchain/modules/builders/series-info-builder.js';
```

## phantasma-sdk-ts/core/types/Carbon/Blockchain/Modules/Builders/TokenInfoBuilder

Source: `dist/types/core/types/Carbon/Blockchain/Modules/Builders/TokenInfoBuilder.d.ts`

### Declarations

```ts
export * from '../../../../../../types/carbon/blockchain/modules/builders/token-info-builder.js';
```

## phantasma-sdk-ts/core/types/Carbon/Blockchain/Modules/Builders/TokenMetadataBuilder

Source: `dist/types/core/types/Carbon/Blockchain/Modules/Builders/TokenMetadataBuilder.d.ts`

### Declarations

```ts
export * from '../../../../../../types/carbon/blockchain/modules/builders/token-metadata-builder.js';
```

## phantasma-sdk-ts/core/types/Carbon/Blockchain/Modules/Builders/TokenSchemasBuilder

Source: `dist/types/core/types/Carbon/Blockchain/Modules/Builders/TokenSchemasBuilder.d.ts`

### Declarations

```ts
export * from '../../../../../../types/carbon/blockchain/modules/builders/token-schemas-builder.js';
```

## phantasma-sdk-ts/core/types/Carbon/Blockchain/Modules/Builders/TokenSeriesMetadataBuilder

Source: `dist/types/core/types/Carbon/Blockchain/Modules/Builders/TokenSeriesMetadataBuilder.d.ts`

### Declarations

```ts
export * from '../../../../../../types/carbon/blockchain/modules/builders/token-series-metadata-builder.js';
```

## phantasma-sdk-ts/core/types/Carbon/Blockchain/Modules/Builders

Source: `dist/types/core/types/Carbon/Blockchain/Modules/Builders/index.d.ts`

### Declarations

```ts
export * from '../../../../../../types/carbon/blockchain/modules/builders/index.js';
```

## phantasma-sdk-ts/core/types/Carbon/Blockchain/Modules/MintPhantasmaNonFungibleArgs

Source: `dist/types/core/types/Carbon/Blockchain/Modules/MintPhantasmaNonFungibleArgs.d.ts`

### Declarations

```ts
export * from '../../../../../types/carbon/blockchain/modules/mint-phantasma-non-fungible-args.js';
```

## phantasma-sdk-ts/core/types/Carbon/Blockchain/Modules/PhantasmaNftMintInfo

Source: `dist/types/core/types/Carbon/Blockchain/Modules/PhantasmaNftMintInfo.d.ts`

### Declarations

```ts
export * from '../../../../../types/carbon/blockchain/modules/phantasma-nft-mint-info.js';
```

## phantasma-sdk-ts/core/types/Carbon/Blockchain/Modules/PhantasmaNftMintResult

Source: `dist/types/core/types/Carbon/Blockchain/Modules/PhantasmaNftMintResult.d.ts`

### Declarations

```ts
export * from '../../../../../types/carbon/blockchain/modules/phantasma-nft-mint-result.js';
```

## phantasma-sdk-ts/core/types/Carbon/Blockchain/Modules/SeriesInfo

Source: `dist/types/core/types/Carbon/Blockchain/Modules/SeriesInfo.d.ts`

### Declarations

```ts
export * from '../../../../../types/carbon/blockchain/modules/series-info.js';
```

## phantasma-sdk-ts/core/types/Carbon/Blockchain/Modules/StandardMeta

Source: `dist/types/core/types/Carbon/Blockchain/Modules/StandardMeta.d.ts`

### Declarations

```ts
export * from '../../../../../types/carbon/blockchain/modules/standard-meta.js';
```

## phantasma-sdk-ts/core/types/Carbon/Blockchain/Modules/TokenContract_Methods

Source: `dist/types/core/types/Carbon/Blockchain/Modules/TokenContract_Methods.d.ts`

### Declarations

```ts
export * from '../../../../../types/carbon/blockchain/modules/token-contract-methods.js';
```

## phantasma-sdk-ts/core/types/Carbon/Blockchain/Modules/TokenHelper

Source: `dist/types/core/types/Carbon/Blockchain/Modules/TokenHelper.d.ts`

### Declarations

```ts
export * from '../../../../../types/carbon/blockchain/modules/token-helper.js';
```

## phantasma-sdk-ts/core/types/Carbon/Blockchain/Modules/TokenInfo

Source: `dist/types/core/types/Carbon/Blockchain/Modules/TokenInfo.d.ts`

### Declarations

```ts
export * from '../../../../../types/carbon/blockchain/modules/token-info.js';
```

## phantasma-sdk-ts/core/types/Carbon/Blockchain/Modules/TokenListing

Source: `dist/types/core/types/Carbon/Blockchain/Modules/TokenListing.d.ts`

### Declarations

```ts
export * from '../../../../../types/carbon/blockchain/modules/token-listing.js';
```

## phantasma-sdk-ts/core/types/Carbon/Blockchain/Modules/TokenSchemas

Source: `dist/types/core/types/Carbon/Blockchain/Modules/TokenSchemas.d.ts`

### Declarations

```ts
export * from '../../../../../types/carbon/blockchain/modules/token-schemas.js';
```

## phantasma-sdk-ts/core/types/Carbon/Blockchain/Modules

Source: `dist/types/core/types/Carbon/Blockchain/Modules/index.d.ts`

### Declarations

```ts
export * from '../../../../../types/carbon/blockchain/modules/index.js';
```

## phantasma-sdk-ts/core/types/Carbon/Blockchain/SignedTxMsg

Source: `dist/types/core/types/Carbon/Blockchain/SignedTxMsg.d.ts`

### Declarations

```ts
export * from '../../../../types/carbon/blockchain/signed-tx-msg.js';
```

## phantasma-sdk-ts/core/types/Carbon/Blockchain/TxHelpers/CreateTokenSeriesTxHelper

Source: `dist/types/core/types/Carbon/Blockchain/TxHelpers/CreateTokenSeriesTxHelper.d.ts`

### Declarations

```ts
export * from '../../../../../types/carbon/blockchain/tx-helpers/create-token-series-tx-helper.js';
```

## phantasma-sdk-ts/core/types/Carbon/Blockchain/TxHelpers/CreateTokenTxHelper

Source: `dist/types/core/types/Carbon/Blockchain/TxHelpers/CreateTokenTxHelper.d.ts`

### Declarations

```ts
export * from '../../../../../types/carbon/blockchain/tx-helpers/create-token-tx-helper.js';
```

## phantasma-sdk-ts/core/types/Carbon/Blockchain/TxHelpers/FeeOptions

Source: `dist/types/core/types/Carbon/Blockchain/TxHelpers/FeeOptions.d.ts`

### Declarations

```ts
export * from '../../../../../types/carbon/blockchain/tx-helpers/fee-options.js';
```

## phantasma-sdk-ts/core/types/Carbon/Blockchain/TxHelpers/MintNonFungibleTxHelper

Source: `dist/types/core/types/Carbon/Blockchain/TxHelpers/MintNonFungibleTxHelper.d.ts`

### Declarations

```ts
export * from '../../../../../types/carbon/blockchain/tx-helpers/mint-non-fungible-tx-helper.js';
```

## phantasma-sdk-ts/core/types/Carbon/Blockchain/TxHelpers/MintPhantasmaNonFungibleTxHelper

Source: `dist/types/core/types/Carbon/Blockchain/TxHelpers/MintPhantasmaNonFungibleTxHelper.d.ts`

### Declarations

```ts
export * from '../../../../../types/carbon/blockchain/tx-helpers/mint-phantasma-non-fungible-tx-helper.js';
```

## phantasma-sdk-ts/core/types/Carbon/Blockchain/TxHelpers

Source: `dist/types/core/types/Carbon/Blockchain/TxHelpers/index.d.ts`

### Declarations

```ts
export * from '../../../../../types/carbon/blockchain/tx-helpers/index.js';
```

## phantasma-sdk-ts/core/types/Carbon/Blockchain/TxMsg

Source: `dist/types/core/types/Carbon/Blockchain/TxMsg.d.ts`

### Declarations

```ts
export * from '../../../../types/carbon/blockchain/tx-msg.js';
```

## phantasma-sdk-ts/core/types/Carbon/Blockchain/TxMsgBurnFungible

Source: `dist/types/core/types/Carbon/Blockchain/TxMsgBurnFungible.d.ts`

### Declarations

```ts
export * from '../../../../types/carbon/blockchain/tx-msg-burn-fungible.js';
```

## phantasma-sdk-ts/core/types/Carbon/Blockchain/TxMsgBurnFungibleGasPayer

Source: `dist/types/core/types/Carbon/Blockchain/TxMsgBurnFungibleGasPayer.d.ts`

### Declarations

```ts
export * from '../../../../types/carbon/blockchain/tx-msg-burn-fungible-gas-payer.js';
```

## phantasma-sdk-ts/core/types/Carbon/Blockchain/TxMsgBurnNonFungible

Source: `dist/types/core/types/Carbon/Blockchain/TxMsgBurnNonFungible.d.ts`

### Declarations

```ts
export * from '../../../../types/carbon/blockchain/tx-msg-burn-non-fungible.js';
```

## phantasma-sdk-ts/core/types/Carbon/Blockchain/TxMsgBurnNonFungibleGasPayer

Source: `dist/types/core/types/Carbon/Blockchain/TxMsgBurnNonFungibleGasPayer.d.ts`

### Declarations

```ts
export * from '../../../../types/carbon/blockchain/tx-msg-burn-non-fungible-gas-payer.js';
```

## phantasma-sdk-ts/core/types/Carbon/Blockchain/TxMsgCall

Source: `dist/types/core/types/Carbon/Blockchain/TxMsgCall.d.ts`

### Declarations

```ts
export * from '../../../../types/carbon/blockchain/tx-msg-call.js';
```

## phantasma-sdk-ts/core/types/Carbon/Blockchain/TxMsgCallMulti

Source: `dist/types/core/types/Carbon/Blockchain/TxMsgCallMulti.d.ts`

### Declarations

```ts
export * from '../../../../types/carbon/blockchain/tx-msg-call-multi.js';
```

## phantasma-sdk-ts/core/types/Carbon/Blockchain/TxMsgMintFungible

Source: `dist/types/core/types/Carbon/Blockchain/TxMsgMintFungible.d.ts`

### Declarations

```ts
export * from '../../../../types/carbon/blockchain/tx-msg-mint-fungible.js';
```

## phantasma-sdk-ts/core/types/Carbon/Blockchain/TxMsgMintNonFungible

Source: `dist/types/core/types/Carbon/Blockchain/TxMsgMintNonFungible.d.ts`

### Declarations

```ts
export * from '../../../../types/carbon/blockchain/tx-msg-mint-non-fungible.js';
```

## phantasma-sdk-ts/core/types/Carbon/Blockchain/TxMsgPhantasma

Source: `dist/types/core/types/Carbon/Blockchain/TxMsgPhantasma.d.ts`

### Declarations

```ts
export * from '../../../../types/carbon/blockchain/tx-msg-phantasma.js';
```

## phantasma-sdk-ts/core/types/Carbon/Blockchain/TxMsgPhantasmaRaw

Source: `dist/types/core/types/Carbon/Blockchain/TxMsgPhantasmaRaw.d.ts`

### Declarations

```ts
export * from '../../../../types/carbon/blockchain/tx-msg-phantasma-raw.js';
```

## phantasma-sdk-ts/core/types/Carbon/Blockchain/TxMsgSpecialResolution

Source: `dist/types/core/types/Carbon/Blockchain/TxMsgSpecialResolution.d.ts`

### Declarations

```ts
export * from '../../../../types/carbon/blockchain/tx-msg-special-resolution.js';
```

## phantasma-sdk-ts/core/types/Carbon/Blockchain/TxMsgTrade

Source: `dist/types/core/types/Carbon/Blockchain/TxMsgTrade.d.ts`

### Declarations

```ts
export * from '../../../../types/carbon/blockchain/tx-msg-trade.js';
```

## phantasma-sdk-ts/core/types/Carbon/Blockchain/TxMsgTransferFungible

Source: `dist/types/core/types/Carbon/Blockchain/TxMsgTransferFungible.d.ts`

### Declarations

```ts
export * from '../../../../types/carbon/blockchain/tx-msg-transfer-fungible.js';
```

## phantasma-sdk-ts/core/types/Carbon/Blockchain/TxMsgTransferFungibleGasPayer

Source: `dist/types/core/types/Carbon/Blockchain/TxMsgTransferFungibleGasPayer.d.ts`

### Declarations

```ts
export * from '../../../../types/carbon/blockchain/tx-msg-transfer-fungible-gas-payer.js';
```

## phantasma-sdk-ts/core/types/Carbon/Blockchain/TxMsgTransferNonFungibleMulti

Source: `dist/types/core/types/Carbon/Blockchain/TxMsgTransferNonFungibleMulti.d.ts`

### Declarations

```ts
export * from '../../../../types/carbon/blockchain/tx-msg-transfer-non-fungible-multi.js';
```

## phantasma-sdk-ts/core/types/Carbon/Blockchain/TxMsgTransferNonFungibleMultiGasPayer

Source: `dist/types/core/types/Carbon/Blockchain/TxMsgTransferNonFungibleMultiGasPayer.d.ts`

### Declarations

```ts
export * from '../../../../types/carbon/blockchain/tx-msg-transfer-non-fungible-multi-gas-payer.js';
```

## phantasma-sdk-ts/core/types/Carbon/Blockchain/TxMsgTransferNonFungibleSingle

Source: `dist/types/core/types/Carbon/Blockchain/TxMsgTransferNonFungibleSingle.d.ts`

### Declarations

```ts
export * from '../../../../types/carbon/blockchain/tx-msg-transfer-non-fungible-single.js';
```

## phantasma-sdk-ts/core/types/Carbon/Blockchain/TxMsgTransferNonFungibleSingleGasPayer

Source: `dist/types/core/types/Carbon/Blockchain/TxMsgTransferNonFungibleSingleGasPayer.d.ts`

### Declarations

```ts
export * from '../../../../types/carbon/blockchain/tx-msg-transfer-non-fungible-single-gas-payer.js';
```

## phantasma-sdk-ts/core/types/Carbon/Blockchain/Vm/VmDynamicStruct

Source: `dist/types/core/types/Carbon/Blockchain/Vm/VmDynamicStruct.d.ts`

### Declarations

```ts
export * from '../../../../../types/carbon/blockchain/vm/vm-dynamic-struct.js';
```

## phantasma-sdk-ts/core/types/Carbon/Blockchain/Vm/VmDynamicVariable

Source: `dist/types/core/types/Carbon/Blockchain/Vm/VmDynamicVariable.d.ts`

### Declarations

```ts
export * from '../../../../../types/carbon/blockchain/vm/vm-dynamic-variable.js';
```

## phantasma-sdk-ts/core/types/Carbon/Blockchain/Vm/VmNamedDynamicVariable

Source: `dist/types/core/types/Carbon/Blockchain/Vm/VmNamedDynamicVariable.d.ts`

### Declarations

```ts
export * from '../../../../../types/carbon/blockchain/vm/vm-named-dynamic-variable.js';
```

## phantasma-sdk-ts/core/types/Carbon/Blockchain/Vm/VmNamedVariableSchema

Source: `dist/types/core/types/Carbon/Blockchain/Vm/VmNamedVariableSchema.d.ts`

### Declarations

```ts
export * from '../../../../../types/carbon/blockchain/vm/vm-named-variable-schema.js';
```

## phantasma-sdk-ts/core/types/Carbon/Blockchain/Vm/VmStructArray

Source: `dist/types/core/types/Carbon/Blockchain/Vm/VmStructArray.d.ts`

### Declarations

```ts
export * from '../../../../../types/carbon/blockchain/vm/vm-struct-array.js';
```

## phantasma-sdk-ts/core/types/Carbon/Blockchain/Vm/VmStructFlags

Source: `dist/types/core/types/Carbon/Blockchain/Vm/VmStructFlags.d.ts`

### Declarations

```ts
export * from '../../../../../types/carbon/blockchain/vm/vm-struct-flags.js';
```

## phantasma-sdk-ts/core/types/Carbon/Blockchain/Vm/VmStructSchema

Source: `dist/types/core/types/Carbon/Blockchain/Vm/VmStructSchema.d.ts`

### Declarations

```ts
export * from '../../../../../types/carbon/blockchain/vm/vm-struct-schema.js';
```

## phantasma-sdk-ts/core/types/Carbon/Blockchain/Vm/VmType

Source: `dist/types/core/types/Carbon/Blockchain/Vm/VmType.d.ts`

### Declarations

```ts
export * from '../../../../../types/carbon/blockchain/vm/vm-type.js';
```

## phantasma-sdk-ts/core/types/Carbon/Blockchain/Vm/VmVariableSchema

Source: `dist/types/core/types/Carbon/Blockchain/Vm/VmVariableSchema.d.ts`

### Declarations

```ts
export * from '../../../../../types/carbon/blockchain/vm/vm-variable-schema.js';
```

## phantasma-sdk-ts/core/types/Carbon/Blockchain/Vm

Source: `dist/types/core/types/Carbon/Blockchain/Vm/index.d.ts`

### Declarations

```ts
export * from '../../../../../types/carbon/blockchain/vm/index.js';
```

## phantasma-sdk-ts/core/types/Carbon/Blockchain

Source: `dist/types/core/types/Carbon/Blockchain/index.d.ts`

### Declarations

```ts
export * from '../../../../types/carbon/blockchain/index.js';
```

## phantasma-sdk-ts/core/types/Carbon/Bytes16

Source: `dist/types/core/types/Carbon/Bytes16.d.ts`

### Declarations

```ts
export * from '../../../types/carbon/bytes16.js';
```

## phantasma-sdk-ts/core/types/Carbon/Bytes32

Source: `dist/types/core/types/Carbon/Bytes32.d.ts`

### Declarations

```ts
export * from '../../../types/carbon/bytes32.js';
```

## phantasma-sdk-ts/core/types/Carbon/Bytes64

Source: `dist/types/core/types/Carbon/Bytes64.d.ts`

### Declarations

```ts
export * from '../../../types/carbon/bytes64.js';
```

## phantasma-sdk-ts/core/types/Carbon/CarbonBlob

Source: `dist/types/core/types/Carbon/CarbonBlob.d.ts`

### Declarations

```ts
export * from '../../../types/carbon/carbon-blob.js';
```

## phantasma-sdk-ts/core/types/Carbon/IntX

Source: `dist/types/core/types/Carbon/IntX.d.ts`

### Declarations

```ts
export * from '../../../types/carbon/int-x.js';
```

## phantasma-sdk-ts/core/types/Carbon/SmallString

Source: `dist/types/core/types/Carbon/SmallString.d.ts`

### Declarations

```ts
export * from '../../../types/carbon/small-string.js';
```

## phantasma-sdk-ts/core/types/Carbon/TxTypes

Source: `dist/types/core/types/Carbon/TxTypes.d.ts`

### Declarations

```ts
export * from '../../../types/carbon/tx-types.js';
```

## phantasma-sdk-ts/core/types/Carbon/Witness

Source: `dist/types/core/types/Carbon/Witness.d.ts`

### Declarations

```ts
export * from '../../../types/carbon/witness.js';
```

## phantasma-sdk-ts/core/types/Carbon

Source: `dist/types/core/types/Carbon/index.d.ts`

### Declarations

```ts
export * from '../../../types/carbon/index.js';
```

## phantasma-sdk-ts/core/types/CarbonSerialization

Source: `dist/types/core/types/CarbonSerialization.d.ts`

### Declarations

```ts
export * from '../../types/carbon-serialization.js';
```

## phantasma-sdk-ts/core/types/Consensus

Source: `dist/types/core/types/Consensus.d.ts`

### Declarations

```ts
export * from '../../types/consensus.js';
```

## phantasma-sdk-ts/core/types/Contract

Source: `dist/types/core/types/Contract.d.ts`

### Declarations

```ts
export * from '../../types/contract.js';
```

## phantasma-sdk-ts/core/types/DomainSettings

Source: `dist/types/core/types/DomainSettings.d.ts`

### Declarations

```ts
export * from '../../types/domain-settings.js';
```

## phantasma-sdk-ts/core/types/Ed25519

Source: `dist/types/core/types/Ed25519.d.ts`

### Declarations

```ts
export * from '../../types/ed25519.js';
```

## phantasma-sdk-ts/core/types/Ed25519Signature

Source: `dist/types/core/types/Ed25519Signature.d.ts`

### Declarations

```ts
export * from '../../types/ed25519-signature.js';
```

## phantasma-sdk-ts/core/types/Entropy

Source: `dist/types/core/types/Entropy.d.ts`

### Declarations

```ts
export * from '../../types/entropy.js';
```

## phantasma-sdk-ts/core/types/Extensions/Base16

Source: `dist/types/core/types/Extensions/Base16.d.ts`

### Declarations

```ts
export * from '../../../types/extensions/base16.js';
```

## phantasma-sdk-ts/core/types/Extensions/Describer

Source: `dist/types/core/types/Extensions/Describer.d.ts`

### Declarations

```ts
export * from '../../../types/extensions/describer.js';
```

## phantasma-sdk-ts/core/types/Extensions/PBinaryReader

Source: `dist/types/core/types/Extensions/PBinaryReader.d.ts`

### Declarations

```ts
export * from '../../../types/extensions/p-binary-reader.js';
```

## phantasma-sdk-ts/core/types/Extensions/PBinaryWriter

Source: `dist/types/core/types/Extensions/PBinaryWriter.d.ts`

### Declarations

```ts
export * from '../../../types/extensions/p-binary-writer.js';
```

## phantasma-sdk-ts/core/types/Extensions

Source: `dist/types/core/types/Extensions/index.d.ts`

### Declarations

```ts
export * from '../../../types/extensions/index.js';
```

## phantasma-sdk-ts/core/types/PhantasmaBigIntSerialization

Source: `dist/types/core/types/PhantasmaBigIntSerialization.d.ts`

### Declarations

```ts
export * from '../../types/phantasma-big-int-serialization.js';
```

## phantasma-sdk-ts/core/types/PhantasmaKeys

Source: `dist/types/core/types/PhantasmaKeys.d.ts`

### Declarations

```ts
export * from '../../types/phantasma-keys.js';
```

## phantasma-sdk-ts/core/types/Serialization

Source: `dist/types/core/types/Serialization.d.ts`

### Declarations

```ts
export * from '../../types/serialization.js';
```

## phantasma-sdk-ts/core/types/Stack

Source: `dist/types/core/types/Stack.d.ts`

### Declarations

```ts
export * from '../../types/stack.js';
```

## phantasma-sdk-ts/core/types/Timestamp

Source: `dist/types/core/types/Timestamp.d.ts`

### Declarations

```ts
export * from '../../types/timestamp.js';
```

## phantasma-sdk-ts/core/types

Source: `dist/types/core/types/index.d.ts`

### Declarations

```ts
export * from '../../types/index.js';
```

## phantasma-sdk-ts/core/utils/Hex

Source: `dist/types/core/utils/Hex.d.ts`

### Declarations

```ts
export * from '../../utils/hex.js';
```

## phantasma-sdk-ts/core/utils/ValidationUtils

Source: `dist/types/core/utils/ValidationUtils.d.ts`

### Declarations

```ts
export * from '../../utils/validation-utils.js';
```

## phantasma-sdk-ts/core/utils

Source: `dist/types/core/utils/index.d.ts`

### Declarations

```ts
export * from '../../utils/index.js';
```

## phantasma-sdk-ts/core/utils/logger

Source: `dist/types/core/utils/logger.d.ts`

### Declarations

```ts
export * from '../../utils/logger.js';
```

## phantasma-sdk-ts/core/vm/Contracts

Source: `dist/types/core/vm/Contracts.d.ts`

### Declarations

```ts
export * from '../../vm/contracts.js';
```

## phantasma-sdk-ts/core/vm/Decoder

Source: `dist/types/core/vm/Decoder.d.ts`

### Declarations

```ts
export * from '../../vm/decoder.js';
```

## phantasma-sdk-ts/core/vm/Disassembler

Source: `dist/types/core/vm/Disassembler.d.ts`

### Declarations

```ts
export * from '../../vm/disassembler.js';
```

## phantasma-sdk-ts/core/vm/EventData

Source: `dist/types/core/vm/EventData.d.ts`

### Declarations

```ts
export * from '../../vm/event-data.js';
```

## phantasma-sdk-ts/core/vm/Opcode

Source: `dist/types/core/vm/Opcode.d.ts`

### Declarations

```ts
export * from '../../vm/opcode.js';
```

## phantasma-sdk-ts/core/vm/ScriptBuilder

Source: `dist/types/core/vm/ScriptBuilder.d.ts`

### Declarations

```ts
export * from '../../vm/script-builder.js';
```

## phantasma-sdk-ts/core/vm/VMObject

Source: `dist/types/core/vm/VMObject.d.ts`

### Declarations

```ts
export * from '../../vm/vm-object.js';
```

## phantasma-sdk-ts/core/vm/VMType

Source: `dist/types/core/vm/VMType.d.ts`

### Declarations

```ts
export * from '../../vm/vm-type.js';
```

## phantasma-sdk-ts/core/vm

Source: `dist/types/core/vm/index.d.ts`

### Declarations

```ts
export * from '../../vm/index.js';
```

## phantasma-sdk-ts/core/vm/utils/DisasmMethodCall

Source: `dist/types/core/vm/utils/DisasmMethodCall.d.ts`

### Declarations

```ts
export * from '../../../vm/utils/disasm-method-call.js';
```

## phantasma-sdk-ts/core/vm/utils/DisasmUtils

Source: `dist/types/core/vm/utils/DisasmUtils.d.ts`

### Declarations

```ts
export * from '../../../vm/utils/disasm-utils.js';
```

## phantasma-sdk-ts/core/vm/utils

Source: `dist/types/core/vm/utils/index.d.ts`

### Declarations

```ts
export * from '../../../vm/utils/index.js';
```

## phantasma-sdk-ts

Source: `dist/types/index.d.ts`

### Declarations

```ts
export * from './core/index.js';
```

```ts
export * as PhantasmaTS from './core/index.js';
```

```ts
export { PhantasmaLink } from './link/phantasma-link.js';
```

```ts
export { EasyConnect } from './link/easy-connect.js';
```

## phantasma-sdk-ts/interfaces/carbon/carbon-blob-like

Source: `dist/types/interfaces/carbon/carbon-blob-like.d.ts`

### Declarations

```ts
export interface CarbonBlobLike {
    write(w: CarbonBinaryWriter): void;
    read(r: CarbonBinaryReader): void;
}
```

```ts
export type ICarbonBlob = CarbonBlobLike;
```

## phantasma-sdk-ts/interfaces/carbon

Source: `dist/types/interfaces/carbon/index.d.ts`

### Declarations

```ts
export * from './carbon-blob-like.js';
```

## phantasma-sdk-ts/interfaces/contract

Source: `dist/types/interfaces/contract.d.ts`

### Declarations

```ts
export interface ContractDescriptor {
    name: string;
    abi: ContractInterface;
}
```

```ts
export interface IContract {
    /** @deprecated Use `name` instead. */
    Name: string;
    /** @deprecated Use `abi` instead. */
    ABI: ContractInterface;
}
```

```ts
export declare enum NativeContractKind {
    Gas = 0,
    Block = 1,
    Stake = 2,
    Swap = 3,
    Account = 4,
    Consensus = 5,
    Governance = 6,
    Storage = 7,
    Validator = 8,
    Interop = 9,
    Exchange = 10,
    Privacy = 11,
    Relay = 12,
    Ranking = 13,
    Market = 14,
    Friends = 15,
    Mail = 16,
    Sale = 17,
    Unknown = 18
}
```

## phantasma-sdk-ts/interfaces

Source: `dist/types/interfaces/index.d.ts`

### Declarations

```ts
export * from './carbon/index.js';
```

```ts
export * from './stack.js';
```

```ts
export * from './token.js';
```

```ts
export * from './contract.js';
```

```ts
export * from './key-pair.js';
```

```ts
export * from './serializable.js';
```

```ts
export * from './signature.js';
```

## phantasma-sdk-ts/interfaces/key-pair

Source: `dist/types/interfaces/key-pair.d.ts`

### Declarations

```ts
export interface KeyPair {
    privateKey: Uint8Array;
    publicKey: Uint8Array;
    sign(msg: Uint8Array): Signature;
}
```

```ts
export interface IKeyPair {
    /** @deprecated Use `privateKey` instead. This alias will be removed in v1.0. */
    PrivateKey: Uint8Array;
    /** @deprecated Use `publicKey` instead. This alias will be removed in v1.0. */
    PublicKey: Uint8Array;
    /** @deprecated Use `sign` instead. This alias will be removed in v1.0. */
    Sign(msg: Uint8Array, customSignFunction?: (message: Uint8Array, privateKey: Uint8Array, publicKey: Uint8Array) => Uint8Array): Signature;
}
```

## phantasma-sdk-ts/interfaces/serializable

Source: `dist/types/interfaces/serializable.d.ts`

### Declarations

```ts
export interface Serializable {
    serializeData(writer: PBinaryWriter): void;
    unserializeData(reader: PBinaryReader): void;
}
```

```ts
export interface LegacySerializable {
    SerializeData(writer: PBinaryWriter): void;
    UnserializeData(reader: PBinaryReader): void;
}
```

```ts
export type SerializableLike = Serializable | LegacySerializable;
```

```ts
export declare function isSerializableLike(value: unknown): value is SerializableLike;
```

```ts
export declare function serializeSerializable(value: SerializableLike, writer: PBinaryWriter): void;
```

```ts
export declare function unserializeSerializable(value: SerializableLike, reader: PBinaryReader): void;
```

```ts
export declare abstract class ISerializable implements LegacySerializable {
    abstract SerializeData(writer: PBinaryWriter): void;
    abstract UnserializeData(reader: PBinaryReader): void;
}
```

## phantasma-sdk-ts/interfaces/signature

Source: `dist/types/interfaces/signature.d.ts`

### Declarations

```ts
export declare enum SignatureKind {
    None = 0,
    Ed25519 = 1,
    ECDSA = 2
}
```

```ts
export declare class ISignature {
    signature: string;
    kind: SignatureKind;
}
```

```ts
export declare abstract class Signature implements ISerializable {
    /** @deprecated Use `bytes` instead. This alias will be removed in v1.0. */
    abstract Bytes: Uint8Array;
    /** @deprecated Use `kind` instead. This alias will be removed in v1.0. */
    abstract Kind: SignatureKind;
    /** @deprecated Use `serializeData` instead. This alias will be removed in v1.0. */
    abstract SerializeData(writer: PBinaryWriter): void;
    /** @deprecated Use `unserializeData` instead. This alias will be removed in v1.0. */
    abstract UnserializeData(reader: PBinaryReader): void;
    abstract verifyMultiple(message: Uint8Array, addresses: Address[]): boolean;
    get bytes(): Uint8Array;
    set bytes(value: Uint8Array);
    get kind(): SignatureKind;
    set kind(value: SignatureKind);
    serializeData(writer: PBinaryWriter): void;
    unserializeData(reader: PBinaryReader): void;
    verify(message: Uint8Array, address: Address): boolean;
    /** @deprecated Use `verifyMultiple` instead. This alias will be removed in v1.0. */
    VerifyMultiple(message: Uint8Array, addresses: Address[]): boolean;
    /** @deprecated Use `verify` instead. This alias will be removed in v1.0. */
    Verify(message: Uint8Array, address: Address): boolean;
    toByteArray(): Uint8Array;
    /** @deprecated Use `toByteArray` instead. This alias will be removed in v1.0. */
    ToByteArray(): Uint8Array;
}
```

## phantasma-sdk-ts/interfaces/stack

Source: `dist/types/interfaces/stack.d.ts`

### Declarations

```ts
export interface StackLike<T> {
    push(item: T): void;
    pop(): T | undefined;
    peek(): T | undefined;
    size(): number;
}
```

```ts
export type IStack<T> = StackLike<T>;
```

## phantasma-sdk-ts/interfaces/token

Source: `dist/types/interfaces/token.d.ts`

### Declarations

```ts
export declare enum TokenFlags {
    None = 0,
    Transferable = 1,
    Fungible = 2,
    Finite = 4,
    Divisible = 8,
    Fuel = 16,
    Stakable = 32,
    Fiat = 64,
    Swappable = 128,
    Burnable = 256
}
```

```ts
export declare enum TokenSeriesMode {
    Unique = 0,
    Duplicated = 1
}
```

```ts
export interface TokenDescriptor {
    readonly name: string;
    readonly symbol: string;
    readonly owner: Address;
    readonly flags: TokenFlags;
    readonly maxSupply: BigInteger;
    readonly decimals: number;
    readonly script: Uint8Array;
    readonly abi: ContractInterface;
}
```

```ts
export interface IToken {
    /** @deprecated Use `name` instead. */
    readonly Name: string;
    /** @deprecated Use `symbol` instead. */
    readonly Symbol: string;
    /** @deprecated Use `owner` instead. */
    readonly Owner: Address;
    /** @deprecated Use `flags` instead. */
    readonly Flags: TokenFlags;
    /** @deprecated Use `maxSupply` instead. */
    readonly MaxSupply: BigInteger;
    /** @deprecated Use `decimals` instead. */
    readonly Decimals: number;
    /** @deprecated Use `script` instead. */
    readonly Script: Uint8Array;
    /** @deprecated Use `abi` instead. */
    readonly ABI: ContractInterface;
}
```

## phantasma-sdk-ts/ledger/address-transcode

Source: `dist/types/ledger/address-transcode.d.ts`

### Declarations

```ts
export declare const getAddressFromPrivateKey: (privateKey: string) => string;
```

```ts
export declare const GetAddressFromPrivateKey: (privateKey: string) => string;
```

```ts
export declare const getAddressFromPublicKey: (publicKey: string) => string;
```

```ts
export declare const GetAddressFromPublicKey: (publicKey: string) => string;
```

```ts
export declare const getAddressPublicKeyFromPublicKey: (publicKey: string) => Address;
```

```ts
export declare const GetAddressPublicKeyFromPublicKey: (publicKey: string) => Address;
```

## phantasma-sdk-ts/ledger

Source: `dist/types/ledger/index.d.ts`

### Declarations

```ts
export * from './mnemonic.js';
```

```ts
export * from './address-transcode.js';
```

```ts
export * from './interfaces/ledger-config.js';
```

```ts
export * from './ledger-utils.js';
```

```ts
export * from './ledger-commands.js';
```

```ts
export * from './transaction-transcode.js';
```

```ts
export * from './transaction-sign.js';
```

```ts
export * from './interfaces/index.js';
```

## phantasma-sdk-ts/ledger/interfaces/application-name-response

Source: `dist/types/ledger/interfaces/application-name-response.d.ts`

### Declarations

```ts
export interface ApplicationNameResponse {
    success: boolean;
    message: string;
    applicationName?: string;
}
```

## phantasma-sdk-ts/ledger/interfaces/device-response

Source: `dist/types/ledger/interfaces/device-response.d.ts`

### Declarations

```ts
export interface DeviceResponse {
    enabled: boolean;
    error: boolean;
    message?: string;
    device?: LedgerTransportDevice;
}
```

## phantasma-sdk-ts/ledger/interfaces/device

Source: `dist/types/ledger/interfaces/device.d.ts`

### Declarations

```ts
export interface LedgerTransportDevice {
    exchange(request: Buffer): Promise<Buffer>;
    close(): Promise<void>;
}
```

```ts
export interface Device {
    enabled: boolean;
    error?: boolean;
    message?: string;
    device?: LedgerTransportDevice;
}
```

## phantasma-sdk-ts/ledger/interfaces

Source: `dist/types/ledger/interfaces/index.d.ts`

### Declarations

```ts
export * from './application-name-response.js';
```

```ts
export * from './device.js';
```

```ts
export * from './device-response.js';
```

```ts
export * from './ledger.js';
```

```ts
export * from './ledger-config.js';
```

```ts
export * from './ledger-device-info-response.js';
```

```ts
export * from './public-key-response.js';
```

```ts
export * from './sign-response.js';
```

```ts
export * from './version-response.js';
```

```ts
export * from './ledger-balance-from-ledger-response.js';
```

```ts
export * from './ledger-signer.js';
```

```ts
export * from './ledger-signer-data.js';
```

```ts
export * from './ledger-send-transaction-response.js';
```

## phantasma-sdk-ts/ledger/interfaces/ledger-balance-from-ledger-response

Source: `dist/types/ledger/interfaces/ledger-balance-from-ledger-response.d.ts`

### Declarations

```ts
export interface LedgerBalanceFromLedgerResponse {
    success: boolean;
    message: string;
    publicKey?: string;
    address?: Address;
    balances?: Map<string, string>;
}
```

## phantasma-sdk-ts/ledger/interfaces/ledger-config

Source: `dist/types/ledger/interfaces/ledger-config.d.ts`

### Declarations

```ts
export interface LedgerTransport {
    isSupported(): Promise<boolean>;
    list(): Promise<string[]>;
    open(path: string): Promise<LedgerTransportDevice>;
}
```

```ts
export interface LedgerBip39 {
    mnemonicToSeedSync(mnemonic: string): Uint8Array | Buffer;
    entropyToMnemonic(entropy: string): string;
}
```

```ts
export interface LedgerBip32Node {
    privateKey: Uint8Array | Buffer;
    derivePath(path: string): LedgerBip32Node;
}
```

```ts
export interface LedgerBip32 {
    fromSeed(seed: Uint8Array): LedgerBip32Node;
}
```

```ts
export type LedgerBip32Factory = (curve: unknown) => LedgerBip32;
```

```ts
export interface LedgerClientConfig {
    debug?: boolean;
    transport: LedgerTransport;
    bip39: LedgerBip39;
    bip32Factory: LedgerBip32Factory;
    curve: unknown;
    nexusName: string;
    chainName: string;
    payload?: string;
    tokenNames?: string[];
    rpc: PhantasmaAPI;
    gasPrice?: number;
    gasLimit?: number;
    verifyResponse?: boolean;
}
```

```ts
export interface LedgerConfig {
    /** @deprecated Use `debug` on `LedgerClientConfig` instead. */
    Debug: boolean;
    /** @deprecated Use `transport` on `LedgerClientConfig` instead. */
    Transport: LedgerTransport;
    /** @deprecated Use `bip39` on `LedgerClientConfig` instead. */
    Bip39: LedgerBip39;
    /** @deprecated Use `bip32Factory` on `LedgerClientConfig` instead. */
    Bip32Factory: LedgerBip32Factory;
    /** @deprecated Use `curve` on `LedgerClientConfig` instead. */
    Curve: unknown;
    /** @deprecated Use `nexusName` on `LedgerClientConfig` instead. */
    NexusName: string;
    /** @deprecated Use `chainName` on `LedgerClientConfig` instead. */
    ChainName: string;
    /** @deprecated Use `payload` on `LedgerClientConfig` instead. */
    Payload: string;
    /** @deprecated Use `tokenNames` on `LedgerClientConfig` instead. */
    TokenNames: string[];
    /** @deprecated Use `rpc` on `LedgerClientConfig` instead. */
    RPC: PhantasmaAPI;
    /** @deprecated Use `gasPrice` on `LedgerClientConfig` instead. */
    GasPrice: number;
    /** @deprecated Use `gasLimit` on `LedgerClientConfig` instead. */
    GasLimit: number;
    /** @deprecated Use `verifyResponse` on `LedgerClientConfig` instead. */
    VerifyResponse: boolean;
}
```

```ts
export type LedgerCompatibleConfig = LedgerClientConfig | LedgerConfig;
```

```ts
export interface NormalizedLedgerConfig {
    debug: boolean;
    transport: LedgerTransport;
    bip39: LedgerBip39;
    bip32Factory: LedgerBip32Factory;
    curve: unknown;
    nexusName: string;
    chainName: string;
    payload: string;
    tokenNames: string[];
    rpc: PhantasmaAPI;
    gasPrice: number;
    gasLimit: number;
    verifyResponse: boolean;
}
```

```ts
export declare function getLedgerDebug(config: LedgerCompatibleConfig): boolean;
```

```ts
export declare function getLedgerTransport(config: LedgerCompatibleConfig): LedgerTransport;
```

```ts
export declare function getLedgerBip39(config: LedgerCompatibleConfig): LedgerBip39;
```

```ts
export declare function getLedgerBip32Factory(config: LedgerCompatibleConfig): LedgerBip32Factory;
```

```ts
export declare function getLedgerCurve(config: LedgerCompatibleConfig): unknown;
```

```ts
export declare function getLedgerNexusName(config: LedgerCompatibleConfig): string;
```

```ts
export declare function getLedgerChainName(config: LedgerCompatibleConfig): string;
```

```ts
export declare function getLedgerPayload(config: LedgerCompatibleConfig): string;
```

```ts
export declare function getLedgerTokenNames(config: LedgerCompatibleConfig): string[];
```

```ts
export declare function getLedgerRpc(config: LedgerCompatibleConfig): PhantasmaAPI;
```

```ts
export declare function getLedgerGasPrice(config: LedgerCompatibleConfig): number;
```

```ts
export declare function getLedgerGasLimit(config: LedgerCompatibleConfig): number;
```

```ts
export declare function getLedgerVerifyResponse(config: LedgerCompatibleConfig): boolean;
```

```ts
export declare function normalizeLedgerConfig(config: LedgerCompatibleConfig): NormalizedLedgerConfig;
```

## phantasma-sdk-ts/ledger/interfaces/ledger-device-info-response

Source: `dist/types/ledger/interfaces/ledger-device-info-response.d.ts`

### Declarations

```ts
export interface LedgerDeviceInfoResponse {
    version: VersionResponse;
    applicationName: ApplicationNameResponse;
}
```

## phantasma-sdk-ts/ledger/interfaces/ledger-send-transaction-response

Source: `dist/types/ledger/interfaces/ledger-send-transaction-response.d.ts`

### Declarations

```ts
export interface LedgerSendTransactionResponse {
    success: boolean;
    message: string;
}
```

## phantasma-sdk-ts/ledger/interfaces/ledger-signer-data

Source: `dist/types/ledger/interfaces/ledger-signer-data.d.ts`

### Declarations

```ts
export interface LedgerSignerData {
    success: boolean;
    message: string;
    publicKey?: string;
    address?: Address;
}
```

## phantasma-sdk-ts/ledger/interfaces/ledger-signer

Source: `dist/types/ledger/interfaces/ledger-signer.d.ts`

### Declarations

```ts
export interface LedgerSigner {
    GetPublicKey: () => string;
    GetAccount: () => Address;
}
```

```ts
export interface LedgerAccountSigner extends LedgerSigner {
    getPublicKey: () => string;
    getAccount: () => Address;
}
```

## phantasma-sdk-ts/ledger/interfaces/ledger

Source: `dist/types/ledger/interfaces/ledger.d.ts`

### Declarations

```ts
export interface Ledger {
    device: Device;
    publicKey: string;
    address: string;
    signature: string;
    error?: boolean;
    message?: string;
}
```

```ts
export type ILedger = Ledger;
```

## phantasma-sdk-ts/ledger/interfaces/public-key-response

Source: `dist/types/ledger/interfaces/public-key-response.d.ts`

### Declarations

```ts
export interface PublicKeyResponse {
    success: boolean;
    message: string;
    publicKey?: string;
}
```

## phantasma-sdk-ts/ledger/interfaces/sign-response

Source: `dist/types/ledger/interfaces/sign-response.d.ts`

### Declarations

```ts
export interface SignResponse {
    success: boolean;
    message: string;
    signature?: string;
}
```

## phantasma-sdk-ts/ledger/interfaces/version-response

Source: `dist/types/ledger/interfaces/version-response.d.ts`

### Declarations

```ts
export interface VersionResponse {
    success: boolean;
    message: string;
    version?: string;
}
```

## phantasma-sdk-ts/ledger/ledger-commands

Source: `dist/types/ledger/ledger-commands.d.ts`

### Declarations

```ts
export declare const leftPad: (number: string | number, length: number) => string;
```

```ts
export declare const LeftPad: (number: string | number, length: number) => string;
```

```ts
export declare const toWholeNumber: (balance: string | number, decimals: number) => string;
```

```ts
export declare const ToWholeNumber: (balance: string | number, decimals: number) => string;
```

```ts
export declare const getLedgerDeviceInfo: (config: LedgerCompatibleConfig) => Promise<LedgerDeviceInfoResponse>;
```

```ts
export declare const GetLedgerDeviceInfo: (config: LedgerCompatibleConfig) => Promise<LedgerDeviceInfoResponse>;
```

```ts
export declare const getLedgerAccountSigner: (config: LedgerCompatibleConfig, accountIx: number) => Promise<LedgerAccountSigner>;
```

```ts
export declare const GetLedgerAccountSigner: (config: LedgerCompatibleConfig, accountIx: number) => Promise<LedgerAccountSigner>;
```

```ts
export declare function getLedgerSignerData(config: LedgerCompatibleConfig, options: LedgerPublicKeyOptions): Promise<LedgerSignerData>;
```

```ts
export declare const GetLedgerSignerData: typeof getLedgerSignerData;
```

```ts
export declare const getBalanceFromLedger: (config: LedgerCompatibleConfig, options: LedgerPublicKeyOptions) => Promise<LedgerBalanceFromLedgerResponse>;
```

```ts
export declare const GetBalanceFromLedger: (config: LedgerCompatibleConfig, options: LedgerPublicKeyOptions) => Promise<LedgerBalanceFromLedgerResponse>;
```

```ts
export declare const getAddressFromLedger: (config: LedgerCompatibleConfig, options: LedgerPublicKeyOptions) => Promise<string | PublicKeyResponse>;
```

```ts
export declare const GetAddressFromLedeger: (config: LedgerCompatibleConfig, options: LedgerPublicKeyOptions) => Promise<string | PublicKeyResponse>;
```

```ts
export declare const SignEncodedTx: typeof signEncodedTx;
```

```ts
export declare function sendTransactionLedger(config: LedgerCompatibleConfig, script: string): Promise<LedgerSendTransactionResponse>;
```

```ts
export declare const SendTransactionLedger: typeof sendTransactionLedger;
```

```ts
export declare const getBalanceFromPrivateKey: (config: LedgerCompatibleConfig, privateKey: string) => Promise<LedgerBalanceFromLedgerResponse>;
```

```ts
export declare const GetBalanceFromPrivateKey: (config: LedgerCompatibleConfig, privateKey: string) => Promise<LedgerBalanceFromLedgerResponse>;
```

```ts
export declare const getBalanceFromMnemonic: (config: LedgerCompatibleConfig, mnemonic: string, index: string) => Promise<LedgerBalanceFromLedgerResponse>;
```

```ts
export declare const GetBalanceFromMnemonic: (config: LedgerCompatibleConfig, mnemonic: string, index: string) => Promise<LedgerBalanceFromLedgerResponse>;
```

```ts
export {};
```

## phantasma-sdk-ts/ledger/ledger-utils

Source: `dist/types/ledger/ledger-utils.d.ts`

### Declarations

```ts
export declare const MAX_SIGNED_TX_LEN = 1024;
```

```ts
export interface LedgerPublicKeyOptions {
    verifyOnDevice?: boolean;
    debug?: boolean;
}
```

```ts
export declare const bip44Path: string;
```

```ts
export declare const ledgerErrorDescriptions: Record<string, string>;
```

```ts
export declare const Bip44Path: string;
```

```ts
export declare const ErrorDescriptions: Record<string, string>;
```

```ts
export declare const getErrorMessage: (responseStr: string) => string;
```

```ts
export declare const GetErrorMessage: (responseStr: string) => string;
```

```ts
export declare const getDevice: (transport: LedgerTransport) => Promise<DeviceResponse>;
```

```ts
export declare const GetDevice: (transport: LedgerTransport) => Promise<DeviceResponse>;
```

```ts
export declare const getApplicationName: (transport: LedgerTransport) => Promise<ApplicationNameResponse>;
```

```ts
export declare const GetApplicationName: (transport: LedgerTransport) => Promise<ApplicationNameResponse>;
```

```ts
export declare const getVersion: (transport: LedgerTransport) => Promise<VersionResponse>;
```

```ts
export declare const GetVersion: (transport: LedgerTransport) => Promise<VersionResponse>;
```

```ts
export declare const getBip44PathMessage: (messagePrefix: Buffer) => Buffer;
```

```ts
export declare const GetBip44PathMessage: (messagePrefix: Buffer) => Buffer;
```

```ts
export declare const getPublicKey: (transport: LedgerTransport, options: LedgerPublicKeyOptions) => Promise<PublicKeyResponse>;
```

```ts
export declare const GetPublicKey: (transport: LedgerTransport, options: LedgerPublicKeyOptions) => Promise<PublicKeyResponse>;
```

```ts
export declare const chunkString: (str: string, length: number) => string[];
```

```ts
export declare const ChunkString: (str: string, length: number) => string[];
```

```ts
export declare const splitMessageIntoChunks: (ledgerMessage: string) => Buffer[];
```

```ts
export declare const SplitMessageIntoChunks: (ledgerMessage: string) => Buffer[];
```

```ts
export declare const decodeSignature: (response: string) => string;
```

```ts
export declare const DecodeSignature: (response: string) => string;
```

```ts
export declare const signLedger: (transport: LedgerTransport, transactionHex: string) => Promise<SignResponse>;
```

```ts
export declare const SignLedger: (transport: LedgerTransport, transactionHex: string) => Promise<SignResponse>;
```

## phantasma-sdk-ts/ledger/mnemonic

Source: `dist/types/ledger/mnemonic.d.ts`

### Declarations

```ts
export declare const SOUL_COIN: number;
```

```ts
export declare const getPrivateKeyFromMnemonic: (config: LedgerCompatibleConfig, mnemonic: string, index: string) => string;
```

```ts
export declare const GetPrivateKeyFromMnemonic: (config: LedgerCompatibleConfig, mnemonic: string, index: string) => string;
```

```ts
export declare const getPrivateKeyFromSeed: (config: LedgerCompatibleConfig, seed: string, index: string) => string;
```

```ts
export declare const GetPrivateKeyFromSeed: (config: LedgerCompatibleConfig, seed: string, index: string) => string;
```

```ts
export declare const getPoltergeistMnemonic: (config: LedgerCompatibleConfig, mnemonic: string, index: string) => string;
```

```ts
export declare const GetPoltergeistMnemonic: (config: LedgerCompatibleConfig, mnemonic: string, index: string) => string;
```

```ts
export declare const getBip44Path: (index: string) => string;
```

```ts
export declare const GetBip44Path: (index: string) => string;
```

## phantasma-sdk-ts/ledger/transaction-sign

Source: `dist/types/ledger/transaction-sign.d.ts`

### Declarations

```ts
export declare const privateToDer: (privateKeyHex: string) => Buffer;
```

```ts
export declare const PrivateToDer: (privateKeyHex: string) => Buffer;
```

```ts
export declare const publicToDer: (publicKeyHex: string) => Buffer;
```

```ts
export declare const PublicToDer: (publicKeyHex: string) => Buffer;
```

```ts
export declare const publicToPem: (publicKeyHex: string) => string;
```

```ts
export declare const PublicToPem: (publicKeyHex: string) => string;
```

```ts
export declare const signBytes: (hash: Buffer, privateKey: Buffer) => string;
```

```ts
export declare const SignBytes: (hash: Buffer, privateKey: Buffer) => string;
```

```ts
export declare const getHash: (encodedTx: string) => Buffer;
```

```ts
export declare const GetHash: (encodedTx: string) => Buffer;
```

```ts
export declare const sign: (encodedTx: string, privateKeyHex: string) => string;
```

```ts
export declare const Sign: (encodedTx: string, privateKeyHex: string) => string;
```

```ts
export declare const verify: (encodedTx: string, signatureHex: string, publicKeyHex: string) => boolean;
```

```ts
export declare const Verify: (encodedTx: string, signatureHex: string, publicKeyHex: string) => boolean;
```

```ts
export declare const getPublicFromPrivate: (privateKey: string) => string;
```

```ts
export declare const GetPublicFromPrivate: (privateKey: string) => string;
```

## phantasma-sdk-ts/ledger/transaction-transcode

Source: `dist/types/ledger/transaction-transcode.d.ts`

### Declarations

```ts
export declare const getDateAsUTCSeconds: (expirationDate: Date) => number;
```

```ts
export declare const GetDateAsUTCSeconds: (expirationDate: Date) => number;
```

```ts
export declare const getExpirationDate: (expirationMinutes?: number) => Date;
```

```ts
export declare const GetExpirationDate: (expirationMinutes?: number) => Date;
```

```ts
export declare const encodeSendTxWithSignature: (transaction: Transaction) => string;
```

```ts
export declare const EncodeSendTxWithSignature: (transaction: Transaction) => string;
```

```ts
export declare const encodeSendTxWithoutSignature: (transaction: Transaction) => string;
```

```ts
export declare const EncodeSendTxWithoutSignature: (transaction: Transaction) => string;
```

## phantasma-sdk-ts/link/easy-connect

Source: `dist/types/link/easy-connect.d.ts`

### Declarations

```ts
export declare class EasyConnect {
    requiredVersion: number;
    platform: string;
    providerHint: string;
    link: PhantasmaLink;
    connected: boolean;
    script: EasyScript;
    nexus: Nexus | null;
    constructor(_options?: string[] | null);
    setConfig(_provider: string): void;
    connect(onSuccess?: EasyCallback, onFail?: EasyCallback): void;
    disconnect(_message?: string): void;
    query(_type?: string | null, _arguments?: string[] | null, _callback?: EasyCallback): Promise<string | import("../index.js").Balance[] | import("./index.js").LinkAccount | null | undefined>;
    action(_type?: string | null, _arguments?: EasyArguments | null, onSuccess?: EasyCallback, onFail?: EasyCallback): Promise<void>;
    signTransaction(script: string, payload?: string | null, onSuccess?: EasyCallback, onFail?: EasyCallback): void;
    signData(data: string, onSuccess?: EasyCallback, onFail?: EasyCallback): void;
    signCarbonTransaction(txMsg: TxMsg, onSuccess?: EasyCallback, onFail?: EasyCallback): void;
    signPrebuiltTransaction(tx: Transaction, onSuccess?: EasyCallback, onFail?: EasyCallback): void;
    invokeScript(script: string, _callback: EasyCallback): void;
    deployContract(script: string, payload?: null, proofOfWork?: ProofOfWork, onSuccess?: EasyCallback, onFail?: EasyCallback): void;
}
```

```ts
export {};
```

## phantasma-sdk-ts/link/easy-script

Source: `dist/types/link/easy-script.d.ts`

### Declarations

```ts
export declare enum Nexus {
    Mainnet = "mainnet",
    Simnet = "simnet",
    Testnet = "testnet"
}
```

```ts
export declare class EasyScript {
    nexus: Nexus;
    sb: ScriptBuilder;
    constructor(nexus?: Nexus);
    buildScript(_type: string, _options?: unknown[]): string;
}
```

## phantasma-sdk-ts/link

Source: `dist/types/link/index.d.ts`

### Declarations

```ts
export * from './interfaces/index.js';
```

## phantasma-sdk-ts/link/interfaces/account

Source: `dist/types/link/interfaces/account.d.ts`

### Declarations

```ts
export interface LinkAccount {
    alias: string;
    name: string;
    address: string;
    avatar: string;
    platform: string;
    external: string;
    balances: Balance[];
    files: LinkFile[];
}
```

```ts
export type IAccount = LinkAccount;
```

## phantasma-sdk-ts/link/interfaces/file

Source: `dist/types/link/interfaces/file.d.ts`

### Declarations

```ts
export interface LinkFile {
    name: string;
    hash: string;
    size: number;
    date: string;
}
```

```ts
export type IFile = LinkFile;
```

## phantasma-sdk-ts/link/interfaces

Source: `dist/types/link/interfaces/index.d.ts`

### Declarations

```ts
export * from './file.js';
```

```ts
export * from './account.js';
```

```ts
export * from './proof-of-work.js';
```

## phantasma-sdk-ts/link/interfaces/proof-of-work

Source: `dist/types/link/interfaces/proof-of-work.d.ts`

### Declarations

```ts
export declare enum ProofOfWork {
    None = 0,
    Minimal = 5,
    Moderate = 15,
    Hard = 19,
    Heavy = 24,
    Extreme = 30
}
```

## phantasma-sdk-ts/link/phantasma-link

Source: `dist/types/link/phantasma-link.d.ts`

### Declarations

```ts
export interface PrebuiltTransactionSignResult {
    success: true;
    signature: string;
    signedTx: string;
}
```

```ts
export declare class PhantasmaLink {
    host: string;
    dapp: string;
    onLogin: ((success: boolean) => void) | null;
    providerHint: string;
    onError: LinkErrorCallback | null;
    socket: PhantasmaLinkSocketLike | null;
    requestCallback: LinkCallback | null;
    private lastSocketErrorMessage;
    socketTransport: 'websocket' | 'injected' | null;
    socketOpen: boolean;
    token: unknown;
    requestID: number;
    account: LinkAccount | null;
    wallet: unknown;
    messageLogging: boolean;
    version: number;
    nexus: string;
    chain: string;
    platform: string;
    constructor(dappID: string, logging?: boolean);
    onMessage: (msg: string) => void;
    private describeFailure;
    login(onLoginCallback: (success: boolean) => void, onErrorCallback: LinkErrorCallback, version?: number, platform?: string, providerHint?: string): void;
    invokeScript(script: string, callback: (message: string | LinkResponse) => void): void;
    signTx(script: string, payload: string | null, callback: LinkCallback, onErrorCallback: LinkErrorCallback, pow?: ProofOfWork, signature?: string): void;
    signCarbonTxAndBroadcast(txMsg: TxMsg, callback?: LinkCallback, onErrorCallback?: (message?: string) => void): void;
    signTxSignature(tx: string, callback: LinkCallback, onErrorCallback: (message?: string) => void, signature?: string): void;
    private decodeWalletSignatureBytes;
    signPrebuiltTransaction(tx: Transaction, callback: (result: PrebuiltTransactionSignResult) => void, onErrorCallback: (message?: string) => void, signature?: string): void;
    multiSig(subject: string, callback: LinkCallback, onErrorCallback: () => void, signature?: string): void;
    getPeer(callback: (result: string) => void, onErrorCallback: () => void): void;
    fetchWallet(callback?: LinkCallback, onErrorCallback?: LinkErrorCallback): void;
    getNexus(callback: LinkCallback, onErrorCallback: LinkErrorCallback): void;
    getWalletVersion(callback: LinkCallback, onErrorCallback: LinkErrorCallback): void;
    signData(data: string, callback: LinkCallback, onErrorCallback: (message: string) => void, signature?: string): void;
    createSocket(isResume?: boolean): void;
    toggleMessageLogging(): void;
    resume(token: unknown): void;
    retry(): void;
    set dappID(dapp: string);
    get dappID(): string;
    sendLinkRequest(request: string, callback: LinkCallback): void;
    private handleSocketFailure;
    disconnect(triggered: string | boolean | undefined): void;
    private serializeCarbonTx;
}
```

```ts
export {};
```

## phantasma-sdk-ts/public

Source: `dist/types/public.d.ts`

### Declarations

```ts
export { PhantasmaAPI } from './rpc/phantasma.js';
```

```ts
export { getRpcErrorMessage, isRpcErrorResult, unwrapRpcResult } from './rpc/rpc-result.js';
```

```ts
export type { JsonRpcErrorObject, JsonRpcErrorResponse, JsonRpcParam, JsonRpcResponse, JsonRpcSuccessResponse, RpcErrorResult, RpcResult, } from './rpc/rpc-result.js';
```

```ts
export type { ABIContract, ABIEvent, ABIMethod, ABIParameter, Account, AccountTransactions, Archive, Auction, Balance, Block, BuildInfoResult, Chain, Channel, CursorPaginatedResult, Dapp, Event as RpcEvent, EventExtended, EventExtendedTyped, ExtendedEventData, Governance, Interop, KeyValue, Leaderboard, LeaderboardRow, Nexus as RpcNexus, NFT, Oracle, Organization, Paginated, Peer, PhantasmaVmConfig, Platform, Receipt, Script, SendRawTx, SignatureResult, Stake, Storage, Swap, Token, TokenData, TokenExternal, TokenPrice, TokenSchemasResult, TokenSeries, TokenSeriesResult, TransactionData, Validator, VmNamedVariableSchemaResult, VmStructSchemaResult, VmVariableSchemaResult, } from './rpc/interfaces/index.js';
```

```ts
export { vmStructSchemaFromRpcResult, vmVariableSchemaFromRpcResult } from './rpc/helpers/index.js';
```

```ts
export { ContractTxHelper, buildContractArtifactBundle, buildContractArtifactManifest, coerceContractBytes, normalizeContractName, ExecutionState, Transaction, } from './tx/index.js';
```

```ts
export type { BuildContractArtifactBundleParams, BuildContractArtifactManifestParams, ContractArtifactBundle, ContractArtifactFileEntry, ContractArtifactManifest, ContractBinaryInput, ContractScriptBuildParams, ContractTransactionBuildParams, ContractTransactionSignParams, } from './tx/index.js';
```

```ts
export { Contracts, Decoder, EventKind, Opcode, ScriptBuilder, TypeAuction, VMObject, VMType, decodeVMObject, getChainValueEventData, getGasEventData, getInfusionEventData, getMarketEventData, getString, getTokenEventData, getTransactionSettleEventData, } from './vm/index.js';
```

```ts
export type { ChainValueEventData, GasEventData, InfusionEventData, MarketEventData, TokenEventData, TransactionSettleEventData, } from './vm/index.js';
```

```ts
export { AccountTrigger, Address, AddressKind, Base16, CarbonBinaryReader, CarbonBinaryWriter, ConsensusMode, ContractEvent, ContractInterface, ContractMethod, ContractParameter, CustomSerializer, Describer, DomainSettings, Ed25519Signature, Entropy, OrganizationTrigger, PBinaryReader, PBinaryWriter, PhantasmaKeys, PollChoice, PollPresence, PollState, PollValue, PollVote, Serialization, Stack, StakeReward, Timestamp, TokenTrigger, TriggerResult, bigIntToTwosComplementLE, readBlob, twosComplementLEToBigInt, writeBlob, } from './types/index.js';
```

```ts
export type { CustomReader, CustomWriter } from './types/index.js';
```

```ts
export { Bytes16, Bytes32, Bytes64, CarbonBlob, CarbonTokenFlags, CreateTokenSeriesTxHelper, CreateTokenTxHelper, FieldType, IntX, MetadataField, MintNonFungibleTxHelper, MintPhantasmaNonFungibleTxHelper, ModuleId, NftRomBuilder, PhantasmaNftRomBuilder, PhantasmaNftMintInfo, PhantasmaNftMintResult, SeriesInfo, SeriesInfoBuilder, SignedTxMsg, SmallString, StandardMeta, TokenContractMethods, TokenHelper, TokenInfo, TokenInfoBuilder, TokenMetadataBuilder, TokenSchemas, TokenSchemasBuilder, TokenSchemasJson, TokenSeriesMetadataBuilder, TxMsg, TxMsgBurnFungible, TxMsgBurnFungibleGasPayer, TxMsgBurnNonFungible, TxMsgBurnNonFungibleGasPayer, TxMsgCall, TxMsgCallMulti, TxMsgMintFungible, TxMsgMintNonFungible, TxMsgPhantasma, TxMsgPhantasmaRaw, TxMsgSigner, TxMsgSpecialResolution, TxMsgTrade, TxMsgTransferFungible, TxMsgTransferFungibleGasPayer, TxMsgTransferNonFungibleMulti, TxMsgTransferNonFungibleMultiGasPayer, TxMsgTransferNonFungibleSingle, TxMsgTransferNonFungibleSingleGasPayer, TxTypes, TokenListing, VmDynamicStruct, VmDynamicVariable, VmNamedDynamicVariable, VmNamedVariableSchema, VmStructArray, VmStructFlags, VmStructSchema, VmType, VmVariableSchema, Witness, findMetadataField, nftDefaultMetadataFields, parseTokenSchemasJson, pushMetadataField, seriesDefaultMetadataFields, standardMetadataFields, } from './types/carbon/index.js';
```

```ts
export type { MetadataValueInput } from './types/carbon/index.js';
```

```ts
export { ANONYMOUS_NAME, ENTRY_CONTEXT_NAME, GENESIS_NAME, NULL_NAME, arrayNumberToUint8Array, bigIntToByteArray, bytesToHex, decodeBase16, encodeBase16, getDifficulty, hexStringToUint8Array, hexToBytes, isReservedIdentifier, isValidIdentifier, isValidTicker, numberToByteArray, reverseHex, setLogger, stringToUint8Array, uint8ArrayToBytes, uint8ArrayToNumberArray, uint8ArrayToString, uint8ArrayToStringDefault, } from './utils/index.js';
```

```ts
export type { Logger } from './utils/index.js';
```

```ts
export { generateNewSeed, generateNewSeedWords, generateNewWif, getAddressFromWif, getPrivateKeyFromWif, getPublicKeyFromPrivateKey, getWifFromPrivateKey, signData, verifyData, } from './tx/utils.js';
```

```ts
export { EasyConnect } from './link/easy-connect.js';
```

```ts
export { EasyScript, Nexus } from './link/easy-script.js';
```

```ts
export { PhantasmaLink } from './link/phantasma-link.js';
```

```ts
export { ProofOfWork } from './link/interfaces/proof-of-work.js';
```

```ts
export type { LinkAccount, LinkFile } from './link/index.js';
```

```ts
export type { PrebuiltTransactionSignResult } from './link/phantasma-link.js';
```

```ts
export { Signature, SignatureKind } from './interfaces/signature.js';
```

```ts
export { NativeContractKind } from './interfaces/contract.js';
```

```ts
export { TokenFlags, TokenSeriesMode } from './interfaces/token.js';
```

```ts
export { getAddressFromLedger, getAddressFromPrivateKey, getAddressFromPublicKey, getAddressPublicKeyFromPublicKey, } from './ledger/index.js';
```

```ts
export type { CarbonBlobLike } from './interfaces/carbon/carbon-blob-like.js';
```

```ts
export type { ContractDescriptor } from './interfaces/contract.js';
```

```ts
export type { FeeOptionsLike } from './types/carbon/blockchain/tx-helpers/fee-options.js';
```

```ts
export type { KeyPair } from './interfaces/key-pair.js';
```

```ts
export type { Ledger } from './ledger/interfaces/ledger.js';
```

```ts
export type { Serializable } from './interfaces/serializable.js';
```

```ts
export type { StackLike } from './interfaces/stack.js';
```

```ts
export type { TokenDescriptor } from './interfaces/token.js';
```

## phantasma-sdk-ts/rpc/helpers

Source: `dist/types/rpc/helpers/index.d.ts`

### Declarations

```ts
export * from './vm-schema-helpers.js';
```

## phantasma-sdk-ts/rpc/helpers/vm-schema-helpers

Source: `dist/types/rpc/helpers/vm-schema-helpers.d.ts`

### Declarations

```ts
export declare function vmStructSchemaFromRpcResult(r: VmStructSchemaResult): VmStructSchema;
```

```ts
export declare function vmVariableSchemaFromRpcResult(v: VmVariableSchemaResult): VmVariableSchema;
```

## phantasma-sdk-ts/rpc

Source: `dist/types/rpc/index.d.ts`

### Declarations

```ts
export * from './helpers/index.js';
```

```ts
export * from './interfaces/index.js';
```

```ts
export * from './phantasma.js';
```

```ts
export * from './rpc-result.js';
```

## phantasma-sdk-ts/rpc/interfaces/abi-contract

Source: `dist/types/rpc/interfaces/abi-contract.d.ts`

### Declarations

```ts
export interface ABIContract {
    name: string;
    methods: Array<ABIMethod>;
}
```

## phantasma-sdk-ts/rpc/interfaces/abi-event

Source: `dist/types/rpc/interfaces/abi-event.d.ts`

### Declarations

```ts
export interface ABIEvent {
    value: number;
    name: string;
    returnType: string;
    description: string;
}
```

## phantasma-sdk-ts/rpc/interfaces/abi-method

Source: `dist/types/rpc/interfaces/abi-method.d.ts`

### Declarations

```ts
export interface ABIMethod {
    name: string;
    returnType: string;
    parameters: Array<ABIParameter>;
}
```

## phantasma-sdk-ts/rpc/interfaces/abi-parameter

Source: `dist/types/rpc/interfaces/abi-parameter.d.ts`

### Declarations

```ts
export interface ABIParameter {
    name: string;
    type: string;
}
```

## phantasma-sdk-ts/rpc/interfaces/account-transactions

Source: `dist/types/rpc/interfaces/account-transactions.d.ts`

### Declarations

```ts
export interface AccountTransactions {
    address: string;
    txs: Array<TransactionData>;
}
```

## phantasma-sdk-ts/rpc/interfaces/account

Source: `dist/types/rpc/interfaces/account.d.ts`

### Declarations

```ts
export interface Account {
    address: string;
    name: string;
    stakes: Stake;
    stake: string;
    unclaimed: string;
    relay: string;
    validator: string;
    storage: Storage;
    balances: Array<Balance>;
    txs: Array<string>;
}
```

## phantasma-sdk-ts/rpc/interfaces/archive

Source: `dist/types/rpc/interfaces/archive.d.ts`

### Declarations

```ts
export interface Archive {
    name: string;
    hash: string;
    time: number;
    size: number;
    encryption: string;
    blockCount: number;
    missingBlocks: Array<number>;
    owners: Array<string>;
}
```

## phantasma-sdk-ts/rpc/interfaces/auction

Source: `dist/types/rpc/interfaces/auction.d.ts`

### Declarations

```ts
export interface Auction {
    creatorAddress: string;
    chainAddress: string;
    startDate: number;
    endDate: number;
    baseSymbol: string;
    quoteSymbol: string;
    tokenId: string;
    price: string;
    endPrice: string;
    extensionPeriod: string;
    type: string;
    rom: string;
    ram: string;
    listingFee: string;
    currentWinner: string;
}
```

## phantasma-sdk-ts/rpc/interfaces/balance

Source: `dist/types/rpc/interfaces/balance.d.ts`

### Declarations

```ts
export interface Balance {
    chain: string;
    amount: string;
    symbol: string;
    decimals: number;
    ids?: Array<string>;
}
```

## phantasma-sdk-ts/rpc/interfaces/block

Source: `dist/types/rpc/interfaces/block.d.ts`

### Declarations

```ts
export interface Block {
    hash: string;
    previousHash: string;
    timestamp: number;
    height: number;
    chainAddress: string;
    protocol: number;
    txs: Array<TransactionData>;
    validatorAddress: string;
    reward: string;
    events: Array<Event>;
    oracles: Array<Oracle>;
}
```

## phantasma-sdk-ts/rpc/interfaces/build-info-result

Source: `dist/types/rpc/interfaces/build-info-result.d.ts`

### Declarations

```ts
export interface BuildInfoResult {
    version: string;
    commit: string;
    buildTimeUtc: string;
}
```

## phantasma-sdk-ts/rpc/interfaces/chain

Source: `dist/types/rpc/interfaces/chain.d.ts`

### Declarations

```ts
export interface Chain {
    name: string;
    address: string;
    parent: string;
    height: number;
    organization: string;
    contracts: Array<string>;
    dapps: Array<string>;
}
```

## phantasma-sdk-ts/rpc/interfaces/channel

Source: `dist/types/rpc/interfaces/channel.d.ts`

### Declarations

```ts
export interface Channel {
    creatorAddress: string;
    targetAddress: string;
    name: string;
    chain: string;
    creationTime: number;
    symbol: string;
    fee: string;
    balance: string;
    active: boolean;
    index: number;
}
```

## phantasma-sdk-ts/rpc/interfaces/contract

Source: `dist/types/rpc/interfaces/contract.d.ts`

### Declarations

```ts
export interface Contract {
    name: string;
    address: string;
    owner: string;
    script: string;
    methods?: Array<ABIMethod>;
    events?: Array<ABIEvent>;
}
```

## phantasma-sdk-ts/rpc/interfaces/cursor-paginated-result

Source: `dist/types/rpc/interfaces/cursor-paginated-result.d.ts`

### Declarations

```ts
export interface CursorPaginatedResult<T> {
    result?: T;
    cursor?: string;
}
```

## phantasma-sdk-ts/rpc/interfaces/dapp

Source: `dist/types/rpc/interfaces/dapp.d.ts`

### Declarations

```ts
export interface Dapp {
    name: string;
    address: string;
    chain: string;
}
```

## phantasma-sdk-ts/rpc/interfaces/event-extended

Source: `dist/types/rpc/interfaces/event-extended.d.ts`

### Declarations

```ts
export interface TokenCreateData {
    symbol: string;
    maxSupply: string;
    decimals: number;
    isNonFungible: boolean;
    carbonTokenId: string;
    metadata: Record<string, string>;
}
```

```ts
export interface TokenSeriesCreateData {
    symbol: string;
    seriesId: string;
    maxMint: number;
    maxSupply: number;
    owner: string;
    carbonTokenId: string;
    carbonSeriesId: number;
    metadata: Record<string, string>;
}
```

```ts
export interface TokenMintData {
    symbol: string;
    tokenId: string;
    seriesId: string;
    mintNumber: number;
    carbonTokenId: string;
    carbonSeriesId: number;
    carbonInstanceId: string;
    owner: string;
    metadata: Record<string, string>;
}
```

```ts
export interface MarketOrderData {
    baseSymbol: string;
    quoteSymbol: string;
    tokenId: string;
    carbonBaseTokenId: string;
    carbonQuoteTokenId: string;
    carbonInstanceId: string;
    seller: string;
    buyer: string;
    price: string;
    endPrice: string;
    startDate: number;
    endDate: number;
    type: string;
}
```

```ts
export interface SpecialResolutionCall {
    moduleId: number;
    module: string;
    methodId: number;
    method: string;
    arguments?: Record<string, string>;
    calls?: SpecialResolutionCall[];
}
```

```ts
export interface SpecialResolutionData {
    resolutionId: string;
    description?: string;
    calls: SpecialResolutionCall[];
}
```

```ts
export type ExtendedEventData = TokenCreateData | TokenSeriesCreateData | TokenMintData | MarketOrderData | SpecialResolutionData;
```

```ts
export interface EventExtended<T = unknown> {
    address: string;
    contract: string;
    kind: string;
    data: T;
}
```

```ts
export type EventExtendedTyped = EventExtended<ExtendedEventData>;
```

## phantasma-sdk-ts/rpc/interfaces/event

Source: `dist/types/rpc/interfaces/event.d.ts`

### Declarations

```ts
export interface Event {
    address: string;
    contract: string;
    kind: string;
    name: string;
    data: string;
}
```

## phantasma-sdk-ts/rpc/interfaces/governance

Source: `dist/types/rpc/interfaces/governance.d.ts`

### Declarations

```ts
export interface Governance {
    name: string;
    value: string;
}
```

## phantasma-sdk-ts/rpc/interfaces

Source: `dist/types/rpc/interfaces/index.d.ts`

### Declarations

```ts
export * from './abi-contract.js';
```

```ts
export * from './abi-event.js';
```

```ts
export * from './abi-method.js';
```

```ts
export * from './abi-parameter.js';
```

```ts
export * from './account.js';
```

```ts
export * from './account-transactions.js';
```

```ts
export * from './archive.js';
```

```ts
export * from './auction.js';
```

```ts
export * from './balance.js';
```

```ts
export * from './block.js';
```

```ts
export * from './chain.js';
```

```ts
export * from './channel.js';
```

```ts
export * from './contract.js';
```

```ts
export * from './dapp.js';
```

```ts
export * from './event.js';
```

```ts
export * from './event-extended.js';
```

```ts
export * from './governance.js';
```

```ts
export * from './interop.js';
```

```ts
export * from './key-value.js';
```

```ts
export * from './leaderboard.js';
```

```ts
export * from './leaderboard-row.js';
```

```ts
export * from './nexus.js';
```

```ts
export * from './nft.js';
```

```ts
export * from './oracle.js';
```

```ts
export * from './organization.js';
```

```ts
export * from './paginated.js';
```

```ts
export * from './peer.js';
```

```ts
export * from './platform.js';
```

```ts
export * from './receipt.js';
```

```ts
export * from './script.js';
```

```ts
export * from './send-raw-tx.js';
```

```ts
export * from './signature-result.js';
```

```ts
export * from './stake.js';
```

```ts
export * from './storage.js';
```

```ts
export * from './swap.js';
```

```ts
export * from './token.js';
```

```ts
export * from './token-data.js';
```

```ts
export * from './token-external.js';
```

```ts
export * from './token-price.js';
```

```ts
export * from './token-series.js';
```

```ts
export * from './transaction-data.js';
```

```ts
export * from './validator.js';
```

```ts
export * from './cursor-paginated-result.js';
```

```ts
export * from './token-series-result.js';
```

```ts
export * from './build-info-result.js';
```

```ts
export * from './phantasma-vm-config.js';
```

```ts
export * from './token-schemas-result.js';
```

```ts
export * from './vm-named-variable-schema-result.js';
```

```ts
export * from './vm-struct-schema-result.js';
```

```ts
export * from './vm-variable-schema-result.js';
```

## phantasma-sdk-ts/rpc/interfaces/interop

Source: `dist/types/rpc/interfaces/interop.d.ts`

### Declarations

```ts
export interface Interop {
    local: string;
    external: string;
}
```

## phantasma-sdk-ts/rpc/interfaces/key-value

Source: `dist/types/rpc/interfaces/key-value.d.ts`

### Declarations

```ts
export interface KeyValue {
    key: string;
    value: string;
}
```

## phantasma-sdk-ts/rpc/interfaces/leaderboard-row

Source: `dist/types/rpc/interfaces/leaderboard-row.d.ts`

### Declarations

```ts
export interface LeaderboardRow {
    address: string;
    value: string;
}
```

## phantasma-sdk-ts/rpc/interfaces/leaderboard

Source: `dist/types/rpc/interfaces/leaderboard.d.ts`

### Declarations

```ts
export interface Leaderboard {
    name: string;
    rows: Array<LeaderboardRow>;
}
```

## phantasma-sdk-ts/rpc/interfaces/nexus

Source: `dist/types/rpc/interfaces/nexus.d.ts`

### Declarations

```ts
export interface Nexus {
    name: string;
    protocol: string;
    platforms: Array<Platform>;
    tokens: Array<Token>;
    chains: Array<Chain>;
    governance: Array<Governance>;
    organizations: Array<string>;
}
```

## phantasma-sdk-ts/rpc/interfaces/nft

Source: `dist/types/rpc/interfaces/nft.d.ts`

### Declarations

```ts
export interface NFT {
    ID: string;
    series: string;
    carbonTokenId: string;
    carbonNftAddress: string;
    mint: string;
    chainName: string;
    ownerAddress: string;
    creatorAddress: string;
    ram: string;
    rom: string;
    status: string;
    infusion: KeyValue[];
    properties: KeyValue[];
}
```

## phantasma-sdk-ts/rpc/interfaces/oracle

Source: `dist/types/rpc/interfaces/oracle.d.ts`

### Declarations

```ts
export interface Oracle {
    url: string;
    content: string;
}
```

## phantasma-sdk-ts/rpc/interfaces/organization

Source: `dist/types/rpc/interfaces/organization.d.ts`

### Declarations

```ts
export interface Organization {
    id: string;
    name: string;
    members: Array<string>;
}
```

## phantasma-sdk-ts/rpc/interfaces/paginated

Source: `dist/types/rpc/interfaces/paginated.d.ts`

### Declarations

```ts
export interface Paginated<T> {
    page: number;
    pageSize: number;
    total: number;
    totalPages: number;
    result: T;
}
```

## phantasma-sdk-ts/rpc/interfaces/peer

Source: `dist/types/rpc/interfaces/peer.d.ts`

### Declarations

```ts
export interface Peer {
    url: string;
    version: string;
    flags: string;
    fee: string;
    pow: number;
}
```

## phantasma-sdk-ts/rpc/interfaces/phantasma-vm-config

Source: `dist/types/rpc/interfaces/phantasma-vm-config.d.ts`

### Declarations

```ts
export interface PhantasmaVmConfig {
    isStored: boolean;
    featureLevel: number;
    gasConstructor: string;
    gasNexus: string;
    gasOrganization: string;
    gasAccount: string;
    gasLeaderboard: string;
    gasStandard: string;
    gasOracle: string;
    fuelPerContractDeploy: string;
}
```

## phantasma-sdk-ts/rpc/interfaces/platform

Source: `dist/types/rpc/interfaces/platform.d.ts`

### Declarations

```ts
export interface Platform {
    platform: string;
    chain: string;
    fuel: string;
    tokens: Array<string>;
    interop: Array<Interop>;
}
```

## phantasma-sdk-ts/rpc/interfaces/receipt

Source: `dist/types/rpc/interfaces/receipt.d.ts`

### Declarations

```ts
export interface Receipt {
    nexus: string;
    channel: string;
    index: string;
    timestamp: number;
    sender: string;
    receiver: string;
    script: string;
}
```

## phantasma-sdk-ts/rpc/interfaces/script

Source: `dist/types/rpc/interfaces/script.d.ts`

### Declarations

```ts
export interface Script {
    events: Array<Event>;
    result: string;
    results: Array<string>;
    oracles: Array<Oracle>;
    error?: string;
}
```

## phantasma-sdk-ts/rpc/interfaces/send-raw-tx

Source: `dist/types/rpc/interfaces/send-raw-tx.d.ts`

### Declarations

```ts
export interface SendRawTx {
    hash: string;
    error: string;
}
```

## phantasma-sdk-ts/rpc/interfaces/signature-result

Source: `dist/types/rpc/interfaces/signature-result.d.ts`

### Declarations

```ts
export interface SignatureResult {
    Kind: string;
    Data: string;
}
```

## phantasma-sdk-ts/rpc/interfaces/stake

Source: `dist/types/rpc/interfaces/stake.d.ts`

### Declarations

```ts
export interface Stake {
    amount: string;
    time: number;
    unclaimed: string;
}
```

## phantasma-sdk-ts/rpc/interfaces/storage

Source: `dist/types/rpc/interfaces/storage.d.ts`

### Declarations

```ts
export interface Storage {
    available: number;
    used: number;
    avatar: string;
    archives: Array<Archive>;
}
```

## phantasma-sdk-ts/rpc/interfaces/swap

Source: `dist/types/rpc/interfaces/swap.d.ts`

### Declarations

```ts
export interface Swap {
    sourcePlatform: string;
    sourceChain: string;
    sourceHash: string;
    sourceAddress: string;
    destinationPlatform: string;
    destinationChain: string;
    destinationHash: string;
    destinationAddress: string;
    symbol: string;
    value: string;
}
```

## phantasma-sdk-ts/rpc/interfaces/token-data

Source: `dist/types/rpc/interfaces/token-data.d.ts`

### Declarations

```ts
export interface TokenData {
    ID: string;
    series: string;
    carbonTokenId: string;
    carbonNftAddress: string;
    mint: string;
    chainName: string;
    ownerAddress: string;
    creatorAddress: string;
    ram: string;
    rom: string;
    status: string;
    infusion: KeyValue[];
    properties: KeyValue[];
}
```

## phantasma-sdk-ts/rpc/interfaces/token-external

Source: `dist/types/rpc/interfaces/token-external.d.ts`

### Declarations

```ts
export interface TokenExternal {
    platform: string;
    hash: string;
}
```

## phantasma-sdk-ts/rpc/interfaces/token-price

Source: `dist/types/rpc/interfaces/token-price.d.ts`

### Declarations

```ts
export interface TokenPrice {
    Timestamp: number;
    Open: string;
    High: string;
    Low: string;
    Close: string;
}
```

## phantasma-sdk-ts/rpc/interfaces/token-schemas-result

Source: `dist/types/rpc/interfaces/token-schemas-result.d.ts`

### Declarations

```ts
export interface TokenSchemasResult {
    seriesMetadata: VmStructSchemaResult;
    rom: VmStructSchemaResult;
    ram: VmStructSchemaResult;
}
```

## phantasma-sdk-ts/rpc/interfaces/token-series-result

Source: `dist/types/rpc/interfaces/token-series-result.d.ts`

### Declarations

```ts
export interface TokenSeriesResult {
    seriesId: string;
    carbonTokenId: string;
    carbonSeriesId: string;
    currentSupply: string;
    maxSupply: string;
    burnedSupply: string;
    mode: string;
    script: string;
    methods: ABIMethod[];
    metadata: KeyValue[];
}
```

## phantasma-sdk-ts/rpc/interfaces/token-series

Source: `dist/types/rpc/interfaces/token-series.d.ts`

### Declarations

```ts
export type TokenSeries = TokenSeriesResult;
```

## phantasma-sdk-ts/rpc/interfaces/token

Source: `dist/types/rpc/interfaces/token.d.ts`

### Declarations

```ts
export interface Token {
    symbol: string;
    name: string;
    decimals: number;
    currentSupply: string;
    maxSupply: string;
    burnedSupply: string;
    address: string;
    owner: string;
    flags: string;
    script: string;
    series: Array<TokenSeries>;
    carbonId: string;
    tokenSchemas?: TokenSchemasResult;
    external?: Array<TokenExternal>;
    price?: Array<TokenPrice>;
}
```

## phantasma-sdk-ts/rpc/interfaces/transaction-data

Source: `dist/types/rpc/interfaces/transaction-data.d.ts`

### Declarations

```ts
export interface TransactionData {
    hash: string;
    chainAddress: string;
    timestamp: number;
    blockHeight: number;
    blockHash: string;
    script: string;
    payload: string;
    carbonTxType: number;
    carbonTxData: string;
    events: Array<Event>;
    extendedEvents?: Array<EventExtended>;
    result: string;
    debugComment: string;
    fee: string;
    state: string;
    signatures: Array<SignatureResult>;
    sender: string;
    gasPayer: string;
    gasTarget: string;
    gasPrice: string;
    gasLimit: string;
    expiration: number;
}
```

## phantasma-sdk-ts/rpc/interfaces/validator

Source: `dist/types/rpc/interfaces/validator.d.ts`

### Declarations

```ts
export interface Validator {
    address: string;
    type: string;
}
```

## phantasma-sdk-ts/rpc/interfaces/vm-named-variable-schema-result

Source: `dist/types/rpc/interfaces/vm-named-variable-schema-result.d.ts`

### Declarations

```ts
export interface VmNamedVariableSchemaResult {
    name: string;
    schema: VmVariableSchemaResult;
}
```

## phantasma-sdk-ts/rpc/interfaces/vm-struct-schema-result

Source: `dist/types/rpc/interfaces/vm-struct-schema-result.d.ts`

### Declarations

```ts
export interface VmStructSchemaResult {
    fields: VmNamedVariableSchemaResult[];
    flags: number;
}
```

## phantasma-sdk-ts/rpc/interfaces/vm-variable-schema-result

Source: `dist/types/rpc/interfaces/vm-variable-schema-result.d.ts`

### Declarations

```ts
export interface VmVariableSchemaResult {
    type: string;
    schema?: VmStructSchemaResult;
}
```

## phantasma-sdk-ts/rpc/phantasma

Source: `dist/types/rpc/phantasma.d.ts`

### Declarations

```ts
export declare class PhantasmaAPI {
    host: string;
    rpcName: string;
    nexus: string;
    availableHosts: RpcPeer[];
    pingAsync(host: string): Promise<number>;
    constructor(defHost: string, peersUrlJson: string | undefined | null, nexus: string);
    JSONRPCResult<T = unknown>(method: string, params: JsonRpcParam[]): Promise<RpcResult<T>>;
    JSONRPC(method: string, params: JsonRpcParam[]): Promise<unknown>;
    setRpcHost(rpcHost: string): void;
    setRpcByName(rpcName: string): void;
    setNexus(nexus: string): void;
    updateRpc(): void;
    convertDecimals(amount: number, decimals: number): number;
    getAccount(account: string, extended?: boolean): Promise<Account>;
    getAccounts(accounts: string[], extended?: boolean): Promise<Account[]>;
    lookUpName(name: string): Promise<string>;
    getBlockHeight(chainInput: string): Promise<number>;
    getBlockTransactionCountByHash(chainAddressOrName: string, blockHash: string): Promise<number>;
    getBlockByHash(blockHash: string): Promise<Block>;
    getBlockByHeight(chainInput: string, height: number): Promise<Block>;
    getLatestBlock(chainInput: string): Promise<Block>;
    getTransactionByBlockHashAndIndex(chainAddressOrName: string, blockHash: string, index: number): Promise<TransactionData>;
    getAddressTransactions(account: string, page: number, pageSize: number): Promise<Paginated<AccountTransactions>>;
    getAddressTransactionCount(account: string, chainInput: string): Promise<number>;
    sendRawTransaction(txData: string): Promise<string>;
    sendCarbonTransaction(txData: string): Promise<string>;
    invokeRawScript(chainInput: string, scriptData: string): Promise<Script>;
    getTransaction(hashText: string): Promise<TransactionData>;
    getChains(extended?: boolean): Promise<Chain[]>;
    getChain(name: string, extended?: boolean): Promise<Chain>;
    getNexus(extended?: boolean): Promise<Nexus>;
    getContracts(chainAddressOrName?: string, extended?: boolean): Promise<Contract[]>;
    getContract(chainAddressOrName: string | undefined, contractName: string): Promise<Contract>;
    getContractByAddress(chainAddressOrName: string | undefined, contractAddress: string): Promise<Contract>;
    getOrganization(ID: string, extended?: boolean): Promise<Organization>;
    getOrganizationByName(name: string, extended?: boolean): Promise<Organization>;
    getOrganizations(extended?: boolean): Promise<Organization[]>;
    getLeaderboard(name: string): Promise<Leaderboard>;
    getTokens(ownerAddress: string | undefined | null, extended?: boolean): Promise<Token[]>;
    getToken(symbol: string, extended?: boolean, carbonTokenId?: bigint): Promise<Token>;
    getTokenData(symbol: string, IDtext: string): Promise<TokenData>;
    getTokenBalance(account: string, tokenSymbol: string, chainInput: string, checkAddressResevedByte?: boolean): Promise<Balance>;
    getTokenSeries(symbol: string, carbonTokenId: bigint, pageSize?: number, cursor?: string): Promise<CursorPaginatedResult<TokenSeriesResult[]>>;
    getTokenSeriesById(symbol: string, carbonTokenId: bigint, seriesId: string, carbonSeriesId: number): Promise<TokenSeriesResult>;
    getTokenNFTs(carbonTokenId: bigint, carbonSeriesId?: number, pageSize?: number, cursor?: string, extended?: boolean): Promise<CursorPaginatedResult<NFT[]>>;
    getAccountFungibleTokens(account: string, tokenSymbol?: string, carbonTokenId?: bigint, pageSize?: number, cursor?: string, checkAddressReservedByte?: boolean): Promise<CursorPaginatedResult<Balance[]>>;
    getAccountNFTs(account: string, tokenSymbol?: string, carbonTokenId?: bigint, carbonSeriesId?: number, pageSize?: number, cursor?: string, extended?: boolean, checkAddressReservedByte?: boolean): Promise<CursorPaginatedResult<NFT[]>>;
    getAccountOwnedTokens(account: string, tokenSymbol?: string, carbonTokenId?: bigint, pageSize?: number, cursor?: string, checkAddressReservedByte?: boolean): Promise<CursorPaginatedResult<Token[]>>;
    getAccountOwnedTokenSeries(account: string, tokenSymbol?: string, carbonTokenId?: bigint, pageSize?: number, cursor?: string, checkAddressReservedByte?: boolean): Promise<CursorPaginatedResult<TokenSeriesResult[]>>;
    getAuctionsCount(chainAddressOrName: string, symbol: string): Promise<number>;
    getAuctions(chainAddressOrName: string, symbol: string, page: number, pageSize: number): Promise<Auction>;
    getAuction(chainAddressOrName: string, symbol: string, IDtext: string): Promise<Auction>;
    getArchive(hashText: string): Promise<Archive>;
    writeArchive(hashText: string, blockIndex: number, blockContent: string): Promise<boolean>;
    getNFT(symbol: string, nftId: string, extended?: boolean): Promise<NFT>;
    getNFTs(symbol: string, nftIDs: string[], extended?: boolean): Promise<NFT[]>;
    getVersion(): Promise<BuildInfoResult>;
    getPhantasmaVmConfig(chainAddressOrName: string): Promise<PhantasmaVmConfig>;
}
```

```ts
export {};
```

## phantasma-sdk-ts/rpc/rpc-result

Source: `dist/types/rpc/rpc-result.d.ts`

### Declarations

```ts
export type JsonRpcParam = string | number | boolean | null | undefined;
```

```ts
export interface JsonRpcErrorObject {
    code?: number;
    message?: string;
    data?: unknown;
}
```

```ts
export interface JsonRpcSuccessResponse<T> {
    jsonrpc?: string;
    id?: string | number | null;
    result: T;
}
```

```ts
export interface JsonRpcErrorResponse {
    jsonrpc?: string;
    id?: string | number | null;
    error: string | JsonRpcErrorObject;
}
```

```ts
export type JsonRpcResponse<T> = JsonRpcSuccessResponse<T> | JsonRpcErrorResponse;
```

```ts
export interface RpcErrorResult {
    error: string;
    code?: number;
    data?: unknown;
    status?: number;
    statusText?: string;
}
```

```ts
export type RpcResult<T> = T | RpcErrorResult;
```

```ts
export declare function isRpcErrorResult(value: unknown): value is RpcErrorResult;
```

```ts
export declare function getRpcErrorMessage(value: unknown, fallback?: string): string;
```

```ts
export declare function normalizeRpcError(error: unknown, fallback?: string): RpcErrorResult;
```

```ts
export declare function unwrapRpcResult<T>(result: RpcResult<T>): T;
```

## phantasma-sdk-ts/tx/contract-artifacts

Source: `dist/types/tx/contract-artifacts.d.ts`

### Declarations

```ts
export type ContractBinaryInput = Uint8Array | string;
```

```ts
export interface ContractArtifactFileEntry {
    path: string;
    size: number;
    sha256: string;
}
```

```ts
export interface ContractArtifactManifest {
    format: 'pha.contract.artifacts/v1';
    contractName: string;
    createdAtUtc: string;
    compiler: {
        name: string;
        version: string;
    };
    sourceFile?: string;
    files: {
        script: ContractArtifactFileEntry;
        abi: ContractArtifactFileEntry;
        debug?: ContractArtifactFileEntry;
    };
}
```

```ts
export interface ContractArtifactBundle {
    contractName: string;
    script: Uint8Array;
    abi: Uint8Array;
    debug?: Uint8Array;
    manifest?: ContractArtifactManifest;
}
```

```ts
export interface BuildContractArtifactManifestParams {
    contractName: string;
    compilerName: string;
    compilerVersion: string;
    scriptPath: string;
    script: ContractBinaryInput;
    abiPath: string;
    abi: ContractBinaryInput;
    sourceFile?: string;
    debugPath?: string;
    debug?: ContractBinaryInput;
    createdAtUtc?: string;
}
```

```ts
export interface BuildContractArtifactBundleParams {
    contractName: string;
    script: ContractBinaryInput;
    abi: ContractBinaryInput;
    debug?: ContractBinaryInput;
    manifest?: ContractArtifactManifest;
}
```

```ts
export declare function normalizeContractName(contractName: string): string;
```

```ts
export declare function coerceContractBytes(input: ContractBinaryInput, label: string): Uint8Array;
```

```ts
export declare function buildContractArtifactManifest(params: BuildContractArtifactManifestParams): ContractArtifactManifest;
```

```ts
export declare function buildContractArtifactBundle(params: BuildContractArtifactBundleParams): ContractArtifactBundle;
```

## phantasma-sdk-ts/tx/contract-tx-helper

Source: `dist/types/tx/contract-tx-helper.d.ts`

### Declarations

```ts
export interface ContractScriptBuildParams {
    from: string | Address;
    contractName: string;
    script: ContractBinaryInput;
    abi: ContractBinaryInput;
    gasPrice?: number | bigint;
    gasLimit?: number | bigint;
}
```

```ts
export interface ContractTransactionBuildParams extends ContractScriptBuildParams {
    nexus: string;
    chain?: string;
    expiration?: Date;
    payloadHex?: string;
}
```

```ts
export interface ContractTransactionSignParams extends ContractTransactionBuildParams {
    signer: string | PhantasmaKeys;
    proofOfWork?: number;
}
```

```ts
export declare class ContractTxHelper {
    static readonly DefaultGasPrice: number;
    static readonly DefaultGasLimit = 100000;
    static buildDeployScript(params: ContractScriptBuildParams): string;
    static buildUpgradeScript(params: ContractScriptBuildParams): string;
    static buildDeployTransaction(params: ContractTransactionBuildParams): Transaction;
    static buildUpgradeTransaction(params: ContractTransactionBuildParams): Transaction;
    static buildDeployTransactionAndEncode(params: ContractTransactionSignParams): string;
    static buildUpgradeTransactionAndEncode(params: ContractTransactionSignParams): string;
    static buildDeployScriptFromBundle(bundle: ContractArtifactBundle, from: string | Address, gasPrice?: number | bigint, gasLimit?: number | bigint): string;
    static buildUpgradeScriptFromBundle(bundle: ContractArtifactBundle, from: string | Address, gasPrice?: number | bigint, gasLimit?: number | bigint): string;
    static encodePayloadText(text: string): string;
    private static buildContractLifecycleScript;
    private static buildContractLifecycleTransaction;
    private static signTransaction;
    private static normalizeAddress;
    private static normalizeSmallInteger;
}
```

## phantasma-sdk-ts/tx/execution-state

Source: `dist/types/tx/execution-state.d.ts`

### Declarations

```ts
export declare enum ExecutionState {
    Running = 0,
    Break = 1,
    Fault = 2,
    Halt = 3
}
```

## phantasma-sdk-ts/tx

Source: `dist/types/tx/index.d.ts`

### Declarations

```ts
export * from './execution-state.js';
```

```ts
export * from './contract-artifacts.js';
```

```ts
export * from './contract-tx-helper.js';
```

```ts
export * from './transaction.js';
```

```ts
export * from './utils.js';
```

## phantasma-sdk-ts/tx/transaction

Source: `dist/types/tx/transaction.d.ts`

### Declarations

```ts
export declare class Transaction implements ISerializable {
    script: string;
    nexusName: string;
    chainName: string;
    payload: string;
    expiration: Date;
    signatures: Array<Signature>;
    hash: string;
    static fromHex(serializedData: string): Transaction;
    static fromBytes(serializedData: Uint8Array): Transaction;
    /** @deprecated Use `fromHex` for serialized hex strings. This alias will be removed in v1.0. */
    static FromBytes(serializedData: string): Transaction;
    constructor(nexusName: string, chainName: string, script: string, // Should be HexString
    expiration: Date, payload: string);
    sign(wif: string): void;
    signWithPrivateKey(privateKey: string): void;
    signWithKeys(keys: PhantasmaKeys): void;
    verifySignature(address: Address | string): boolean;
    /** @deprecated Use `verifySignature` instead. This alias will be removed in v1.0. */
    VerifySignature(address: Address | string): boolean;
    verifySignatures(addresses: Array<Address | string>): {
        ok: boolean;
        matched: string[];
    };
    /** @deprecated Use `verifySignatures` instead. This alias will be removed in v1.0. */
    VerifySignatures(addresses: Array<Address | string>): {
        ok: boolean;
        matched: string[];
    };
    getUnsignedBytes(): Uint8Array;
    /** @deprecated Use `getUnsignedBytes` instead. This alias will be removed in v1.0. */
    GetUnsignedBytes(): Uint8Array;
    getSignatureInfo(): Array<{
        kind: number;
        length: number;
    }>;
    /** @deprecated Use `getSignatureInfo` instead. This alias will be removed in v1.0. */
    GetSignatureInfo(): Array<{
        kind: number;
        length: number;
    }>;
    toByteArray(withSignature: boolean): Uint8Array;
    /** @deprecated Use `toByteArray` instead. This typoed alias will be removed in v1.0. */
    ToByteAray(withSignature: boolean): Uint8Array;
    unserializeData(reader: PBinaryReader): void;
    /** @deprecated Use `unserializeData` instead. This alias will be removed in v1.0. */
    UnserializeData(reader: PBinaryReader): void;
    serializeData(writer: PBinaryWriter): void;
    /** @deprecated Use `serializeData` instead. This alias will be removed in v1.0. */
    SerializeData(writer: PBinaryWriter): void;
    toString(withSignature: boolean): string;
    toStringEncoded(withSignature: boolean): string;
    /** @deprecated Use `toStringEncoded` instead. This alias will be removed in v1.0. */
    ToStringEncoded(withSignature: boolean): string;
    getHash(): string;
    mineTransaction(difficulty: number): void;
    private getSign;
    unserialize(serializedData: string): Transaction;
    static deserialize(serialized: Uint8Array): Transaction;
    /** @deprecated Use `deserialize` instead. This alias will be removed in v1.0. */
    static Unserialize(serialized: Uint8Array): Transaction;
}
```

## phantasma-sdk-ts/tx/utils

Source: `dist/types/tx/utils.d.ts`

### Declarations

```ts
export declare function getPrivateKeyFromWif(wif: string): string;
```

```ts
export declare function getAddressFromWif(wif: string): string;
```

```ts
export declare function getPublicKeyFromPrivateKey(privateKey: string): string;
```

```ts
export declare function generateNewSeed(): string;
```

```ts
export declare function generateNewSeedWords(): string[];
```

```ts
export declare function generateNewWif(): string;
```

```ts
export declare function getWifFromPrivateKey(privateKey: string): string;
```

```ts
export declare function signData(msgHex: string, privateKey: string): string;
```

```ts
export declare function verifyData(msgHex: string, phaSig: string, address: string): boolean;
```

## phantasma-sdk-ts/types/address

Source: `dist/types/types/address.d.ts`

### Declarations

```ts
export declare enum AddressKind {
    Invalid = 0,
    User = 1,
    System = 2,
    Interop = 3
}
```

```ts
export declare class Address implements ISerializable {
    static readonly nullText: string;
    /** @deprecated Use `nullText` instead. This alias will be removed in v1.0. */
    static readonly NullText: string;
    static readonly lengthInBytes: number;
    /** @deprecated Use `lengthInBytes` instead. This alias will be removed in v1.0. */
    static readonly LengthInBytes: number;
    static readonly maxPlatformNameLength: number;
    /** @deprecated Use `maxPlatformNameLength` instead. This alias will be removed in v1.0. */
    static readonly MaxPlatformNameLength: number;
    private static nullPublicKey;
    static readonly nullAddress: Address;
    /** @deprecated Use `nullAddress` instead. This alias will be removed in v1.0. */
    static readonly Null: Address;
    private _bytes;
    get kind(): AddressKind;
    /** @deprecated Use `kind` instead. This alias will be removed in v1.0. */
    get Kind(): AddressKind;
    get isSystem(): boolean;
    /** @deprecated Use `isSystem` instead. This alias will be removed in v1.0. */
    get IsSystem(): boolean;
    get isInterop(): boolean;
    /** @deprecated Use `isInterop` instead. This alias will be removed in v1.0. */
    get IsInterop(): boolean;
    get isUser(): boolean;
    /** @deprecated Use `isUser` instead. This alias will be removed in v1.0. */
    get IsUser(): boolean;
    get isNull(): boolean;
    /** @deprecated Use `isNull` instead. This alias will be removed in v1.0. */
    get IsNull(): boolean;
    private _text;
    private static _keyToTextCache;
    get text(): string;
    /** @deprecated Use `text` instead. This alias will be removed in v1.0. */
    get Text(): string;
    private constructor();
    static fromPublicKey(publicKey: Uint8Array): Address;
    /** @deprecated Use `fromBytes` for 34-byte address data. This typoed alias will be removed in v1.0. */
    static FromPublickKey(bytes: Uint8Array): Address;
    static fromText(text: string): Address;
    /** @deprecated Use `fromText` instead. This alias will be removed in v1.0. */
    static FromText(text: string): Address;
    static parse(text: string): Address;
    /** @deprecated Use `parse` instead. This alias will be removed in v1.0. */
    static Parse(text: string): Address;
    static isValidAddress(text: string): boolean;
    /** @deprecated Use `isValidAddress` instead. This alias will be removed in v1.0. */
    static IsValidAddress(text: string): boolean;
    static fromBytes(bytes: Uint8Array): Address;
    /** @deprecated Use `fromBytes` instead. This alias will be removed in v1.0. */
    static FromBytes(bytes: Uint8Array): Address;
    static fromKey(key: KeyPair): Address;
    static fromKey(key: IKeyPair): Address;
    /** @deprecated Use `fromKey` instead. This alias will be removed in v1.0. */
    static FromKey(key: IKeyPair): Address;
    static fromHash(str: string): Address;
    static fromHash(input: Uint8Array): Address;
    /** @deprecated Use `fromHash` instead. This alias will be removed in v1.0. */
    static FromHash(str: string): Address;
    static FromHash(input: Uint8Array): Address;
    static fromWif(wif: string): Address;
    /** @deprecated Use `fromWif` instead. This alias will be removed in v1.0. */
    static FromWif(wif: string): Address;
    compareTo(other: Address): number;
    equals(other: unknown): boolean;
    toString(): string;
    getPublicKey(): Uint8Array;
    /** @deprecated Use `getPublicKey` instead. This alias will be removed in v1.0. */
    GetPublicKey(): Uint8Array;
    toByteArray(): Uint8Array;
    /** @deprecated Use `toByteArray` instead. This alias will be removed in v1.0. */
    ToByteArray(): Uint8Array;
    serializeData(writer: PBinaryWriter): void;
    /** @deprecated Use `serializeData` instead. This alias will be removed in v1.0. */
    SerializeData(writer: PBinaryWriter): void;
    unserializeData(reader: PBinaryReader): void;
    /** @deprecated Use `unserializeData` instead. This alias will be removed in v1.0. */
    UnserializeData(reader: PBinaryReader): void;
}
```

## phantasma-sdk-ts/types/carbon/blockchain/carbon-token-flags

Source: `dist/types/types/carbon/blockchain/carbon-token-flags.d.ts`

### Declarations

```ts
export declare enum CarbonTokenFlags {
    None = 0,
    BigFungible = 1,
    NonFungible = 2
}
```

## phantasma-sdk-ts/types/carbon/blockchain/extensions

Source: `dist/types/types/carbon/blockchain/extensions/index.d.ts`

### Declarations

```ts
export * from './tx-msg-signer.js';
```

## phantasma-sdk-ts/types/carbon/blockchain/extensions/tx-msg-signer

Source: `dist/types/types/carbon/blockchain/extensions/tx-msg-signer.d.ts`

### Declarations

```ts
export declare class TxMsgSigner {
    static sign(msg: TxMsg, key: PhantasmaKeys): SignedTxMsg;
    static signAndSerialize(msg: TxMsg, key: PhantasmaKeys): Uint8Array;
}
```

## phantasma-sdk-ts/types/carbon/blockchain

Source: `dist/types/types/carbon/blockchain/index.d.ts`

### Declarations

```ts
export * from './extensions/index.js';
```

```ts
export * from './modules/index.js';
```

```ts
export * from './tx-helpers/index.js';
```

```ts
export * from './vm/index.js';
```

```ts
export * from './carbon-token-flags.js';
```

```ts
export * from './module-id.js';
```

```ts
export * from './signed-tx-msg.js';
```

```ts
export * from './tx-msg.js';
```

```ts
export * from './tx-msg-call.js';
```

```ts
export * from './tx-msg-call-multi.js';
```

```ts
export * from './tx-msg-special-resolution.js';
```

```ts
export * from './tx-msg-trade.js';
```

```ts
export * from './tx-msg-mint-fungible.js';
```

```ts
export * from './tx-msg-mint-non-fungible.js';
```

```ts
export * from './tx-msg-burn-fungible.js';
```

```ts
export * from './tx-msg-burn-fungible-gas-payer.js';
```

```ts
export * from './tx-msg-burn-non-fungible.js';
```

```ts
export * from './tx-msg-burn-non-fungible-gas-payer.js';
```

```ts
export * from './tx-msg-transfer-fungible.js';
```

```ts
export * from './tx-msg-transfer-fungible-gas-payer.js';
```

```ts
export * from './tx-msg-transfer-non-fungible-single.js';
```

```ts
export * from './tx-msg-transfer-non-fungible-single-gas-payer.js';
```

```ts
export * from './tx-msg-transfer-non-fungible-multi.js';
```

```ts
export * from './tx-msg-transfer-non-fungible-multi-gas-payer.js';
```

```ts
export * from './tx-msg-phantasma.js';
```

```ts
export * from './tx-msg-phantasma-raw.js';
```

## phantasma-sdk-ts/types/carbon/blockchain/module-id

Source: `dist/types/types/carbon/blockchain/module-id.d.ts`

### Declarations

```ts
export declare enum ModuleId {
    Governance = 0,
    Token = 1,
    PhantasmaVm = 2,
    Organization = 3
}
```

## phantasma-sdk-ts/types/carbon/blockchain/modules/builders/id-helper

Source: `dist/types/types/carbon/blockchain/modules/builders/id-helper.d.ts`

### Declarations

```ts
export declare function getRandomPhantasmaId(): Promise<bigint>;
```

## phantasma-sdk-ts/types/carbon/blockchain/modules/builders

Source: `dist/types/types/carbon/blockchain/modules/builders/index.d.ts`

### Declarations

```ts
export * from './id-helper.js';
```

```ts
export * from './nft-rom-builder.js';
```

```ts
export * from './phantasma-nft-rom-builder.js';
```

```ts
export * from './series-info-builder.js';
```

```ts
export * from './token-info-builder.js';
```

```ts
export * from './token-metadata-builder.js';
```

```ts
export * from './token-schemas-builder.js';
```

```ts
export * from './token-series-metadata-builder.js';
```

```ts
export * from './metadata-helper.js';
```

## phantasma-sdk-ts/types/carbon/blockchain/modules/builders/metadata-helper

Source: `dist/types/types/carbon/blockchain/modules/builders/metadata-helper.d.ts`

### Declarations

```ts
export declare class MetadataField {
    name: string;
    value: MetadataValueInput;
}
```

```ts
export declare class FieldType {
    name: string;
    type: VmType;
}
```

```ts
export declare const seriesDefaultMetadataFields: readonly FieldType[];
```

```ts
export declare const nftDefaultMetadataFields: readonly FieldType[];
```

```ts
export declare const standardMetadataFields: readonly FieldType[];
```

```ts
export declare function findMetadataField(fields: MetadataField[], name: string): MetadataField | undefined;
```

```ts
export declare function pushMetadataField(fieldSchema: VmNamedVariableSchema, metadata: VmDynamicStruct, metadataFields: MetadataField[]): void;
```

```ts
export type MetadataValueInput = MetadataPlainValue | MetadataStructInput | MetadataValueArray;
```

```ts
export {};
```

## phantasma-sdk-ts/types/carbon/blockchain/modules/builders/nft-rom-builder

Source: `dist/types/types/carbon/blockchain/modules/builders/nft-rom-builder.d.ts`

### Declarations

```ts
export declare class NftRomBuilder {
    static buildAndSerialize(nftRomSchema: VmStructSchema, phantasmaNftId: bigint, metadata: MetadataField[]): Uint8Array;
}
```

## phantasma-sdk-ts/types/carbon/blockchain/modules/builders/phantasma-nft-rom-builder

Source: `dist/types/types/carbon/blockchain/modules/builders/phantasma-nft-rom-builder.d.ts`

### Declarations

```ts
export declare class PhantasmaNftRomBuilder {
    private static readonly reservedFieldNames;
    static buildPublicMintSchema(nftRomSchema: VmStructSchema): VmStructSchema;
    static buildAndSerialize(nftRomSchema: VmStructSchema, metadata: MetadataField[]): Uint8Array;
}
```

## phantasma-sdk-ts/types/carbon/blockchain/modules/builders/series-info-builder

Source: `dist/types/types/carbon/blockchain/modules/builders/series-info-builder.d.ts`

### Declarations

```ts
export declare class SeriesInfoBuilder {
    static build(seriesSchema: VmStructSchema, phantasmaSeriesId: bigint, maxMint: number, maxSupply: number, ownerPublicKey: Bytes32, metadata: MetadataField[]): SeriesInfo;
}
```

## phantasma-sdk-ts/types/carbon/blockchain/modules/builders/token-info-builder

Source: `dist/types/types/carbon/blockchain/modules/builders/token-info-builder.d.ts`

### Declarations

```ts
export declare class TokenInfoBuilder {
    static build(symbol: string, maxSupply: IntX, isNFT: boolean, decimals: number, creatorPublicKey: Bytes32, metadata?: Uint8Array | null | undefined, tokenSchemas?: TokenSchemas | null | undefined): TokenInfo;
    static maxSymbolLength: number;
    /**
     * Mirrors carbon::CheckIsValidSymbol from contracts/token.cpp.
     * Returns true when valid, or false when the symbol must be rejected.
     */
    static checkIsValidSymbol(symbol: string): {
        ok: boolean;
        error: string | null;
    };
}
```

## phantasma-sdk-ts/types/carbon/blockchain/modules/builders/token-metadata-builder

Source: `dist/types/types/carbon/blockchain/modules/builders/token-metadata-builder.d.ts`

### Declarations

```ts
export declare class TokenMetadataBuilder {
    private static readonly iconDataUriPrefixPattern;
    private static readonly base64PayloadPattern;
    static buildAndSerialize(fields?: Record<string, unknown>): Uint8Array;
    private static validateIcon;
}
```

## phantasma-sdk-ts/types/carbon/blockchain/modules/builders/token-schemas-builder

Source: `dist/types/types/carbon/blockchain/modules/builders/token-schemas-builder.d.ts`

### Declarations

```ts
export declare class TokenSchemasJson {
    seriesMetadata: FieldType[];
    rom: FieldType[];
    ram: FieldType[];
}
```

```ts
export declare function parseTokenSchemasJson(json: string): TokenSchemasJson;
```

```ts
export declare class TokenSchemasBuilder {
    private static assertMetadataField;
    private static defaultSeriesSchema;
    private static defaultNftRomSchema;
    private static seriesSchemaFromFieldTypes;
    private static nftRomSchemaFromFieldTypes;
    private static nftRamSchemaFromFieldTypes;
    static prepareStandard(sharedMetadata: boolean): TokenSchemas;
    static fromJson(json: string): TokenSchemas;
    static verify(schemas: TokenSchemas): Readonly<{
        ok: boolean;
        error: string | null;
    }>;
    static serialize(tokenSchemas: TokenSchemas): Readonly<Uint8Array>;
    static serializeHex(tokenSchemas: TokenSchemas): Readonly<string>;
    static logSchema(schema: VmStructSchema): void;
}
```

## phantasma-sdk-ts/types/carbon/blockchain/modules/builders/token-series-metadata-builder

Source: `dist/types/types/carbon/blockchain/modules/builders/token-series-metadata-builder.d.ts`

### Declarations

```ts
export declare class TokenSeriesMetadataBuilder {
    static buildAndSerialize(seriesMetadataSchema: VmStructSchema, newPhantasmaSeriesId: bigint, metadata: MetadataField[]): Uint8Array;
}
```

## phantasma-sdk-ts/types/carbon/blockchain/modules

Source: `dist/types/types/carbon/blockchain/modules/index.d.ts`

### Declarations

```ts
export * from './builders/index.js';
```

```ts
export * from './mint-phantasma-non-fungible-args.js';
```

```ts
export * from './phantasma-nft-mint-info.js';
```

```ts
export * from './phantasma-nft-mint-result.js';
```

```ts
export * from './series-info.js';
```

```ts
export * from './standard-meta.js';
```

```ts
export * from './token-contract-methods.js';
```

```ts
export * from './token-helper.js';
```

```ts
export * from './token-info.js';
```

```ts
export * from './token-listing.js';
```

```ts
export * from './token-schemas.js';
```

## phantasma-sdk-ts/types/carbon/blockchain/modules/mint-phantasma-non-fungible-args

Source: `dist/types/types/carbon/blockchain/modules/mint-phantasma-non-fungible-args.d.ts`

### Declarations

```ts
export declare class MintPhantasmaNonFungibleArgs implements CarbonBlobLike {
    tokenId: bigint;
    address: Bytes32;
    tokens: PhantasmaNftMintInfo[];
    constructor(init?: Partial<MintPhantasmaNonFungibleArgs>);
    write(w: CarbonBinaryWriter): void;
    read(r: CarbonBinaryReader): void;
    static read(r: CarbonBinaryReader): MintPhantasmaNonFungibleArgs;
}
```

## phantasma-sdk-ts/types/carbon/blockchain/modules/phantasma-nft-mint-info

Source: `dist/types/types/carbon/blockchain/modules/phantasma-nft-mint-info.d.ts`

### Declarations

```ts
export declare class PhantasmaNftMintInfo implements CarbonBlobLike {
    phantasmaSeriesId: IntX;
    rom: Uint8Array;
    ram: Uint8Array;
    constructor(init?: Partial<PhantasmaNftMintInfo>);
    write(w: CarbonBinaryWriter): void;
    read(r: CarbonBinaryReader): void;
    static read(r: CarbonBinaryReader): PhantasmaNftMintInfo;
}
```

## phantasma-sdk-ts/types/carbon/blockchain/modules/phantasma-nft-mint-result

Source: `dist/types/types/carbon/blockchain/modules/phantasma-nft-mint-result.d.ts`

### Declarations

```ts
export declare class PhantasmaNftMintResult implements CarbonBlobLike {
    phantasmaNftId: Bytes32;
    carbonInstanceId: bigint;
    constructor(init?: Partial<PhantasmaNftMintResult>);
    write(w: CarbonBinaryWriter): void;
    read(r: CarbonBinaryReader): void;
    static read(r: CarbonBinaryReader): PhantasmaNftMintResult;
}
```

## phantasma-sdk-ts/types/carbon/blockchain/modules/series-info

Source: `dist/types/types/carbon/blockchain/modules/series-info.d.ts`

### Declarations

```ts
export declare class SeriesInfo implements CarbonBlobLike {
    maxMint: number;
    maxSupply: number;
    owner: Bytes32;
    metadata: Uint8Array;
    rom: VmStructSchema;
    ram: VmStructSchema;
    constructor(init?: Partial<SeriesInfo>);
    write(w: CarbonBinaryWriter): void;
    read(r: CarbonBinaryReader): void;
    static read(r: CarbonBinaryReader): SeriesInfo;
}
```

## phantasma-sdk-ts/types/carbon/blockchain/modules/standard-meta

Source: `dist/types/types/carbon/blockchain/modules/standard-meta.d.ts`

### Declarations

```ts
export declare const StandardMeta: {
    readonly id: SmallString;
    readonly Chain: {
        readonly address: SmallString;
        readonly name: SmallString;
        readonly nexus: SmallString;
        readonly tokenomics: SmallString;
    };
    readonly Token: {
        readonly staking_org_id: SmallString;
        readonly staking_org_threshold: SmallString;
        readonly staking_reward_token: SmallString;
        readonly staking_reward_period: SmallString;
        readonly staking_reward_mul: SmallString;
        readonly staking_reward_div: SmallString;
        readonly staking_lock: SmallString;
        readonly staking_booster_token: SmallString;
        readonly staking_booster_mul: SmallString;
        readonly staking_booster_div: SmallString;
        readonly staking_booster_limit: SmallString;
        readonly phantasma_script: SmallString;
        readonly phantasma_abi: SmallString;
        readonly pre_burn: SmallString;
    };
};
```

## phantasma-sdk-ts/types/carbon/blockchain/modules/token-contract-methods

Source: `dist/types/types/carbon/blockchain/modules/token-contract-methods.d.ts`

### Declarations

```ts
export declare enum TokenContractMethods {
    TransferFungible = 0,
    TransferNonFungible = 1,
    CreateToken = 2,
    MintFungible = 3,
    BurnFungible = 4,
    GetBalance = 5,
    CreateTokenSeries = 6,
    DeleteTokenSeries = 7,
    MintNonFungible = 8,
    BurnNonFungible = 9,
    GetInstances = 10,
    GetNonFungibleInfo = 11,
    GetNonFungibleInfoByRomId = 12,
    GetSeriesInfo = 13,
    GetSeriesInfoByMetaId = 14,
    GetTokenInfo = 15,
    GetTokenInfoBySymbol = 16,
    GetTokenSupply = 17,
    GetSeriesSupply = 18,
    GetTokenIdBySymbol = 19,
    GetBalances = 20,
    CreateMintedTokenSeries = 21,
    ApplyInflation = 22,
    UpdateTokenMetadata = 23,
    GetNextTokenInflation = 24,
    SetTokensConfig = 25,
    UpdateSeriesMetadata = 26,
    MintPhantasmaNonFungible = 27
}
```

```ts
export { TokenContractMethods as TokenContract_Methods };
```

## phantasma-sdk-ts/types/carbon/blockchain/modules/token-helper

Source: `dist/types/types/carbon/blockchain/modules/token-helper.d.ts`

### Declarations

```ts
export type CarbonNftAddressInfo = {
    carbonTokenId: bigint;
    instanceId: bigint;
    seriesId: number;
    mintNumber: number;
};
```

```ts
export declare class TokenHelper {
    static getNftAddress(carbonTokenId: bigint, instanceId: bigint): Bytes32;
    private static readUint64LE;
    /**
     * Unpacks a Carbon NFT address (32 bytes) into its logical parts:
     * - carbonTokenId: identifies the NFT token contract
     * - instanceId: 64-bit composite id (series + mint)
     * - seriesId / mintNumber: 32-bit halves of instanceId
     */
    static unpackNftAddress(address: Uint8Array): CarbonNftAddressInfo;
}
```

## phantasma-sdk-ts/types/carbon/blockchain/modules/token-info

Source: `dist/types/types/carbon/blockchain/modules/token-info.d.ts`

### Declarations

```ts
export declare class TokenInfo implements CarbonBlobLike {
    maxSupply: IntX;
    flags: CarbonTokenFlags;
    decimals: number;
    owner: Bytes32;
    symbol: SmallString;
    metadata: Uint8Array;
    tokenSchemas?: Uint8Array;
    constructor(init?: Partial<TokenInfo>);
    write(w: CarbonBinaryWriter): void;
    read(r: CarbonBinaryReader): void;
    static read(r: CarbonBinaryReader): TokenInfo;
}
```

## phantasma-sdk-ts/types/carbon/blockchain/modules/token-listing

Source: `dist/types/types/carbon/blockchain/modules/token-listing.d.ts`

### Declarations

```ts
export declare enum ListingType {
    FixedPrice = 0
}
```

```ts
export declare class TokenListing implements CarbonBlobLike {
    type: ListingType;
    seller: Bytes32;
    quoteTokenId: bigint;
    price: IntX;
    startDate: bigint;
    endDate: bigint;
    constructor(type?: ListingType, seller?: Bytes32, quoteTokenId?: bigint, price?: IntX, startDate?: bigint, endDate?: bigint);
    write(w: CarbonBinaryWriter): void;
    read(r: CarbonBinaryReader): void;
    static read(r: CarbonBinaryReader): TokenListing;
}
```

## phantasma-sdk-ts/types/carbon/blockchain/modules/token-schemas

Source: `dist/types/types/carbon/blockchain/modules/token-schemas.d.ts`

### Declarations

```ts
export declare class TokenSchemas implements CarbonBlobLike {
    seriesMetadata: VmStructSchema;
    rom: VmStructSchema;
    ram: VmStructSchema;
    constructor(init?: Partial<TokenSchemas>);
    write(w: CarbonBinaryWriter): void;
    read(r: CarbonBinaryReader): void;
    static read(r: CarbonBinaryReader): TokenSchemas;
}
```

## phantasma-sdk-ts/types/carbon/blockchain/signed-tx-msg

Source: `dist/types/types/carbon/blockchain/signed-tx-msg.d.ts`

### Declarations

```ts
export declare class SignedTxMsg implements CarbonBlobLike {
    msg: TxMsg;
    witnesses: Witness[];
    constructor(msg?: TxMsg, witnesses?: Witness[]);
    write(w: CarbonBinaryWriter): void;
    read(r: CarbonBinaryReader): void;
    static read(r: CarbonBinaryReader): SignedTxMsg;
}
```

## phantasma-sdk-ts/types/carbon/blockchain/tx-helpers/create-token-series-tx-helper

Source: `dist/types/types/carbon/blockchain/tx-helpers/create-token-series-tx-helper.d.ts`

### Declarations

```ts
export declare class CreateTokenSeriesTxHelper {
    /** Build a Tx without signing. */
    static buildTx(tokenId: bigint, // ulong
    seriesInfo: SeriesInfo, creatorPublicKey: Bytes32, feeOptions?: CreateSeriesFeeOptions, maxData?: bigint, expiry?: bigint): TxMsg;
    /** Build and sign, returning raw bytes. */
    static buildTxAndSign(tokenId: bigint, seriesInfo: SeriesInfo, signer: PhantasmaKeys, feeOptions?: CreateSeriesFeeOptions, maxData?: bigint, expiry?: bigint): Uint8Array;
    /** Build, sign and return hex string. */
    static buildTxAndSignHex(tokenId: bigint, seriesInfo: SeriesInfo, signer: PhantasmaKeys, feeOptions?: CreateSeriesFeeOptions, maxData?: bigint, expiry?: bigint): string;
    static parseResult(resultHex: string): number;
}
```

## phantasma-sdk-ts/types/carbon/blockchain/tx-helpers/create-token-tx-helper

Source: `dist/types/types/carbon/blockchain/tx-helpers/create-token-tx-helper.d.ts`

### Declarations

```ts
export declare class CreateTokenTxHelper {
    static buildTx(tokenInfo: TokenInfo, creatorPublicKey: Bytes32, feeOptions?: CreateTokenFeeOptions, maxData?: bigint, expiry?: bigint): TxMsg;
    static buildTxAndSign(tokenInfo: TokenInfo, signer: PhantasmaKeys, feeOptions?: CreateTokenFeeOptions, maxData?: bigint, expiry?: bigint): Uint8Array;
    static buildTxAndSignHex(tokenInfo: TokenInfo, signer: PhantasmaKeys, feeOptions?: CreateTokenFeeOptions, maxData?: bigint, expiry?: bigint): string;
    static parseResult(resultHex: string): number;
}
```

## phantasma-sdk-ts/types/carbon/blockchain/tx-helpers/fee-options

Source: `dist/types/types/carbon/blockchain/tx-helpers/fee-options.d.ts`

### Declarations

```ts
export interface FeeOptionsLike {
    feeMultiplier: bigint;
    calculateMaxGas(...args: unknown[]): bigint;
}
```

```ts
export type IFeeOptions = FeeOptionsLike;
```

```ts
export declare class FeeOptions implements FeeOptionsLike {
    gasFeeBase: bigint;
    feeMultiplier: bigint;
    constructor(gasFeeBase?: bigint, feeMultiplier?: bigint);
    calculateMaxGas(): bigint;
    calculateMaxGas(count: CountInput): bigint;
}
```

```ts
export declare class CreateTokenFeeOptions extends FeeOptions implements FeeOptionsLike {
    gasFeeCreateTokenBase: bigint;
    gasFeeCreateTokenSymbol: bigint;
    constructor(gasFeeBase?: bigint, gasFeeCreateTokenBase?: bigint, gasFeeCreateTokenSymbol?: bigint, feeMultiplier?: bigint);
    calculateMaxGas(): bigint;
    calculateMaxGas(symbol: SymbolInput): bigint;
}
```

```ts
export declare class CreateSeriesFeeOptions extends FeeOptions implements FeeOptionsLike {
    gasFeeCreateSeriesBase: bigint;
    constructor(gasFeeBase?: bigint, gasFeeCreateSeriesBase?: bigint, feeMultiplier?: bigint);
    calculateMaxGas(): bigint;
}
```

```ts
export declare class MintNftFeeOptions extends FeeOptions implements FeeOptionsLike {
    constructor(gasFeeBase?: bigint, feeMultiplier?: bigint);
    calculateMaxGas(): bigint;
    calculateMaxGas(count: CountInput): bigint;
    calculateMaxGas(tokens: readonly unknown[]): bigint;
}
```

```ts
export {};
```

## phantasma-sdk-ts/types/carbon/blockchain/tx-helpers

Source: `dist/types/types/carbon/blockchain/tx-helpers/index.d.ts`

### Declarations

```ts
export * from './create-token-series-tx-helper.js';
```

```ts
export * from './create-token-tx-helper.js';
```

```ts
export * from './fee-options.js';
```

```ts
export * from './mint-phantasma-non-fungible-tx-helper.js';
```

```ts
export * from './mint-non-fungible-tx-helper.js';
```

## phantasma-sdk-ts/types/carbon/blockchain/tx-helpers/mint-non-fungible-tx-helper

Source: `dist/types/types/carbon/blockchain/tx-helpers/mint-non-fungible-tx-helper.d.ts`

### Declarations

```ts
export declare class MintNonFungibleTxHelper {
    static buildTx(carbonTokenId: bigint, carbonSeriesId: number, senderPublicKey: Bytes32, receiverPublicKey: Bytes32, rom: Uint8Array, ram: Uint8Array, feeOptions?: MintNftFeeOptions, maxData?: bigint, expiry?: bigint): TxMsg;
    static buildTxAndSign(tokenId: bigint, seriesId: number, signer: PhantasmaKeys, receiverPublicKey: Bytes32, rom: Uint8Array, ram: Uint8Array, feeOptions?: MintNftFeeOptions, maxData?: bigint, expiry?: bigint): Uint8Array;
    static buildTxAndSignHex(tokenId: bigint, seriesId: number, signer: PhantasmaKeys, receiverPublicKey: Bytes32, rom: Uint8Array, ram: Uint8Array | null | undefined, feeOptions?: MintNftFeeOptions, maxData?: bigint, expiry?: bigint): string;
    static parseResult(carbonTokenId: bigint, resultHex: string): Bytes32[];
}
```

## phantasma-sdk-ts/types/carbon/blockchain/tx-helpers/mint-phantasma-non-fungible-tx-helper

Source: `dist/types/types/carbon/blockchain/tx-helpers/mint-phantasma-non-fungible-tx-helper.d.ts`

### Declarations

```ts
export declare class MintPhantasmaNonFungibleTxHelper {
    static buildTx(tokenId: bigint, phantasmaSeriesId: bigint, senderPublicKey: Bytes32, receiverPublicKey: Bytes32, publicRom: Uint8Array, ram?: Uint8Array, feeOptions?: MintNftFeeOptions, maxData?: bigint, expiry?: bigint): TxMsg;
    static buildTx(tokenId: bigint, senderPublicKey: Bytes32, receiverPublicKey: Bytes32, tokens: PhantasmaNftMintInfo[], feeOptions?: MintNftFeeOptions, maxData?: bigint, expiry?: bigint): TxMsg;
    private static buildTxCore;
    static buildTxAndSign(tokenId: bigint, phantasmaSeriesId: bigint, signer: PhantasmaKeys, receiverPublicKey: Bytes32, publicRom: Uint8Array, ram?: Uint8Array, feeOptions?: MintNftFeeOptions, maxData?: bigint, expiry?: bigint): Uint8Array;
    static buildTxAndSign(tokenId: bigint, tokens: PhantasmaNftMintInfo[], signer: PhantasmaKeys, receiverPublicKey: Bytes32, feeOptions?: MintNftFeeOptions, maxData?: bigint, expiry?: bigint): Uint8Array;
    static buildTxAndSignHex(tokenId: bigint, phantasmaSeriesId: bigint, signer: PhantasmaKeys, receiverPublicKey: Bytes32, publicRom: Uint8Array, ram?: Uint8Array, feeOptions?: MintNftFeeOptions, maxData?: bigint, expiry?: bigint): string;
    static buildTxAndSignHex(tokenId: bigint, tokens: PhantasmaNftMintInfo[], signer: PhantasmaKeys, receiverPublicKey: Bytes32, feeOptions?: MintNftFeeOptions, maxData?: bigint, expiry?: bigint): string;
    static parseResult(resultHex: string): PhantasmaNftMintResult[];
}
```

## phantasma-sdk-ts/types/carbon/blockchain/tx-msg-burn-fungible-gas-payer

Source: `dist/types/types/carbon/blockchain/tx-msg-burn-fungible-gas-payer.d.ts`

### Declarations

```ts
export declare class TxMsgBurnFungibleGasPayer implements CarbonBlobLike {
    tokenId: bigint;
    from: Bytes32;
    amount: IntX;
    constructor(init?: Partial<TxMsgBurnFungibleGasPayer>);
    write(w: CarbonBinaryWriter): void;
    read(r: CarbonBinaryReader): void;
    static read(r: CarbonBinaryReader): TxMsgBurnFungibleGasPayer;
}
```

## phantasma-sdk-ts/types/carbon/blockchain/tx-msg-burn-fungible

Source: `dist/types/types/carbon/blockchain/tx-msg-burn-fungible.d.ts`

### Declarations

```ts
export declare class TxMsgBurnFungible implements CarbonBlobLike {
    tokenId: bigint;
    amount: IntX;
    constructor(init?: Partial<TxMsgBurnFungible>);
    write(w: CarbonBinaryWriter): void;
    read(r: CarbonBinaryReader): void;
    static read(r: CarbonBinaryReader): TxMsgBurnFungible;
}
```

## phantasma-sdk-ts/types/carbon/blockchain/tx-msg-burn-non-fungible-gas-payer

Source: `dist/types/types/carbon/blockchain/tx-msg-burn-non-fungible-gas-payer.d.ts`

### Declarations

```ts
export declare class TxMsgBurnNonFungibleGasPayer implements CarbonBlobLike {
    tokenId: bigint;
    from: Bytes32;
    instanceId: bigint;
    constructor(init?: Partial<TxMsgBurnNonFungibleGasPayer>);
    write(w: CarbonBinaryWriter): void;
    read(r: CarbonBinaryReader): void;
    static read(r: CarbonBinaryReader): TxMsgBurnNonFungibleGasPayer;
}
```

## phantasma-sdk-ts/types/carbon/blockchain/tx-msg-burn-non-fungible

Source: `dist/types/types/carbon/blockchain/tx-msg-burn-non-fungible.d.ts`

### Declarations

```ts
export declare class TxMsgBurnNonFungible implements CarbonBlobLike {
    tokenId: bigint;
    instanceId: bigint;
    constructor(init?: Partial<TxMsgBurnNonFungible>);
    write(w: CarbonBinaryWriter): void;
    read(r: CarbonBinaryReader): void;
    static read(r: CarbonBinaryReader): TxMsgBurnNonFungible;
}
```

## phantasma-sdk-ts/types/carbon/blockchain/tx-msg-call-multi

Source: `dist/types/types/carbon/blockchain/tx-msg-call-multi.d.ts`

### Declarations

```ts
export declare class TxMsgCallMulti implements CarbonBlobLike {
    calls: TxMsgCall[];
    constructor(calls?: TxMsgCall[]);
    write(w: CarbonBinaryWriter): void;
    read(r: CarbonBinaryReader): void;
    static read(r: CarbonBinaryReader): TxMsgCallMulti;
}
```

## phantasma-sdk-ts/types/carbon/blockchain/tx-msg-call

Source: `dist/types/types/carbon/blockchain/tx-msg-call.d.ts`

### Declarations

```ts
export type MsgCallArgs = {
    registerOffset: number;
    args: Uint8Array;
};
```

```ts
export declare class MsgCallArgSections {
    argSections: MsgCallArgs[];
    constructor(argSections?: MsgCallArgs[]);
    hasSections(): boolean;
    write(w: CarbonBinaryWriter): void;
    static readWithCount(r: CarbonBinaryReader, countNegative: number): MsgCallArgSections;
}
```

```ts
export declare class TxMsgCall implements CarbonBlobLike {
    moduleId: number;
    methodId: number;
    args: Uint8Array;
    sections: MsgCallArgSections | null;
    constructor(moduleId?: number, methodId?: number, args?: Uint8Array);
    write(w: CarbonBinaryWriter): void;
    read(r: CarbonBinaryReader): void;
    static read(r: CarbonBinaryReader): TxMsgCall;
}
```

## phantasma-sdk-ts/types/carbon/blockchain/tx-msg-mint-fungible

Source: `dist/types/types/carbon/blockchain/tx-msg-mint-fungible.d.ts`

### Declarations

```ts
export declare class TxMsgMintFungible implements CarbonBlobLike {
    tokenId: bigint;
    to: Bytes32;
    amount: IntX;
    constructor(init?: Partial<TxMsgMintFungible>);
    write(w: CarbonBinaryWriter): void;
    read(r: CarbonBinaryReader): void;
    static read(r: CarbonBinaryReader): TxMsgMintFungible;
}
```

## phantasma-sdk-ts/types/carbon/blockchain/tx-msg-mint-non-fungible

Source: `dist/types/types/carbon/blockchain/tx-msg-mint-non-fungible.d.ts`

### Declarations

```ts
export declare class TxMsgMintNonFungible implements CarbonBlobLike {
    tokenId: bigint;
    to: Bytes32;
    seriesId: number;
    rom: Uint8Array;
    ram: Uint8Array;
    constructor(init?: Partial<TxMsgMintNonFungible>);
    write(w: CarbonBinaryWriter): void;
    read(r: CarbonBinaryReader): void;
    static read(r: CarbonBinaryReader): TxMsgMintNonFungible;
}
```

## phantasma-sdk-ts/types/carbon/blockchain/tx-msg-phantasma-raw

Source: `dist/types/types/carbon/blockchain/tx-msg-phantasma-raw.d.ts`

### Declarations

```ts
export declare class TxMsgPhantasmaRaw implements CarbonBlobLike {
    transaction: Uint8Array;
    constructor(transaction?: Uint8Array);
    write(w: CarbonBinaryWriter): void;
    read(r: CarbonBinaryReader): void;
    static read(r: CarbonBinaryReader): TxMsgPhantasmaRaw;
}
```

## phantasma-sdk-ts/types/carbon/blockchain/tx-msg-phantasma

Source: `dist/types/types/carbon/blockchain/tx-msg-phantasma.d.ts`

### Declarations

```ts
export declare class TxMsgPhantasma implements CarbonBlobLike {
    nexus: SmallString;
    chain: SmallString;
    script: Uint8Array;
    constructor(init?: Partial<TxMsgPhantasma>);
    write(w: CarbonBinaryWriter): void;
    read(r: CarbonBinaryReader): void;
    static read(r: CarbonBinaryReader): TxMsgPhantasma;
}
```

## phantasma-sdk-ts/types/carbon/blockchain/tx-msg-special-resolution

Source: `dist/types/types/carbon/blockchain/tx-msg-special-resolution.d.ts`

### Declarations

```ts
export declare class TxMsgSpecialResolution implements CarbonBlobLike {
    resolutionId: bigint;
    calls: TxMsgCall[];
    constructor(resolutionId?: bigint, calls?: TxMsgCall[]);
    write(w: CarbonBinaryWriter): void;
    read(r: CarbonBinaryReader): void;
    static read(r: CarbonBinaryReader): TxMsgSpecialResolution;
}
```

## phantasma-sdk-ts/types/carbon/blockchain/tx-msg-trade

Source: `dist/types/types/carbon/blockchain/tx-msg-trade.d.ts`

### Declarations

```ts
export declare class TxMsgTrade implements CarbonBlobLike {
    transferF: TxMsgTransferFungibleGasPayer[];
    transferN: TxMsgTransferNonFungibleSingleGasPayer[];
    mintF: TxMsgMintFungible[];
    burnF: TxMsgBurnFungibleGasPayer[];
    mintN: TxMsgMintNonFungible[];
    burnN: TxMsgBurnNonFungibleGasPayer[];
    constructor(init?: Partial<TxMsgTrade>);
    write(w: CarbonBinaryWriter): void;
    read(r: CarbonBinaryReader): void;
    static read(r: CarbonBinaryReader): TxMsgTrade;
}
```

## phantasma-sdk-ts/types/carbon/blockchain/tx-msg-transfer-fungible-gas-payer

Source: `dist/types/types/carbon/blockchain/tx-msg-transfer-fungible-gas-payer.d.ts`

### Declarations

```ts
export declare class TxMsgTransferFungibleGasPayer implements CarbonBlobLike {
    to: Bytes32;
    from: Bytes32;
    tokenId: bigint;
    amount: bigint;
    constructor(init?: Partial<TxMsgTransferFungibleGasPayer>);
    write(w: CarbonBinaryWriter): void;
    read(r: CarbonBinaryReader): void;
    static read(r: CarbonBinaryReader): TxMsgTransferFungibleGasPayer;
}
```

## phantasma-sdk-ts/types/carbon/blockchain/tx-msg-transfer-fungible

Source: `dist/types/types/carbon/blockchain/tx-msg-transfer-fungible.d.ts`

### Declarations

```ts
export declare class TxMsgTransferFungible implements CarbonBlobLike {
    to: Bytes32;
    tokenId: bigint;
    amount: bigint;
    constructor(to?: Bytes32, tokenId?: bigint, amount?: bigint);
    write(w: CarbonBinaryWriter): void;
    read(r: CarbonBinaryReader): void;
    static read(r: CarbonBinaryReader): TxMsgTransferFungible;
}
```

## phantasma-sdk-ts/types/carbon/blockchain/tx-msg-transfer-non-fungible-multi-gas-payer

Source: `dist/types/types/carbon/blockchain/tx-msg-transfer-non-fungible-multi-gas-payer.d.ts`

### Declarations

```ts
export declare class TxMsgTransferNonFungibleMultiGasPayer implements CarbonBlobLike {
    to: Bytes32;
    from: Bytes32;
    tokenId: bigint;
    instanceIds: bigint[];
    constructor(init?: Partial<TxMsgTransferNonFungibleMultiGasPayer>);
    write(w: CarbonBinaryWriter): void;
    read(r: CarbonBinaryReader): void;
    static read(r: CarbonBinaryReader): TxMsgTransferNonFungibleMultiGasPayer;
}
```

## phantasma-sdk-ts/types/carbon/blockchain/tx-msg-transfer-non-fungible-multi

Source: `dist/types/types/carbon/blockchain/tx-msg-transfer-non-fungible-multi.d.ts`

### Declarations

```ts
export declare class TxMsgTransferNonFungibleMulti implements CarbonBlobLike {
    to: Bytes32;
    tokenId: bigint;
    instanceIds: bigint[];
    constructor(init?: Partial<TxMsgTransferNonFungibleMulti>);
    write(w: CarbonBinaryWriter): void;
    read(r: CarbonBinaryReader): void;
    static read(r: CarbonBinaryReader): TxMsgTransferNonFungibleMulti;
}
```

## phantasma-sdk-ts/types/carbon/blockchain/tx-msg-transfer-non-fungible-single-gas-payer

Source: `dist/types/types/carbon/blockchain/tx-msg-transfer-non-fungible-single-gas-payer.d.ts`

### Declarations

```ts
export declare class TxMsgTransferNonFungibleSingleGasPayer implements CarbonBlobLike {
    to: Bytes32;
    from: Bytes32;
    tokenId: bigint;
    instanceId: bigint;
    constructor(init?: Partial<TxMsgTransferNonFungibleSingleGasPayer>);
    write(w: CarbonBinaryWriter): void;
    read(r: CarbonBinaryReader): void;
    static read(r: CarbonBinaryReader): TxMsgTransferNonFungibleSingleGasPayer;
}
```

## phantasma-sdk-ts/types/carbon/blockchain/tx-msg-transfer-non-fungible-single

Source: `dist/types/types/carbon/blockchain/tx-msg-transfer-non-fungible-single.d.ts`

### Declarations

```ts
export declare class TxMsgTransferNonFungibleSingle implements CarbonBlobLike {
    to: Bytes32;
    tokenId: bigint;
    instanceId: bigint;
    constructor(init?: Partial<TxMsgTransferNonFungibleSingle>);
    write(w: CarbonBinaryWriter): void;
    read(r: CarbonBinaryReader): void;
    static read(r: CarbonBinaryReader): TxMsgTransferNonFungibleSingle;
}
```

## phantasma-sdk-ts/types/carbon/blockchain/tx-msg

Source: `dist/types/types/carbon/blockchain/tx-msg.d.ts`

### Declarations

```ts
export declare class TxMsg implements CarbonBlobLike {
    type: TxTypes;
    expiry: bigint;
    maxGas: bigint;
    maxData: bigint;
    gasFrom: Bytes32;
    payload: SmallString;
    msg?: TxMsgPayload | undefined;
    constructor(type?: TxTypes, expiry?: bigint, // int64
    maxGas?: bigint, // uint64
    maxData?: bigint, // uint64
    gasFrom?: Bytes32, payload?: SmallString, msg?: TxMsgPayload | undefined);
    write(w: CarbonBinaryWriter): void;
    read(r: CarbonBinaryReader): void;
    static read(r: CarbonBinaryReader): TxMsg;
}
```

```ts
export {};
```

## phantasma-sdk-ts/types/carbon/blockchain/vm

Source: `dist/types/types/carbon/blockchain/vm/index.d.ts`

### Declarations

```ts
export * from './vm-dynamic-struct.js';
```

```ts
export * from './vm-dynamic-variable.js';
```

```ts
export * from './vm-named-dynamic-variable.js';
```

```ts
export * from './vm-named-variable-schema.js';
```

```ts
export * from './vm-struct-array.js';
```

```ts
export * from './vm-struct-flags.js';
```

```ts
export * from './vm-struct-schema.js';
```

```ts
export * from './vm-type.js';
```

```ts
export * from './vm-variable-schema.js';
```

## phantasma-sdk-ts/types/carbon/blockchain/vm/vm-dynamic-struct

Source: `dist/types/types/carbon/blockchain/vm/vm-dynamic-struct.d.ts`

### Declarations

```ts
export declare class VmDynamicStruct implements CarbonBlobLike {
    fields: VmNamedDynamicVariable[];
    getValue(key: SmallString): VmDynamicVariable | undefined;
    write(w: CarbonBinaryWriter): void;
    read(r: CarbonBinaryReader): void;
    static read(r: CarbonBinaryReader): VmDynamicStruct;
    writeWithSchema(schema: VmStructSchema, w: CarbonBinaryWriter): boolean;
    readWithSchema(schema: VmStructSchema, r: CarbonBinaryReader): void;
}
```

## phantasma-sdk-ts/types/carbon/blockchain/vm/vm-dynamic-variable

Source: `dist/types/types/carbon/blockchain/vm/vm-dynamic-variable.d.ts`

### Declarations

```ts
export type VmDynamicVariableData = null | VmDynamicVariable | Uint8Array | VmDynamicStruct | number | bigint | Bytes16 | Bytes32 | Bytes64 | string | VmDynamicVariable[] | Uint8Array[] | VmStructArray | number[] | bigint[] | Bytes16[] | Bytes32[] | Bytes64[] | string[];
```

```ts
export declare class VmDynamicVariable implements CarbonBlobLike {
    type: VmType;
    data: VmDynamicVariableData;
    static fromType(t: VmType): VmDynamicVariable;
    write(w: CarbonBinaryWriter): void;
    writeWithSchema(schema: VmVariableSchema, w: CarbonBinaryWriter): boolean;
    read(r: CarbonBinaryReader): void;
    readWithSchema(schema: VmVariableSchema, r: CarbonBinaryReader): void;
    static readStatic(type: VmType, outVar: VmDynamicVariable, schema: VmStructSchema | null, r: CarbonBinaryReader): void;
    static writeStatic(type: VmType, v: VmDynamicVariable, schema: VmStructSchema | null, w: CarbonBinaryWriter): boolean;
}
```

## phantasma-sdk-ts/types/carbon/blockchain/vm/vm-named-dynamic-variable

Source: `dist/types/types/carbon/blockchain/vm/vm-named-dynamic-variable.d.ts`

### Declarations

```ts
export declare class VmNamedDynamicVariable implements CarbonBlobLike {
    name: SmallString;
    value: VmDynamicVariable;
    static from(name: string | SmallString, type: VmType, value: VmDynamicVariableData): VmNamedDynamicVariable;
    write(w: CarbonBinaryWriter): void;
    read(r: CarbonBinaryReader): void;
    static read(r: CarbonBinaryReader): VmNamedDynamicVariable;
}
```

## phantasma-sdk-ts/types/carbon/blockchain/vm/vm-named-variable-schema

Source: `dist/types/types/carbon/blockchain/vm/vm-named-variable-schema.d.ts`

### Declarations

```ts
export declare class VmNamedVariableSchema implements CarbonBlobLike {
    name: SmallString;
    schema: VmVariableSchema;
    constructor(name?: SmallString | string, schema?: VmVariableSchema | VmType);
    write(w: CarbonBinaryWriter): void;
    read(r: CarbonBinaryReader): void;
    static read(r: CarbonBinaryReader): VmNamedVariableSchema;
}
```

## phantasma-sdk-ts/types/carbon/blockchain/vm/vm-struct-array

Source: `dist/types/types/carbon/blockchain/vm/vm-struct-array.d.ts`

### Declarations

```ts
export declare class VmStructArray {
    schema: VmStructSchema;
    structs: VmDynamicStruct[];
}
```

## phantasma-sdk-ts/types/carbon/blockchain/vm/vm-struct-flags

Source: `dist/types/types/carbon/blockchain/vm/vm-struct-flags.d.ts`

### Declarations

```ts
export declare enum VmStructFlags {
    None = 0,
    DynamicExtras = 1
}
```

## phantasma-sdk-ts/types/carbon/blockchain/vm/vm-struct-schema

Source: `dist/types/types/carbon/blockchain/vm/vm-struct-schema.d.ts`

### Declarations

```ts
export declare class VmStructSchema implements CarbonBlobLike {
    static Flags: {
        readonly None: 0;
        readonly DynamicExtras: number;
        readonly IsSorted: number;
    };
    fields: VmNamedVariableSchema[];
    flags: number;
    constructor(fields?: VmNamedVariableSchema[], flags?: number);
    write(w: CarbonBinaryWriter): void;
    read(r: CarbonBinaryReader): void;
    static read(r: CarbonBinaryReader): VmStructSchema;
}
```

## phantasma-sdk-ts/types/carbon/blockchain/vm/vm-type

Source: `dist/types/types/carbon/blockchain/vm/vm-type.d.ts`

### Declarations

```ts
export declare enum VmType {
    Dynamic = 0,
    Array = 1,
    Bytes = 2,
    Struct = 4,
    Int8 = 6,
    Int16 = 8,
    Int32 = 10,
    Int64 = 12,
    Int256 = 14,
    Bytes16 = 16,
    Bytes32 = 18,
    Bytes64 = 20,
    String = 22,
    Array_Dynamic = 1,
    Array_Bytes = 3,
    Array_Struct = 5,
    Array_Int8 = 7,
    Array_Int16 = 9,
    Array_Int32 = 11,
    Array_Int64 = 13,
    Array_Int256 = 15,
    Array_Bytes16 = 17,
    Array_Bytes32 = 19,
    Array_Bytes64 = 21,
    Array_String = 23
}
```

```ts
export declare function vmTypeFromString(type: string): VmType;
```

## phantasma-sdk-ts/types/carbon/blockchain/vm/vm-variable-schema

Source: `dist/types/types/carbon/blockchain/vm/vm-variable-schema.d.ts`

### Declarations

```ts
export declare class VmVariableSchema implements CarbonBlobLike {
    type: VmType;
    structure: VmStructSchema;
    constructor(type?: VmType, structure?: VmStructSchema);
    write(w: CarbonBinaryWriter): void;
    read(r: CarbonBinaryReader): void;
    static read(r: CarbonBinaryReader): VmVariableSchema;
}
```

## phantasma-sdk-ts/types/carbon/bytes16

Source: `dist/types/types/carbon/bytes16.d.ts`

### Declarations

```ts
export declare class Bytes16 implements CarbonBlobLike {
    bytes: Uint8Array;
    static readonly Empty: Bytes16;
    constructor(bytes?: Uint8Array);
    write(w: CarbonBinaryWriter): void;
    read(r: CarbonBinaryReader): void;
    static read(r: CarbonBinaryReader): Bytes16;
    equals(other: Bytes16): boolean;
    toHex(): string;
    /** @deprecated Use `toHex` instead. This alias will be removed in v1.0. */
    ToHex(): string;
}
```

## phantasma-sdk-ts/types/carbon/bytes32

Source: `dist/types/types/carbon/bytes32.d.ts`

### Declarations

```ts
export declare class Bytes32 implements CarbonBlobLike {
    bytes: Uint8Array;
    static readonly Empty: Bytes32;
    constructor(bytes?: Uint8Array);
    write(w: CarbonBinaryWriter): void;
    read(r: CarbonBinaryReader): void;
    static read(r: CarbonBinaryReader): Bytes32;
    equals(other: Bytes32): boolean;
    toHex(): string;
    /** @deprecated Use `toHex` instead. This alias will be removed in v1.0. */
    ToHex(): string;
}
```

## phantasma-sdk-ts/types/carbon/bytes64

Source: `dist/types/types/carbon/bytes64.d.ts`

### Declarations

```ts
export declare class Bytes64 implements CarbonBlobLike {
    bytes: Uint8Array;
    static readonly Empty: Bytes64;
    constructor(bytes?: Uint8Array);
    write(w: CarbonBinaryWriter): void;
    read(r: CarbonBinaryReader): void;
    static read(r: CarbonBinaryReader): Bytes64;
    equals(other: Bytes64): boolean;
    toHex(): string;
    /** @deprecated Use `toHex` instead. This alias will be removed in v1.0. */
    ToHex(): string;
}
```

## phantasma-sdk-ts/types/carbon/carbon-blob

Source: `dist/types/types/carbon/carbon-blob.d.ts`

### Declarations

```ts
export declare class CarbonBlob {
    static fromReader<T extends CarbonBlobLike>(ctor: Ctor<T>, r: CarbonBinaryReader): T;
    /** @deprecated Use `fromReader` instead. This alias will be removed in v1.0. */
    static New<T extends CarbonBlobLike>(ctor: Ctor<T>, r: CarbonBinaryReader): T;
    static fromBytes<T extends CarbonBlobLike>(ctor: Ctor<T>, bytes: Uint8Array, offset: number): T;
    /** @deprecated Use `fromBytes` instead. This alias will be removed in v1.0. */
    static NewFromBytes<T extends CarbonBlobLike>(ctor: Ctor<T>, bytes: Uint8Array, offset: number): T;
    static fromBytesChecked<T extends CarbonBlobLike>(ctor: Ctor<T>, bytes: Uint8Array, allowTrailingBytes?: boolean, offset?: number): T;
    /** @deprecated Use `fromBytesChecked` instead. This alias will be removed in v1.0. */
    static NewFromBytesEx<T extends CarbonBlobLike>(ctor: Ctor<T>, bytes: Uint8Array, allowTrailingBytes?: boolean, offset?: number): T;
    static serialize<T extends CarbonBlobLike>(carbonBlob: T): Uint8Array;
    /** @deprecated Use `serialize` instead. This alias will be removed in v1.0. */
    static Serialize<T extends CarbonBlobLike>(carbonBlob: T): Uint8Array;
}
```

```ts
export {};
```

## phantasma-sdk-ts/types/carbon

Source: `dist/types/types/carbon/index.d.ts`

### Declarations

```ts
export * from './blockchain/index.js';
```

```ts
export * from './bytes16.js';
```

```ts
export * from './bytes32.js';
```

```ts
export * from './bytes64.js';
```

```ts
export * from './carbon-blob.js';
```

```ts
export * from './int-x.js';
```

```ts
export * from './small-string.js';
```

```ts
export * from './tx-types.js';
```

```ts
export * from './witness.js';
```

## phantasma-sdk-ts/types/carbon/int-x

Source: `dist/types/types/carbon/int-x.d.ts`

### Declarations

```ts
export declare class IntX implements CarbonBlobLike {
    private big;
    private small;
    private isBig;
    static fromBigInt(v: bigint): IntX;
    static fromI64(v: number | bigint): IntX;
    toBigInt(): bigint;
    toString(): string;
    is8ByteSafe(): boolean;
    write(w: CarbonBinaryWriter): void;
    read(r: CarbonBinaryReader): void;
    static read(r: CarbonBinaryReader): IntX;
}
```

## phantasma-sdk-ts/types/carbon/small-string

Source: `dist/types/types/carbon/small-string.d.ts`

### Declarations

```ts
export declare class SmallString implements CarbonBlobLike {
    data: string;
    constructor(data?: string);
    write(w: CarbonBinaryWriter): void;
    read(r: CarbonBinaryReader): void;
    static read(r: CarbonBinaryReader): SmallString;
    static readonly empty: SmallString;
    compareTo(other: SmallString): number;
}
```

## phantasma-sdk-ts/types/carbon/tx-types

Source: `dist/types/types/carbon/tx-types.d.ts`

### Declarations

```ts
export declare enum TxTypes {
    Call = 0,
    Call_Multi = 1,
    Trade = 2,
    TransferFungible = 3,
    TransferFungible_GasPayer = 4,
    TransferNonFungible_Single = 5,
    TransferNonFungible_Single_GasPayer = 6,
    TransferNonFungible_Multi = 7,
    TransferNonFungible_Multi_GasPayer = 8,
    MintFungible = 9,
    BurnFungible = 10,
    BurnFungible_GasPayer = 11,
    MintNonFungible = 12,
    BurnNonFungible = 13,
    BurnNonFungible_GasPayer = 14,
    Phantasma = 15,
    Phantasma_Raw = 16
}
```

## phantasma-sdk-ts/types/carbon/witness

Source: `dist/types/types/carbon/witness.d.ts`

### Declarations

```ts
export declare class Witness implements CarbonBlobLike {
    address: Bytes32;
    signature: Bytes64;
    constructor(address?: Bytes32, signature?: Bytes64);
    write(w: CarbonBinaryWriter): void;
    read(r: CarbonBinaryReader): void;
    static read(r: CarbonBinaryReader): Witness;
}
```

## phantasma-sdk-ts/types/carbon-serialization

Source: `dist/types/types/carbon-serialization.d.ts`

### Declarations

```ts
export declare class Throw {
    static If(cond: boolean, msg: string): void;
    static Assert(cond: boolean, msg?: string): void;
}
```

```ts
export declare class CarbonBinaryWriter {
    private chunks;
    private size;
    private push;
    toUint8Array(): Uint8Array;
    write(data: Uint8Array): void;
    write1(v: number): void;
    write2(v: number): void;
    write4(v: number): void;
    write4u(v: number): void;
    write8(v: bigint): void;
    write8u(v: bigint): void;
    writeExactly(data: Uint8Array, count: number): void;
    write16(data: Uint8Array | Bytes16): void;
    write32(data: Uint8Array | Bytes32): void;
    write64(data: Uint8Array | Bytes64): void;
    writeBlob<T extends CarbonBlobLike>(data: T): void;
    writeArrayBlob<T extends CarbonBlobLike>(arr: T[]): void;
    writeBigInt(value: bigint): void;
    writeArrayBigInt(items: bigint[]): void;
    writeSz(s: string): void;
    writeArraySz(arr: string[]): void;
    writeArray(bytes: Uint8Array): void;
    writeArray64u(arr: bigint[]): void;
    writeArray64(arr: bigint[]): void;
    writeArray32(arr: number[]): void;
    writeArray16(arr: number[]): void;
    writeArray8(arr: number[]): void;
    writeArrayOfArrays(arr: Uint8Array[]): void;
}
```

```ts
export declare class CarbonBinaryReader {
    private offset;
    private readonly view;
    private readonly bytes;
    constructor(buffer: ArrayBuffer | Uint8Array);
    private take;
    readRemaining(): Uint8Array;
    read1(): number;
    read2(): number;
    read4(): number;
    read4u(): number;
    read8(): bigint;
    read8u(): bigint;
    readExactly(count: number): Uint8Array;
    read16(): Uint8Array;
    read32(): Uint8Array;
    read64(): Uint8Array;
    readInto16(out: Bytes16): void;
    readInto32(out: Bytes32): void;
    readInto64(out: Bytes64): void;
    readBlob<T extends CarbonBlobLike>(ctor: new () => T): T;
    readArrayBlob<T extends CarbonBlobLike>(ctor: new () => T): T[];
    readBigInt(preReadHeader?: number): bigint;
    readArrayBigInt(): bigint[];
    readSz(): string;
    readArraySz(): string[];
    readArray(): Uint8Array;
    readArrayOfArrays(): Uint8Array[];
    readArray64u(): bigint[];
    readArray64(): bigint[];
    readArray32(): number[];
    readArray16(): number[];
    readArray8(): number[];
}
```

```ts
export declare function bigIntToTwosComplementLE(value: bigint): Uint8Array;
```

```ts
export declare function twosComplementLEToBigInt(bytes: Uint8Array): bigint;
```

```ts
export declare function writeBlob<T extends CarbonBlobLike>(w: CarbonBinaryWriter, data: T): void;
```

```ts
export declare function readBlob<T extends CarbonBlobLike>(r: CarbonBinaryReader, ctor: new () => T): T;
```

## phantasma-sdk-ts/types/consensus

Source: `dist/types/types/consensus.d.ts`

### Declarations

```ts
export declare enum ConsensusMode {
    Unanimity = 0,
    Majority = 1,
    Popularity = 2,
    Ranking = 3
}
```

```ts
export declare enum PollState {
    Inactive = 0,
    Active = 1,
    Consensus = 2,
    Failure = 3
}
```

```ts
export declare class PollChoice implements ISerializable {
    value: string;
    constructor(value: string | number[]);
    serializeData(writer: PBinaryWriter): void;
    /** @deprecated Use `serializeData` instead. This alias will be removed in v1.0. */
    SerializeData(writer: PBinaryWriter): void;
    unserializeData(reader: PBinaryReader): void;
    /** @deprecated Use `unserializeData` instead. This alias will be removed in v1.0. */
    UnserializeData(reader: PBinaryReader): void;
    static deserialize(reader: PBinaryReader): PollChoice;
    /** @deprecated Use `deserialize` instead. This alias will be removed in v1.0. */
    static Unserialize(reader: PBinaryReader): PollChoice;
}
```

```ts
export declare class PollValue implements ISerializable {
    value: string;
    ranking: bigint;
    votes: bigint;
    serializeData(writer: PBinaryWriter): void;
    /** @deprecated Use `serializeData` instead. This alias will be removed in v1.0. */
    SerializeData(writer: PBinaryWriter): void;
    unserializeData(reader: PBinaryReader): void;
    /** @deprecated Use `unserializeData` instead. This alias will be removed in v1.0. */
    UnserializeData(reader: PBinaryReader): void;
    static deserialize(reader: PBinaryReader): PollValue;
    /** @deprecated Use `deserialize` instead. This alias will be removed in v1.0. */
    static Unserialize(reader: PBinaryReader): PollValue;
}
```

```ts
export declare class PollVote implements ISerializable {
    index: bigint;
    percentage: bigint;
    serializeData(writer: PBinaryWriter): void;
    /** @deprecated Use `serializeData` instead. This alias will be removed in v1.0. */
    SerializeData(writer: PBinaryWriter): void;
    unserializeData(reader: PBinaryReader): void;
    /** @deprecated Use `unserializeData` instead. This alias will be removed in v1.0. */
    UnserializeData(reader: PBinaryReader): void;
    static deserialize(reader: PBinaryReader): PollVote;
    /** @deprecated Use `deserialize` instead. This alias will be removed in v1.0. */
    static Unserialize(reader: PBinaryReader): PollVote;
}
```

```ts
export declare class ConsensusPoll implements ISerializable {
    subject: string;
    organization: string;
    mode: ConsensusMode;
    state: PollState;
    entries: PollValue[];
    round: bigint;
    startTime: Timestamp;
    endTime: Timestamp;
    choicesPerUser: bigint;
    totalVotes: bigint;
    constructor();
    serializeData(writer: PBinaryWriter): void;
    /** @deprecated Use `serializeData` instead. This alias will be removed in v1.0. */
    SerializeData(writer: PBinaryWriter): void;
    unserializeData(reader: PBinaryReader): void;
    static deserialize(reader: PBinaryReader): ConsensusPoll;
    /** @deprecated Use `deserialize` instead. This alias will be removed in v1.0. */
    static Unserialize(reader: PBinaryReader): ConsensusPoll;
    /** @deprecated Use `unserializeData` instead. This alias will be removed in v1.0. */
    UnserializeData(reader: PBinaryReader): void;
}
```

```ts
export declare class PollPresence implements ISerializable {
    subject: string;
    round: bigint;
    serializeData(writer: PBinaryWriter): void;
    /** @deprecated Use `serializeData` instead. This alias will be removed in v1.0. */
    SerializeData(writer: PBinaryWriter): void;
    unserializeData(reader: PBinaryReader): void;
    /** @deprecated Use `unserializeData` instead. This alias will be removed in v1.0. */
    UnserializeData(reader: PBinaryReader): void;
    static deserialize(reader: PBinaryReader): PollPresence;
    /** @deprecated Use `deserialize` instead. This alias will be removed in v1.0. */
    static Unserialize(reader: PBinaryReader): PollPresence;
}
```

## phantasma-sdk-ts/types/contract

Source: `dist/types/types/contract.d.ts`

### Declarations

```ts
export declare class ContractParameter {
    name: string;
    type: VMType;
    constructor(name: string, type: VMType);
}
```

```ts
export declare class ContractInterface implements ISerializable {
    static readonly empty: ContractInterface;
    /** @deprecated Use `empty` instead. This alias will be removed in v1.0. */
    static readonly Empty: ContractInterface;
    private _methods;
    private _events;
    get methods(): ContractMethod[];
    set methods(value: ContractMethod[]);
    /** @deprecated Use `methods` instead. This alias will be removed in v1.0. */
    get Methods(): ContractMethod[];
    set Methods(value: ContractMethod[]);
    get methodCount(): number;
    /** @deprecated Use `methodCount` instead. This alias will be removed in v1.0. */
    get MethodCount(): number;
    set MethodCount(_value: number);
    get events(): ContractEvent[];
    set events(value: ContractEvent[]);
    /** @deprecated Use `events` instead. This alias will be removed in v1.0. */
    Events(): ContractEvent[];
    get eventCount(): number;
    /** @deprecated Use `eventCount` instead. This alias will be removed in v1.0. */
    EventCount(): number;
    newEmpty(): void;
    constructor(methods?: ContractMethod[], events?: ContractEvent[]);
    get(name: string): ContractMethod | null;
    hasMethod(name: string): boolean;
    /** @deprecated Use `hasMethod` instead. This alias will be removed in v1.0. */
    HasMethod(name: string): boolean;
    hasTokenTrigger(trigger: TokenTrigger): boolean;
    /** @deprecated Use `hasTokenTrigger` instead. This alias will be removed in v1.0. */
    HasTokenTrigger(trigger: TokenTrigger): boolean;
    findMethod(name: string): ContractMethod | null;
    /** @deprecated Use `findMethod` instead. This alias will be removed in v1.0. */
    FindMethod(name: string): ContractMethod | null;
    findEvent(value: number): ContractEvent | null;
    /** @deprecated Use `findEvent` instead. This alias will be removed in v1.0. */
    FindEvent(value: number): ContractEvent | null;
    implementsEvent(evt: ContractEvent): boolean;
    /** @deprecated Use `implementsEvent` instead. This alias will be removed in v1.0. */
    ImplementsEvent(evt: ContractEvent): boolean;
    implementsMethod(method: ContractMethod): boolean;
    /** @deprecated Use `implementsMethod` instead. This alias will be removed in v1.0. */
    ImplementsMethod(method: ContractMethod): boolean;
    implementsInterface(other: ContractInterface): boolean;
    /** @deprecated Use `implementsInterface` instead. This alias will be removed in v1.0. */
    ImplementsInterface(other: ContractInterface): boolean;
    unserializeData(reader: PBinaryReader): void;
    /** @deprecated Use `unserializeData` instead. This alias will be removed in v1.0. */
    UnserializeData(reader: PBinaryReader): void;
    serializeData(writer: PBinaryWriter): void;
    /** @deprecated Use `serializeData` instead. This alias will be removed in v1.0. */
    SerializeData(writer: PBinaryWriter): void;
}
```

```ts
export declare class ContractMethod implements ISerializable {
    name: string;
    returnType: VMType;
    parameters: ContractParameter[];
    offset: number;
    serializeData(writer: PBinaryWriter): void;
    /** @deprecated Use `serializeData` instead. This alias will be removed in v1.0. */
    SerializeData(writer: PBinaryWriter): void;
    unserializeData(reader: PBinaryReader): void;
    /** @deprecated Use `unserializeData` instead. This alias will be removed in v1.0. */
    UnserializeData(reader: PBinaryReader): void;
    constructorOne(name: string, returnType: VMType, labels: Map<string, number>, parameters: ContractParameter[]): void;
    constructor(name?: string, returnType?: VMType, offset?: number, parameters?: ContractParameter[]);
    isProperty(): boolean;
    isTrigger(): boolean;
    toString(): string;
    static fromBytes(bytes: Uint8Array): ContractMethod;
    static deserialize(reader: PBinaryReader): ContractMethod;
    /** @deprecated Use `deserialize` instead. This alias will be removed in v1.0. */
    static Unserialize(reader: PBinaryReader): ContractMethod;
    serialize(writer: PBinaryWriter): void;
    /** @deprecated Use `serialize` instead. This alias will be removed in v1.0. */
    Serialize(writer: PBinaryWriter): void;
    toArray(): Uint8Array;
}
```

```ts
export declare class ContractEvent implements ISerializable {
    value: number;
    name: string;
    returnType: VMType;
    description: Uint8Array;
    constructor(value?: number, name?: string, returnType?: VMType, description?: Uint8Array);
    serializeData(writer: PBinaryWriter): void;
    /** @deprecated Use `serializeData` instead. This alias will be removed in v1.0. */
    SerializeData(writer: PBinaryWriter): void;
    unserializeData(reader: PBinaryReader): void;
    /** @deprecated Use `unserializeData` instead. This alias will be removed in v1.0. */
    UnserializeData(reader: PBinaryReader): void;
    toString(): string;
    static deserialize(reader: PBinaryReader): ContractEvent;
    /** @deprecated Use `deserialize` instead. This alias will be removed in v1.0. */
    static Unserialize(reader: PBinaryReader): ContractEvent;
    serialize(writer: PBinaryWriter): void;
    /** @deprecated Use `serialize` instead. This alias will be removed in v1.0. */
    Serialize(writer: PBinaryWriter): void;
}
```

## phantasma-sdk-ts/types/domain-settings

Source: `dist/types/types/domain-settings.d.ts`

### Declarations

```ts
export declare enum TriggerResult {
    Failure = 0,
    Missing = 1,
    Success = 2
}
```

```ts
export declare enum AccountTrigger {
    OnMint = 0,// address, symbol, amount
    OnBurn = 1,// address, symbol, amount
    OnSend = 2,// address, symbol, amount
    OnReceive = 3,// address, symbol, amount
    OnWitness = 4,// address
    OnUpgrade = 5,// address
    OnMigrate = 6,// from, to
    OnKill = 7
}
```

```ts
export declare enum TokenTrigger {
    OnMint = 0,// address, symbol, amount
    OnBurn = 1,// address, symbol, amount
    OnSend = 2,// address, symbol, amount
    OnReceive = 3,// address, symbol, amount
    OnInfuse = 4,// address, symbol, amount
    OnUpgrade = 5,// address
    OnSeries = 6,// address
    OnWrite = 7,// address, data
    OnMigrate = 8,// from, to
    OnKill = 9
}
```

```ts
export declare enum OrganizationTrigger {
    OnAdd = 0,// address
    OnRemove = 1,// address
    OnUpgrade = 2
}
```

```ts
export declare class StakeReward {
    staker: Address;
    date: Timestamp;
    constructor(staker: Address, date: Timestamp);
}
```

```ts
export declare class DomainSettings {
    static LatestKnownProtocol: number;
    static Phantasma20Protocol: number;
    static Phantasma30Protocol: number;
    static MaxTxPerBlock: number;
    static MaxOracleEntriesPerBlock: number;
    static MaxEventsPerBlock: number;
    static MaxEventsPerTx: number;
    static MaxTriggerLoop: number;
    static MAX_TOKEN_DECIMALS: number;
    static DefaultMinimumGasFee: number;
    static InitialValidatorCount: number;
    static FuelTokenSymbol: string;
    static FuelTokenName: string;
    static FuelTokenDecimals: number;
    static NexusMainnet: string;
    static NexusTestnet: string;
    static StakingTokenSymbol: string;
    static StakingTokenName: string;
    static StakingTokenDecimals: number;
    static FiatTokenSymbol: string;
    static FiatTokenName: string;
    static FiatTokenDecimals: number;
    static RewardTokenSymbol: string;
    static RewardTokenName: string;
    static LiquidityTokenSymbol: string;
    static LiquidityTokenName: string;
    static LiquidityTokenDecimals: number;
    static FuelPerContractDeployTag: string;
    static FuelPerTokenDeployTag: string;
    static FuelPerOrganizationDeployTag: string;
    static SystemTokens: string[];
    static RootChainName: string;
    static ValidatorsOrganizationName: string;
    static MastersOrganizationName: string;
    static StakersOrganizationName: string;
    static PhantomForceOrganizationName: string;
    static PlatformName: string;
    static ArchiveMinSize: number;
    static ArchiveMaxSize: number;
    static InfusionName: string;
    static NameMaxLength: number;
    static UrlMaxLength: number;
    static ArgsMax: number;
    static AddressMaxSize: number;
    static ScriptMaxSize: number;
    static FieldMaxLength: number;
    static FieldMinLength: number;
}
```

## phantasma-sdk-ts/types/ed25519-signature

Source: `dist/types/types/ed25519-signature.d.ts`

### Declarations

```ts
export declare class Ed25519Signature implements Signature {
    bytes: Uint8Array;
    kind: SignatureKind;
    constructor(bytes?: Uint8Array);
    /** @deprecated Use `bytes` instead. This alias will be removed in v1.0. */
    get Bytes(): Uint8Array;
    set Bytes(value: Uint8Array);
    /** @deprecated Use `kind` instead. This alias will be removed in v1.0. */
    get Kind(): SignatureKind;
    set Kind(value: SignatureKind);
    verify(message: Uint8Array, address: Address): boolean;
    /** @deprecated Use `verify` instead. This alias will be removed in v1.0. */
    Verify(message: Uint8Array, address: Address): boolean;
    verifyMultiple(message: Uint8Array, addresses: Address[]): boolean;
    /** @deprecated Use `verifyMultiple` instead. This alias will be removed in v1.0. */
    VerifyMultiple(message: Uint8Array, addresses: Address[]): boolean;
    serializeData(writer: PBinaryWriter): void;
    /** @deprecated Use `serializeData` instead. This alias will be removed in v1.0. */
    SerializeData(writer: PBinaryWriter): void;
    unserializeData(reader: PBinaryReader): void;
    /** @deprecated Use `unserializeData` instead. This alias will be removed in v1.0. */
    UnserializeData(reader: PBinaryReader): void;
    toByteArray(): Uint8Array;
    /** @deprecated Use `toByteArray` instead. This alias will be removed in v1.0. */
    ToByteArray(): Uint8Array;
    static generate(keypair: KeyPair, message: Uint8Array): Ed25519Signature;
    static generate(keypair: IKeyPair, message: Uint8Array): Ed25519Signature;
    /** @deprecated Use `generate` instead. This alias will be removed in v1.0. */
    static Generate(keypair: IKeyPair, message: Uint8Array): Ed25519Signature;
}
```

## phantasma-sdk-ts/types/ed25519

Source: `dist/types/types/ed25519.d.ts`

### Declarations

```ts
export declare function getEd25519PublicKey(privateKey: Uint8Array): Uint8Array;
```

```ts
export declare function getEd25519PublicKeyHex(privateKeyHex: string): string;
```

```ts
export declare function signEd25519(message: Uint8Array, privateKey: Uint8Array): Uint8Array;
```

```ts
export declare function verifyEd25519(message: Uint8Array, signature: Uint8Array, publicKey: Uint8Array): boolean;
```

## phantasma-sdk-ts/types/entropy

Source: `dist/types/types/entropy.d.ts`

### Declarations

```ts
export declare class Entropy {
    static getRandomBytes(targetLength: number): Buffer;
    /** @deprecated Use `getRandomBytes` instead. This alias will be removed in v1.0. */
    static GetRandomBytes(targetLength: number): Buffer;
}
```

## phantasma-sdk-ts/types/extensions/base16

Source: `dist/types/types/extensions/base16.d.ts`

### Declarations

```ts
export declare class Base16 {
    static encode(str: string): string;
    static encodeUint8Array(arr: Uint8Array): string;
    static decode(str: string): string;
    static decodeUint8Array(str: string): Uint8Array;
}
```

## phantasma-sdk-ts/types/extensions/describer

Source: `dist/types/types/extensions/describer.d.ts`

### Declarations

```ts
export declare class Describer {
    private static FRegEx;
    static describe(val: {
        prototype: object;
        toString(): string;
    }, parent?: boolean): string[];
}
```

## phantasma-sdk-ts/types/extensions

Source: `dist/types/types/extensions/index.d.ts`

### Declarations

```ts
export * from './p-binary-reader.js';
```

```ts
export * from './p-binary-writer.js';
```

```ts
export * from './base16.js';
```

```ts
export * from './describer.js';
```

## phantasma-sdk-ts/types/extensions/p-binary-reader

Source: `dist/types/types/extensions/p-binary-reader.d.ts`

### Declarations

```ts
export declare class PBinaryReader {
    reader: BinaryReader;
    get length(): number;
    get position(): number;
    set position(value: number);
    get isEndOfStream(): boolean;
    readBoolean(): boolean;
    readByte(): number;
    readBytes(bytesToRead: number): number[];
    readSignedByte(): number;
    readShort(): number;
    readUnsignedShort(): number;
    readInt(): number;
    readUnsignedInt(): number;
    readLongString(): string;
    readLong(): number;
    readUnsignedLongString(): string;
    readUnsignedLong(): number;
    readFloat(): number;
    readDouble(): number;
    readChar(encoding: Encoding): string;
    readChars(charactersToRead: number, encoding: Encoding): string;
    readCharBytes(bytesToRead: number, encoding: Encoding): string;
    constructor(arg1: Buffer | Uint8Array);
    read(numBytes: number): string;
    readString(): string;
    readStringBytes(numBytes: number): string;
    readBigInteger(): bigint;
    readBigIntAccurate(): string;
    readSignatureV2(): Signature | null;
    readSignature(): Signature | null;
    readByteArray(): string;
    readTimestamp(): Timestamp;
    readVarInt(): number;
    readVarString(): string;
    readVmObject(): string | number | boolean | Record<string, unknown>;
}
```

## phantasma-sdk-ts/types/extensions/p-binary-writer

Source: `dist/types/types/extensions/p-binary-writer.d.ts`

### Declarations

```ts
export declare class PBinaryWriter {
    private writer;
    constructor(arg1?: Buffer | Uint8Array);
    get length(): number;
    get position(): number;
    set position(value: number);
    writeBoolean(value: boolean): void;
    writeByte(value: number): void;
    writeSameByte(value: number, repeats: number): void;
    writeSignedByte(value: number): void;
    writeShort(value: number): void;
    writeUnsignedShort(value: number): void;
    writeInt(value: number): void;
    writeUnsignedInt(value: number): void;
    writeLong(value: string | number): void;
    writeUnsignedLong(value: string | number): void;
    writeFloat(value: number): void;
    writeDouble(value: number): void;
    writeChar(character: string | number, encoding: Encoding): void;
    writeChars(characters: string | number[], encoding: Encoding): void;
    clear(): void;
    toArray(): number[];
    toUint8Array(): Uint8Array;
    appendByte(value: number): this;
    appendBytes(bytes: Uint8Array): void;
    writeEnum(value: number): this;
    writeBytes(bytes: byte[]): this;
    writeVarInt(value: number): this;
    writeTimestamp(obj: Timestamp): this;
    writeDateTime(obj: Date): this;
    rawString(value: string): number[];
    writeByteArray(bytes: number[] | Uint8Array): this;
    writeString(text: string): this;
    emitUInt32(value: number): this;
    writeBigInteger(value: bigint): this;
    writeBigIntegerString(value: string): this;
    writeSignature(signature: Signature | null): this;
    appendHexEncoded(bytesHex: string): this;
    /** @deprecated Use `appendHexEncoded` instead. This alias will be removed in v1.0. */
    AppendHexEncoded(bytesHex: string): this;
}
```

```ts
export {};
```

## phantasma-sdk-ts/types

Source: `dist/types/types/index.d.ts`

### Declarations

```ts
export * from './carbon/index.js';
```

```ts
export * from './carbon-serialization.js';
```

```ts
export * from './consensus.js';
```

```ts
export * from './timestamp.js';
```

```ts
export * from './stack.js';
```

```ts
export * from './address.js';
```

```ts
export * from './contract.js';
```

```ts
export * from './ed25519-signature.js';
```

```ts
export * from './phantasma-keys.js';
```

```ts
export * from './domain-settings.js';
```

```ts
export * from './entropy.js';
```

```ts
export * from './extensions/index.js';
```

```ts
export * from './serialization.js';
```

## phantasma-sdk-ts/types/phantasma-big-int-serialization

Source: `dist/types/types/phantasma-big-int-serialization.d.ts`

### Declarations

```ts
export declare function bigIntToCsharpLE(n: bigint): Uint8Array;
```

```ts
export declare function bigIntToTwosComplementLE_phantasma(n: bigint): Uint8Array;
```

```ts
export declare function bigIntFromTwosComplementLE_phantasma(data: Uint8Array): bigint;
```

## phantasma-sdk-ts/types/phantasma-keys

Source: `dist/types/types/phantasma-keys.d.ts`

### Declarations

```ts
export declare class PhantasmaKeys implements KeyPair, IKeyPair {
    private _privateKey;
    get privateKey(): Uint8Array<ArrayBufferLike>;
    /** @deprecated Use `privateKey` instead. This alias will be removed in v1.0. */
    get PrivateKey(): Uint8Array<ArrayBufferLike>;
    private _publicKey;
    get publicKey(): Uint8Array<ArrayBufferLike>;
    /** @deprecated Use `publicKey` instead. This alias will be removed in v1.0. */
    get PublicKey(): Uint8Array<ArrayBufferLike>;
    private readonly _address;
    get address(): Address;
    /** @deprecated Use `address` instead. This alias will be removed in v1.0. */
    get Address(): Address;
    static readonly PrivateKeyLength = 32;
    constructor(privateKey: Uint8Array);
    toString(): string;
    static generate(): PhantasmaKeys;
    static fromWIF(wif: string): PhantasmaKeys;
    toWIF(): string;
    static xor(x: Uint8Array, y: Uint8Array): Uint8Array;
    sign(msg: Uint8Array): Signature;
    /** @deprecated Use `sign` instead. This alias will be removed in v1.0. */
    Sign(msg: Uint8Array, customSignFunction?: (msg: Uint8Array, privateKey: Uint8Array, publicKey: Uint8Array) => Uint8Array): Signature;
}
```

## phantasma-sdk-ts/types/serialization

Source: `dist/types/types/serialization.d.ts`

### Declarations

```ts
export interface CustomReader {
    (reader: PBinaryReader): unknown;
}
```

```ts
export interface CustomWriter {
    (writer: PBinaryWriter, obj: unknown): void;
}
```

```ts
export declare class CustomSerializer {
    readonly read: CustomReader;
    readonly write: CustomWriter;
    constructor(reader: CustomReader, writer: CustomWriter);
    /** @deprecated Use `read` instead. This alias will be removed in v1.0. */
    get Read(): CustomReader;
    /** @deprecated Use `write` instead. This alias will be removed in v1.0. */
    get Write(): CustomWriter;
}
```

```ts
export declare class Serialization {
    private static _customSerializers;
    static registerType<T>(type: T, reader: CustomReader, writer: CustomWriter): void;
    /** @deprecated Use `registerType` instead. This alias will be removed in v1.0. */
    static RegisterType<T>(type: T, reader: CustomReader, writer: CustomWriter): void;
    static serializeEnum(obj: unknown): Uint8Array;
    /** @deprecated Use `serializeEnum` instead. This alias will be removed in v1.0. */
    static SerializeEnum(obj: unknown): Uint8Array;
    static serialize(obj: unknown): Uint8Array;
    /** @deprecated Use `serialize` instead. This alias will be removed in v1.0. */
    static Serialize(obj: unknown): Uint8Array;
    static serializeObject(writer: PBinaryWriter, obj: unknown, type: unknown | null): void;
    /** @deprecated Use `serializeObject` instead. This alias will be removed in v1.0. */
    static SerializeObject(writer: PBinaryWriter, obj: unknown, type: unknown | null): void;
    static deserialize<T>(bytesOrBytes: Uint8Array | PBinaryReader, type?: unknown): T;
    /** @deprecated Use `deserialize` instead. This alias will be removed in v1.0. */
    static Unserialize<T>(bytesOrBytes: Uint8Array | PBinaryReader, type?: unknown): T;
    static deserializeObject<T>(reader: PBinaryReader, type: Constructor<T> | unknown): T;
    /** @deprecated Use `deserializeObject` instead. This alias will be removed in v1.0. */
    static UnserializeObject<T>(reader: PBinaryReader, type: Constructor<T> | unknown): T;
}
```

```ts
export {};
```

## phantasma-sdk-ts/types/stack

Source: `dist/types/types/stack.d.ts`

### Declarations

```ts
export declare class Stack<T> implements StackLike<T> {
    private capacity;
    private storage;
    constructor(capacity?: number);
    push(item: T): void;
    pop(): T | undefined;
    peek(): T | undefined;
    size(): number;
    isEmpty(): boolean;
    toArray(): T[];
    clear(): void;
    toString(): string;
    isFull(): boolean;
}
```

## phantasma-sdk-ts/types/timestamp

Source: `dist/types/types/timestamp.d.ts`

### Declarations

```ts
export declare class Timestamp {
    value: number;
    constructor(value: number);
    toString(): string;
    toStringFormat(_format?: string): string;
    static now: number;
    static null: Timestamp;
    compareTo(other: Timestamp): 0 | 1 | -1;
    equals(obj: unknown): boolean;
    getHashCode(): number;
    getSize(): number;
    static equal(A: Timestamp, B: Timestamp): boolean;
    static notEqual(A: Timestamp, B: Timestamp): boolean;
    static lessThan(A: Timestamp, B: Timestamp): boolean;
    static greaterThan(A: Timestamp, B: Timestamp): boolean;
    static lessThanOrEqual(A: Timestamp, B: Timestamp): boolean;
    static greaterThanOrEqual(A: Timestamp, B: Timestamp): boolean;
    static subtract(A: Timestamp, B: Timestamp): number;
    static fromNumber(ticks: number): Timestamp;
    static fromDate(time: Date): Timestamp;
    static addTimeSpan(A: Timestamp, B: number): number;
    static subtractTimeSpan(A: Timestamp, B: number): number;
    serializeData(writer: PBinaryWriter): void;
    unserializeData(reader: PBinaryReader): void;
    static serialize(timestamp: Timestamp, writer: PBinaryWriter): void;
    static deserialize(reader: PBinaryReader): Timestamp;
    /** @deprecated Use `serializeData` or `Timestamp.serialize` instead. This alias will be removed in v1.0. */
    static Serialize(timestamp?: Timestamp, writer?: PBinaryWriter): void;
    /** @deprecated Use `Timestamp.deserialize` instead. This alias will be removed in v1.0. */
    static Unserialize(reader?: PBinaryReader): Timestamp | undefined;
}
```

## phantasma-sdk-ts/utils/hex

Source: `dist/types/utils/hex.d.ts`

### Declarations

```ts
export declare function bytesToHex(bytes: Uint8Array): string;
```

```ts
export declare function bytesToHex(bytes: readonly number[]): string;
```

```ts
export declare function bytesToHex(bytes: ArrayLike<number>): string;
```

```ts
export declare function hexToBytes(hex: string): Uint8Array;
```

## phantasma-sdk-ts/utils

Source: `dist/types/utils/index.d.ts`

### Declarations

```ts
export * from './hex.js';
```

```ts
export * from './validation-utils.js';
```

```ts
export * from './logger.js';
```

```ts
export declare function reverseHex(hex: string): string;
```

```ts
export declare function getDifficulty(transactionHash: string): number;
```

```ts
export declare function decodeBase16(hex: string): string;
```

```ts
export declare function encodeBase16(str: string): string;
```

```ts
export declare function uint8ArrayToString(array: Uint8Array): string;
```

```ts
export declare function uint8ArrayToStringDefault(array: Uint8Array): string;
```

```ts
export declare function uint8ArrayToNumberArray(array: Uint8Array): number[];
```

```ts
export declare function stringToUint8Array(str: string): Uint8Array;
```

```ts
export declare function hexStringToUint8Array(str: string): Uint8Array;
```

```ts
export declare function arrayNumberToUint8Array(arr: number[]): Uint8Array;
```

```ts
export declare function uint8ArrayToBytes(array: Uint8Array): number[];
```

```ts
export declare function numberToByteArray(num: number, size?: number): Uint8Array;
```

```ts
export declare function bigIntToByteArray(bigint: bigint): Uint8Array;
```

```ts
export declare const hex2ascii: (hexx: string) => string;
```

```ts
export declare const Int2Buffer: (i: number) => Buffer;
```

## phantasma-sdk-ts/utils/logger

Source: `dist/types/utils/logger.d.ts`

### Declarations

```ts
export interface Logger {
    log?: (...args: unknown[]) => void;
    info?: (...args: unknown[]) => void;
    warn?: (...args: unknown[]) => void;
    error?: (...args: unknown[]) => void;
    debug?: (...args: unknown[]) => void;
    trace?: (...args: unknown[]) => void;
}
```

```ts
export declare const logger: Required<Logger>;
```

```ts
export declare function setLogger(custom?: Logger): void;
```

## phantasma-sdk-ts/utils/validation-utils

Source: `dist/types/utils/validation-utils.d.ts`

### Declarations

```ts
export declare const ANONYMOUS_NAME = "anonymous";
```

```ts
export declare const GENESIS_NAME = "genesis";
```

```ts
export declare const ENTRY_CONTEXT_NAME = "entry";
```

```ts
export declare const NULL_NAME = "null";
```

```ts
export declare function isReservedIdentifier(name: string): boolean;
```

```ts
export declare function isValidIdentifier(name: string | null | undefined): boolean;
```

```ts
export declare function isValidTicker(name: string | null | undefined): boolean;
```

## phantasma-sdk-ts/vm/contracts

Source: `dist/types/vm/contracts.d.ts`

### Declarations

```ts
export declare enum Contracts {
    GasContractName = "gas",
    BlockContractName = "block",
    StakeContractName = "stake",
    SwapContractName = "swap",
    AccountContractName = "account",
    ConsensusContractName = "consensus",
    GovernanceContractName = "governance",
    StorageContractName = "storage",
    ValidatorContractName = "validator",
    InteropContractName = "interop",
    ExchangeContractName = "exchange",
    PrivacyContractName = "privacy",
    RelayContractName = "relay",
    RankingContractName = "ranking"
}
```

## phantasma-sdk-ts/vm/decoder

Source: `dist/types/vm/decoder.d.ts`

### Declarations

```ts
export declare class Decoder {
    str: string;
    constructor(str: string);
    isEnd(): boolean;
    readCharPair(): string;
    readByte(): number;
    read(numBytes: number): string;
    readString(): string;
    readStringBytes(numBytes: number): string;
    readByteArray(): string | never[];
    readSignature(): ISignature | null;
    readTimestamp(): number;
    readVarInt(): number;
    readBigInt(): number;
    private readBigIntAsBigInt;
    readBigIntAccurate(): string;
    readVmObject(): string | number | boolean | Record<string, unknown>;
}
```

## phantasma-sdk-ts/vm/disassembler

Source: `dist/types/vm/disassembler.d.ts`

### Declarations

```ts
export declare class Disassembler {
}
```

```ts
export declare class Dissassembler extends Disassembler {
}
```

## phantasma-sdk-ts/vm/event-data

Source: `dist/types/vm/event-data.d.ts`

### Declarations

```ts
export declare enum EventKind {
    Unknown = 0,
    ChainCreate = 1,
    TokenCreate = 2,
    TokenSend = 3,
    TokenReceive = 4,
    TokenMint = 5,
    TokenBurn = 6,
    TokenStake = 7,
    TokenClaim = 8,
    AddressRegister = 9,
    AddressLink = 10,
    AddressUnlink = 11,
    OrganizationCreate = 12,
    OrganizationAdd = 13,
    OrganizationRemove = 14,
    GasEscrow = 15,
    GasPayment = 16,
    AddressUnregister = 17,
    OrderCreated = 18,
    OrderCancelled = 19,
    OrderFilled = 20,
    OrderClosed = 21,
    FeedCreate = 22,
    FeedUpdate = 23,
    FileCreate = 24,
    FileDelete = 25,
    ValidatorPropose = 26,
    ValidatorElect = 27,
    ValidatorRemove = 28,
    ValidatorSwitch = 29,
    PackedNFT = 30,
    ValueCreate = 31,
    ValueUpdate = 32,
    PollCreated = 33,
    PollClosed = 34,
    PollVote = 35,
    ChannelCreate = 36,
    ChannelRefill = 37,
    ChannelSettle = 38,
    LeaderboardCreate = 39,
    LeaderboardInsert = 40,
    LeaderboardReset = 41,
    PlatformCreate = 42,
    ChainSwap = 43,
    ContractRegister = 44,
    ContractDeploy = 45,
    AddressMigration = 46,
    ContractUpgrade = 47,
    Log = 48,
    Inflation = 49,
    OwnerAdded = 50,
    OwnerRemoved = 51,
    DomainCreate = 52,
    DomainDelete = 53,
    TaskStart = 54,
    TaskStop = 55,
    CrownRewards = 56,
    Infusion = 57,
    Crowdsale = 58,
    OrderBid = 59,
    ContractKill = 60,
    OrganizationKill = 61,
    MasterClaim = 62,
    ExecutionFailure = 63,
    Custom = 64,
    Custom_V2 = 65,
    GovernanceSetGasConfig = 66,
    GovernanceSetChainConfig = 67,
    TokenSeriesCreate = 68,
    SpecialResolution = 69
}
```

```ts
export declare enum TypeAuction {
    Fixed = 0,
    Classic = 1,
    Reserve = 2,
    Dutch = 3
}
```

```ts
export declare function decodeVMObject(str: string): unknown;
```

```ts
export interface TokenEventData {
    symbol: string;
    value: string;
    chainName: string;
}
```

```ts
export declare function getTokenEventData(str: string): TokenEventData;
```

```ts
export interface ChainValueEventData {
    name: string;
    value: number;
}
```

```ts
export declare function getChainValueEventData(str: string): ChainValueEventData;
```

```ts
export interface TransactionSettleEventData {
    hash: string;
    platform: string;
    chain: string;
}
```

```ts
export declare function getTransactionSettleEventData(str: string): TransactionSettleEventData;
```

```ts
export interface GasEventData {
    address: string;
    price: number;
    amount: number;
    endAmount: number;
}
```

```ts
export declare function getGasEventData(str: string): GasEventData;
```

```ts
export interface InfusionEventData {
    baseSymbol: string;
    tokenId: string;
    infusedSymbol: string;
    infusedValue: string;
    chainName: string;
    /** @deprecated Use `tokenId` instead. This alias will be removed in v1.0. */
    TokenID: string;
    /** @deprecated Use `infusedSymbol` instead. This alias will be removed in v1.0. */
    InfusedSymbol: string;
    /** @deprecated Use `infusedValue` instead. This alias will be removed in v1.0. */
    InfusedValue: string;
    /** @deprecated Use `chainName` instead. This alias will be removed in v1.0. */
    ChainName: string;
}
```

```ts
export declare function getInfusionEventData(str: string): InfusionEventData;
```

```ts
export interface MarketEventData {
    baseSymbol: string;
    quoteSymbol: string;
    id: string;
    amount: number;
}
```

```ts
export declare function getMarketEventData(str: string): MarketEventData;
```

```ts
export declare function getString(str: string): string;
```

## phantasma-sdk-ts/vm

Source: `dist/types/vm/index.d.ts`

### Declarations

```ts
export * from './script-builder.js';
```

```ts
export * from './contracts.js';
```

```ts
export * from './opcode.js';
```

```ts
export * from './vm-type.js';
```

```ts
export * from './event-data.js';
```

```ts
export * from './decoder.js';
```

```ts
export * from './disassembler.js';
```

```ts
export * from './vm-object.js';
```

## phantasma-sdk-ts/vm/opcode

Source: `dist/types/vm/opcode.d.ts`

### Declarations

```ts
export declare enum Opcode {
    NOP = 0,
    MOVE = 1,// copy reference
    COPY = 2,// copy by value
    PUSH = 3,
    POP = 4,
    SWAP = 5,
    CALL = 6,
    EXTCALL = 7,
    JMP = 8,
    JMPIF = 9,
    JMPNOT = 10,
    RET = 11,
    THROW = 12,
    LOAD = 13,
    CAST = 14,
    CAT = 15,
    RANGE = 16,
    LEFT = 17,
    RIGHT = 18,
    SIZE = 19,
    COUNT = 20,
    NOT = 21,
    AND = 22,
    OR = 23,
    XOR = 24,
    EQUAL = 25,
    LT = 26,
    GT = 27,
    LTE = 28,
    GTE = 29,
    INC = 30,
    DEC = 31,
    SIGN = 32,
    NEGATE = 33,
    ABS = 34,
    ADD = 35,
    SUB = 36,
    MUL = 37,
    DIV = 38,
    MOD = 39,
    SHL = 40,
    SHR = 41,
    MIN = 42,
    MAX = 43,
    POW = 44,
    CTX = 45,
    SWITCH = 46,
    PUT = 47,
    GET = 48,// lookups a key and copies a reference into register
    CLEAR = 49,// clears a register
    UNPACK = 50,// unpacks serialized struct based on ref struct
    PACK = 51,// unused for now
    DEBUG = 52,
    SUBSTR = 53
}
```

## phantasma-sdk-ts/vm/script-builder

Source: `dist/types/vm/script-builder.d.ts`

### Declarations

```ts
export declare class ScriptBuilder {
    _labelLocations: {
        [id: string]: number;
    };
    _jumpLocations: {
        [id: number]: string;
    };
    str: string;
    writer: PBinaryWriter;
    NullAddress: string;
    static create(): ScriptBuilder;
    /** @deprecated Use `ScriptBuilder.create()` instead. This alias will be removed in v1.0. */
    static ScriptBuilder(): ScriptBuilder;
    constructor();
    beginScript(): this;
    getScript(): string;
    endScript(): string;
    emit(opcode: Opcode, bytes?: number[]): this;
    emitThrow(reg: byte): this;
    emitPush(reg: byte): this;
    emitPop(reg: byte): this;
    emitExtCall(method: string, reg?: byte): this;
    emitBigInteger(value: string): this;
    emitAddress(textAddress: string): this;
    rawString(value: string): number[];
    private emitLoadBigInt;
    emitLoad(reg: number, obj: ScriptLoadValue): this;
    emitLoadBytes(reg: number, bytes: byte[], type?: VMType): this;
    emitLoadArray(reg: number, obj: unknown[]): this;
    emitLoadSerializable(reg: number, obj: SerializableLike): this;
    emitLoadVmObject(reg: number, obj: VMObject): this;
    emitLoadEnum(reg: number, enumVal: number): this;
    emitLoadAddress(reg: number, obj: Address): this;
    emitLoadTimestamp(reg: number, obj: Date | Timestamp): this;
    emitLoadVarInt(reg: number, val: number): this;
    emitMove(src_reg: number, dst_reg: number): this;
    emitCopy(src_reg: number, dst_reg: number): this;
    emitLabel(label: string): this;
    emitJump(opcode: Opcode, label: string, reg?: number): this;
    emitCall(label: string, regCount: byte): this;
    emitConditionalJump(opcode: Opcode, src_reg: byte, label: string): this;
    insertMethodArgs(args: ScriptLoadValue[]): void;
    callInterop(method: string, args: ScriptLoadValue[]): this;
    callContract(contractName: string, method: string, args: ScriptLoadValue[]): this;
    allowGas(from: string | Address, to: string | Address, gasPrice: number | bigint, gasLimit: number | bigint): this;
    spendGas(address: string | Address): this;
    mintTokens(symbol: string, from: string | Address, to: string | Address, amount: number | bigint): this;
    transferTokens(symbol: string, from: string | Address, to: string | Address, amount: number | bigint): this;
    transferBalance(symbol: string, from: string | Address, to: string | Address): this;
    transferNft(symbol: string, from: string | Address, to: string | Address, tokenId: number | bigint): this;
    crossTransferToken(destinationChain: string | Address, symbol: string, from: string | Address, to: string | Address, amount: number | bigint): this;
    crossTransferNft(destinationChain: string | Address, symbol: string, from: string | Address, to: string | Address, tokenId: number | bigint): this;
    stake(address: string | Address, amount: number | bigint): this;
    unstake(address: string | Address, amount: number | bigint): this;
    callNft(symbol: string, seriesId: number | bigint, method: string, args?: ScriptLoadValue[]): this;
    emitTimestamp(obj: Date): this;
    emitByteArray(bytes: number[]): this;
    emitVarString(text: string): this;
    emitVarInt(value: number): this;
    emitUInt32(value: number): this;
    emitBytes(bytes: byte[]): this;
    byteToHex(byte: number): string;
    appendByte(byte: number): void;
    appendBytes(bytes: byte[]): void;
    appendUShort(ushort: number): void;
    appendHexEncoded(bytes: string): this;
    /** @deprecated Use `beginScript` instead. This alias will be removed in v1.0. */
    BeginScript(): this;
    /** @deprecated Use `getScript` instead. This alias will be removed in v1.0. */
    GetScript(): string;
    /** @deprecated Use `endScript` instead. This alias will be removed in v1.0. */
    EndScript(): string;
    /** @deprecated Use `emit` instead. This alias will be removed in v1.0. */
    Emit(opcode: Opcode, bytes?: number[]): this;
    /** @deprecated Use `emitThrow` instead. This typoed alias will be removed in v1.0. */
    EmitThorw(reg: byte): this;
    /** @deprecated Use `emitPush` instead. This alias will be removed in v1.0. */
    EmitPush(reg: byte): this;
    /** @deprecated Use `emitPop` instead. This alias will be removed in v1.0. */
    EmitPop(reg: byte): this;
    /** @deprecated Use `emitExtCall` instead. This alias will be removed in v1.0. */
    EmitExtCall(method: string, reg?: byte): this;
    /** @deprecated Use `emitBigInteger` instead. This alias will be removed in v1.0. */
    EmitBigInteger(value: string): this;
    /** @deprecated Use `emitAddress` instead. This alias will be removed in v1.0. */
    EmitAddress(textAddress: string): this;
    /** @deprecated Use `rawString` instead. This alias will be removed in v1.0. */
    RawString(value: string): number[];
    /** @deprecated Use `emitLoad` instead. This alias will be removed in v1.0. */
    EmitLoad(reg: number, obj: ScriptLoadValue): this;
    /** @deprecated Use `emitLoadBytes` instead. This alias will be removed in v1.0. */
    EmitLoadBytes(reg: number, bytes: byte[], type?: VMType): this;
    /** @deprecated Use `emitLoadArray` instead. This alias will be removed in v1.0. */
    EmitLoadArray(reg: number, obj: unknown[]): this;
    /** @deprecated Use `emitLoadSerializable` instead. This alias will be removed in v1.0. */
    EmitLoadISerializable(reg: number, obj: ISerializable): this;
    /** @deprecated Use `emitLoadVmObject` instead. This alias will be removed in v1.0. */
    EmitLoadVMObject(reg: number, obj: VMObject): this;
    /** @deprecated Use `emitLoadEnum` instead. This alias will be removed in v1.0. */
    EmitLoadEnum(reg: number, enumVal: number): this;
    /** @deprecated Use `emitLoadAddress` instead. This alias will be removed in v1.0. */
    EmitLoadAddress(reg: number, obj: Address): this;
    /** @deprecated Use `emitLoadTimestamp` instead. This alias will be removed in v1.0. */
    EmitLoadTimestamp(reg: number, obj: Date | Timestamp): this;
    /** @deprecated Use `emitLoadVarInt` instead. This alias will be removed in v1.0. */
    EmitLoadVarInt(reg: number, val: number): this;
    /** @deprecated Use `emitMove` instead. This alias will be removed in v1.0. */
    EmitMove(src_reg: number, dst_reg: number): this;
    /** @deprecated Use `emitCopy` instead. This alias will be removed in v1.0. */
    EmitCopy(src_reg: number, dst_reg: number): this;
    /** @deprecated Use `emitLabel` instead. This alias will be removed in v1.0. */
    EmitLabel(label: string): this;
    /** @deprecated Use `emitJump` instead. This alias will be removed in v1.0. */
    EmitJump(opcode: Opcode, label: string, reg?: number): this;
    /** @deprecated Use `emitCall` instead. This alias will be removed in v1.0. */
    EmitCall(label: string, regCount: byte): this;
    /** @deprecated Use `emitConditionalJump` instead. This alias will be removed in v1.0. */
    EmitConditionalJump(opcode: Opcode, src_reg: byte, label: string): this;
    /** @deprecated Use `insertMethodArgs` instead. This alias will be removed in v1.0. */
    InsertMethodArgs(args: ScriptLoadValue[]): void;
    /** @deprecated Use `callInterop` instead. This alias will be removed in v1.0. */
    CallInterop(method: string, args: ScriptLoadValue[]): this;
    /** @deprecated Use `callContract` instead. This alias will be removed in v1.0. */
    CallContract(contractName: string, method: string, args: ScriptLoadValue[]): this;
    /** @deprecated Use `allowGas` instead. This alias will be removed in v1.0. */
    AllowGas(from: string | Address, to: string | Address, gasPrice: number | bigint, gasLimit: number | bigint): this;
    /** @deprecated Use `spendGas` instead. This alias will be removed in v1.0. */
    SpendGas(address: string | Address): this;
    /** @deprecated Use `mintTokens` instead. This alias will be removed in v1.0. */
    MintTokens(symbol: string, from: string | Address, to: string | Address, amount: number | bigint): this;
    /** @deprecated Use `transferTokens` instead. This alias will be removed in v1.0. */
    TransferTokens(symbol: string, from: string | Address, to: string | Address, amount: number | bigint): this;
    /** @deprecated Use `transferBalance` instead. This alias will be removed in v1.0. */
    TransferBalance(symbol: string, from: string | Address, to: string | Address): this;
    /** @deprecated Use `transferNft` instead. This alias will be removed in v1.0. */
    TransferNFT(symbol: string, from: string | Address, to: string | Address, tokenId: number | bigint): this;
    /** @deprecated Use `crossTransferToken` instead. This alias will be removed in v1.0. */
    CrossTransferToken(destinationChain: string | Address, symbol: string, from: string | Address, to: string | Address, amount: number | bigint): this;
    /** @deprecated Use `crossTransferNft` instead. This alias will be removed in v1.0. */
    CrossTransferNFT(destinationChain: string | Address, symbol: string, from: string | Address, to: string | Address, tokenId: number | bigint): this;
    /** @deprecated Use `stake` instead. This alias will be removed in v1.0. */
    Stake(address: string | Address, amount: number | bigint): this;
    /** @deprecated Use `unstake` instead. This alias will be removed in v1.0. */
    Unstake(address: string | Address, amount: number | bigint): this;
    /** @deprecated Use `callNft` instead. This alias will be removed in v1.0. */
    CallNFT(symbol: string, seriesId: number | bigint, method: string, args?: ScriptLoadValue[]): this;
    /** @deprecated Use `emitTimestamp` instead. This alias will be removed in v1.0. */
    EmitTimestamp(obj: Date): this;
    /** @deprecated Use `emitByteArray` instead. This alias will be removed in v1.0. */
    EmitByteArray(bytes: number[]): this;
    /** @deprecated Use `emitVarString` instead. This alias will be removed in v1.0. */
    EmitVarString(text: string): this;
    /** @deprecated Use `emitVarInt` instead. This alias will be removed in v1.0. */
    EmitVarInt(value: number): this;
    /** @deprecated Use `emitUInt32` instead. This alias will be removed in v1.0. */
    EmitUInt32(value: number): this;
    /** @deprecated Use `emitBytes` instead. This alias will be removed in v1.0. */
    EmitBytes(bytes: byte[]): this;
    /** @deprecated Use `byteToHex` instead. This alias will be removed in v1.0. */
    ByteToHex(byte: number): string;
    /** @deprecated Use `appendByte` instead. This alias will be removed in v1.0. */
    AppendByte(byte: number): void;
    /** @deprecated Use `appendBytes` instead. This alias will be removed in v1.0. */
    AppendBytes(bytes: byte[]): void;
    /** @deprecated Use `appendUShort` instead. This alias will be removed in v1.0. */
    AppendUshort(ushort: number): void;
    /** @deprecated Use `appendHexEncoded` instead. This alias will be removed in v1.0. */
    AppendHexEncoded(bytes: string): this;
}
```

```ts
export {};
```

## phantasma-sdk-ts/vm/utils/disasm-method-call

Source: `dist/types/vm/utils/disasm-method-call.d.ts`

### Declarations

```ts
export declare class DisasmMethodCall {
    contractName: string;
    methodName: string;
    arguments: VMObject[];
    /** @deprecated Use `contractName` instead. This alias will be removed in v1.0. */
    get ContractName(): string;
    set ContractName(value: string);
    /** @deprecated Use `methodName` instead. This alias will be removed in v1.0. */
    get MethodName(): string;
    set MethodName(value: string);
    /** @deprecated Use `arguments` instead. This alias will be removed in v1.0. */
    get Arguments(): VMObject[];
    set Arguments(value: VMObject[]);
    toString(): string;
}
```

## phantasma-sdk-ts/vm/utils/disasm-utils

Source: `dist/types/vm/utils/disasm-utils.d.ts`

### Declarations

```ts
export declare class DisasmUtils {
    private static PopArgs;
}
```

## phantasma-sdk-ts/vm/utils

Source: `dist/types/vm/utils/index.d.ts`

### Declarations

```ts
export * from './disasm-utils.js';
```

```ts
export * from './disasm-method-call.js';
```

## phantasma-sdk-ts/vm/vm-object

Source: `dist/types/vm/vm-object.d.ts`

### Declarations

```ts
export declare class VMObject implements ISerializable {
    /** @deprecated Use `type` instead. This alias will be removed in v1.0. */
    Type: VMType;
    /** @deprecated Use `data` instead. This alias will be removed in v1.0. */
    Data: unknown;
    get type(): VMType;
    set type(value: VMType);
    get data(): unknown;
    set data(value: unknown);
    get isEmpty(): boolean;
    private _localSize;
    private static readonly TimeFormat;
    private static readonly MaxArraySize;
    getChildren(): Map<VMObject, VMObject> | null;
    get size(): number;
    constructor();
    private static bytesFromAny;
    private static bigIntFromAny;
    private static serializeToBytes;
    private static base64Encode;
    private getArrayValue;
    asTimestamp(): Timestamp;
    asByteArray(): Uint8Array;
    asString(): string;
    asNumber(): bigint;
    asEnum<T>(): T;
    getArrayType(): VMType;
    asType(type: VMType): unknown;
    static isEnum(instance: unknown): boolean;
    asBool(): boolean;
    static isStructOrClass(type: unknown): boolean;
    static isSerializable(type: unknown): boolean;
    static isPrimitive(type: unknown): boolean;
    static isValueType(type: unknown): boolean;
    static isClass(type: unknown): boolean;
    static isInterface(type: unknown): boolean;
    private static ConvertObjectInternal;
    toArray(arrayElementType: unknown): unknown[];
    toObjectType(type: unknown): unknown;
    toObject(): unknown;
    toStruct<T>(structType: VMObjectConstructor<T>): T;
    static getVmType(type: unknown): VMType;
    static isVmType(type: unknown): boolean;
    setValue(value: unknown): VMObject;
    setValue(val: unknown, type: VMType): VMObject;
    static validateStructKey(key: VMObject): void;
    castViaReflection(srcObj: unknown, level: number, dontConvertSerializables?: boolean): VMObject;
    setKey(key: VMObject, obj: VMObject): void;
    copy(other: VMObject): void;
    setType(type: VMType): void;
    static fromArray(array: unknown[]): VMObject;
    static castTo(srcObj: VMObject, type: VMType): VMObject;
    static fromObject(obj: unknown): VMObject | null;
    static fromEnum(obj: unknown): VMObject;
    static fromStruct(obj: unknown): VMObject;
    static fromBytes(bytes: Uint8Array | Buffer): VMObject;
    serializeData(writer: PBinaryWriter): Uint8Array<ArrayBufferLike> | undefined;
    /** @deprecated Use `serializeData` instead. This alias will be removed in v1.0. */
    SerializeData(writer: PBinaryWriter): Uint8Array<ArrayBufferLike> | undefined;
    serializeObjectCall(writer: PBinaryWriter): Uint8Array<ArrayBufferLike> | undefined;
    /** @deprecated Use `isEmpty` instead. This alias will be removed in v1.0. */
    get IsEmpty(): boolean;
    /** @deprecated Use `getChildren` instead. This alias will be removed in v1.0. */
    GetChildren(): Map<VMObject, VMObject> | null;
    /** @deprecated Use `size` instead. This alias will be removed in v1.0. */
    get Size(): number;
    /** @deprecated Use `asTimestamp` instead. This alias will be removed in v1.0. */
    AsTimestamp(): Timestamp;
    /** @deprecated Use `asByteArray` instead. This alias will be removed in v1.0. */
    AsByteArray(): Uint8Array;
    /** @deprecated Use `asString` instead. This alias will be removed in v1.0. */
    AsString(): string;
    /** @deprecated Use `asString` instead. This alias will be removed in v1.0. */
    ToString(): string;
    /** @deprecated Use `asNumber` instead. This alias will be removed in v1.0. */
    AsNumber(): bigint;
    /** @deprecated Use `asEnum` instead. This alias will be removed in v1.0. */
    AsEnum<T>(): T;
    /** @deprecated Use `getArrayType` instead. This alias will be removed in v1.0. */
    GetArrayType(): VMType;
    /** @deprecated Use `asType` instead. This alias will be removed in v1.0. */
    AsType(type: VMType): unknown;
    /** @deprecated Use `asBool` instead. This alias will be removed in v1.0. */
    AsBool(): boolean;
    /** @deprecated Use `toArray` instead. This alias will be removed in v1.0. */
    ToArray(arrayElementType: unknown): unknown[];
    /** @deprecated Use `toObjectType` instead. This alias will be removed in v1.0. */
    ToObjectType(type: unknown): unknown;
    /** @deprecated Use `toObject` instead. This alias will be removed in v1.0. */
    ToObject(): unknown;
    /** @deprecated Use `toStruct` instead. This alias will be removed in v1.0. */
    ToStruct<T>(structType: VMObjectConstructor<T>): T;
    /** @deprecated Use `getVmType` instead. This alias will be removed in v1.0. */
    static GetVMType(type: unknown): VMType;
    /** @deprecated Use `isVmType` instead. This alias will be removed in v1.0. */
    static IsVMType(type: unknown): boolean;
    /** @deprecated Use `setValue` instead. This alias will be removed in v1.0. */
    SetValue(value: unknown): VMObject;
    SetValue(val: unknown, type: VMType): VMObject;
    /** @deprecated Use `validateStructKey` instead. This alias will be removed in v1.0. */
    static ValidateStructKey(key: VMObject): void;
    /** @deprecated Use `castViaReflection` instead. This alias will be removed in v1.0. */
    CastViaReflection(srcObj: unknown, level: number, dontConvertSerializables?: boolean): VMObject;
    /** @deprecated Use `setKey` instead. This alias will be removed in v1.0. */
    SetKey(key: VMObject, obj: VMObject): void;
    /** @deprecated Use `copy` instead. This alias will be removed in v1.0. */
    Copy(other: VMObject): void;
    /** @deprecated Use `setType` instead. This alias will be removed in v1.0. */
    SetType(type: VMType): void;
    /** @deprecated Use `fromArray` instead. This alias will be removed in v1.0. */
    static FromArray(array: unknown[]): VMObject;
    /** @deprecated Use `castTo` instead. This alias will be removed in v1.0. */
    static CastTo(srcObj: VMObject, type: VMType): VMObject;
    /** @deprecated Use `fromObject` instead. This alias will be removed in v1.0. */
    static FromObject(obj: unknown): VMObject | null;
    /** @deprecated Use `fromEnum` instead. This alias will be removed in v1.0. */
    static FromEnum(obj: unknown): VMObject;
    /** @deprecated Use `fromStruct` instead. This alias will be removed in v1.0. */
    static FromStruct(obj: unknown): VMObject;
    /** @deprecated Use `fromBytes` instead. This alias will be removed in v1.0. */
    static FromBytes(bytes: Uint8Array | Buffer): VMObject;
    /** @deprecated Use `serializeObjectCall` instead. This alias will be removed in v1.0. */
    SerializeObjectCall(writer: PBinaryWriter): Uint8Array<ArrayBufferLike> | undefined;
    unserializeData(reader: PBinaryReader): void;
    /** @deprecated Use `unserializeData` instead. This alias will be removed in v1.0. */
    UnserializeData(reader: PBinaryReader): void;
}
```

```ts
export {};
```

## phantasma-sdk-ts/vm/vm-type

Source: `dist/types/vm/vm-type.d.ts`

### Declarations

```ts
export declare enum VMType {
    None = 0,
    Struct = 1,
    Bytes = 2,
    Number = 3,
    String = 4,
    Timestamp = 5,
    Bool = 6,
    Enum = 7,
    Object = 8
}
```
