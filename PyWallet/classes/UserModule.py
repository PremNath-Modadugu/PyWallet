'''
Created on Aug 9, 2017

@author: modadugu.nath
'''

class User:
   
    def __init__(self):
        self.__name=None
        self.__mobile_number=None
        self.__email_id=None
        self.__password=None
        self.__question=None
        self.__answer=None
        self.__balance=None

    def get_balance(self):
        return self.__balance

    def set_balance(self, balance):
        self.__balance = balance

    def get_question(self):
        return self.__question

    def get_answer(self):
        return self.__answer

    def set_question(self, question):
        self.__question = question


    def set_answer(self, answer):
        self.__answer = answer

        
    def get_name(self):
        return self.__name

    def get_mobile_number(self):
        return self.__mobile_number

    def get_email_id(self):
        return self.__email_id

    def get_password(self):
        return self.__password

    def set_name(self, name):
        self.__name = name

    def set_mobile_number(self, mobile_number):
        self.__mobile_number = mobile_number

    def set_email_id(self, email_id):
        self.__email_id = email_id

    def set_password(self, password):
        self.__password = password
   
    