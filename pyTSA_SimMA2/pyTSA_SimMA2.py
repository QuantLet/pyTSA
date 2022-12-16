import numpy as np
import pandas as pd
from statsmodels.tsa.arima_process import arma_generate_sample
import matplotlib.pyplot as plt
from PythonTsa.plot_acf_pacf import acf_pacf_fig
from pandas.plotting import lag_plot
ma = np.array([1, 0.6, -0.3])
np.random.seed(123457)
x = arma_generate_sample(ar = [1], ma = ma, nsample = 500)# ar = [1] means no ar part in the model
type(x) # x is not a series
x = pd.Series(x)
type(x)# now x is a series
x.plot()
plt.savefig('pyTSA_SimMA2_fig3-10.png', dpi = 1200, 
             bbox_inches ='tight', transparent = True, legend = None); plt.show()
acf_pacf_fig(x, both = True, lag = 20)
plt.savefig('pyTSA_SimMA2_fig3-11.png', dpi = 1200, 
             bbox_inches ='tight', transparent = True, legend = None); plt.show()
fig1 = plt.figure()
lag_plot(x, lag = 1, ax = fig1.add_subplot(211))
lag_plot(x, lag = 2, ax = fig1.add_subplot(212))
plt.savefig('pyTSA_SimMA2_fig3-12.png', dpi = 1200, 
             bbox_inches ='tight', transparent = True, legend = None); plt.show()
fig2 = plt.figure()
lag_plot(x, lag = 3, ax = fig2.add_subplot(211))
lag_plot(x, lag = 4, ax = fig2.add_subplot(212))
plt.savefig('pyTSA_SimMA2_fig3-13.png', dpi = 1200, 
             bbox_inches ='tight', transparent = True, legend = None); plt.show()