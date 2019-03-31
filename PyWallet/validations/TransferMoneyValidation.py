'''
Created on Aug 11, 2017

@author: modadugu.nath
'''
from exceptions.CustomException5 import MaxTranferExceedexception
def validate_transfer_money(amount):
    try:        
        if(0<int(amount)<=2000):
            return True
        else:
            raise MaxTranferExceedexception()
    except MaxTranferExceedexception as e:
        print(e)
    except Exception:
        print("invalid amount")
        
    