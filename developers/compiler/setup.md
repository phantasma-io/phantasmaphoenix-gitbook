---
description: Basic setup of the Phoenix Smart Language Compiler
---

# Setup

## Recommended installation

Install `pha-tomb` as a .NET global tool:

```bash
dotnet tool install --global pha-tomb
dotnet tool update --global pha-tomb
```

Verify the install:

```bash
pha-tomb --version
pha-tomb --help
```

## Build from source

If you want to pin a local compiler build, work on the compiler itself, or avoid whichever global `pha-tomb` is currently first in `PATH`, build it from source.

Source repository:
- `https://github.com/phantasma-io/TOMB`

Basic source build:

```bash
git clone https://github.com/phantasma-io/TOMB
cd TOMB
dotnet build TombCompiler.sln
```

Published build:

```bash
dotnet publish Compiler/TombCompiler.csproj -c Release
```

Current project notes:
- executable name: `pha-tomb`
- target framework: `net10.0`
- source extension: `.tomb`

## Add the compiler to PATH

This is useful when you want to invoke `pha-tomb` directly without a full path.

### Windows

Add the directory containing `pha-tomb.exe` to `Path`.

1. Right-click on the Start Button
2. Select “System” from the context menu.
3. Click “Advanced system settings”
4. Go to the “Advanced” tab
5. Click “Environment Variables…”
6. Click variable called “Path” and click “Edit…”
7. Click “New”
8. Enter the path to the folder containing `pha-tomb.exe`

Example:

```shell
pha-tomb my_contract.tomb
```

### Linux & MacOS

Add the directory containing `pha-tomb` to `PATH`.

Example:

```bash
export PATH="$PATH:/path/to/pha-tomb-directory"
```

Then you can run:

```bash
pha-tomb my_contract.tomb
```

## Using a pinned compiler with pha-deploy

When using `pha-deploy contract compile`, you can pin an exact compiler binary instead of relying on `PATH`.

Use either:

```bash
pha-deploy contract compile --compiler /path/to/pha-tomb ...
```

or:

```bash
export PHA_TOMB_PATH=/path/to/pha-tomb
```
