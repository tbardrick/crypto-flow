# crypto-flow

## Getting started

### Install Requirements

In order to start, you should have installed:

- Python 3.7

It is recommended to use a clean virtual environment with `virtualenv` or `pyenv`

To install all necessary requirements:

```(sh)
$ pip install --upgrade pip
$ pip install -r requirements.txt
```

### Configure Secrets

For security reasons, we do not want to commit any secrets (we consider any API Keys as secrets).

- infura
From [infura](https://infura.io) create your API key to access hosted ETH node.
Create`secrets.py` inside `/eth` directory.
Define variable `API_KEY = <INSERT YOUR API KEY>` inside `secret.py`.