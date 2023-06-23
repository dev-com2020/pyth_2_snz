import matplotlib.pyplot as plt
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

fb.plot(kind='line', subplots=True, layout=(3, 2),
        figsize=(15, 10), title='stocki facebooka')

plt.show()
