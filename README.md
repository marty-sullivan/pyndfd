ndfd
====

Python Routines for retrieving forecast data from NWS's NDFD.

Package available on PyPI:

    pip install pyndfd

Library Dependencies:

1. Python 2.6+
2. grib_api
3. PROJ4

Python Dependencies:

1. numpy
2. pygrib
3. pyproj
4. bitstring

Example:

    from pyndfd import ndfd
    
    analysis = ndfd.getForecastAnalysis('temp', lat, lon)
    weather = ndfd.getWeatherAnalysis(lat, lon)
