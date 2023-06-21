

import numpy as np
import pytest
from venues import Venues 
#tetsing the venue file 
#test suite to assure that whats 
#expected is happening 

def test_venue():
    # Test if the class initializes properly
    v = Venues()
    assert isinstance(v.camping_arr, np.ndarray)
    assert isinstance(v.hotel_arr, np.ndarray)
    assert isinstance(v.restaraunt_arr, np.ndarray)

def test_add_venue():
    # Test if the add_venue method is working correctly
    v = Venues()
    v.add_venue('camping', 'Camping Spot 1')
    v.add_venue('hotel', 'Hotel Inn')
    v.add_venue('restaraunt', 'Random')
    
    assert 'Camping Spot 1' in v.camping_arr
    assert 'Hotel Inn' in v.hotel_arr
    assert 'Random' in v.restaraunt_arr


def test_display_venue(capfd):  # capfd is a built-in pytest fixture for capturing stdout and stderr.
    # Test if the display_venue method is working correctly
    v = Venues()
    v.add_venue('camping', 'Camping Spot 1')
    v.add_venue('hotel', 'Hotel Inn')
    v.add_venue('restaraunt', 'Random')
    
    v.display_venue('camping')
    out, err = capfd.readouterr()
    assert 'Camping Spot 1' in out

    v.display_venue('hotel')
    out, err = capfd.readouterr()
    assert 'Hotel Inn' in out

    v.display_venue('restaraunt')
    out, err = capfd.readouterr()
    assert 'Random' in out
