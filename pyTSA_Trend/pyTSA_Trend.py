import numpy as np
import matplotlib.pyplot as plt
from PythonTsa.RandomWalk import RandomWalk_with_drift
from PythonTsa.plot_acf_pacf import acf_pacf_fig
np.random.seed(1373)
rw0 = RandomWalk_with_drift(drift = 0.0, nsample = 250, burnin = 10)
# burnin: the number of observation at the beginning of the sample to drop.
# Used to reduce dependence on initial values.
rw0.plot(); 
plt.savefig('pyTSA_Trend_fig9-1.png', dpi = 1200, bbox_inches ='tight', 
            transparent = True, legend = None); plt.show() 
t = np.arange(1,len(rw0) + 1)
Mydata = 0.3 + 0.2*t + rw0
Mydata.plot()
plt.savefig('pyTSA_Trend_fig9-2.png', dpi = 1200, bbox_inches ='tight', 
            transparent = True, legend = None); plt.show() 
drw = rw0.diff(1).dropna()
drw.plot()
plt.savefig('pyTSA_Trend_fig9-3.png', dpi = 1200, bbox_inches ='tight', 
            transparent = True, legend = None); plt.show() 
acf_pacf_fig(drw, both = False, lag = 15)
plt.savefig('pyTSA_Trend_fig9-4.png', dpi = 1200, bbox_inches ='tight', 
            transparent = True, legend = None); plt.show() 