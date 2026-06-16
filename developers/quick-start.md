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
Every Phantasma node serves both a JSON-RPC and a REST interface on the same host. In these pages, "RPC" means the node endpoint unless REST or JSON-RPC is called out explicitly.
{% endhint %}

The interface paths are the same on every node and network:

| Interface | Path | Notes |
| --- | --- | --- |
| JSON-RPC | `/rpc` | Primary programmatic interface (HTTP POST). |
| REST | `/api/v1` | Same methods and argument names as JSON-RPC. |
| API reference | `/` | The node root redirects to the interactive Swagger UI. |

For example, on mainnet node 1, JSON-RPC is `https://pharpc1.phantasma.info/rpc` and REST is `https://pharpc1.phantasma.info/api/v1`. In production, discover live nodes from the network's peers list instead of hardcoding a single node.

### Mainnet

<table><thead><tr><th>Resource</th><th>Endpoint</th></tr></thead><tbody>
<tr><td>Explorer</td><td><a href="https://explorer.phantasma.info">explorer.phantasma.info</a></td></tr>
<tr><td>RPC node 1</td><td>

```
https://pharpc1.phantasma.info
```

</td></tr>
<tr><td>RPC node 2</td><td>

```
https://pharpc2.phantasma.info
```

</td></tr>
<tr><td>RPC node 3</td><td>

```
https://pharpc3.phantasma.info
```

</td></tr>
<tr><td>Peers list</td><td>

```
https://peers.phantasma.info/mainnet-getpeers.json
```

</td></tr>
</tbody></table>

### Testnet

<table><thead><tr><th>Resource</th><th>Endpoint</th></tr></thead><tbody>
<tr><td>Explorer</td><td><a href="https://testnet-explorer.phantasma.info">testnet-explorer.phantasma.info</a></td></tr>
<tr><td>RPC node</td><td>

```
https://testnet.phantasma.info
```

</td></tr>
<tr><td>Peers list</td><td>

```
https://peers.phantasma.info/testnet-getpeers.json
```

</td></tr>
</tbody></table>

### Devnet

<table><thead><tr><th>Resource</th><th>Endpoint</th></tr></thead><tbody>
<tr><td>Explorer</td><td><a href="https://devnet-explorer.phantasma.info">devnet-explorer.phantasma.info</a></td></tr>
<tr><td>RPC node</td><td>

```
https://devnet.phantasma.info
```

</td></tr>
<tr><td>Peers list</td><td>

```
https://peers.phantasma.info/devnet-getpeers.json
```

</td></tr>
</tbody></table>

### Phantasma SDK's

{% hint style="info" %}
Phantasma ships SDKs for C#, Unity, TypeScript/JavaScript, Go, Python, Rust, and C++. Pick the one that matches your stack.
{% endhint %}


{% content-ref url="/developers/sdks/" %}
Software Development Kits
{% endcontent-ref %}
