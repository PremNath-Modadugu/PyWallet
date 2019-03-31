'''
Created on Aug 9, 2017

@author: neerajalakshmia.k
'''
class Nearbyplaces:
    def __init__(self):
        self.__pincode=None
        self.__name=None
        self.__address=None

    def get_name(self):
        return self.__name


    def get_address(self):
        return self.__address


    def set_name(self, value):
        self.__name = value


    def set_address(self, value):
        self.__address = value


    def get_pincode(self):
        return self.__pincode


    def set_pincode(self, value):
        self.__pincode = value
    
        
    