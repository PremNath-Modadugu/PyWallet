'''
Created on Aug 9, 2017

@author: modadugu.nath
'''
#for login module
class InvalidLoginException(Exception):
    def __init__(self):
        super().__init__("Maximum Login attempts exceeded")
        
class InvalidUserException(Exception):
    def __init__(self):
        super().__init__("user name or password does not match")
        
#for registration module      
class InvalidUserNameException(Exception):
    def __init__(self):
        super().__init__("Invalid UserName")
        
class InvalidMobileException(Exception):
    def __init__(self):
        super().__init__("Invalid mobile number")
        
class InvalidEmailException(Exception):
    def __init__(self):
        super().__init__("Invalid Email-Id")
    
class InvalidPasswordException(Exception):
    def __init__(self):
        super().__init__("Invalid Password")
        
class InvalidCaptchaException(Exception):
    def __init__(self):
        super().__init__("Invalid Captcha")
        
#for add money module 
class InvalidCvvException(Exception):
    def __init__(self):
        super().__init__("Invalid cvv number")
        
class CardNumberException(Exception):
    def __init__(self):
        super().__init__("Invalid card number")
        
class InvalidExpiryException(Exception):
    def __init__(self):
        super().__init__("Invalid card Month or Year")
        
class InvalidBankNameException(Exception):
    def __init__(self):
        super().__init__("Invalid BankName")

class InvalidAnswerException(Exception):
    def __init__(self):
        super().__init__("Answer doesnt matches")
        
class InvalidAmountException(Exception):
    def __init__(self):
        super().__init__("Amount should be in positive value")