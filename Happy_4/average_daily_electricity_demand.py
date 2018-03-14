
import pandas as pd
import requests
import numpy as np
import math


# Create a dataframe of average daily demand of electricty of a chosen area.
def electricity_demand(input_name):
    
    # Create a dataframe to store the ID of all electric system 
    df = pd.read_excel('Happy_4/id.xlsx')
    df['URL'] = '0'
    for i in range(len(df['NAME'])):
        df['URL'][i] = 'http://api.eia.gov/series/?series_id=' + df['ID'][i] +'&api_key=dc18856f7f589c8cb34de219b44f58ac&out=json'
    name_list = df['ABBREVIATION'].tolist()
    
    if input_name in name_list:
        i = name_list.index(input_name)
 
        # download the data of electricity demand and convert it a pandas data frame
        url_data = df['URL'][i]
        values_dict = {}
        search = requests.get(url_data)
        lst_dates = [x[0][0:4] + "-" + x[0][4:6] + "-" + x[0][6:8] + " " + x[0][9:11] + ':00:00' for x in search.json()['series'][0]['data']]
        lst_values = [x[1] for x in search.json()['series'][0]['data']]
        demand = [('date', lst_dates), ('value', lst_values)]
        df_demand = pd.DataFrame.from_items(demand)
        df_demand.set_index('date', inplace = True)
            
        # convert index to datetime
        df_demand.index = pd.to_datetime(df_demand.index)
            
        # convert hourly data to daily data
        df_demand_daily = df_demand.resample('D').sum()
            
        # drop the last term
        df_demand_daily = df_demand_daily.drop(df_demand_daily.index[len(df_demand_daily)-1])
            
        # drop the NaN term
        df_demand_daily = df_demand_daily.dropna(axis=0, how='any')
        df_demand_daily.tail()
            
        # drop the data of 2016-02-29
        df_demand_daily = df_demand_daily.drop(pd.to_datetime('2016-02-29'))
            
        # average the daily electrcity demand for each day 
        df_demand_daily_group = df_demand_daily.groupby([df_demand_daily.index.month, df_demand_daily.index.day]).mean()
        daily_demand_average_list = []
        for date, value in df_demand_daily.groupby([df_demand_daily.index.month, df_demand_daily.index.day]):
            daily_demand_average_list.append(df_demand_daily_group.loc[date][0])
        daily_demand_average = pd.DataFrame(daily_demand_average_list, columns=['demand'])
        daily_demand_average = daily_demand_average.set_index(pd.date_range('1/1/2019', freq='1D', periods=365))
            
        return daily_demand_average
    
    else:
        print('The data of' + input_name + 'is not available.' )