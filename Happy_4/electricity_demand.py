import pandas as pd
import requests
import numpy as np
import matplotlib.pyplot as plt
import math

# Create a dataframe to store the ID of all electric system 
df = pd.read_excel('id.xlsx')
df.head()
df['URL'] = '0'
for i in range(len(df['NAME'])):
    df['URL'][i] = 'http://api.eia.gov/series/?series_id=' + df['ID'][i] +'&api_key=dc18856f7f589c8cb34de219b44f58ac&out=json'

# Get input information from the user.
input_name = input("Please input the name of Energy System:")

def electricity_demand(input_name):
    import pandas as pd
    # Download the data of electricity demand and convert it a pandas data frame
    n = 0
    for i in range(len(df['NAME'])):
        if input_name == df['NAME'][i]:
            url_data = df['URL'][i]
            values_dict = {}
            search = requests.get(url_data)
            lst_dates = [x[0][0:4] + "-" + x[0][4:6] + "-" + x[0][6:8] + " " + x[0][9:11] + ':00:00' for x in search.json()['series'][0]['data']]
            lst_values = [x[1] for x in search.json()['series'][0]['data']]
            demand = [('date', lst_dates), ('value', lst_values)]
            df_demand = pd.DataFrame.from_items(demand)
            df_demand.set_index('date', inplace = True)
            df_demand.head()
            n = 1
    if n == 0:
        print("Sorry, this area is not in the prediction.")
    else:
        df_demand_series = pd.Series(lst_values, df_demand.index.to_datetime())
        df_demand_day = df_demand_series.resample('D').sum()
        pre = list()
        # July
        for i in range(0,31):
            ypred = (df_demand_day[i] + df_demand_day[i+366] + df_demand_day[i+731])/3
            pre.append(ypred)

        # Aug
        for i in range(31, 62):
            ypred = (df_demand_day[i] + df_demand_day[i+366] + df_demand_day[i+731])/3
            pre.append(ypred)

        # Sep
        for i in range(62, 92):
            ypred = (df_demand_day[i] + df_demand_day[i+366] + df_demand_day[i+731])/3
            pre.append(ypred)

        #Oct
        for i in range(92, 123):
            ypred = (df_demand_day[i] + df_demand_day[i+366] + df_demand_day[i+731])/3
            pre.append(ypred)

        #Nov
        for i in range(123, 153):
            ypred = (df_demand_day[i] + df_demand_day[i+366] + df_demand_day[i+731])/3
            pre.append(ypred)

        #Dec
        for i in range(153, 184):
            ypred = (df_demand_day[i] + df_demand_day[i+366] + df_demand_day[i+731])/3
            pre.append(ypred)

        #Jan
        for i in range(184, 215):
            ypred = (df_demand_day[i] + df_demand_day[i+366] + df_demand_day[i+731])/3
            pre.append(ypred)

        #Feb
        for i in range(215, 243):
            ypred = (df_demand_day[i] + df_demand_day[i+366] + df_demand_day[i+731])/3
            pre.append(ypred)

        #March
        for i in range(244, 275):
            ypred = (df_demand_day[i] + df_demand_day[i+365])/2
            pre.append(ypred)

        #April
        for i in range(275, 305):
            ypred = (df_demand_day[i] + df_demand_day[i+365])/2
            pre.append(ypred)

        #May
        for i in range(305, 336):
            ypred = (df_demand_day[i] + df_demand_day[i+365])/2
            pre.append(ypred)

        #June
        for i in range(336, 366):
            ypred = (df_demand_day[i] + df_demand_day[i+365])/2
            pre.append(ypred)
        pre
        data = pd.date_range('2019-01-01', periods=365, freq='D')
        demand = pd.Series(pre, data)

    # return the demand of every day
        return demand
