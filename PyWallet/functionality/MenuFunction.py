'''
Created on Aug 9, 2017

@author: modadugu.nath
'''
from functionality import AddMoneyFunction, TransactionFunction,RechargeFunctions,\
    NearbyPlacesFunctions, BookMovieFunction,TransferMoneyFunction
    
'''Display Menu to user'''
def display_menu(user):
    print(" + ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ + ")
    print("$ Welcomes To PyWallet $")
    print(" + ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ + ")
    print("Choose an option from below:\n")
    end=False
    while(end==False):
        print("1. Add Money")
        print("2. Recharge")
        print("3. Book on Pywallet")
        print("4. Near By Places")
        print("5. View recent transactions")
        print("6. Transfer Money")
        print("7. Exit")
        
        option=input()
        if(option.isdigit() and (int(option)>=1) and int(option)<=7):
            if(int(option)==1):
                AddMoneyFunction.add_money(user)
            if(int(option)==2):
                RechargeFunctions.recharge(user)
            if(int(option)==3):
                BookMovieFunction.BookMovie(user)
            
            if(int(option)==4):
                NearbyPlacesFunctions.Find_NearbyPlaces()
            
            if(int(option)==5):
                TransactionFunction.transaction(user)
            
            if(int(option)==6):
                TransferMoneyFunction.transfer_money(user)
            
            if(int(option)==7):
                print("Thank you")
                end=True
        else:
            print("Please enter a valid option ( 1 to 7)")