'''
Created on Aug 11, 2017

@author: modadugu.nath
'''
from validations import TransferMoneyValidation
from exceptions.CustomException5 import MaxTranferExceedexception
'''
positive test cases
'''

print(TransferMoneyValidation.validate_transfer_money('1000'))
        
'''
negative test cases
'''    
try:
    if TransferMoneyValidation.validate_transfer_money('h123'):
        print('valid')
    
except MaxTranferExceedexception as e:
    print(e)
    
try:
    if TransferMoneyValidation.validate_transfer_money('3000'):
        print('valid')
    
except MaxTranferExceedexception as e:
    print(e)
    
try:
    if TransferMoneyValidation.validate_transfer_money('-3000'):
        print('valid')
    
except MaxTranferExceedexception as e:
    print(e)