'''
Created on Aug 11, 2017

@author: neerajalakshmia.k
'''
from validations import UserValidation, BookMovieValidations,BankingValidation,TransferMoneyValidation
from database import TransferMoneyDB, CheckDB,InsertDB
import time
from exceptions.CustomException import InvalidMobileException
from classes.TransactionModule import Transaction
from classes.UserModule import User
from exceptions.CustomException5 import MaxTranferExceedexception


def transfer_money(user):
    transact=Transaction()
    end=False
    while(end==False):
        try:      
        
            print("Enter the mobile number you wish to transfer money:")
            receiver_no=input()
            sender_no=user.get_mobile_number()
            if receiver_no.isdigit() and sender_no!=int(receiver_no) and UserValidation.recheck_mobile(receiver_no)==1:
                print("your current wallet balance is:",CheckDB.check_balance(user))
                end=True
                b_flag=False
                while(b_flag==False):                    
                    print("Enter the amount you wish to transfer:")
                    amount=float(input())
                    try:
                        
                        if(TransferMoneyValidation.validate_transfer_money(amount)):
                            if BookMovieValidations.validate_balance(sender_no,amount):
                                receiver=User()
                                receiver.set_mobile_number(receiver_no)
                                b_flag=True
                                TransferMoneyDB.update_sender_balance(user,sender_no, amount)
                                TransferMoneyDB.update_receiver_balance(receiver,int(receiver_no), amount)
                                print("Working...")
                                time.sleep(1)
                                print("Money Transfered Successfully..")
                                debited_balance=CheckDB.check_balance(user)
                                print("your current balance is after transfer:",debited_balance)
             
                                '''Update sender transaction table'''
                                temp=transact.get_transaction_id()
                                temp=BankingValidation.check_transid(temp)
                                transact.set_transaction_id(temp)
                                transact.set_mobile_number(sender_no)
                                remark="Transfer/To/"+receiver_no
                                transact.set_remarks(remark)
                                transact.set_type("Dr.")
                                transact.set_amount(amount)
                                InsertDB.InsertTrarnsaction(transact)
                
                                '''Update receiver transaction table'''
                                temp=transact.get_transaction_id()
                                temp=BankingValidation.check_transid(temp)
                                transact.set_transaction_id(temp)
                                transact.set_mobile_number(int(receiver_no))
                                remark="Received/From/"+str(sender_no)
                                transact.set_remarks(remark)
                                transact.set_type("Cr.")
                                transact.set_amount(amount)
                                InsertDB.InsertTrarnsaction(transact)
                            else:
                                print("Enter Valid amount...")
                    except MaxTranferExceedexception as e:
                        print(e)
                
                                
                l=False
                while(l==False):
                    print("Do you wish to continue..(Y/N)")
                    choice=input()
                    if choice.lower()=='y':
                        l=True
                        end=False
                    elif choice.lower()=='n':
                        l=True
                        end=True
                    else:
                        print("Enter valid choice")
                
            else:
                raise InvalidMobileException()        
            
        except InvalidMobileException as e:
            print(e)
        except Exception as e:
            print("Invalid Input")
    
        
            
            
        
                

            