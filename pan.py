import pandas as pd

dane = pd.read_csv('pliki/AAPL_stock_price_example.csv', index_col='Date', parse_dates=True).assign(
    close_price_trading=lambda x: pd.cut(
        x.Close, bins=3, labels=['low', 'med', 'high']
    )
)
# print(dane)
# print(dane[224:226])
# print(dane['Date'].is_unique)
# print(dane['2019-07-01':'2019-09-01'])
print(dane.first('1M'))
print(dane.last('1M'))
print(dane.info())
print(dane.describe())