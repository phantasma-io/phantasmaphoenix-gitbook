# 🚠 Run the Docker Node



Dive into the specifics of getting the chain up and running on your machine!

{% hint style="info" %}
**Dev Tip:** Just running the docker container it's easier and simple if you just want to get you local node running.
{% endhint %}

### Requirements

1. Have **Docker** installed.

## Install & Run

Let's get it to run.&#x20;

1. Open the terminal & type `docker pull phantasmachain/phantasma-devnet`
2.  Now depending on if you have the docker application or not, you can use this command to start it up by

    ```
    docker run --name phantasma-devnet -tid -p 5102:5102 -p 5101:5101 -p 5103:5103 -p 5104:5104 -p 26057:26057 phantasmachain/phantasma-devnet
    ```
3. Or by going to the Docker Application, do the following steps



### Docker Application

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

## Check that everything is working

To check if everything is working

{% hint style="info" %}
**How can I check that it's live?**

Go to this url [http://127.0.0.1:5101/swagger](http://127.0.0.1:5101/swagger)

If it returns something like this, it should be working!&#x20;
{% endhint %}

<figure><img src="../../.gitbook/assets/Screenshot 2022-10-19 at 09.51.41.png" alt=""><figcaption><p>Swagger Response</p></figcaption></figure>
