
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
{'nhemi': {'lonC': -100.5547707337221, 'latC': 40.60568536609355, 'size': 1509825}, 'guam': {'lonC': 145.9833572496674, 'latC': 14.583394122119477, 'size': 37249}, 'puertori': {'lonC': -66.00615355628241, 'latC': 18.25443391528987, 'size': 76275}, 'midatlan': {'lonC': -80.08212268970772, 'latC': 35.50017273099019, 'size': 38800}, 'alaska': {'lonC': -153.0128931396447, 'latC': 60.12781502200543, 'size': 456225}, 'splains': {'lonC': -99.42894335201238, 'latC': 31.776849688255663, 'size': 86350}, 'nplains': {'lonC': -98.32997169916455, 'latC': 45.12557007784838, 'size': 60228}, 'npacocn': {'lonC': -179.56420967686748, 'latC': 24.663412972627867, 'size': 1580529}, 'crrocks': {'lonC': -107.30242999298261, 'latC': 39.8247573600583, 'size': 46990}, 'crgrlake': {'lonC': -83.04687038362809, 'latC': 43.269091951527486, 'size': 37887}, 'crmissvy': {'lonC': -89.85525808934726, 'latC': 38.18659888001805, 'size': 36839}, 'srockies': {'lonC': -108.39840154112714, 'latC': 35.31391549893657, 'size': 50730}, 'conus': {'lonC': -95.4524033407926, 'latC': 38.21829701333828, 'size': 2953665}, 'umissvly': {'lonC': -93.20517762503603, 'latC': 44.1604283677903, 'size': 66150}, 'smissvly': {'lonC': -90.69563009235515, 'latC': 32.73214446882297, 'size': 36616}, 'neast': {'lonC': -72.4333066919216, 'latC': 43.06356470945907, 'size': 42823}, 'seast': {'lonC': -84.47197282984519, 'latC': 28.340905405095224, 'size': 48843}, 'pacswest': {'lonC': -116.095115120485, 'latC': 36.14134643164874, 'size': 78624}, 'crplains': {'lonC': -99.0486831495504, 'latC': 39.10288297842758, 'size': 41701}, 'nrockies': {'lonC': -107.92280242464689, 'latC': 45.19031554443591, 'size': 69768}, 'pacnwest': {'lonC': -118.10980677782631, 'latC': 45.351542779764905, 'size': 66356}, 'hawaii': {'lonC': -157.69694691722103, 'latC': 20.60086183593535, 'size': 72225}, 'ergrlake': {'lonC': -80.62536576992913, 'latC': 43.0970932712032, 'size': 35904}}

def ndfdDefs():
    return { 'vars': NDFD_VARS, 'wx': WX_VARS, 'wwa': WWA_VARS, 'grids': GRID_VARS }
