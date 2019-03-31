'''
Created on Aug 9, 2017

@author: neerajalakshmia.k
'''
from classes.NearbyPlacesModule import Nearbyplaces
from database import NearbyPlacesDB
from validations import NearbyPlacesValidations
from exceptions.CustomException4 import InvalidPincodeException,InvalidOptionException

             
''' this function finds the nearby places for the entered pincode'''         

def Find_NearbyPlaces():
    end=False
    while(end==False):
        try:
            print("Nearby...")
            pincode=input("Enter pin code:")
            
            '''validates pincode in the database'''
            
            if NearbyPlacesValidations.validate_pincode(pincode):
#                 end=True
                if (str(pincode).endswith('12')) or (str(pincode).endswith('01')):
                    print("1.Malls")
                    print("2.Restaurants")
                    print("3.Super market")
                    print("4.Hospitals")
                    opt=False
                    option_dict={1:"Mall",2:"Restaurant",3:"Super market",4:"Hospital"}
                    while(opt==False):
                        try:
                            option=input("Choose an option:")
                            if option.isdigit() and int(option) in option_dict:
                                category=option_dict[int(option)]
                                NearbyPlacesDB.place(pincode,category)
                                opt=True 
#                                 loop()              
                            
                            else:
                                raise InvalidOptionException()
                            
                        except InvalidOptionException as e:
                            print(e)
                            
                else:
                    print("1.Restaurants")
                    print("2.Super market")
                    print("3.Hospitals")
                    opt=False
                    option_dict={1:"Restaurant",2:"Super market",3:"Hospital"}
                    while(opt==False):
                        try:
                            option=input("Choose an option:")
                            if option.isdigit() and int(option) in option_dict:
                                category=option_dict[int(option)]
                                NearbyPlacesDB.place(pincode,category) 
                                opt=True
#                                 loop()
                            else:
                                raise InvalidOptionException()
                                
                        
                        except InvalidOptionException as e:
                            print(e)
#                             loop()
                x=input("Do you wish to continue..(y/n)")
                if(x.lower() =='n'):
                    end=True
        
        
        except InvalidPincodeException as e:
            print(e)
            x=input("Do you wish to continue..(y/n)")
            if(x.lower() =='n'):
                end=True
#             loop()
     
        

            
                
                
                
