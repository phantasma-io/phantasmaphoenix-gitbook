# ⚙️ Installation

### Installation

This guide will walk you through the process of installing the Phantasma Unity SDK and setting up the wallet connection in your Unity project. The Phantasma Unity SDK is a UPM library that allows you to interact with the Phantasma blockchain from your Unity project.

#### Importing the Phantasma Unity SDK to Your Project

1. Open your Unity project.
2. Navigate to `Window > Package Manager` from the top menu.
3. In the Package Manager window, click the `+` button in the top left corner.
4. Select `Add package from git URL`.
5. Enter the following git URL: `https://github.com/phantasma-io/Phantasma-UnitySDK.git` and click `Add`.
6. The Phantasma Unity SDK will now be imported into your project.

#### Connecting to the Wallet via the SDK

1. Set up your Unity scene.
2. Add the `PhantasmaLinkClient` prefab to your scene.
3. Configure the following settings in the `PhantasmaLinkClient` inspector:
   * **Nexus**: Choose the appropriate Nexus based on your deployment target:
     * For local node development, set the Nexus to `localnet`.
     * For testnet deployment, set the Nexus to `testnet`.
     * For mainnet deployment, set the Nexus to `mainnet`.
   * **DappID**: Set the DappID to your Dapp's contract name. This will be displayed when a user logs in to your Dapp.
   * **Version**: The recommended version is `2`.
   * **Wallet Endpoint**: The default wallet endpoint is `localhost:7090`. Do not change this unless required.
   * **Platform and Signature**: Choose the appropriate platform and signature:
     * For Phantasma, select `ED25519`.
     * For Ethereum, select `ECDSA`.

#### Connecting to the Wallet via the SDK (Android)

1. Follow the same steps as mentioned in the "Connecting to the Wallet via the SDK" section.
2. Add the `PhantasmaLinkClientPlugin` prefab to your scene.
3. Build your project for Android.

Congratulations! You have successfully installed the Phantasma Unity SDK and connected to the wallet. You are now ready to start developing your Dapp on the Phantasma blockchain.
