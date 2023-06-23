from urllib.request import urlopen
from urllib.error import HTTPError
import pandas as pd
from seaborn.utils import urlretrieve
import os
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# datafile = 'https://docs.misoenergy.org/marketreports/20210203_mom.xlsx'
# mom_data = urlopen(datafile).read()
# df = pd.read_excel(mom_data)
# print(df.head())

url2 = 'https://docs.misoenergy.org/marketreports/{}_mom.xlsx'
dates = pd.date_range(start='20191106', end='20210205')
dates = dates.strftime(date_format='%Y%m%d')
print(dates)

for d in dates:
    filename = f'/pliki/{d}_mom.xlsx'
    if os.path.exists(filename):
        continue
    try:
        urlretrieve(url2.format(d), filename)
    except HTTPError:
        continue
