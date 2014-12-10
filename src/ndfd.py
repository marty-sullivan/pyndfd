'''

	NDFD Forecast Retrieval Routines

	Author: 	Marty J. Sullivan
	Revision: 	0.1
	Date:		December 3, 2014
	Purpose:	Routines that will cache NDFD forecast variables locally
			to allow for easy and fast forecast analysis by lat/lon

'''

###########
#         #
# IMPORTS #
#         #
###########

from bitstring import BitArray
from datetime import datetime, timedelta
from math import isnan, sqrt
from ncepgrib2 import Grib2Decode as ncepgrib
from numpy.ma.core import MaskedConstant as NAN
from os import makedirs, path
from pyproj import Geod, Proj
from sys import stderr
from urllib import urlretrieve
import json
import ndfd_defs
import pygrib

#############
#           #
# CONSTANTS #
#           #
#############

DEFS = ndfd_defs.ndfdDefs()
G = Geod(ellps='clrk66')

CACHE_SERVER_BUFFER_MIN = 10

NDFD_LOCAL_SERVER = None
NDFD_REMOTE_SERVER = 'http://weather.noaa.gov/pub/SL.us008001/ST.opnl/DF.gr2/'
NDFD_DIR = 'DC.ndfd/AR.{0}/VP.{1}/'
NDFD_STATIC = 'static/DC.ndfd/AR.{0}/'
NDFD_VAR = 'ds.{0}.bin'
NDFD_TMP = '/tmp/ndfd/'

########################
#                      #
# FUNCTION DEFINITIONS #
#                      #
########################

'''

  Function:	setLocalCacheServer
  Purpose:	Set a server to use instead of weather.noaa.gov
  Params:
	uri:	String denoting the server URI to use

'''
def setLocalCacheServer(uri):
    global NDFD_LOCAL_SERVER 
    NDFD_LOCAL_SERVER = uri

'''

  Function:	stdDev
  Purpose:	Calculate the standard deviation of a list of float values
  Params:
	vals:	List of float values to use in calculation

'''
def stdDev(vals):
    mean = sum(vals) / len(vals)
    squared = []
    for val in vals:
        squared.append(pow(val - mean, 2))
    variance = sum(squared) / len(squared)
    return sqrt(variance)

'''

  Function:	median
  Purpose:	Calculate the median of a list of int/float values
  Params:
	vals:	List of int/float values to use in calculation

'''
def median(vals):
    sortedLst = sorted(vals)
    lstLen = len(vals)
    index = (lstLen - 1) // 2
    if (lstLen % 2):
        return sortedLst[index]
    else:
        return (sortedLst[index] + sortedLst[index + 1]) / 2.0

'''

  Function: 	getLatestForecastTime
  Purpose:  	For caching purposes, compare this time to cached time to see if
		the cached variable needs to be updated

'''
def getLatestForecastTime():
    latestTime = datetime.utcnow()
    if latestTime.minute <= CACHE_SERVER_BUFFER_MIN:
        latestTime = (datetime.utcnow() - timedelta(hours=1))
    return latestTime.replace(minute=0, second=0, microsecond=0)

'''

  Function:	getVariable
  Purpose:	Cache the requested variable if not already cached and return
		the paths of the cached files
  Params:
	var:	The NDFD variable to retrieve
	area:	The NDFD grid area to retrieve

'''
def getVariable(var, area):
    gribs = []
    dirTime = NDFD_TMP + getLatestForecastTime().strftime('%Y-%m-%d-%H') + '/'
    if not path.isdir(dirTime):
        makedirs(dirTime)
    if area in DEFS['vars']:
        for vp in DEFS['vars'][area]:
            if var in DEFS['vars'][area][vp]:
                varDir = NDFD_DIR.format(area, vp)
                varName = varDir + NDFD_VAR.format(var)
                localDir = dirTime + varDir
                localVar = dirTime + varName
                if not path.isdir(localDir):
                    makedirs(localDir)
                if not path.isfile(localVar):
                    if NDFD_LOCAL_SERVER != None:
                        remoteVar = NDFD_LOCAL_SERVER + varName
                        urlretrieve(remoteVar, localVar)
                    else:
                        remoteVar = NDFD_REMOTE_SERVER + varName
                        urlretrieve(remoteVar, localVar)
                if not path.isfile(localVar):
                    raise RuntimeError('Cannot retrieve NDFD variables at this time. Try again in a moment.')
                gribs.append(localVar)
    else:
        raise ValueError('Invalid Area: ' + str(area))

    return gribs

'''

  Function:	getElevationVariable
  Purpose:	Cache the static elevation variable if not already cached and return
		the path of the cached file
  Params:
	area:	The NDFD grid area to retrieve elevation for
  
  Notes:
	- Cannot be retrieved from weather.noaa.gov, must use a local cache server
	  using the format in const NDFD_STATIC
	- Puerto Rico terrian info not currently available. 
	- Terrain data for NDFD will be updated sometime in 2015

'''
def getElevationVariable(area):
    if area == 'puertori':
        raise ValueError('Elevation currently not available for Puerto Rico. Set elev=False')
    if NDFD_LOCAL_SERVER == None:
        raise RuntimeError('Local cache server must provide elevation data. Specify cache server with ndfd.setLocalCacheServer(uri)')
    if not path.isdir(NDFD_TMP):
        makedirs(NDFD_TMP)
    remoteVar = NDFD_LOCAL_SERVER + NDFD_STATIC.format(area) + NDFD_VAR.format('elev')
    localDir = NDFD_TMP + NDFD_STATIC.format(area)
    localVar = localDir + NDFD_VAR.format('elev')
    if not path.isdir(localDir):
        makedirs(localDir)
    if not path.isfile(localVar):
        urlretrieve(remoteVar, localVar)
    if not path.isfile(localVar):
        raise RuntimeError('Cannot retrieve NDFD variables at this time. Try again in a moment.')
    return localVar

'''

  Function:	getSmallestGrid
  Purpose:	Use the provided lat, lon coordinates to find the smallest
		NDFD area that contains those coordinates. Return the name of the area.
  Params:
	lat:	Latitude 
	lon:	Longitude

'''
def getSmallestGrid(lat, lon):
    smallest = 'neast'
    minDist = G.inv(lon, lat, DEFS['grids'][smallest]['lonC'], DEFS['grids'][smallest]['latC'])

    for area in DEFS['grids'].keys():
        if area == 'conus' or area == 'nhemi' or area == 'npacocn':
            continue
        curArea = DEFS['grids'][area]
        smallArea = DEFS['grids'][smallest]
        dist = G.inv(lon, lat, curArea['lonC'], curArea['latC'])[-1]
        if dist < minDist:
            minDist = dist
            smallest = area

    return smallest

'''

  Function:	getNearestGridPoint
  Purpose:	Find the nearest grid point to the provided coordinates in the supplied
		grib message. Return the indexes to the numpy array as well as the
		lat/lon and grid coordinates of the grid point.
  Params:
	grb:		The grib message to search
	lat:		Latitude
	lon:		Longitude
	projparams:	Optional: Use to supply different Proj4 parameters than the
				  supplied grib message uses.

'''
def getNearestGridPoint(grb, lat, lon, projparams=None):
    if projparams == None:
        p = Proj(grb.projparams)
    else:
        p = Proj(projparams)
    offsetX, offsetY = p(grb['longitudeOfFirstGridPointInDegrees'], grb['latitudeOfFirstGridPointInDegrees'])
    gridX, gridY = p(lon, lat)
    try:
        x = int(round((gridX - offsetX) / grb['DxInMetres']))
        y = int(round((gridY - offsetY) / grb['DyInMetres']))
        gLon, gLat = p(x * grb['DxInMetres'] + offsetX, y * grb['DyInMetres'] + offsetY, inverse=True)
    except:
        x = int(round((gridX - offsetX) / grb['DiInMetres']))
        y = int(round((gridY - offsetY) / grb['DjInMetres']))
        gLon, gLat = p(x * grb['DiInMetres'] + offsetX, y * grb['DjInMetres'] + offsetY, inverse=True)
    return x, y, gridX, gridY, gLat, gLon
    
'''

  Function:	validateArguments
  Purpose:	Validate the arguments passed into an analysis function to make sure
		they will work with each other.
  Params:
	var:		The NDFD variable being requested
	area:		The NDFD grid area being requested
	timeStep:	The time step to be used in the returned analysis
	minTime:	The minimum forecast time to analyze
	maxTime:	The maximum forecast time to analyze
  Notes:
	- maxTime is not currently being evaluated

'''
def validateArguments(var, area, timeStep, minTime, maxTime):
    if timeStep < 1:
        raise ValueError('timeStep must be >= 1')
    #if minTime != None and minTime < getLatestForecastTime():
    #    raise ValueError('minTime is before the current forecast time.')
    #if maxTime > ...
    
    try:
        areaVP = DEFS['vars'][area]
    except IndexError:
        raise ValueError('Invalid Area.')

    validVar = False
    for vp in areaVP:
        if var in areaVP[vp]:
            validVar = True
            break
    if not validVar:
        raise ValueError('Variable not available in area: ' + area)

'''

  Function:	getForecastAnalysis
  Purpose:	Analyze a grid point for any NDFD forecast variable in any NDFD grid area.
		The grid point will be the closest point to the supplied coordinates.
  Params:
	var:		The NDFD variable to analyzes
	lat:		Latitude
	lon:		Longitude
	n:		The levels away from the grid point to analyze. Default = 1
	timeStep:	The time step in hours to use in analyzing forecasts. Default = 1
	elev:		Boolean that indicates whether to include elevation of the grid points
			Default = False
	minTime:	Optional minimum time for the forecast analysis
	maxTime:	Optional maximum time for the forecast analysis
	area:		Used to specify a specific NDFD grid area. Default is to find the 
			smallest grid the supplied coordinates lie in.

'''
def getForecastAnalysis(var, lat, lon, n=0, timeStep=1, elev=False, minTime=None, maxTime=None, area=None):
    if n < 0:
        raise ValueError('n must be >= 0')
    negN = n * -1

    if area == None:
        area = getSmallestGrid(lat, lon)
    validateArguments(var, area, timeStep, minTime, maxTime)

    analysis = { }
    analysis['var'] = var
    analysis['reqLat'] = lat
    analysis['reqLon'] = lon
    analysis['n'] = n
    analysis['forecastTime'] = getLatestForecastTime()
    analysis['forecasts'] = { }
    
    validTimes = []
    for hour in range(0, 250, timeStep):
        t = analysis['forecastTime'] - timedelta(hours=analysis['forecastTime'].hour) + timedelta(hours=hour)
        if minTime != None and t < minTime:
            continue
        if maxTime != None and t > maxTime:
            break
        validTimes.append(t)
    
    varGrbs = getVariable(var, area)
    allVals = []
    firstRun = True
    for g in varGrbs:
        grbs = pygrib.open(g)
        for grb in grbs:
            t = datetime(grb['year'], grb['month'], grb['day'], grb['hour']) + timedelta(hours=grb['forecastTime'])
            if not t in validTimes:
                continue

            x, y, gridX, gridY, gLat, gLon = getNearestGridPoint(grb, lat, lon)
            if firstRun:
                analysis['gridLat'] = gLat
                analysis['gridLon'] = gLon
                analysis['units'] = grb['parameterUnits']
                try: 
                    analysis['deltaX'] = grb['DxInMetres']
                    analysis['deltaY'] = grb['DyInMetres']
                except:
                    analysis['deltaX'] = grb['DiInMetres']
                    analysis['deltaY'] = grb['DjInMetres']
                analysis['distance'] = G.inv(lon, lat, gLon, gLat)[-1]
                firstRun = False
            
            vals = []
            if elev:
                eGrbs = pygrib.open(getElevationVariable(area))
                e = eGrbs[1]
                eX, eY, eGridX, eGridY, eLat, eLon = getNearestGridPoint(e, lat, lon, projparams=grb.projparams)
                eVals = []
            try:
                if n == 0:
                    val = grb.values[y][x]
                    if type(val) == NAN:
                        val = float('nan')
                    vals.append(val)
                    allVals.append(val)
                    nearestVal = val
                    if elev:
                        eVal = e.values[eY][eX]
                        if type(eVal) == NAN:
                            eVal = float('nan')
                        eVals.append(eVal)
                        eNearestVal = eVal
                else:
                    for i in range(min(n, negN), max(n, negN) + 1):
                        for j in range(min(n, negN), max(n, negN) + 1):
                            val = grb.values[y + j][x + i]
                            if type(val) == NAN:
                                val = float('nan')
                            vals.append(val)
                            allVals.append(val)
                            if i == 0 and j == 0:
                                nearestVal = val
                            if elev:
                                eVal = e.values[eY + j][eX + i]
                                if type(eVal) == NAN:
                                    eVal = float('nan')
                                eVals.append(eVal)
                                if i == 0 and j == 0:
                                    eNearestVal = eVal
            except IndexError:
                raise ValueError('Given coordinates go beyond the grid. Use different coordinates, a larger area or use a smaller n value.')
            
            forecast = { }
            forecast['nearest'] = nearestVal
            if len(vals) > 1:
                forecast['points'] = len(vals)
                forecast['min'] = min(vals)
                forecast['max'] = max(vals)
                forecast['mean'] = sum(vals) / len(vals)
                forecast['median'] = median(vals)
                forecast['stdDev'] = stdDev(vals)        

            if elev:
                elevation = { }
                elevation['nearest'] = eNearestVal
                elevation['units'] = e['parameterUnits']
                if len(eVals) > 1:
                    elevation['points'] = len(eVals)
                    elevation['min'] = min(eVals)
                    elevation['max'] = max(eVals)
                    elevation['mean'] = sum(eVals) / len(eVals)
                    elevation['median'] = median(eVals)
                    elevation['stdDev'] = stdDev(eVals)
                analysis['elevation'] = elevation
                eGrbs.close()
                elev = False
             
            analysis['forecasts'][t] = forecast
        grbs.close()

    analysis['min'] = min(allVals)
    analysis['max'] = max(allVals)
    analysis['mean'] = sum(allVals) / len(allVals)
    analysis['median'] = median(allVals)
    analysis['stdDev'] = stdDev(allVals)

    return analysis

'''

  Function:	unpackString
  Purpose:	To unpack the packed binary string in the local use section of NDFD gribs
  Params:
	raw:	The raw byte string containing the packed data
  Notes:
	- This function is pretty slow and could be optimized with a C routine.

'''
def unpackString(raw):
    msg = ''

    bits = BitArray(bytes=raw)
    mask = BitArray('0b01111111')

    i = 0
    while 1:
        try:
            iByte = (bits[i:i + 8] & mask).int
            if iByte == 0:
                msg += '\n'
            elif iByte >= 32 and iByte <= 126:
                msg += chr(iByte)
            i += 7
        except:
            break

    codes = []
    for line in msg.splitlines():
        if len(line) >= 4 and (line.count(':') >= 4 or line.count('.') >= 1 or '<None>' in line):
            codes.append(line)

    return codes

'''

  Function:	parseWeatherString
  Purpose:	To create a readable, English string describing the weather
  Params:
	wxString:	The weather string to translate into English
  Notes:
	- See http://graphical.weather.gov/docs/grib_design.html for details

'''
def parseWeatherString(wxString):
    weatherString = ''
    visibility = float('nan')

    words = wxString.split('^')
    for word in words:
        entries = word.split(':')
        coverage = entries[0]
        weather = entries[1]
        intensity = entries[2]
        vis = entries[3]
        attributes = entries[4].split(',')

        ws = ''
        prepend = False
        OR = False
        likely = False

        if '<NoCov>' in coverage:
            pass
        elif 'Lkly' in coverage:
            likely = True
        elif coverage in DEFS['wx']['coverage']:
            ws += DEFS['wx']['coverage'][coverage] + ' '
        else:
            stderr.write('WARNING: Unknown coverage code: ' + coverage + '\n'); stderr.flush()

        if '<NoInten>' in intensity:
            pass
        elif intensity in DEFS['wx']['intensity']:
            ws += DEFS['wx']['intensity'][intensity] + ' '
        else:
            stderr.write('WARNING: Unknown intensity code: ' + intensity + '\n'); stderr.flush()

        if '<NoWx>' in weather:
            pass
        elif weather in DEFS['wx']['weather']:
            ws += DEFS['wx']['weather'][weather] + ' '
        else:
            stderr.write('WARNING: Unknown weather code: ' + weather + '\n'); stderr.flush()

        if likely:
            ws += 'likely '

        for attribute in attributes:
            if len(attribute) == 0 or '<None>' in attribute:
                pass
            elif attribute == 'Primary':
                prepend = True
            elif attribute == 'OR':
                OR = True
            elif attribute in DEFS['wx']['hazards']:
                ws += 'with ' + DEFS['wx']['hazards'][attribute]
            elif attribute in DEFS['wx']['attributes']:
                ws += DEFS['wx']['attributes'][attribute]
            else:
                stderr.write('WARNING: Unknown attribute code: ' + attribute + '\n'); stderr.flush()

        if len(weatherString) == 0:
            weatherString = ws
        else:
            if prepend and OR:
                weatherString = ws + 'or ' + weatherString.lower()
            elif prepend:
                weatherString = ws + 'and ' + weatherString.lower()
            elif OR:
                weatherString += 'or ' + ws.lower()
            else:
                weatherString += 'and ' + ws.lower()

        if '<NoVis>' in vis:
            vis = float('nan')
        elif vis in DEFS['wx']['visibility']:
            vis = DEFS['wx']['visibility'][vis]
        else:
            stderr.write('WARNING: Unknown visibility code: ' + vis + '\n'); stderr.flush()
            vis = float('nan')

        if not isnan(vis) and isnan(visibility):
            visibility = vis
        elif not isnan(vis) and vis < visibility:
            visibility = vis

    if len(weatherString) == 0:
        weatherString = '<NoWx>'
    else:
        weatherString = weatherString.strip().capitalize()

    return weatherString, visibility

'''

  Function:	parseAdvisoryString
  Purpose:	To create a readable, English string describing current weather hazards
  Params:
	wwaString:	The Watch, Warning, Advisory string to translate to English
  Notes:
	- See http://graphical.weather.gov/docs/grib_design.html for details

'''
def parseAdvisoryString(wwaString):
    advisoryString = ''

    words = wwaString.split('^')
    for word in words:
        if '<None>' in word:
            continue

        entries = word.split('.')
        hazard = entries[0]
        advisory = entries[1]

        if hazard in DEFS['wwa']['hazards']:
            advisoryString += DEFS['wwa']['hazards'][hazard] + ' '
        else:
            stderr.write('WARNING: Unknown hazard code: ' + hazard + '\n'); stderr.flush()

        if advisory in DEFS['wwa']['advisories']:
            advisoryString += DEFS['wwa']['advisories'][advisory] + '\n'
        else:
            stderr.write('WARNING: Unknown advisory code: ' + advisory + '\n'); stderr.flush()

    if len(advisoryString) == 0:
        advisoryString = '<None>'
    else:
        advisoryString = advisoryString.strip().title()

    return advisoryString

'''

  Function:	getWeatherAnalysis
  Purpose:	To get an English representation of the current weather and any NWS
		watch, warning, advisories in effect

'''
def getWeatherAnalysis(lat, lon, timeStep=1, minTime=None, maxTime=None, area=None):
    if area == None:
        area = getSmallestGrid(lat, lon)
    validateArguments('wx', area, timeStep, minTime, maxTime)

    analysis = { }
    analysis['reqLat'] = lat
    analysis['reqLon'] = lon
    analysis['forecastTime'] = getLatestForecastTime()
    analysis['forecasts'] = { }

    validTimes = []
    for hour in range(0, 250, timeStep):
        t = analysis['forecastTime'] - timedelta(hours=analysis['forecastTime'].hour) + timedelta(hours=hour)
        if minTime != None and t < minTime:
            continue
        if maxTime != None and t > maxTime:
            break
        validTimes.append(t)

    wxGrbs = getVariable('wx', area)
    firstRun = True
    for g in wxGrbs:
        grbs = pygrib.open(g)
        ncepgrbs = ncepgrib(g)
        for grb in grbs:
            t = datetime(grb['year'], grb['month'], grb['day'], grb['hour']) + timedelta(hours=grb['forecastTime'])
            if not t in validTimes:
                continue
            
            ncepgrb = ncepgrbs[grb.messagenumber - 1]
            if not ncepgrb.has_local_use_section:
                raise RuntimeError('Unable to read wx definitions from grib. Is it not a wx grib file??')
            
            x, y, gridX, gridY, gLat, gLon = getNearestGridPoint(grb, lat, lon)
            if firstRun:
                analysis['gridLat'] = gLat
                analysis['gridLon'] = gLon
                try: 
                    analysis['deltaX'] = grb['DxInMetres']
                    analysis['deltaY'] = grb['DyInMetres']
                except:
                    analysis['deltaX'] = grb['DiInMetres']
                    analysis['deltaY'] = grb['DjInMetres']
                analysis['distance'] = G.inv(lon, lat, gLon, gLat)[-1]
                firstRun = False

            try:
                val = grb.values[y][x]
            except IndexError:
                raise ValueError('Coordinates outside the given area.')

            forecast = { }
            forecast['wxString'] = None
            forecast['weatherString'] = None
            forecast['visibility'] = float('nan')
            forecast['wwaString'] = None
            forecast['advisoryString'] = None

            if val != grb['missingValue']:
                defs = unpackString(ncepgrb._local_use_section)
                forecast['wxString'] = defs[int(val)]
                forecast['weatherString'], forecast['visibility'] = parseWeatherString(forecast['wxString'])
            
            analysis['forecasts'][t] = forecast
        grbs.close()

    wwaGrbs = getVariable('wwa', area)
    for g in wwaGrbs:
        grbs = pygrib.open(g)
        ncepgrbs = ncepgrib(g)
        for grb in grbs:
            t = datetime(grb['year'], grb['month'], grb['day'], grb['hour']) + timedelta(hours=grb['forecastTime'])
            if not t in validTimes:
                continue
            
            ncepgrb = ncepgrbs[grb.messagenumber - 1]
            if not ncepgrb.has_local_use_section:
                raise RuntimeError('Unable to read wwa definitions from grib. Is it not a wwa grib file??')

            x, y, gridX, gridY, gLat, gLon = getNearestGridPoint(grb, lat, lon)
            try:
                val = grb.values[y][x]
            except IndexError:
                raise ValueError('Coordinates outside given area.')

            if not t in analysis['forecasts']:
                forecast = { }
                forecast['wxString'] = None
                forecast['weatherString'] = None
                forecast['visibility'] = float('nan')
                forecast['wwaString'] = None
                forecast['advisoryString'] = None
            else:
                forecast = analysis['forecasts'][t]
            
            if val != grb['missingValue']:
                defs = unpackString(ncepgrb._local_use_section)
                forecast['wwaString'] = defs[int(val)]
                forecast['advisoryString'] = parseAdvisoryString(forecast['wwaString'])

            analysis['forecasts'][t] = forecast
        grbs.close()

    return analysis
