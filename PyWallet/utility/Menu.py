'''

Created on Jul 29, 2015

@author: Sara
'''
from functionality import LoginFunction, RegisterFunction
from exceptions.CustomException import InvalidLoginException
'''
This module displays a menu to the user.
'''
print(" + ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ + ")
print("     $ Welcomes To PyWallet $      ")
print(" + ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ + ")

print("Choose an option from below:\n")

end=False
count=0
while(end==False):
    try:
        print("1. Login")
        print("2. Registration")
        print("3. Forget Password")
        print("4. Exit")
        
        option=input()
        if(option.isdigit() and (int(option)>=1) and int(option)<=4):
            if(int(option)==1):
                if(count<3):
                    print("User login")
                    count+=1
                    LoginFunction.Login()
                else:
                    end=True
                    raise InvalidLoginException()
                
            if(int(option)==2):
                print("Welcome to registration")
                RegisterFunction.register_user()
            
            if(int(option)==3):
                RegisterFunction.forget_password()
            
            if(int(option)==4):
                print("Thank you")
            
                end=True
        else:
            print("Please enter a valid option ( 1,2,3 & 4)")
    
    except InvalidLoginException as e:
        print(e)
    