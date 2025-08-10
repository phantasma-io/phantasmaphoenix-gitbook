---
description: Here, we will provide information on how to deploy your Smart Contract
---

# How to Deploy

{% hint style="info" %}
**Are you ready?** Do you have your smart contract ready? the **.pvm** & **.abi** file?

If not, go and compile it with Phoenix Smart Language Compiler.
{% endhint %}

## Using Cman

For using Cman, we need to compile it, or download the Published files at the repository.\
Step by step on how to do it.

1. Download the Published (Compiled) files.
2. Extract them to a folder.
3. Enter the folder, open up the terminal or command line there.
4. Now let's type some commands:

```
cman.exe deploy --contract "/path/to/the/.pvm" --wif "yourWif" --rpc-url "http://127.0.0.1:5101/rpc" --nexus "testnet"
```

### Arguments explanation

All the arguments that can be used.

* `--contract <value>` -> attribute to select the path to the contract .pvm (`/path/to/some/contract.pvm`).
* `--rpc-url <value>` -> attribute to select the rpc url.
* `--wif <value>` -> attribute to set the wif of the wallet used to deploy the contact.
* `--nexus <value>` -> attribute to select the nexus name.
* `--token` -> attribute to deploy if the smart contract is a token
* `--update` -> attribute to update the smart contract previously deployed

## Using Phantasma HUB

Go to the Phantasma HUB where you can deploy your contract and do much more than that!

{% embed url="https://contract.phantasma.info/" %}
Phantasma - Hub
{% endembed %}



1. Go to the contract Management Tab

<figure><img src="../../../.gitbook/assets/Screenshot 2023-04-14 at 10.27.42.png" alt=""><figcaption><p>Tab</p></figcaption></figure>

2. Now select Deploy contract ( This would be the same for updating the contract )&#x20;

<figure><img src="../../../.gitbook/assets/Screenshot 2023-04-14 at 10.29.10.png" alt=""><figcaption><p>Deploy new contract</p></figcaption></figure>

3. Fill the Contract/Token name, upload the .pvm and .abi files

<figure><img src="../../../.gitbook/assets/Screenshot 2023-04-14 at 10.30.33.png" alt=""><figcaption><p>Fill the data</p></figcaption></figure>

{% hint style="info" %}
**Don't forget:** Don't forget to connect your wallet and then you can deploy your token or contract.&#x20;
{% endhint %}

4. Deploy to the chain.

<figure><img src="../../../.gitbook/assets/Screenshot 2023-04-14 at 10.33.36.png" alt=""><figcaption><p>Deploy</p></figcaption></figure>
