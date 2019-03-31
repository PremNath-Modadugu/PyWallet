'''
Created on Aug 9, 2017

@author: nagamani.undralla
'''
#from functionality.BookMovieFunction import view
from database import BookMovieDB
from exceptions import customexception3


def validate_date(date):
    try:
        l=BookMovieDB.dateofmovie(date)
        if date in l:
            return True
        else:
            raise customexception3.InvalidDateException()
    except customexception3.InvalidDateException as e:
        print(e)

def validate_language(date,language):
    try:
        l=BookMovieDB.language(date,language)
        if language.lower() in l:
            return True
        else:
            raise customexception3.InvalidLanguageException()
    except customexception3.InvalidLanguageException as e:
        print(e)
        
def validate_time(time):
    try:
        if (time=='10:00' or time=='13:30'):
            return True
        else:
            raise customexception3.InvalidTimeException()
    except customexception3.InvalidTimeException as e:
        print(e)

def validate_tickets(total_seats,no_of_tickets,no,date):
    try:
        if(no_of_tickets<=4):
            if no_of_tickets<=total_seats:
                tickets=BookMovieDB.get_tickets(no,date)
                if (tickets+no_of_tickets)<=4:                
                    return True
                else:
                    raise customexception3.InvalidUserTicketException()
                
            else:
                raise customexception3.InvalidTicketException()
        else:
            print("You Cannot book more than 4 tickets per day")
    except customexception3.InvalidTicketException as e:
        print(e)
    except customexception3.InvalidUserTicketException as e:
        print(e)

def validate_balance(no,price):
    try:
        bal=BookMovieDB.get_balance(no)
        if (bal>=price):
            return True
        else:
            raise customexception3.InvalidBalanceException()
    except customexception3.InvalidBalanceException as e:
        print(e)
    