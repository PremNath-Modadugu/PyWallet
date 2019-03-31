'''
Created on Aug 9, 2017

@author: nagamani.undralla
'''

   
def generate_seat_number(movie_id,total_seats,no_of_tickets):   
    ticket_list=[]    
    
    a=(total_seats)
    b=(total_seats+no_of_tickets)
    if (movie_id==1):   
        for i in range(a+1,b+1):              
            ticket='A'+str(i)
            ticket_list.append(ticket)
            
            
    if (movie_id==2):   
        for i in range(a+1,b+1):              
            ticket='B'+str(i)
            ticket_list.append(ticket)  
            
            
    if (movie_id==3):   
        for i in range(a+1,b+1):              
            ticket='C'+str(i)
            ticket_list.append(ticket) 
            
            
    return ticket_list
