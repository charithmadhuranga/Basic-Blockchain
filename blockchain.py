''' Blockchain List '''
blockchain = []

''' Returning User Inputs '''
def user_input_transaction():
    tx_amount=float(input("Enter transaction value:"))
    return tx_amount

''' Returning the last blockchain Value '''
def last_transaction():
    if len(blockchain)<1:
        return None
    return blockchain[-1]

''' Adding blocks to the Chain '''
def add_transaction(tx_amount,last_transaction_amount=[1]):
    if last_transaction_amount==None:
        last_transaction_amount=[1]
    blockchain.append([last_transaction_amount,tx_amount])

''' Printing the blockchain elements '''
def printing_blockchain():
    for block in blockchain:
        print("printing blockchain")
        print(block)
        print('-'*20)

''' getting user choice '''
def get_user_choice():
    user_choice=input("Enter your choice:")
    return user_choice

'''verifying the blockchain to prevent manupilations'''
def verify_blockchain():
    #blockchain_index=0
    is_valid=True
    for blockchain_index in range(len(blockchain)):
        if blockchain_index==0:
            continue
        elif blockchain[blockchain_index][0]==blockchain[blockchain_index-1]:
            is_valid=True
        else:
            is_valid=False
            break
    return is_valid
        


''' Adding the genises block '''
add_transaction(user_input_transaction())


'''Infinite loop '''
while True:
    '''Printing the menu'''
    print("1.Add transaction")
    print("2.Print the blockchain")
    print("h.Manupilate the blockchain")
    print("q.exit")
    user_choice=get_user_choice()
    '''checking  the user input'''
    if user_choice=='1':        
        ''' Adding blocks to the chain '''
        add_transaction(user_input_transaction(),last_transaction())
    elif user_choice=='2':
        printing_blockchain()
    elif user_choice=='h':
        if len(blockchain)>=1:
            blockchain[0]=[2]
    elif user_choice=='q':
        break
    else:
        print("\n!!!!!!!!Input is invalid.Please check menue and enter correct option!!!\n")   
    print("Choice registered!")
    if not verify_blockchain():
        printing_blockchain()
        print('This blockchain is invalid!!!!!!')
        break
print('Done')