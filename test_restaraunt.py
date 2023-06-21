from restaraunt import Restaraunt 
from reservation import Reservation 

import pytest
#tetsing the restaraunt file 
#test suite to assure that whats 
#expected is happening 


def test_restaurant():
    # Test if the class initializes properly
    res = Reservation("Karla", "Martinez", 5, "06-02-1997")
    rest = Restaraunt(res, ["peanuts"], "18:00")

    assert rest.allergies == ["peanuts"]
    assert rest.time == "18:00"
    assert rest.first_name == "Karla"
    assert rest.last_name == "Martinez"
    assert rest.party == 5
    assert rest.date == "06-02-1997"

def test_add_allergies():
    # Test if the add_allergies method is working correctly
    res = Reservation("Karla", "Martinez", 5, "06-02-1997")
    rest = Restaraunt(res, ["peanuts"], "18:00")

    rest.add_allergies("gluten")
    assert "gluten" in rest.allergies








