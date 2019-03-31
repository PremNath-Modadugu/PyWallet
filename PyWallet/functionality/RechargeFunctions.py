'''
Created on Aug 9, 2017

@author: mukesh.barik
'''

from classes.RechargeModule import Recharge,RechargeDth
from validations.RechargeValidation import *
from database.OperatorsDB import check_mobile_operator,validate_dth_operator,get_package_detail
from database.UpdateBalanceDB import update_balance
from classes.TransactionModule import Transaction
from validations import BankingValidation
from database import InsertDB
def recharge(user):
    transact=Transaction()
    end=False
    while(end==False):
        try:
            flag=0
            
            choice=input("1.Mobile Recharge\n2.DTH Recharge\n3.Exit")
            if(choice.isdigit()):
            
                '''
                for mobile recharge
                '''
            
                if(int(choice)==1):
                    recharge_obj=Recharge()
                    '''
                    input plan and validate
                    '''
                    plan=input("Prepaid or Postpaid:")
                    if(validate_plan(plan)):
                        recharge_obj.set_plan(plan)
                        
                        '''
                        input mobile number ,auto populate operator and validate mobile number
                        '''
                        mobile_number=input("Enter mobile number:")
                        if(validate_mobile_number(mobile_number)):
                            recharge_obj.set_mobile_number(mobile_number)
                            operator_code=str(mobile_number)[0:4]
                            operator_name=check_mobile_operator(operator_code)
                            recharge_obj.set_operator(operator_name)
                            print("select operator:",recharge_obj.get_operator())
                            
                            
                            '''
                            input amount and validate then set 
                            '''
                            amount=input("enter amount:")
                            user_balance=user.get_balance()
                            if(validate_amount(amount,user_balance)):
                                new_amount= user_balance-int(amount)
                                '''
                                upadte database for successsful recharge
                                '''
                                
                                update_balance(user,new_amount)
                                recharge_obj.set_amount(amount)
                                print("successfully rechareged!!")
                                flag=1
                                recharge.count_mobile+=1
                                recharge.total_paid+=int(amount)
                                print("your Pywallet balance is",user.get_balance())
                                
                                   
                            '''
                            for DTH recharge
                            ''' 
                                
                elif(int(choice)==2):
                    recharge_dth_obj=RechargeDth()
                    
                    current_operator=input("Current Operator:").upper()
                    '''
                    validate dth operator name
                    '''
                   
                    if(validate_dth_operator(current_operator)):
                        cust_id=input("Customer Id:")
                        package_detail=get_package_detail(cust_id,current_operator.upper())
                        #print(package_detail)
                        '''
                        set dth user class vriables
                        '''
                        recharge_dth_obj.set_cust_id((package_detail[0])[0])
                        recharge_dth_obj.set_current_operator((package_detail[0])[1])
                        recharge_dth_obj.set_package_type((package_detail[0])[2])
                        recharge_dth_obj.set_amount((package_detail[0])[3])
                        print("Package Type:",recharge_dth_obj.get_package_type())
                        print("Amount:",recharge_dth_obj.get_amount())
                        package_amount=recharge_dth_obj.get_amount()
                        balance=user.get_balance()
                        '''
                        validate pywallet balance,rechage dth and upadte user database
                        '''
                        if(validate_pywallet_amount(package_amount,balance)):
                            
                            new_amount=balance-package_amount
                            update_balance(user,new_amount)
                            print("successfully rechareged!!")
                            flag=1
                            recharge.count_dth+=1
                            recharge.total_paid+=package_amount
                            amount=package_amount
                            print("your Pywallet balance is",user.get_balance())
                            '''
                            while option 3 is selected check for cashback offer ,if valid add cashback to user pywallet
                            '''
                elif(int(choice)==3):
                    print("your Pywallet balance is",user.get_balance())
                    if(validate_cash_back(recharge.count_dth,recharge.count_mobile,recharge.total_paid)):
                        amount=0.1* recharge.total_paid
                        print("you got a cashback of rupees:",amount)
                        update_balance(user,new_amount+amount)
                        print("Now your Pywallet balance is",user.get_balance())
                        flag=1
                    end=True
                    recharge.count_mobile=0
                    recharge.count_dth=0
                    recharge.total_paid=0

                else:
                    print("Please enter a valid option ( 1,2,3)")
               
            if(flag==1):
                temp=transact.get_transaction_id()
                temp=BankingValidation.check_transid(temp)
                transact.set_transaction_id(temp)
                transact.set_mobile_number(user.get_mobile_number())
                
                if(int(choice)==3):
                    remark="To Wallet/"+str(temp)+"/Cashback"
                    transact.set_remarks(remark)
                    transact.set_type("Cr.")
                else:
                    remark="BIL/"+str(temp)+"/Recharge"
                    transact.set_remarks(remark)
                    transact.set_type("Dr.")
                transact.set_amount(amount)
                InsertDB.InsertTrarnsaction(transact)
            
            '''
            handling exception
            '''
                        
        except InvalidPlanException as e:
            print(e)
            
                
        except InvalidMobileNumberException as e:
            print(e)
            
        except InvalidAmountException as e:
            print(e)
           
        except InvalidDTHOperatorException as e:
            print(e)
            
                    
        except LowBalanceException as e:
            print(e)    
        
        
    
               
'''
static variable to track purchase and totala amount
'''
recharge.count_mobile=0
recharge.count_dth=0
recharge.total_paid=0

    
                    



        
        
    
    