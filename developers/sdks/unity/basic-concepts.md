# 📚 Basic Concepts

### Basic Concepts

This page introduces the core concepts and components used by the Phantasma
Unity SDK.

#### Phantasma Blockchain

Phantasma is a blockchain platform with smart contracts, side chains, and
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

Smart contracts are self-executing contracts with the terms of the agreement directly written into code. They run on the Phantasma blockchain and can be invoked using the Phantasma Unity SDK. The SDK allows you to interact with smart contracts by sending transactions and receiving responses.

#### Transactions

Transactions transfer assets, invoke smart contracts, and update chain state.
The Unity SDK provides helpers for creating, signing, and broadcasting
transactions from a Unity project.

#### DappID

DappID is a unique identifier for your decentralized application on the Phantasma blockchain. It is used to associate your DApp with a specific smart contract and is displayed when users log in to your application.

### ScriptBuilder

The `ScriptBuilder` creates transaction scripts and serializes them into the byte format required by the chain. The following example builds a custom operation script.

#### SendRawTransaction

`SendRawTransaction` is a method provided by the Phantasma Unity SDK that allows you to interact with the Phantasma blockchain in a way that can change its state. This method is used to perform actions such as transferring assets or invoking smart contracts that modify the blockchain's data. When you use `SendRawTransaction`, you broadcast a signed transaction to the network, and if it is successfully executed, it results in an updated state on the blockchain.

#### InvokeRawScript

`InvokeRawScript` is another method provided by the SDK that allows you to query the Phantasma blockchain without changing its state. This method is useful for fetching data and information from the blockchain without affecting the stored values. Examples of `InvokeRawScript` usage include retrieving account balances, checking the status of a transaction, or reading data from a smart contract. Since it does not modify the blockchain's state, `InvokeRawScript` does not require a signed transaction and can be called directly.

{% hint style="info" %}
**Good to know:** Use **`SendRawTransaction`** for signed state-changing
transactions. Use **`InvokeRawScript`** for read-only script calls.
{% endhint %}
