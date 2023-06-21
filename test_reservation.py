#Karla Martinez 
#pytest for reservation class 


from reservation import Reservation

import pytest 
#tetsing the reservation file 
#test suite to assure that whats 
#expected is happening 

def test_reservation():
    # Test if the class initializes properly
    res = Reservation("Karla", "Martinez", 5 , "06-02-1997")
    assert res.first_name == "Karla"
    assert res.last_name == "Martinez"
    assert res.party == 5
    assert res.date == "06-02-1997"




