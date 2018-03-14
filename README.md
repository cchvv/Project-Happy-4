# Project-
## Happy_4

Happy-4 is a project to find the best way to combine solar and wind energy in order to achieve a stable clean energy resource.

Users input a location to download the corresponding data of insolation and wind speed automatically.  Data are put into the simulation models of  System Advisor Model (SAM) to estimate the energy generation of a solar panel and a wind turbine.  Since the results of Dickey Fuller Test show that both the simluated data of solar and wind energy are stationary, the simulated data of years are then processed to acquire averaged daily data for 365 days in a year.  Based on the processed results, this project returns a optimal ratio of solar panels and wind turbines and upon the ratio a stable combinational energy generation resource can be obtained.  The figures of of the generation of a single solar panel and a wind turbine and the combiation of the ratio are provided.

Also, anther input from users is the abbreviation of different data bases for electricity demands.  The data electricity demand of are also stationary according to Dickey Fuller Test so a similar process is done to averaged daily data for 365 days in a year.  Along with the information obtained from the energy generation, the numbers of solar panels and wind turbines required to meet the eletiricty demand are then calculated.

### How to use

    conda install ipython
    conda install jupyter
    conda install pandas
    conda install scipy
    pip install geopy
 
1. Ipython
2. import Happy_4.
3. %run setup2.py
4. Input a abbreviation (ex:SCL) from the list and then input a location (ex: Seattle,Spokane)

### Organization of the  project

The project has the following structure:

    Project-Happy-4/
      |- README.md
      |- ssc.dylib
      |- ssc.so
      |- ssc.dll
      |- requirements.txt
      |- setup.py
      |- setup2.py
      |- version.py
      |- design/
         |- Software_Design.ipynb
         |- Diagram.png
      |- Happy_4/
         |- __init__.py
         |- output.py
         |- output2.py
         |- electricity_demand.py
         |- average_daily_electricity_demand.py
         |- id.xlsx
         |- PySSC.py
         |- solar_input.py
         |- wind_input.py
         |- average_daily_solarandwind.py
         |- sscapi.py  
         |- test_solar_input.py
         |- test_wind_input.py
         |- test_average_daily_solarandwind.py
         |- test_output.py
         |- test_output2.py
         |- test_average_daily_electricity_demand.py
         |- README.md
         |- Poster.pdf
      |- doc
         |- Handbook for SAM
      |- LICENSE


### Module code

We place the module code for solar energy in a file called `solar_input.py` in directory called
`Happy_4`. This structure is to download the data of radiation of the longitude, latitude and year input by user.
The System Advisor Model (SAM) will simulate the daily power provided by a solar panel.

The module code for wind energy is in a file called `wind_input.py` in directory called
`Happy_4`. This structure is to download the data of radiation of the longitude, latitude and year input by user.
The System Advisor Model (SAM) will simulate the daily power provided by a wind turbine.

The module code for processing solar and wind energy is in a file called `average_daily_solarandwind.py` in directory called
`Happy_4`. This structure is to collect the simulation data of years for a location input by users and acquire averaged daily data for 365 days in a year.

The module code for output is in a file called `output.py` in directory called
`Happy_4`. This structure is to find a suitable number ratio of solar panels and wind turbines, 
and this combination can provide stable energy resource. Also, figures of daily solar energy, 
daily solar energy and daily total energy are given.

The module code for electricity consumption is in a file called `electricity_demand.py` in directory called `Happy_4`. This structure is to download the ID for all electric systems in US and get the electricity consumption of specific electric system based on user's input.

The module code for processing the electricity demand is in a file called `average_daily_electricity_demand.py` in directory called `Happy_4`. This structure is to collect the electricity demand data of years provided by the government unit  input by users and acquire averaged daily data for 365 days in a year.

### Project Data

In this case, the project data is rather large, and recorded in csv
files. Due to all the data are downloaded and removed by the code automaticly,
We do not place any data here, and you need to wait more time according to your web condition.

### Testing

Testing file `test_solar_input.py` for `solar_input.py`, `test_wind_input.py` for `wind_input.py` , `test_average_daily_solarandwind.py` for `average_daily_solarandwind.py` , `test_average_daily_solarandwind.py` for `average_daily_solarandwind.py` , `test_potput.py` for `potput.py`
and `test_potput2.py` for `output2.py`.

For testing, you need use nosetests in terminal.


### Reference

[1] System Advisor Model Version 2016.3.14 (SAM 2016.3.14) Website. Simple Efficiency Module. National Renewable Energy Laboratory. Golden, CO. Accessed October 31, 2016. https://sam.nrel.gov/content/simple-efficiency-module.

[2] Blair, N.; Dobos, A.; Freeman, J.; Neises, T.; Wagner, M.; Ferguson, T.; Gilman, P.; Janzou, S. (2014). System Advisor Model, SAM 2014.1.14: General Description. NREL/TP-6A20-61019. National Renewable Energy Laboratory. Golden, CO. Accessed October 31, 2016. http://www.nrel.gov/docs/fy14osti/61019.pdf.

[3] System Advisor Model Version 2016.3.14 (SAM 2016.3.14) User Documentation. Weather File Formats. National Renewable Energy Laboratory. Golden, CO.


