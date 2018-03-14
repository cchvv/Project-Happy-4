# Project-
## Happy_4

Happy-4 is a project to find the best way to combine solar and wind energy to get a stable clean energy resource. 

User can use this code to download the corresponding data of radiation and wind speed automatically.

Data will be put into the System Advisor Model (SAM) model to simulate the power a solar panel and a wind turbine can provide in a specific place.

Based on the simulation, this project can return a suitable number ratio of solar panels and wind turbines, and this combination can provide stable energy resource.

Also, figures of daily solar energy provided a solar panel, daily solar energy provided by a wind turbine and daily total energy are given.

### How to use

    conda install ipython
    conda install jupyter
    conda install pandas
    conda install scipy
    pip install geopy
    
##### Calcualte the ratio of solar panels and wind turbines.
1. Ipython
2. import Happy_4.
3. %run setup.py
4. Input your position, year.(Year: 2007-2012   Position: the United States).

##### Calcualte the total number of solar panels and wind turbines needed to meet the electricity demand.
1. Ipython
2. import Happy_4.
3. %run setup2.py
4. Input your position, and Area of electriciy demand.

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
         |- average_daily_electricity_demand.py
         |- average_daily_solarandwind.py
         |- output.py
         |- output2.py
         |- electricity_demand.py
         |- id.xlsx
         |- PySSC.py
         |- solar_input.py
         |- wind_input.py
         |- sscapi.py
         |- test_output.py
         |- test_solar_input.py
         |- test_wind_input.py
         |- README.md
         |- Poster.pdf
         |- ssc.dylib
         |- ssc.so
         |- ssc.dll
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

The module code for output is in a file called `output.py` in directory called
`Happy_4`. This structure is to find a suitable number ratio of solar panels and wind turbines, 
and this combination can provide stable energy resource. Also, figures of daily solar energy, 
daily solar energy and daily total energy are given.

The module code for electricity consumption is in a file called `electricity_demand.py` in directory called `Happy_4`. This structure is to download the ID for all electric systems in US and get the electricity consumption of specific electric system based on user's input. 

### Project Data

In this case, the project data is rather large, and recorded in csv
files. Due to all the data are downloaded and removed by the code automaticly,
We do not place any data here, and you need to wait more time according to your web condition.

### Testing

Testing file `test_solar_input.py` for `solar_input.py`, `test_wind_input.py` for `wind_input.py` 
and `test_output.py` for `output.py`.

For testing, you need use nosetests in terminal.


### Reference

[1] System Advisor Model Version 2016.3.14 (SAM 2016.3.14) Website. Simple Efficiency Module. National Renewable Energy Laboratory. Golden, CO. Accessed October 31, 2016. https://sam.nrel.gov/content/simple-efficiency-module.

[2] Blair, N.; Dobos, A.; Freeman, J.; Neises, T.; Wagner, M.; Ferguson, T.; Gilman, P.; Janzou, S. (2014). System Advisor Model, SAM 2014.1.14: General Description. NREL/TP-6A20-61019. National Renewable Energy Laboratory. Golden, CO. Accessed October 31, 2016. http://www.nrel.gov/docs/fy14osti/61019.pdf.

[3] System Advisor Model Version 2016.3.14 (SAM 2016.3.14) User Documentation. Weather File Formats. National Renewable Energy Laboratory. Golden, CO.


