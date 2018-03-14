from setuptools import setup, find_packages
import sys, os
import pandas as pd
from geopy.geocoders import Nominatim
from Happy_4 import average_daily_solarandwind
from Happy_4 import average_daily_electricity_demand
from Happy_4 import output2


PACKAGES = find_packages()

# Get version and release info, which is all stored in shablona/version.py
ver_file = os.path.join('version.py')
with open(ver_file) as f:
    exec(f.read())

opts = dict(name=NAME,
            maintainer=MAINTAINER,
            maintainer_email=MAINTAINER_EMAIL,
            description=DESCRIPTION,
            long_description=LONG_DESCRIPTION,
            url=URL,
            download_url=DOWNLOAD_URL,
            license=LICENSE,
            classifiers=CLASSIFIERS,
            author=AUTHOR,
            author_email=AUTHOR_EMAIL,
            platforms=PLATFORMS,
            version=VERSION,
            packages=PACKAGES,
            package_data=PACKAGE_DATA,
            install_requires=REQUIRES,
            requires=REQUIRES)


if __name__ == '__main__':
    def generate(locat, lat, lon, area_ed):
        daily_solar_average, generation_solar_average = average_daily_solarandwind.average_daily_solar(lat, lon)
        daily_wind_average, generation_wind_average = average_daily_solarandwind.average_daily_wind(lat, lon)
        daily_demand_average = average_daily_electricity_demand.electricity_demand(area_ed)
        output2.checkout(locat, 2019, daily_solar_average, daily_wind_average, daily_demand_average)
        return
    
    long_description = """

Happy-4
========

Happy-4 is a project to find the best way to combine solar and wind energy to 
get a stable clean energy resource. 
User can just input the position and year to download the corresponding data of 
radiation and wind speed automaticly.

Data will be put into the System Advisor Model (SAM) model to simulate the power
a solar panel and a wind turbine can provide in a specific place.

Based on the simulation, this project can return a suitable number ratio of solar 
panels and wind turbines, and this combination can provide stable energy resource.

Also, figures of daily solar energy provided a solar panel, daily solar 
energy provided by a wind turbine and daily total energy are given.


License
=======
``Happy-4`` is licensed under the terms of the MIT license. See the file
"LICENSE" for information on the history of this software, terms & conditions
for usage, and a DISCLAIMER OF ALL WARRANTIES.

All trademarks referenced herein are property of their respective holders.
"""
    print(long_description)
    
    print(pd.read_excel('Happy_4/id.xlsx')[['NAME','ABBREVIATION']])
    
    area_ed = str(input('Area of electriciy demand:'))
    #locat = str(input("Location(address):"))
    locat = [x for x in input("Locations (addresses):").split(',')]

    for i in range(len(locat)):
        geolocator = Nominatim()    
        location = geolocator.geocode(locat[i])
        lat = location.latitude
        lon = location.longitude
            
        generate(locat[i], lat, lon, area_ed)

    