
from Happy_4 import solar_input
from Happy_4 import wind_input
from Happy_4 import average_daily_solarandwind
import pandas as pd

def test_average_daily_solar():
    # check if the data of different year are appended one after one
    daily_solar_total = pd.DataFrame()
    for y in [2007, 2009, 2010, 2011]:
        daily_solar, generation_solar = solar_input.solar(30, -100, y)
        daily_solar_total = daily_solar_total.append(daily_solar)
    assert (len(daily_solar_total) % 365) == 0, 'The data of years are not collected completely.'
    
    # check if a dataframe is acquired 
    daily_solar_average, generation_solar_average = average_daily_solarandwind.average_daily_solar(30,-100)
    if isinstance(daily_solar_average, pd.DataFrame):
        pass
    else:
        raise Exception('The output data is not a dataframe')
    return


def test_average_daily_wind():
    # check if the data of different year are appended one after one
    daily_wind_total = pd.DataFrame()
    for y in [2007, 2009, 2010, 2011]:
        daily_wind, generation_wind = wind_input.wind(30, -100, y)
        daily_wind_total = daily_wind_total.append(daily_wind)
    assert (len(daily_wind_total) % 365) == 0, 'The data of years are not collected completely.'
    
    
    # check if a dataframe is acquired
    daily_wind_average, generation_wind_average = average_daily_solarandwind.average_daily_wind(30,-100)
    if isinstance(daily_wind_average, pd.DataFrame):
        pass
    else:
        raise Exception('The output data is not a dataframe')
    return