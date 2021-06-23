# crypto-flow

## Getting started

### Install Requirements

In order to start, you should have installed:

- Python 3.7

It is recommended to use a clean virtual environment with `virtualenv`.

To install all necessary requirements:

```(sh)
$ pip install --upgrade pip
$ pip install -r requirements.txt
```

### Activating `virtualenv`
```(sh)
# Install virtualenv if it is not available:
$ which virtualenv || pip install --upgrade virtualenv

# *If* the above command displays an error, you can try installing as root:
$ sudo pip install virtualenv

# Create a virtual environment:
$ virtualenv -p python3 ~/.venv-py3

# Activate your new virtual environment:
$ source ~/.venv-py3/bin/activate

# With virtualenv active, make sure you have the latest packaging tools
$ pip install --upgrade pip setuptools

# Now we can install web3.py...
$ pip install --upgrade web3
```

Each new terminal session requires you to reactivate your `virtualenv`.

### Configure Secrets

For security reasons, we do not want to commit any secrets (we consider any API Keys as secrets).

- infura

From [infura](https://infura.io) create your API key to access hosted ETH node.

Create`secrets.py` inside `/eth` directory.

Define variable `API_KEY = <INSERT YOUR API KEY>` inside `secret.py`.