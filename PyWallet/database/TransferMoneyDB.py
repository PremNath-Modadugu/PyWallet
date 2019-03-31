'''
Created on Aug 11, 2017

@author: neerajalakshmia.k
'''
from utility import DBConnectivity
def update_sender_balance(user,sender_no,amount):
    try:
        con=DBConnectivity.create_connection()
        cur=DBConnectivity.create_cursor(con)
        cur.execute("select balance from Pyusers where mobilenumber=:sender_no",{"sender_no":sender_no})
        for row in cur:
            bal=row[0]
        bal=bal-amount
        cur.execute("update Pyusers set balance=:bal1 where (mobilenumber=:num)",{"bal1":bal,"num":sender_no})
        con.commit()
        cur.execute("select balance from Pyusers where mobilenumber=:sender_no",{"sender_no":sender_no})
        for row in cur:
            bal1=row[0]
        user.set_balance(bal1)
        
    finally:
        cur.close()
        con.close()
        
def update_receiver_balance(receiver,receiver_no,amount):
    try:
        con=DBConnectivity.create_connection()
        cur=DBConnectivity.create_cursor(con)
        cur.execute("select balance from Pyusers where mobilenumber=:receiver_no",{"receiver_no":receiver_no})
        for row in cur:
            bal=row[0]
        bal=bal+amount
        cur.execute("update Pyusers set balance=:bal1 where (mobilenumber=:num)",{"bal1":bal,"num":receiver_no})
        con.commit()
        cur.execute("select balance from Pyusers where mobilenumber=:receiver_no",{"receiver_no":receiver_no})
        for row in cur:
            bal1=row[0]
        receiver.set_balance(bal1)
    finally:
        cur.close()
        con.close()
        
