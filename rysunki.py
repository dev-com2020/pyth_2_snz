import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

fb = pd.read_csv('pliki/fb_stock_prices_2018.csv', index_col='date', parse_dates=True)
# plt.plot('high', 'low', 'or', data=fb.head(20))
# plt.show()

# fb.plot(kind='line', y='open', figsize=(10, 5), legend=False, title='Otwarcie', color='red', linestyle='solid')
# fb.first('1W').plot(
#     y=['open', 'high', 'low', 'close'],
#     style=['o-b', '--r', ':k', '.-g'],
#     title='1st week of trading'
# ).autoscale()

# fb.plot(kind='line', subplots=True, layout=(3, 2),
#         figsize=(15, 10), title='stocki facebooka')

# fb.assign(
#     log_volume=np.log(fb.volume),
#     max_abs_change=fb.high - fb.low
# ).plot(kind='hexbin', x='log_volume', y='max_abs_change', colormap='gray_r', gridsize=20, sharex=False)

ax = fb.high.plot(kind='hist', density=True, alpha=0.5)
fb.high.plot(ax=ax, kind='kde', color='green')
plt.xlabel("Price")

plt.show()
