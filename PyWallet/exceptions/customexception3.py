'''
Created on Aug 10, 2017

@author: nagamani.undralla
'''
class InvalidChoiceException(Exception):
    def __init__(self):
        super().__init__("Sorry! Enter a valid Choice")    
    
class InvalidDateException(Exception):
    def __init__(self):
        super().__init__("Please select a date in DD-MM-YYYY format")
        
class InvalidLanguageException(Exception):
    def __init__(self):
        super().__init__("Please select another language")        
        
class InvalidTimeException(Exception):
    def __init__(self):
        super().__init__("please Choose a valid Show time")

class InvalidTicketException(Exception):
    def __init__(self):
        super().__init__("sorry! Insufficient tickets for the movie")
        
class InvalidUserTicketException(Exception):
    def __init__(self):
        super().__init__("Oops! maximum limit per day reached")
        
class InvalidBalanceException(Exception):
    def __init__(self):
        super().__init__("Insufficient Balance")