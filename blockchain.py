blockchain = [[1]]

def get_last_blockchain_value():
    return blockchain[-1]

def add_value():
    blockchain.append([get_last_blockchain_value(), 5])
    print(blockchain)

add_value()
add_value()
add_value()