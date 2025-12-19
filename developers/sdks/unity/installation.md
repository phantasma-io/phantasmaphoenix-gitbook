# Installation

This guide will walk you through the process of installing the Phantasma Unity SDK and setting up the wallet connection in your Unity project. The Phantasma Unity SDK is a UPM library that allows you to interact with the Phantasma blockchain from your Unity project.

## Importing the Phantasma Unity SDK to your project

* Open your Unity project.
* Navigate to `Window > Package Manager` from the top menu.
* In the Package Manager window, click the `+` button in the top left corner.
* Select `Install package from git URL...`.
* Enter one of the following git URLs:
  * To install PhantasmaPhoenix.Unity.Core package: `https://github.com/phantasma-io/Phantasma-UnitySDK.git?path=PhantasmaPhoenix.Unity.Core`
  * To install PhantasmaPhoenix.Unity.LinkClient package: `https://github.com/phantasma-io/Phantasma-UnitySDK.git?path=PhantasmaPhoenix.Unity.LinkClient`
* And click `Add`.
* The Phantasma Unity SDK will now be imported into your project.

{% hint style="info" %}
**Note:** To install specific version of package add commit hash of this version to the end of git link, separating it from the rest of the link with # sign: https://github.com/phantasma-io/Phantasma-UnitySDK.git?path=PhantasmaPhoenix.Unity.Core#d011152db4d212e3787628334c6ebd6ce31cea47
{% endhint %}

## Connecting to the Wallet via the SDK

1. Set up your Unity scene.
2. Add the `PhantasmaLinkClient` prefab to your scene.
3. Configure the following settings in the `PhantasmaLinkClient` inspector:
   * **Nexus**: Choose the appropriate Nexus based on your deployment target:
     * For local node deployments, set the Nexus to `simnet`.
     * For testnet deployment, set the Nexus to `testnet`.
     * For mainnet deployment, set the Nexus to `mainnet`.
   * **DappID**: Set the DappID to your Dapp's contract name. This will be displayed when a user logs in to your Dapp.
   * **Version**: The recommended version is `2`.
   * **Wallet Endpoint**: The default wallet endpoint is `localhost:7090`. Do not change this unless required.
   * **Platform and Signature**: Choose the appropriate platform and signature:
     * For Phantasma, select `ED25519`.
     * For Ethereum, select `ECDSA`.

## Connecting to the Wallet via the SDK (Android)

1. Follow the same steps as mentioned in the "Connecting to the Wallet via the SDK" section.
2. Add the `PhantasmaLinkClientPlugin` prefab to your scene.
3. Build your project for Android.

Congratulations! You have successfully installed the Phantasma Unity SDK and connected to the wallet. You are now ready to start developing your Dapp on the Phantasma blockchain.
