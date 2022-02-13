import numpy as np
import matplotlib.pyplot as plt
from PythonTsa.RandomWalk import RandomWalk_with_drift
from PythonTsa.plot_acf_pacf import acf_pacf_fig
np.random.seed(1379)
rw0 = RandomWalk_with_drift(drift = 0.0, nsample = 300, burnin = 10)
wn = np.random.normal(loc = 0, scale = 2.0, size = 300)
y = rw0+wn
y.plot()
plt.savefig('pyTSA_SimLLM_fig8-1.png', dpi = 1200, bbox_inches ='tight', 
            transparent = True, legend = None); plt.show() 
dy = y.diff().dropna()
dy.plot()
plt.savefig('pyTSA_SimLLM_fig8-2.png', dpi = 1200, bbox_inches ='tight', 
            transparent = True, legend = None); plt.show() 
acf_pacf_fig(dy, both = False, lag = 20)
plt.savefig('pyTSA_SimLLM_fig8-3.png', dpi = 1200, bbox_inches ='tight', 
            transparent = True, legend = None); plt.show() 