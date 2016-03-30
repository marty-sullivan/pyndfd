pyndfd
====

Python Routines for retrieving forecast data from NWS's NDFD.

Package available on PyPI:

    pip install pyndfd

Library Dependencies:

1. Python 2.6+
2. GRIB-API
3. PROJ.4

Python Dependencies:

1. numpy
2. pyproj
3. pygrib

Example:

    from pyndfd import ndfd
    
    analysis = ndfd.getForecastAnalysis('temp', lat, lon)
    weather = ndfd.getWeatherAnalysis(lat, lon)

See demo.py for more info

See http://www.nws.noaa.gov/ndfd/technical.htm for more info about NDFD variables and areas.
