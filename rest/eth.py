from web3 import Web3
import secrets
import sqlite3 as sq3

# connect to our infura hosted eth node
w3 = Web3(Web3.HTTPProvider(f'https://mainnet.infura.io/v3/{secrets.WEB3_INFURA_PROJECT_ID_ETH}'))

# check we are connected to our node
assert w3.isConnected()

# get blocks from 'start_block'
start = w3.eth.get_block('latest').number - 1

def get_blocks(start_block=0):
    # get latest completed block
    latest_block = w3.eth.get_block('latest')

    #  return blocks in range
    for i in range(start_block, latest_block.number):
        yield w3.eth.get_block(i)

blocks = [*get_blocks(start_block = start)]

# get transaction info for each block
for b in blocks:
    ts = [w3.eth.get_transaction(t) for t in b['transactions']]
    trs = [w3.eth.get_transaction_receipt(ts) for ts in b['transactions']]
    print(ts)
