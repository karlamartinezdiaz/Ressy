#Name : Karla Martinez 
#CS302 Karla Fant
#

import numpy as np 




class Venues():
    def __init__ (self):
        self.camping_arr = np.array([])
        self.hotel_arr = np.array([])
        self.restaraunt_arr = np.array([])
        #self.arr = arr 
    
    def add_venue(self, venue_type, venue_name):
        if(venue_type == "camping"):
            self.camping_arr = np.append(self.camping_arr, venue_name)
        if(venue_type == "hotel"):
            self.hotel_arr = np.append(self.hotel_arr, venue_name)
        if(venue_type == "restaraunt"): 
            self.restaraunt_arr = np.append(self.restaraunt_arr, venue_name)

    def display_venue(self, venue_name):
        if(venue_name == "camping"):
            for x in self.camping_arr:
                print(f"Venue name : {x}")

        if(venue_name == "hotel"):
            for x in self.hotel_arr:
                print(f"Venue name : {x}") 

        if(venue_name == "restaraunt"):
            for x in self.restaraunt_arr:
                print(f"Venue name : {x}") 

def main ():
    choice = input("Want to add a venue? 1 for yes:  ")
    object = Venues()
    while (choice == '1'):
        venue_type = input("Enter venue type(camping, hotel, restaraunt)")
        venue_name = input("Enter a venue name: ")
        object.add_venue(venue_type, venue_name)
        choice = input("Another? : ")
    
    option = input("Would you like to see a venue? 1 for yes, anything else for no:  ")
    while(option == '1'):
        venue = input("Which venue would you like to see?(camping, hotel or restaraunt) : ")
        object.display_venue(venue)
        option = input("Would you like to see another venue? 1 for yes, anything else for no:   ") 
    #object.display_venue("restaraunt")
    #object.display_venue("camping")

   

if __name__ == "__main__": 
    main()

# print()
# arr = np.array([])

# list = [1, 2, 3, 8]
# print(list)

# arr = np.array([1,2,4,5])
# print(arr)

# new_arr= np.append(arr,3)
# print(new_arr)
# print(arr[1])






