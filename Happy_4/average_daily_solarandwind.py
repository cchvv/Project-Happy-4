from Happy_4 import solar_input
from Happy_4 import wind_input
import pandas as pd

'''
This file can use data from 2007 to 2012 to calculate the average daily data.
'''
def leap_year_bool(yr):
    if yr % 4 ==0:
        if yr % 100 ==0:
            if yr % 400 ==0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def average_daily_solar(lat, lon):
    
    # collect the data of 2007, 2009, 2010, 2011
    daily_solar_total = pd.DataFrame()
    generation_solar_total = []
    for y in [2007, 2009, 2010, 2011]:
        daily_solar, generation_solar = solar_input.solar(lat, lon, y)

        # drop the data on 02/29
        #if leap_year_bool == True:
            #daily_solar = daily_solar.drop(pd.to_datetime(year+'-02-29')
        #else:
           #pass
        
        daily_solar_total = daily_solar_total.append(daily_solar)
        generation_solar_total.append(generation_solar)
        
        # average the daily solar energy data for each day                                  
        daily_solar_average_group = daily_solar_total.groupby([daily_solar_total.index.month, daily_solar_total.index.day]).mean()
        daily_solar_average_list = []
        for date, value in daily_solar_total.groupby([daily_solar_total.index.month, daily_solar_total.index.day]):
            daily_solar_average_list.append(daily_solar_average_group.loc[date][0])
        daily_solar_average = pd.DataFrame(daily_solar_average_list, columns=['generation'])
        daily_solar_average = daily_solar_average.set_index(pd.date_range('1/1/2019', freq='1D', periods=365))
        
        # average the generation of solar energy 
        generation_solar_average = sum(generation_solar_total) / len(generation_solar_total)
        
    return daily_solar_average, generation_solar_average


def average_daily_wind(lat, lon):
    
    # collect the data of 2007, 2009, 2010, 2011
    daily_wind_total = pd.DataFrame()
    generation_wind_total = []
    for y in [2007, 2009, 2010, 2011]: 
        daily_wind, generation_wind = wind_input.wind(lat, lon, y)
        
        # drop the data on 02/29
        #if leap_year_bool == True:
            #daily_wind = daily_wind.drop(pd.to_datetime(year+'-02-29')
        #else:
           #pass
        
        daily_wind_total = daily_wind_total.append(daily_wind)
        generation_wind_total.append(generation_wind)
        
        # average the daily wind energy data for each day                                  
        daily_wind_average_group = daily_wind_total.groupby([daily_wind_total.index.month, daily_wind_total.index.day]).mean()
        daily_wind_average_list = []
        for date, value in daily_wind_total.groupby([daily_wind_total.index.month, daily_wind_total.index.day]):
            daily_wind_average_list.append(daily_wind_average_group.loc[date][0])
        daily_wind_average = pd.DataFrame(daily_wind_average_list, columns=['generation'])
        daily_wind_average = daily_wind_average.set_index(pd.date_range('1/1/2019', freq='1D', periods=365))
        
        # average the generation of wind energy 
        generation_wind_average = sum(generation_wind_total) / len(generation_wind_total)
        
    return daily_wind_average, generation_wind_average
