from logging.config import listen


class Node:
    def __init_(self):
        self.blockchain =[]


    def get_transaction_value(self):
        """Returns the input of the user.(a new transaction amount)"""
        # get the user input, transform

        tx_recipient = input('Enter the recipient of the transaction:  ')
        tx_amount = float(input('plz enter your transaction amount:  '))

        # This is a tuple, can also wrap it with paranthesis, worthless having empty paranthesis,
        return tx_recipient, tx_amount
        # when having one value "(tx_amount, )""


    def get_user_choice(self):
        user_input = input('Your choice:  ')
        return user_input


    def print_blockchain_elements(self):
        # output the blockchain list to the console
        for block in self.blockchain:
            print('Outputting block')
            print(block)
        else:
            print('-'*20)

    def listen_for_input(self):
        waiting_for_input = True


        while waiting_for_input:
            print('Please choose')
            print('1: Add a new transaction value ')
            print('2: Mine a new block ')
            print('3: Output the blockchain blocks ')
            print('4: Check transaction validity ')
            print('q: Quit')
            user_choice = self.get_user_choice()
            if user_choice == '1':
                tx_data = self.get_transaction_value()
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
                self.print_blockchain_elements()
            elif user_choice == '4':
                verifier = Verification()
                if verifier.verify_transactions(open_transactions, get_balance):
                    print('All transactions are valid!')
                else:
                    print('There are invalid transactions')
            elif user_choice == 'q':
                waiting_for_input = False
            else:
                print('Input was invalid, please pick a value from the list. ')
            verifier = Verification()
            if not verifier.verify_chain(blockchain):
                self.print_blockchain_elements()
                print('Invalid blockchain, please try again.')
                break
            # string formatting
            print('Balance of {}: {:6.2f}'.format('Isurika', get_balance('Isurika')))
        else:
            print('User left')

        print('Done!')
