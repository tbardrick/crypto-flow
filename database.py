import sqlite3 as sq3
import os

class BlockchainDB():

    def __init__(self, db_name):
        self.db_name = db_name

    def __enter__(self):
        self.conn = sq3.connect(self.db_name) 
        self.cur = self.conn.cursor()
        return self

    def create_tables(self):
        """ create the schema for the database"""

        blocks_query = """
            CREATE TABLE IF NOT EXISTS blocks (
                number INTEGER PRIMARY KEY,
                size INTEGER,
                timestamp INTEGER,
                miner TEXT,
                gasLimit INTEGER,
                gasUsed INTEGER,
                -- transactions TEXT,
                parentHash TEXT,
                hash TEXT,
                extraData TEXT,
                difficulty TEXT,
                totalDifficulty TEXT,
                nonce TEXT,
                mixHash TEXT,
                uncles TEXT,
                sha3Uncles TEXT,
                receiptsRoot TEXT, 
                stateRoot TEXT,
                transactionsRoot TEXT, 
                logsBloom TEXT
                );

            """
        self.cur.execute(blocks_query)
        
        txns_query = """
            CREATE TABLE IF NOT EXISTS txns (
                blockHash TEXT,
                blockNumber INTEGER,
                hash TEXT PRIMARY KEY,
                fromAddress TEXT,
                toAddress TEXT,
                value INTEGER,
                gas INTEGER,
                gasPrice INTEGER,
                nonce INTEGER,
                r TEXT, 
                s TEXT, 
                v INTEGER,
                input TEXT,
                transactionIndex INTEGER
                );
            """
        self.cur.execute(txns_query)

        txn_receipts_query = """
            CREATE TABLE IF NOT EXISTS txn_receipts ( 
                blockHash TEXT,
                blockNumber INTEGER,
                contactAddress TEXT,
                cumulativeGasUsed INTEGER,
                fromAddress TEXT,
                gasUsed INTEGER,
                logs TEXT,
                logsBloom TEXT,
                status INTEGER,
                toAddress TEXT,
                transactionHash TEXT,
                transactionIndex INTEGER
                );
            """
        self.cur.execute(txn_receipts_query)

    def create_index(self):
        blocks_idx_query = "CREATE INDEX index_blocks ON blocks(timestamp);"
        self.cur.execute(blocks_idx_query)
        txns_idx_query = "CREATE INDEX index_txns ON txns(blockNumber);"
        self.cur.execute(txns_idx_query)
        txn_receipts_idx_query = "CREATE INDEX index_quick ON txn_receipts(blockNumber);"
        self.cur.execute(txn_receipts_idx_query)

        
    def update_database(self, blocks_data, txns_data, txn_receipts_data):
        """ write lists of dictionaries into the database"""

        blocks_query = """
            INSERT INTO blocks VALUES (
                :number,
                :size,
                :timestamp,
                :miner,
                :gasLimit,
                :gasUsed,
                -- :transactions,
                :parentHash,
                :hash,
                :extraData,
                :difficulty,
                :totalDifficulty,
                :nonce,
                :mixHash,
                :uncles,
                :sha3Uncles,
                :receiptsRoot, 
                :stateRoot,
                :transactionsRoot, 
                :logsBloom
                ); 
            """
        self.cur.executemany(blocks_query, blocks_data)

        txns_query = """
            INSERT INTO txns VALUES (
                :blockHash,
                :blockNumber,
                :hash,
                :fromAddress,
                :toAddress,
                :value,
                :gas,
                :gasPrice,
                :nonce,
                :r, 
                :s, 
                :v
                ); 
            """
    
        self.cur.executemany(txns_query, txns_data)

        txn_receipts_query = """
            INSERT INTO txn_receipts VALUES (
                :blockHash,
                :blockNumber,
                :contactAddress,
                :cumulativeGasUsed,
                :fromAddress,
                :gasUsed,
                :logs,
                :logsBloom,
                :status,
                :toAddress,
                :transactionHash,
                :transactionIndex
                ); 
            """

        self.cur.executemany(txn_receipts_query, txn_receipts_query)

    def sample_query(self, query):

        self.cur.execute(query)
        a = self.cur.fetchall() 
        return a


    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.commit()
        self.conn.close()


# def main():
#     db_name = 'ethereum.db'
#     db_is_new = not os.path.exists(db_name)

#     with BlockchainDB(db_name) as db:

#         if db_is_new:
#             print('Creating a new DB.')
#             db.create_tables()
#             db.create_index()
#             db.update_database(cur, table_quick, table_tx, table_block)
#         else:
#             db.update_database(cur,table_quick, table_tx, table_block)


# if __name__ == '__main__':
#     main()