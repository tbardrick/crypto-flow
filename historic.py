import pymysql
from web3 import Web3
from secrets import (
    INFURA_PROJECT_ID_ETH,
    AWS_RDS_HOST,
    AWS_RDS_USER,
    AWS_RDS_PASSWORD,
)


def main():
    # connect to our infura node
    w3 = Web3(Web3.HTTPProvider(f'https://mainnet.infura.io/v3/{INFURA_PROJECT_ID_ETH}'))

    # check we are connected to our node
    assert w3.isConnected()

    # define end block
    end_block = w3.eth.get_block('latest').number

    # define start block
    start_block = end_block - 1

    # get all txn_hashes between these blocks
    txns_list = []
    for b in range(start_block, end_block):
        txns = w3.eth.get_block(b).transactions

        for t in txns:
            # get txn data
            txn_m = {k : w3.eth.get_transaction(t)[k] for k in ['blockNumber', 'hash', 'from', 'to', 'value', 'gas', 'gasPrice']}
            txn_r = {k : w3.eth.get_transaction_receipt(t)[k] for k in ['cumulativeGasUsed','gasUsed']}
            txn = {**txn_m, **txn_r}

            # rename txn fields
            txn["fromAddress"] = txn.pop("from")
            txn["toAddress"] = txn.pop("to")

            # convert bytes to hex string
            txn['hash'] = txn['hash'].hex()

            # store txn data
            txns_list.append(txn)

    # connect to RDS
    connection = pymysql.connect(
        host=AWS_RDS_HOST,
        user=AWS_RDS_USER,
        password=AWS_RDS_PASSWORD,
        database="eth",
        port=3306,
        cursorclass=pymysql.cursors.DictCursor,
    )

    with connection:
        with connection.cursor() as cursor:
            # drop existing transactions table
            sql = "DROP TABLE IF EXISTS transactions;"

            cursor.execute(sql)
            # connection.commit()

            # define table / schema
            sql = """
            CREATE TABLE transactions (
                blockNumber INT,
                hash VARCHAR(66),
                fromAddress VARCHAR(42),
                toAddress VARCHAR(42),
                value BIGINT,
                gas INT,
                gasPrice BIGINT,
                cumulativeGasUsed BIGINT,
                gasUsed INT,
                PRIMARY KEY (hash)
            )
            """

            cursor.execute(sql)
            # connection.commit()

            # insert txns into table
            columns = ", ".join(txns_list[0].keys())
            placeholders = ", ".join([f"%({k})s" for k in txns_list[0].keys()])
            sql = "INSERT INTO transactions ( %s ) VALUES ( %s )" % (columns, placeholders)
            cursor.executemany(sql, txns_list)

            # commit changes to RDS
            connection.commit()

            # query data from table
            sql = "SELECT * FROM transactions"
            cursor.execute(sql)
            result = cursor.fetchall()
            print(result)
    

if __name__ == '__main__':
    main()
