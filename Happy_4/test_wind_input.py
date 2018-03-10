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
        wind_input.wind(-30,100,2010)
    except (Exception):
        pass
    else:
        raise Exception("cannot get useful info of location ")
        
def test_wind_value_output():      
# check if output of daily wind is right value 
    a,b = wind_input.wind(30,-100,2010)
    assert a.iloc[0]['generation']==12.914752278645834,'cannot get right daily wind value'
#check if output of generation solar is right value
    assert b == 4094.263194816311,'cannot get right generation wind value'

def test_shape_value_output():  
#check if out of daily wind has right day value
    c,d = wind_input.wind(30,-100,2010)
    assert c.shape == (365, 1),'cannot get all the daily wind value'
#check if out of daily wind are dataframe
    if isinstance(c, pd.DataFrame):
        pass
    else:
        raise Exception('Bad type', 'Not a dataframe')
    return


