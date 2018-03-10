from Happy_4 import sscapi
import numpy as np
import pandas as pd 
import requests

def solar(lat, lon, y):
    api_key = 'Mow538glfN0fjR9Sk9RFqnnhuUDm5lxZBcTTqeKK'
    # Set the attributes to extract (e.g., dhi, ghi, etc.), separated by commas.
    attributes = 'ghi,dhi,dni,wind_speed_10m_nwp,surface_air_temperature_nwp,solar_zenith_angle'
    # Choose year of data
    year = str(y)
    # Set leap year to true or false. True will return leap day data if present, false will not.
    leap_year = 'false'
    # Set time interval in minutes, i.e., '30' is half hour intervals. Valid intervals are 30 & 60.
    interval = '30'
    # Specify Coordinated Universal Time (UTC), 'true' will use UTC, 'false' will use the local time zone of the data.
    # NOTE: In order to use the NSRDB data in SAM, you must specify UTC as 'false'. SAM requires the data to be in the
    # local time zone.
    utc = 'false'
    your_name = 'Zihao+Tao'
    reason_for_use = 'beta+testing'
    your_affiliation = 'university+of+washington'
    your_email = 'taozihao@uw.edu'
    mailing_list = 'true'
    # Declare url string
    url = 'http://developer.nrel.gov/api/solar/nsrdb_0512_download.csv?wkt=POINT({lon}%20{lat})&names={year}&leap_day={leap}&interval={interval}&utc={utc}&full_name={name}&email={email}&affiliation={affiliation}&mailing_list={mailing_list}&reason={reason}&api_key={api}&attributes={attr}'.format(year=year, lat=lat, lon=lon, leap=leap_year, interval=interval, utc=utc, name=your_name, email=your_email, mailing_list=mailing_list, affiliation=your_affiliation, reason=reason_for_use, api=api_key, attr=attributes)
    import requests
    req = requests.get(url)
    assert req.status_code == 200, "The download failed, can not find this place's database."# if the download failed, this line will generate an error
    # Return just the first 2 lines to get metadata:
    info = pd.read_csv(url, nrows=1)
    # See metadata for specified properties, e.g., timezone and elevation
    timezone, elevation = info['Local Time Zone'], info['Elevation']
    # Return all but first 2 lines of csv to get data:
    df = pd.read_csv('http://developer.nrel.gov/api/solar/nsrdb_0512_download.csv?wkt=POINT({lon}%20{lat})&names={year}&leap_day={leap}&interval={interval}&utc={utc}&full_name={name}&email={email}&affiliation={affiliation}&mailing_list={mailing_list}&reason={reason}&api_key={api}&attributes={attr}'.format(year=year, lat=lat, lon=lon, leap=leap_year, interval=interval, utc=utc, name=your_name, email=your_email, mailing_list=mailing_list, affiliation=your_affiliation, reason=reason_for_use, api=api_key, attr=attributes), skiprows=2)
    # Set the time index in the pandas dataframe:
    df = df.set_index(pd.date_range('1/1/{yr}'.format(yr=year), freq=interval+'Min', periods=525600/int(interval)))
    ssc = sscapi.PySSC()
    
    # Resource inputs for SAM model:
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
    
    # Create SAM compliant object 
    dat = ssc.data_create()
    ssc.data_set_table(dat, b'solar_resource_data', wfd)
    ssc.data_free(wfd)
    
    # Specify the system Configuration
    # Set system capacity in MW
    system_capacity = 4
    ssc.data_set_number(dat, b'system_capacity', system_capacity)
    # Set DC/AC ratio (or power ratio). See https://sam.nrel.gov/sites/default/files/content/virtual_conf_july_2013/07-sam-virtual-conference-2013-woodcock.pdf
    ssc.data_set_number(dat, b'dc_ac_ratio', 1.1)
    # Set tilt of system in degrees
    ssc.data_set_number(dat, b'tilt', 25)
    # Set azimuth angle (in degrees) from north (0 degrees)
    ssc.data_set_number(dat, b'azimuth', 180)
    # Set the inverter efficency
    ssc.data_set_number(dat, b'inv_eff', 96)
    # Set the system losses, in percent
    ssc.data_set_number(dat, b'losses', 14.0757)
    # Specify fixed tilt system (0=Fixed, 1=Fixed Roof, 2=1 Axis Tracker, 3=Backtracted, 4=2 Axis Tracker)
    ssc.data_set_number(dat, b'array_type', 0)
    # Set ground coverage ratio
    ssc.data_set_number(dat, b'gcr', 0.4)
    # Set constant loss adjustment
    ssc.data_set_number(dat, b'adjust:constant', 0)
    
    # execute and put generation results back into dataframe
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
    # free the memory
    ssc.data_free(dat)
    ssc.module_free(mod)
    generation_solar = df['generation'].sum()/system_capacity
    
    return Daily_solar,generation_solar