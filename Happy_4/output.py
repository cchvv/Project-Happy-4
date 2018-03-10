from Happy_4 import solar_input, wind_input
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

'''
The file can download wind and solar energy database, and find the best way to combine these two kinds of energy. The result is the ratio of wind and solar energy. With this ratio, the daily total energy has the least standard error.
'''
#get the total power dataframe
def output_loop(lat, lon, year, x, y, df_solar, df_wind):
    a = []
    for i in range(len(df_solar)):
        a.append(x*df_solar.iloc[i]['generation'] + y*df_wind.iloc[i]['generation'])
    final = pd.DataFrame(a, columns = ['generation']) 
    final = final.set_index(pd.date_range('1/1/{yr}'.format(yr=year), freq='1'+'D', periods=len(df_solar)))
    return final

#output the best proportion of system capacities of solar and wind power and figues of solar, wind, and total power per day.
def checkout(lat, lon, year, Daily_solar, Daily_wind):
    a = []
    b = []
    c = []
    
    for x in np.arange(0.1,1,0.001):
        y = 1-x
        a.append(x)
        b.append(y)
        c.append(output_loop(lat, lon, year, x, y, Daily_solar, Daily_wind).std().values[0])
    A = pd.DataFrame(a, columns = ['x'])
    B = pd.DataFrame(b, columns = ['y'])
    C = pd.DataFrame(c, columns = ['StandardError'])
    D = pd.concat([A, B, C], axis = 1)
    
    
    for i in range (len(D)):
        if D.StandardError[i] == D.StandardError.min():
            x_value = D.x[i]
            y_value = D.y[i]
    
    
    b = []
    for i in range(len(Daily_solar)):
        b.append(x_value*Daily_solar.iloc[i]['generation'] + y_value*Daily_wind.iloc[i]['generation'])
    final = pd.DataFrame(b, columns = ['generation']) 
    final = final.set_index(pd.date_range('1/1/{yr}'.format(yr=year), freq='1'+'D', periods=len(Daily_solar)))
    
    average_solar_energy = Daily_solar.sum()/len(Daily_solar)
    average_wind_energy = Daily_wind.sum()/len(Daily_wind)
    
    print('the number ratio of solar panels and wind turbines is %f : %f' %(x_value, y_value))
    print('the average daily solar energy a solar panel can product is %f kW' %average_solar_energy)
    print('the average daily windr energy a wind turbine can product is %f kW' %average_wind_energy)
    
    plt.subplots(figsize = (50,30))
    
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
    
    return
