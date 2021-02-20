# Blockchain_with_Python

In this repository we will be working with python to do several things related to crypto-currency and blockchain. We will first generate a Mnemonic key from the BIP39 website using the Bip44 Derivation pATH. FOR btctest COIN AND eTHEREUM (eth). 

We are using BIP44 because keys generated using this derivation path can be used in multiple wallets for multiple coin address types. 

After generating the mnemonic phrase we will create several function using python code:

Functions:
- def derive_wallets
- def priv_key_to_account
- def create_raw_tx
- def send_tx

Each of these functions has a purpose in this notebook. 

Derive wallets will derive address and private keys for a BTCTest wallet and an ETH wallet. 

Private Keys to Account will be used to obtain the private key for each coin from the list of coins printed from the derive wallet function.

Create Raw transaction and Send transaction will be used to create and send a transaction.

Using this code I was able to obtain the wallet coins for each crypto currency. However, I had a very difficult time funding my BTCtest wallet and did nto understand how to fund the Ethereum wallet. 
I provided several screen shots of the successful portion from the code that was used. 
However, I do understand what i need to work on in order to have code function properly.
