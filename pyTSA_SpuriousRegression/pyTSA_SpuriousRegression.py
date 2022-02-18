import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.arima_process import arma_generate_sample
import statsmodels.formula.api as smf
from PythonTsa.plot_acf_pacf import acf_pacf_fig
ar = np.array([1, -1.0])
np.random.seed(1373)
x =  arma_generate_sample(ar = ar, ma = [1], nsample = 300)
y =  arma_generate_sample(ar = ar, ma = [1], nsample = 300)
x = pd.Series(x); y = pd.Series(y)
xy = pd.DataFrame({'x': x, 'y': y})
xy.plot(style = ['-', ':'])
plt.savefig('pyTSA_SpuriousRegression_fig9-27.png', dpi = 1200, bbox_inches ='tight', 
            transparent = True, legend = None); plt.show()
regresults  =  smf.ols('y ~ x', data = xy).fit()
print(regresults.summary())
resid = regresults.resid
resid.plot()
plt.savefig('pyTSA_SpuriousRegression_fig9-28.png', dpi = 1200, bbox_inches ='tight', 
            transparent = True, legend = None); plt.show()
acf_pacf_fig(resid, both = False, lag = 25)
plt.savefig('pyTSA_SpuriousRegression_fig9-29.png', dpi = 1200, bbox_inches ='tight', 
            transparent = True, legend = None); plt.show()
adfuller(resid, regression = 'ctt')
dxy = xy.diff(1).dropna()
dxy.columns = ['dx', 'dy']
dregresults  =  smf.ols('dy ~ dx', data = dxy).fit()
print(dregresults.summary())