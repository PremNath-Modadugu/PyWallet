'''
Created on Aug 9, 2017

@author: nagamani.undralla
'''
class BookMovie:
    def __init__(self):
        self.__moviename=None
        self.__language=None
        self.__price=None
        self.__movieid=None
        self.__no_of_seats1=None
        self.__no_of_seats2=None
        self.__showtime1=None
        self.__showtime2=None
        self.__no_of_booked1=None
        self.__no_of_booked2=None

    def get_no_of_booked1(self):
        return self.__no_of_booked1

    def get_no_of_booked2(self):
        return self.__no_of_booked2

    def set_no_of_booked1(self,no_of_booked1):
        self.__no_of_booked1 = no_of_booked1

    def set_no_of_booked2(self,no_of_booked2):
        self.__no_of_booked2 = no_of_booked2
        
    def get_showtime1(self):
        return self.__showtime1

    def get_showtime2(self):
        return self.__showtime2

    def set_showtime1(self,showtime1):
        self.__showtime1 =showtime1

    def set_showtime2(self,showtime2):
        self.__showtime2 =showtime2
        
    def get_no_of_seats1(self):
        return self.__no_of_seats1

    def get_no_of_seats2(self):
        return self.__no_of_seats2

    def set_no_of_seats1(self,no_of_seats1):
        self.__no_of_seats1 = no_of_seats1

    def set_no_of_seats2(self,no_of_seats2):
        self.__no_of_seats2 = no_of_seats2

    def set_movieid(self,movieid):
        self.__movieid=movieid
        
    def get_movieid(self):
        return self.__movieid

    def get_moviename(self):
        return self.__moviename

    def get_language(self):
        return self.__language

    def get_price(self):
        return self.__price

    def set_moviename(self,moviename):
        self.__moviename =moviename

    def set_language(self,language):
        self.__language = language

    def set_price(self,price):
        self.__price =price
   
    
    