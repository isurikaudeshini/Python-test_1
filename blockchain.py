blockchain = []

def get_last_blockchain_value():
    return blockchain[-1]

def add_value(transaction_amount,last_transaction=[-1]):
    blockchain.append([last_transaction,transaction_amount])
    
tx_amount = float(input('plz enter your transaction amount'))
add_value(tx_amount)
tx_amount = float(input('plz enter your transaction amount'))
add_value(tx_amount, get_last_blockchain_value())
tx_amount = float(input('plz enter your transaction amount'))
add_value(tx_amount,get_last_blockchain_value())

print(blockchain)
