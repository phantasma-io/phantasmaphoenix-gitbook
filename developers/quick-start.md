---
cover: .gitbook/assets/gitbook-banner-pha-phoenix-dev-tools.png
coverY: 0
---

# Quick start

## Smart contract Development

{% hint style="info" %}
Are you looking for creating your own smart contract?
{% endhint %}

{% content-ref url="/developers/blockchain/smart-contracts/" %}
Smart Contracts
{% endcontent-ref %}

## Connecting to the Chain APIs

{% hint style="info" %}
All Phantasma Phoenix RPCs come with both REST and RPC interfaces.
In these pages, `RPC` refers to the node endpoint unless the REST or JSON-RPC
interface is called out explicitly.
{% endhint %}

To access the REST API reference served through Swagger, open the node URL in a
browser. It redirects to the Swagger page.
For example, opening https://testnet.phantasma.info/ redirects to:
https://testnet.phantasma.info/swagger/index.html

To send a JSON-RPC query, add `/rpc` to the node URL. For testnet, the endpoint
is:
https://testnet.phantasma.info/rpc

REST and JSON-RPC interfaces use the same endpoint and argument names.

### Testnet URLs

| Type                                | Link                                                                                                     |
| ----------------------------------- | -------------------------------------------------------------------------------------------------------- |
| Testnet Explorer                    | [https://test-explorer.phantasma.info](https://test-explorer.phantasma.info)                             |
| Testnet RPC1 REST API Documentation | [https://testnet.phantasma.info](https://testnet.phantasma.info)                                         |
| Testnet RPC1 REST API               | [https://testnet.phantasma.info/api/v1](https://testnet.phantasma.info/api/v1)                           |
| Testnet RPC1 RPC API                | [https://testnet.phantasma.info/rpc](https://testnet.phantasma.info/rpc)                                 |
| JSON with available testnet RPCs    | [https://peers.phantasma.info/testnet-getpeers.json](https://peers.phantasma.info/testnet-getpeers.json) |

### Mainnet URLs

| Type                                  | Link                                                                                                     |
| ------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| Mainnet Explorer                      | [https://explorer.phantasma.info](https://test-explorer.phantasma.info)                                  |
| Mainnet RPC1 REST API Documentation   | [https://pharpc1.phantasma.info](https://pharpc1.phantasma.info)                                         |
| Mainnet RPC1 REST API                 | [https://pharpc1.phantasma.info/api/v1](https://pharpc1.phantasma.info/api/v1)                           |
| Mainnet RPC1 RPC API                  | [https://pharpc1.phantasma.info/rpc](https://pharpc1.phantasma.info/rpc)                                 |
| Mainnet RPC2 REST API Documentation   | [https://pharpc2.phantasma.info](https://pharpc2.phantasma.info)                                         |
| Mainnet RPC2 REST API                 | [https://pharpc2.phantasma.info/api/v1](https://pharpc2.phantasma.info/api/v1)                           |
| Mainnet RPC2 RPC API                  | [https://pharpc2.phantasma.info/rpc](https://pharpc2.phantasma.info/rpc)                                 |
| JSON with available mainnet RPCs      | [https://peers.phantasma.info/mainnet-getpeers.json](https://peers.phantasma.info/mainnet-getpeers.json) |

### Phantasma SDK's

{% hint style="info" %}
Explore our wide selection of Phantasma blockchain SDKs available for platforms like Unity, Typescript, and C++. These tools empower you to innovate and integrate with the Phantasma ecosystem, irrespective of your preferred development environment. Click to unleash the potential of decentralized technology.
{% endhint %}


{% content-ref url="/developers/sdks/" %}
Software Development Kits
{% endcontent-ref %}
