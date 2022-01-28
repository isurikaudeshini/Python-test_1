blockchain = []

def get_last_blockchain_value():
    return blockchain[-1]

def add_value(transaction_amount,last_transaction):
    blockchain.append([last_transaction,transaction_amount])
    print(blockchain)

add_value(2,[1])
add_value(10, get_last_blockchain_value())
add_value(0.2,get_last_blockchain_value())
