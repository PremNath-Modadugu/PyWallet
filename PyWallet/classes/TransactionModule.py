'''
Created on Aug 10, 2017

@author: modadugu.nath
'''

class Transaction():

    __transaction_id=100000

    def __init__(self):
        self.__mobile_number=None
        self.__date=None
        self.__remarks=None
        self.__type=None
        self.__amount=None

    def get_mobile_number(self):
        return self.__mobile_number

    def get_date(self):
        return self.__date

    def get_remarks(self):
        return self.__remarks

    def get_type(self):
        return self.__type

    def get_amount(self):
        return self.__amount

    def set_mobile_number(self, mobile_number):
        self.__mobile_number = mobile_number

    def set_date(self, date):
        self.__date = date

    def set_remarks(self, remarks):
        self.__remarks = remarks

    def set_type(self, t_type):
        self.__type = t_type

    def set_amount(self,amount):
        self.__amount = amount
        
    def get_transaction_id(self):
        return self.__transaction_id

    def set_transaction_id(self, transaction_id):
        self.__transaction_id = transaction_id
