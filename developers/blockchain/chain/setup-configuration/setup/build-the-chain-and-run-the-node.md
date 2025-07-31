# 🛠️ Build the Chain & Run the Node

Dive into the specifics of getting the chain up and running on your machine!

## Install the chain

1. Download / clone the repository [`https://github.com/phantasma-io/phantasma-ng`](https://github.com/phantasma-io/phantasma-ng)&#x20;
2. Extract it (if you downloaded)
3. Go to the folder and open a terminal there
4.  Run

    <pre class="language-bash" data-overflow="wrap"><code class="lang-bash"><strong>dotnet publish
    </strong></code></pre>

{% hint style="success" %}
That's it, you have the compiler ready!

Now you can add it to the path.
{% endhint %}



## Compiling the docker

1.  Run the command accordingly to your operating system.

    <pre class="language-bash" data-overflow="wrap"><code class="lang-bash"><strong>./build-docker.sh // Linux
    </strong><strong>./build-docker-windows.bat // Windows
    </strong><strong>./build-docker-macos-arm64.sh // MacOS ARM64
    </strong><strong>./build-docker-macos-amd64.sh // MacOS AMD64
    </strong></code></pre>
2. After the command run, you can go to the docker hub and see your new image there.



## Running the Chain

To run the chain there's to possible way's, from the terminal or from the Docker UI

### Docker UI

Inside the Docker Desktop, after building the docker image, go to **Images**

<figure><img src="../../.gitbook/assets/Screenshot 2022-10-19 at 09.47.44.png" alt=""><figcaption></figcaption></figure>

On Images, selected the desired image and **Run**

<figure><img src="../../.gitbook/assets/Screenshot 2022-10-19 at 09.44.27.png" alt=""><figcaption></figcaption></figure>



<figure><img src="../../.gitbook/assets/Screenshot 2022-10-19 at 09.47.17.png" alt=""><figcaption><p>Run Button on the image</p></figcaption></figure>

Configure the docker container with an identical configuration

<figure><img src="../../.gitbook/assets/Screenshot 2022-10-19 at 09.45.52.png" alt=""><figcaption></figcaption></figure>

{% hint style="success" %}
Now you'll have your chain instance running!
{% endhint %}

{% hint style="info" %}
**How can I check that it's live?**

Go to this url [http://127.0.0.1:5101/swagger](http://127.0.0.1:5101/swagger)

If it returns something like this, it should be working!&#x20;
{% endhint %}

<figure><img src="../../.gitbook/assets/Screenshot 2022-10-19 at 09.51.41.png" alt=""><figcaption><p>Swagger Response</p></figcaption></figure>

<figure><img src="../../.gitbook/assets/Screenshot 2022-10-19 at 10.03.54.png" alt=""><figcaption></figcaption></figure>

### Terminal

After compiling the docker image, you can run the chain with this command.

Depending on the OS that you're using, you can run the command accordingly

```bash
# For Windows
./testnet-startup-windows.bat

# For Linux / MacOS (Intel)
./testnet-startup.sh

# For Linux ARM64/ MacOS
./testnet-startup-arm64.sh 
```

{% hint style="info" %}
**How can I check that it's live?**

Go to this url [http://127.0.0.1:5101/swagger](http://127.0.0.1:5101/swagger)

If it returns something like this, it should be working!&#x20;
{% endhint %}



<figure><img src="../../.gitbook/assets/Screenshot 2022-10-19 at 09.51.41.png" alt=""><figcaption><p>Swagger Response</p></figcaption></figure>

