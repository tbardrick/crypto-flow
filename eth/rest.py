from web3 import Web3
from secrets import API_KEY

# connect to our infura hosted eth node
w3 = Web3(Web3.HTTPProvider(f'https://mainnet.infura.io/v3/{API_KEY}'))

def get_blocks(start_block=0):
    # get latest completed block
    latest_block = w3.eth.get_block('latest')

    #  return blocks in range
    for i in range(start_block, latest_block.number):
        yield w3.eth.get_block(i)


def get_trans(block):
    # get transacions for a block
    for j in range(len(block.transactions)):
        return w3.eth.getTransactionByBlock(block.hash, j)

# test start
start = w3.eth.get_block('latest').number - 1

all_blocks = [*get_blocks(start_block = start)]

all_transactions = [get_trans(b) for b in all_blocks]
print(all_transactions)