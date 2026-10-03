# Installation

The Phantasma Unity SDK is distributed as Unity Package Manager packages. Use
`PhantasmaPhoenix.Unity.Core` for RPC access and signing helpers, and
`PhantasmaPhoenix.Unity.LinkClient` when the project needs wallet connection
through Phantasma Link.

Both packages require Unity 2022.3 or later. The sample project in the SDK
repository is built with Unity 6000.0 LTS.

## Importing the Phantasma Unity SDK to your project

* Open your Unity project.
* Navigate to `Window > Package Manager` from the top menu.
* In the Package Manager window, click the `+` button in the top left corner.
* Select `Install package from git URL...`.
* Enter one of the following git URLs:
  * To install PhantasmaPhoenix.Unity.Core package: `https://github.com/phantasma-io/phantasma-sdk-unity.git?path=PhantasmaPhoenix.Unity.Core`
  * To install PhantasmaPhoenix.Unity.LinkClient package: `https://github.com/phantasma-io/phantasma-sdk-unity.git?path=PhantasmaPhoenix.Unity.LinkClient`
* Click `Add`.
* Repeat the package import when the project needs both Core and LinkClient.

{% hint style="info" %}
**Note:** To pin a package to a specific source revision, append `#` and the
commit hash to the Git URL. Example:
`https://github.com/phantasma-io/phantasma-sdk-unity.git?path=PhantasmaPhoenix.Unity.Core#704143b141129df210d83bf3d248f8873748b761`
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
   * **Platform and Signature**: `Phantasma` and `ED25519`. The other values of the two enums are not used by current wallets.

## Connecting to the Wallet via the SDK (Android)

1. Follow the same setup from "Connecting to the Wallet via the SDK".
2. Add the `PhantasmaLinkClientPlugin` prefab to your scene.
3. Build your project for Android.
