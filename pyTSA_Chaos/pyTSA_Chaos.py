import pandas as pd
import numpy as np
x = pd.Series(dtype = float)
y = 0.3 # start value
for t in range(1, 501):
    y = 4.0 * y * (1 - y)
    x = x.append(pd.Series(y))
index = range(1, 501)
x.index = index
np.savetxt('Chaos.csv', np.column_stack((x.index, x)), delimiter=',')