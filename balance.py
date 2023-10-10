from web3 import Web3, HTTPProvider
from web3.middleware import geth_poa_middleware

eth_node_url = "https://nova.arbitrum.io/rpc"

# Connect to Ethereum network
w3 = Web3(HTTPProvider(eth_node_url))
w3.middleware_onion.inject(geth_poa_middleware, layer=0)

def get_balance(private_key):
    # Get the wallet address from the private key
    wallet_address = w3.eth.account.from_key(private_key).address

    # Get the balance of the wallet in Wei
    balance_wei = w3.eth.get_balance(wallet_address)

    # Convert the balance to Ether
    balance_eth = w3.fromWei(balance_wei, 'ether')

    return balance_eth

# Read private keys from file
with open('private-keys2.txt', 'r') as file:
    private_keys = [line.strip() for line in file]

# Get balances and write them to a new file
with open('balances.txt', 'w') as file:
    for private_key in private_keys:
        balance = get_balance(private_key)
        file.write(f"Balance of the wallet with private key {private_key} is {balance} Ether.\n")
