import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PythonTsa.RandomWalk import RandomWalk_with_drift
t = pd.Series(range(300), dtype = 'float64')
Tt = 0.1 + 0.4*t
np.random.seed(13711)
wn = np.random.normal(loc = 0, scale = 2, size = 300)
X = Tt + wn
Y = RandomWalk_with_drift(drift = 0.4, nsample = 300, burnin = 10)
XY = pd.DataFrame({'$X_t = 0.1 + 0.4t + \epsilon_t$':X, 
'$Y_t = 0.4 + Y_{t-1} + \epsilon_t$':Y})
XY.plot(style = ['-', ':'])
plt.savefig('pyTSA_Stationarity_fig9-21.png', dpi = 1200, bbox_inches ='tight', 
            transparent = True, legend = None); plt.show() 