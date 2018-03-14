
from Happy_4 import average_daily_electricity_demand
import pandas as pd
import requests
import numpy as np
import math
import requests


def test_electricity_demand():
    
    # check every url in the dataframe is good 
    df = pd.read_excel('id.xlsx')
    df['URL'] = '0'
    for i in range(len(df['NAME'])):
        df['URL'][i] = 'http://api.eia.gov/series/?series_id=' + df['ID'][i] +'&api_key=dc18856f7f589c8cb34de219b44f58ac&out=json'
        req = requests.get(df['URL'][i])
        if req.status_code == 200:
            pass
        else:
            raise Exception('The url of ' + df['ABBREVIATION'][i] + ' does not work.')
    
    # check the input_name
    try:
        average_daily_electricity_demand.electricity_demand('AAA')
    except Exception:
        pass
    
    return