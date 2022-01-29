blockchain = []


def get_last_blockchain_value():
    """Returns the last value of the current block chain"""
    return blockchain[-1]


def add_value(transaction_amount, last_transaction=[-1]):
    """Append a new value as well as the last blockchain value to the blockchain

    Arguments:
        :transaction_amount :the amount that should be added

        :last_transaction : the last blockchain transaction.(default[1])
        """
    blockchain.append([last_transaction, transaction_amount])


def get_user_input():
    """Returns the input of the user.(a new transaction amount)"""
    return float(input('plz enter your transaction amount'))


tx_amount = get_user_input()
add_value(tx_amount)
tx_amount = get_user_input()
add_value(last_transaction=get_last_blockchain_value(),
          transaction_amount=tx_amount)   #Command pallete-> format doc (structured with indentation)
tx_amount = get_user_input()
add_value(tx_amount, get_last_blockchain_value())

print(blockchain)


#output the blockchain list to the console
for block in blockchain:
    print('Outputting block')
    print(block)

print('Done!')