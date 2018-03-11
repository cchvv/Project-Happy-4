import numpy as np
import pandas as pd 
import math
from Happy_4 import solar_input, wind_input
from Happy_4.output import output_loop, checkout
from geopy.geocoders import Nominatim
"""
check if we can get the total power dataframe, check if the different proportion of system capacities of solar and wind power add equal to 1
"""

def test_output_loop():
#check if we can get the total power dataframe
    t,j = solar_input.solar(30,-100,2010)
    m,n = wind_input.wind(30,-100,2010)
    d= output_loop(30,-100,2010,0.5,0.5,t,m)
    if isinstance(d, pd.DataFrame):
        pass
    else:
        raise Exception('Bad type', 'Not a dataframe')
    return

#check if we can get right total value from wind and solar dataframe
    i=0
    assert output_loop(30,-100,2010,0.5,0.5,t,m).iloc[i]['generation']==0.5*x.iloc[i]['generation'] + 0.5*m.iloc[i]['generation'],'cannot get right total energy value'

def test_checkout():
    #check if the different proportion of system capacities of solar and wind power add equal to 1
    a = []
    b = []
    c = []
    t,j = solar_input.solar(30,-100,2010)
    m,n = wind_input.wind(30,-100,2010)
    for x in np.arange(0.1,1,0.001):
        y = 1-x
        a.append(x)
        b.append(y)
        c.append(output_loop(30,-100,2010,x,y,t,m).std().values[0])
    A = pd.DataFrame(a, columns = ['x'])
    B = pd.DataFrame(b, columns = ['y'])
    C = pd.DataFrame(c, columns = ['StandardError'])
    D = pd.concat([A, B, C], axis = 1)

    assert D.x[5]+D.y[5]==1,'cannot get right proportion'

    for i in range (len(D)):
        if D.StandardError[i] == D.StandardError.min():
            index = i
            T=index+1
            x_value = D.x[i]
            y_value = D.y[i]
        
        #check if  D.StandardError[i] is min value
    if D.StandardError[index] < D.StandardError[T]:
        pass
    else:
        raise Exception("cannot get min D.StandardError[i]")
