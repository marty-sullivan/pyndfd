from bitstring import BitArray
from datetime import datetime, timedelta
from math import isnan, sqrt
from ncepgrib2 import Grib2Decode as ncepgrib
from numpy.ma.core import MaskedConstant as NAN
from os import mkdir, path
from pyproj import Geod, Proj
from subprocess import call
from sys import stderr
import json
import ndfd_defs
import pygrib

DEFS = ndfd_defs.ndfdDefs()
G = Geod(ellps='clrk66')

CMD_WGET_REMOTE = 'wget -x -nH --cut-dirs=4 -P {0} {1}'
CMD_WGET_LOCAL = 'wget -x -nH -P {0} {1}'

CACHE_SERVER_BUFFER_MIN = 10

NDFD_LOCAL_SERVER = None
NDFD_REMOTE_SERVER = 'http://weather.noaa.gov/pub/SL.us008001/ST.opnl/DF.gr2/'
NDFD_VAR = 'DC.ndfd/AR.{0}/VP.{1}/ds.{2}.bin'
NDFD_STATIC = 'static/DC.ndfd/AR.{0}/ds.{1}.bin'
NDFD_TMP = '/tmp/ndfd/'

def setLocalCacheServer(uri):
    global NDFD_LOCAL_SERVER 
    NDFD_LOCAL_SERVER = uri

def stdDev(vals):
    mean = sum(vals) / len(vals)
    squared = []
    for val in vals:
        squared.append(pow(val - mean, 2))
    variance = sum(squared) / len(squared)
    return sqrt(variance)

def median(vals):
    sortedLst = sorted(vals)
    lstLen = len(vals)
    index = (lstLen - 1) // 2
    if (lstLen % 2):
        return sortedLst[index]
    else:
        return (sortedLst[index] + sortedLst[index + 1]) / 2.0

def getLatestForecastTime():
    latestTime = datetime.utcnow()
    if latestTime.minute <= CACHE_SERVER_BUFFER_MIN:
        latestTime = (datetime.utcnow() - timedelta(hours=1))
    return latestTime.replace(minute=0, second=0, microsecond=0)

def getVariable(var, area):
    gribs = []
    dirTime = NDFD_TMP + getLatestForecastTime().strftime('%Y-%m-%d-%H') + '/'
    if not path.isdir(NDFD_TMP):
        mkdir(NDFD_TMP)
    if not path.isdir(dirTime):
        mkdir(dirTime)
    if area in DEFS['vars']:
        for vp in DEFS['vars'][area]:
            if var in DEFS['vars'][area][vp]:
                varName = NDFD_VAR.format(area, vp, var)
                localVar = dirTime + varName
                if not path.isfile(localVar):
                    if NDFD_LOCAL_SERVER != None:
                        remoteVar = NDFD_LOCAL_SERVER + varName
                        call(CMD_WGET_LOCAL.format(dirTime, remoteVar).split())
                    else:
                        remoteVar = NDFD_REMOTE_SERVER + varName
                        call(CMD_WGET_REMOTE.format(dirTime, remoteVar).split())
                if not path.isfile(localVar):
                    raise RuntimeError('Cannot retrieve NDFD variables at this time. Try again in a moment.')
                gribs.append(localVar)

    return gribs

def getElevationVariable(area):
    if area == 'puertori':
        raise ValueError('Elevation currently not available for Puerto Rico. Set elev=False')
    if NDFD_LOCAL_SERVER == None:
        raise RuntimeError('Local cache server must provide elevation data. Specify cache server with ndfd.setLocalCacheServer(uri)')
    if not path.isdir(NDFD_TMP):
        mkdir(NDFD_TMP)
    remoteVar = NDFD_LOCAL_SERVER + NDFD_STATIC.format(area, 'elev')
    localVar = NDFD_TMP + NDFD_STATIC.format(area, 'elev')
    if not path.isfile(localVar):
        call(CMD_WGET_LOCAL.format(NDFD_TMP, remoteVar).split())
    if not path.isfile(localVar):
        raise RuntimeError('Cannot retrieve NDFD variables at this time. Try again in a moment.')
    return localVar

def getSmallestGrid(lat, lon):
    smallest = 'conus'

    for area in DEFS['grids'].keys():
        curArea = DEFS['grids'][area]
        smallArea = DEFS['grids'][smallest]
        if curArea['size'] < smallArea['size']:
            if lat >= curArea['lat1'] and lat <= curArea['lat2']:
                if lon >= curArea['lon1'] and lon <= curArea['lon2']:
                    smallest = area

    return smallest

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
    

def validateArguments(var, area, timeStep, minTime, maxTime):
    if timeStep < 1:
        raise ValueError('timeStep must be >= 1')
    if minTime != None and minTime < getLatestForecastTime():
        raise ValueError('minTime is before the current forecast time.')
    #if maxTime > ...
    
    try:
        area = DEFS['vars'][area]
    except IndexError:
        raise ValueError('Invalid Area.')

    validVar = False
    for vp in area:
        if var in area[vp]:
            validVar = True
            break
    if not validVar:
        raise ValueError('Variable not available in area: ' + area)

def getForecastAnalysis(var, lat, lon, n=1, timeStep=1, elev=False, minTime=None, maxTime=None, area=None, shiftX=0, shiftY=0):
    if n < 0:
        raise ValueError('n must be >= 0')
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

    negN = n * -1

    validTimes = []
    for hour in range(0, 250, timeStep):
        t = analysis['forecastTime'] - timedelta(hours=analysis['forecastTime'].hour) + timedelta(hours=hour)
        if minTime != None and t < minTime:
            continue
        if maxTime != None and t > maxTime:
            break
        validTimes.append(t)
    
    varGrbs = getVariable(var, area)
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
                analysis['distanceM'] = G.inv(lon, lat, gLon, gLat)
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
                    if elev:
                        eVal = e.values[eY][eX]
                        if type(eVal) == NAN:
                            eVal = float('nan')
                        eVals.append(eVal)
                else:
                    for i in range(min(n, negN), max(n, negN) + 1):
                        for j in range(min(n, negN), max(n, negN) + 1):
                            val = grb.values[y + j][x + i]
                            if type(val) == NAN:
                                val = float('nan')
                            vals.append(val)
                            if elev:
                                eVal = e.values[eY + j][eX + i]
                                if type(eVal) == NAN:
                                    eVal = float('nan')
                                eVals.append(eVal)
            except IndexError:
                raise ValueError('Given coordinates go beyond the grid. Use different coordinates, use a smaller n value or shiftX/Y')
            
            forecast = { }
            forecast['points'] = len(vals)
            forecast['min'] = min(vals)
            forecast['max'] = max(vals)
            forecast['mean'] = sum(vals) / len(vals)
            forecast['median'] = median(vals)
            forecast['stdDev'] = stdDev(vals)        

            if elev:
                elevation = { }
                elevation['points'] = len(eVals)
                elevation['min'] = min(eVals)
                elevation['max'] = max(eVals)
                elevation['mean'] = sum(eVals) / len(eVals)
                elevation['median'] = median(eVals)
                elevation['stdDev'] = stdDev(eVals)
                elevation['units'] = e['parameterUnits']
                analysis['elevation'] = elevation
                eGrbs.close()
                elev = False
             
            analysis['forecasts'][t] = forecast
        grbs.close()
    return analysis

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
                analysis['distanceM'] = G.inv(lon, lat, gLon, gLat)
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
