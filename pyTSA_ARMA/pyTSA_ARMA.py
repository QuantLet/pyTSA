import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima_process import arma_generate_sample
from PythonTsa.plot_acf_pacf import acf_pacf_fig
ar = np.array([1, -0.8, 0.6])
ma = np.array([1, 0.7, 0.4])
np.random.seed(123457)
x =  arma_generate_sample(ar = ar, ma = ma, nsample = 500)
x = pd.Series(x)
x.plot(); plt.savefig('pyTSA_ARMA_fig3-19.png', dpi = 1200, 
                      bbox_inches ='tight', transparent = True); plt.show()
acf_pacf_fig(x, both = True, lag = 50); 
plt.savefig('pyTSA_ARMA_fig3-20.png', dpi = 1200, 
                      bbox_inches ='tight', transparent = True)