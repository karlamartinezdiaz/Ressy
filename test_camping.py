#Karla Martinez 
#CS302 Karla Fant 

#tetsing the campping file 
#test suite to assure that whats 
#expected is happening 


from camping import Camping
from reservation import Reservation  

import pytest

def test_camping():
    # Test if the class initializes properly
    res = Reservation("Karla", "Martinez", 5, "06-02-1997")
    camp = Camping(res, 3, "medium")
    
    assert camp.nights == 3
    assert camp.size == "medium"
    assert camp.first_name == "Karla"
    assert camp.last_name == "Martinez"
    assert camp.party == 5
    assert camp.date == "06-02-1997"

# def test_change_lot_size():
#     # Test if the change_lot_size method is working correctly
#     res = Reservation("Karla", "Martinez", 5, "06-02-1997")
#     camp = Camping(res, 3, "medium")
    
    # camp.change_lot_size("large")
    # assert camp.size == "large"










