# Python SDK Setup

The Python SDK package is `phantasma-sdk-py`. Its import namespace is
`phantasma_py`.

## Requirements

- Python 3.11 or newer.
- Runtime dependencies from the package metadata:
  - `cryptography>=42`
  - `requests>=2.32`

## Install

```bash
pip install phantasma-sdk-py
```

Verify that the import namespace is available:

```bash
python - <<'PY'
import phantasma_py

print(phantasma_py.__version__)
PY
```

## Local Development

The SDK repository uses `uv`, `just`, `ruff`, `mypy`, and `pytest` for local
development.

```bash
git clone https://github.com/phantasma-io/phantasma-sdk-py.git
cd phantasma-sdk-py
uv sync --extra dev
just check
```

The source `just check` gate runs formatting, lint, strict typing, tests, and
package build checks.

## Endpoint Selection

`PhantasmaRPC.mainnet()` and `PhantasmaRPC.testnet()` are convenience
constructors. You can also pass an explicit endpoint:

```python
from phantasma_py.rpc import PhantasmaRPC

rpc = PhantasmaRPC("http://localhost:5172/rpc")
```

For scripts and examples, prefer environment variables so endpoint choices and
addresses stay outside source files:

```bash
export PHANTASMA_RPC="http://localhost:5172/rpc"
export PHANTASMA_ADDRESS="P..."
```

Never hard-code private keys or WIF values in documentation, examples, or
application source.
