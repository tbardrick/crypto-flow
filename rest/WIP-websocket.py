# from web3 import Web3
# from secrets import API_KEY

# w3 = Web3(Web3.WebsocketProvider(f'wss://mainnet.infura.io/ws/v3/{API_KEY}', websocket_timeout=60))

# import time

# def handle_event(event):
#     print(event)

# def log_loop(event_filter, poll_interval):
#     while True:
#         for event in event_filter.get_new_entries():
#             handle_event(event)
#         time.sleep(poll_interval)

# def main():
#     block_filter = w3.eth.filter('latest')
#     log_loop(block_filter, 2)

# if __name__ == '__main__':
#     main()


# NOTE : WEB3_PROVIDER_URI - this needs the ws uri
# https://web3py.readthedocs.io/en/stable/filters.html

# waitForTransactionReceipt