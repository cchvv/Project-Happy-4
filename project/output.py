import sys, os
import sscapi
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd 
import statsmodels.api as sm
from sklearn import linear_model
from sklearn.linear_model import LogisticRegression
import statsmodels.formula.api as smf
import math
import os
from sklearn.model_selection import learning_curve
from sklearn.svm import SVC
import solar_input,wind_input



def output_loop(lat, lon, year, x, y , df_solar, df_wind):
    a = []
    for i in range(len(df_solar)):
        a.append(x*df_solar.iloc[i]['generation']+y*df_wind.iloc[i]['generation'])
    final = pd.DataFrame(a, columns=['generation']) 
    final = final.set_index(pd.date_range('1/1/{yr}'.format(yr=year), freq='1'+'D', periods=len(df_solar)))
    return final


def checkout(lat, lon, year, Daily_solar, Daily_wind):
    a=[]
    b=[]
    c=[]
    
    for x in np.arange(0.1,1,0.001):
        y = 1-x
        a.append(x)
        b.append(y)
        c.append(output_loop(47.61, -122.34, 2010, x, y, Daily_solar, Daily_wind).std().values[0])
    A=pd.DataFrame(a,columns=['x'])
    B=pd.DataFrame(b,columns=['y'])
    C=pd.DataFrame(c,columns=['StandardError'])
    D = pd.concat([A,B,C],axis = 1)
    
    
    for i in range (len(D)):
        if D.StandardError[i] == D.StandardError.min():
            index = i
            x_value = D.x[i]
            y_value = D.y[i]
    
    
    b = []
    for i in range(len(Daily_solar)):
        b.append(x_value*Daily_solar.iloc[i]['generation']+y_value*Daily_wind.iloc[i]['generation'])
    final = pd.DataFrame(b, columns=['generation']) 
    final = final.set_index(pd.date_range('1/1/{yr}'.format(yr=year), freq='1'+'D', periods=len(Daily_solar)))
  

    plt.subplots(figsize = (60,10))
    
    plt.subplot(311)
    plt.plot(Daily_solar.index,Daily_solar.generation)
    plt.xlabel('Date')
    plt.ylabel('kW')
    plt.title('Daily_solar')
    
    plt.subplot(312)
    plt.plot(Daily_wind.index,Daily_wind.generation)
    plt.xlabel('Date')
    plt.ylabel('kW')
    plt.title('Daily_wind')
    
    plt.subplot(313)
    plt.plot(final.index,final.generation)
    plt.xlabel('Date')
    plt.ylabel('kW')
    plt.title('Daily_solar + Daily_wind')
    plt.show()
    print('the proportion of system capacities of solar and wind power is %f : %f' %(x_value, y_value))
    return
