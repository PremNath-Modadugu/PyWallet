'''
Created on Aug 10, 2017

@author: group 10
'''

from Resources.DataStructures import Stack
from database import CheckDB
def transaction(user):
    details=Stack(100)
    data=CheckDB.get_transactions(user)
    if(len(data)==0):
        print("No Transactions yet done")
    else:
        print("Transaction date\t"+"Reamrks \t\t"+"Cr/Dr\t\t"+"Amount")
        for j in range(len(data)):
            details.push(list(data[j]))
            
        while not details.is_empty():
            temp=details.pop()
            now=temp[0]
            dot=str(now.day)+'/'+str(now.month)+'/'+str(now.year)[2:]
            print(dot,"\t",temp[1],"\t\t",temp[2],"\t\t",temp[3])