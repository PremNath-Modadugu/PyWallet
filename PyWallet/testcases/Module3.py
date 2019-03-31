'''
Created on Aug 10, 2017

@author: nagamani.undralla
'''
from validations.BookMovieValidations import validate_date,validate_language,validate_tickets,validate_time
from exceptions.customexception3 import InvalidDateException,InvalidLanguageException,InvalidTimeException,InvalidUserTicketException



'''
positive test cases 
'''
print(validate_date('15-08-2017')) #positive test case for validating date
print(validate_language('15-08-2017','English')) #positive test case for validating language
print(validate_time('10:00')) #positive test case for validating time
print(validate_tickets(100,4,9912459019,'18-08-2017'))

'''
negative test cases 
'''

try:
    listofmovies=validate_date('26-08-2017')
except InvalidDateException as e:
    print(e)
try:
    listofmovies=validate_date('30-08-2017')
except InvalidDateException as e:
    print(e)
 
try:
    time=validate_time('10:20')
except InvalidTimeException as e:
    print(e)
try:
    time=validate_time('14:20')
except InvalidTimeException as e:
    print(e)

try:
    lang=validate_language('26-08-2017','hindi')
except InvalidLanguageException as e:
    print(e)
try:
    lang=validate_language('27-08-2017','english')
except InvalidLanguageException as e:
    print(e)
    
try:
    vt=validate_tickets(100,5,9912459019,'16-08-2017')
except InvalidUserTicketException as e:
    print(e)
try:
    vt=validate_tickets(100,8,8501944054,'16-08-2017')
except InvalidUserTicketException as e:
    print(e)