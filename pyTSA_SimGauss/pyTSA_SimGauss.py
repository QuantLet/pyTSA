import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
np.random.seed(135)
x = np.random.normal(loc=4.1, scale=2.2, size = 1000)
type(x)
h_fig = plt.hist(x, bins=25)
plt.xlabel('simulated sample'); plt.ylabel('frequency')
plt.savefig('pyTSA_SimGauss_fig1-5.png', dpi = 1200, 
             bbox_inches ='tight', transparent = True, legend = None); plt.show()
xts = pd.Series(x)
type(xts)
xts.plot(); plt.xlabel('Time'); plt.ylabel('Simulated sample')
plt.savefig('pyTSA_SimGauss_fig1-6.png', dpi = 1200, 
             bbox_inches ='tight', transparent = True, legend = None); plt.show()
