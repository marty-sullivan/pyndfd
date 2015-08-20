from distutils.core import setup

setup(
  name = 'pyndfd',
  packages = ['pyndfd'],
  version = '0.7',
  license = 'MIT License',
  description = 'Python routines for easy caching/retrieval of NWS\'s NDFD variables',
  author = 'Marty J. Sullivan',
  author_email = 'marty.sullivan@cornell.edu',
  url = 'https://github.com/marty-sullivan/pyndfd',
  download_url = 'https://github.com/marty-sullivan/pyndfd/tarball/0.7',
  install_requires = ['numpy', 'pygrib', 'pyproj'],
  keywords = ['noaa', 'ndfd', 'nws', 'weather', 'forecast', 'cornell', 'amospheric', 'science']
)
