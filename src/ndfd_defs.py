
NDFD_VARS = \
{
  'conus': 
  { 
    '001-003': 
    [ 
      'apt',
      'conhazo',
      'critfireo',
      'dryfireo',
      'iceaccum',
      'maxrh',
      'maxt',
      'minrh',
      'mint',
      'phail',
      'pop12',
      'ptornado',
      'ptotsvrtstm',
      'ptotxsvrtstm',
      'ptstmwinds',
      'pxhail',
      'pxtornado',
      'pxtstmwinds',
      'qpf',
      'rhm',
      'sky',
      'snow',
      'tcwspdabv34c',
      'tcwspdabv34i',
      'tcwspdabv50c',
      'tcwspdabv50i',
      'tcwspdabv64c',
      'tcwspdabv64i',
      'td',
      'temp',
      'waveh',
      'wdir',
      'wgust',
      'wspd',
      'wwa',
      'wx'
    ],
    '004-007': 
    [ 
      'apt',
      'conhazo',
      'critfireo',
      'dryfireo',
      'maxrh',
      'maxt',
      'minrh',
      'mint',
      'pop12',
      'rhm',
      'sky',
      'tcwspdabv34c',
      'tcwspdabv34i',
      'tcwspdabv50c',
      'tcwspdabv50i',
      'tcwspdabv64c',
      'tcwspdabv64i',
      'td',
      'temp',
      'waveh',
      'wdir',
      'wspd',
      'wwa',
      'wx'
    ],
    '008-450': 
    [ 
      'prcpabv14d',
      'prcpabv30d',
      'prcpabv90d',
      'prcpblw14d',
      'prcpblw30d',
      'prcpblw30d',
      'tmpabv14d',
      'tmpabv30d',
      'tmpabv90d',
      'tmpblw14d',
      'tmpblw30d',
      'tmpblw90d'
    ]
  },
  'alaska': 
  { 
    '008-450':
    [ 
      'prcpabv14d',
      'prcpabv30d',
      'prcpabv90d',
      'prcpblw14d',
      'prcpblw30d',
      'prcpblw30d',
      'tmpabv14d',
      'tmpabv30d',
      'tmpabv90d',
      'tmpblw14d',
      'tmpblw30d',
      'tmpblw90d'
    ]
  },
  'guam': 
  {
    '001-003': 
    [ 
      'apt',
      'maxrh',
      'maxt',
      'minrh',
      'mint',
      'pop12',
      'rhm',
      'sky',
      'td',
      'temp',
      'waveh',
      'wdir',
      'wgust',
      'wspd',
      'wwa',
      'wx'
    ],
    '004-007': 
    [ 
      'apt',
      'maxrh',
      'maxt',
      'minrh',
      'mint',
      'pop12',
      'rhm',
      'sky',
      'td',
      'temp',
      'waveh',
      'wdir',
      'wspd',
      'wwa',
      'wx'
    ]
  },
  'hawaii': 
  {
    '001-003': 
    [ 
      'apt',
      'maxrh',
      'maxt',
      'minrh',
      'mint',
      'pop12',
      'qpf',
      'rhm',
      'sky',
      'snow',
      'td',
      'temp',
      'waveh',
      'wdir',
      'wgust',
      'wspd',
      'wwa',
      'wx'
    ],
    '004-007': 
    [ 
      'apt',
      'maxrh',
      'maxt',
      'minrh',
      'mint',
      'pop12',
      'rhm',
      'sky',
      'td',
      'temp',
      'waveh',
      'wdir',
      'wspd',
      'wwa',
      'wx'
    ] 
  },
  'nhemi': 
  { 
    '001-003': 
    [ 
      'tcwspdabv34c',
      'tcwspdabv34i',
      'tcwspdabv50c',
      'tcwspdabv50i',
      'tcwspdabv64c',
      'tcwspdabv64i'
    ],
    '004-007': 
    [ 
      'tcwspdabv34c',
      'tcwspdabv34i',
      'tcwspdabv50c',
      'tcwspdabv50i',
      'tcwspdabv64c',
      'tcwspdabv64i'
    ]
  },
  'npacocn': 
  {
    '001-003': 
    [ 
      'tcwspdabv34c',
      'tcwspdabv34i',
      'tcwspdabv50c',
      'tcwspdabv50i',
      'tcwspdabv64c',
      'tcwspdabv64i'
    ],
    '004-007': 
    [ 
      'tcwspdabv34c',
      'tcwspdabv34i',
      'tcwspdabv50c',
      'tcwspdabv50i',
      'tcwspdabv64c',
      'tcwspdabv64i'
    ]
  },
  'puertori': 
  { 
    '001-003': 
    [ 
      'apt',
      'maxrh',
      'maxt',
      'minrh',
      'mint',
      'pop12',
      'qpf',
      'rhm',
      'sky',
      'td',
      'temp',
      'waveh',
      'wdir',
      'wgust',
      'wspd',
      'wwa',
      'wx'
    ],
    '004-007': 
    [ 
      'apt',
      'maxrh',
      'maxt',
      'minrh',
      'mint',
      'pop12',
      'rhm',
      'sky',
      'td',
      'temp',
      'waveh',
      'wdir',
      'wspd',
      'wwa',
      'wx'
    ]
  }
}
NDFD_VARS['crgrlake'] = NDFD_VARS['conus']
NDFD_VARS['crmissvy'] = NDFD_VARS['conus']
NDFD_VARS['crplains'] = NDFD_VARS['conus']
NDFD_VARS['crrocks'] = NDFD_VARS['conus']
NDFD_VARS['ergrlake'] = NDFD_VARS['conus']
NDFD_VARS['midatlan'] = NDFD_VARS['conus']
NDFD_VARS['neast'] = NDFD_VARS['conus']
NDFD_VARS['nplains'] = NDFD_VARS['conus']
NDFD_VARS['nrockies'] = NDFD_VARS['conus']
NDFD_VARS['pacnwest'] = NDFD_VARS['conus']
NDFD_VARS['pacswest'] = NDFD_VARS['conus']
NDFD_VARS['seast'] = NDFD_VARS['conus']
NDFD_VARS['smissvly'] = NDFD_VARS['conus']
NDFD_VARS['splains'] = NDFD_VARS['conus']
NDFD_VARS['srockies'] = NDFD_VARS['conus']
NDFD_VARS['umissvly'] = NDFD_VARS['conus']

WX_VARS = \
{
  'coverage':
  {
    '<NoCov>': 'No Coverage',
    'Sct': 'Scattered',
    'Wide': 'Widespread',
    'SChc': 'Slight chance of',
    'Lkly': 'Likely',
    'Patchy': 'Patchy',
    'Brf': 'Brief',
    'Frq': 'Frequent',
    'Iso': 'Isolated',
    'Num': 'Numerous',
    'Ocnl': 'Occasional',
    'Chc': 'Chance of',
    'Def': 'Definite',
    'Areas': 'Areas of',
    'Pds': 'Periods of',
    'Inter': 'Intermittent',
  },
  'weather':
  {
    '<NoWx>': 'No Weather',
    'A': 'hail',
    'RW': 'rain showers',
    'ZR': 'freezing rain',
    'S': 'snow',
    'IP': 'sleet',
    'H': 'haze',
    'K': 'smoke',
    'FR': 'frost',
    'IF': 'ice fog',
    'ZF': 'freezing fog',
    'VA': 'volcanic ash',
    'T': 'thunder',
    'R': 'rain',
    'L': 'drizzle',
    'ZL': 'freezing drizzle',
    'SW': 'snow showers',
    'F': 'fog',
    'BS': 'blowing snow',
    'BD': 'blowing dust',
    'BN': 'blowing sand',
    'IC': 'ice crystals',
    'ZY': 'freezing spray',
    'WP': 'water spouts',
  },
  'intensity':
  {
    '<NoInten>': 'No Intensity',
    '--': 'very light',
    '-': 'light',
    'm': 'moderate',
    '+': 'heavy'
  },
  'visibility':
  {
    '<NoVis>': float('nan'),
    '0SM': 0.0,
    '1/4SM': 0.25,
    '1/2SM': 0.5,
    '3/4SM': 0.75,
    '1SM': 1.0,
    '11/2SM': 1.5,
    '2SM': 2.0,
    '21/2SM': 2.5,
    '3SM': 3.0,
    '4SM': 4.0,
    '5SM': 5.0,
    '6SM': 6.0,
    'P6SM': 7.0
  },
  'hazards':
  {
    'FL': 'frequent lightning',
    'HvyRn': 'heavy rain',
    'SmA': 'small hail',
    'Dry': 'dry conditions',
    'GW': 'gusty winds',
    'DmgW': 'damaging winds',
    'LgA': 'Large Hail',
    'TOR': 'tornado'
  },
  'attributes':
  {
    'OLA': 'on outlying areas',
    'OGA': 'on grassy areas',
    'Mention': 'include unconditionally',
    'Mx': 'mixture',
    'OBO': 'on bridges and overpasses',
    'OR': 'or',
    'Primary': 'highest ranking'
  }
}

WWA_VARS = \
{
  'advisories':
  {
    'A': 'Watch',
    'S': 'Statement',
    'W': 'Warning',
    'Y': 'Advisory'
  },
  'hazards':
  {
    '<None>': 'No Hazard',
    'AF': 'Ash Fall',
    'AS': 'Air Stagnation',
    'BS': 'Blowing Snow',
    'BW': 'Brisk Wind',
    'BZ': 'Blizzard',
    'CF': 'Coastal Flood',
    'DS': 'Dust Storm',
    'DU': 'Blowing Dust',
    'EC': 'Extreme Cold',
    'EH': 'Excessive Heat',
    'EW': 'Extreme Wind',
    'FA': 'Areal Flood',
    'FF': 'Flash Flood',
    'FG': 'Dense Fog',
    'FL': 'Flood',
    'FR': 'Frost',
    'FW': 'Fire Weather',
    'FZ': 'Freeze',
    'GL': 'Gale',
    'HF': 'Hurricane Force Wind',
    'HI': 'Hurricane Wind',
    'HS': 'Heavy Snow',
    'HT': 'Heat',
    'HU': 'Hurricane',
    'HW': 'High Wind',
    'HZ': 'Hard Freeze',
    'IP': 'Sleet',
    'IS': 'Ice Storm',
    'LB': 'Lake Effect Snow and Blowing Snow',
    'LE': 'Lake Effect Snow',
    'LO': 'Low Water',
    'LS': 'Lake Shore Flood',
    'LW': 'Lake Wind',
    'MA': 'Marine Weather',
    'MF': 'Dense Fog',
    'MH': 'Ash Fall',
    'MS': 'Dense Smoke',
    'RB': 'Small Craft: Rough Bar',
    'SB': 'Snow and Blowing Snow',
    'SC': 'Small Craft',
    'SE': 'Hazardous Seas',
    'SI': 'Small Craft: Winds',
    'SM': 'Dense Smoke',
    'SN': 'Snow',
    'SR': 'Storm',
    'SU': 'High Surf',
    'SV': 'Severe Thunderstorm',
    'SW': 'Small Craft: Hazardous Waters',
    'TI': 'Tropical Storm Wind',
    'TO': 'Tornado',
    'TR': 'Tropical Storm',
    'TS': 'Tsunami',
    'TY': 'Typhoon',
    'UP': 'Heavy Freezing Spray',
    'WC': 'Wind Chill',
    'WI': 'Wind',
    'WS': 'Winter Storm',
    'WW': 'Winter Weather',
    'ZF': 'Freezing Fog',
    'ZR': 'Freezing Rain',
    'ZY': 'Freezing Spray'
  }
}

GRID_VARS = \
{'nhemi': {'lon1': -152.85541168816883, 'lon2': -49.385297482599491, 'lat1': 12.189999000000027, 'size': 1509825, 'lat2': 61.279780495548636}, 'guam': {'lon1': 143.68653800000001, 'lon2': 148.28, 'lat1': 12.349881999999987, 'size': 37249, 'lat2': 16.794398999999988}, 'puertori': {'lon1': -68.027832999999944, 'lon2': -63.984399999999987, 'lat1': 16.977482999999985, 'size': 76275, 'lat2': 19.521998999999973}, 'midatlan': {'lon1': -85.794219999999996, 'lon2': -74.008085199844743, 'lat1': 30.467212622968102, 'size': 38800, 'lat2': 40.280273659938707}, 'alaska': {'lon1': -179.99992765407791, 'lon2': 179.99980900453446, 'lat1': 40.530100999999995, 'size': 456225, 'lat2': 75.390971355528919}, 'splains': {'lon1': -108.49667483865878, 'lon2': -90.882510149476047, 'lat1': 25.106399000000025, 'size': 86350, 'lat2': 37.996679029684856}, 'nplains': {'lon1': -106.54790842857874, 'lon2': -90.524887641693269, 'lat1': 39.682700999999966, 'size': 60228, 'lat2': 50.137654874480404}, 'npacocn': {'lon1': -152.85541168816883, 'lon2': -49.385297482599491, 'lat1': 12.189999000000027, 'size': 1509825, 'lat2': 61.279780495548636}, 'crrocks': {'lon1': -115.30442150569472, 'lon2': -99.879845149060557, 'lat1': 35.104578999999966, 'size': 46990, 'lat2': 44.181214656978113}, 'crgrlake': {'lon1': -88.462128000000007, 'lon2': -77.130810670250483, 'lat1': 38.120194976858158, 'size': 37887, 'lat2': 48.150116622929914}, 'crmissvy': {'lon1': -95.412004133854126, 'lon2': -83.902858231730818, 'lat1': 33.77643285374711, 'size': 36839, 'lat2': 42.352563220781988}, 'srockies': {'lon1': -116.44821114426371, 'lon2': -100.85428275515683, 'lat1': 30.311589999999999, 'size': 50730, 'lat2': 39.919553736741626}, 'conus': {'lon1': -130.10343806997807, 'lon2': -60.885557729221034, 'lat1': 20.191999000000006, 'size': 2953665, 'lat2': 52.807668603250377}, 'umissvly': {'lon1': -100.86154032997325, 'lon2': -85.335284305236669, 'lat1': 38.049607496521858, 'size': 66150, 'lat2': 49.809296579738962}, 'smissvly': {'lon1': -96.061065121286958, 'lon2': -85.022550430823642, 'lat1': 28.3298312445107, 'size': 36616, 'lat2': 36.882529384900494}, 'neast': {'lon1': -78.717347000000004, 'lon2': -65.593524135209833, 'lat1': 37.393581074202316, 'size': 42823, 'lat2': 48.443564876376101}, 'seast': {'lon1': -90.897338999999988, 'lon2': -77.587992693829918, 'lat1': 23.253478160492701, 'size': 48843, 'lat2': 33.181282469968735}, 'pacswest': {'lon1': -126.10643935436615, 'lon2': -106.91132120541704, 'lat1': 29.26025000000001, 'size': 78624, 'lat2': 42.485093563698527}, 'crplains': {'lon1': -105.78122959322997, 'lon2': -92.625834521693918, 'lat1': 34.698848000000027, 'size': 41701, 'lat2': 43.220059737973706}, 'nrockies': {'lon1': -118.23276935582662, 'lon2': -98.530702200560185, 'lat1': 39.44027999999998, 'size': 69768, 'lat2': 50.306421764712873}, 'pacnwest': {'lon1': -128.86862112004593, 'lon2': -108.05966621083027, 'lat1': 39.494510000000005, 'size': 66356, 'lat2': 50.594747080761714}, 'hawaii': {'lon1': -161.524979, 'lon2': -153.869001, 'lat1': 18.072656000000002, 'size': 72225, 'lat2': 23.087799}, 'ergrlake': {'lon1': -86.487304999999964, 'lon2': -74.317366030289435, 'lat1': 38.416006782690651, 'size': 35904, 'lat2': 47.479141508380813}}

def ndfdDefs():
    return { 'vars': NDFD_VARS, 'wx': WX_VARS, 'wwa': WWA_VARS, 'grids': GRID_VARS }
