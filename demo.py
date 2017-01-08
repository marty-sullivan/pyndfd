
from datetime import datetime, timedelta
from math import isnan
from time import time

from pyndfd import ndfd


def KtoF(k):
    return '{0:.2f}F'.format((k - 273.15) * 1.8 + 32.0)

def MMtoIN(mm):
    return '{0:.2f}"'.format(mm * 0.03937)

def MtoFT(m):
    return '{0:.2f}\''.format(m * 3.2808)

def MtoIN(m):
    return '{0:.2f}"'.format(m * 39.370)

def percent(pc):
    return str(pc) + '%'



# It's important to set the cache server to our own, or vars will be retrieved from NWS (slow)
ndfd.setLocalCacheServer('http://ndfd.eas.cornell.edu/')








# game farm rd
lat = 42.449167
lon = -76.449034


# variable to get
var = 'temp'

# time step for forecasts
timeStep = 3

# the minimum time and maximum time you would like to get back
minTime = datetime.utcnow() + timedelta(hours=0)
maxTime = datetime.utcnow() + timedelta(hours=12)

# whether to get elevation
getElev = False

# specify a specific area/grid to use
area = 'conus'






startTime = int(time() * 1000)



analysis = ndfd.getForecastAnalysis(var, lat, lon, elev=True, timeStep=timeStep, area='conus')
#analysis = ndfd.getWeatherAnalysis(lat, lon, timeStep=timeStep, minTime=minTime, maxTime=maxTime)

print '\n**********'
print 'Var: ' + str(analysis['var'])
print 'Units: ' + str(analysis['units'])
print 'Distance: ' + str(analysis['distance'])
print 'Forecast Time: ' + str(analysis['forecastTime'])
print 'Max: ' + str(analysis['max'])
print 'Min: ' + str(analysis['min'])
print 'Mean: ' + str(analysis['mean'])
#print 'Elev: ' + str(analysis['elevation']['nearest'])
print 'stdDev: ' + str(analysis['stdDev'])
print '**********\n'

for t in sorted(analysis['forecasts']):
    forecast = analysis['forecasts'][t]
    print '{0}: {1}'.format(str(t), KtoF(forecast['nearest']))
    #print '\n{0}:\n{1}\n{2}\nwx:{3}\nVis: {4}'.format(str(t), forecast['advisoryString'], forecast['weatherString'], forecast['wxString'], forecast['visibility'])

print '\nElapsed: ' + str(int(time() * 1000) - startTime)
