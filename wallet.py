import subprocess
from subprocess import Popen,PIPE
import json
from web3 import Web3
from constants import BTCTEST
from constants import ETH
from constants import BTC
from pprint import pprint
from bit import PrivateKeyTestnet
from bit.network import NetworkAPI
from web3 import Web3, middleware, Account
from web3.gas_strategies.time_based import medium_gas_price_strategy
from web3.middleware import geth_poa_middleware
import os
from web3.auto.gethdev import w3
from bit import wif_to_key
from dotenv import load_dotenv
from getpass import getpass
from eth_account import Account
load_dotenv()

#Connecting Web3 to port 8545:
w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))
w3.middleware_onion.inject(geth_poa_middleware, layer=0)

# Put my mnemonic key in an ENV file for protected access to keys:
mnemonic = os.getenv('MNEMONIC')

# Created function that lets me print multiple BTCTEST and ETH coin addresses and private keys:
def derive_wallets(coin=BTC, mnemonic=mnemonic, depth=3):
    p = subprocess.Popen(
        f"php derive  -g --mnemonic='{mnemonic}' --coin={coin} --numderive={depth} --format=json",
        stdout=subprocess.PIPE,
        shell=True)
    output, err = p.communicate()
    p_status = p.wait()
    keys = json.loads(output)
    return keys

coins = {
    ETH: derive_wallets(ETH),
    BTCTEST: derive_wallets(BTCTEST)
}

#print(coins)

#print(f"Ethereum Private Key {coins[ETH][0]['privkey']}"
#print(f"Bitcoin Private Key {coins[BTCTEST][0]['privkey']}"

#Selects account for each coin:
def priv_key_to_account(coin, priv_key):
    if coin == ETH:
       return Account.privateKeyToAccount(priv_key)
    elif coin == BTCTEST:
       return PrivateKeyTestnet(priv_key)

account_one = priv_key_to_account(BTCTEST, coins[BTCTEST][1]['privkey'])
account_two = priv_key_to_account(ETH, coins[ETH][1]['privkey'])


# The following function will be used to transact between addresses of commoon coins:
def create_raw_tx(coin, account, recipient, amount):
    if coin == ETH:
        gasEstimate = w3.eth.estimateGas(
            {"from": account.address, "to": recipient, "value": amount}
        )
        return {
            "from": account.address,
            "to": recipient,
            "value": amount,
            "gasPrice": w3.eth.gasPrice,
            "gas": gasEstimate,
            "nonce": w3.eth.getTransactionCount(account.address),
            "chainId": w3.net.chainId,
        }
    elif coin == BTCTEST:
        return PrivateKeyTestnet.prepare_transaction(account.address, [(recipient, amount, BTC)])

def send_tx(coin, account, to, amount):
    tx = create_tx(coin, account, to, amount)
    signed_tx = account.sign_transaction(tx)
    if coin == ETH:
        return w3.eth.sendRawTransaction(signed.rawTransaction)
    elif coin == BTCTEST:
        return NetworkAPI.broadcast_tx_testnet(signed_tx)

# Use the below to insert private key here
### Need to add variables to pull keys:
#  = wif_to_key()
#  = wif_to_key()


print(coins)
print(coins[ETH][1]['privkey'])
print(coins[BTCTEST][2]['address'])

#print(account_one)
#print(account_two)

# print(.get_balance("btc"))
# print(.balance_as("usd"))
# print(.get_transactions())

