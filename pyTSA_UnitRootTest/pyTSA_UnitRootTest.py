import numpy as np
import pandas as pd
import statsmodels.api as sm
from PythonTsa.plot_acf_pacf import acf_pacf_fig
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import adfuller, kpss
usrgdp = pd.read_csv('us-q-rgdp.csv', header = 0)
usrgdp.index = usrgdp['DATE']
usrgdp = usrgdp.GDPC1
lusrgdp = np.log(usrgdp)
lusrgdp.name = 'lrgdp'
adfuller(lusrgdp, regression = 'ct')
kpss(lusrgdp, regression = 'ct', nlags = 'auto')
t = pd.Series(range(len(lusrgdp)), dtype = 'float64')
t.index = lusrgdp.index
t.name = 'trend'
ct = sm.add_constant(t, prepend = False)
modfit = sm.OLS(lusrgdp, ct).fit()
print(modfit.summary())
myfitted = modfit.fittedvalues
dnf = pd.DataFrame({'Log US real GDP':lusrgdp, 'Trend':myfitted})
dnf.plot(style = ['-', ':'])
plt.xticks(rotation = 15)
plt.savefig('pyTSA_UnitRootTest_fig9-23.png', dpi = 1200, bbox_inches ='tight', 
            transparent = True, legend = None); plt.show()
myresid = modfit.resid
myresid.plot()
plt.xticks(rotation = 15)
plt.savefig('pyTSA_UnitRootTest_fig9-24.png', dpi = 1200, bbox_inches ='tight', 
            transparent = True, legend = None); plt.show()
adfuller(myresid, regression = 'c')
kpss(myresid, regression = 'c', nlags = 'auto')
dlusrgdp = lusrgdp.diff().dropna()
dlusrgdp.plot()
plt.xticks(rotation = 15)
plt.savefig('pyTSA_UnitRootTest_fig9-25.png', dpi = 1200, bbox_inches ='tight', 
            transparent = True, legend = None); plt.show()
acf_pacf_fig(dlusrgdp, both = False, lag = 36)
plt.savefig('pyTSA_UnitRootTest_fig9-26.png', dpi = 1200, bbox_inches ='tight', 
            transparent = True, legend = None); plt.show()
adfuller(dlusrgdp, regression = 'c')
kpss(dlusrgdp, regression = 'c', nlags = 'auto')
