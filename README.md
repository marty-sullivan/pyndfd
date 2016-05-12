pyndfd
====

PyNDFD is an open source Python module that, in one line of code, retrieves up-to-date forecast data from the US National Weather Service - National Digital Forecasting Database. Data can be retrieved for any coordinate within the United States in a fraction of a second. Important decisions can be made easier with rain, wind, temperature and a multitude of other forecast variable monitoring. Weather advisories and weather descriptions are also constructed by PyNDFD. 

The difficulty of retrieving and processing all of this data is reduced to a simple function call. This leaves the developer with a simple way to work with the data they need, without having to deal with the hassle of manually downloading and processing the complex data formats used by NOAA. There is also no need for any backend servers, just install PyNDFD and go!

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
