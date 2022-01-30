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


def get_transaction_value():
    """Returns the input of the user.(a new transaction amount)"""
    user_input = float(input('plz enter your transaction amount:  '))

    return user_input


def get_user_choice():
    user_input = input('Your choice:  ')
    return user_input


def print_blockchain_elements():
    # output the blockchain list to the console
    for block in blockchain:
        print('Outputting block')
        print(block)
    


#Get the first transaction input and add the value to the blockchain
tx_amount = get_transaction_value()
add_value(tx_amount)

while True:
    print('Please choose')
    print('1: Add a new transaction value ')
    print('2: Output the blockchain blocks ')
    print('q: Quit')
    user_choice = get_user_choice()
    if user_choice == '1':
        tx_amount = get_transaction_value()
        add_value(tx_amount, get_last_blockchain_value())
    elif user_choice == '2':
        print_blockchain_elements()
    elif user_choice == 'q':
        break
    else:
        print('Input was invalid, please pick a value from the list. ')
    print('Choice registered')


print('Done!')
