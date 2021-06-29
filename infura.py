from web3 import Web3
import secrets

class InfuraData():

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
            yield dict(self.w3.eth.get_block(i))

            # what to do if only one block in update - assert?
    
    def get_txns(self, block_list):

        # get transaction info for each block
        for b in block_list:
            return [dict(self.w3.eth.get_transaction(t)) for t in b['transactions']]

    def get_txn_receipts(self, block_list):

        # get transaction_receipt info for each block
        for b in block_list:
            return [dict(self.w3.eth.get_transaction_receipt(t)) for t in b['transactions']]

def main():

    eth = InfuraData(
        secrets.WEB3_INFURA_PROJECT_ID_ETH
    )

    blocks = [*eth.get_blocks()]
    txns = eth.get_txns(blocks)
    txn_receipts = eth.get_txn_receipts(blocks)

    print(dir(blocks[0]), dir(txns[0]), dir(txn_receipts[0]))
    

if __name__ == '__main__':
    main()