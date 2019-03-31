'''
Created on Aug 9, 2017

@author: modadugu.nath
'''
import datetime
from database import CheckDB
from exceptions import CustomException


def check_number(c_number):
    if(len(c_number)==12 and c_number.isdigit()):
        return True
    raise CustomException.CardNumberException()

def check_expiry(c_month,c_year):
    now = datetime.datetime.now()
    if(int(c_year)==int(str(now.year)[2:])):
        if(int(c_month)>=now.month):
            return True
    elif(len(c_year)==2 and int(c_year)>int(str(now.year)[2:])):
        if(int(c_month)>0 and int(c_month)<13):
            return True
    raise CustomException.InvalidExpiryException()
    
def check_cvv(cvv):
    if(len(cvv)==3 and cvv.isdigit()):
        return True
    raise CustomException.InvalidCvvException()

def check_bank_name(n_name):
    list1=CheckDB.check_name()
    if(n_name.upper() in list1):
        return True
    return CustomException.InvalidCvvException()

def check_user_id(n_user_id):
    if(n_user_id.isalnum()):
        return True
    raise CustomException.InvalidUserNameException()

def check_b_password(n_password):
    if not n_password.isalnum():
        return True
    raise CustomException.InvalidPasswordException()

def check_transid(temp):
    db_transid=CheckDB.get_transactionid()
    if(db_transid==None):
        return temp
    elif(db_transid==temp):
        return temp+1
    else:
        return db_transid+1

def check_amount(amount):
    if(amount>0):
        return True 
    raise CustomException.InvalidAmountException()