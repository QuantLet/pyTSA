import numpy as np
from PythonTsa.True_acf import Tacf_pacf_fig
import matplotlib.pyplot as plt
ar1 = np.array([1, 0, 0, 0, -0.36])
Tacf_pacf_fig(ar = ar1, ma = [1], both = True, lag = 20)
plt.savefig('pyTSA_SARMA_fig5-6.png', dpi = 1200, 
             bbox_inches ='tight', transparent = True, legend = None);
ma1 = np.array([1,0,0,0,0.46])
Tacf_pacf_fig(ar = [1], ma = ma1, both = True, lag = 20)
plt.savefig('pyTSA_SARMA_fig5-7.png', dpi = 1200, 
             bbox_inches ='tight', transparent = True, legend = None);
Tacf_pacf_fig(ar = ar1, ma = ma1, both = True, lag = 20)
plt.savefig('pyTSA_SARMA_fig5-8.png', dpi = 1200, 
             bbox_inches ='tight', transparent = True, legend = None);
