'''
Created on Aug 9, 2017

@author: mukesh.barik
'''
class Recharge:
    def __init__(self):
        self.__plan=None
        self.__mobile_number=None
        self.__operator=None
        self.__amount=None
        

    def get_plan(self):
        return self.__plan


    def get_mobile_number(self):
        return self.__mobile_number


    def get_operator(self):
        return self.__operator


    def get_amount(self):
        return self.__amount


    def set_plan(self, value):
        self.__plan = value


    def set_mobile_number(self, value):
        self.__mobile_number = value


    def set_operator(self, value):
        self.__operator = value


    def set_amount(self, value):
        self.__amount = value
class RechargeDth():
    def __init__(self):
        
        self.__cust_id=None
        self.__current_operator=None
        self.__package_type=None
        self.__amount=None

    def get_cust_id(self):
        return self.__cust_id


    def get_current_operator(self):
        return self.__current_operator


    def get_package_type(self):
        return self.__package_type


    def get_amount(self):
        return self.__amount


    def set_cust_id(self, value):
        self.__cust_id = value


    def set_current_operator(self, value):
        self.__current_operator = value


    def set_package_type(self, value):
        self.__package_type = value


    def set_amount(self, value):
        self.__amount = value

    
    
        
        
    