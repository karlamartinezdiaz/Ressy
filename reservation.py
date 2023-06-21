#Karla Martinez
#File holding my Reservation
#class, this class is the base class 
#that is the basic information needed 
#for the rest of the program 
#commonalities like name, and venue name
#will be placed in here and the derived 
#classes will have access through being a 
#derived class of this class 


import os 
import numpy as np


class Reservation:
    #will initialize the reservations members
    def __init__(self, first_name = None, last_name = None, party = 0, date = None, venue_name = None):
        self.first_name = first_name
        self.last_name = last_name
        self.party = party
        self.date = date 
        self.venue_name = venue_name

    #Will display the reservatiosn basic information 

    def display(self):
        print("First name : ", self.first_name)
        print("Last Name : ", self.last_name)
        print("Party : ", self.party)
        print("Date of arrival : ", self.date)
        print("Venue : ", self.venue_name)


    def change_date(self, new_date):
        self.date = new_date
    
    #Will return the venue name to 
    #be used in tree to sort by name 
    #of venue 

    def get_venue(self):
        return self.venue_name
    
    #operator overload for the == 
    #Will compare two venues and return true 
    #If they match and false if they dont match 

    def __eq__ (self, compare):
        if (self.venue_name == compare):
            return True 
        return False 
    
    #Operator overload of the < 
    # will be used in the tree to determine where in the 
    #tree the venue should go to 

    def __lt__ (self, compare):
        if(isinstance(compare, self.__class__)):
            return self.venue_name < compare.get_venue()
        return False 

    #Operator overload of the > 
    # will be used in the tree to determine where in the 
    #tree the venue should go to 
    def __gt__(self, compare):
        if(isinstance(compare, self.__class__)):
            return self.venue_name > compare.get_venue()
        return False 


#function to get the information from 
#user to place into the reservation object 
#Will return the object to be used in
#by the derived functions 
 
def get_basic_info():
    first_name = input("Please enter your first name : ")
    last_name = input("Please enter your last name: ")
    #print(type(party)) checks what data type this is 
    party = int(input("How many in your party? "))
    date = input("What date would you like to book for? (m/d/y)")
    venue_name = input("What is the venue? : ")
    object = Reservation(first_name, last_name, party, date, venue_name)
    return object

#object = get_basic_info()








