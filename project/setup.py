import sys, os
import sscapi
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd 
import math
import solar_input,wind_input
from output import output_loop, checkout

def generate(lat, lon, year):
    Daily_solar,generation_solar = solar_input.solar(lat, lon, year)
    Daily_wind,generation_wind = wind_input.wind(lat, lon, year)
    checkout(lat, lon, year, Daily_solar, Daily_wind)
    return

year = int(input("Enter the year，from 2007 to 2012: "))
lat = float(input("Enter the latitude: "))
lon = float(input("Enter the longitude: "))
generate(lat, lon, year)
