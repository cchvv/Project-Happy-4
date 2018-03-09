import os
from setuptools import setup, find_packages
import sys, os
import sscapi
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd 
import math
import solar_input, wind_input
from output import output_loop, checkout
from geopy.geocoders import Nominatim
import urllib

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
    def generate(lat, lon, year):
        Daily_solar, generation_solar = solar_input.solar(lat, lon, year)
        Daily_wind, generation_wind = wind_input.wind(lat, lon, year)
        checkout(lat, lon, year, Daily_solar, Daily_wind)
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
    year = int(input("Enter the year，from 2007 to 2012: "))
    locat = str(input("Location(address):"))
    
    geolocator = Nominatim()    
    location = geolocator.geocode(locat)
    lat = location.latitude
    lon = location.longitude
    
    if (2007 <= year and year <= 2012):        
        generate(lat, lon, year)
    else:
         print('the year is out of range')