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



def solar(lat, lon, y):
    api_key = 'Mow538glfN0fjR9Sk9RFqnnhuUDm5lxZBcTTqeKK'
    attributes = 'ghi,dhi,dni,wind_speed_10m_nwp,surface_air_temperature_nwp,solar_zenith_angle'
    year = str(y)
    leap_year = 'false'
    interval = '30'
    utc = 'false'
    your_name = 'Zihao+Tao'
    reason_for_use = 'beta+testing'
    your_affiliation = 'university+of+washington'
    your_email = 'taozihao@uw.edu'
    mailing_list = 'true'
    url = 'http://developer.nrel.gov/api/solar/nsrdb_0512_download.csv?wkt=POINT({lon}%20{lat})&names={year}&leap_day={leap}&interval={interval}&utc={utc}&full_name={name}&email={email}&affiliation={affiliation}&mailing_list={mailing_list}&reason={reason}&api_key={api}&attributes={attr}'.format(year=year, lat=lat, lon=lon, leap=leap_year, interval=interval, utc=utc, name=your_name, email=your_email, mailing_list=mailing_list, affiliation=your_affiliation, reason=reason_for_use, api=api_key, attr=attributes)
    info = pd.read_csv(url, nrows=1)
    timezone, elevation = info['Local Time Zone'], info['Elevation']
    df = pd.read_csv('http://developer.nrel.gov/api/solar/nsrdb_0512_download.csv?wkt=POINT({lon}%20{lat})&names={year}&leap_day={leap}&interval={interval}&utc={utc}&full_name={name}&email={email}&affiliation={affiliation}&mailing_list={mailing_list}&reason={reason}&api_key={api}&attributes={attr}'.format(year=year, lat=lat, lon=lon, leap=leap_year, interval=interval, utc=utc, name=your_name, email=your_email, mailing_list=mailing_list, affiliation=your_affiliation, reason=reason_for_use, api=api_key, attr=attributes), skiprows=2)
    df = df.set_index(pd.date_range('1/1/{yr}'.format(yr=year), freq=interval+'Min', periods=525600/int(interval)))
    ssc = sscapi.PySSC()
    wfd = ssc.data_create()
    ssc.data_set_number(wfd, b'lat', lat)
    ssc.data_set_number(wfd, b'lon', lon)
    ssc.data_set_number(wfd, b'tz', timezone)
    ssc.data_set_number(wfd, b'elev', elevation)
    ssc.data_set_array(wfd, b'year', df.index.year)
    ssc.data_set_array(wfd, b'month', df.index.month)
    ssc.data_set_array(wfd, b'day', df.index.day)
    ssc.data_set_array(wfd, b'hour', df.index.hour)
    ssc.data_set_array(wfd, b'minute', df.index.minute)
    ssc.data_set_array(wfd, b'dn', df['DNI'])
    ssc.data_set_array(wfd, b'df', df['DHI'])
    ssc.data_set_array(wfd, b'wspd', df['Wind Speed'])
    ssc.data_set_array(wfd, b'tdry', df['Temperature'])
    dat = ssc.data_create()
    ssc.data_set_table(dat, b'solar_resource_data', wfd)
    ssc.data_free(wfd)
    system_capacity = 4
    ssc.data_set_number(dat, b'system_capacity', system_capacity)
    ssc.data_set_number(dat, b'dc_ac_ratio', 1.1)
    ssc.data_set_number(dat, b'tilt', 25)
    ssc.data_set_number(dat, b'azimuth', 180)
    ssc.data_set_number(dat, b'inv_eff', 96)
    ssc.data_set_number(dat, b'losses', 14.0757)
    ssc.data_set_number(dat, b'array_type', 0)
    ssc.data_set_number(dat, b'gcr', 0.4)
    ssc.data_set_number(dat, b'adjust:constant', 0)
    
    mod = ssc.module_create(b'pvwattsv5')
    ssc.module_exec(mod, dat)
    df['generation'] = np.array(ssc.data_get_array(dat, b'gen'))
    Daily = []
    for i in range(int(len(df)/48)):
        a = 0
        for j in range(48):
            a = a + df.iloc[int(i*48+j)]['generation']/system_capacity
        Daily.append(a)
    Daily = pd.DataFrame(Daily, columns=['generation'])
    Daily_solar = Daily.set_index(pd.date_range('1/1/{yr}'.format(yr=year), freq='1'+'D', periods=len(df)/48))
    ssc.data_free(dat)
    ssc.module_free(mod)
    generation_solar = df['generation'].sum()/system_capacity
    
    return Daily_solar,generation_solar