'''
Created on Aug 9, 2017

@author: neerajalakshmia.k
'''
from database import NearbyPlacesDB
from exceptions.CustomException4 import InvalidPincodeException

def validate_pincode(pincode):
    if len(pincode)==6 and str(pincode).isdigit() and NearbyPlacesDB.pincode(pincode):
        return True
    else:
        raise InvalidPincodeException() 