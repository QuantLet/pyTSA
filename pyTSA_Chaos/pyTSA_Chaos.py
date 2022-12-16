import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from PythonTsa.plot_acf_pacf import acf_pacf_fig
x = pd.Series(dtype = float)
y = 0.3 # start value
for t in range(1, 501):
    y = 4.0 * y * (1 - y)
    x = x.append(pd.Series(y))
index = range(1, 501)
x.index = index
np.savetxt('Chaos.csv', np.column_stack((x.index, x)), delimiter=',')
xts = pd.Series(x)
xts.plot();
plt.savefig('pyTSA_Chaos_fig1-11.png', dpi = 1200, 
             bbox_inches ='tight', transparent = True, legend = None); plt.show()
acf_pacf_fig(xts, both = False, lag = 30)
plt.savefig('pyTSA_Chaos_fig1-12.png', dpi = 1200, 
             bbox_inches ='tight', transparent = True, legend = None); plt.show()