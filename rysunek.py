import matplotlib.pyplot as plt
import pandas as pd

dane = pd.read_csv('pliki/AAPL_stock_price_example.csv', index_col='Date', parse_dates=True)
plt.plot(dane.index, dane.Close)
plt.show()
