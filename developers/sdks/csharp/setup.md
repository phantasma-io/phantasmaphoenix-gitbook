# Setup

In your project, just import our **Nuget Packages.**

{% hint style="info" %}
**Important:** Before the Phoenix chain update, a different set of NuGet packages was used. These packages are now obsolete and strictly deprecated. Use the new package set instead.
{% endhint %}

Full list of packages is available on our Nuget page:
https://www.nuget.org/profiles/Phantasma.info

| Package name                           | Description       |
| ---------------------------------------| ----------------- |
| [PhantasmaPhoenix.Core](https://www.nuget.org/packages/PhantasmaPhoenix.Core) | Core types and utilities for Phantasma Phoenix SDK |
| [PhantasmaPhoenix.Cryptography](https://www.nuget.org/packages/PhantasmaPhoenix.Cryptography) | Cryptographic primitives and utilities for the Phantasma Phoenix SDK |
| [PhantasmaPhoenix.Cryptography.Legacy](https://www.nuget.org/packages/PhantasmaPhoenix.Cryptography.Legacy) | Legacy cryptographic primitives and utilities for the Phantasma Phoenix SDK. Deprecated, but still used in certain scenarios |
| [PhantasmaPhoenix.InteropChains.Legacy](https://www.nuget.org/packages/PhantasmaPhoenix.InteropChains.Legacy) | Address generation and basic utilities for Neo2 and Ethereum chains, used for external wallet compatibility in the Phantasma Phoenix SDK. Deprecated, but still used in certain scenarios |
| [PhantasmaPhoenix.Link](https://www.nuget.org/packages/PhantasmaPhoenix.Link) | Lightweight WebSocket-based server implementation for the Phantasma Link protocol. Allows dApps to connect with Phantasma wallets |
| [PhantasmaPhoenix.NFT](https://www.nuget.org/packages/PhantasmaPhoenix.NFT) | Utilities for parsing NFT ROM data and accessing metadata in Phantasma |
| [PhantasmaPhoenix.Protocol](https://www.nuget.org/packages/PhantasmaPhoenix.Protocol) | Protocol types, enums, and constants for the Phantasma Phoenix SDK  |
| [PhantasmaPhoenix.Protocol.Carbon](https://www.nuget.org/packages/PhantasmaPhoenix.Protocol.Carbon) | Carbon protocol types and helpers for scriptless (Carbon) transactions |
| [PhantasmaPhoenix.RPC](https://www.nuget.org/packages/PhantasmaPhoenix.RPC) | Provides client-side types and helpers for interacting with the Phantasma Phoenix blockchain RPC and REST APIs |
| [PhantasmaPhoenix.VM](https://www.nuget.org/packages/PhantasmaPhoenix.VM) | Virtual machine implementation and script execution utilities for Phantasma Phoenix SDK |



To import the **nuget,** you can use the nuget window on the **Visual Studio** or **Rider.**&#x20;

Or use the command line:

```
dotnet add package PhantasmaPhoenix.Core
```
```
dotnet add package PhantasmaPhoenix.Cryptography
```
```
dotnet add package PhantasmaPhoenix.Cryptography.Legacy
```
```
dotnet add package PhantasmaPhoenix.InteropChains.Legacy
```
```
dotnet add package PhantasmaPhoenix.Link
```
```
dotnet add package PhantasmaPhoenix.NFT
```
```
dotnet add package PhantasmaPhoenix.Protocol
```
```
dotnet add package PhantasmaPhoenix.Protocol.Carbon
```
```
dotnet add package PhantasmaPhoenix.RPC
```
```
dotnet add package PhantasmaPhoenix.VM
```
