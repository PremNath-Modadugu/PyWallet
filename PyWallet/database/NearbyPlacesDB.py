'''
Created on Aug 9, 2017

@author: neerajalakshmia.k
'''
from utility import DBConnectivity
from classes.NearbyPlacesModule import Nearbyplaces
from exceptions.CustomException4 import NoPlaceException

def pincode(pincode):
    try:
        con=DBConnectivity.create_connection()
        cur=DBConnectivity.create_cursor(con)
        cur.execute("select pincode  from Nearbyplaces where pincode between :pincode1 and :pincode2",{"pincode1":int(pincode)-5,"pincode2":int(pincode)+5})
        pn=cur.fetchall()
        if pn!=[]:
            return True
        return False
    finally:
        cur.close()
        con.close()        

def place(pincode,category):
    try:
        con=DBConnectivity.create_connection()
        cur=DBConnectivity.create_cursor(con)
        list_of_place=[]
        cur.execute("select name, address,pincode  from Nearbyplaces where lower(category)=:category and pincode between :pincode1 and :pincode2",{"category":category.lower(),"pincode1":int(pincode)-5,"pincode2":int(pincode)+5})
        
        for name, address,pincode in cur:
            '''
            In this loop, we are creating a product object for every row
            and setting the values from the row into the product object
            '''
            nearbyplaces=Nearbyplaces()
            nearbyplaces.set_pincode(pincode)
            nearbyplaces.set_name(name)
            nearbyplaces.set_address(address)            
            '''
            Here were are adding the product to a list
            '''
            list_of_place.append(nearbyplaces)
        print(category)
        if list_of_place!=[]:
            count=1
            for nearbyplaces in list_of_place:
                
                print("  "+str(count)+"."+nearbyplaces.get_name())
                print("    "+nearbyplaces.get_address())
                print("    Pin code:"+str(nearbyplaces.get_pincode()))
                count+=1
        else:
            raise NoPlaceException()   
    except NoPlaceException as e:
        print(e)
        
        
    finally:
        cur.close()
        con.close()