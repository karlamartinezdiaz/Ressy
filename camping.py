#Karla Martinez 
#CS302 Karla Fant 
#Class holding my camping reservations 

from reservation import Reservation 

#Camping class derived from reservation class 
#Will work with its own data and initialize 
#base class data 


class Camping(Reservation):
    def __init__(self, reservation = None, nights = 0, size = None):
        super().__init__(reservation.first_name, reservation.last_name, reservation.party, reservation.date, reservation.venue_name)
        self.nights = nights 
        #self.cabin_size = cabin_size
        self.size = size

    #fucntion to chnage the size of lot 
    def change_lot_size(self, new_size):
        size = new_size

    #function to change the cabin size 
    def change_cabin_size(self, new_size):
        self.size = new_size

    #displays the camping information 
    def display(self):
        print("--------Camping--------")
        print(f"Nights reserved : {self.nights}")
        print(f"Size : {self.size}")
        print(f"Venue Name : {self.venue_name}")

#function to get the information from 
#user to place into the camping object 
#Will return the object to be used in
#the tree 

def get_camping(ressy):
    nights = input("How many nights would you like to reserve a spot for? : ")
    option = input("If you'd like a cabin enter 1, if you'd like a lot enter 2 : ")
    if(option == '1'):
        print("Would you like a small, medium or large cabin?")
        print("Please keep in mind that : ") 
        print("__________________________________________________________")
        print("Small cabins are ideal for parties of 1 - 5")
        print("__________________________________________________________")
        print("Medium is ideal for parties of 5 - 8")
        print("__________________________________________________________")
        print("Large is ideal for parties of size 8 - 15")
        size = input(": ")
        print(f"ok you have selected a {size} cabin")
    if(option == '2'):
        print("Would you like a small, medium or large lot?")
        print("Please keep in mind that : ")
        print("__________________________________________________________")
        print("Small lots are ideal for parties of 1 - 5 and can hold")
        print("a single RV or up to two small tents and a vehicle")
        print("__________________________________________________________")
        print("Medium is ideal for parties of 5 - 8")
        print("and can hold up to one RV as well as two small tents")
        print("__________________________________________________________")
        print("Large is ideal for parties of size 8 - 15") 
        print("and can hold up to two RV's as well as 3 tents")
        size = input(": ")
        print(f"You have selected a {size} lot size ")

    object = Camping(ressy, nights, size)
    return object

