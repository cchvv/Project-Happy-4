from __future__ import absolute_import, division, print_function
from os.path import join as pjoin

# Format expected by setup.py and doc/source/conf.py: string of form "X.Y.Z"
_version_major = 0
_version_minor = 1
_version_micro = ''  # use '' for first of series, number for 1 and above
_version_extra = 'dev'
# _version_extra = ''  # Uncomment this for full releases

# Construct full version string from these.
_ver = [_version_major, _version_minor]
if _version_micro:
    _ver.append(_version_micro)
if _version_extra:
    _ver.append(_version_extra)

__version__ = '.'.join(map(str, _ver))

CLASSIFIERS = ["Development Status :: 3 - Alpha",
               "Environment :: Console",
               "Intended Audience :: Science/Research",
               "License :: OSI Approved :: MIT License",
               "Operating System :: OS Independent",
               "Programming Language :: Python",
               "Topic :: Scientific/Engineering"]

# Description should be a one-liner:
description = "Happy-4: a project to find the best way to combine solar and wind energy to get a stable clean energy resource."
# Long description will go up on the pypi page
long_description = """

Happy-4
========

Happy-4 is a project to find the best way to combine solar and wind energy to get a stable clean energy resource. 
User can just input the position and year to download the corresponding data of radiation and wind speed automaticly.

Data will be put into the System Advisor Model (SAM) model to simulate the power a solar panel and a wind turbine can provide in a specific place.

Based on the simulation, this project can return a suitable number ratio of solar panels and wind turbines, and this combination can provide stable energy resource.

Also, figures of daily solar energy provided a solar panel, daily solar energy provided by a wind turbine and daily total energy are given.


License
=======
``Happy-4`` is licensed under the terms of the MIT license. See the file
"LICENSE" for information on the history of this software, terms & conditions
for usage, and a DISCLAIMER OF ALL WARRANTIES.

All trademarks referenced herein are property of their respective holders.

Copyright (c) 2015--, Ariel Rokem, The University of Washington
eScience Institute.
"""

NAME = "Happy-4"
MAINTAINER = "Zihao Tao"
MAINTAINER_EMAIL = "taozihao@uw.edu"
DESCRIPTION = description
LONG_DESCRIPTION = long_description
URL = "http://github.com/uwescience/shablona"
DOWNLOAD_URL = ""
LICENSE = "MIT"
AUTHOR = "Zihao Tao"
AUTHOR_EMAIL = "taozihao@uw.edu"
PLATFORMS = "OS Independent"
MAJOR = _version_major
MINOR = _version_minor
MICRO = _version_micro
VERSION = __version__
PACKAGE_DATA = {'Zihao Tao': [pjoin('data', '*')]}
REQUIRES = ["numpy"]
