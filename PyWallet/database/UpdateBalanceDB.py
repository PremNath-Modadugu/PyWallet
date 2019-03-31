'''
Created on Aug 10, 2017

@author: mukesh.barik
'''

from utility import DBConnectivity
def update_balance(user,new_amount):
    try:
        con=DBConnectivity.create_connection()
        cur=DBConnectivity.create_cursor(con)
        cur2=DBConnectivity.create_cursor(con)
        cur.execute('UPDATE Pyusers set Balance=:Balance where MobileNumber=:MobileNumber',{"Balance":new_amount,"MobileNumber":user.get_mobile_number()})
        cur2.execute('select Balance from Pyusers where MobileNumber=:MobileNumber',{"MobileNumber":user.get_mobile_number()})
        con.commit()
        data=cur2.fetchall()
        user.set_balance((data[0])[0])
            
            
        
    finally:
        con.commit()
        cur.close()
        con.close()
        
        