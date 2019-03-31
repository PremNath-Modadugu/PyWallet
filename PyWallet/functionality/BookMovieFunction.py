'''
Created on Aug 9, 2017

@author: nagamani.undralla
'''


from functionality import seatfunction
from validations import BookMovieValidations,BankingValidation
from exceptions.customexception3 import InvalidChoiceException
from database import BookMovieDB, CheckDB
from classes.TransactionModule  import Transaction     
from database import InsertDB 
import math 

def BookMovie(users):
    transact=Transaction()
    no=users.get_mobile_number()
    end=False
    while (end==False):
        trans=0
        try:
            print('1.Book Movies')
            print('2.Go Back to Login Menu')
            choice=input('Choose an option: ')
             
            if (choice)=="1":
                end=True
                flag=False
                while (flag==False):
                    date=input('Enter Date: ')
                    if BookMovieValidations.validate_date(date): 
                        flag=True              
                        language=input('Choose a Language: ')
                        if BookMovieValidations.validate_language(date,language):                                      
                            list_of_movies=BookMovieDB.movies(date,language)                            
                            s=[]
                            opt=False
                            while (opt==False):
                                option=input('Choose an option: ')
                                for i in list_of_movies:
                                    s.append(i.get_movieid())
                                    
                                if option.isdigit() and int(option) in s: 
                                    option=int(option)
                                    opt=True                      
                                    b=False
                                    while(b==False):
                                        time=input('Enter the show timing for the movie: ')
                                        if BookMovieValidations.validate_time(time):  
                                            for i in list_of_movies:
                                                if i.get_movieid()==option:
                                                    seat1=i.get_no_of_seats1()
                                                    seat2=i.get_no_of_seats2()
                                                    price=i.get_price()
                                                    available1=seat1-i.get_no_of_booked1()
                                                    available2=seat2-i.get_no_of_booked2()
                                            b=True                       
                                            c=False
                                            while(c==False):
                                                no_of_tickets=input('Enter Number of tickets: ')
                                                total_price=math.ceil(price*int(no_of_tickets))+35.42
                                                if time=='10:00':
                                                    if BookMovieValidations.validate_tickets(available1,int(no_of_tickets),no,date):
                                                        if (BookMovieValidations.validate_balance(no,total_price)):
                                                            final=BookMovieDB.booking(option,date,time,int(no_of_tickets),list_of_movies)                                                      
                                                            c=True                          
                                                            l=seatfunction.generate_seat_number(option,final,int(no_of_tickets))
                                                            BookMovieDB.update_movie_user(no,date,int(no_of_tickets))
                                                            BookMovieDB.update_balance(users,no,total_price)
                                                            print('Seat Numbers: ',','.join(l))
                                                            print('Total Ticket Price (Including tax) :',total_price)
                                                            print('Booking Successful')
                                                            trans=1
                                                            print('Your Wallet Balance is: ',BookMovieDB.get_balance(no))
                                                        else:
                                                            end=True
                                                            c=True
                                                            b=True
                                                            opt=True
                                                            flag=True
                                                    else:
                                                        end=False
                                                        c=True
                                                        b=True
                                                        opt=True
                                                        flag=True
                                        
                                                            
                                                elif time=='13:30':
                                                    if BookMovieValidations.validate_tickets(available2,int(no_of_tickets),no,date):
                                                        if (BookMovieValidations.validate_balance(no,total_price)):
                                                            final=BookMovieDB.booking(option,date,time,int(no_of_tickets),list_of_movies)                                                      
                                                            c=True                      
                                                            l=seatfunction.generate_seat_number(option,final,int(no_of_tickets))
                                                            BookMovieDB.update_movie_user(no,date,int(no_of_tickets))
                                                            BookMovieDB.update_balance(users,no,total_price)
                                                            print('Seat Numbers: ',','.join(l))
                                                            print('Total Ticket Price (Including tax) :',total_price)
                                                            print('Booking Successful')
                                                            trans=1
                                                            print('Your Wallet Balance is: ',BookMovieDB.get_balance(no))
                                                        else:
                                                            end=True
                                                            c=True
                                                            b=True
                                                            opt=True
                                                            flag=True
                                                    else:
                                                        end=False
                                                        c=True
                                                        b=True
                                                        opt=True
                                                        flag=True
                                                
                                            if(trans==1):
                                                temp=transact.get_transaction_id()
                                                temp=BankingValidation.check_transid(temp)
                                                transact.set_transaction_id(temp)
                                                transact.set_mobile_number(users.get_mobile_number())
                                                remark="BIL/"+str(temp)+"/MB-/NPS"
                                                transact.set_remarks(remark)
                                                transact.set_type("Dr.")
                                                transact.set_amount(total_price)
                                                InsertDB.InsertTrarnsaction(transact)        
                                                
                                else:
                                    print('Invalid Option. Please choose another option')
                        else:
                            flag=False         
                    else:
                        flag=False
                print('Do You Wish to Continue? (Y/N)')
                ch=input()
                if ch.lower()=='y':
                    print("Your current wallet balance is: ",CheckDB.check_balance(users))
                    end=False
                elif(ch.lower()=='n'):
                    end=True
            
            elif(choice=='2'):
                end=True
                
            
            else:
                raise InvalidChoiceException()           
            
                
        
        except InvalidChoiceException as e:
            print(e)            
            

    
  
        