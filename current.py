import pymysql
from web3 import Web3
from secrets import (
    INFURA_PROJECT_ID_ETH,
    AWS_RDS_HOST,
    AWS_RDS_USER,
    AWS_RDS_PASSWORD,
)

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
        # query data from table
        sql = "SELECT MAX(blockNumber) FROM transactions"
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)

        sql = "SELECT MIN(blockNumber) FROM transactions"
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)