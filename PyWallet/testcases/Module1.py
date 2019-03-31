'''
Created on Aug 11, 2017

@author: modadugu.nath
'''

from validations.UserValidation import check_user_name,check_mobile,check_email,check_password,check_captcha
from validations.BankingValidation import check_user_id,check_b_password,check_expiry,check_cvv,check_number,\
    check_amount
from exceptions import CustomException
'''
positive test cases 
'''
'''1 means True'''

print(check_user_name("Premnath"))

print(check_email('modadugu.nath@gmail.com'))

print(check_password('Pp1!prem','Pp1!prem'))

print(check_captcha('2d6$','2d6$'))


print(check_user_id('prem123'))

print(check_b_password('prem@123'))

print(check_expiry('08','23'))

print(check_number('345216548541'))

print(check_cvv('123'))

print(check_amount(2000))

'''
negative test cases 
'''

try:
    u_name=check_user_name("Premnath123")
except CustomException.InvalidUserNameException as e:
        print(e)
try:
    u_name=check_user_name("Premnath@123")
except CustomException.InvalidUserNameException as e:
        print(e)
   
    
try:
    u_mobile=check_mobile('991245901900')
except CustomException.InvalidMobileException as e:
        print(e)
try:
    u_mobile=check_mobile('991245')
except CustomException.InvalidMobileException as e:
        print(e)
   
        
try:
    u_email=check_email('modadugu.nath@gmail')
except CustomException.InvalidEmailException as e:
        print(e)
try:
    u_email=check_email('modadugunath@gmail.com')
except CustomException.InvalidEmailException as e:
        print(e)
    
    
        
try:
    u_password=check_password('Pp1!prem','pp1!prrem')
except CustomException.InvalidPasswordException as e:
        print(e)
try:
    u_password=check_password('Pp1prem','pp1!prrem')
except CustomException.InvalidPasswordException as e:
        print(e)
    
    
    
try:
    u_captcha=check_captcha('2d6$','2D6$')
except CustomException.InvalidCaptchaException as e:
        print(e)
try:
    u_captcha=check_captcha('2d6$','2D$')
except CustomException.InvalidCaptchaException as e:
        print(e)
    
try:
    b_userid=check_user_id('p*rem123')
except CustomException.InvalidUserNameException as e:
        print(e)
        

try:
    b_userid=check_b_password('prem123')
except CustomException.InvalidPasswordException as e:
        print(e)
    
try:
    b_expiry=check_expiry('08','15')
except CustomException.InvalidExpiryException as e:
        print(e)
    
try:
    b_number=check_number('345216548434541')
except CustomException.CardNumberException as e:
        print(e)
try:
    b_number=check_number('34521654')
except CustomException.CardNumberException as e:
        print(e)
        
        
try:
    b_cvv=check_cvv('123')
except CustomException.InvalidCvvException as e:
        print(e)
    
        
try:
    b_amount=check_amount(-2000)
except CustomException.InvalidAmountException as e:
        print(e)
    