# Quick Start

Ecosystem Plugin for Harmony support in Ape

## Dependencies

* [python3](https://www.python.org/downloads) version 3.8 or greater, python3-dev

## Installation

### via `ape`

You can install this plugin using `ape`:

```bash
ape plugins install harmony
```

or via config file:

```yaml
# ape-config.yaml
plugins:
  - name: harmony
```

### via `pip`

You can install the latest release via [`pip`](https://pypi.org/project/pip/):

```bash
pip install ape-harmony
```

### via `setuptools`

You can clone the repository and use [`setuptools`](https://github.com/pypa/setuptools) for the most up-to-date version:

```bash
git clone https://github.com/ApeWorX/ape-harmony.git
cd ape_harmony
python3 setup.py install
```

## Quick Usage

Installing this plugin adds support for the Harmony ecosystem:

```bash
ape console --network harmony:mainnet
```
