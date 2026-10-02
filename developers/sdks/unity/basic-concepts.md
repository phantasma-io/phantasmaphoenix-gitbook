# 📚 Basic Concepts

### Basic Concepts

This page introduces the core concepts and components used by the Phantasma
Unity SDK.

#### Phantasma Blockchain

Phantasma is a blockchain platform with smart contracts, side chains (coming soon), and
decentralized storage. The Phantasma Unity SDK lets Unity projects read chain
data, connect wallets, sign transactions, and invoke contracts.

#### PhantasmaLinkClient

`PhantasmaLinkClient` is a prefab provided by the SDK. It handles wallet
connections, transaction signing, and smart contract invocation through
Phantasma Link.

#### Wallet Connection

Wallet connection lets users approve account access and transaction signing.
The `PhantasmaLinkClient` prefab supports nexus and wallet endpoint settings
for simnet, testnet, and mainnet deployments.

#### Smart Contracts

Smart contracts are VM programs deployed on the chain. The Unity SDK calls their methods through scripts and reads their state through RPC.

#### Transactions

Transactions transfer assets, invoke smart contracts, and update chain state.
The Unity SDK provides helpers for creating, signing, and broadcasting
transactions from a Unity project.

#### DappID

The DappID names your application in the wallet's approval prompt when a user connects.

### ScriptBuilder

The `ScriptBuilder` creates transaction scripts and serializes them into the byte format required by the chain. The following example builds a custom operation script.

#### SendRawTransaction

`SendRawTransaction` broadcasts a signed script transaction, which can change chain state: transfer assets, call a contract, mint or burn.

#### InvokeRawScript

`InvokeRawScript` runs a script against the current state without committing anything; use it to read data.

{% hint style="info" %}
**Good to know:** Use **`SendRawTransaction`** for signed state-changing
transactions. Use **`InvokeRawScript`** for read-only script calls.
{% endhint %}
