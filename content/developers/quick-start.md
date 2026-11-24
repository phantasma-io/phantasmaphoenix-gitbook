---
title: "Quick start"
linkTitle: "Quick Start"
weight: 10
---

![](/images/banner-pha-phoenix-dev-tools.png)

## Smart contract Development

Smart contracts are written in TOMB and deployed with `pha-deploy`:

- [Smart Contracts](blockchain/smart-contracts/_index.md)

## Connecting to the Chain APIs

> [!NOTE]
> Every Phantasma node serves both a JSON-RPC and a REST interface on the same host. In these pages, "RPC" means the node endpoint unless REST or JSON-RPC is called out explicitly.

The interface paths are the same on every node and network:

| Interface | Path | Notes |
| --- | --- | --- |
| JSON-RPC | `/rpc` | Primary programmatic interface (HTTP POST). |
| REST | `/api/v1` | Same methods and argument names as JSON-RPC. |
| JSON-RPC, REST | `/rpc/v2`, `/api/v2` | The same methods with metadata and NFT property values as real JSON. |
| API reference | `/` | The node root redirects to the interactive Swagger UI. |

For example, on mainnet node 1, JSON-RPC is `https://pharpc1.phantasma.info/rpc` and REST is `https://pharpc1.phantasma.info/api/v1`. In production, discover live nodes from the network's peers list instead of hardcoding a single node. [Node RPC](rpc/_index.md) describes every method and answer.

### Mainnet

<table><thead><tr><th width="25%">Resource</th><th width="75%">Endpoint</th></tr></thead><tbody>
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

<table><thead><tr><th width="25%">Resource</th><th width="75%">Endpoint</th></tr></thead><tbody>
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

<table><thead><tr><th width="25%">Resource</th><th width="75%">Endpoint</th></tr></thead><tbody>
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

### Phantasma SDKs

> [!NOTE]
> Phantasma ships SDKs for C#, Unity, TypeScript/JavaScript, Go, Python, Rust, and C++. Pick the one that matches your stack.


- [Software Development Kits](sdks/_index.md)
