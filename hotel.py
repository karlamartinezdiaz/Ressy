#Karla Martinez 
#CS302 Karla Fant 
#Class holding my hotel reservations 

from reservation import Reservation

#Derived class for Hotel from reservation 

#Will work with its own data and initialize 
#base class data 
class Hotel(Reservation): 

#initialization for Hotel 
    def __init__(self, reservation, beds, nights):
        super().__init__(reservation.first_name, reservation.last_name, reservation.party, reservation.date, reservation.venue_name)
        self.beds = beds
        self.nights = nights 
    
#display function for the hotel 
    def display(self):
        print("--------Hotel--------")
        print("Beds needed: ", self.beds)
        print("Nights needed : ", self.nights)
        print("Venue Name : ", self.venue_name)

#function to get the information from 
#user to place into the hotel object 
#Will return the object to be used in
#the tree 

def get_hotel(ressy):
    beds = input("How many beds would you like in the room? : ")
    nights = input("How many nights would you like to book for? : ")
    object = Hotel(ressy, beds, nights)
    return object


    


