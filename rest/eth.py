from web3 import Web3
import secrets
import sqlite3 as sq3

class ETHData():

    def __init__(self, project_id, start_block=0):
        # connect to our infura hosted eth node
        self.w3 = Web3(Web3.HTTPProvider(f'https://mainnet.infura.io/v3/{project_id}'))
        self.start_block = start_block

        # check we are connected to our node
        assert self.w3.isConnected()

    def get_blocks(self):
        # get up to the latest block
        latest_block = self.w3.eth.get_block('latest').number

        #  return blocks in range
        # for i in range(self.start_block, latest_block):
        #     yield self.w3.eth.get_block(i)

        # for testing
        for i in range(latest_block - 1, latest_block):
            yield self.w3.eth.get_block(i)
    
    def get_txns(self, block_list):

        # get transaction info for each block
        for b in block_list:
            return [self.w3.eth.get_transaction(t) for t in b['transactions']]

    def get_txn_receipts(self, block_list):

        # get transaction_receipt info for each block
        for b in block_list:
            return [self.w3.eth.get_transaction_receipt(t) for t in b['transactions']]

def main():
    
    eth = ETHData(
        secrets.WEB3_INFURA_PROJECT_ID_ETH
    )

    blocks = [*eth.get_blocks()]
    txns = eth.get_txns(blocks)
    txn_receipts = eth.get_txn_receipts(blocks)

    return blocks, txns, txn_receipts
    

if __name__ == '__main__':
    b, ts, trs = main()
    print(b, ts, trs)