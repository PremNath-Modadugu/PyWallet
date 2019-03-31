'''
Created on Aug 9, 2017

@author: mukesh.barik
'''
class InvalidMobileNumberException(Exception):
    def __init__(self):
        super().__init__("The Mobile Number is invalid")
      

class InvalidAmountException(Exception):
    def __init__(self):
        super().__init__("Enter amount between 10 to 500 and in multiple of 10")

class InvalidPlanException(Exception):
    def __init__(self):
        super().__init__("Recharge Plan doesnot exists !!! ")
class InvalidDTHOperatorException(Exception):
    def __init__(self):
        super().__init__("Invalid Operator or Customer ID !!!")
class LowBalanceException(Exception):
    def __init__(self):
        super().__init__("You Donot Have Sufficient Pywallet Balance")