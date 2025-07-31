# Non Validator Node

### Before starting keep in mind that you need to install this libraries <a href="#before-starting-keep-in-mind-that-you-need-to-install-this-libraries" id="before-starting-keep-in-mind-that-you-need-to-install-this-libraries"></a>

`1sudo apt-get install -y libc6-dev libsnappy-dev libicu-dev screen bash vim net-tools ca-certificates openssl libssl-dev librocksdb-dev`

### Clone Phantasma-ng <a href="#clone-phantasma-ng" id="clone-phantasma-ng"></a>

{% embed url="https://github.com/phantasma-io/phantasma-ng/tree/dev" %}

### Tendermint <a href="#tendermint" id="tendermint"></a>

#### Setup **Tendermint** <a href="#setup-tendermint" id="setup-tendermint"></a>

{% embed url="https://github.com/tendermint/tendermint/releases/tag/v0.34.24" %}

* Either Install tendermint in the PATH or
* Extract the contents to the folder **NodeExample/tendermint**

#### Configure Tendermint <a href="#configure-tendermint" id="configure-tendermint"></a>

To configure **tendermint** it takes some time, but last go at it

In the **config.toml** we need to change a few things.

1.  **proxy\_app** → here we just change the port to our desired port

    `1proxy_app = "tcp://127.0.0.1:26558"`

    &#x20;
2.  **moniker →** This is the node name, you can name as you want it.

    `1moniker = "nodeExample" # Change this to you node name`
3.  **rpc.laddr →** change the port\
    \


    `1[rpc] 2laddr = "tcp://0.0.0.0:26557"`
4. **p2p.laddr** → Change the port
5.  **p2p.seeds** → Add the seeds (Validator nodes)

    `1[p2p] 2seeds = "node_ID@ip_address:node_port"`

    \
    Instead of changing the **config.toml**, on running can be passed as an argument.

    `1--p2p.seeds "node_ID@ip_address:node_port"`

&#x20;

**Testnet Configuration for tendermint.**

For connecting to the **testnet** you have here the **seed,** you can add it to your node **config.toml** file or run it with the **--p2p.seeds** flag

`10c8203a0e63d7c025a4be9e4391b42fb65d344ab@testnet.phantasma.io:26056`

&#x20;

&#x20;

#### Run Tendermint <a href="#run-tendermint" id="run-tendermint"></a>

To run **tendermint** after extracting it to the **tendermint** folder and giving it the **permission** to execute

`1# This line of code is from the NodeExample folder. 2chmod u+x ./tendermint/tendermint`

Then also give **permission** to the **runTendermintNode.sh**

`1chmod u+x runTendermintNode.sh`

\
There’s some configuration that you can change from the runTendermintNode.sh

* `NODENAME` → Change the node name to the desired one, this will be the name of the folder as well
* `TENDERMINTPATH` → if you have the tendermint globally setuped just change it to tendermint

&#x20;

Now that the permissions are setuped let’s run it!

`1./runTendermintNode.sh`

&#x20;

&#x20;

### Phantasma Node <a href="#phantasma-node" id="phantasma-node"></a>

#### Configure Phantasma Node <a href="#configure-phantasma-node" id="configure-phantasma-node"></a>

On the **config\_example.json** provided on the **NodeExample** Folder

1.  **tendermint.rpc.port →** Change the port for the desired one.

    `1"tendermint.rpc.port": "26557"`
2.  **tendermint.proxy.port** → Change the port

    `1"tendermint.proxy.port": "26558"`
3.  **tendermint.key** → Change the wif to your node wif (tendermint key, this key can be found on the **node/config/priv\_validator\_key.json** and it’s the “priv\_key” > “value”)

    ![](blob:https://phantasma.atlassian.net/cb463ca4-2622-4a89-a34b-5c6becd9cc16#media-blob-url=true\&id=9a8e9a99-ce61-4702-ba60-f2ac69ca61c1\&collection=contentId-24215579\&contextId=24215579\&height=274\&width=865\&alt=)`1"tendermint.key": "ZYsBV9y3a6T1ie2vt8+bVjtv93pUcWqWSMWGORhLc1kKgCIhXLqKxxxbTD1HCQY0LPyoy081q9Q1HJQGDwfTYA==",`

    &#x20;
4.  **api.proxy.url** → URL to the seed node setuped previously\
    If you're testing with your **own nodes** use this **URL**

    `1"api.proxy.url": "http://127.0.0.1:5101/rpc"`

    if you are testing with the **public testnet** use this instead

    `1"api.proxy.url": "http://testnet.phantasma.io:5101/rpc"`
5.  **node.mode →** Either normal or proxy

    `1"node.mode": "normal"`
6.  **node.host →** change the port of the node, this will be the your rpc url

    `1"node.host": "http://*:5105"`

&#x20;

&#x20;

#### To run the node <a href="#to-run-the-node" id="to-run-the-node"></a>

To run the node compile it

`1dotnet build --project Phantasma.Node`

Then go to **Phantasma.Node/bin/Debug/net6.0/**

1. Add the previously configure file with your change and rename it to config.json

&#x20;

Before starting up the **Phantasma.Node** make sure that **Tendermint** is running

`1./phantasma-node --urls "http://*:5105" 2or 3dotnet phantasma-node.dll --urls "http://*:5105"`

&#x20;

### Notes <a href="#notes" id="notes"></a>

Also keep in mind if you have a Storage inside the **Phantasma.Node/bin/Debug/net6.0/**, just delete it before starting everything

Also keep in mind that you have to change the **node/data/priv\_validator\_state.json** to current chain settings.

There’s another thing to have in mind the **validator nodes** also have something in their configuration that limit the **number of connections** they can have, the **default** value is **4**, but you can change it on the **config.toml.** It’s at the end of the file

`1max_open_connections = 4 # Change this value to more than 4.`

&#x20;

#### Setup Tendermint from 0 to Hero ( This is just to use when setuping on the mainnet ) <a href="#setup-tendermint-from-0-to-hero-this-is-just-to-use-when-setuping-on-the-mainnet" id="setup-tendermint-from-0-to-hero-this-is-just-to-use-when-setuping-on-the-mainnet"></a>

This will create the node folder

`1tendermint init --home "/path/to/folder/"`

Then you just need to copy the **config.toml** from the **NodeExample** and change the value stated below.

Now just run the **node**

`1tendermint node --home "/path/to/folder/"`

&#x20;
