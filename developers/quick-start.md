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

## Connecting to the Chain (API's)

{% hint style="info" %}
All Phantasma Phoenix RPCs come with both REST and RPC interfaces.
Everywhere in documentation RPC nodes will be just called RPCs despite the fact that they support both protocols.
{% endhint %}

To access REST documentation served through Swagger, just open RPC's URL in interner browser. It will automatically redirect you to documetation page.
For example, if you'll open https://testnet.phantasma.info/ URL, you will be redirected to this Swagger page:
https://testnet.phantasma.info/swagger/index.html

To send query through RPC protocol, you need to add '/rpc' to URL, for example for testnet this is the full address of RPC:
https://testnet.phantasma.info/rpc

REST and RPC interfaces use same names for endpoints and arguments. This way REST API Documentation can be easily used to compose RPC queries.

### Testnet URLs

| Type                                | Link                                                                                            |
| ----------------------------------- | ----------------------------------------------------------------------------------------------- |
| Testnet Explorer                    | [https://test-explorer.phantasma.info](https://test-explorer.phantasma.info)                    |
| Testnet RPC1 REST API Documentation | [https://testnet.phantasma.info](https://testnet.phantasma.info)                                |
| Testnet RPC1 REST API               | [https://testnet.phantasma.info/api/v1](https://testnet.phantasma.info/api/v1)                  |
| Testnet RPC1 RPC API                | [https://testnet.phantasma.info/rpc](https://testnet.phantasma.info/rpc)                        |
| JSON with available testnet RPCs    | https://peers.phantasma.info/testnet-getpeers.json                                              |

### Mainnet URLs

| Type                                  | Link                                                                                            |
| ------------------------------------- | ----------------------------------------------------------------------------------------------- |
| Mainnet Explorer                      | [https://explorer.phantasma.info](https://test-explorer.phantasma.info)                         |
| Mainnet RPC1 REST API Documentation   | [https://pharpc1.phantasma.info](https://pharpc1.phantasma.info)                                |
| Mainnet RPC1 REST API                 | [https://pharpc1.phantasma.info/api/v1](https://pharpc1.phantasma.info/api/v1)                  |
| Mainnet RPC1 RPC API                  | [https://pharpc1.phantasma.info/rpc](https://pharpc1.phantasma.info/rpc)                        |
| Mainnet RPC2 REST API Documentation   | [https://pharpc2.phantasma.info](https://pharpc2.phantasma.info)                                |
| Mainnet RPC2 REST API                 | [https://pharpc2.phantasma.info/api/v1](https://pharpc2.phantasma.info/api/v1)                  |
| Mainnet RPC2 RPC API                  | [https://pharpc2.phantasma.info/rpc](https://pharpc2.phantasma.info/rpc)                        |
| JSON with available mainnet RPCs      | https://peers.phantasma.info/mainnet-getpeers.json                                              |

### Phantasma SDK's

{% hint style="info" %}
Explore our wide selection of Phantasma blockchain SDKs available for platforms like Unity, Typescript, and C++. These tools empower you to innovate and integrate with the Phantasma ecosystem, irrespective of your preferred development environment. Click to unleash the potential of decentralized technology.
{% endhint %}


{% content-ref url="/developers/sdks/" %}
Software Development Kits
{% endcontent-ref %}
