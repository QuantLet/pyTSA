import numpy as np
import matplotlib.pyplot as plt
from PythonTsa.plot_multi_ACF import multi_ACFfig
from PythonTsa.MultiCorrPvalue import MultiTrCorrPvalue
from PythonTsa.plot_multi_Q_pvalue import MultiQpvalue_plot
mean = [0, 0, 0, 0]
cov = [[1.0, 0.6, 0.2, 0.1], 
[0.6, 1.0, 0.1, 0.4], 
[0.2, 0.1, 1.0, 0.5], 
[0.1, 0.4, 0.5, 1.0]]
np.random.seed(1517)
x = np.random.multivariate_normal(mean, cov, size = 10000)
multi_ACFfig(x, nlags = 12)
plt.savefig('pyTSA_MultiDimGN_fig7-1.png', dpi = 1200, bbox_inches ='tight', 
            transparent = True, legend = None)
tr_st, pv = MultiTrCorrPvalue(x, lags = 20)
plt.savefig('pyTSA_MultiDimGN_fig7-2.png', dpi = 1200, bbox_inches ='tight', 
            transparent = True, legend = None)
qs, pv = MultiQpvalue_plot(x, nolags = 24)
plt.savefig('pyTSA_MultiDimGN_fig7-3.png', dpi = 1200, bbox_inches ='tight', 
            transparent = True, legend = None)
