'''
Created on Aug 9, 2017

@author: modadugu.nath
'''
from database import CheckDB, InsertDB
from validations import BankingValidation
from exceptions import CustomException
from classes.TransactionModule import Transaction

'''For adding money into wallet'''
def add_money(user):
    transact=Transaction()

    end=False
    try:
        while(end==False):
            flag=0
            print("your current wallet balance is:",CheckDB.check_balance(user))
            amount=float(input("enter amount to be added: "))
            BankingValidation.check_amount(amount)
            print("Choose your payment mode from the options below:\n")
            print("1. Credit Card")
            print("2. Debit Card")
            print("3. Net Banking")
            option=input()
            if(option.isdigit() and (int(option)>=1) and int(option)<=3):
                if(int(option)==1 or int(option)==2):
                    c_number=input("enter your 12 digit card number: ")
                    c_month=input("Month: ")
                    c_year=input("Year(last 2 digits): ")
                    cvv=input("CVV: ")
                    if(BankingValidation.check_number(c_number)):
                        if(BankingValidation.check_expiry(c_month,c_year)):
                            if(BankingValidation.check_cvv(cvv)):
                                flag=1
                                InsertDB.InsertAmount(user,amount)
                                print("amount added to the wallet successfully")
                                print("your wallet balance is :",CheckDB.check_balance(user))
                                
                if(int(option)==3):
                    n_name=input("enter bank name: ")
                    n_user_id=input("enter user id :")
                    n_password=input("enter password: ")
                    if(BankingValidation.check_bank_name(n_name)):
                        if(BankingValidation.check_user_id(n_user_id)):
                            if(BankingValidation.check_b_password(n_password)):
                                flag=1
                                InsertDB.InsertAmount(user,amount)
                                print("amount added to the wallet successfully")
                                print("your wallet balance is :",CheckDB.check_balance(user))   
                    else:
                        raise CustomException.InvalidBankNameException
                end=True
            else:
                print("Please enter a valid option ( 1,2 & 3)")
                
            ''' For inserting into transaction database'''
            if(flag==1):
                temp=transact.get_transaction_id()
                temp=BankingValidation.check_transid(temp)
                transact.set_transaction_id(temp)
                transact.set_mobile_number(user.get_mobile_number())
                remark="To Wallet/"+str(user.get_mobile_number())
                transact.set_remarks(remark)
                transact.set_type("Cr.")
                transact.set_amount(amount)
                InsertDB.InsertTrarnsaction(transact)
                temp=input("Do you wish to continue?(Y/N)")
                if(temp.lower()=='y'):
                    end=False
                    
                    
    except CustomException.InvalidCvvException as e:
        print(e)
    except CustomException.CardNumberException as e:
        print(e)
    except CustomException.InvalidExpiryException as e:
        print(e)
    except CustomException.InvalidBankNameException as e:
        print(e)
    except CustomException.InvalidPasswordException as e:
        print(e)
    except CustomException.InvalidUserNameException as e:
        print(e)
    except CustomException.InvalidAmountException as e:
        print(e)