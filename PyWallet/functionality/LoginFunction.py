from validations import UserValidation
from functionality import MenuFunction
from classes.UserModule import User
from database import CheckDB
from exceptions import CustomException

'''Login Module'''
def Login():
    try:
        mnumber=int(input('enter mobile number:'))
        password=input('enter password:')
        if(UserValidation.check_user(mnumber,password)):
            user=User()
            details_list=CheckDB.get_details(mnumber)
            '''inserting data into user object'''
            user.set_mobile_number(details_list[0])     
            user.set_name(details_list[1])
            user.set_email_id(details_list[2])
            user.set_password(details_list[3])
            user.set_question(details_list[4])
            user.set_answer(details_list[5])
            user.set_balance(details_list[6])
            MenuFunction.display_menu(user)    
        
    except CustomException.InvalidUserException as e:
        print(e)
    except Exception as e:
        print("invalid input")