import sys, os
import sscapi
import numpy as np
import pandas as pd 
import solar_input, wind_input


def test_year_value_input():
# check if input year is in the right range
    list=[2007,2008,2009,2010,2011,2012]
    year=2010
    if year in list:
        pass
    else:
        raise Exception("cannot get useful info of year")
        
def test_location_value_input(): 
#check if input location is in the right range
    try:
        solar_input.solar(-30,100,2010)
    except (Exception):
        pass
    else:
        raise Exception("cannot get useful info of location ")

def test_solar_value_output():
    # check if output of daily solar is right value
    a,b = solar_input.solar(30,-100,2010)
    assert a.iloc[0]['generation']==9.915022276341915,'cannot get right daily solar value'
    #check if output of generation solar is right value
    assert b == 3224.3481877838713,'cannot get right generation solar value'

def test_shape_value_output():
    #check if out of daily solar has right day value
    c,d = solar_input.solar(30,-100,2010)
    assert c.shape == (365, 1),'cannot get all the daily solar value'
    #check if out of daily solar are dataframe
    if isinstance(c, pd.DataFrame):
        pass
    else:
        raise Exception('Bad type', 'Not a dataframe')
    return

def test_shape_value_output():  
#check if out of daily solar has right day value
    c,d = solar_input.solar(30,-100,2010)
    assert c.shape == (365, 1),'cannot get all the daily solar value'
#check if out of daily solar are dataframe
    if isinstance(c, pd.DataFrame):
        pass
    else:
        raise Exception('Bad type', 'Not a dataframe')
    return


