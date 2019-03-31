'''
Created on Aug 10, 2017

@author: mukesh.barik
'''
from validations import RechargeValidation
from exceptions import CustomExceptions2
from database import OperatorsDB

print("test cases for mobile number validation\n")
'''
positive test case
'''
print(RechargeValidation.validate_mobile_number('9040058469'))
            
'''
negative test case for mobile number
'''

try:
    x=RechargeValidation.validate_mobile_number('12345678901')
except OperatorsDB.InvalidMobileNumberException as e:
    print(e)
try:
    x=RechargeValidation.validate_mobile_number('123456789')
except OperatorsDB.InvalidMobileNumberException as e:
    print(e)

print('_______________________________________')

print("test cases for mobile recharge amount validataion\n")
'''
positive test case
'''

print(RechargeValidation.validate_amount('300',500))
print(RechargeValidation.validate_amount('10',500))
print(RechargeValidation.validate_amount('500',500))

'''
negative test case for mobile number
'''
try:
    x=RechargeValidation.validate_amount('394',500)
except CustomExceptions2.InvalidAmountException as e:
    print(e)
try:
    x=RechargeValidation.validate_amount('9',500)
except CustomExceptions2.InvalidAmountException as e:
    print(e)
try:
    x=RechargeValidation.validate_amount('501',600)
except CustomExceptions2.InvalidAmountException as e:
    print(e)
try:
    x=RechargeValidation.validate_amount('200',100)
except CustomExceptions2.LowBalanceException as e:
    print(e)
try:
    x=RechargeValidation.validate_amount('-20',600)
except CustomExceptions2.InvalidAmountException as e:
    print(e)
    
try:
    x=RechargeValidation.validate_amount('a',600)
except CustomExceptions2.InvalidAmountException as e:
    print(e)

print("______________________________________________")

print("test cases for mobile recharge plan validation\n")

'''
positive test cases
'''
print(RechargeValidation.validate_plan('PREPAID'))
print(RechargeValidation.validate_plan('prepaid'))
print(RechargeValidation.validate_plan('PRepaid'))
print(RechargeValidation.validate_plan('POSTPAID'))
print(RechargeValidation.validate_plan('postpaid'))
print(RechargeValidation.validate_plan('postPAID'))

'''
negative test cases
'''
try:
    RechargeValidation.validate_plan('x')
except CustomExceptions2.InvalidPlanException as e:
    print(e)
print("______________________________________________")
print("Test cases to validate pywallet amount")
        
'''
positive test cases
'''
print(RechargeValidation.validate_pywallet_amount(500,500))
print(RechargeValidation.validate_pywallet_amount(499,500))
'''
negative test cases
'''
try:
    x=RechargeValidation.validate_pywallet_amount(501,500)
except CustomExceptions2.LowBalanceException as e:
    print(e)
print("__________________________________________________")

print("validate cash back")

'''
positive test cases
'''

print(RechargeValidation.validate_cash_back(1,1,501))

'''
negative test cases
'''

print(RechargeValidation.validate_cash_back(0,1,501))
print(RechargeValidation.validate_cash_back(1,0,501))
print(RechargeValidation.validate_cash_back(0,0,501))
print(RechargeValidation.validate_cash_back(0,1,500))
print("________________________________________________________")

print("validate mobile number in mobile  operator database")

'''
positive test cases
'''

print(OperatorsDB.check_mobile_operator(9040))

'''
negative test cases
'''
try:
    x=OperatorsDB.check_mobile_operator(9000)
except OperatorsDB.InvalidMobileNumberException as e:
    print(e)
print("____________________________________________________________")
print("validate dth operator name")

'''
positive test cases
'''
print(OperatorsDB.validate_dth_operator('SMP'))

'''
negative testcase
'''
try:
    x=OperatorsDB.validate_dth_operator('x')
except OperatorsDB.InvalidDTHOperatorException as e:
    print(e)
    
print("_____________________________________________")
print("validate custid and operator combination")
'''
positive test cases
'''
print(OperatorsDB.get_package_detail('4','SMP'))

'''
negative testcase
'''
try:
    OperatorsDB.get_package_detail('1','SMP')
except OperatorsDB.InvalidDTHOperatorException as e:
    print(e)



    


    