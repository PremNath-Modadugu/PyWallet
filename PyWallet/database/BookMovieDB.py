'''
Created on Aug 9, 2017

@author: nagamani.undralla
'''
from utility import DBConnectivity
from classes.BookMovieModule import BookMovie
      
'''validating date given'''         
def dateofmovie(date):
    l=[]
    con=DBConnectivity.create_connection()
    cur=DBConnectivity.create_cursor(con)  
    cur.execute("select dateofmovie from BookMovie")    
    for i in cur:        
        l.append(i[0])
    
    return l

'''validating language'''
def language(mdate,language):
    con=DBConnectivity.create_connection()
    cur=DBConnectivity.create_cursor(con)
    cur.execute("select language from BookMovie where dateofmovie=:date1",{"date1":mdate})
    l=[]
    for row in cur:
        l.append(row[0].lower())
    return l


def movies(mdate,language):
    con=DBConnectivity.create_connection()
    cur=DBConnectivity.create_cursor(con)        
    cur.execute("select moviename,price,no_of_seats1,no_of_seats2,showtime1,showtime2,no_of_booked1,no_of_booked2 from BookMovie where (Dateofmovie =:dateofmovie and lower(Language)=:language)",{"dateofmovie":mdate,"language":language.lower()})
    list_of_movies=[]
    count=1
    for moviename,price,no_of_seats1,no_of_seats2,showtime1,showtime2,no_of_booked1,no_of_booked2 in cur:
        '''
        In this loop, we are creating a movie object for every row
        and setting the values from the row into the movie object
        '''
        movie=BookMovie()
        movie.set_movieid(count)
        movie.set_language(language)          
        movie.set_moviename(moviename)
        movie.set_price(price)  
        movie.set_showtime1(showtime1)
        movie.set_showtime2(showtime2)
        movie.set_no_of_seats1(no_of_seats1)
        movie.set_no_of_seats2(no_of_seats2)
        movie.set_no_of_booked1(no_of_booked1)
        movie.set_no_of_booked2(no_of_booked2)
        
        count+=1           
        '''
        Here we  are adding the movie to a list
        '''
        list_of_movies.append(movie)
    print("                      weekend movie @multiplex                      ")
    print("--------------------------------------------------------------------")
    print("---------MovieName            Show time                price--------")
    print("--------------------------------------------------------------------")
    for i in list_of_movies:
        print(str(i.get_movieid())+" "+i.get_moviename()+"("+i.get_language()+")"+"         "+i.get_showtime1()+"   "+i.get_showtime2()+"         "+str(i.get_price()))
    
    return list_of_movies

'''function for booking movie tickets'''
def booking(option,mdate,time,no_of_tickets,list_of_movies):
    for movie in list_of_movies:                        
        if movie.get_movieid()==option:
            moviename=movie.get_moviename()
    if time=='10:00':        
        con=DBConnectivity.create_connection()
        cur1=DBConnectivity.create_cursor(con) 
        cur1.execute("select no_of_booked1 from bookmovie where (dateofmovie=:date1 and moviename=:moviename)",{"date1":mdate,"moviename":moviename})
        for row1 in cur1:                    
            no_of_seats=row1[0]  
        total_seats=no_of_seats+int(no_of_tickets)                                
        cur1.execute("update BookMovie set no_of_booked1 =:total_seats where (dateofmovie=:date1 and moviename=:moviename)",{"total_seats":total_seats,"date1":mdate,"moviename":moviename})
        con.commit()
    
    elif time=='13:30':
        con=DBConnectivity.create_connection()
        cur1=DBConnectivity.create_cursor(con) 
        cur1.execute("select no_of_booked2 from bookmovie where (dateofmovie=:date2 and moviename=:moviename)",{"date2":mdate,"moviename":moviename})
        for row1 in cur1:                    
            no_of_seats=row1[0]          
        total_seats=no_of_seats+int(no_of_tickets)
        cur1.execute("update BookMovie set no_of_booked2 =:total_seats where (dateofmovie=:date2 and moviename=:moviename)",{"total_seats":total_seats,"date2":mdate,"moviename":moviename})
        con.commit()      
    return no_of_seats

'''checks for maximum number of tickets booked by a user per day'''
def get_tickets(no,mdate):
    try:
        con=DBConnectivity.create_connection()
        cur=DBConnectivity.create_cursor(con)
        cur.execute("select sum(ticketspurchased) from ticketstatus where mobilenumber=:no1 and mdate=:date1 group by mdate",{"no1":no,"date1":mdate})
        k=cur.fetchall()
        if(len(k))>0:
            for i in k:
                ticket=i[0]
        else:
            return 0
        return ticket
    finally:
        cur.close()
        con.close()

'''retreives the balance of user'''
def get_balance(no):
    try:
        con=DBConnectivity.create_connection()
        cur=DBConnectivity.create_cursor(con)
        cur.execute("select balance from PyUsers where mobilenumber=:no1",{"no1":no})
        for row in cur:
            balance=row[0]
        return balance
    finally:
        cur.close()
        con.close()
    
'''updating the table ticketstatus'''
def update_movie_user(no,mdate,no_of_tickets):
    try:
        con=DBConnectivity.create_connection()
        cur=DBConnectivity.create_cursor(con)
        cur.execute("insert into ticketstatus values(:no1,:date1,:no_of_tickets)",{"no1":no,"date1":mdate,"no_of_tickets":no_of_tickets})
        con.commit()
    finally:
        cur.close()
        con.close()
        
'''updating the wallet balance of the user'''
def update_balance(users,no,price):
    try:
        con=DBConnectivity.create_connection()
        cur=DBConnectivity.create_cursor(con)
        cur.execute("select balance from PyUsers where mobilenumber=:no1",{"no1":no})
        for row in cur:
            bal=row[0]
        bal=bal-price
        users.set_balance(bal)
        cur.execute("update PyUsers set balance=:bal1 where (mobilenumber=:num)",{"bal1":bal,"num":no})
        con.commit()
    finally:
        cur.close()
        con.close()



    