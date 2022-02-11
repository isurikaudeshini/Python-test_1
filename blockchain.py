from functools import reduce  # gives access to reduce function
import hashlib as hl
import json
import pickle

from collections import OrderedDict

from hash_util import hash_string_256, hash_block
{
    "field": "value",
    "field1": [
        {}
    ]
}
# initializing the genesis block, very first one
MINING_REAWARD = 10
genesis_block = {
    'previous hash': '',
    'index': 0,
    'transactions': [],
    'proof': 100
}
blockchain = [genesis_block]
open_transactions = []
owner = 'Isurika'
# A "set" is initialized here, *mutable *unordered list * no duplicates *~only one type
participants = {'Isurika'}


def load_data():
    with open('blockchain.txt', mode='r') as f:
        # file_content = pickle.loads(f.read())
        file_content = f.readlines()
        
        global blockchain
        global open_transactions
        # blockchain = file_content['chain']
        # open_transactions = file_content['ot']
        blockchain = json.loads(file_content[0][:-1])
        updated_blockchain =[]
        for block in blockchain:
            updated_block = {
                'previous hash': block['previous_hash'],
                'index': block['index'],
                'proof': block['proof'],
                'transactions': [OrderedDict([('sender', tx['sender']), ('recipient', tx['recipient']), ('amount', tx ['amount'])]) for tx in block['transactions']]
            }
            updated_blockchain.append(updated_block)
        blockchain = updated_blockchain
        open_transactions = json.loads(file_content[1])
        updated_transactions = []
        for tx in open_transactions:
            updated_transactions = OrderedDict(
                [('sender', tx['sender']), ('recipient', tx['recipient']), ('amount', tx ['amount'])])
            updated_transactions.append(updated_transactions)
        open_transactions = updated_transactions


#load_data()

def save_data():
    with open('blockchain.txt', mode='w') as f:
        f.write(json.dumps(blockchain))
        f.write('\n')
        f.write(json.dumps(open_transactions))
        # save_data = {
        #     'chain': blockchain,
        #     'ot' : open_transactions
        # }
        # f.write(pickle.dumps(save_data))


def valid_proof(transactions, last_hash, proof):
    guess = (str(transactions) + str(last_hash) + str(proof)).encode()
    print(guess)
    guess_hash = hash_string_256(guess)
    print(guess_hash)
    return guess_hash[0:2] == '00'


def proof_of_work():
    last_block = blockchain[-1]
    last_hash = hash_block(last_block)
    proof = 0
    while not valid_proof(open_transactions, last_hash, proof):
        proof += 1
    return proof


def get_balance(participant):
    tx_sender = [[tx['amount'] for tx in block['transactions']
                  if tx['sender'] == participant] for block in blockchain]
    open_tx_sender = [tx['amount']
                      for tx in open_transactions if tx['sender'] == participant]
    tx_sender.append(open_tx_sender)
    print(tx_sender)
    amount_sent = reduce(lambda tx_sum, tx_amt: tx_sum + sum(tx_amt)
                         if len(tx_amt) > 0 else tx_sum + 0, tx_sender, 0)

    tx_recipient = [[tx['amount'] for tx in block['transactions']
                     if tx['recipient'] == participant] for block in blockchain]
    amount_received = reduce(lambda tx_sum, tx_amt: tx_sum + sum(tx_amt)
                             if len(tx_amt) > 0 else tx_sum + 0, tx_recipient, 0)

    return amount_received - amount_sent


def get_last_blockchain_value():
    """Returns the last value of the current block chain"""
    if len(blockchain) < 1:
        return None
    return blockchain[-1]


def verify_transaction(transaction):
    sender_balance = get_balance(transaction['sender'])
    return sender_balance >= transaction['amount']


def add_transaction(recipient, sender=owner, amount=1.0):
    """Append a new value as well as the last blockchain value to the blockchain

    Arguments:
        :sender: The sender of the coins
        :recipient: The recipient of the coins
        :amount: The amount of coins sent with the transaction (default 1.0)
    """
    # transaction = {
    #     'sender': sender,
    #     'recipient': recipient,
    #     'amount': amount
    # }  # A dictionary has been used to store transaction data
    transaction = OrderedDict(
        [('sender', sender), ('recipient', recipient), ('amount', amount)])
    if verify_transaction(transaction):
        open_transactions.append(transaction)
        participants.add(sender)
        participants.add(recipient)
        save_data()
        return True
    return False


def mine_block():
    last_block = blockchain[-1]
    # list comprehensions, using a for loop
    hashed_block = hash_block(last_block)
    proof = proof_of_work()
    # reward_transaction ={
    #     'sender' :'MINING',
    #     'recipient' : owner,
    #     'amount' : MINING_REAWARD
    # }
    reward_transaction = OrderedDict(
        [('sender', 'MINING'), ('recipient', owner), ('amount', MINING_REAWARD)])

    copied_transactions = open_transactions[:]
    copied_transactions.append(reward_transaction)

    # for key in last_block:
    #     value = last_block[key]
    #     hashed_block = hashed_block + str(value)

    block = {
        'previous_hash': hashed_block,
        'index': len(blockchain),
        'transactions': copied_transactions,
        'proof': proof
    }
    blockchain.append(block)
    return True


def get_transaction_value():
    """Returns the input of the user.(a new transaction amount)"""
    # get the user input, transform

    tx_recipient = input('Enter the recipient of the transaction:  ')
    tx_amount = float(input('plz enter your transaction amount:  '))

    # This is a tuple, can also wrap it with paranthesis, worthless having empty paranthesis,
    return tx_recipient, tx_amount
    # when having one value "(tx_amount, )""


def get_user_choice():
    user_input = input('Your choice:  ')
    return user_input


def print_blockchain_elements():
    # output the blockchain list to the console
    for block in blockchain:
        print('Outputting block')
        print(block)
    else:
        print('-'*20)


def verify_chain():
    """ verify the current blockchain and return True if it is valid"""
    for (index, block) in enumerate(blockchain):
        if index == 0:
            continue
        if block['previous_hash'] != hash_block(blockchain[index-1]):
            return False
        if not valid_proof(block['transactions'][:-1], block['previous_hash'], block['proof']):
            print('Proof of work is invalid')
            return False
    return True


def verify_transactions():
    return all([verify_transaction(tx) for tx in open_transactions])

    #     if block_index == 0:
    #         block_index += 1
    #         continue
    #     elif block[0] == blockchain[block_index -1 ]:
    #         is_valid = True
    #     else:
    #         is_valid = False
    #         break
    #     block_index += 1
    return is_valid


waiting_for_input = True

while waiting_for_input:
    print('Please choose')
    print('1: Add a new transaction value ')
    print('2: Mine a new block ')
    print('3: Output the blockchain blocks ')
    print('4: Output participants')
    print('5: Check transaction validity ')
    print('h: Manipulate the chain ')
    print('q: Quit')
    user_choice = get_user_choice()
    if user_choice == '1':
        tx_data = get_transaction_value()
        recipient, amount = tx_data  # unpacking the tuple
        if add_transaction(recipient, amount=amount):
            print('Added transaction')
        else:
            print('Transaction failed!')
        print(open_transactions)
    elif user_choice == '2':
        if mine_block():
            open_transactions = []
            save_data()
    elif user_choice == '3':
        print_blockchain_elements()
    elif user_choice == '4':
        print(participants)
    elif user_choice == '5':
        if verify_transactions():
            print('All transactions are valid!')
        else:
            print('There are invalid transactions')
    elif user_choice == 'h':
        if len(blockchain) >= 1:
            blockchain[0] = {
                'previous hash': '',
                'index': 0,
                'transactions': [{'sender': 'Chris', 'recepient': 'Isurika', 'amount': 100}]
            }
    elif user_choice == 'q':
        waiting_for_input = False
    else:
        print('Input was invalid, please pick a value from the list. ')
    if not verify_chain():
        print_blockchain_elements()
        print('Invalid blockchain, please try again.')
        break
    # string formatting
    print('Balance of {}: {:6.2f}'.format('Isurika', get_balance('Isurika')))
else:
    print('User left')

print('Done!')
