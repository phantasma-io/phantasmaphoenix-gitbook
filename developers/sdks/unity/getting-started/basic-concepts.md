# Basic Concepts

### Basic Concepts

This section introduces the fundamental concepts and components of the Phantasma Unity SDK. Understanding these concepts will help you effectively utilize the SDK in your Unity projects.

#### Phantasma Blockchain

Phantasma is a blockchain platform designed for fast, secure, and scalable decentralized applications (DApps). It offers features such as smart contracts, side chains, and a decentralized storage system called "Phantasma Storage." The Phantasma Unity SDK allows Unity developers to interact with the Phantasma blockchain and integrate it into their projects.

#### PhantasmaLinkClient

`PhantasmaLinkClient` is a prefab provided by the SDK that acts as the main interface between your Unity project and the Phantasma blockchain. It handles wallet connections, sending and receiving transactions, and invoking smart contracts. By adding this prefab to your scene, you can quickly set up the necessary connections to interact with the Phantasma network.

#### Wallet Connection

Connecting to a wallet is a crucial step in any DApp, as it allows users to manage their assets and interact with the Phantasma blockchain. The SDK provides a simple and secure way to connect to the wallet via the `PhantasmaLinkClient` prefab, which supports different nexus configurations and wallet endpoints depending on your deployment target (localnet, testnet, or mainnet).

#### Smart Contracts

Smart contracts are self-executing contracts with the terms of the agreement directly written into code. They run on the Phantasma blockchain and can be invoked using the Phantasma Unity SDK. The SDK allows you to interact with smart contracts by sending transactions and receiving responses.

#### Transactions

Transactions are the means by which users interact with the Phantasma blockchain. They can be used to transfer assets, invoke smart contracts, and more. The Phantasma Unity SDK simplifies the process of creating, signing, and broadcasting transactions from within your Unity project.

#### DappID

DappID is a unique identifier for your decentralized application on the Phantasma blockchain. It is used to associate your DApp with a specific smart contract and is displayed when users log in to your application.

### ScriptBuilder

The `ScriptBuilder` is a powerful tool provided by the Phantasma SDK that allows you to create and customize transaction scripts for various operations on the Phantasma blockchain. The `ScriptBuilder` helps you create the necessary calls and convert them into byte format, which is required for sending a transaction. The following example demonstrates how to use the `ScriptBuilder` for a custom operation.

#### SendRawTransaction

`SendRawTransaction` is a method provided by the Phantasma Unity SDK that allows you to interact with the Phantasma blockchain in a way that can change its state. This method is used to perform actions such as transferring assets or invoking smart contracts that modify the blockchain's data. When you use `SendRawTransaction`, the transaction is signed and broadcasted to the network, and if it is successfully executed, it results in an updated state on the blockchain.

#### InvokeRawScript

`InvokeRawScript` is another method provided by the SDK that allows you to query the Phantasma blockchain without changing its state. This method is useful for fetching data and information from the blockchain without affecting the stored values. Examples of `InvokeRawScript` usage include retrieving account balances, checking the status of a transaction, or reading data from a smart contract. Since it does not modify the blockchain's state, `InvokeRawScript` does not require a signed transaction and can be called directly.

{% hint style="info" %}
**Good to know:** These two methods, **`SendRawTransaction`** and **`InvokeRawScript`**, are essential components of the Phantasma Unity SDK, allowing developers to interact with the Phantasma blockchain by either modifying its state or fetching data without altering the state. Understanding the difference between these methods will help you effectively utilize the SDK in your Unity projects.
{% endhint %}



By understanding these basic concepts, you will have a solid foundation for working with the Phantasma Unity SDK in your Unity projects. As you progress through the documentation, you'll learn more about the SDK's features and how to use them effectively.
