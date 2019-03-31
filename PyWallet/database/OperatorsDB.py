'''
Created on Aug 9, 2017

@author: mukesh.barik
'''
from utility import DBConnectivity
from exceptions.CustomExceptions2 import InvalidMobileNumberException,InvalidDTHOperatorException
#from functionality.RechargeFunctions import recharge


def check_mobile_operator(operator_code):
    try:
        con=DBConnectivity.create_connection()
        cur=DBConnectivity.create_cursor(con)
        cur.execute("select OperatorName from MobileOperator  where OperatorCode=:OperatorCode",{"OperatorCode":operator_code})
        data=cur.fetchall()
        if(len(data)==0):
           
            raise InvalidMobileNumberException()
        else:
            
                return ((data[0])[0])
    finally:
        cur.close()
        con.close()
        
            
def validate_dth_operator(current_operator):
    try:
        con=DBConnectivity.create_connection()
        cur=DBConnectivity.create_cursor(con)
        cur.execute("select Operator from DTHUser  where Operator=:Operator",{"Operator":current_operator})
        data=cur.fetchall()
        if(len(data)==0):
           
            raise InvalidDTHOperatorException()
        else:
            return True
            #print("yes")
    #except InvalidDTHOperatorException as e:
        #print(e)
        
    finally:
        cur.close()
        con.close()
def get_package_detail(cust_id,current_operator):
    if(cust_id.isalpha()):
        raise InvalidDTHOperatorException()
        
    try:
        con=DBConnectivity.create_connection()
        cur=DBConnectivity.create_cursor(con)
        cur.execute("select * from DTHUser  where CustId=:CustId and Operator=:Operator",{"CustId":cust_id,"Operator":current_operator})
        data=cur.fetchall()
        if(len(data)==0):
            raise InvalidDTHOperatorException()
        else:
            return data
            
        
    finally:
        cur.close()
        con.close()
        
        
    
    #except InvalidMobileNumberException as e:
        #print(e)
    
#check_mobile_operator(9040)
#validate_dth_operator('SMP')
#get_package_detail(1)