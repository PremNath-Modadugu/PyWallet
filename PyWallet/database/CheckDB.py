'''
Created on Aug 9, 2017

@author: modadugu.nath
'''
from utility import DBConnectivity
def get_user(mnumber):
    try:
        con=DBConnectivity.create_connection()
        cur=DBConnectivity.create_cursor(con)
        cur.execute("select Password from PyUsers where MobileNumber=:MobileNumber",{"MobileNumber":mnumber})
        for p in cur:
            return p[0]
    finally:
        cur.close()
        con.close()
        
def check_mobile(mnumber):
    try:
        con=DBConnectivity.create_connection()
        cur=DBConnectivity.create_cursor(con)
        cur.execute("select Name from PyUsers where MobileNumber=:MobileNumber",{"MobileNumber":mnumber})
        data=cur.fetchall()
        return data
    finally:
        cur.close()
        con.close()
        
def check_email(email):
    try:
        con=DBConnectivity.create_connection()
        cur=DBConnectivity.create_cursor(con)
        cur.execute("select Name from PyUsers where EmailId=:EmailId",{"EmailId":email})
        data=cur.fetchall()
        return data
    finally:
        cur.close()
        con.close()
        
def check_balance(user):
    try:
        con=DBConnectivity.create_connection()
        cur=DBConnectivity.create_cursor(con)
        cur.execute("select Balance from PyUsers where MobileNumber=:MobileNumber",{"MobileNumber":user.get_mobile_number()})
        for p in cur:
            return p[0]
    finally:
        cur.close()
        con.close()
        
def check_name():
    try:
        list1=[]
        con=DBConnectivity.create_connection()
        cur=DBConnectivity.create_cursor(con)
        cur.execute("select * from bank")
        for p in cur:
            list1.append(p[0])
        return list1
    finally:
        cur.close()
        con.close()
        
def get_ques(mnumber):
    try:
        list1=[]
        con=DBConnectivity.create_connection()
        cur=DBConnectivity.create_cursor(con)
        cur.execute("select Question,Answer from PyUsers where MobileNumber=:MobileNumber",{"MobileNumber":mnumber})
        data=cur.fetchall()
        for i in range(len(data)+1):
            list1.append(data[0][i])
        return list1
    finally:
        cur.close()
        con.close()
        
def get_details(mnumber):
    try:
        list1=[]
        con=DBConnectivity.create_connection()
        cur=DBConnectivity.create_cursor(con)
        cur.execute("select * from PyUsers where MobileNumber=:MobileNumber",{"MobileNumber":mnumber})
        data=cur.fetchall()
        for i in range(len(data[0])):
            list1.append(data[0][i])
        return list1
    finally:
        cur.close()
        con.close()
        
def get_transactions(user):
    try:
        list1=[]
        con=DBConnectivity.create_connection()
        cur=DBConnectivity.create_cursor(con)
        cur.execute("select DOT,remarks,t_type,amount from transaction where MobileNumber=:MobileNumber order by DOT ASC",{"MobileNumber":user.get_mobile_number()})
        data=cur.fetchall()
        for i in range(len(data)):
            list1.append(data[i])
        return list1
    finally:
        cur.close()
        con.close()

def get_transactionid():
    try:
        con=DBConnectivity.create_connection()
        cur=DBConnectivity.create_cursor(con)
        cur.execute("select max(Transactionid) from transaction")
        for p in cur:
            return p[0]
    finally:
        cur.close()
        con.close()
        