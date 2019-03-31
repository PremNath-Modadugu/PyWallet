'''
Created on Aug 9, 2017

@author: modadugu.nath
'''
from database import CheckDB
from exceptions import CustomException

def check_user(mnumber,password):
    p_word=CheckDB.get_user(mnumber)
    if(p_word==password):
        return True
    else:
        raise CustomException.InvalidUserException()
    
def check_user_name(uname):
    if uname.isalpha():
        return True
    else:
        raise CustomException.InvalidUserNameException()
    
def check_mobile(mnumber):
    if(len(mnumber)==10 and mnumber.isnumeric()):
        db_check=CheckDB.check_mobile(mnumber)
        if(len(db_check)==0):
            return 1
    else:
        raise CustomException.InvalidMobileException() 

def check_email(email):
    t_list=email.split('@')
    if(len(t_list)==2):
        if(t_list[0].count('.')>=1 and t_list[1].count('.')==1):
            temp=t_list[0].count('.')
            for i in range(temp):
                x=t_list[0].replace('.','p')
            if(x.isalnum()):
                db_check=CheckDB.check_email(email)
                if(len(db_check)==0):
                    return True
    raise CustomException.InvalidEmailException() 

def check_password(p_word,re_p_word):
    l_flag=u_flag=d_flag=s_flag=0
    if(len(p_word)>7 and p_word==re_p_word):
        for i in p_word:
            if i.isalpha() and i.lower()==i:
                l_flag=1
                break
        for i in p_word:
            if i.isalpha() and i.upper()==i:
                u_flag=1
                break
        for i in p_word:
            if i.isdigit():
                d_flag=1
                break
        for i in p_word:
            if not(i.isalpha() or i.isdigit()):
                s_flag=1
                break
            
        if l_flag==1 and u_flag==1 and d_flag==1 and s_flag==1:
            return True
    else:
        raise CustomException.InvalidPasswordException()

def check_captcha(sys_cap,cap):
    if(sys_cap==cap):
        return True
    else:
        raise CustomException.InvalidCaptchaException()

def recheck_mobile(mnumber):
    if(len(mnumber)==10 and mnumber.isnumeric()):
        db_check=CheckDB.check_mobile(mnumber)
        if(len(db_check)!=0):
            return 1
    return 0

def recheck_quesans(ans,user_ans):
    if ans==user_ans:
        return True
    return 0