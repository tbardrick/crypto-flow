import secrets
from infura import InfuraData
from database import BlockchainDB
import os

def main():

    # get eth data
    eth = InfuraData(
        secrets.WEB3_INFURA_PROJECT_ID_ETH
    )

    blocks = [*eth.get_blocks()]
    print(blocks[0])
    txns = eth.get_txns(blocks)
    txn_receipts = eth.get_txn_receipts(blocks)

    # create / update database tables with data
    db_name = 'ethereum.db'
    db_is_new = not os.path.exists(db_name)

    with BlockchainDB(db_name) as db:

        if db_is_new:
            print('Creating a new DB.')
            db.create_tables()
            db.create_index()
            db.update_database(blocks, txns, txn_receipts)
        
        else:
            db.update_database(blocks, txns, txn_receipts)

        print(db.sample_query("SELECT * FROM blocks LIMIT 5"))


if __name__ == '__main__':
    main()