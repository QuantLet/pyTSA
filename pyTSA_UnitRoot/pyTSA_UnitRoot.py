import numpy as np
import pandas as pd
from statsmodels.tsa.arima_process import arma_generate_sample
import matplotlib.pyplot as plt
#from PythonTsa.plot_acf_pacf import acf_pacf_fig
p = [-0.2, 0.0, 0.0, -0.6, -0.2, 1]
roots = np.roots(p)
abs(roots)
ar = np.array([1, -0.2, -0.6, 0.0, 0.0, -0.2])
np.random.seed(12347)
x =  arma_generate_sample(ar = ar, ma = [1], nsample = 500)
x = pd.Series(x)
x.plot() 
plt.savefig('pyTSA_UnitRoot_fig9-22.png', dpi = 1200, bbox_inches ='tight', 
            transparent = True, legend = None); plt.show() 