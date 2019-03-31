'''
Created on Aug 9, 2017

@author: modadugu.nath
'''
from utility import DBConnectivity
def InsertData(user):
    try:
        con=DBConnectivity.create_connection()
        cur=DBConnectivity.create_cursor(con)
        cur.execute('INSERT INTO PyUsers (MobileNumber,Name,EmailId,Password,Question,Answer)VALUES(:MobileNumber,:Name,:EmailId,:Password,:Question,:Answer)',{"MobileNumber":user.get_mobile_number(),"Name":user.get_name(),"EmailId":user.get_email_id(),"Password":user.get_password(),"Question":user.get_question(),"Answer":user.get_answer()})
        con.commit()
    finally:
        cur.close()
        con.close()
        
def InsertAmount(user,amount):
    try:
        con=DBConnectivity.create_connection()
        cur=DBConnectivity.create_cursor(con)
        cur.execute("select Balance from PyUsers where MobileNumber=:MobileNumber",{"MobileNumber":user.get_mobile_number()})
        for p in cur:
            x=p[0]
        amount+=x
        cur.execute('UPDATE PyUsers SET Balance=:Balance where MobileNumber=:MobileNumber',{"Balance":amount,"MobileNumber":user.get_mobile_number()})
        user.set_balance(amount)
        con.commit()
    finally:
        cur.close()
        con.close()
        
def InsertTrarnsaction(transact):
    try:
        con=DBConnectivity.create_connection()
        cur=DBConnectivity.create_cursor(con)
        cur.execute('INSERT INTO Transaction (Transactionid,MobileNumber,remarks,t_type,amount)VALUES(:Transactionid,:MobileNumber,:remarks,:t_type,:amount)',{"Transactionid":transact.get_transaction_id(),"MobileNumber":transact.get_mobile_number(),"Remarks":transact.get_remarks(),"t_type":transact.get_type(),"Amount":transact.get_amount()})
        con.commit()
    finally:
        cur.close()
        con.close()