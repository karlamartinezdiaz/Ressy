#Karla Martinez 
#CS302 Karla Fant 
from reservation import *
from camping import * 
from restaraunt import * 
from data_structure import *
from hotel import *

#Main file to manmage all reservation 
#classes and direct "traffic" 

#from reservation import get_basic_info 
#from hotel import Reservation 
#from restaraunt import Restaraunt

def main():
    print("Welcome to Resy reservations.")
    bst = tree()
    option = input("\nWould you like to continue? Press 1 for yes and anything else for no: ")
    
    while(option == '1'):
        #ressy = get_basic_info()
        
        print("\nWhat kind of reservation would you like to make? ")
        print("1. Camping")
        print("2. Restaraunt")
        print("3. Hotel")
        print("4. Display all reservations")
        print("5. Remove a venue")
        print("6. Retrieve")
 
        reservation_type = input(": ")

        if(reservation_type == '1'):
            ressy = get_basic_info() 
            print(f"You selected {reservation_type} for Camping")
            print("Now lets get some basic information for your camping trip")
            camping = get_camping(ressy)
            bst.insert(camping)
            #bst.display_()

        if(reservation_type == '2'):
            ressy = get_basic_info()
            print(f"You selected {reservation_type} for restaraunt")
            print("Now lets get some basic information")
            restaraunt = get_restaraunt(ressy)
            bst.insert(restaraunt)
            
            #restaraunt.display_allergies()

        if(reservation_type == '3'):
            ressy = get_basic_info()
            print(f"You selected {reservation_type} for Hotel")
            print("Now lets get some basic information")
            hotel = get_hotel(ressy)
            bst.insert(hotel)
            
        
        if(reservation_type == '4'):
            bst.display_()

        if(reservation_type == '5'):
            bst.display_()
            to_delete = input("Which venue would you like to delete : ")
            bst.delete(to_delete)

        if(reservation_type == '6'):
            bst.display_()
            name = input("\nWhich venue would you like to retrieve ? : ")
            here = bst.retrieve(name)
            if(here != None):
                print("\nHere ya go : ")
                here.data.display()
            else: 
                print("not found, sorry x.x")

           

        option = input("\nWould you like to continue(enter 1), enter anything else to exit (x.X) ? :  ") 

       

if __name__ == "__main__": 
    main()









