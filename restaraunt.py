#Karla Martinez 
#CS302 Karla Fant 
#Class holding my restaraunt reservations 

from reservation import Reservation
#Restaraunt class derived from reservation class 
#Will work with its own data and initialize 
#base class data 
class Restaraunt(Reservation):

    def __init__(self, reservation = None, allergies = None, time = 0):
        super(). __init__(reservation.first_name, reservation.last_name, reservation.party, reservation.date, reservation.venue_name)
        self.allergies = allergies 
        self.time = time 

    #fucntion to add to the allergies list 
    def add_allergies(self, adding):
        self.allergies.append(adding)

    #fucntions to display the restaraunts 
    #information 
    def display(self):
        print("---------Restaraunt---------")
        print("Allergies : ", self.allergies)
        print("Time : ", self.time)
        print("Venue Name : ", self.venue_name)

    #Function to display the allergies of client 
    def display_allergies(self):
        print(self.allergies)
    



#function to get the information from 
#user to place into the restaraunt object 
#Will return the object to be used in
#the tree 

def get_restaraunt(ressy):
    object = Restaraunt(ressy)
    time = input("What would you like your time of arrival to be? : (00:00 AM / 00:00 PM : ")
    allergies = []

    answer = input("Do you have any allergies? (yes or no) : ")
    while answer.lower() == 'yes':
        allergy = input("Please enter what you are allergic to: ")
        allergies.append(allergy)
        answer = input("Would you like to enter another allergy? (yes or no): ")
    object = Restaraunt(ressy, allergies, time)
    return object
    
    

        




