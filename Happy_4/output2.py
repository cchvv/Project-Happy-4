from Happy_4 import solar_input, wind_input
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

'''
The file can download wind and solar energy database, and find the best way to combine these two kinds of energy. The result is the ratio of wind and solar energy. With this ratio, the daily total energy has the least standard error.
'''
#get the total power dataframe
def output_loop(year, x, y, df_solar, df_wind):
    a = []
    for i in range(len(df_solar)):
        a.append(x*df_solar.iloc[i]['generation'] + y*df_wind.iloc[i]['generation'])
    final = pd.DataFrame(a, columns = ['generation']) 
    final = final.set_index(pd.date_range('1/1/{yr}'.format(yr=year), freq='1'+'D', periods=len(df_solar)))
    return final

#output the best proportion of system capacities of solar and wind power and figues of solar, wind, and total power per day.
def checkout(locat, year, Daily_solar, Daily_wind, Daily_demand):
    a = []
    b = []
    c = []
    
    for x in np.arange(0.1,1,0.001):
        y = 1-x
        a.append(x)
        b.append(y)
        c.append(output_loop(year, x, y, Daily_solar, Daily_wind).std().values[0])
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
    
    # make the plot and print infomation
    plt.figure(figsize=(20,10))
    plt.plot(Daily_solar, label='solar energy')
    plt.plot(Daily_wind, label='wind energy')
    plt.plot(final, label='solar energy + wind energy')
    #plt.plot(daily_demand_average, label='electricity demand')
    plt.title(locat, fontsize = 10)
    plt.ylabel('kW', fontsize = 10)
    plt.xticks(['2019-01','2019-03','2019-05','2019-07','2019-09','2019-11','2020-01'],['01','03','05','07','09','11','01'])
    plt.legend(fontsize = 10)
    plt.tick_params(axis='both', which='major', labelsize=10)
    plt.show()

    # find the ratio k
    k = 2000* Daily_demand['demand'].sum() / (x_value * Daily_solar['generation'].sum() + y_value * Daily_wind['generation'].sum())
    print(locat + ':')
    print('the ideal ratio for the combination of solar panels and wind turbines is %f : %f' %(x_value, y_value))
    print('the resulting stand error of the combinational generation is %f' % D.StandardError.min()) 
    print('the total number of solar panels and wind turbines needed to meet the electricity demand are %i and %i' % (int(x_value*k), int(y_value*k)))

    return
