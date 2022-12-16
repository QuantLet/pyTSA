from numpy import random
import pandas as pd
import matplotlib.pyplot as plt
from PythonTsa.plot_acf_pacf import acf_pacf_fig
random.seed(135) # for repeat
x = random.normal(loc = 0, scale = 1, size = 1000)
xts = pd.Series(x)
xts.plot(); plt.xlabel('Time')
plt.ylabel('Simulated white noise')
plt.savefig('pyTSA_GaussWN_fig1-9.png', dpi = 1200, 
             bbox_inches ='tight', transparent = True, legend = None); plt.show()
acf_pacf_fig(xts, both=False, lag=30)
plt.savefig('pyTSA_GaussWN_fig1-10.png', dpi = 1200, 
             bbox_inches ='tight', transparent = True, legend = None); plt.show()