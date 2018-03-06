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


def wind(lat, lon, yr):
    year = str(yr)
    lat = str(lat)
    lon = str(lon)
    key = 'CNN87trTlIjPrPURSZM9VEUDnWzKulgUFtUVjUmr'
    url = 'http://developer.nrel.gov/api/wind/srw_aggregate_extract?api_key={APIKEY}&year={YEAR}&lat={LAT}&lon={LON}'.format(LAT=lat, LON=lon, YEAR=year, APIKEY=key);
    import requests
    req = requests.get(url)
    assert req.status_code == 200 # if the download failed, this line will generate an error
    with open("test.csv","wb") as f:
        f.write(req.content)
    interval = '30'
    df =pd.read_csv(url)
    df = df[:][4:]
    df = df.set_index(pd.date_range('1/1/{yr}'.format(yr=year), freq=interval+'Min', periods=len(df)))
    from PySSC import PySSC
    system_capacity = 48000
    ssc = PySSC()
    ssc.module_exec_set_print(0)
    dat = ssc.data_create()
    local = os.getcwd()+'/test.csv'
    ssc.data_set_string( dat, b'wind_resource_filename', bytes(local, 'utf-8'));
    ssc.data_set_number( dat, b'wind_resource_shear', 0.14000000059604645 )
    ssc.data_set_number( dat, b'wind_resource_turbulence_coeff', 0.10000000149011612 )
    ssc.data_set_number( dat, b'system_capacity', 48000 )
    ssc.data_set_number( dat, b'wind_resource_model_choice', 0 )
    ssc.data_set_number( dat, b'weibull_reference_height', 50 )
    ssc.data_set_number( dat, b'weibull_k_factor', 2 )
    ssc.data_set_number( dat, b'weibull_wind_speed', 7.25 )
    ssc.data_set_number( dat, b'wind_turbine_rotor_diameter', 77 )
    wind_turbine_powercurve_windspeeds =[ 0, 0.25, 0.5, 0.75, 1, 1.25, 1.5, 1.75, 2, 2.25, 2.5, 2.75, 3, 3.25, 3.5, 3.75, 4, 4.25, 4.5, 4.75, 5, 5.25, 5.5, 5.75, 6, 6.25, 6.5, 6.75, 7, 7.25, 7.5, 7.75, 8, 8.25, 8.5, 8.75, 9, 9.25, 9.5, 9.75, 10, 10.25, 10.5, 10.75, 11, 11.25, 11.5, 11.75, 12, 12.25, 12.5, 12.75, 13, 13.25, 13.5, 13.75, 14, 14.25, 14.5, 14.75, 15, 15.25, 15.5, 15.75, 16, 16.25, 16.5, 16.75, 17, 17.25, 17.5, 17.75, 18, 18.25, 18.5, 18.75, 19, 19.25, 19.5, 19.75, 20, 20.25, 20.5, 20.75, 21, 21.25, 21.5, 21.75, 22, 22.25, 22.5, 22.75, 23, 23.25, 23.5, 23.75, 24, 24.25, 24.5, 24.75, 25, 25.25, 25.5, 25.75, 26, 26.25, 26.5, 26.75, 27, 27.25, 27.5, 27.75, 28, 28.25, 28.5, 28.75, 29, 29.25, 29.5, 29.75, 30, 30.25, 30.5, 30.75, 31, 31.25, 31.5, 31.75, 32, 32.25, 32.5, 32.75, 33, 33.25, 33.5, 33.75, 34, 34.25, 34.5, 34.75, 35, 35.25, 35.5, 35.75, 36, 36.25, 36.5, 36.75, 37, 37.25, 37.5, 37.75, 38, 38.25, 38.5, 38.75, 39, 39.25, 39.5, 39.75, 40 ];
    ssc.data_set_array( dat, b'wind_turbine_powercurve_windspeeds',  wind_turbine_powercurve_windspeeds);
    wind_turbine_powercurve_powerout =[ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 21.319999694824219, 33.509998321533203, 45.689998626708984, 65.209999084472656, 79.830001831054688, 104.25, 128.66000366210938, 157.97000122070312, 187.27000427246094, 216.58000183105469, 250.77999877929688, 292.32000732421875, 333.85000610351562, 375.39999389648438, 426.72000122070312, 475.60000610351562, 534.27001953125, 597.80999755859375, 656.489990234375, 724.94000244140625, 798.28997802734375, 871.6300048828125, 940.08001708984375, 1010, 1060, 1130, 1190, 1240, 1290, 1330, 1370, 1390, 1410, 1430, 1440, 1460, 1470, 1475, 1480, 1485, 1490, 1495, 1500, 1500, 1500, 1500, 1500, 1500, 1500, 1500, 1500, 1500, 1500, 1500, 1500, 1500, 1500, 1500, 1500, 1500, 1500, 1500, 1500, 1500, 1500, 1500, 1500, 1500, 1500, 1500, 1500, 1500, 1500, 1500, 1500, 1500, 1500, 1500, 1500, 1500, 1500, 1500, 1500, 1500, 1500, 1500, 1500, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ];
    ssc.data_set_array( dat, b'wind_turbine_powercurve_powerout',  wind_turbine_powercurve_powerout);
    ssc.data_set_number( dat, b'wind_turbine_hub_ht', 80 )
    ssc.data_set_number( dat, b'wind_turbine_max_cp', 0.44999998807907104 )
    wind_farm_xCoordinates =[ 0, 616, 1232, 1848, 2464, 3080, 3696, 4312, 308, 924, 1540, 2156, 2772, 3388, 4004, 4620, 0, 616, 1232, 1848, 2464, 3080, 3696, 4312, 308, 924, 1540, 2156, 2772, 3388, 4004, 4620 ];
    ssc.data_set_array( dat, b'wind_farm_xCoordinates',  wind_farm_xCoordinates);
    wind_farm_yCoordinates =[ 0, 0, 0, 0, 0, 0, 0, 0, 616, 616, 616, 616, 616, 616, 616, 616, 1232, 1232, 1232, 1232, 1232, 1232, 1232, 1232, 1848, 1848, 1848, 1848, 1848, 1848, 1848, 1848 ];
    ssc.data_set_array( dat, b'wind_farm_yCoordinates',  wind_farm_yCoordinates);
    ssc.data_set_number( dat, b'wind_farm_losses_percent', 0 )
    ssc.data_set_number( dat, b'wind_farm_wake_model', 0 )
    ssc.data_set_number( dat, b'adjust:constant', 0 )
    mod = ssc.module_create(b'windpower')	
 
    ssc.module_exec_set_print( 0 );     
    if ssc.module_exec(mod, dat) == 0:
        print ('windpower simulation error')
        idx = 1
        msg = ssc.module_log(mod, 0)
        while (msg != None):
            print ('	: ' + msg.decode("utf - 8"))
            msg = ssc.module_log(mod, idx)
            idx = idx + 1
        SystemExit( "Simulation Error" );    
    
    df = np.array(ssc.data_get_array(dat, b'gen')); 
    df = pd.DataFrame(df,columns=['generation'])
    df = df.set_index(pd.date_range('1/1/{yr}'.format(yr=year), freq=interval+'Min', periods=525600/60))
    Daily=[]
    for i in range(int(len(df)/24)):
        a = 0
        for j in range(24):
            a = a + df.iloc[int(i*24+j)].values[0]/system_capacity
        Daily.append(a)
    Daily = pd.DataFrame(Daily, columns=['generation'])
    Daily_wind = Daily.set_index(pd.date_range('1/1/{yr}'.format(yr=year), freq='1'+'D', periods=365))
    generation_wind = Daily_wind['generation'].sum()
    ssc.data_free(dat)
    ssc.module_free(mod)
    os.remove('test.csv')
       
    return Daily_wind, generation_wind