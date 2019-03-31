'''
Created on Aug 11, 2017

@author: modadugu.nath
'''
class MaxTranferExceedexception(Exception):
    def __init__(self):
        super().__init__("maximum Transfer limit Rs.2000/- exceeded")