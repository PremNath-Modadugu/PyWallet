'''
Created on Aug 10, 2017

@author: neerajalakshmia.k
'''

from validations import NearbyPlacesValidations
from exceptions.CustomException4 import InvalidPincodeException
'''
positive test cases
'''

print(NearbyPlacesValidations.validate_pincode('570021'))
        
'''
negative test cases
'''    
try:
    if NearbyPlacesValidations.validate_pincode('570022131'):
        print('valid')
    
except InvalidPincodeException as e:
    print(e)
    
try:
    if NearbyPlacesValidations.validate_pincode('570dsf32'):
        print('valid')
    
except InvalidPincodeException as e:
    print(e)
    
try:
    if NearbyPlacesValidations.validate_pincode('200'):
        print('valid')
    
except InvalidPincodeException as e:
    print(e)