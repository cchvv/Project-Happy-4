# Project-
## Happy-4

Happy-4 is a project to find the best way to combine solar and wind energy to get a stable clean energy resource. 
User can just input the position and year to download the corresponding data of radiation and wind speed automaticly.

Data will be put into the System Advisor Model (SAM) model to simulate the power a solar panel and a wind turbine can provide in a specific place.

Based on the simulation, this project can return a suitable number ratio of solar panels and wind turbines, and this combination can provide stable energy resource.

Also, figures of daily solar energy provided a solar panel, daily solar energy provided by a wind turbine and daily total energy are given.

### How to use

conda install ipython
conda install jupyter
conda install pandas
conda install scipy
pip install geopy

 
1. Ipython setup.py, it is in directory called `Happy-4`.
2. Input your position, year.(year:2007-2012, postion:in the United States).
3. Wait for the figues.
4. Close the windows of figues. The simulated number ratio of solar panels and wind turbines will be printed.

### Organization of the  project

The project has the following structure:

    Project-Happy-4/
      |- README.md
      |- design/
         |- Software_Design.ipynb
         |- Diagram.png
      |- Happy-4/
         |- __init__.py
         |- ssc.dylib
         |- output.py
         |- PySSC.py
         |- setup.py
         |- solar_input.py
         |- wind_input.py
         |- sscapi.py  
      |- tests/
         |- ...
      |- doc
      |- LICENSE


### Module code

We place the module code for solar energy in a file called `solar_input.py` in directory called
`Happy-4`. This structure is to download the data of radiation of the longitude, latitude and year input by user.
The System Advisor Model (SAM) will simulate the daily power provided by a solar panel.

The module code for wind energy is in a file called `wind_input.py` in directory called
`Happy-4`. This structure is to download the data of radiation of the longitude, latitude and year input by user.
The System Advisor Model (SAM) will simulate the daily power provided by a wind turbine.

The module code for output is in a file called `output.py` in directory called
`Happy-4`. This structure is to find a suitable number ratio of solar panels and wind turbines, 
and this combination can provide stable energy resource. Also, figures of daily solar energy, 
daily solar energy and daily total energy are given.

### Project Data

In this case, the project data is rather large, and recorded in csv
files. Due to all the data are downloaded and removed by the code automaticly,
We do not place any data here, and you need to wait more time according to your web condition.

### Testing

Testing file is in a file called `test_` in directory called `tests`. You need to put this file and 
in the same diretory

### Reference

[1] System Advisor Model Version 2016.3.14 (SAM 2016.3.14) Website. Simple Efficiency Module. National Renewable Energy Laboratory. Golden, CO. Accessed October 31, 2016. https://sam.nrel.gov/content/simple-efficiency-module.

[2] Blair, N.; Dobos, A.; Freeman, J.; Neises, T.; Wagner, M.; Ferguson, T.; Gilman, P.; Janzou, S. (2014). System Advisor Model, SAM 2014.1.14: General Description. NREL/TP-6A20-61019. National Renewable Energy Laboratory. Golden, CO. Accessed October 31, 2016. http://www.nrel.gov/docs/fy14osti/61019.pdf.

[3] System Advisor Model Version 2016.3.14 (SAM 2016.3.14) User Documentation. Weather File Formats. National Renewable Energy Laboratory. Golden, CO.


