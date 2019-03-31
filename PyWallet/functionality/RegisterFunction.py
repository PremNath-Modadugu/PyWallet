'''
Created on Aug 9, 2017

@author: modadugu.nath
'''
from classes.UserModule import User
from validations import UserValidation
from random import randrange
from exceptions import CustomException
from database import InsertDB, CheckDB

'''Registering New User'''
def register_user():
    try:
        user=User()
        question_list=["Your favourite color","Name of your pet","Name of your birth place"]
        name=input("enter name:")
        mobile=input("enter mobile number:")
        email=input("enter email id:")
        p_word=input("enter password:")
        re_p_word=input("re-enter password:")
        print("select any one security question from below")
        for i in range(len(question_list)):
            print(i+1,".",question_list[i])
        end=False
        while(end==False):
            option=input()
            if(option.isdigit() and (int(option)>=1) and int(option)<=3):
                if(int(option)==1):
                    ques=question_list[0]
                    ans=input("Enter answer for selected question")
                elif(int(option)==2):
                    ques=question_list[1]
                    ans=input("Enter answer for selected question")    
                elif(int(option)==3):
                    ques=question_list[2]
                    ans=input("Enter answer for selected question")
                end=True
            else:
                print("Please enter a valid option ( 1,2 & 3)")
                
        sys_cap=str(randrange(0,9))+chr(randrange(97,122))+str(randrange(0,9))+chr(randrange(33,41))
        print("captcha:",sys_cap)
        cap=input("enter captch:")
        
        if(UserValidation.check_user_name(name)):
            if(UserValidation.check_mobile(mobile)):
                if(UserValidation.check_email(email)):
                    if(UserValidation.check_password(p_word,re_p_word)):
                        if(UserValidation.check_captcha(sys_cap,cap)):
                            user.set_name(name)
                            user.set_mobile_number(mobile)
                            user.set_email_id(email)
                            user.set_password(p_word)
                            user.set_question(ques)
                            user.set_answer(ans)
                            InsertDB.InsertData(user)
                            print("Registraion Sucessful")
                            
    except CustomException.InvalidUserNameException as e:
        print(e)
        
    except CustomException.InvalidMobileException as e:
        print(e)
    
    except CustomException.InvalidEmailException as e:
        print(e)
    
    except CustomException.InvalidPasswordException as e:
        print(e)
        
    except CustomException.InvalidCaptchaException as e:
        print(e)
        
def forget_password():
    try:
        mnumber=input("Enter your Mobile number")
        if(UserValidation.recheck_mobile(mnumber)):
            quesans=CheckDB.get_ques(mnumber)
            print("What is",quesans[0])
            user_ans=input()
            if(UserValidation.recheck_quesans(quesans[1].lower(),user_ans.lower())):
                print("your password is:",CheckDB.get_user(mnumber))
            else:
                raise CustomException.InvalidAnswerException()
        else:
            raise CustomException.InvalidMobileException()
    except CustomException.InvalidMobileException as e:
        print(e)
    except CustomException.InvalidAnswerException as e:
        print(e)