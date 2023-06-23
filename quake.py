import pandas as pd
from matplotlib import pyplot as plt

# quakes = pd.read_csv('pliki/quakes.csv')
# x = quakes.query('magType == "ml"').mag
# fig, axes = plt.subplots(1, 2, figsize=(10, 3))
# for ax, bins in zip(axes, [7, 35]):
#     ax.hist(x, bins=bins)
#     ax.set_title(f'bin params: {bins}')

fig = plt.figure(figsize=(3, 3))
outside = fig.add_axes([0.1, 0.1, 0.9, 0.9])
inside = fig.add_axes([0.7, 0.7, 0.25, 0.25])

plt.show()
