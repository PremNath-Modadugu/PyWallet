'''
Created on Aug 9, 2017

@author: neerajalakshmia.k
'''
class InvalidPincodeException(Exception):
    def __init__(self):
        super().__init__("Pin code is invalid")
        
class NoPlaceException(Exception):
    def __init__(self):
        super().__init__("  No Places Found")
        
class InvalidOptionException(Exception):
    def __init__(self):
        super().__init__("Invalid Option...Try again")
        