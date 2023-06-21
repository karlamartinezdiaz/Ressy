#Karla Martinez 
#pytest for hotel 

from reservation import Reservation
from hotel import Hotel
import pytest
#tetsing the hotel file 
#test suite to assure that whats 
#expected is happening 

def test_hotel():
    # Test if the class initializes properly
    reservation = Reservation("Karla", "Martinez", 5, "06-02-1997")
    hotel = Hotel(reservation, 2, 3)
    assert hotel.first_name == "Karla"
    assert hotel.last_name == "Martinez"
    assert hotel.party == 5
    assert hotel.date == "06-02-1997"
    assert hotel.beds == 2
    assert hotel.nights == 3

