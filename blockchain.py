blockchain = [[1]]

def get_last_blockchain_value():
    return blockchain[-1]

def add_value(transaction_amount):
    blockchain.append([get_last_blockchain_value(), 5])
    print(blockchain)

add_value(2)
add_value(10)
add_value(0.2)

