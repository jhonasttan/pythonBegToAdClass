import matplotlib.pyplot as plt
import numpy as np

years = [1, 1000, 1500, 1600, 1700, 1750, 1800, 1850, 1900]
years = years + list(np.arange(1950, 2020, 5))

pop = [200, 400, 458, 580, 682, 791, 1000, 1261, 1650, 2525, 2758, 3018, 3322, 3682, 4061, 4440, 4853, 5310, 5735,
       6127, 6520, 6930, 7349]

plt.plot(years,pop)
plt.show()
