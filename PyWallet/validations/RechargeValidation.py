'''
Created on Aug 9, 2017

@author: mukesh.barik
'''
from exceptions.CustomExceptions2 import *
def validate_mobile_number(mobile_number):
    if(mobile_number.isdigit() and len(mobile_number)==10):
        return True
    else:
        raise InvalidMobileNumberException()
def validate_amount(amount,user_balance):
    
    if(amount.isdigit() and int(amount)%10==0 and int(amount)>=10 and int(amount)<=500):
        if(user_balance-int(amount)>=0):
            return True
        else:
            raise LowBalanceException()
    else:
        raise InvalidAmountException()
            
    
    
    
def validate_plan(plan):
    if(plan.lower()== "prepaid" or plan.lower()=="postpaid" and plan.isalpha()):
        return True
    else:
        raise InvalidPlanException()
def validate_pywallet_amount(package_amount,balance):
    if(balance-package_amount>=0):
        
        return True
    else:
        raise LowBalanceException()
def validate_cash_back(count_dth,count_mobile,totalpaid):
    if(count_dth>=1 and count_mobile>=1 and totalpaid>500):
        return True
    else:
        return False

    