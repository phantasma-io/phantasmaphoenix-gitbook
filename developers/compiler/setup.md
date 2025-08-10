---
description: Basic setup of the Phoenix Smart Language Compiler
---

# Setup

## Phoenix Smart Language Compiler Installation

1. Download / clone the repository [https://github.com/phantasma-io/TOMB/tree/tomb-ng](https://github.com/phantasma-io/TOMB/tree/tomb-ng)
2. Extract it (if you downloaded)
3. Go to the folder and open a terminal there
4.  Run

    <pre class="language-bash" data-overflow="wrap"><code class="lang-bash"><strong>dotnet publish
    </strong></code></pre>

{% hint style="success" %}
That's it, you have the compiler ready!

Now you can add it to the path.
{% endhint %}

## Phoenix Smart Language Compiler to PATH

{% hint style="info" %}
**Setup Phoenix Smart Language Compiler to the PATH**

It's really helpful, so you don't need to always specify the full path to the folder if you have the Phoenix Smart Language compiler in the path
{% endhint %}

### Windows

On Windows what you should do is:

1. Right-click on the Start Button
2. Select “System” from the context menu.
3. Click “Advanced system settings”
4. Go to the “Advanced” tab
5. Click “Environment Variables…”
6. Click variable called “Path” and click “Edit…”
7. Click “New”
8. Enter the path to the folder containing the binary you want on your PATH. To add: C:\PathToPSLC\Compiler\bin\Debug\net6.0\publish

Now you can do something like&#x20;

```shell
PslCompiler.exe myPslContract.psl // From everywhere on Windows
```

### Linux & MacOS

On Linux and MacOS:

1. On the terminal
2. ```bash
   export PATH=$PATH:/pathToPslCompiler/Compiler/bin/Debug/net6.0/publish
   ```
3. That's it.

```shell
./PslCompiler.dll myPslContract.psl // From everywhere on Linux/Mac
```

For more information

{% embed url="https://www.baeldung.com/linux/path-variable" %}

